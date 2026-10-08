"""Standardised progress messages: what step is running and what it produced.

Every message the agent relays to the user is rendered here from fixed templates over workspace
state, so the same state always gives the same text, byte for byte. Renderers never read a clock,
a random source or the message sequence number.

    progress.jsonl    every emitted message, appended
    candidates.jsonl  candidate batches surfaced by neighbors, sample --purpose and resolve
    screening.jsonl   screening decisions recorded by psb screen (the latest per PMID counts)

None of these files is part of ``validation.input_snapshot``: they never affect evaluation,
critic binding or delivery verification.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path

from . import syntax
from .strategy import lint
from .workspace import Workspace, WorkspaceError, normalize_pmids, read_json

TOTAL_STEPS = 7
STEPS = {1: "Intake", 2: "Scope", 3: "Known records", 4: "Vocabulary", 5: "Test & revise", 6: "Critic", 7: "Deliver"}
STAGES = {"intake": 1, "scope": 2, "known-records": 3, "vocabulary": 4, "test": 5, "critic": 6, "deliver": 7}
ROLE_ORDER = ("seed", "relevant", "validation", "benchmark")
ROLE_USE = {
    "seed": "user-supplied; used for development and term mining",
    "relevant": "screened in during the build; used for development and term mining",
    "validation": "held out from term mining; semi-independent check",
    "benchmark": "a prior review's included studies; external benchmark, not mined",
}
DEVELOPMENT_ROLES = {"seed", "relevant"}
SCREEN_BUDGET = {"standard": 150, "thorough": 400}
DECISIONS = ("include", "exclude", "uncertain")
PURPOSES = {"prior-reviews": "Prior-review search", "pilot": "Pilot search", "noise-check": "Noise check"}
CANDIDATE_PURPOSES = {"prior-reviews", "pilot"}
LINK_TITLES = {"similar": "Similar articles", "refs": "Citation search, backward", "citedin": "Citation search, forward"}
LINK_SHORT = {"similar": "similar articles", "refs": "backward citations", "citedin": "forward citations"}
LINK_DETAIL = {"similar": "similar articles", "refs": "reference lists (backward)", "citedin": "citing records (forward)"}
MESH_FIELDS = {"mh", "majr", "nm", "sh"}
TEXT_FIELDS = {"tiab", "ti", "ab", "tw", "ot"}
REPORT_PURPOSES = {"report", "diagnostic", "publication-failed"}
FILES = "final-query.txt · audit.md · validation-manifest.json"
PRESS = "This is a draft. It needs PRESS peer review by an information specialist before use."
UNLOGGED = "Not from a logged psb search"
NOT_MEASURED = "not measured (evaluation did not complete)"
ROLE_LABELS = {"search": "Searched", "screen": "Screened", "optional": "Optional"}
SCOPE_MEANING = [
    "What this means:",
    "- **Searched**: a block of the PubMed search. A record is found only if it matches every searched concept, "
    "so each one narrows the results and can miss relevant studies that describe it differently.",
    "- **Screened**: not in the search. It is judged when titles, abstracts and full texts are screened against "
    "the eligibility criteria, so studies that report it unevenly are not lost.",
    "- **Optional**: not in the main search. It may be tested as an extra block during the build to see what it "
    "would add or lose.",
]
SCOPE_DECISION = [
    "Your decision: reply **keep** to use this scope as it is, or tell me what to change:",
    "- move a concept to another role (for example, screen it instead of searching it)",
    "- add, remove or reword a concept",
    "- add, change or remove a limit or an eligibility criterion",
]


class ProgressError(ValueError):
    pass


# -- formatting -------------------------------------------------------------------------------

def _n(value) -> str:
    return "n/a" if value is None else f"{value:,}"


def _pct(value) -> str:
    return "n/a" if value is None else f"{value:.1f}%"


def clean(text, limit: int) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _cell(text, limit: int) -> str:
    return clean(text, limit).replace("|", "\\|")


def _ticks(text: str) -> int:
    return max((len(m) for m in re.findall(r"`+", text)), default=0)


def code(text: str) -> str:
    fence = "`" * (_ticks(text) + 1)
    pad = " " if text.startswith("`") or text.endswith("`") else ""
    return f"{fence}{pad}{text}{pad}{fence}"


def _fence(text: str) -> list[str]:
    fence = "`" * max(3, _ticks(text) + 1)
    return [fence + "text", text, fence]


def _list(value) -> list:
    return value if isinstance(value, list) else []


def _int_key(pmid: str):
    return (0, int(pmid)) if str(pmid).isdigit() else (1, str(pmid))


def _pmids(values, cap: int = 10) -> str:
    items = sorted({str(v) for v in values or []}, key=_int_key)
    if not items:
        return "none"
    shown = ", ".join(items[:cap])
    return shown + (f" and {len(items) - cap} more" if len(items) > cap else "")


def _plural(count: int, word: str, plural: str | None = None) -> str:
    return f"{_n(count)} {word if count == 1 else plural or word + 's'}"


def _set_order(sets: dict) -> list[str]:
    def key(name):
        role = str((sets[name] or {}).get("role"))
        return (ROLE_ORDER.index(role) if role in ROLE_ORDER else len(ROLE_ORDER), name)
    return sorted(sets, key=key)


def _recall(evaluation: dict) -> str:
    sets = evaluation.get("sets") or {}
    if not sets:
        return "not measured (no known-record sets)"
    parts = []
    for name in _set_order(sets):
        data = sets[name]
        parts.append(f"{name} {_n(data.get('retrieved'))}/{_n(data.get('in_pubmed'))} ({_pct(data.get('recall_percent'))})")
    return " · ".join(parts)


def _misses(evaluation: dict, cap: int = 10) -> str:
    misses = sorted(evaluation.get("misses") or [], key=lambda m: _int_key(m["pmid"]))
    if not misses:
        return "none"
    rows = []
    for m in misses[:cap]:
        failing = ", ".join(m.get("failing_blocks") or []) or ("limits" if m.get("lost_to_limits") else "none")
        rows.append(f"{m['pmid']} ({', '.join(sorted(m.get('sets') or []))}; fails {failing})")
    more = f" and {len(misses) - cap} more" if len(misses) > cap else ""
    return f"{len(misses)}: " + "; ".join(rows) + more


def _checks(evaluation: dict) -> str:
    validation = evaluation.get("validation") or {}
    blockers = validation.get("blockers") or []
    codes = sorted({b.get("code") for b in blockers})
    lint_rows = evaluation.get("lint") or []
    errors = sum(1 for i in lint_rows if i.get("severity") == "error")
    warnings = sum(1 for i in lint_rows if i.get("severity") == "warning")
    text = f"{_plural(len(blockers), 'blocker')}"
    if codes:
        text += f" ({', '.join(codes)})"
    return (text + f" · {_n(len(validation.get('review_required') or []))} need critic review"
            + f" · lint {_plural(errors, 'error')}, {_plural(warnings, 'warning')}")


def _limit_text(limit) -> str:
    if isinstance(limit, dict):
        name = next((limit[k] for k in ("limit", "clause", "name", "text") if limit.get(k)), "")
        reason = next((limit[k] for k in ("reason", "rationale") if limit.get(k)), "")
        return clean(name, 120) + (f" ({clean(reason, 120)})" if reason else " (no reason recorded)")
    return clean(limit, 160)


def _next(stage: str, depth: str | None) -> str:
    depth = depth or "standard"
    from .deliver import revision_budget
    text = {
        "intake": "Step 2/7 Scope: split the question into concepts and decide which are searched, screened or optional.",
        "scope": ("Step 3/7 Known records: add any seed articles (no discovery at quick depth)." if depth == "quick" else
                  f"Step 3/7 Known records: add seeds, look for prior reviews, run pilot and citation searches, and "
                  f"screen up to ~{SCREEN_BUDGET.get(depth, 150)} candidates ({depth})."),
        "known-records": "Step 4/7 Vocabulary: build MeSH and [tiab] terms for each searched concept.",
        "vocabulary": "Step 5/7 Test & revise: evaluate counts and recall, and fix misses one change at a time.",
        "test": (f"Step 6/7 Critic: fresh-context PRESS-structured review, up to {revision_budget(depth)} revision "
                 f"round(s) then a closing round ({depth})."),
        "critic": "Step 7/7 Deliver: live revalidation and the protected final query (psb report).",
    }[stage]
    return "Next: " + text


# -- files ------------------------------------------------------------------------------------

def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                row = json.loads(line)
            except ValueError:
                continue  # a line torn by a concurrent write
            if isinstance(row, dict):
                rows.append(row)
    return rows


def _append(path: Path, entry: dict) -> None:
    # One os.write to an O_APPEND descriptor, as Workspace.log does, so concurrent writers cannot
    # interleave a line.
    line = (json.dumps(entry, ensure_ascii=False) + "\n").encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        os.write(fd, line)
    finally:
        os.close(fd)


def messages(ws: Workspace) -> list[dict]:
    return _read_jsonl(ws.root / "progress.jsonl")


def batches(ws: Workspace) -> list[dict]:
    return _read_jsonl(ws.root / "candidates.jsonl")


def record_batch(ws: Workspace, via: str, label: str, pmids: list[str], *, total: int,
                 origin: list[str] | None = None, query: str | None = None) -> dict:
    entry = {"batch": f"C{len(batches(ws)) + 1}", "via": via, "label": label, "from": list(origin or []),
             "query": query, "total": total, "pmids": list(pmids)}
    _append(ws.root / "candidates.jsonl", entry)
    return entry


def neighbors_label(links: list[str], origin: list[str], sets: list[str]) -> str:
    source = f" ({'set' if len(sets) == 1 else 'sets'} {', '.join(sets)})" if sets else ""
    kinds = " + ".join(LINK_SHORT.get(l, l) for l in links)
    return kinds[:1].upper() + kinds[1:] + f" from {_plural(len(origin), 'record')}{source}"


def decisions(ws: Workspace) -> dict[str, dict]:
    """The latest screening decision for each PMID."""
    latest: dict[str, dict] = {}
    for row in _read_jsonl(ws.root / "screening.jsonl"):
        if row.get("decision") in DECISIONS and str(row.get("pmid", "")).isdigit():
            latest[str(row["pmid"])] = row
    return latest


def attribution(ws: Workspace) -> dict[str, dict]:
    """Each PMID's source: the earliest candidate batch that showed it."""
    found: dict[str, dict] = {}
    for batch in batches(ws):
        for pmid in batch.get("pmids") or []:
            found.setdefault(str(pmid), batch)
    return found


def record_screening(ws: Workspace, *, include=(), exclude=(), uncertain=(), reason: str = "",
                     file: str | None = None) -> list[dict]:
    rows: list[tuple[str, str, str]] = []
    for decision, values in (("include", include), ("exclude", exclude), ("uncertain", uncertain)):
        rows += [(p, decision, reason.strip()) for p in normalize_pmids(values or [])]
    if file:
        data = read_json(Path(file))
        if not isinstance(data, list):
            raise ProgressError("the decisions file must be a JSON list of {pmid, decision, reason}")
        for item in data:
            if not isinstance(item, dict) or item.get("decision") not in DECISIONS:
                raise ProgressError(f"each decision needs a decision of {', '.join(DECISIONS)}: {item!r}")
            rows += [(p, item["decision"], str(item.get("reason") or reason).strip())
                     for p in normalize_pmids([item.get("pmid", "")])]
    if not rows:
        raise ProgressError("give at least one PMID with --include, --exclude, --uncertain or --file")
    seen: dict[str, str] = {}
    for pmid, decision, _ in rows:
        if seen.setdefault(pmid, decision) != decision:
            raise ProgressError(f"PMID {pmid} has two decisions ({seen[pmid]} and {decision}) in one call")
    unique = list({pmid: (pmid, decision, why) for pmid, decision, why in rows}.values())
    before = decisions(ws)
    entries = []
    for pmid, decision, why in unique:
        entry = {"pmid": pmid, "decision": decision, "reason": why,
                 "previous": before[pmid]["decision"] if pmid in before else None}
        _append(ws.root / "screening.jsonl", entry)
        entries.append(entry)
    return entries


# -- emitting ---------------------------------------------------------------------------------

EVENTS: dict[str, tuple[int, object]] = {}


def event(name: str, step: int):
    def register(render):
        EVENTS[name] = (step, render)
        return render
    return register


def render(ws: Workspace | None, name: str, data: dict | None = None) -> dict:
    if name not in EVENTS:
        raise ProgressError(f"unknown progress event {name!r}")
    step, renderer = EVENTS[name]
    title, lines = renderer(ws, data or {})
    text = "\n".join([f"**PSB · Step {step}/{TOTAL_STEPS} {STEPS[step]} · {title}**", *lines])
    return {"event": name, "step": step, "text": text}


def emit(ws: Workspace, name: str, data: dict | None = None) -> dict:
    message = render(ws, name, data)
    seq = len(messages(ws)) + 1
    _append(ws.root / "progress.jsonl", {**message, "seq": seq,
                                          "sha256": hashlib.sha256(message["text"].encode("utf-8")).hexdigest()})
    return {**message, "seq": seq}


def fallback(name: str, exc: BaseException) -> dict:
    step = EVENTS[name][0] if name in EVENTS else 0
    label = f"Step {step}/{TOTAL_STEPS} {STEPS[step]}" if step else "Progress"
    text = (f"**PSB · {label} · {name}**\nProgress message unavailable ({type(exc).__name__}); "
            "the command itself ran: see its JSON result.")
    return {"event": name, "step": step, "text": text, "error": f"{type(exc).__name__}: {exc}"}


def attach(body: dict, ws: Workspace, name: str, data=None) -> dict:
    """Add the message for a command that has already done its work.

    ``data`` is a dict, or a function returning one (so preparing the message, including any
    candidate batch it records, is guarded too). A message never changes what the command did,
    its ``ok`` or its exit code: on any failure the command carries a fixed fallback message.
    """
    try:
        body["progress"] = emit(ws, name, data() if callable(data) else data)
    except Exception as exc:  # noqa: BLE001 - the command's own result must stand
        message = fallback(name, exc)
        try:
            _append(ws.root / "progress.jsonl", {**message, "seq": len(messages(ws)) + 1})
        except Exception:  # noqa: BLE001
            pass
        body["progress"] = message
    return body


# -- automatic messages -----------------------------------------------------------------------

@event("resolve", 3)
def _resolve(ws, data):
    resolved = data.get("resolved") or {}
    lines = [f"Resolved {_n(len(resolved))} of {_plural(data.get('given', 0), 'identifier')} to PMIDs",
             f"- PMIDs: {_pmids(resolved.values())}",
             f"- Not in PubMed or added after the as-of date: {_pmids(data.get('not_in_pubmed_or_after_as_of'))}"]
    unresolved = sorted(clean(i, 60) for i in data.get("unresolved") or [])
    lines.append(f"- Unresolved: {', '.join(unresolved[:10]) + (f' and {len(unresolved) - 10} more' if len(unresolved) > 10 else '') if unresolved else 'none'}")
    if data.get("batch"):
        lines.append(f"- Recorded as candidate batch {data['batch']}")
    return "Identifiers resolved", lines


def _search_event(purpose: str):
    def renderer(ws, data):
        lines = [f"{PURPOSES[purpose]}: {_n(data.get('count'))} records for {code(clean(data.get('query'), 200))}"]
        shown = data.get("shown")
        if shown is None:
            lines.append("- Count only; no records shown")
        elif purpose == "noise-check":
            lines.append(f"- Sampled {_plural(shown, 'record')} from offset {_n(data.get('retstart', 0))} to inspect noise")
        elif purpose == "prior-reviews":
            lines.append(f"- Shown: {_plural(shown, 'review')} to check against the scope (batch {data['batch']})"
                         if shown and data.get("batch") else "- No reviews to check")
        else:
            lines.append(f"- Shown for screening: {_plural(shown, 'record')} as candidate batch {data['batch']}"
                         if shown and data.get("batch") else "- No records to screen")
        return PURPOSES[purpose], lines
    return renderer


for _purpose, _step in (("prior-reviews", 3), ("pilot", 3), ("noise-check", 5)):
    event(f"search:{_purpose}", _step)(_search_event(_purpose))


@event("neighbors", 3)
def _neighbors(ws, data):
    links = data.get("links") or []
    origin = data.get("from") or []
    sets = data.get("sets") or []
    source = f" ({'set ' if len(sets) == 1 else 'sets '}{', '.join(sets)})" if sets else ""
    lines = [f"Found {_plural(data.get('candidates', 0), 'candidate record')} linked to "
             f"{_plural(len(origin), 'known record')}{source}"]
    for link in links:
        lines.append(f"- {LINK_DETAIL.get(link, link).capitalize()}: {_n((data.get('per_link') or {}).get(link, 0))}")
    lines.append(f"- Already in a known-record set: {_n(data.get('known', 0))}"
                 + (" (excluded)" if data.get("exclude_known") else " (still listed)"))
    lines.append(f"- Shown for screening: {_plural(data.get('shown', 0), 'record')}"
                 + (f" as candidate batch {data['batch']}" if data.get("batch") else ""))
    return " + ".join(LINK_TITLES.get(l, l) for l in links), lines


def _budget_line(ws: Workspace, screened: int) -> str:
    depth = ws.protocol().get("depth") or "standard"
    if depth in SCREEN_BUDGET:
        return f"- Screening budget used: {_n(screened)} of ~{_n(SCREEN_BUDGET[depth])} ({depth})"
    return f"- Screened so far: {_n(screened)} (no discovery budget at {depth} depth)"


def _included_unset(ws: Workspace) -> list[str]:
    in_sets = {p for data in ws.sets().values() for p in data.get("pmids", [])}
    return [p for p, row in decisions(ws).items() if row["decision"] == "include" and p not in in_sets]


def _by_source(ws: Workspace, rows: list[dict]) -> list[str]:
    source = attribution(ws)
    groups: dict[str, dict] = {}
    for row in rows:
        batch = source.get(row["pmid"])
        key = batch["batch"] if batch else ""
        group = groups.setdefault(key, {"label": batch["label"] if batch else UNLOGGED, "screened": 0, "include": 0})
        group["screened"] += 1
        group["include"] += row["decision"] == "include"
    order = sorted(groups, key=lambda k: (k == "", int(k[1:]) if k else 0))
    return [f"- {groups[k]['label']}{f' ({k})' if k else ''}: {_n(groups[k]['screened'])} screened → "
            f"{_n(groups[k]['include'])} include" for k in order]


def _tally(rows) -> str:
    counts = {d: sum(1 for r in rows if r["decision"] == d) for d in DECISIONS}
    return " · ".join(f"{_n(counts[d])} {d}" for d in DECISIONS)


@event("screen", 3)
def _screen(ws, data):
    rows = data.get("entries") or []
    lines = [f"Screened {_plural(len(rows), 'candidate')}: {_tally(rows)}", *_by_source(ws, rows)]
    changed = [r for r in rows if r.get("previous") and r["previous"] != r["decision"]]
    if changed:
        lines.append(f"- Decisions changed from an earlier screen: {_pmids(r['pmid'] for r in changed)}")
    lines.append(_budget_line(ws, len(decisions(ws))))
    lines.append(f"- Included but not yet in a set: {_pmids(_included_unset(ws))}")
    return "Screening", lines


@event("set", 3)
def _set(ws, data):
    role = data.get("role")
    lines = [f"Set {data.get('name')} ({role}): {_n(data.get('before', 0))} → {_plural(data.get('after', 0), 'record')}",
             f"- Use: {ROLE_USE.get(role, 'unknown role')}"]
    if data.get("added"):
        lines.append(f"- Added: {_pmids(data['added'])}")
    if data.get("removed"):
        lines.append(f"- Removed: {_pmids(data['removed'])}")
    for other, pmids in sorted((data.get("overlap") or {}).items()):
        lines.append(f"- Also in {other}, which has another role: {_pmids(pmids)}")
    return "Set updated", lines


@event("split", 3)
def _split(ws, data):
    total = data.get("development", 0) + data.get("validation", 0)
    return "Hold-out", [
        f"Held out {_n(data.get('validation', 0))} of {_plural(total, 'record')} from {data.get('name')} as "
        f"{data.get('into')} (role validation)",
        f"- {data.get('name')}: {_plural(data.get('development', 0), 'record')} remain for development and term mining",
        f"- {data.get('into')}: not mined; semi-independent check, consulted at every eval",
    ]


@event("terms-rank", 4)
def _terms_rank(ws, data):
    sets = data.get("sets")
    held = sorted(data.get("held_out_mined") or [])
    scope = ("sets " + ", ".join(sets)) if sets else "all seed and relevant sets"
    scope += (f"; includes held-out {', '.join(held)}, which now count as development" if held
              else "; held-out sets excluded")
    return "Term mining", [
        f"Mined candidate terms from {_plural(data.get('records', 0), 'record')} ({scope})",
        f"- Candidate terms: {_n(data.get('candidates', 0))} · already in the strategy: {_n(data.get('already_covered', 0))}"
        f" · scored: {_n(data.get('scored', 0))}",
        "- Candidates, not additions: each is tested with psb eval before it is kept",
    ]


def _eval_lines(evaluation: dict, note: str) -> list[str]:
    version = evaluation.get("version")
    since = evaluation.get("since_previous") or {}
    head = f"v{version}: {_n(evaluation.get('count'))} records" if evaluation.get("count") is not None else f"v{version}: not measured"
    if since.get("count_before") is not None and evaluation.get("count") is not None:
        head += f" ({since['count_change']:+,} vs v{since.get('from_version')})" if since.get("from_version") else f" ({since['count_change']:+,} vs last eval)"
    if evaluation.get("saved"):
        head += " · same strategy, re-evaluated"
    lines = [head]
    if note.strip():
        lines.append(f"- Change: {clean(note, 160)}")
    measured = evaluation.get("count") is not None
    if measured:
        lines += [f"- Recall: {_recall(evaluation)}", f"- Missed known records: {_misses(evaluation)}"]
    else:
        lines.append(f"- Recall: {NOT_MEASURED}")
    if since:
        if measured:
            lines.append(f"- Since the last eval: lost {_pmids(since.get('known_lost'))} · gained {_pmids(since.get('known_gained'))}")
        changes = []
        for block, change in (since.get("changes") or {}).items():
            if block == "_combine":
                changes.append("combination changed")
            elif block == "_limits":
                changes.append("limits changed")
            elif change.get("block") == "added":
                changes.append(f"{block} added")
            elif change.get("block") == "removed":
                changes.append(f"{block} removed")
            else:
                changes.append(f"{block} +{len(change.get('terms_added', []))}/-{len(change.get('terms_removed', []))} terms")
        lines.append(f"- Strategy changes: {'; '.join(changes) or 'none'}")
    lines.append(f"- Checks: {_checks(evaluation)}")
    return lines


@event("eval", 5)
def _eval(ws, data):
    evaluation = data.get("evaluation") or {}
    return f"Evaluation v{evaluation.get('version')}", _eval_lines(evaluation, data.get("note") or "")


@event("terms-miss", 5)
def _terms_miss(ws, data):
    misses = data.get("misses") or []
    by_set: dict[str, int] = {}
    for m in misses:
        for name in m.get("sets") or []:
            by_set[name] = by_set.get(name, 0) + 1
    lines = [f"Diagnosed {_plural(len(misses), 'missed known record')} from v{data.get('version')}",
             f"- Missed: {_pmids(m['pmid'] for m in misses)}",
             f"- By set: {', '.join(f'{k} {v}' for k, v in sorted(by_set.items())) or 'none'}",
             "- Each miss is fixed in its failing block or recorded as out of reach"]
    return "Miss diagnosis", lines


@event("critic-packet", 6)
def _critic_packet(ws, data):
    from .deliver import latest_evaluation, next_round, revision_budget
    rounds = _list(data.get("rounds_before"))
    evaluation = latest_evaluation(ws)
    number, kind = next_round(ws, evaluation, rounds)
    revision = sum(bool(r.get("review_sha256")) and not r.get("closing") for r in rounds if isinstance(r, dict)) + 1
    label = f"revision {revision} of {revision_budget(ws.protocol().get('depth'))}" if kind == "revision" else kind
    return f"Round {number} packet", [
        f"Round {number} ({label}) packet written for v{evaluation.get('version')}",
        f"- Packet: critic/{data.get('packet')}",
        f"- A fresh-context reviewer reads only this packet; its reply is saved as critic/round-{number}.json",
    ]


def _finding_counts(findings: list[dict]) -> tuple[str, str]:
    severity = " · ".join(f"{_n(sum(1 for f in findings if f.get('severity') == s))} {s}" for s in ("must-fix", "should-fix", "document"))
    status = " · ".join(f"{_n(sum(1 for f in findings if f.get('status') == s))} {s}" for s in ("open", "resolved", "rejected", "accepted-risk"))
    return severity, status


def _problems_line(problems: list) -> str:
    shown = "; ".join(clean(p, 100) for p in problems[:3])
    return (f"{_plural(len(problems), 'problem')}" + (f": {shown}" if shown else "")
            + (f" and {len(problems) - 3} more" if len(problems) > 3 else ""))


@event("critic-check", 6)
def _critic_check(ws, data):
    from .deliver import DOMAINS, critic_rounds
    round_data = data.get("round") if isinstance(data.get("round"), dict) else {}
    number = round_data.get("round")
    earlier = [r for r in critic_rounds(ws) if isinstance(r.get("round"), int) and r["round"] < number]
    kind = round_kinds([*earlier, round_data])[-1]
    domains = round_data.get("domains") if isinstance(round_data.get("domains"), dict) else {}
    verdicts = {d: domains[d].get("verdict") if isinstance(domains.get(d), dict) else None for d in DOMAINS}
    revise = [d for d in DOMAINS if verdicts[d] == "revise"]
    findings = sorted((f for f in _list(round_data.get("findings")) if isinstance(f, dict)), key=lambda f: str(f.get("id")))
    severity, status = _finding_counts(findings)
    check = data.get("check") if isinstance(data.get("check"), dict) else {}
    lines = [f"Round {number} ({kind}): {sum(v == 'pass' for v in verdicts.values())} domains pass · {len(revise)} revise",
             f"- Revise: {', '.join(revise) or 'none'}",
             f"- Findings: {severity}",
             f"- Status: {status}",
             f"- Open must-fix: {', '.join(sorted(map(str, _list(check.get('open_must_fix'))))) or 'none'}"]
    lines.append("- Check: passes" if check.get("ok") else f"- Check: {_problems_line(_list(check.get('problems')))}")
    if _list(check.get("overridable")):
        lines.append(f"- Overridable after the closing round: {', '.join(sorted(map(str, check['overridable'])))}")
    return f"Round {number} result", lines


@event("critic-invalid", 6)
def _critic_invalid(ws, data):
    return "Round file invalid", [f"{data.get('file')} was not checked: {_problems_line(_list(data.get('problems')))}",
                                  "- Fix the round file and run psb critic check again"]


@event("critic-override", 6)
def _critic_override(ws, data):
    from .deliver import critic_rounds
    finding: dict = {}
    for r in critic_rounds(ws):  # the latest round's copy of the finding
        for f in _list(r.get("findings")):
            if isinstance(f, dict) and f.get("id") == data.get("id"):
                finding = f
    return "Override", [f"Overrode {data.get('id')} ({finding.get('severity')}, {finding.get('kind')}) after the closing round",
                        "- The audit opens with the critic's objection and the reason, for the peer reviewer"]


def _blocker_codes(blockers: list[dict]) -> str:
    counts: dict[str, int] = {}
    for b in blockers:
        counts[str(b.get("code"))] = counts.get(str(b.get("code")), 0) + 1
    return ", ".join(f"{code} ({n})" if n > 1 else code for code, n in sorted(counts.items())) or "none"


def _attempt(ws: Workspace, attempt_id: str | None) -> dict:
    try:
        return read_json(ws.root / "attempts" / f"{attempt_id}.json").get("evaluation") or {}
    except (WorkspaceError, AttributeError):
        return {}


def _critic_line(ws: Workspace, overridden: list[str]) -> str:
    from .deliver import critic_rounds
    rounds = critic_rounds(ws)
    return (f"- Critic: {_plural(len(rounds), 'round')} (internal PRESS-structured critique, not PRESS peer review); "
            f"overridden findings: {', '.join(sorted(overridden)) or 'none'}")


@event("report", 7)
def _report(ws, data):
    result = data.get("result") or {}
    if result.get("ok"):
        evaluation = _attempt(ws, result.get("attempt_id"))
        manifest = read_json(ws.root / "validation-manifest.json")
        return "Report", [f"Delivered: final query validated live, {_n(evaluation.get('count'))} records",
                          f"- Recall: {_recall(evaluation)}",
                          _critic_line(ws, manifest.get("overridden_findings") or []),
                          f"- Files: {FILES}",
                          f"- {PRESS}"]
    blockers = result.get("blockers") or []
    diagnostic = Path(result["diagnostic"]).name if result.get("diagnostic") else None
    if data.get("diagnostic") and not blockers:
        head, title = "Diagnostic only: no blockers found; psb report would deliver", "Diagnostic check"
    else:
        head = f"Not delivered: {_plural(len(blockers), 'blocker')}"
        title = "Diagnostic check" if data.get("diagnostic") else "Report blocked"
    lines = [head, f"- Blockers: {_blocker_codes(blockers)}"]
    if diagnostic:
        lines.append(f"- Diagnostic output: {diagnostic} (unfinished; not a final query)")
    return title, lines


# -- stage summaries --------------------------------------------------------------------------

@event("intake-request", 1)
def _intake_request(ws, data):
    asks = [] if data.get("have_question") else ["The review question in plain language"]
    asks += ["Known relevant articles (PMIDs, DOIs or PMCIDs), if you have any (optional)",
             "Depth: quick, standard (default) or thorough",
             "Required limits, such as dates or languages, if any"]
    return "Request", ["To build the search I need:", *[f"{i}. {a}" for i, a in enumerate(asks, 1)],
                       'Reply "proceed" to use the defaults for anything you leave out.']


@event("stage:intake", 1)
def _stage_intake(ws, data):
    protocol = ws.protocol()
    if not str(protocol.get("question") or "").strip():
        raise ProgressError("protocol.json has no question; record it first")
    seeds = {p for d in ws.sets().values() if d.get("role") == "seed" for p in d.get("pmids", [])}
    limits = protocol.get("limits") or []
    return "Summary", [
        f"Question: {clean(protocol.get('question'), 300)}",
        f"- Depth: {protocol.get('depth') or 'standard'}",
        f"- Required limits: {'; '.join(_limit_text(l) for l in limits) if limits else 'none'}",
        f"- Known articles recorded: {_plural(len(seeds), 'seed PMID') if seeds else 'none yet (added in Step 3)'}",
        f"- Assumptions and notes: {clean(protocol.get('notes'), 300) or 'none'}",
        f"- Workspace: {ws.root}",
        _next("intake", protocol.get("depth")),
    ]


def _role_rank(concept: dict) -> int:
    role = concept.get("role")
    return list(ROLE_LABELS).index(role) if isinstance(role, str) and role in ROLE_LABELS else len(ROLE_LABELS)


def _role_label(role) -> str:
    if isinstance(role, str) and role in ROLE_LABELS:
        return ROLE_LABELS[role]
    return f"{_cell(role, 40)} (unrecognised)" if clean(role, 40) else "missing"


@event("stage:scope", 2)
def _stage_scope(ws, data):
    """The scope as a fixed table, then either the confirmation or the fixed keep-or-change question."""
    protocol = ws.protocol()
    concepts = [c for c in protocol.get("concepts") or [] if isinstance(c, dict)]
    if not concepts:
        raise ProgressError("protocol.json has no concepts; record them with roles first")
    lines = [f"Question: {clean(protocol.get('question'), 300) or 'not recorded'}", "",
             "| Concept | Role | Why |", "|---|---|---|"]
    for c in sorted(concepts, key=_role_rank):  # stable: protocol order within each role
        lines.append(f"| {_cell(c.get('name') or c.get('id'), 80)} | {_role_label(c.get('role'))} | "
                     f"{_cell(c.get('rationale'), 140) or 'not recorded'} |")
    roles = [c.get("role") for c in concepts]
    limits = protocol.get("limits") or []
    lines += ["", f"{_n(roles.count('search'))} searched · {_n(roles.count('screen'))} screened · "
                  f"{_n(roles.count('optional'))} optional concepts",
              f"Limits (applied to the search): {'; '.join(_limit_text(l) for l in limits) if limits else 'none'}"]
    eligibility = protocol.get("eligibility") if isinstance(protocol.get("eligibility"), dict) else {}
    criteria = [f"- {label.capitalize()}: {clean(item, 200)}" for label in ("include", "exclude")
                for item in _list(eligibility.get(label)) if clean(item, 200)]
    lines += ["", "Eligibility criteria (applied at screening):" + ("" if criteria else " none recorded"), *criteria]
    if protocol.get("scope_confirmed"):
        lines += ["", "Scope confirmed by the user.", _next("scope", protocol.get("depth"))]
    else:
        lines += ["", *SCOPE_MEANING, "", *SCOPE_DECISION]
    return "Summary", lines


def _kind(batch: dict) -> str:
    via = str(batch.get("via"))
    if via.startswith("neighbors:"):
        return "neighbour search"
    return {"prior-reviews": "prior-review search", "pilot": "pilot search", "resolve": "identifier resolution"}.get(via, via)


@event("stage:known-records", 3)
def _stage_known(ws, data):
    protocol = ws.protocol()
    sets = ws.sets()
    held = {p for d in sets.values() if d.get("role") not in DEVELOPMENT_ROLES for p in d.get("pmids", [])}
    development = {p for d in sets.values() if d.get("role") in DEVELOPMENT_ROLES for p in d.get("pmids", [])} - held
    lines = [f"Known relevant records: {_n(len(development))} for development · {_n(len(held))} held out "
             "(validation and benchmark)"]
    for name in _set_order(sets):
        role = sets[name].get("role")
        lines.append(f"- {name} ({role}): {_plural(len(sets[name].get('pmids', [])), 'record')} — {ROLE_USE.get(role, 'unknown role')}")
    if not sets:
        lines.append("- No known records: recall will not be estimated; the strategy is empirically unvalidated.")
    validation_sets = [n for n in _set_order(sets) if sets[n].get("role") == "validation"]
    lines.append("- Held-out validation set: " + (", ".join(
        f"{n} ({_plural(len(sets[n].get('pmids', [])), 'record')})" for n in validation_sets)
        if validation_sets else f"none (development records: {_n(len(development))})"))
    kinds: dict[str, int] = {}
    for batch in batches(ws):
        kinds[_kind(batch)] = kinds.get(_kind(batch), 0) + 1
    lines.append(f"- Candidate searches: {_n(sum(kinds.values()))}"
                 + (f" ({', '.join(f'{v} {k}' for k, v in sorted(kinds.items()))})" if kinds else ""))
    screened = list(decisions(ws).values())
    if screened:
        lines.append(f"- Screening: {_n(len(screened))} screened → {_tally(screened)}")
    else:
        lines.append("- Screening: none recorded")
    lines.append(_budget_line(ws, len(screened)))
    lines.append(f"- Included but not in a set: {_pmids(_included_unset(ws))}")
    included = {p for p, row in decisions(ws).items() if row["decision"] == "include"}
    unscreened = {p for d in sets.values() if d.get("role") in {"relevant", "benchmark"} for p in d.get("pmids", [])} - included
    if unscreened:
        lines.append(f"- In a relevant or benchmark set with no include decision: {_pmids(unscreened)}")
    lines.append(_next("known-records", protocol.get("depth")))
    return "Summary", lines


def _command(argv: list) -> list[str]:
    words, skip = [], False
    for token in argv or []:
        if skip:
            skip = False
        elif token in {"--workspace", "--env-file"}:
            skip = True
        elif not str(token).startswith("-"):
            words.append(str(token))
    return words


@event("stage:vocabulary", 4)
def _stage_vocabulary(ws, data):
    protocol = ws.protocol()
    strategy = ws.strategy()
    if not strategy.blocks:
        raise ProgressError("strategy.json has no blocks yet")
    lines = [f"{_plural(len(strategy.blocks), 'searched concept block')} · "
             f"{_plural(sum(len(b.terms) for b in strategy.blocks), 'term')}"]
    for block in strategy.blocks:
        mesh = text = other = 0
        for term in block.terms:
            fields = {a["field"] for a in syntax.atoms(term)}
            if fields & MESH_FIELDS:
                mesh += 1
            elif fields & TEXT_FIELDS:
                text += 1
            else:
                other += 1
        lines.append(f"- {clean(block.name or block.id, 80)} ({block.id}): {_plural(len(block.terms), 'term')} — "
                     f"{_n(mesh)} MeSH · {_n(text)} text-word · {_n(other)} other")
    blocked = {b.id for b in strategy.blocks}
    rest = [c for c in protocol.get("concepts") or [] if isinstance(c, dict) and c.get("id") not in blocked]
    lines.append("- Concepts not searched: " + (", ".join(f"{clean(c.get('name') or c.get('id'), 60)} ({c.get('role')})"
                                                          for c in rest) or "none"))
    commands = [_command(e.get("argv")) for e in ws.log_entries() if e.get("type") == "command"]
    lookups = sum(1 for c in commands if c[:2] == ["mesh", "lookup"])
    shows = sum(1 for c in commands if c[:2] == ["mesh", "show"])
    mined = sum(1 for c in commands if c[:2] == ["terms", "rank"])
    lines.append(f"- MeSH lookups: {_n(lookups)} · MeSH records inspected: {_n(shows)}")
    lines.append(f"- Term mining from development records: {'run ' + _plural(mined, 'time') if mined else 'not run'}")
    issues = lint(strategy, concepts=protocol.get("concepts") or [])
    lines.append(f"- Lint: {_plural(sum(i['severity'] == 'error' for i in issues), 'error')} · "
                 f"{_plural(sum(i['severity'] == 'warning' for i in issues), 'warning')}")
    lines.append(_next("vocabulary", protocol.get("depth")))
    return "Summary", lines


def _latest_measured(ws: Workspace) -> dict:
    for attempt in reversed(ws.attempts()):
        if (attempt.get("evaluation") or {}).get("count") is not None:
            return attempt["evaluation"]
    versions = ws.versions()
    return versions[-1]["evaluation"] if versions else {}


@event("stage:test", 5)
def _stage_test(ws, data):
    versions = ws.versions()
    if not versions:
        raise ProgressError("no evaluated version yet; run psb eval")
    latest = _latest_measured(ws)
    first = versions[0]["evaluation"].get("count")
    lost = set()
    for entry in versions:
        lost |= set((entry["evaluation"].get("since_previous") or {}).get("known_lost") or [])
    lost = (lost & set(latest.get("known_in_pubmed") or [])) - set(latest.get("retrieved_known") or [])
    note = clean(versions[-1].get("note"), 160)
    lines = [f"{_plural(len(versions), 'version')} evaluated: {_n(first)} → {_n(latest.get('count'))} records",
             f"- Latest: v{versions[-1]['version']}" + (f" — {note}" if note else "")]
    if latest.get("count") is not None:
        lines += [f"- Recall: {_recall(latest)}",
                  f"- Missed known records: {_misses(latest)}",
                  f"- Known records lost along the way and not recovered: {_pmids(lost)}"]
    else:
        lines.append(f"- Recall: {NOT_MEASURED}")
    lines += [f"- Checks: {_checks(latest)}", _next("test", ws.protocol().get("depth"))]
    return "Summary", lines


def round_kinds(rounds: list[dict]) -> list[str]:
    kinds, closings = [], 0
    for r in rounds:
        if r.get("closing"):
            closings += 1
            kinds.append("closing" if closings == 1 else "verification")
        else:
            kinds.append("revision")
    return kinds


@event("stage:critic", 6)
def _stage_critic(ws, data):
    from .deliver import critic_overrides, critic_rounds
    rounds = critic_rounds(ws)
    if not rounds:
        raise ProgressError("no critic round yet; run psb critic packet")
    kinds = round_kinds(rounds)
    lines = [f"{_plural(len(rounds), 'critic round')}: {_n(kinds.count('revision'))} revision · "
             f"{_n(len(kinds) - kinds.count('revision'))} closing"]
    active: dict[str, dict] = {}
    for r, kind in zip(rounds, kinds):
        findings = [f for f in _list(r.get("findings")) if isinstance(f, dict)]
        severity, _ = _finding_counts(findings)
        lines.append(f"- Round {r.get('round')} ({kind}) on v{r.get('strategy_version')}: "
                     f"{_plural(len(findings), 'finding')} — {severity}")
        active.update({str(f.get("id")): f for f in findings})
    _, status = _finding_counts(list(active.values()))
    lines.append(f"- Findings by latest status: {status}")
    overrides = [o.get("id") for o in critic_overrides(ws) if o.get("round") == rounds[-1].get("round")]
    lines.append(f"- Overridden: {', '.join(sorted(map(str, overrides))) or 'none'}")
    current = rounds[-1].get("review_sha256") == _latest_measured(ws).get("review_sha256")
    lines.append(f"- Latest round reviewed the latest evaluation: {'yes' if current else 'no'}")
    lines.append(_next("critic", ws.protocol().get("depth")))
    return "Summary", lines


@event("stage:deliver", 7)
def _stage_deliver(ws, data):
    from .deliver import _line_table, _recall_table, verify_delivery
    delivery = verify_delivery(ws)
    if delivery["ok"]:
        manifest = delivery["manifest"]
        evaluation = _attempt(ws, manifest.get("attempt_id"))
        lines = [f"Delivered: {_n(evaluation.get('count'))} records; every line revalidated live", "",
                 "Search strategy (single line, for PubMed):", *_fence(manifest.get("query") or ""), "",
                 "Line by line:", "", *_line_table(evaluation), "", "Recall against known relevant records:", ""]
        if evaluation.get("sets"):
            lines += _recall_table(evaluation)
            lines += ["", "Relative recall, not sensitivity: development sets were used to build the strategy."]
        else:
            lines.append("Recall was not estimated; the strategy is empirically unvalidated.")
        lines += ["", _critic_line(ws, manifest.get("overridden_findings") or []), f"- Files: {FILES}", f"- {PRESS}"]
        return "Final search", lines
    reports = [a for a in ws.attempts() if a.get("purpose") in REPORT_PURPOSES]
    if not reports:
        raise ProgressError("psb report has not run yet")
    blockers = (reports[-1].get("evaluation") or {}).get("delivery_blockers") or []
    lines = ["No current delivery: no protected final query was issued",
             f"- Delivery check: {clean(delivery.get('error'), 200)}",
             f"- Blockers at the last report: {_blocker_codes(blockers)}"]
    if (ws.root / "diagnostic-audit.md").exists():
        lines.append("- Diagnostic output: diagnostic-audit.md (unfinished; not a final query)")
    return "Not delivered", lines


# -- status reminder --------------------------------------------------------------------------

RESEND_WHEN_CHANGED = ("scope", "deliver")  # the user must see the current version of these


def stage_reminders(ws: Workspace) -> tuple[dict, list[str]]:
    """Which stage summaries were sent, and which are due but not sent. Never blocks anything."""
    try:
        return _stage_reminders(ws)
    except Exception as exc:  # noqa: BLE001 - psb status must never fail because of progress files
        return {}, [f"progress state could not be read ({type(exc).__name__}); psb progress list shows what was sent"]


def _stage_reminders(ws: Workspace) -> tuple[dict, list[str]]:
    sent = {stage: [m for m in messages(ws) if m.get("event") == f"stage:{stage}"] for stage in STAGES}
    protocol = ws.protocol()
    strategy_blocks = bool(ws.strategy().blocks) if (ws.root / "strategy.json").exists() else False
    due = {
        "intake": True,
        "scope": bool(protocol.get("concepts")),
        "known-records": bool(ws.sets() or decisions(ws) or strategy_blocks),
        "vocabulary": strategy_blocks,
        "test": bool(ws.versions()),
        "critic": any((ws.root / "critic").glob("round-*.json")),
        "deliver": any(a.get("purpose") in REPORT_PURPOSES for a in ws.attempts()),
    }
    todo = [f"send the Step {STAGES[s]} summary: psb progress {s}" for s in STAGES if due[s] and not sent[s]]
    for stage in RESEND_WHEN_CHANGED:
        if due[stage] and sent[stage]:
            try:
                current = render(ws, f"stage:{stage}")["text"]
            except (ProgressError, WorkspaceError, OSError, ValueError):
                continue
            if current != sent[stage][-1].get("text"):
                todo.append(f"send the Step {STAGES[stage]} summary again (it changed since it was sent): "
                            f"psb progress {stage}")
    return {stage: bool(rows) for stage, rows in sent.items()}, todo

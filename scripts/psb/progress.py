"""Standardised progress messages: what step is running and what it produced.

Every message the agent relays to the user is rendered here from fixed templates over workspace
state, so the same state always gives the same text, byte for byte. Renderers never read a clock,
a random source or the message sequence number.

    progress.jsonl    every emitted message, appended
    candidates.jsonl  candidate batches surfaced by neighbors, sample --purpose and resolve
    screening.jsonl   screening decisions recorded by psb screen (the latest per PMID counts)

None of these files is part of ``validation.input_snapshot``: they never affect evaluation,
critic binding or delivery verification.

A restricted invocation (one serving the separate screening context; see disclosure.py) gets a
``separate:*`` message built from permitted facts only. Messages for the builder never list a record
whose latest decision was made in the separate context, and never attribute screening yields to a
batch from that context.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import unicodedata
from pathlib import Path

from . import syntax
from .disclosure import DISCLOSURE_VERSION, OPERATIONS, command_tokens
from .strategy import lint
from .workspace import ORIGINS, Workspace, WorkspaceError, normalize_pmids, purpose_label, purpose_of, read_json

TOTAL_STEPS = 7
STEPS = {1: "Intake", 2: "Scope", 3: "Known records", 4: "Vocabulary", 5: "Develop & revise", 6: "Critic", 7: "Deliver"}
# "test" keeps naming Step 5 so legacy progress logs still read; the held-out test is psb holdout-test.
STAGES = {"intake": 1, "scope": 2, "known-records": 3, "vocabulary": 4, "test": 5, "critic": 6, "deliver": 7}
PURPOSE_ORDER = ("development", "comparison")
PURPOSE_GROUPS = {"development": "development sets", "comparison": "comparison lists"}
PURPOSE_USE = {
    "development": "used for term mining, diagnosing misses and repeated development checks",
    "comparison": "outside the allocation pool; checked and reported separately, not mined, never a held-out test",
}
SCREEN_BUDGET = {"quick": 30, "standard": 150, "thorough": 400}
DECISIONS = ("include", "exclude", "uncertain")
CONTEXTS = ("separate", "builder")
EVIDENCE = ("title", "abstract", "full-text")
# The origin a candidate batch gives the records it showed.
VIA_ORIGIN = {"prior-reviews": "prior-review", "pilot": "pilot-search", "resolve": "user-supplied",
              "similar": "similar-articles", "refs": "citation-backward", "citedin": "citation-forward"}
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
        purpose = purpose_of(sets[name] or {})
        return (PURPOSE_ORDER.index(purpose) if purpose in PURPOSE_ORDER else len(PURPOSE_ORDER), name)
    return sorted(sets, key=key)


def _recall(evaluation: dict) -> str:
    """Retrieval of each known-record set, development first; held-out records are never here."""
    sets = evaluation.get("sets") or {}
    if not sets:
        return "not measured (no known-record sets)"
    groups: dict[str, list[str]] = {}
    for name in _set_order(sets):
        data = sets[name]
        purpose = purpose_of(data)
        groups.setdefault(PURPOSE_GROUPS.get(purpose, purpose), []).append(
            f"{name} {_n(data.get('retrieved'))}/{_n(data.get('in_pubmed'))} ({_pct(data.get('recall_percent'))})")
    return " · ".join(f"{group}: {', '.join(parts)}" for group, parts in groups.items())


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
        "scope": (f"Step 3/7 Known records: screen any seed articles, with targeted discovery up to "
                  f"~{SCREEN_BUDGET['quick']} candidates (quick), then freeze the allocation (psb allocate)."
                  if depth == "quick" else
                  f"Step 3/7 Known records: screen seeds, look for prior reviews, run pilot and citation searches, "
                  f"screen up to ~{SCREEN_BUDGET.get(depth, 150)} candidates ({depth}), then choose the allocation "
                  "(psb allocate)."),
        "known-records": "Step 4/7 Vocabulary: build MeSH and [tiab] terms for each searched concept.",
        "vocabulary": ("Step 5/7 Develop & revise: check counts and development retrieval, and fix misses one change "
                       "at a time."),
        "test": (f"Step 6/7 Critic: fresh-context PRESS-structured review, up to {revision_budget(depth)} revision "
                 f"round(s) then a closing round ({depth})."),
        "critic": ("Step 7/7 Deliver: the held-out test when records are reserved (psb holdout-test), then live "
                   "revalidation and the protected final query (psb report)."),
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
    path.parent.mkdir(parents=True, exist_ok=True)
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
                 origin: list[str] | None = None, query: str | None = None, private: bool = False) -> dict:
    """Append a candidate batch; the allocation reads its ``via`` and ``pmids`` for origins. A batch
    found in the separate context keeps a fixed label and no query or seeds in candidates.jsonl: its
    raw provenance goes to screening/batches.jsonl under the same batch id."""
    number = f"C{len(batches(ws)) + 1}"
    if private:
        _append(ws.root / "screening" / "batches.jsonl",
                {"batch": number, "via": via, "label": label, "from": list(origin or []), "query": query})
    entry = {"batch": number, "via": via, "label": method_label(via) if private else label,
             "from": [] if private else list(origin or []), "query": None if private else query, "total": total,
             "pmids": list(pmids), "private": private, "disclosure_version": DISCLOSURE_VERSION}
    _append(ws.root / "candidates.jsonl", entry)
    return entry


def method_label(via: str) -> str:
    """A batch's discovery method, from its fixed ``via`` code alone."""
    if via.startswith("neighbors:"):
        kinds = " + ".join(LINK_SHORT.get(l, "linked records") for l in via.split(":", 1)[1].split(","))
        return kinds[:1].upper() + kinds[1:]
    return {"prior-reviews": PURPOSES["prior-reviews"], "pilot": PURPOSES["pilot"],
            "resolve": "Resolved identifiers"}.get(via, "Candidate search")


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


def _details(item: dict, defaults: dict) -> dict:
    """The screening record's context, study group, origin, evidence basis and source reference."""
    out = {}
    context = item.get("context") or defaults.get("context") or "builder"
    if context not in CONTEXTS:
        raise ProgressError(f"context must be one of {', '.join(CONTEXTS)}")
    out["context"] = context
    group = item.get("group", defaults.get("group"))
    out["group"] = clean(group, 120) or None
    origin = item.get("origin", defaults.get("origin")) or []
    origin = [origin] if isinstance(origin, str) else list(origin)
    if any(o not in ORIGINS for o in origin):
        raise ProgressError(f"origin must be one of {', '.join(ORIGINS)}")
    out["origin"] = sorted(set(origin))
    evidence = item.get("evidence", defaults.get("evidence"))
    if evidence is not None and evidence not in EVIDENCE:
        raise ProgressError(f"evidence must be one of {', '.join(EVIDENCE)}")
    out["evidence"] = evidence
    out["source_ref"] = clean(item.get("source_ref", defaults.get("source_ref")), 300) or None
    return out


def record_screening(ws: Workspace, *, include=(), exclude=(), uncertain=(), reason: str = "",
                     file: str | None = None, context: str | None = None, group: str | None = None,
                     origin=None, evidence: str | None = None, source_ref: str | None = None) -> list[dict]:
    """Append screening decisions. A decision made in the separate screening context keeps its reason
    and source reference in the private store (screening/decisions.jsonl): they describe the record."""
    defaults = {"context": context, "group": group, "origin": origin, "evidence": evidence, "source_ref": source_ref}
    rows: list[tuple[str, str, str, dict]] = []
    for decision, values in (("include", include), ("exclude", exclude), ("uncertain", uncertain)):
        rows += [(p, decision, reason.strip(), _details({}, defaults)) for p in normalize_pmids(values or [])]
    if file:
        data = read_json(Path(file))
        if not isinstance(data, list):
            raise ProgressError("the decisions file must be a JSON list of {pmid, decision, reason}")
        for item in data:
            if not isinstance(item, dict) or item.get("decision") not in DECISIONS:
                raise ProgressError(f"each decision needs a decision of {', '.join(DECISIONS)}: {item!r}")
            rows += [(p, item["decision"], str(item.get("reason") or reason).strip(), _details(item, defaults))
                     for p in normalize_pmids([item.get("pmid", "")])]
    if not rows:
        raise ProgressError("give at least one PMID with --include, --exclude, --uncertain or --file")
    seen: dict[str, str] = {}
    for pmid, decision, _, _ in rows:
        if seen.setdefault(pmid, decision) != decision:
            raise ProgressError(f"PMID {pmid} has two decisions ({seen[pmid]} and {decision}) in one call")
    unique = list({pmid: (pmid, decision, why, extra) for pmid, decision, why, extra in rows}.values())
    before = decisions(ws)
    entries = []
    for pmid, decision, why, extra in unique:
        private = extra["context"] == "separate"
        entry = {"pmid": pmid, "decision": decision, "reason": "" if private else why,
                 "previous": before[pmid]["decision"] if pmid in before else None,
                 **{k: v for k, v in extra.items() if k != "source_ref" or not private}}
        if private:
            entry["private"] = True
            _append(ws.root / "screening" / "decisions.jsonl",
                    {"pmid": pmid, "decision": decision, "reason": why, "source_ref": extra["source_ref"]})
        _append(ws.root / "screening.jsonl", entry)
        entries.append(entry)
    return entries


def private_decisions(ws: Workspace) -> dict[str, dict]:
    """The separate context's latest reason and source reference per PMID (never shown to the builder)."""
    latest: dict[str, dict] = {}
    for row in _read_jsonl(ws.root / "screening" / "decisions.jsonl"):
        if str(row.get("pmid", "")).isdigit():
            latest[str(row["pmid"])] = row
    return latest


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
    head = f"**PSB · Step {step}/{TOTAL_STEPS} {STEPS[step]} · {title}**" if step else f"**PSB · {title}**"
    return {"event": name, "step": step, "text": "\n".join([head, *lines])}


def _store(ws: Workspace, message: dict) -> dict:
    seq = len(messages(ws)) + 1
    _append(ws.root / "progress.jsonl", {**message, "seq": seq,
                                          "sha256": hashlib.sha256(message["text"].encode("utf-8")).hexdigest(),
                                          "disclosure_version": DISCLOSURE_VERSION})
    return {**message, "seq": seq}


def emit(ws: Workspace, name: str, data: dict | None = None) -> dict:
    return _store(ws, render(ws, name, data))


def fallback(name: str, exc: BaseException) -> dict:
    """A fixed message naming the exception class only: an exception's text can quote private content."""
    step = EVENTS[name][0] if name in EVENTS else 0
    label = f"Step {step}/{TOTAL_STEPS} {STEPS[step]}" if step else "Progress"
    text = (f"**PSB · {label} · {name}**\nProgress message unavailable ({type(exc).__name__}); "
            "the command itself ran: see its JSON result.")
    return {"event": name, "step": step, "text": text, "error": type(exc).__name__}


def attach(body: dict, ws: Workspace, name: str, data=None, *, verbose: bool | None = None) -> dict:
    """Add the message for a command that has already done its work.

    ``data`` is a dict, or a function returning one (so preparing the message is guarded too). A
    message never changes what the command did, its ``ok`` or its exit code: on any failure the
    command carries a fixed fallback message.

    ``verbose``: add the event's bounded details (see ``DETAILS``). None reads the progress mode,
    once, and only for an event that has details; standard mode does no detail work at all.
    """
    try:
        data = data() if callable(data) else data
        message = render(ws, name, data)
        if name in DETAILS:
            if verbose is None:
                mode, notice = read_mode(ws)
                verbose = mode == "verbose"
                if notice:
                    body["progress_notice"] = notice
            if verbose:
                message, notice = _detailed(name, ws, data or {}, message)
                if notice:
                    body["progress_notice"] = notice
        body["progress"] = _store(ws, message)
    except Exception as exc:  # noqa: BLE001 - the command's own result must stand
        message = fallback(name, exc)
        if getattr(ws, "restricted", False):
            try:  # the raw error stays with the separate context
                ws.log({"type": "error", "event": name, "error": f"{type(exc).__name__}: {exc}"})
            except Exception:  # noqa: BLE001
                pass
        try:
            _append(ws.root / "progress.jsonl", {**message, "seq": len(messages(ws)) + 1,
                                                  "disclosure_version": DISCLOSURE_VERSION})
        except Exception:  # noqa: BLE001
            pass
        body["progress"] = message
    return body


def attach_restricted(body: dict, ws: Workspace, name: str, *, processed: int | None = None,
                      recorded: int | None = None, separate_only: bool | None = None,
                      links: list[str] | None = None) -> dict:
    """The message of a restricted invocation. Only these named facts reach its template: never the
    command's queries, seeds, records, decisions or reasons."""
    facts = {"processed": processed, "recorded": recorded, "separate_only": separate_only,
             "links": [l for l in links or [] if l in LINK_TITLES] or None}
    # Never verbose: privacy comes before verbosity.
    return attach(body, ws, f"separate:{name}", {k: v for k, v in facts.items() if v is not None}, verbose=False)


# -- verbose mode -----------------------------------------------------------------------------
# An opt-in, per-run preference (progress-settings.json) that adds a bounded "Details:" section to
# the completion messages of the commands in DETAILS. The section is built from the command's own
# in-memory results, never from new requests, and changes nothing the command did. Restricted
# invocations and stage summaries never get one.

SETTINGS = "progress-settings.json"
MODES = ("standard", "verbose")
SETTINGS_NOTICE = ("progress-settings.json is not a valid progress setting, so standard messages are used; "
                   "set it again with psb progress mode standard or psb progress mode verbose")
DETAIL_NOTICE = "Verbose details could not be prepared ({}); the standard message was sent"
DETAIL_HEAD = "Details:"
DETAIL_ROWS, DETAIL_WORDS, DETAIL_CHARS = 3, 80, 800
SEVERITY = {"error": 0, "warning": 1}
INFO = 2
_MARKDOWN = re.compile(r"([\\`*_\[\]<>|#~])")
# Each command's details: (ws, data) -> rows of (severity rank, source order, "- text").
DETAILS: dict[str, object] = {}


def read_mode(ws: Workspace) -> tuple[str, str | None]:
    """The progress mode and, when the setting is invalid, the fixed notice for the command's JSON. A
    missing file means standard; an invalid one is never repaired here."""
    try:
        data = json.loads((ws.root / SETTINGS).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return "standard", None
    except (OSError, ValueError):
        return "standard", SETTINGS_NOTICE
    if (isinstance(data, dict) and set(data) == {"version", "mode"} and type(data["version"]) is int
            and data["version"] == 1 and data["mode"] in MODES):
        return data["mode"], None
    return "standard", SETTINGS_NOTICE


def write_mode(ws: Workspace, mode: str) -> None:
    """Replace the setting atomically through a uniquely named temporary file."""
    if mode not in MODES:
        raise ProgressError(f"mode must be one of {', '.join(MODES)}")
    fd, temporary = tempfile.mkstemp(prefix=".progress-settings-", suffix=".tmp", dir=ws.root)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(json.dumps({"version": 1, "mode": mode}) + "\n")
        os.replace(temporary, ws.root / SETTINGS)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def _plain(text, limit: int) -> str:
    """Untrusted text on one line: control and format characters become spaces, then ``clean``."""
    return clean("".join(" " if unicodedata.category(c)[0] == "C" else c for c in str(text or "")), limit)


def _escaped(text, limit: int) -> str:
    """Untrusted prose, cut first and escaped after, so no Markdown syntax is cut midway."""
    return _MARKDOWN.sub(r"\\\1", _plain(text, limit))


def _term(text, limit: int = 60) -> str:
    return code(_plain(text, limit) or "?")


def _omitted(count: int) -> str:
    return f"- {_plural(count, 'more detail')} omitted"


def _fits(lines: list[str]) -> bool:
    text = "\n".join(lines)
    return len(text.split()) <= DETAIL_WORDS and len(text) <= DETAIL_CHARS


def section(rows: list[tuple[int, int, str]]) -> list[str]:
    """At most three whole rows, actionable ones first (by severity, then source order), within 80 words
    and 800 characters including the heading and the omission marker."""
    ordered = [text for _, _, text in sorted(rows, key=lambda r: (r[0], r[1]))]
    if not ordered:
        return []
    chosen: list[str] = []
    for row in ordered[:DETAIL_ROWS]:
        trial = [*chosen, row]
        rest = len(ordered) - len(trial)
        if not _fits([DETAIL_HEAD, *trial, *([_omitted(rest)] if rest else [])]):
            break  # whole rows only, and never a lower-priority row ahead of one that did not fit
        chosen = trial
    rest = len(ordered) - len(chosen)
    return [DETAIL_HEAD, *chosen, *([_omitted(rest)] if rest else [])]


def _detailed(name: str, ws: Workspace, data: dict, message: dict) -> tuple[dict, str | None]:
    """The message with its details, or the standard message and a fixed notice if they fail."""
    try:
        lines = section(DETAILS[name](ws, data))
    except Exception as exc:  # noqa: BLE001 - details never fail the command or its standard message
        return message, DETAIL_NOTICE.format(type(exc).__name__)
    return ({**message, "text": "\n".join([message["text"], *lines])} if lines else message), None


def details(name: str):
    def register(function):
        DETAILS[name] = function
        return function
    return register


@event("progress-mode", 0)
def _progress_mode(ws, data):
    if data.get("mode") == "verbose":
        return "Progress messages", ["Verbose: completion messages now add up to three bounded details. Searches, "
                                     "screening and what stays private are unchanged."]
    return "Progress messages", ["Standard: completion messages are back to their usual length."]


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
    label = "Records with a screening decision so far (all contexts)"
    if depth in SCREEN_BUDGET:
        return f"- {label}: {_n(screened)} of ~{_n(SCREEN_BUDGET[depth])} ({depth})"
    return f"- {label}: {_n(screened)} (no discovery budget at {clean(depth, 40)} depth)"


# -- the separate screening context ------------------------------------------------------------
# A restricted invocation's message: fixed labels, the processed-record count, the cumulative number
# of screening decisions with the budget, and whether allocation is pending. Two calls that differ
# only in private content (queries, seeds, records, decisions, reasons, groups, file names) give the
# same text.

SEPARATE = "Run in the separate screening context; details are kept private."
SEPARATE_EVENTS = {
    "search:prior-reviews": (3, PURPOSES["prior-reviews"]), "search:pilot": (3, PURPOSES["pilot"]),
    "search:noise-check": (5, PURPOSES["noise-check"]), "neighbors": (3, "Neighbour search"),
    "resolve": (3, "Identifier resolution"), "fetch": (3, "Records retrieved"), "screen": (3, "Screening"),
    "failed": (3, "Separate screening"),
}


def _separate_state(ws: Workspace) -> list[str]:
    lines = [_budget_line(ws, len(decisions(ws)))]
    if ws.allocation() is None:
        lines.append("- Allocation is pending.")
    return lines


def _separate_event(name: str, title: str):
    def renderer(ws, data):
        if name == "screen":
            recorded = _plural(data.get("recorded", 0), "candidate")
            lead = (f"Recorded decisions for {recorded} in the separate screening context; details are kept private."
                    if data.get("separate_only") else
                    f"Recorded decisions for {recorded}; detailed attribution is withheld.")
        elif name == "failed":
            operation = data.get("operation") if data.get("operation") in OPERATIONS.values() else "A command"
            lead = f"{operation} did not complete in the separate screening context; details are kept private."
        else:
            lead = SEPARATE
        lines = [lead]
        if data.get("processed") is not None:
            lines.append(f"- {'Identifiers' if name == 'resolve' else 'Records'} processed: {_n(data['processed'])}")
        if ws is not None:
            lines += _separate_state(ws)
        links = [LINK_TITLES[l] for l in data.get("links") or [] if l in LINK_TITLES]
        return (" + ".join(links) if name == "neighbors" and links else title), lines
    return renderer


for _name, (_step, _title) in SEPARATE_EVENTS.items():
    event(f"separate:{_name}", _step)(_separate_event(_name, _title))


def _included_unset(ws: Workspace) -> list[str]:
    """Included records in no set and not allocated: reserved records are never listed."""
    in_sets = {p for data in ws.sets().values() for p in data.get("pmids", [])}
    allocation = ws.allocation()
    allocated = {p for u in (allocation or {}).get("units", []) for p in u.get("members", [])} | ws.reserved_pmids()
    return [p for p, row in decisions(ws).items() if row["decision"] == "include" and p not in in_sets | allocated]


def builder_visible(ws: Workspace, pmids) -> list[str]:
    """``pmids`` without records whose latest screening decision was made in the separate context: listed,
    they would give the held-out records by subtraction once the development set is visible."""
    latest = decisions(ws)
    return [p for p in dict.fromkeys(str(p) for p in pmids) if (latest.get(p) or {}).get("context") != "separate"]


def _separate_pending(ws: Workspace) -> int:
    """Records whose latest separate-context decision is include and that the allocation has not yet
    considered. Neither a builder decision nor a set change can move this count, so it gives no feedback
    on a record the builder also handles."""
    latest: dict[str, str] = {}
    for row in _read_jsonl(ws.root / "screening.jsonl"):
        if row.get("context") == "separate" and row.get("decision") in DECISIONS and str(row.get("pmid", "")).isdigit():
            latest[str(row["pmid"])] = row["decision"]
    allocation = ws.allocation() or {}
    excluded = allocation.get("excluded") or {}
    considered = ({str(p) for u in allocation.get("units", []) for p in u.get("members", [])}
                  | {str(p) for key in ("unavailable", "on_comparison") for p in excluded.get(key) or []}
                  | ws.reserved_pmids())
    return sum(1 for p, decision in latest.items() if decision == "include" and p not in considered)


def _unset(ws: Workspace) -> str:
    """Included records waiting for a set or the allocation: the builder's own are listed, those from the
    separate context only counted."""
    shown = builder_visible(ws, _included_unset(ws))
    pending = _separate_pending(ws)
    if not pending:
        return _pmids(shown)
    counted = f"{_plural(pending, 'record')} from the separate screening context (not listed)"
    return f"{_pmids(shown)}; plus {counted}" if shown else counted


WITHHELD = "Separate-context or earlier discovery (attribution withheld)"


def _builder_batch(batch: dict) -> bool:
    """A batch the builder ran itself, recorded under the current disclosure policy."""
    return batch.get("disclosure_version") == DISCLOSURE_VERSION and not batch.get("private")


def _batch_number(batch: dict) -> int:
    number = str(batch.get("batch", ""))[1:]
    return int(number) if number.isdigit() else 0


def _by_source(ws: Workspace, rows: list[dict]) -> list[str]:
    """Screened records by the batch that first showed them, with each batch's include yield. Batches
    from the separate context, and batches recorded before they were marked, fold into one row with no
    yield, whoever screens: a yield would be eligibility feedback on a private query."""
    source = attribution(ws)
    groups: dict[tuple, dict] = {}
    for row in rows:
        batch = source.get(row["pmid"])
        if batch is None:
            key, label = (2, 0), UNLOGGED
        elif _builder_batch(batch):
            key, label = (0, _batch_number(batch)), f"{batch['label']} ({batch['batch']})"
        else:
            key, label = (1, 0), WITHHELD
        group = groups.setdefault(key, {"label": label, "screened": 0, "include": 0})
        group["screened"] += 1
        group["include"] += row["decision"] == "include"
    return [f"- {g['label']}: {_n(g['screened'])} screened"
            + ("" if key[0] == 1 else f" → {_n(g['include'])} include") for key, g in sorted(groups.items())]


def _previous_contexts(ws: Workspace, pmids: set[str]) -> dict[str, str]:
    """The context of the decision before each PMID's latest one."""
    history: dict[str, list[str]] = {}
    for row in _read_jsonl(ws.root / "screening.jsonl"):
        pmid = str(row.get("pmid", ""))
        if pmid in pmids and row.get("decision") in DECISIONS:
            history.setdefault(pmid, []).append(row.get("context") or "builder")
    return {p: h[-2] for p, h in history.items() if len(h) > 1}


def _tally(rows) -> str:
    counts = {d: sum(1 for r in rows if r["decision"] == d) for d in DECISIONS}
    return " · ".join(f"{_n(counts[d])} {d}" for d in DECISIONS)


@event("screen", 3)
def _screen(ws, data):
    rows = data.get("entries") or []
    lines = [f"Screened {_plural(len(rows), 'candidate')}: {_tally(rows)}", *_by_source(ws, rows)]
    # A change from a separate-context decision would reveal that decision: it is never mentioned.
    earlier = _previous_contexts(ws, {r["pmid"] for r in rows})
    changed = [r for r in rows if r.get("previous") and r["previous"] != r["decision"]
               and earlier.get(r["pmid"]) != "separate"]
    if changed:
        lines.append(f"- Decisions changed from an earlier screen: {_pmids(r['pmid'] for r in changed)}")
    lines.append(_budget_line(ws, len(decisions(ws))))
    lines.append(f"- Included but not yet in a set: {_unset(ws)}")
    return "Screening", lines


@event("set", 3)
def _set(ws, data):
    purpose = data.get("purpose")
    lines = [f"Set {data.get('name')} ({purpose}): {_n(data.get('before', 0))} → {_plural(data.get('after', 0), 'record')}",
             f"- Use: {PURPOSE_USE.get(purpose, 'unknown purpose')}"]
    if data.get("origin"):
        lines.append(f"- Origin: {', '.join(data['origin'])}")
    if data.get("added"):
        lines.append(f"- Added: {_pmids(data['added'])}")
    if data.get("removed"):
        lines.append(f"- Removed: {_pmids(data['removed'])}")
    if data.get("late"):
        lines.append(f"- Kept out: {_plural(data['late'], 'record')} reporting a study reserved for the held-out test")
    for other, pmids in sorted((data.get("overlap") or {}).items()):
        lines.append(f"- Also in {other}, which has another purpose: {_pmids(pmids)}")
    return "Set updated", lines


# The allocation-choice message: fixed text around the counts. Relayed verbatim; asked once.
CHOICE_EXPLAINED = (
    "A held-out check can reveal retrieval gaps. Retrieving every reserved record would show that the query found "
    "those records; it would not establish that all relevant literature was found. The reassurance depends on the "
    "test's size, coverage, and separation from development.")
CHOICE_QUESTION = "**Keep the proposed holdout**, or **use everything for development**?"
CHOICE_TRADEOFF = "Using everything provides more development material but leaves no independent final test."


def _separation(proposal: dict) -> str:
    n, u = proposal["N"], proposal["U"]
    return (f"{_plural(u, 'unit')} of {_n(n)} were screened only in the separate context and never shown to the builder; "
            f"the held-out units are drawn from these. The other {_plural(n - u, 'unit')} were seen by the builder and "
            "go to development")


@event("allocation-preview", 3)
def _allocation_preview(ws, data):
    from .interpret import NO_HOLDOUT
    proposal = data.get("proposal") or {}
    units = lambda c: f"{_plural(c['units'], 'unit')} ({_plural(c['records'], 'record')})"  # noqa: E731
    if not proposal.get("H"):
        lines = [f"No holdout is proposed: {NO_HOLDOUT.get(proposal.get('reason'), 'not recorded')}.",
                 f"- Eligible pool: {units(proposal['pool'])}; all of it is used for development",
                 f"- Unexposed units: {_n(proposal.get('U', 0))} of {_n(proposal.get('N', 0))}",
                 "- Next: psb allocate freezes this allocation"]
        return "Allocation", lines
    studies = (f"{_plural(proposal['studies'], 'study', 'studies')}" if proposal.get("studies") is not None
               else "an unverified number of studies")
    lines = ["**Choose how to use the eligible reference records**", "",
             f"Eligible pool: **{_plural(proposal['pool']['records'], 'record')} representing {studies}.**", "",
             f"- **Development: {units(proposal['development'])}** — used for term mining, diagnosing misses, and "
             "improving the search.",
             f"- **Held-out test: {units(proposal['holdout'])}** — reserved for one retrieval check after the query is "
             "finalised.", "",
             f"**Separation:** {_separation(proposal)}.", "",
             CHOICE_EXPLAINED, "", CHOICE_QUESTION, "", CHOICE_TRADEOFF]
    return "Choose the allocation", lines


@event("allocation", 3)
def _allocation(ws, data):
    from .allocation import summary
    held = summary(ws)
    if held is None:
        raise ProgressError("no allocation frozen")
    text = _allocation_text(held)
    lines = [text[:1].upper() + text[1:]]
    if data.get("rebind"):
        removed = sum(len(e.get("removed") or []) for e in ws.allocation_events() if e.get("type") == "rebind")
        lines.append(f"- Re-bound to the current scope: {_plural(removed, 'reserved record')} removed in total")
    if held["H"] and not held["released"]:
        lines.append("- Held-out records are not shown, mined, sampled or diagnosed until the held-out test")
    return "Allocation frozen", lines


@event("holdout-test", 7)
def _holdout_test(ws, data):
    return "Held-out test", str(data.get("text") or "").split("\n")


@event("holdout-release", 7)
def _holdout_release(ws, data):
    event = data.get("event") or {}
    return "Held-out records released", [
        f"Released {_plural(len(event.get('members') or []), 'held-out record')} to development: "
        f"{clean(event.get('reason'), 200)}",
        f"- Receipts kept: {', '.join(str(n) for n in event.get('receipts') or []) or 'none (released before testing)'}",
        "- The revised query will have no independent held-out test; its review starts a repair epoch "
        "(one revision round, then the closing round)"]


@event("terms-rank", 4)
def _terms_rank(ws, data):
    sets = data.get("sets")
    mined = sorted(data.get("comparison_mined") or [])
    scope = ("sets " + ", ".join(sets)) if sets else "all development sets"
    scope += (f"; includes comparison {', '.join(mined)}" if mined
              else "; comparison lists excluded; held-out records are never mined")
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
        lines += [f"- Known-record retrieval: {_recall(evaluation)}", f"- Missed known records: {_misses(evaluation)}"]
    else:
        lines.append(f"- Known-record retrieval: {NOT_MEASURED}")
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
    from .deliver import current_epoch, epoch_budget, epoch_kind, latest_evaluation, next_round, round_epoch
    rounds = _list(data.get("rounds_before"))
    evaluation = latest_evaluation(ws)
    number, kind = next_round(ws, evaluation, rounds)
    epoch = current_epoch(ws)
    revision = sum(bool(r.get("review_sha256")) and not r.get("closing") for r in rounds
                   if isinstance(r, dict) and round_epoch(r) == epoch) + 1
    label = f"revision {revision} of {epoch_budget(ws, epoch)}" if kind == "revision" else kind
    if epoch > 1:
        label = f"{epoch_kind(ws, epoch)} {label}"
    return f"Round {number} packet", [
        f"Round {number} ({label}) packet written for v{evaluation.get('version')}",
        f"- Packet: critic/{data.get('packet')}",
        f"- A fresh-context reviewer reads only this packet; its reply is saved as critic/round-{number}.json",
    ]


def _extension_line(ws: Workspace) -> list[str]:
    from .deliver import critic_extensions
    return [f"- Review budget extended at the user's request: {clean(e.get('reason'), 200)}" for e in critic_extensions(ws)]


@event("critic-extend", 6)
def _critic_extend(ws, data):
    return "Review extended", [
        f"Review budget extended at the user's request: {clean(data.get('reason'), 200)}",
        f"- One more review period after round {_n(data.get('after_round'))}: one revision round, then a closing round "
        "and a verification round",
        "- The audit discloses the extension on its first page; held-out records are not touched",
        "- Next: psb critic packet",
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
    from .deliver import critic_extensions, critic_rounds
    rounds = critic_rounds(ws)
    extended = "".join(f"; review budget extended at the user's request: {clean(e.get('reason'), 200)}"
                       for e in critic_extensions(ws))
    return (f"- Critic: {_plural(len(rounds), 'round')} (internal PRESS-structured critique, not PRESS peer review); "
            f"overridden findings: {', '.join(sorted(overridden)) or 'none'}{extended}")


def _held_result(manifest: dict) -> str:
    """The Result line of the delivered interpretation; the whole text is in the Step 7 summary."""
    text = str((manifest.get("holdout") or {}).get("text") or "")
    line = next((l for l in text.split("\n") if l.startswith("- **Result:** ")), "")
    return line.removeprefix("- **Result:** ") or "not recorded (legacy delivery)"


@event("report", 7)
def _report(ws, data):
    result = data.get("result") or {}
    if result.get("ok"):
        evaluation = _attempt(ws, result.get("attempt_id"))
        manifest = read_json(ws.root / "validation-manifest.json")
        return "Report", [f"Delivered: final query validated live, {_n(evaluation.get('count'))} records",
                          f"- Known-record retrieval: {_recall(evaluation)}",
                          f"- Held-out test: {_held_result(manifest)}",
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


# -- verbose details --------------------------------------------------------------------------
# Rows come from the finished command's results only: no request, check or judgement is added. A
# row says "returned" or "not run" rather than implying completeness it does not have.

def _rank(issue: dict) -> int:
    return SEVERITY.get(issue.get("severity"), INFO)


def _search_details(ws, data):
    rows: list[tuple[int, int, str]] = []
    for issue in data.get("issues") or []:
        rows.append((_rank(issue), len(rows), f"- PubMed translation {_plain(issue.get('severity') or 'note', 10)}: "
                                              f"{_term(issue.get('code'), 40)}"))
    shown, total = data.get("shown"), data.get("count")
    if shown is not None:  # a count says "count only" in its standard line already
        if not total:
            method = "no records matched, so none were shown"
        elif data.get("random"):
            method = (f"{_plural(shown, 'record')} of {_n(total)} from offset {_n(data.get('retstart') or 0)}, the offset "
                      f"chosen at random with seed {_n(data.get('seed'))}")
        else:
            method = f"the first {_plural(shown, 'record')} of {_n(total)}, in the order PubMed returned them"
        rows.append((INFO, len(rows), f"- Method: {method}"))
    if data.get("translation"):
        rows.append((INFO, len(rows), f"- PubMed translation: {_term(data['translation'], 160)}"))
    for record in data.get("records") or []:
        rows.append((INFO, len(rows), f"- Example: PMID {_plain(record.get('pmid'), 12)}, {_term(record.get('title'), 100)}"))
    return rows


for _purpose in PURPOSES:
    details(f"search:{_purpose}")(_search_details)


@details("neighbors")
def _neighbors_details(ws, data):
    links = " and ".join(LINK_DETAIL.get(l, _plain(l, 20)) for l in data.get("links") or [])
    rows = [(INFO, 0, f"- Method: {links} of {_plural(len(data.get('from') or []), 'record')}, up to "
                      f"{_n(data.get('max_per_seed'))} per record and link, ranked by the number of linking "
                      "records, then score")]
    for i, row in enumerate(data.get("rows") or []):
        rows.append((INFO, i + 1, f"- Example: PMID {_plain(row.get('pmid'), 12)}, linked from "
                                  f"{_plural(len(row.get('from') or []), 'record')}"))
    return rows


@details("resolve")
def _resolve_details(ws, data):
    given = [str(i).strip() for i in [*(data.get("resolved") or {}), *(data.get("unresolved") or [])]]
    routes = [text for test, text in (
        (any(i.isdigit() for i in given), "PMIDs as given"),
        (any(i.upper().startswith("PMC") for i in given), "PMCIDs through the PMC ID converter"),
        (any(i.lower().startswith(("10.", "doi:", "https://doi.org/")) for i in given),
         "DOIs by a [doi] search that must return exactly one record")) if test]
    return [(INFO, 0, f"- Method: {'; '.join(routes) or 'no recognised identifier'}; every PMID then checked "
                      "against PubMed")]


@event("mesh-lookup", 4)
def _mesh_lookup(ws, data):
    matches = data.get("matches") or []
    return "MeSH lookup", [f"{_term(data.get('query'), 120)}: {_plural(len(matches), 'candidate record')} returned"]


@details("mesh-lookup")
def _mesh_lookup_details(ws, data):
    # NCBI's order is not by relevance: a heading named exactly as the phrase comes first, then that order.
    phrase = " ".join(str(data.get("query") or "").casefold().split())
    return [(INFO, -1 if " ".join(str(m.get("name") or "").casefold().split()) == phrase else i,
             f"- {_term(m.get('name'), 80)} ({_plain(m.get('ui'), 12) or 'no UI'}, "
             f"{_plain(m.get('type'), 20) or 'type not returned'})")
            for i, m in enumerate(data.get("matches") or [])]


@event("mesh-show", 4)
def _mesh_show(ws, data):
    record = data.get("record") or {}
    counts = record.get("pubmed_count")
    if isinstance(counts, dict):
        line = "- PubMed counts: " + " · ".join(f"{_term(label, 20)} {_n(value)}" for label, value in counts.items())
    else:
        line = "- PubMed counts: " + ("not requested (--no-counts)" if data.get("no_counts") else "not returned")
    return "MeSH record", [f"Details retrieved for {_term(record.get('name'), 120)} ({_plain(record.get('ui'), 12) or 'no UI'}, "
                           f"{_plain(record.get('type'), 20) or 'type not returned'})", line]


def _examples(values: list, limit: int = 3) -> str:
    shown = ", ".join(_term(v, 40) for v in values[:limit])
    return f", e.g. {shown}" if shown else ""


@details("mesh-show")
def _mesh_show_details(ws, data):
    record = data.get("record") or {}
    note = _escaped(record.get("scope_note"), 160)
    entries = record.get("entry_terms") if isinstance(record.get("entry_terms"), list) else []
    narrower = record.get("narrower")
    rows = [(INFO, 0, f"- Scope note: {note}" if note else "- Scope note: none returned"),
            (INFO, 1, f"- Entry terms: {_n(len(entries))} returned{_examples(entries)}")]
    if isinstance(narrower, list):
        capped = " (the list stops at 100)" if len(narrower) >= 100 else ""
        rows.append((INFO, 2, f"- Narrower headings: {_n(len(narrower))} returned{capped}"
                              f"{_examples([n.get('name') for n in narrower if isinstance(n, dict)])}"))
    else:
        rows.append((INFO, 2, "- Narrower headings: not retrieved"))
    return rows


@details("terms-rank")
def _terms_rank_details(ws, data):
    if data.get("comparison_mined"):
        # The existing disclosure stands; examples could come from comparison records.
        return [(INFO, 0, "- Examples withheld: comparison records were mined, so the candidates' development-only "
                          "provenance is not established")]
    scored = data.get("ranking") or []
    if not scored:
        reason = "no candidate terms were found" if not data.get("candidates") else \
            f"no candidates were scored (background-count budget {_n(data.get('budget'))})"
        return [(INFO, 0, f"- Examples: none; {reason}")]
    rows = []
    for i, row in enumerate(scored):
        flags = [label for flag, label in (("generic", "generic"), ("noise_risk", "noise risk")) if row.get(flag)]
        rows.append((INFO, i, f"- {_term(row.get('term'))} ({_plain(row.get('field'), 10)}): in {_n(row.get('df'))} of "
                              f"{_n(data.get('records'))} records · {_n(row.get('background'))} in PubMed"
                              + (f" · {', '.join(flags)}" if flags else "")))
    return rows


@details("eval")
def _eval_details(ws, data):
    evaluation = data.get("evaluation") or {}
    if evaluation.get("count") is None:
        return [(0, 0, "- Details: not available (the evaluation did not complete)")]
    rows: list[tuple[int, int, str]] = []
    add = lambda rank, text: rows.append((rank, len(rows), text))  # noqa: E731 - source order
    for blocker in (evaluation.get("validation") or {}).get("blockers") or []:
        add(0, f"- Blocker: {_term(blocker.get('code'), 40)} at {_plain(blocker.get('location'), 30)}")
    for issue in evaluation.get("translation_issues") or []:
        add(_rank(issue), f"- Final query {_plain(issue.get('severity') or 'note', 10)}: {_term(issue.get('code'), 40)}")
    lines = evaluation.get("lines") or []
    for line in lines:
        for issue in line.get("issues") or []:
            if issue.get("code") == "zero_hits":
                add(_rank(issue), f"- Zero hits: line {_n(line.get('n'))} {_term(line.get('text') or line.get('query'), 80)}")
            else:
                add(_rank(issue), f"- Line {_n(line.get('n'))} {_plain(issue.get('severity') or 'note', 10)}: "
                                  f"{_term(issue.get('code'), 40)}")
    if data.get("term_counts") is False or not any(line.get("kind") == "term" for line in lines):
        add(INFO, "- Term checks: not run (--no-term-counts)" if data.get("term_counts") is False
            else "- Term checks: no term lines returned")
    sets = evaluation.get("sets") or {}
    coverage = evaluation.get("block_recall")
    if not sets:
        add(INFO, "- Block coverage: not measured (no known-record sets)")
    elif isinstance(coverage, dict):
        # block_recall counts development and comparison records together; per-set figures are above.
        combined = any(purpose_of(s) == "comparison" for s in sets.values())
        label = "combined known-record coverage" if combined else "development records"
        for block, found in coverage.items():
            add(INFO, f"- Block {_term(block, 40)}: {_n(found.get('retrieved'))}/{_n(found.get('of'))} ({label})")
    ablation = evaluation.get("ablation")
    if isinstance(ablation, str):
        add(INFO, f"- Ablation: {_plain(ablation, 100)}")
    elif sets and ablation is None:
        add(INFO, "- Ablation: not run (one block)")
    for row in ablation if isinstance(ablation, list) else []:
        if row.get("known_gained"):
            add(1, f"- Ablation: without {_term(row.get('drop'), 40)}, {_plural(row['known_gained'], 'more known record')} "
                   f"retrieved ({_n(row.get('count'))} records)")
        else:
            add(INFO, f"- Ablation: without {_term(row.get('drop'), 40)}, no known record gained ({_n(row.get('count'))} records)")
    return rows


@details("terms-miss")
def _terms_miss_details(ws, data):
    development = ws.set_pmids("development")
    rows = []
    for i, miss in enumerate(data.get("report") or []):
        pmid = str(miss.get("pmid"))
        failing = ", ".join(_plain(b, 30) for b in miss.get("failing_blocks") or []) \
            or ("limits" if miss.get("lost_to_limits") else "none")
        if pmid not in development:
            rows.append((1, i, f"- PMID {_plain(pmid, 12)}: fails {failing} (comparison record: no vocabulary examples)"))
            continue
        found = [*(miss.get("mesh_not_in_strategy") or [])[:1], *(miss.get("text_not_in_strategy") or [])[:2]]
        rows.append((1, i, f"- PMID {_plain(pmid, 12)}: fails {failing}; "
                           + (f"candidates {', '.join(_term(t, 40) for t in found)}" if found
                              else "no uncovered vocabulary returned")))
    return rows


# -- stage summaries --------------------------------------------------------------------------

@event("intake-request", 1)
def _intake_request(ws, data):
    """Asks only for what the user has not already given (``have_question``, ``have_articles``,
    ``have_depth``, ``have_limits``, ``have_mode``), with what each depth and the verbose mode change."""
    from .deliver import revision_budget
    rounds = lambda depth: _plural(revision_budget(depth), "critic revision round")  # noqa: E731
    asks: list[tuple[str, list[str]]] = []
    if not data.get("have_question"):
        asks.append(("The review question in plain language", []))
    if not data.get("have_articles"):
        asks.append(("Known relevant articles (PMIDs, DOIs or PMCIDs), if any (optional). These help identify useful "
                     "search terms and check whether the search retrieves studies it should find.", []))
    if not data.get("have_depth"):
        asks.append(("Depth: quick, standard (default) or thorough\n   Screening means checking retrieved articles for "
                     "relevance to help improve and test the search strategy. More screening allows more extensive "
                     "testing and refinement.", [
            f"quick: targeted discovery, up to ~{SCREEN_BUDGET['quick']} retrieved articles checked for relevance; "
            f"no automatic held-out test; {rounds('quick')}, then a closing round; fastest",
            f"standard: prior reviews, pilot and citation searches, up to ~{SCREEN_BUDGET['standard']} candidates "
            "screened; a held-out test is proposed when at least 10 eligible studies were screened privately; "
            f"{rounds('standard')}, then a closing round",
            f"thorough: as standard, up to ~{SCREEN_BUDGET['thorough']} candidates screened; "
            f"{rounds('thorough')}, then a closing round; takes longest"]))
    if not data.get("have_limits"):
        asks.append(("Required limits, such as dates or languages, if any", []))
    if not data.get("have_mode"):
        asks.append(("Progress messages: standard (default) or verbose", [
            "standard: short messages at each step",
            "verbose: up to three extra detail lines on search, MeSH, term-mining and evaluation messages (how "
            "records were found, headings returned, block coverage); it never changes what is searched, "
            "screened or kept private, and you can switch at any time"]))
    if not asks:
        return "Request", ["I have what I need to start."]
    lines = ["To build the search I need:"]
    for number, (ask, notes) in enumerate(asks, 1):
        lines += [f"{number}. {ask}", *[f"   - {note}" for note in notes]]
    return "Request", [*lines, 'Reply "proceed" to use the defaults (standard depth, standard messages, no limits) '
                               "for anything you leave out."]


@event("stage:intake", 1)
def _stage_intake(ws, data):
    protocol = ws.protocol()
    if not str(protocol.get("question") or "").strip():
        raise ProgressError("protocol.json has no question; record it first")
    seeds = {p for d in ws.sets().values() if d.get("role") == "seed" or "user-supplied" in (d.get("origin") or [])
             for p in d.get("pmids", [])}
    limits = protocol.get("limits") or []
    return "Summary", [
        f"Question: {clean(protocol.get('question'), 300)}",
        f"- Depth: {protocol.get('depth') or 'standard'}",
        f"- Required limits: {'; '.join(_limit_text(l) for l in limits) if limits else 'none'}",
        f"- Known articles recorded: {_plural(len(seeds), 'seed PMID') if seeds else 'none yet (added in Step 3)'}",
        f"- Progress messages: {read_mode(ws)[0]}",
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
    from .allocation import summary
    protocol = ws.protocol()
    sets = ws.sets()
    held = summary(ws)
    development = ws.set_pmids("development")
    comparison = ws.set_pmids("comparison") - development
    reserved = (held or {}).get("holdout", {}).get("records", 0) if held and not held["released"] else 0
    lines = [f"Known records: {_n(len(development))} for development · {_n(reserved)} held out · "
             f"{_n(len(comparison))} on comparison lists"]
    for name in _set_order(sets):
        purpose = purpose_of(sets[name])
        lines.append(f"- {name} ({purpose_label(sets[name])}): {_plural(len(sets[name].get('pmids', [])), 'record')} — "
                     f"{PURPOSE_USE.get(purpose, 'unknown purpose')}")
    if not sets and not held and not _included_unset(ws):  # eligible records waiting for allocation are known
        lines.append("- No known records yet: without them the strategy is empirically unvalidated.")
    lines.append(f"- Allocation: {_allocation_text(held)}")
    kinds: dict[str, int] = {}
    for batch in batches(ws):
        kinds[_kind(batch)] = kinds.get(_kind(batch), 0) + 1
    lines.append(f"- Candidate searches: {_n(sum(kinds.values()))}"
                 + (f" ({', '.join(f'{v} {k}' for k, v in sorted(kinds.items()))})" if kinds else ""))
    screened = list(decisions(ws).values())
    if screened:
        separate = sum(1 for row in screened if row.get("context") == "separate")
        lines.append(f"- Screening: {_n(len(screened))} screened → {_tally(screened)} "
                     f"(separate context {_n(separate)} · builder {_n(len(screened) - separate)})")
    else:
        lines.append("- Screening: none recorded")
    lines.append(_budget_line(ws, len(screened)))
    label = "Eligible, not yet allocated" if held is None else "Included after the allocation, not in a set"
    lines.append(f"- {label}: {_unset(ws)}")
    included = {p for p, row in decisions(ws).items() if row["decision"] == "include"}
    # A record decided last in the separate context is left out whatever its decision.
    unscreened = builder_visible(ws, development - included)
    if unscreened:
        lines.append(f"- In a development set with no include decision: {_pmids(unscreened)}")
    lines.append(_next("known-records", protocol.get("depth")))
    return "Summary", lines


def _allocation_text(held: dict | None) -> str:
    """Counts only: the builder never sees which records are reserved."""
    from .interpret import CHOICES, NO_HOLDOUT
    if held is None:
        return "not frozen yet (psb allocate --preview, then psb allocate)"
    units = lambda c: f"{_plural(c['units'], 'unit')} ({_plural(c['records'], 'record')})"  # noqa: E731
    text = f"frozen: {units(held['development'])} for development · {units(held['holdout'])} held out"
    if held["released"]:
        return text + " · released to development for repair"
    reason = CHOICES.get(held.get("choice")) or f"no holdout proposed: {NO_HOLDOUT.get(held.get('reason'), 'not recorded')}"
    text += f" · {reason}"
    if held["stale"]:
        text += f" · stale: {'; '.join(held['stale'])}"
    return text


def _command(entry: dict) -> list[str]:
    """A logged command's words: its canonical words, or those of an older row's argv. A restricted
    invocation's row has no argv in log.jsonl."""
    words = entry.get("command")
    return [str(w) for w in words] if isinstance(words, list) else command_tokens(entry.get("argv"))


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
    commands = [_command(e) for e in ws.log_entries() if e.get("type") == "command"]
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
        lines += [f"- Known-record retrieval: {_recall(latest)}",
                  f"- Missed known records: {_misses(latest)}",
                  f"- Known records lost along the way and not recovered: {_pmids(lost)}"]
    else:
        lines.append(f"- Known-record retrieval: {NOT_MEASURED}")
    lines += [f"- Checks: {_checks(latest)}", _next("test", ws.protocol().get("depth"))]
    return "Summary", lines


def round_kinds(rounds: list[dict]) -> list[str]:
    """revision, closing or verification; closing rounds count afresh in each repair epoch."""
    kinds, closings, epoch = [], 0, 1
    for r in rounds:
        current = r.get("epoch", 1) if type(r.get("epoch", 1)) is int else 1
        if current != epoch:
            epoch, closings = current, 0
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
    lines += _extension_line(ws)
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
                 "Line by line:", "", *_line_table(evaluation), ""]
        if delivery.get("legacy"):
            lines += [f"{delivery['note'].capitalize()}.", "", "Recall against known relevant records:", ""]
            lines += _recall_table(evaluation) if evaluation.get("sets") else ["Recall was not estimated."]
        else:
            # The interpretation stored with the delivery: the same bytes the audit embeds.
            lines += ["Known-record retrieval and the held-out test:", "",
                      *str((manifest.get("holdout") or {}).get("text") or "").split("\n")]
            if evaluation.get("sets"):
                lines += ["", "Development checks:", "", *_recall_table(evaluation)]
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

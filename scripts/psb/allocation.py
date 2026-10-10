"""Allocation: split the eligible reference records into development and held-out units, once.

The pool is every record whose latest screening decision is include, plus every development-set
member, less records not in PubMed by the effective date and records on a comparison list. Records
that share a screening group key are reports of one study and form one unit; a record's key is the
latest one screened for it, so a later decision without a key keeps it in its study. A record without
a key is its own unit, and the study count is then unverified.

A unit is unexposed only if every member was screened only in the separate context and no
builder-facing command ever showed it, or any other report of its study (``reserved.py``). Unknown
exposure is exposure. Exposed units go to development: moving a seen record out of development
cannot make it independent.

    N = eligible units, U = unexposed units
    N < 10 or U = 0 (or quick depth) -> all development
    otherwise H = min((3N + 5) // 10, U) held out

The held-out units are the first H unexposed units ordered by sha256("{seed}:{unit id}"), which,
unlike ``random.sample``, gives the same draw on every Python version. The ten-unit trigger and the
30% fraction are operational defaults, not adequacy thresholds.

allocation.json never changes after the freeze. Later events (late companions, re-binding after an
eligibility or as_of change, release for repair) are appended to allocation-log.jsonl.
"""

from __future__ import annotations

import hashlib

from . import progress, reserved, validation
from .disclosure import DISCLOSURE_VERSION
from .evaluate import cutoff_record
from .interpret import NO_HOLDOUT
from .workspace import (LEGACY_CUTOFF, Workspace, WorkspaceError, append_jsonl, normalize_pmids, now, purpose_of,
                        read_jsonl, write_json)

METHOD = "sha256-order-v1"
TRIGGER = 10
DEVELOPMENT_SET = "development"
CHOICES = ("keep-holdout", "all-development", "proceed-default", "designated")


def holdout_size(n: int, u: int) -> int:
    """H = min(round-half-up(0.3 N), U) when N >= 10 and U > 0; integer arithmetic, no float rounding."""
    return 0 if n < TRIGGER or u <= 0 else min((3 * n + 5) // 10, u)


def order_key(seed: int, unit_id: str) -> str:
    return hashlib.sha256(f"{seed}:{unit_id}".encode("utf-8")).hexdigest()


def eligibility_digest(protocol: dict) -> str:
    return validation.digest(protocol.get("eligibility") or {})


# -- the pool -----------------------------------------------------------------------------------

def _screening_rows(ws: Workspace) -> dict[str, list[dict]]:
    rows: dict[str, list[dict]] = {}
    for row in read_jsonl(ws.root / "screening.jsonl"):
        if str(row.get("pmid", "")).isdigit() and row.get("decision") in progress.DECISIONS:
            rows.setdefault(str(row["pmid"]), []).append(row)
    return rows


def study_keys(ws: Workspace, rows: dict[str, list[dict]] | None = None) -> dict[str, str]:
    """Each record's study: the latest non-empty group key screened for it, in either context. A later
    decision without a key keeps the record in its study (a builder decision rarely repeats the separate
    context's key); a different key moves it."""
    rows = _screening_rows(ws) if rows is None else rows
    found = {}
    for pmid, history in rows.items():
        key = next((r["group"] for r in reversed(history) if r.get("group")), None)
        if key:
            found[pmid] = key
    return found


def routes(ws: Workspace) -> dict[str, dict[str, bool]]:
    """Each PMID's discovery routes (origins), each marked private when only the separate context gave
    it: the candidate batch that showed the record (a batch from the separate context, or one recorded
    before batches were marked, is private), the origin of any development set holding it (the builder's
    own), and the origin the screener recorded (private for a separate-context decision)."""
    found: dict[str, dict[str, bool]] = {}

    def add(pmid: str, names, private: bool) -> None:
        entry = found.setdefault(str(pmid), {})
        for name in names:
            entry[name] = entry.get(name, True) and private

    for batch in progress.batches(ws):
        via = str(batch.get("via") or "")
        links = via.split(":", 1)[1].split(",") if via.startswith("neighbors:") else [via]
        names = {progress.VIA_ORIGIN[l] for l in links if l in progress.VIA_ORIGIN}
        private = bool(batch.get("private")) or batch.get("disclosure_version") != DISCLOSURE_VERSION
        for pmid in batch.get("pmids") or []:
            add(pmid, names, private)
    for data in ws.sets().values():
        if purpose_of(data) == "development":
            role_origin = {"user-supplied"} if data.get("role") == "seed" else set()
            for pmid in data.get("pmids", []):
                add(pmid, set(data.get("origin") or []) | role_origin, False)
    for pmid, rows in _screening_rows(ws).items():
        for row in rows:
            add(pmid, row.get("origin") or [], row.get("context") == "separate")
    return found


def _origins(ws: Workspace) -> dict[str, set[str]]:
    """Each PMID's origins: what the screener recorded, the candidate batch that showed it, and the
    origin of any development set holding it."""
    return {pmid: set(names) for pmid, names in routes(ws).items()}


def pool(ws: Workspace) -> dict:
    """The eligible pool as allocation units, with each unit's exposure. Makes PMID-only NCBI calls."""
    rows = _screening_rows(ws)
    latest = {p: r[-1] for p, r in rows.items()}
    development = ws.set_pmids("development")
    comparison = ws.set_pmids("comparison")
    included = {p for p, row in latest.items() if row["decision"] == "include"}
    candidates = sorted(included | development, key=int)
    on_comparison = [p for p in candidates if p in comparison and p not in development]
    candidates = [p for p in candidates if p not in on_comparison]
    available = ws.pubmed.existing(candidates) if candidates else set()
    unavailable = [p for p in candidates if p not in available]
    members = [p for p in candidates if p in available]
    exposure = reserved.by_pmid(ws)
    origins = _origins(ws)

    def reasons(pmid: str) -> list[str]:
        found = []
        if pmid in development:
            found.append("in a development set")
        history = rows.get(pmid) or []
        if not history:
            found.append("not screened")
        elif any(r.get("context") != "separate" for r in history):
            found.append("screened by the builder")
        for event in exposure.get(pmid, []):
            found.append(f"{event.get('kind')} {'declared' if event.get('declared') else 'shown by psb ' + str(event.get('via'))}")
        return found

    keys = study_keys(ws, rows)
    # A study's reports outside the pool (excluded, uncertain, unavailable, on a comparison list): seeing
    # any of them exposes the study, so its eligible reports cannot be held out as unseen.
    reports: dict[str, list[str]] = {}
    for pmid, key in keys.items():
        reports.setdefault(key, []).append(pmid)

    def companion(pmid: str) -> list[str]:
        found = reasons(pmid) + (["on a comparison list"] if pmid in comparison else [])
        return [f"{reason} (another report of this study)" for reason in found]

    groups: dict[tuple[str, str], list[str]] = {}
    for pmid in members:
        key = keys.get(pmid)
        groups.setdefault(("group", key) if key else ("pmid", pmid), []).append(pmid)
    units = []
    for (kind, key), pmids in groups.items():
        pmids = sorted(pmids, key=int)
        exposed = {p: reasons(p) for p in pmids}
        if kind == "group":
            exposed.update({p: companion(p) for p in sorted(set(reports[key]) - set(pmids), key=int)})
        units.append({
            "id": pmids[0], "members": pmids, "group": key if kind == "group" else None,
            "grouping": "verified" if kind == "group" else "unverified",
            "exposed": any(exposed.values()),
            "exposure": [{"pmid": p, "reasons": r} for p, r in exposed.items() if r],
            "origins": sorted({o for p in pmids for o in origins.get(p, set())}),
            "contexts": sorted({r.get("context") or "builder" for p in pmids for r in rows.get(p, [])}),
            "evidence": sorted({str(r.get("evidence")) for p in pmids for r in rows.get(p, []) if r.get("evidence")}),
        })
    units.sort(key=lambda u: int(u["id"]))
    return {"units": units, "unavailable": unavailable, "on_comparison": on_comparison,
            "unscreened": [p for p in members if p in development and p not in included]}


def _counts(units: list[dict]) -> dict:
    return {"units": len(units), "records": sum(len(u["members"]) for u in units)}


def studies(units: list[dict]) -> int | None:
    """Distinct studies, when every unit's grouping was recorded by the screener; otherwise None."""
    return len(units) if units and all(u["grouping"] == "verified" for u in units) else None


def propose(ws: Workspace, *, seed: int = 1) -> dict:
    """The automatic proposal: which units would be held out, and why none when none would be."""
    found = pool(ws)
    units = found["units"]
    n = len(units)
    unexposed = [u for u in units if not u["exposed"]]
    depth = ws.protocol().get("depth") or "standard"
    h = 0 if depth == "quick" else holdout_size(n, len(unexposed))
    chosen = {u["id"] for u in sorted(unexposed, key=lambda u: order_key(seed, u["id"]))[:h]}
    reason = None
    if not h:
        reason = ("empty" if n == 0 else "quick" if depth == "quick" else "small" if n < TRIGGER else "exposed")
    for unit in units:
        unit["purpose"] = "holdout" if unit["id"] in chosen else "development"
    return {**found, "N": n, "U": len(unexposed), "H": h, "seed": seed, "method": METHOD, "depth": depth,
            "reason": reason, "studies": studies(units),
            "development": _counts([u for u in units if u["purpose"] == "development"]),
            "holdout": _counts([u for u in units if u["purpose"] == "holdout"]), "pool": _counts(units)}


# -- the freeze ---------------------------------------------------------------------------------

def _designate(ws: Workspace, proposal: dict, reserve: list[str]) -> list[dict]:
    """Hold out exactly the records the user designated (and the other reports of their studies)."""
    latest = progress.decisions(ws)
    unscreened = [p for p in reserve if p not in latest]
    if unscreened:
        raise WorkspaceError(f"{len(unscreened)} designated record(s) have no screening decision: screen them in "
                             "the separate context first (psb screen --context separate)")
    removed = []
    keep = set()
    by_member = {p: u for u in proposal["units"] for p in u["members"]}
    for pmid in reserve:
        decision = latest[pmid]["decision"]
        if decision != "include":
            removed.append({"pmid": pmid, "reason": f"screened {decision}"})
        elif pmid not in by_member:
            removed.append({"pmid": pmid, "reason": "not in PubMed by the effective date or on a comparison list"})
        else:
            keep.add(by_member[pmid]["id"])
    for unit in proposal["units"]:
        unit["purpose"] = "holdout" if unit["id"] in keep else "development"
    return removed


def freeze(ws: Workspace, *, choice: str | None = None, seed: int = 1, reserve: list[str] | None = None) -> dict:
    """Freeze the allocation. Without a choice, freezes only when no holdout is proposed."""
    if ws.allocation() is not None:
        raise WorkspaceError("the allocation is already frozen; it never changes (psb holdout-release returns "
                             "held-out records to development)")
    proposal = propose(ws, seed=seed)
    removed: list[dict] = []
    if reserve:
        if proposal["depth"] == "quick":
            raise WorkspaceError("a held-out test is a standard-depth step: ask whether to switch to standard depth "
                                 "(and keep these papers reserved) or to use them for development")
        removed = _designate(ws, proposal, normalize_pmids(reserve))
        choice = "designated"
    elif choice in {"keep-holdout", "proceed-default"}:
        if not proposal["H"]:
            raise WorkspaceError(f"no holdout is proposed ({NO_HOLDOUT[proposal['reason']]}); run psb allocate "
                                 "without a choice to freeze every unit for development")
    elif choice == "all-development":
        for unit in proposal["units"]:
            unit["purpose"] = "development"
    elif choice is None:
        if proposal["H"]:
            raise WorkspaceError("a holdout is proposed: relay psb allocate --preview to the user, then record their "
                                 "choice with --keep-holdout or --all-development (--proceed-default when they asked "
                                 "you not to wait for answers)")
    else:
        raise WorkspaceError(f"unknown choice {choice!r}")
    units = proposal["units"]
    held = [u for u in units if u["purpose"] == "holdout"]
    protocol = ws.protocol()
    # With no holdout proposed there was no choice to make: the reason says why.
    if held or (choice == "all-development" and proposal["H"]):
        made, reason = choice, None
    elif choice == "designated":
        made, reason = choice, "designated-none"
    else:
        made, reason = None, proposal["reason"]
    allocation = {
        "version": 1, "method": METHOD, "seed": seed, "created": now(), "depth": proposal["depth"],
        "choice": made, "reason": reason,
        "N": proposal["N"], "U": proposal["U"], "H": len(held), "proposed_H": proposal["H"],
        "studies": proposal["studies"], "units": units,
        "excluded": {"unavailable": proposal["unavailable"], "on_comparison": proposal["on_comparison"],
                     "designated_removed": removed},
        "bindings": {"eligibility_sha256": eligibility_digest(protocol), "as_of": ws.pubmed.as_of,
                     **cutoff_record(ws.pubmed),
                     "policy_version": validation.POLICY_VERSION,
                     "screening_rows": len(read_jsonl(ws.root / "screening.jsonl")),
                     "exposure_rows": len(reserved.events(ws))},
    }
    write_json(ws.root / "allocation.json", allocation)
    development = [p for u in units if u["purpose"] == "development" for p in u["members"]]
    _add_development(ws, development, "psb allocate")
    ws.log({"type": "allocation", "N": allocation["N"], "U": allocation["U"], "H": allocation["H"],
            "choice": allocation["choice"]})
    return allocation


def _add_development(ws: Workspace, pmids: list[str], source: str) -> None:
    """Put records into the development set unless a development set already holds them."""
    already = ws.set_pmids("development")
    new = [p for p in pmids if p not in already]
    if not new:
        return
    existing = ws.get_set(DEVELOPMENT_SET) if ws.set_path(DEVELOPMENT_SET).exists() else None
    if existing is not None and purpose_of(existing) != "development":
        raise WorkspaceError(f"set {DEVELOPMENT_SET!r} exists with another purpose; rename it first")
    current = list(existing["pmids"]) if existing else []
    ws.save_set(DEVELOPMENT_SET, "development", current + [p for p in new if p not in current],
                source=(existing or {}).get("source") or source, note=(existing or {}).get("note", ""),
                origin=(existing or {}).get("origin") or [])


# -- after the freeze ---------------------------------------------------------------------------

def bindings(ws: Workspace, allocation: dict) -> dict:
    """The current eligibility and as_of bindings: the freeze's, updated by any re-binding."""
    current = dict(allocation.get("bindings") or {})
    for event in ws.allocation_events():
        if event.get("type") == "rebind":
            current.update(eligibility_sha256=event.get("eligibility_sha256"), as_of=event.get("as_of"))
            current.pop("as_of_field", None)
            current.update({k: v for k, v in event.items() if k == "as_of_field"})
    return current


def stale(ws: Workspace, allocation: dict) -> list[str]:
    """Why the reserved records no longer match the scope they were screened against."""
    bound = bindings(ws, allocation)
    found = []
    if bound.get("eligibility_sha256") != eligibility_digest(ws.protocol()):
        found.append("eligibility changed after the allocation was frozen")
    if (bound.get("as_of") or None) != (ws.pubmed.as_of or None):
        found.append("the effective date (as_of) changed after the allocation was frozen")
    elif ws.pubmed.as_of and (bound.get("as_of_field") or LEGACY_CUTOFF) != ws.pubmed.as_of_field:
        # Records available by the date were decided on the bound field: another field changes the pool.
        found.append(f"the effective date's field changed after the allocation was frozen "
                     f"({bound.get('as_of_field') or LEGACY_CUTOFF}, now {ws.pubmed.as_of_field})")
    return found


def state(ws: Workspace) -> dict | None:
    """The allocation as it stands now: frozen units, removals, late companions and release."""
    allocation = ws.allocation()
    if allocation is None:
        return None
    events = ws.allocation_events()
    removed = {str(p): e.get("reasons", {}).get(str(p), "re-screened") for e in events if e.get("type") == "rebind"
               for p in e.get("removed", [])}
    late = [e for e in events if e.get("type") == "late-companion"]
    release = ws.released()
    units = allocation["units"]
    held = [u for u in units if u.get("purpose") == "holdout"]
    current = []
    for unit in held:
        members = [p for p in unit["members"] if p not in removed]
        if members:
            current.append({**unit, "members": members})
    return {
        "allocation": allocation, "sha256": validation.digest(allocation),
        "events_sha256": validation.digest(events), "removed": removed, "late": late, "released": release,
        "held": current, "development": [u for u in units if u.get("purpose") != "holdout"],
        "stale": stale(ws, allocation) if held and not release else [],
    }


def late_companions(ws: Workspace, pmids: list[str]) -> list[str]:
    """Records that report a reserved study. They are kept out of development, never mined and left out
    of the frozen denominators; a companion the builder has seen exposes its study."""
    allocation = ws.allocation()
    if allocation is None or ws.released():
        return []
    groups = {u.get("group"): u for u in allocation["units"] if u.get("purpose") == "holdout" and u.get("group")}
    if not groups:
        return []
    rows = _screening_rows(ws)
    keys = study_keys(ws, rows)
    exposure = reserved.by_pmid(ws)
    already = {str(e.get("pmid")) for e in ws.allocation_events() if e.get("type") == "late-companion"}
    found = []
    for pmid in pmids:
        group = keys.get(pmid)
        unit = groups.get(group) if group else None
        if unit is None or pmid in unit["members"]:
            continue
        found.append(pmid)
        if pmid in already:
            continue
        seen = any(r.get("context") != "separate" for r in rows.get(pmid, [])) or pmid in exposure
        append_jsonl(ws.root / "allocation-log.jsonl", {"type": "late-companion", "pmid": pmid, "unit": unit["id"],
                                                        "group": group, "exposed": seen, "at": now()})
    return found


def rebind(ws: Workspace) -> dict:
    """After an eligibility or as_of change: drop reserved records the separate context no longer includes
    or that are not in PubMed by the new date. Every reserved record must have been re-screened in the
    separate context after the freeze. Removals are disclosed; nothing is ever added."""
    current = state(ws)
    if current is None or not current["held"] or current["released"]:
        raise WorkspaceError("no reserved records to re-bind")
    if not current["stale"]:
        raise WorkspaceError("the allocation still matches the eligibility criteria and effective date")
    rows = read_jsonl(ws.root / "screening.jsonl")
    after = rows[int(current["allocation"]["bindings"].get("screening_rows") or 0):]
    latest = {}
    for row in after:
        if str(row.get("pmid", "")).isdigit() and row.get("context") == "separate":
            latest[str(row["pmid"])] = row
    members = [p for u in current["held"] for p in u["members"]]
    missing = [p for p in members if p not in latest]
    if missing:
        raise WorkspaceError(f"{len(missing)} reserved record(s) were not re-screened in the separate context "
                             "after the change; screen them against the current criteria first")
    available = ws.pubmed.existing(members)
    reasons = {}
    for pmid in members:
        if latest[pmid]["decision"] != "include":
            reasons[pmid] = f"re-screened {latest[pmid]['decision']} against the revised criteria"
        elif pmid not in available:
            reasons[pmid] = "not in PubMed by the revised effective date"
    event = {"type": "rebind", "removed": sorted(reasons, key=int), "reasons": reasons,
             "eligibility_sha256": eligibility_digest(ws.protocol()), "as_of": ws.pubmed.as_of,
             **cutoff_record(ws.pubmed), "at": now()}
    append_jsonl(ws.root / "allocation-log.jsonl", event)
    return event


def release(ws: Workspace, reason: str) -> dict:
    """Return the held-out records to development for a repair. The receipts are kept."""
    if not str(reason or "").strip():
        raise WorkspaceError("give the reason for releasing the held-out records")
    current = state(ws)
    if current is None or not current["held"]:
        raise WorkspaceError("there are no held-out records to release")
    if current["released"]:
        raise WorkspaceError("the held-out records were already released")
    from .holdout import receipts
    numbers = [r["number"] for r in receipts(ws)]
    members = [p for u in current["held"] for p in u["members"]] + [str(e["pmid"]) for e in current["late"]]
    event = {"type": "release", "reason": reason.strip(), "receipts": numbers, "members": members, "at": now()}
    append_jsonl(ws.root / "allocation-log.jsonl", event)
    _add_development(ws, members, "released from the held-out test")
    return event


def summary(ws: Workspace) -> dict | None:
    """Counts only: safe to show the builder."""
    current = state(ws)
    if current is None:
        return None
    allocation = current["allocation"]
    held = current["held"]
    return {"N": allocation["N"], "U": allocation["U"], "H": len(held), "choice": allocation.get("choice"),
            "reason": allocation.get("reason"),
            "development": _counts(current["development"]), "holdout": _counts(held),
            "released": bool(current["released"]), "stale": current["stale"], "late_companions": len(current["late"])}

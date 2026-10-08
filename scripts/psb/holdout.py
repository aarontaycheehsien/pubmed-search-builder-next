"""The held-out test: one retrieval check of the frozen query against the reserved records.

It runs after the development checks and a current critic review, and once per binding:

    query, strategy, review_sha256, as_of, allocation, held-out membership, eligibility,
    policy version and template version

A repeat run with the same binding returns the stored receipt. A new receipt is allowed only when the
binding changed for a reason other than a strategy edit (PubMed's translation or the vocabulary
drifted). After a receipt, a changed strategy is refused until ``psb holdout-release``: a query
revised after seeing the result cannot claim the test. Every receipt is kept.

    holdout/receipt-N.json   status complete, empty (no reserved record in PubMed by the effective
                             date) or incomplete (a service failure: no counts are stored or shown)
"""

from __future__ import annotations

import json

from . import allocation, interpret, progress, reserved, validation
from .ncbi import NcbiError
from .workspace import Workspace, WorkspaceError, now, read_json, write_json


def receipts(ws: Workspace) -> list[dict]:
    found = []
    for path in (ws.root / "holdout").glob("receipt-*.json"):
        data = read_json(path)
        if isinstance(data, dict) and isinstance(data.get("number"), int):
            found.append(data)
    return sorted(found, key=lambda r: r["number"])


def receipt_path(ws: Workspace, number: int):
    return ws.root / "holdout" / f"receipt-{number}.json"


def receipt_digest(ws: Workspace, number: int) -> str:
    return validation.digest(read_json(receipt_path(ws, number)))


def held_members(state: dict) -> list[str]:
    return sorted({p for u in state["held"] for p in u["members"]}, key=int)


def binding(evaluation: dict, state: dict, protocol: dict) -> dict:
    return {
        "query": evaluation.get("query"),
        "strategy_sha256": validation.digest(evaluation["inputs"]["strategy"]),
        "review_sha256": evaluation.get("review_sha256"),
        "as_of": evaluation.get("as_of"),
        "allocation_sha256": state["sha256"],
        "holdout_sha256": validation.digest(held_members(state)),
        "eligibility_sha256": allocation.eligibility_digest(protocol),
        "policy_version": validation.POLICY_VERSION,
        "template_version": interpret.TEMPLATE_VERSION,
    }


def _ready(ws: Workspace) -> tuple[dict, dict]:
    """The allocation state and the evaluation the test would rest on, or a refusal saying what is missing."""
    from .deliver import latest_evaluation, review_gate
    state = allocation.state(ws)
    if state is None:
        raise WorkspaceError("freeze the allocation first (psb allocate)")
    if state["released"]:
        raise WorkspaceError("the held-out records were released for repair; this query has no held-out test")
    if not state["held"]:
        raise WorkspaceError("no records are held out, so there is no held-out test to run")
    if state["stale"]:
        raise WorkspaceError(f"{'; '.join(state['stale'])}: re-screen the reserved records in the separate context, "
                             "then psb allocate --rebind")
    evaluation = latest_evaluation(ws)
    if not evaluation["validation"]["complete"] or evaluation["validation"]["blockers"]:
        raise WorkspaceError("run a complete psb eval with no technical blockers before the held-out test")
    gate = review_gate(ws, evaluation)
    if gate["blockers"]:
        codes = ", ".join(sorted({b["code"] for b in gate["blockers"]}))
        raise WorkspaceError(f"finish the critic review of the current evaluation before the held-out test ({codes})")
    return state, evaluation


def run(ws: Workspace) -> dict:
    """Run the held-out test once for the current binding and store its receipt."""
    state, evaluation = _ready(ws)
    bind = binding(evaluation, state, ws.protocol())
    existing = receipts(ws)
    for receipt in reversed(existing):
        if receipt.get("binding") == bind and receipt.get("status") in {"complete", "empty"}:
            return {**receipt, "repeat": True}
    tested = [r for r in existing if r.get("status") in {"complete", "empty"}]
    if any(r["binding"].get("strategy_sha256") != bind["strategy_sha256"] for r in tested):
        raise WorkspaceError("the strategy changed after the held-out test; a query revised after seeing the result "
                             "cannot claim it. To repair the search, psb holdout-release --reason \"...\"")
    members = held_members(state)
    receipt = {"number": (existing[-1]["number"] + 1) if existing else 1, "created": now(), "binding": bind,
               "choice": state["allocation"].get("choice")}
    cache = ws.pubmed.cache
    enabled = cache.enabled
    cache.enabled = False  # a live check, like psb report
    try:
        in_pubmed = ws.pubmed.existing(members)
        retrieved = ws.pubmed.among(evaluation["query"], in_pubmed) & in_pubmed if in_pubmed else set()
    except (NcbiError, ValueError) as exc:
        receipt.update(status="incomplete", reason=f"the PubMed check did not complete ({exc})")
    else:
        receipt.update(_result(ws, state, in_pubmed, retrieved, members))
    finally:
        cache.enabled = enabled
    write_json(receipt_path(ws, receipt["number"]), receipt)
    ws.log({"type": "holdout-test", "receipt": receipt["number"], "status": receipt["status"]})
    return receipt


def _result(ws: Workspace, state: dict, in_pubmed: set[str], retrieved: set[str], members: list[str]) -> dict:
    held = state["held"]
    verified = all(u.get("grouping") == "verified" for u in held)
    units = [u for u in held if set(u["members"]) & in_pubmed]
    return {
        "status": "complete" if in_pubmed else "empty",
        "records": {"eligible": len(in_pubmed), "retrieved": len(retrieved),
                    "missed": sorted(in_pubmed - retrieved, key=int),
                    "unavailable": sorted(set(members) - in_pubmed, key=int)},
        "studies": ({"eligible": len(units), "retrieved": sum(1 for u in units if set(u["members"]) & retrieved)}
                    if verified else None),
        "distinct_studies": verified and all(len(set(u["members"]) & in_pubmed) == 1 for u in units),
        "units": [{"id": u["id"], "members": u["members"], "retrieved": sorted(set(u["members"]) & retrieved, key=int),
                   "origins": u.get("origins") or [], "grouping": u.get("grouping")} for u in held],
        "exposure": _exposure(ws, state),
        "development": {"units": len(state["development"]),
                        "records": sum(len(u["members"]) for u in state["development"])},
        "holdout": {"units": len(held), "records": len(members)},
        "removed": state["removed"],
    }


def _exposure(ws: Workspace, state: dict) -> list[dict]:
    """Every held-out unit's recorded exposure: before the reservation, after it, and through a late
    companion the builder saw."""
    after = reserved.events(ws)[int(state["allocation"]["bindings"].get("exposure_rows") or 0):]
    rows = []
    for unit in state["held"]:
        reasons = [f"PMID {e['pmid']}: {', '.join(e['reasons'])}" for e in unit.get("exposure") or []]
        for event in after:
            if str(event["pmid"]) in unit["members"]:
                how = "declared" if event.get("declared") else f"shown by psb {event.get('via')}"
                reasons.append(f"PMID {event['pmid']}: {event.get('kind')} {how} after the reservation")
        for late in state["late"]:
            if late.get("unit") == unit["id"] and late.get("exposed"):
                reasons.append(f"PMID {late['pmid']}: a later report of this study was seen by the builder")
        if reasons:
            rows.append({"unit": unit["id"], "reasons": reasons})
    return rows


def matching(ws: Workspace, evaluation: dict, state: dict) -> tuple[dict | None, str | None]:
    """The receipt a delivery of ``evaluation`` rests on, or the blocker code saying why there is none."""
    bind = binding(evaluation, state, ws.protocol())
    found = receipts(ws)
    for receipt in reversed(found):
        if receipt.get("binding") == bind and receipt.get("status") in {"complete", "empty"}:
            return receipt, None
    if not found:
        return None, "holdout_test_missing"
    tested = [r for r in found if r.get("status") in {"complete", "empty"}]
    if any(r["binding"].get("strategy_sha256") != bind["strategy_sha256"] for r in tested):
        return None, "holdout_strategy_changed"
    if found[-1].get("status") == "incomplete":
        return None, "holdout_test_incomplete"
    return None, "holdout_test_stale"


def released_receipt(ws: Workspace) -> dict | None:
    """The last complete receipt before a release: the result that applies to the earlier query."""
    release = ws.released()
    if not release:
        return None
    numbers = set(release.get("receipts") or [])
    tested = [r for r in receipts(ws) if r["number"] in numbers and r.get("status") == "complete"]
    return tested[-1] if tested else None


def message(ws: Workspace, receipt: dict | None = None, evaluation: dict | None = None) -> dict:
    """The fixed interpretation for the current state; ``receipt`` defaults to the one that applies."""
    state = allocation.state(ws)
    if state is not None and state["released"]:
        receipt = released_receipt(ws)
    comparison = interpret.comparison_rows(evaluation or {})
    return interpret.render(state, receipt, comparison=comparison)


def records_section(ws: Workspace, receipt: dict) -> list[str]:
    """After the test: each held-out record with its screening reason and source, for the peer reviewer."""
    private = progress.private_decisions(ws)
    retrieved = {p for u in receipt.get("units") or [] for p in u.get("retrieved") or []}
    rows = ["| PMID | Unit | Retrieved | Origins | Screening reason | Source |", "|---|---|---|---|---|---|"]
    for unit in receipt.get("units") or []:
        for pmid in unit["members"]:
            detail = private.get(pmid, {})
            cell = lambda value: progress.clean(value, 160).replace("|", "\\|") or "not recorded"  # noqa: E731
            state = ("yes" if pmid in retrieved else "not in PubMed by the date"
                     if pmid in (receipt.get("records") or {}).get("unavailable", []) else "no")
            rows.append(f"| {pmid} | {unit['id']} | {state} | {', '.join(unit.get('origins') or []) or 'not recorded'} | "
                        f"{cell(detail.get('reason'))} | {cell(detail.get('source_ref'))} |")
    return rows


def dump(receipt: dict) -> str:
    return json.dumps(receipt, indent=2, ensure_ascii=False)

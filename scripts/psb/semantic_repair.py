"""Evidence for a semantic repair: decisions, measured delta and budgeted screening.

These records support human/critic judgement; a nonempty explanation is not proof of
generalisability. No command here changes the Boolean strategy or the held-out allocation.
"""
from __future__ import annotations

import json

from . import progress, reserved, validation
from .miss_hunt import PRIVATE, RECEIPT, _known_protected
from .strategy import full_query
from .workspace import WorkspaceError, read_json, read_jsonl, write_json, now

DECISIONS = "semantic-repair-decisions.json"
CHECK = "semantic-repair-check.json"
CAUSES = {"vocabulary", "structure", "limit", "searchable-information"}


def _receipt(ws):
    return read_json(ws.root / RECEIPT)


def _selected(ws):
    return {r["pmid"] for r in _receipt(ws)["candidates"]} - _known_protected(ws)


def _eligible(ws):
    screened = progress.decisions(ws)
    return {p for p in _selected(ws) if screened.get(p, {}).get("decision") == "include"}


def _before_test(ws):
    if list((ws.root / "holdout").glob("*.json")) or ws.released():
        raise WorkspaceError("record semantic repair evidence before the held-out test")


def save_decisions(ws, data):
    _before_test(ws)
    if not isinstance(data, dict) or not isinstance(data.get("decisions"), list):
        raise WorkspaceError("repair decisions must be an object containing a decisions list")
    rows, seen = [], set()
    eligible = _eligible(ws)
    for row in data["decisions"]:
        if not isinstance(row, dict):
            raise WorkspaceError("each repair decision must be an object")
        pmid = str(row.get("pmid", ""))
        if pmid not in eligible or pmid in seen:
            raise WorkspaceError("repair decisions must name each confirmed eligible candidate exactly once")
        seen.add(pmid)
        if row.get("diagnosis") not in CAUSES or row.get("disposition") not in {"repair", "retain-miss"}:
            raise WorkspaceError("give a vocabulary/structure/limit/searchable-information diagnosis and repair/retain-miss disposition")
        if not isinstance(row.get("rationale"), str) or not row["rationale"].strip():
            raise WorkspaceError("every repair or retained miss needs a rationale")
        evidence = row.get("evidence")
        if not isinstance(evidence, list) or not evidence or any(not isinstance(s, str) or not s.strip() for s in evidence):
            raise WorkspaceError("every decision needs a nonempty list of evidence references")
        if (row["diagnosis"] == "vocabulary" and row["disposition"] == "repair"
                and (not isinstance(row.get("general_concept"), str) or not row["general_concept"].strip())):
            raise WorkspaceError("vocabulary repairs need a general_concept, not just a distinctive phrase")
        rows.append({k: row.get(k) for k in ("pmid", "diagnosis", "disposition", "rationale", "evidence", "general_concept")})
        rows[-1]["pmid"] = pmid
    if seen != eligible:
        raise WorkspaceError("record a diagnosis for every confirmed eligible candidate")
    result = {"version": 1, "receipt_sha256": validation.digest(_receipt(ws)), "decisions": rows,
              "known_loss_rationale": str(data.get("known_loss_rationale") or "").strip(),
              "sampling_limitation": str(data.get("sampling_limitation") or "").strip()}
    write_json(ws.root / DECISIONS, result)
    return {"ok": True, "recorded": len(rows), "next": "make justified edits, then miss-hunt --check-repair"}


def check_repair(ws, *, sample_size=5):
    _before_test(ws)
    if not 0 <= sample_size <= 10:
        raise WorkspaceError("incremental screening sample must be between 0 and 10")
    receipt = _receipt(ws)
    selected, eligible = _selected(ws), _eligible(ws)
    screened = progress.decisions(ws)
    if selected - screened.keys():
        raise WorkspaceError("screen the queued candidates before checking the repair")
    if eligible - ws.set_pmids("development"):
        raise WorkspaceError("add confirmed eligible misses to development before checking the repair")
    decisions = read_json(ws.root / DECISIONS) if (ws.root / DECISIONS).exists() else None
    if eligible and (not decisions or {r["pmid"] for r in decisions["decisions"]} != eligible):
        raise WorkspaceError("record repair decisions for every confirmed eligible miss first")
    if decisions and decisions["receipt_sha256"] != validation.digest(receipt):
        raise WorkspaceError("repair decisions refer to a different discovery receipt")
    strategy = ws.strategy()
    strategy.validate()
    current = full_query(strategy)
    baseline = receipt["query"]
    delta = f"({current}) NOT ({baseline})"
    binding = {"strategy_sha256": validation.digest(strategy.to_dict()), "as_of": ws.pubmed.as_of,
               "as_of_field": ws.pubmed.as_of_field, "receipt_sha256": validation.digest(receipt),
               "decisions_sha256": validation.digest(decisions), "sample_size": sample_size}
    binding["protocol_sha256"] = validation.digest(validation.review_inputs({"protocol": ws.protocol()})["protocol"])
    if (binding["as_of"], binding["as_of_field"]) != (receipt["as_of"], receipt["as_of_field"]):
        raise WorkspaceError("repair cutoff differs from discovery")
    pending = ws.root / PRIVATE / "repair-pending.json"
    if pending.exists():
        result = read_json(pending)
        if result["binding"] != binding:
            # New strategy/decisions need a new measurement, not reuse of an earlier delta.
            result = None
    else:
        result = None
    if result is None:
        total_budget = progress.screening_budget(ws)
        remaining = max(0, total_budget - len(screened))
        limit = min(sample_size, remaining)
        pm = ws.pubmed
        added = pm.search(delta, retmax=0)
        if any(i.get("severity") == "error" for i in added.get("issues", [])):
            raise WorkspaceError("PubMed rejected the incremental retrieval query")
        hidden = _known_protected(ws)
        omit = selected | set(screened) | hidden | ws.set_pmids("development", "comparison")
        page = pm.search(delta, retmax=limit + len(omit)) if limit and added["count"] else {"pmids": []}
        if any(i.get("severity") == "error" for i in page.get("issues", [])):
            raise WorkspaceError("PubMed rejected the incremental screening sample")
        sample = list(dict.fromkeys(p for p in page["pmids"] if p not in omit))[:limit]
        development = ws.set_pmids("development") - hidden
        before = pm.among(baseline, development)
        after = pm.among(current, development)
        counts = [pm.search(q, retmax=0) for q in (baseline, current)]
        if any(i.get("severity") == "error" for r in counts for i in r.get("issues", [])):
            raise WorkspaceError("PubMed rejected the baseline or revised retrieval count")
        result = {"version": 1, "binding": binding, "checked_at": now(), "query": current, "delta_query": delta,
                  "baseline_count": counts[0]["count"], "revised_count": counts[1]["count"],
                  "incremental_count": added["count"], "known_lost": sorted(before - after, key=int),
                  "confirmed_retrieved": sorted(eligible & after, key=int), "sample_pmids": sample,
                  "remaining_budget_at_check": remaining, "sample_limit": limit}
        write_json(pending, result)
    sample = result["sample_pmids"]
    if set(sample) & _known_protected(ws):
        raise WorkspaceError("protection changed during interrupted repair check; no sample can be exposed")
    reserved.refuse(ws, sample, "incremental screening")
    key = "semantic-repair-" + validation.digest(result["binding"])
    if sample:
        progress.record_batch(ws, "semantic-repair", "Semantic repair incremental sample", sample,
                              total=len(sample), event_key=key)
        reserved.record(ws, sample, "feedback", "miss-hunt repair check", event_key=key)
    write_json(ws.root / CHECK, result)
    return {"ok": True, **result, "next": "screen incremental sample PMIDs, then psb eval and critic"}


def evidence(ws):
    """A bounded, builder-safe snapshot used by the critic and delivery manifest."""
    if not (ws.root / RECEIPT).exists() and not (ws.root / PRIVATE / "request.json").exists():
        return None
    receipt = _receipt(ws) if (ws.root / RECEIPT).exists() else None
    decisions = read_json(ws.root / DECISIONS) if (ws.root / DECISIONS).exists() else None
    check = read_json(ws.root / CHECK) if (ws.root / CHECK).exists() else None
    relevant = ({r["pmid"] for r in receipt["candidates"]} if receipt else set()) | set((check or {}).get("sample_pmids", []))
    # Persist all decisions for effort accounting, but never expose newly recognised protected content.
    rows = [r for r in read_jsonl(ws.root / "screening.jsonl") if r.get("pmid") in relevant]
    return {"receipt_sha256": validation.digest(receipt), "decisions_sha256": validation.digest(decisions),
            "check_sha256": validation.digest(check), "screening_sha256": validation.digest(rows)}


def gate(ws):
    """Structural checks, not an automated judgement of the quality of an explanation."""
    if not (ws.root / RECEIPT).exists():
        return []
    receipt = _receipt(ws)
    if receipt.get("version", 1) < 2:
        return []  # legacy receipts remain readable; new runs require the stronger contract
    errors = []
    check = read_json(ws.root / CHECK) if (ws.root / CHECK).exists() else None
    decisions = read_json(ws.root / DECISIONS) if (ws.root / DECISIONS).exists() else None
    eligible = _eligible(ws)
    if not check:
        return [validation.issue("semantic_repair_unchecked", "Run miss-hunt --check-repair before final review")]
    expected = {"strategy_sha256": validation.digest(ws.strategy().to_dict()), "as_of": ws.pubmed.as_of,
                "as_of_field": ws.pubmed.as_of_field, "receipt_sha256": validation.digest(receipt),
                "decisions_sha256": validation.digest(decisions), "sample_size": check["binding"]["sample_size"]}
    expected["protocol_sha256"] = validation.digest(validation.review_inputs({"protocol": ws.protocol()})["protocol"])
    if check["binding"] != expected:
        errors.append(validation.issue("semantic_repair_stale", "Recheck the repair after changing strategy, cutoff or decisions"))
    screened = progress.decisions(ws)
    queued = _selected(ws) | (set(check["sample_pmids"]) - _known_protected(ws))
    if queued - screened.keys():
        errors.append(validation.issue("semantic_screening_pending", "Finish screening the miss-hunt and incremental queues"))
    rows = (decisions or {}).get("decisions", [])
    if eligible != {r["pmid"] for r in rows} or eligible - ws.set_pmids("development"):
        errors.append(validation.issue("semantic_diagnoses_missing", "Every confirmed miss needs a development record and repair disposition"))
    if any(r["disposition"] == "repair" and r["pmid"] not in check["confirmed_retrieved"] for r in rows):
        errors.append(validation.issue("semantic_repair_unretrieved", "A record marked repaired is still missed; revise or retain it with justification"))
    if check["known_lost"] and not (decisions or {}).get("known_loss_rationale"):
        errors.append(validation.issue("semantic_known_loss", "Explain previously retrieved development records lost by the repair"))
    if check["incremental_count"] and not check["sample_pmids"] and not (decisions or {}).get("sampling_limitation"):
        errors.append(validation.issue("semantic_sampling_unexplained", "Explain why no new incremental records could be screened within budget"))
    if len(screened) > progress.screening_budget(ws):
        errors.append(validation.issue("semantic_budget_exceeded", "The experiment exceeded its shared screening allowance"))
    return errors


def summary(ws):
    check = read_json(ws.root / CHECK) if (ws.root / CHECK).exists() else None
    if not check:
        return {"checked": False}
    screened = progress.decisions(ws)
    visible = set(check["sample_pmids"]) - _known_protected(ws)
    return {"checked": True, "baseline_count": check["baseline_count"], "revised_count": check["revised_count"],
            "incremental_count": check["incremental_count"], "known_lost_count": len(check["known_lost"]),
            "sampled": len(visible), "sample_outcomes": {d: sum(screened.get(p, {}).get("decision") == d for p in visible)
                                                       for d in progress.DECISIONS}}


def critic_lines(ws):
    if not (ws.root / RECEIPT).exists():
        return []
    hidden = _known_protected(ws)
    decisions = read_json(ws.root / DECISIONS) if (ws.root / DECISIONS).exists() else {}
    safe = {**decisions, "decisions": [r for r in decisions.get("decisions", []) if r["pmid"] not in hidden]}
    return ["", "## Semantic repair evidence", "",
            "Assess whether the proposed concept generalises and whether added retrieval is justified. "
            "Recorded explanations are claims to review, not automatic proof.", "", "```json",
            json.dumps({"decisions": safe, "measurement": summary(ws)}, indent=2), "```", ""]

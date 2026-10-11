"""One optional Step 5 counterexample batch; never changes the query or allocation.

The private archive may contain reserved identifiers. Only the filtered receipt is public.
Failed rounds resume their frozen requests; completed rounds cannot be repeated in a build.
"""
from __future__ import annotations

import json
import os
import re
import time

from . import allocation, progress, reserved, validation
from .evaluate import effective_query
from .openalex import OpenAlex
from .strategy import full_query
from .workspace import Workspace, WorkspaceError, now, read_json, read_jsonl, write_json

RECEIPT = "semantic-miss-hunt.json"
PRIVATE = "screening/semantic-miss-hunt"
MAX_QUERIES, MAX_RESULTS, MAX_SCREEN = 3, 50, 30


def _binding(ws):
    return {"strategy": ws.strategy().to_dict(), "protocol": ws.protocol(),
            "as_of": ws.pubmed.as_of, "as_of_field": ws.pubmed.as_of_field,
            "allocation": validation.digest(ws.allocation()),
            "sets": validation.digest(ws.sets())}


def _protected(ws, pmids):
    # Recognise known companions before any content or retrieval feedback is emitted.
    return ws.reserved_pmids() | set(allocation.late_companions(ws, list(pmids)))


def _known_protected(ws):
    """Read-only protection for summaries, including companions not yet offered to a set."""
    hidden = ws.reserved_pmids()
    if ws.released():
        return hidden
    groups = {u.get("group") for u in (ws.allocation() or {}).get("units", [])
              if u.get("purpose") == "holdout" and u.get("group")}
    return hidden | {p for p, key in allocation.study_keys(ws).items() if key in groups}


def _resolve(pm, row):
    ids = row.get("ids") if isinstance(row.get("ids"), dict) else {}
    value = str(ids.get("pmid") or "")
    match = re.fullmatch(r"(?:https?://(?:pubmed\.ncbi\.nlm\.nih\.gov/|www\.ncbi\.nlm\.nih\.gov/pubmed/))?0*([1-9][0-9]*)/?", value)
    if match:
        return match[1]
    doi = str(ids.get("doi") or row.get("doi") or "").strip()
    doi = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", doi, flags=re.I)
    # Never turn arbitrary provider text into a PubMed query.
    if not re.fullmatch(r'10\.[0-9]{4,9}/[^\s"\[\]]+', doi):
        return None
    hits = pm.search(f'"{doi}"[doi]', retmax=2)["pmids"]
    return hits[0] if len(hits) == 1 else None


def run(ws: Workspace, queries: list[str], *, limit: int = MAX_SCREEN,
        per_query: int = MAX_RESULTS, client=None) -> dict:
    if (not isinstance(queries, list) or not 1 <= len(queries) <= MAX_QUERIES
            or any(not isinstance(q, str) or not q.strip() or len(q) > 2000 for q in queries)):
        raise WorkspaceError("provide one to three nonempty semantic queries, each at most 2000 characters")
    queries = [q.strip() for q in queries]
    if len(set(queries)) != len(queries):
        raise WorkspaceError("semantic queries must be distinct")
    if not 1 <= limit <= MAX_SCREEN or not 1 <= per_query <= MAX_RESULTS:
        raise WorkspaceError("miss hunting permits 1–30 screenings and 1–50 results per query")
    if ws.allocation() is None:
        raise WorkspaceError("miss hunting is Step 5 only: freeze the allocation first")
    if ws.pubmed.as_of and ws.pubmed.as_of_field != "crdt":
        raise WorkspaceError("retrospective semantic discovery requires a Create Date cutoff; use a new workspace")
    if list((ws.root / "holdout").glob("*.json")) or ws.released():
        raise WorkspaceError("miss hunting must finish before the held-out test or release for repair")
    if allocation.state(ws)["stale"]:
        raise WorkspaceError("the allocation is stale; resolve its scope/cutoff binding first")
    for query in queries:
        reserved.check_query(ws, query)
    ws.strategy().validate()
    versions = ws.versions()
    if (not versions or not versions[-1]["evaluation"].get("ok")
            or versions[-1]["evaluation"].get("input_sha256") != validation.digest(validation.input_snapshot(ws))):
        raise WorkspaceError("run psb eval on the current strategy and inputs before miss hunting")
    path = ws.root / RECEIPT
    if path.exists():
        raise WorkspaceError("this build already completed its one miss-hunt batch; use --summary")
    lock = ws.root / ".miss-hunt.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise WorkspaceError("miss hunt already running or interrupted; inspect .miss-hunt.lock before retrying") from None
    try:
        os.write(fd, f"pid={os.getpid()} started={now()}".encode())
        os.close(fd)
        if path.exists():
            raise WorkspaceError("this build already completed its one miss-hunt batch; use --summary")
        return _run(ws, queries, limit, per_query, client or OpenAlex())
    finally:
        lock.unlink(missing_ok=True)


def _run(ws, queries, limit, per_query, client):
    private = ws.root / PRIVATE
    request = {"queries": queries, "limit": limit, "per_query": per_query, "binding": _binding(ws)}
    state_path = private / "request.json"
    if state_path.exists():
        if read_json(state_path)["request"] != request:
            raise WorkspaceError("interrupted miss hunt is bound to its original queries, strategy and cutoff")
    else:
        write_json(state_path, {"request": request, "started_at": now()})
    screened = progress.decisions(ws)
    remaining = max(0, progress.SCREEN_BUDGET.get(ws.protocol().get("depth"), 150) - len(screened))
    if not remaining:
        raise WorkspaceError("the build screening budget is exhausted; reserve allowance before Step 5")
    limit = min(limit, remaining)
    started = time.monotonic()
    archives = []
    for index, query in enumerate(queries):
        archive = private / f"response-{index + 1}.json"
        if archive.exists():
            entry = read_json(archive)
            if (entry.get("query") != query
                    or entry.get("response_sha256") != validation.digest(entry.get("response"))):
                raise WorkspaceError("archived semantic response failed its query/hash check")
        else:
            response = client.search(query, per_query)
            entry = {"query": query, "fetched_at": now(), "response": response,
                     "response_sha256": validation.digest(response)}
            write_json(archive, entry)
        archives.append(entry)
    # Round-robin across prompts, retaining all provenance for duplicate PMIDs.
    candidates, unresolved, returned = {}, 0, 0
    for rank in range(per_query):
        for index, entry in enumerate(archives):
            rows = entry["response"]["results"]
            if rank >= len(rows):
                continue
            row = rows[rank]
            returned += 1
            pmid = _resolve(ws.pubmed, row)
            if pmid is None:
                unresolved += 1
                continue
            candidates.setdefault(pmid, []).append({"query": index + 1, "rank": rank + 1,
                                                    "work_id": row.get("id")})
    hidden = _protected(ws, candidates)
    visible = [p for p in candidates if p not in hidden]
    known = set(screened) | ws.set_pmids("development", "comparison")
    fresh = [p for p in visible if p not in known]
    available = ws.pubmed.existing(fresh)
    query = full_query(ws.strategy())
    retrieved = ws.pubmed.among(query, available)
    misses = [p for p in fresh if p in available and p not in retrieved]
    # A failing PubMed call raises: it must never be treated as an empty retrieval set.
    current = _binding(ws)
    if current != request["binding"]:
        raise WorkspaceError("workspace inputs changed during miss hunting; no candidates were exposed")
    if progress.decisions(ws) != screened:
        raise WorkspaceError("screening changed during miss hunting; retry to recalculate the remaining budget")
    hidden = _protected(ws, misses)
    selected = [p for p in misses if p not in hidden][:limit]
    receipt = {"version": 1, "provider": "openalex-semantic", "completed_at": now(),
               "query": effective_query(query, ws.pubmed.as_of, ws.pubmed.as_of_field),
               "strategy_sha256": validation.digest(ws.strategy().to_dict()),
               "as_of": ws.pubmed.as_of, "as_of_field": ws.pubmed.as_of_field,
               "queries": queries, "per_query": per_query, "screening_limit": limit,
               "responses": [{k: e[k] for k in ("query", "fetched_at", "response_sha256")} for e in archives],
               "counts": {"returned": returned, "unresolved": unresolved,
                          "already_known": len(set(visible) & known),
                          "unavailable_at_cutoff": len(set(fresh) - available),
                          "available_new": len(available), "already_retrieved": len(retrieved),
                          "candidate_misses": len(misses), "queued": len(selected)},
               "candidates": [{"pmid": p, "sources": candidates[p]} for p in selected],
               "seconds_this_attempt": round(time.monotonic() - started, 3),
               "provider_cost_usd": None,
               "note": "Current semantic index and PubMed metadata, restricted to date-eligible records; "
                       "not a historical snapshot or an estimate of absolute recall."}
    if selected:
        progress.record_batch(ws, "semantic-miss", "Semantic miss hunting", selected, total=len(selected))
        reserved.record(ws, selected, "feedback", "miss-hunt")
    write_json(ws.root / RECEIPT, receipt)
    ws.log({"type": "semantic-miss-hunt", "strategy_sha256": receipt["strategy_sha256"],
            "queued": len(selected)})
    return {"ok": True, **receipt, "next": "Fetch and screen queued PMIDs. Add confirmed eligible records to "
            "development only, diagnose with psb eval and psb terms miss, then justify any revision."}


def summary(ws: Workspace) -> dict:
    path = ws.root / RECEIPT
    if not path.exists():
        return {"performed": False, "attempted": (ws.root / PRIVATE / "request.json").exists()}
    receipt = read_json(path)
    selected = {r["pmid"] for r in receipt["candidates"]} - _known_protected(ws)
    decisions = progress.decisions(ws)
    counts = {d: sum(decisions.get(p, {}).get("decision") == d for p in selected) for d in progress.DECISIONS}
    rows = [r for r in read_jsonl(ws.root / "screening.jsonl") if r.get("pmid") in selected]
    return {"performed": True, "strategy_sha256": receipt["strategy_sha256"],
            "counts": receipt["counts"], "screening": counts,
            "awaiting_screening": len(selected - decisions.keys()),
            "confirmed_in_development": sum(decisions.get(p, {}).get("decision") == "include"
                                            for p in selected & ws.set_pmids("development")),
            "screening_decisions": len(rows),
            "full_text_decisions": sum(r.get("evidence") == "full-text" for r in rows),
            "provider_cost_usd": receipt["provider_cost_usd"], "note": receipt["note"]}


def audit_lines(ws):
    data = summary(ws)
    if not data["performed"] and not data.get("attempted"):
        return []
    if not data["performed"]:
        return ["## Experimental semantic miss hunting", "",
                "Attempted but no completed batch was recorded. No discovery or recall conclusion is available.", ""]
    return ["## Experimental semantic miss hunting", "", data["note"], "",
            "Counts and screening outcomes (not recall):", "", "```json",
            json.dumps(data, indent=2), "```", "",
            "Frozen query, semantic prompts, response hashes and candidate provenance: semantic-miss-hunt.json.", ""]

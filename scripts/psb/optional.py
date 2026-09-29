"""Optional concepts: searchable concepts that are tested as an extra AND-ed block, not dropped.

A concept whose role is ``optional`` (typically a topic-defining outcome, setting or design) gets a
candidate block in ``strategy.json`` ``candidates``. Candidates are never part of the query. Every
``psb eval`` measures each one: the count with it AND-ed, the known records it would lose, and the
query for the records it would remove. The agent screens a random loss sample of those removed
records and records a decision on the concept in ``protocol.json``::

    "decision": {"choice": "and" | "leave_out", "reason": "...", "fingerprint": "...",
                 "loss_sample": {"screened": [...], "relevant": [...]}}

``choice: and`` moves the candidate into ``blocks``, where leave-one-block-out ablation keeps
checking it. A decision is current while its fingerprint (the candidate's terms and the query it is
AND-ed to) still matches. Over the workload budget, delivery needs a current decision for every
optional concept.
"""

from __future__ import annotations

import datetime as dt
import json
import random

from . import validation
from .strategy import Block, Strategy, StrategyError, apply_limits, block_query, core_query

DEFAULT_BUDGET = {"quick": None, "standard": 10_000, "thorough": 20_000}
SAMPLE_SIZE = {"quick": 0, "standard": 30, "thorough": 60}
MATERIAL_REDUCTION = 30.0  # percent; the guidance threshold for AND-ing, reported, not enforced
# AND-ing an optional block is only safe when enough known records show it loses none. With 15
# retained, a block that loses 20% of relevant records would have shown a loss about 96% of the
# time; a 30-record loss sample almost never catches it, because relevant records are rare.
MIN_KNOWN_FOR_AND = 15
ESEARCH_WINDOW = 9_999  # PubMed will not page past this many records


def workload_budget(protocol: dict) -> int | None:
    """``workload_budget`` from the protocol (0 or null: no gate), else the depth default."""
    if "workload_budget" in protocol:
        value = protocol.get("workload_budget")
        return int(value) if value else None
    return DEFAULT_BUDGET.get(protocol.get("depth") or "standard", DEFAULT_BUDGET["standard"])


def sample_size(protocol: dict) -> int:
    return SAMPLE_SIZE.get(protocol.get("depth") or "standard", SAMPLE_SIZE["standard"])


def optional_concepts(protocol: dict) -> list[dict]:
    return [c for c in protocol.get("concepts") or [] if c.get("role") == "optional"]


def placement(strategy: Strategy, concept_id: str) -> tuple[str | None, Block | None, str | None]:
    """Where a concept's block is, the block, and the core query it is (or would be) AND-ed to.

    ``candidate``: tested but not in the query; the base is the whole current core query.
    ``block``: AND-ed; the base is the core query without it (none under a custom combination).
    """
    for block in strategy.candidates:
        if block.id == concept_id:
            return "candidate", block, core_query(strategy)
    for block in strategy.blocks:
        if block.id == concept_id:
            if strategy.combine or len(strategy.blocks) < 2:
                return "block", block, None
            return "block", block, core_query(strategy, exclude=concept_id)
    return None, None, None


def fingerprint(strategy: Strategy, block: Block, base: str | None) -> str:
    return validation.digest({"terms": block.terms,
                              "base": apply_limits(base, strategy.limits) if base else None})[:16]


def queries(strategy: Strategy, block: Block, base: str) -> dict:
    return {"base": apply_limits(base, strategy.limits),
            "with": apply_limits(f"({base}) AND {block_query(block)}", strategy.limits),
            "removed": apply_limits(f"({base}) NOT {block_query(block)}", strategy.limits)}


def measure(pm, strategy: Strategy, protocol: dict, in_pubmed: set[str], sets: dict) -> list[dict]:
    """One row per optional concept: its placement, and what AND-ing its block costs and saves."""
    rows = []
    for concept in optional_concepts(protocol):
        cid = str(concept.get("id"))
        where, block, base = placement(strategy, cid)
        row = {"concept": cid, "name": concept.get("name") or cid, "placement": where,
               "decision": concept.get("decision"), "sample_required": sample_size(protocol)}
        if block is None:
            rows.append({**row, "status": "untested"})
            continue
        row["fingerprint"] = fingerprint(strategy, block, base)
        if base is None:
            rows.append({**row, "status": "unmeasurable",
                         "note": "a custom combination or single-block strategy cannot be measured block by block"})
            continue
        q = queries(strategy, block, base)
        count_base, count_with = pm.count(q["base"]), pm.count(q["with"])
        hit_base = pm.among(q["base"], in_pubmed) if in_pubmed else set()
        hit_with = pm.among(q["with"], in_pubmed) if in_pubmed else set()
        lost = sorted(hit_base - hit_with, key=int)
        row.update(
            count_without_block=count_base, count_with_block=count_with,
            reduction_percent=round(100.0 * (count_base - count_with) / count_base, 1) if count_base else None,
            known_lost=lost, known_in_base=len(hit_base),
            known_lost_by_set={name: [p for p in lost if p in data.get("pmids", [])]
                               for name, data in sets.items() if set(lost) & set(data.get("pmids", []))},
            removed_query=q["removed"], removed_count=count_base - count_with,
        )
        row["status"] = decision_status(concept.get("decision"), where, row["fingerprint"])
        rows.append(row)
    return rows


def decision_status(decision: dict | None, where: str | None, current: str) -> str:
    if not isinstance(decision, dict) or not decision.get("choice"):
        return "undecided"
    if decision.get("fingerprint") != current:
        return "stale"
    expected = {"and": "block", "leave_out": "candidate"}.get(decision["choice"])
    return "current" if expected == where else "misplaced"


def issues(pm, rows: list[dict], protocol: dict, count: int | None) -> list[dict]:
    """Delivery gate and review items for optional concepts.

    Over the budget, every optional concept needs a current, well-formed decision (errors). At any
    count, AND-ing a block that loses known or sampled relevant records needs a review disposition.
    """
    found = []
    budget = workload_budget(protocol)
    over = budget is not None and count is not None and count > budget
    if over:
        found.append(validation.issue(
            "over_workload_budget",
            f"{count:,} results exceed the workload budget of {budget:,}; confirm every searchable concept "
            "that is only screened has been considered as an optional block", severity="warning", budget=budget))
    for row in rows:
        cid, decision = row["concept"], row.get("decision") or {}
        location = f"concept:{cid}"
        if over:
            problem = {
                "untested": ("optional_untested", "Optional concept has no candidate block to test"),
                "unmeasurable": ("optional_unmeasurable", "Optional concept cannot be measured under this combination"),
                "undecided": ("optional_undecided", "Optional concept needs a recorded decision (psb optional decide)"),
                "stale": ("optional_decision_stale", "Decision was measured against a different block or strategy; decide again"),
                "misplaced": ("optional_decision_misplaced", "Decision does not match where the block is (and: in blocks; leave_out: in candidates)"),
            }.get(row["status"])
            if problem:
                found.append(validation.issue(*problem, location=location))
                continue
            if decision.get("choice") == "leave_out" and not str(decision.get("reason") or "").strip():
                found.append(validation.issue("optional_reason_missing", "A leave-out decision needs a reason", location=location))
            sample = decision.get("loss_sample") or {}
            screened = [str(p) for p in sample.get("screened") or []]
            needed = min(row["sample_required"], row.get("removed_count") or 0)
            if len(set(screened)) < needed:
                found.append(validation.issue("loss_sample_short", f"Screen at least {needed} records the block removes",
                                              location=location, screened=len(set(screened)), required=needed))
            elif screened:
                outside = sorted(set(screened) - pm.among(row["removed_query"], screened), key=int)
                if outside:
                    found.append(validation.issue("loss_sample_invalid", "Loss sample includes records the block does not remove",
                                                  location=location, pmids=outside))
        if row["status"] == "current" and decision.get("choice") == "and" and row.get("known_in_base", 0) < MIN_KNOWN_FOR_AND:
            found.append(validation.issue(
                "optional_and_underpowered",
                f"An optional block can be AND-ed only when at least {MIN_KNOWN_FOR_AND} known records sit in the "
                "strategy without it and it loses none; find more known records or leave it out",
                location=location, known_in_base=row.get("known_in_base", 0)))
        if row["status"] == "current" and decision.get("choice") == "and":
            if row.get("known_lost"):
                found.append(validation.issue("optional_and_loses_known", "AND-ed optional block loses known relevant records",
                                              severity="warning", location=location, pmids=row["known_lost"]))
            relevant = sorted({str(p) for p in (decision.get("loss_sample") or {}).get("relevant") or []})
            if relevant:
                found.append(validation.issue("optional_and_loses_relevant", "AND-ed optional block removes relevant records found in its loss sample",
                                              severity="warning", location=location, pmids=relevant))
    return found


# -- sampling and deciding -------------------------------------------------------------------------

def _bins(pm, query: str, start: dt.date, end: dt.date, count: int) -> list[tuple[dt.date, dt.date, int]]:
    """Split an Entrez-date range until every bin can be paged through (<= ESEARCH_WINDOW records)."""
    if count <= ESEARCH_WINDOW or start >= end:
        return [(start, end, count)]
    middle = start + (end - start) // 2
    left_q = _dated(query, start, middle)
    left = pm.search(left_q, dated=False)["count"]
    return (_bins(pm, query, start, middle, left)
            + _bins(pm, query, middle + dt.timedelta(days=1), end, count - left))


def _dated(query: str, start: dt.date, end: dt.date) -> str:
    return f'({query}) AND ("{start:%Y/%m/%d}"[edat] : "{end:%Y/%m/%d}"[edat])'


def draw(pm, query: str, n: int, *, seed: int = 1) -> dict:
    """A uniform random sample of ``n`` records a query retrieves, however many there are."""
    total = pm.count(query)
    rng = random.Random(seed)
    if total <= ESEARCH_WINDOW:
        pmids = pm.search(query, retmax=total)["pmids"] if total else []
        return {"count": total, "pmids": sorted(rng.sample(pmids, min(n, len(pmids))), key=int), "frame": "all records"}
    end = dt.date.fromisoformat(pm.as_of) if pm.as_of else dt.date.today()
    bins = [b for b in _bins(pm, query, dt.date(1800, 1, 1), end, total) if b[2]]
    ranks = sorted(rng.sample(range(total), min(n, total)))
    picked, offset, index = [], 0, 0
    for start, stop, size in bins:
        while index < len(ranks) and ranks[index] < offset + size:
            within = ranks[index] - offset
            if within < ESEARCH_WINDOW:
                picked += pm.search(_dated(query, start, stop), retmax=1, retstart=within, dated=False)["pmids"]
            index += 1
        offset += size
    return {"count": total, "pmids": sorted(set(picked), key=int), "frame": f"all records, {len(bins)} Entrez-date bins"}


def sample(ws, concept_id: str, *, n: int | None = None, seed: int = 1) -> dict:
    """Draw and store the loss sample for one optional concept."""
    protocol = ws.protocol()
    strategy = ws.strategy()
    if concept_id not in {str(c.get("id")) for c in optional_concepts(protocol)}:
        raise StrategyError(f"{concept_id!r} is not an optional concept in protocol.json")
    where, block, base = placement(strategy, concept_id)
    if block is None or base is None:
        raise StrategyError(f"no measurable block for {concept_id!r}: add it to strategy.json candidates")
    removed = queries(strategy, block, base)["removed"]
    drawn = draw(ws.pubmed, removed, n or sample_size(protocol) or SAMPLE_SIZE["standard"], seed=seed)
    records = ws.ensure_records(drawn["pmids"])
    stored = {"concept": concept_id, "placement": where, "fingerprint": fingerprint(strategy, block, base),
              "removed_query": removed, "removed_count": drawn["count"], "frame": drawn["frame"], "seed": seed,
              "pmids": drawn["pmids"], "drawn": validation_now()}
    path = sample_path(ws, concept_id)
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(stored, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {**stored, "sample_file": str(path),
            "records": [{"pmid": p, "year": r.get("year"), "title": r.get("title")} for p, r in records.items()],
            "next": "screen every record against the eligibility criteria (psb fetch --abstracts), add relevant ones "
                    "to a relevant set, then run psb optional decide"}


def sample_path(ws, concept_id: str):
    return ws.root / "optional" / f"{concept_id}-sample.json"


def decide(ws, concept_id: str, *, choice: str, reason: str, screened: list[str] | None, relevant: list[str]) -> dict:
    """Record a decision bound to the current block and strategy; ``and`` moves the candidate into blocks.

    ``screened`` defaults to the stored loss sample (psb optional sample): every drawn record counts
    as screened, so the relevant ones must be named.
    """
    if choice not in {"and", "leave_out"}:
        raise StrategyError("choice must be 'and' or 'leave_out'")
    if screened is None:
        path = sample_path(ws, concept_id)
        screened = json.loads(path.read_text(encoding="utf-8-sig"))["pmids"] if path.exists() else []
    protocol = ws.protocol()
    concepts = protocol.get("concepts") or []
    concept = next((c for c in concepts if str(c.get("id")) == concept_id and c.get("role") == "optional"), None)
    if concept is None:
        raise StrategyError(f"{concept_id!r} is not an optional concept in protocol.json")
    if not set(relevant) <= set(screened):
        raise StrategyError("relevant records must be among the screened records")
    strategy = ws.strategy()
    where, block, base = placement(strategy, concept_id)
    if block is None or base is None:
        raise StrategyError(f"no measurable block for {concept_id!r}: add it to strategy.json candidates")
    if choice == "and":
        known = sorted({p for data in ws.sets().values() for p in data.get("pmids", [])})
        in_base = ws.pubmed.among(apply_limits(base, strategy.limits), ws.pubmed.existing(known)) if known else set()
        if len(in_base) < MIN_KNOWN_FOR_AND:
            raise StrategyError(f"only {len(in_base)} known records sit in the strategy without {concept_id!r}; AND-ing "
                                f"it needs at least {MIN_KNOWN_FOR_AND} (none lost). Find more known records or leave it out")
        lost = in_base - ws.pubmed.among(apply_limits(f"({base}) AND {block_query(block)}", strategy.limits), in_base)
        if lost:
            raise StrategyError(f"AND-ing {concept_id!r} loses known records {', '.join(sorted(lost, key=int))}; leave it out")
    moved = False
    if choice == "and" and where == "candidate":
        strategy.candidates = [c for c in strategy.candidates if c.id != concept_id]
        strategy.blocks.append(block)
        moved = True
    elif choice == "leave_out" and where == "block":
        strategy.blocks = [b for b in strategy.blocks if b.id != concept_id]
        strategy.candidates.append(block)
        moved = True
    concept["decision"] = {"choice": choice, "reason": reason.strip(), "fingerprint": fingerprint(strategy, block, base),
                           "loss_sample": {"screened": sorted(set(screened), key=int), "relevant": sorted(set(relevant), key=int)},
                           "decided": validation_now()}
    ws.write_protocol(protocol)
    if moved:
        ws.write_strategy(strategy)
    return {"concept": concept_id, "decision": concept["decision"], "moved": moved,
            "next": "run psb eval to measure the strategy with this decision"}


def validation_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

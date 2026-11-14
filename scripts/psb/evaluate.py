"""Evaluate a strategy: one command for every measurement the build loop needs.

- lint and PubMed's translation of the whole query
- counts for every line (term, block, combination, limit)
- recall on every PMID set, labelled by how independent that set is
- for each missed known record, the blocks that fail to retrieve it
- leave-one-block-out ablation
- for each optional block, what AND-ing it would do to the count and to the known records
- the change since the previous evaluated version, including known records it lost

The numbers are recomputed every time; nothing here is read back from an earlier report
except the previous version's retrieved PMIDs, used for the diff.
"""

from __future__ import annotations

from .ncbi import NcbiError
from . import validation, mesh, syntax
from .progress import attribution
from .strategy import block_query, core_query, full_query, lint, numbered_lines, query_with_optional
from .workspace import MINING_ROLES, ROLES, Workspace, now

# A known record is independent of the searcher's wording when no psb search led to it: the user
# supplied it, or it is on a review's reference list. A record found by a keyword search names the
# searched words by construction, and its similar and citing articles inherit that bias, so neither
# can show what a block built on those words would lose. The bound is computed on independent
# records only. With none lost out of n it is 1 - 0.05 ** (1 / n): 26% at 10, 14% at 20, 10% at 30.
INDEPENDENT_ROUTES = {"resolve", "neighbors:refs"}
NO_INDEPENDENT_RECORDS = ("Every known record came from a keyword search, or from the similar or citing articles of one. "
                          "Such records name the searched words by construction, so the recall figures check the "
                          "strategy's wording; they do not estimate recall. A prior review's reference list "
                          "(psb neighbors <review PMID> --links refs) gives records that do not depend on your wording.")
OPTIONAL_MIN_INDEPENDENT = 20
OPTIONAL_MIN_REDUCTION = 25.0


def _recall(retrieved: int, total: int) -> float | None:
    return round(100.0 * retrieved / total, 1) if total else None


def _term_diff(old: dict, new: dict) -> dict:
    before = {b["id"]: b["terms"] for b in old.get("blocks", [])}
    after = {b["id"]: b["terms"] for b in new.get("blocks", [])}
    changes = {}
    for block_id in list(dict.fromkeys([*before, *after])):
        added = [t for t in after.get(block_id, []) if t not in before.get(block_id, [])]
        removed = [t for t in before.get(block_id, []) if t not in after.get(block_id, [])]
        if block_id not in before:
            changes[block_id] = {"block": "added", "terms_added": added}
        elif block_id not in after:
            changes[block_id] = {"block": "removed", "terms_removed": removed}
        elif added or removed:
            changes[block_id] = {"terms_added": added, "terms_removed": removed}
    if old.get("combine") != new.get("combine"):
        changes["_combine"] = {"before": old.get("combine"), "after": new.get("combine")}
    if old.get("limits") != new.get("limits"):
        changes["_limits"] = {"before": old.get("limits"), "after": new.get("limits")}
    if old.get("optional") != new.get("optional"):
        changes["_optional"] = {"before": [b.get("id") for b in old.get("optional") or []],
                                "after": [b.get("id") for b in new.get("optional") or []]}
    return changes


def loss_upper_bound(lost: int, total: int, confidence: float = 0.95) -> float | None:
    """One-sided exact (Clopper-Pearson) upper bound, in percent, on the share of records lost."""
    if total <= 0:
        return None
    if lost >= total:
        return 100.0

    def at_most(p: float) -> float:  # P(X <= lost) for X ~ Binomial(total, p)
        term = cumulative = (1 - p) ** total
        for k in range(lost):
            term *= (total - k) / (k + 1) * p / (1 - p)
            cumulative += term
        return cumulative

    low, high = lost / total, 1.0
    for _ in range(60):
        middle = (low + high) / 2
        low, high = (middle, high) if at_most(middle) > 1 - confidence else (low, middle)
    return round(100 * high, 1)


def without_keyword_search(ws: Workspace, pmids) -> set[str]:
    """The known records no psb search led to: supplied directly (in no batch), resolved, or on a reference list."""
    routes = {pmid: str(batch.get("via")) for pmid, batch in attribution(ws).items()}
    return {p for p in pmids if routes.get(p, "resolve") in INDEPENDENT_ROUTES}


def _free_recall(free: set[str], held_out: set[str], hit: set[str]) -> dict:
    """Recall on records that neither a keyword search nor the build itself can have favoured.

    A record used for mining is retrieved because the strategy was built on it, and a record found
    by a search is retrieved because it uses the searched words. Only a record that is neither
    (a held-out seed, a review's included study) says anything about records not yet seen.
    """
    tested = free & held_out
    bound = loss_upper_bound(len(tested - hit), len(tested))
    found = {"in_pubmed": len(free), "retrieved": len(free & hit),
             "held_out": {"in_pubmed": len(tested), "retrieved": len(tested & hit),
                          "recall_lower_95_percent": None if bound is None else round(100 - bound, 1)}}
    if not free:
        found["reading"] = NO_INDEPENDENT_RECORDS
    elif not tested:
        found["reading"] = (f"{found['retrieved']} of the {len(free)} known records found without a keyword search are "
                            "retrieved, but all of them were used to build the strategy, so this checks the build and "
                            "does not estimate recall. Hold some out (psb set split) or add a review's included "
                            "studies as a benchmark set.")
    else:
        held = found["held_out"]
        found["reading"] = (f"{held['retrieved']} of the {held['in_pubmed']} held-out known records found without a keyword "
                            f"search are retrieved: on their evidence recall is at least {held['recall_lower_95_percent']}% "
                            "(95% bound; it is as wide as the number of such records makes it).")
    return found


def _optional_reading(entry: dict) -> str:
    known = entry.get("known")
    saving = (f"the result falls from {entry['count_now']:,} to {entry['count_if_added']:,}"
              + (f" ({entry['reduction_percent']}% fewer)" if entry.get("reduction_percent") is not None else ""))
    if not known:
        return f"AND-ing this block: {saving}. No known records, so nothing shows what it would lose: do not AND it on the count alone."
    kept = known["retrieved_now"]
    if known["lost_if_added"]:
        return (f"AND-ing this block would lose {len(known['lost_if_added'])} of the {kept} known records retrieved now "
                f"({saving}). Keep it out of the search, or broaden it and test again.")
    if entry.get("reduction_percent") is not None and entry["reduction_percent"] < OPTIONAL_MIN_REDUCTION:
        return f"AND-ing this block loses no known record but saves little: {saving}. Leave it out."
    independent = known["by_route"]["without_keyword_search"]["retrieved_now"]
    bound = known["loss_upper_95_percent"]
    if independent < OPTIONAL_MIN_INDEPENDENT:
        return (f"AND-ing this block loses none of the {kept} known records retrieved now and {saving}. That is weak "
                f"evidence: only {independent} of them were found independently of a keyword search (user seeds, a "
                "review's reference list). The rest name the searched words by construction, so they cannot show what "
                "this block would lose"
                + (f"; on the independent records alone, up to {bound}% of relevant records could still be lost (95% bound)"
                   if bound is not None else "; the loss is unmeasured")
                + ". Find independent known records and test again. AND it without them only if the result is otherwise "
                  "too large to screen, and report the loss as an open, unmeasured risk.")
    return (f"AND-ing this block loses none of the {kept} known records retrieved now, {independent} of them found "
            f"independently of a keyword search (95% bound on the share lost: {bound}%), and {saving}. It is a "
            "candidate for a searched block: decide and record the reason.")


def _optional_entry(pm, strategy, block, result: dict, free_known: set, in_pubmed, hit_full, sets) -> dict:
    alone = pm.search(effective_query(block_query(block), pm.as_of), dated=False)
    added = effective_query(query_with_optional(strategy, block), pm.as_of)
    count = pm.count(added) if alone["count"] else 0
    entry = {"id": block.id, "name": block.name, "terms": len(block.terms), "count_alone": alone["count"],
             "count_now": result["count"], "count_if_added": count,
             "reduction_percent": round(100 * (1 - count / result["count"]), 1) if result["count"] else None,
             "issues": [{"code": i["code"], "severity": i["severity"], "evidence": i.get("evidence")} for i in alone["issues"]]}
    if in_pubmed:
        kept = pm.among(added, hit_full) if alone["count"] else set()
        lost = sorted(hit_full - kept, key=int)
        in_block = pm.among(block_query(block), in_pubmed) if alone["count"] else set()
        free = hit_full & free_known
        by_route = {route: {"retrieved_now": len(members), "lost_if_added": len(members - kept)}
                    for route, members in (("without_keyword_search", free), ("from_keyword_search", hit_full - free))}
        entry["known"] = {
            "retrieved_now": len(hit_full), "lost_if_added": lost,
            "lost_by_set": {name: sorted(set(data.get("pmids", [])) & set(lost), key=int) for name, data in (sets or {}).items()
                            if set(data.get("pmids", [])) & set(lost)},
            "loss_upper_95_percent": loss_upper_bound(len(free - kept), len(free)),
            "by_route": by_route,
            "block_recall": {"retrieved": len(in_block), "of": len(in_pubmed), "recall_percent": _recall(len(in_block), len(in_pubmed))},
            "missed_now_but_in_block": sorted(in_block - hit_full, key=int),
        }
    entry["reading"] = _optional_reading(entry)
    return entry


def _measure_optional(ws: Workspace, strategy, result: dict, *, in_pubmed: set[str] | None = None,
                      hit_full: set[str] | None = None, sets: dict | None = None) -> None:
    """What AND-ing each optional block would do. Diagnostic only: nothing here reaches the query."""
    if not strategy.optional:
        return
    pm = ws.pubmed
    free_known = without_keyword_search(ws, in_pubmed or set())
    rows = []
    for block in strategy.optional:
        try:
            entry = _optional_entry(pm, strategy, block, result, free_known, in_pubmed, hit_full, sets)
        except NcbiError as exc:
            # A block that is never delivered must not stop an evaluation or a delivery.
            entry = {"id": block.id, "name": block.name, "terms": len(block.terms), "error": str(exc),
                     "reading": "Not measured: PubMed did not answer for this optional block. Nothing can be concluded about it."}
        rows.append(entry)
    result["optional_blocks"] = rows


def effective_query(query: str, as_of: str | None) -> str:
    if not as_of:
        return query
    import datetime
    bound = datetime.date.fromisoformat(as_of).strftime("%Y/%m/%d")
    return f'({query}) AND ("1800/01/01"[edat] : "{bound}"[edat])'


def evaluate(ws: Workspace, *, term_counts: bool = True) -> dict:
    inputs = validation.input_snapshot(ws)
    result = {"inputs": inputs, "input_sha256": validation.digest(inputs), "run_date": now(),
              "lint": lint(ws.strategy(), concepts=inputs["protocol"].get("concepts") or []),
              "lines": [], "vocabulary": [], "ok": False}
    collected = []
    complete = False
    try:
        unknowns = [i for i in result["lint"] if i["code"] == "unknown_tag"]
        if unknowns and not any(i["severity"] == "error" for i in result["lint"]):
            names = ws.pubmed.field_names()
            result["lint"] = [i for i in result["lint"] if not (
                i["code"] == "unknown_tag" and all(a["tag"].split(":")[0].casefold() in names
                    or a["tag"].split(":")[0].casefold() in syntax.ALIASES for a in syntax.atoms(i["term"]))) ]
        collected.extend(validation.identify(i, i.get("location") or "block:" + i.get("block", "strategy")) for i in result["lint"])
        if not any(i["blocking"] for i in collected):
            result["query"] = effective_query(full_query(ws.strategy()), ws.pubmed.as_of)
            result["vocabulary"], vocabulary_issues = mesh.validate_query(ws.pubmed, result["query"], result["run_date"])
            collected.extend(vocabulary_issues)
            _measure(ws, result, term_counts=term_counts)
            complete = term_counts and not any(r.get("status") == "unverified" for r in result["vocabulary"])
    except (NcbiError, ValueError) as exc:
        collected.append(validation.issue("validation_unavailable", "Evaluation could not complete", evidence=str(exc)))
    collected.extend(validation.identify(i, "final") for i in result.get("translation_issues", []))
    for line in result["lines"]:
        collected.extend(validation.identify(i, f"line:{line['n']}") for i in line.get("issues", []))
    if result.get("misses"):
        collected.append(validation.issue("known_records_missed", "Investigate missed known records and explain any retained misses",
                                         severity="warning", evidence=result["misses"]))
    if validation.digest(validation.input_snapshot(ws)) != result["input_sha256"]:
        collected.append(validation.issue("inputs_changed", "Workspace inputs changed during evaluation"))
        complete = False
    result["validation"] = validation.summarize(collected, complete=complete)
    result["ok"] = not result["validation"]["blockers"]
    result["review_sha256"] = validation.review_fingerprint(result)
    return result


def _measure(ws: Workspace, result: dict, *, term_counts: bool) -> None:
    strategy = ws.strategy()
    pm = ws.pubmed
    full = result["query"]
    core = core_query(strategy)
    search = pm.search(full, dated=False)
    if search["count"] and not search.get("translation", "").strip():
        raise NcbiError("PubMed returned hits without a query translation")
    result.update(as_of=pm.as_of, count=search["count"], translation=search["translation"],
                  raw_diagnostics=search.get("raw_diagnostics"), translation_issues=search["issues"])
    if strategy.limits:
        result["count_without_limits"] = pm.count(core)

    lines = result["lines"]
    for line in numbered_lines(strategy):
        if line["kind"] == "term" and not term_counts:
            continue
        query = effective_query(line["query"], pm.as_of)
        found = pm.search(query, dated=False)
        entry = {**line, "query": query, "count": found["count"], "translation": found["translation"],
                 "raw_diagnostics": found.get("raw_diagnostics"), "issues": list(found["issues"])}
        if found["count"] and not found.get("translation", "").strip():
            entry["issues"].append({"severity": "error", "code": "translation_missing", "message": "Hits returned without translation"})
        if not found["count"] and line["kind"] == "term":
            entry["issues"].append({"severity": "warning", "code": "zero_hits", "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds", "query": query, "translation": found["translation"]})
        lines.append(entry)
    sets = ws.sets()
    known = sorted({p for data in sets.values() for p in data.get("pmids", [])})
    if not known:
        result["sets"] = {}
        result["note"] = "no PMID sets: recall not measured (add seeds, relevant, validation or benchmark sets)"
        _measure_optional(ws, strategy, result)
        return

    in_pubmed = pm.existing(known)
    hit_full = pm.among(full, in_pubmed)
    hit_core = pm.among(core, in_pubmed) if strategy.limits else hit_full
    hit_block = {b.id: pm.among(block_query(b), in_pubmed) for b in strategy.blocks}

    free_known = without_keyword_search(ws, in_pubmed)
    mined = {p for data in sets.values() if data.get("role") in MINING_ROLES for p in data.get("pmids", [])}
    result["known_without_keyword_search"] = _free_recall(free_known, in_pubmed - mined, hit_full)
    per_set = {}
    for name, data in sets.items():
        pmids = [p for p in data.get("pmids", [])]
        present = [p for p in pmids if p in in_pubmed]
        missed = [p for p in present if p not in hit_full]
        per_set[name] = {
            "role": data.get("role"),
            "independence": ROLES.get(str(data.get("role")), "unknown"),
            "size": len(pmids),
            "in_pubmed": len(present),
            "not_in_pubmed": [p for p in pmids if p not in in_pubmed],
            "retrieved": len(present) - len(missed),
            "recall_percent": _recall(len(present) - len(missed), len(present)),
            "missed": missed,
            "without_keyword_search": {"in_pubmed": len(set(present) & free_known),
                                       "retrieved": len(set(present) & free_known & hit_full)},
        }
    result["sets"] = per_set
    result["retrieved_known"] = sorted(hit_full)
    result["known_in_pubmed"] = sorted(in_pubmed)

    misses = sorted(in_pubmed - hit_full)
    result["misses"] = [
        {
            "pmid": pmid,
            "failing_blocks": [b.id for b in strategy.blocks if pmid not in hit_block[b.id]],
            "lost_to_limits": pmid in hit_core and pmid not in hit_full,
            "sets": [name for name, data in sets.items() if pmid in data.get("pmids", [])],
        }
        for pmid in misses
    ]
    result["block_recall"] = {
        b.id: {"retrieved": len(hit_block[b.id]), "of": len(in_pubmed), "recall_percent": _recall(len(hit_block[b.id]), len(in_pubmed))}
        for b in strategy.blocks
    }

    if len(strategy.blocks) >= 2 and not strategy.combine:
        ablation = []
        for block in strategy.blocks:
            without = core_query(strategy, exclude=block.id)
            gained = pm.among(without, in_pubmed) - hit_core
            ablation.append(
                {"drop": block.id, "count": pm.count(without), "known_gained": len(gained), "gained_pmids": sorted(gained)}
            )
        result["ablation"] = ablation
    elif strategy.combine:
        result["ablation"] = "skipped: ablation needs the default AND combination"
    _measure_optional(ws, strategy, result, in_pubmed=in_pubmed, hit_full=hit_full, sets=sets)
    return


def compare(previous: dict | None, current: dict, strategy: dict) -> dict | None:
    if previous is None:
        return None
    before = previous.get("evaluation", {})
    old_hits = set(before.get("retrieved_known", []))
    new_hits = set(current.get("retrieved_known", []))
    # Only records still in a current set can be lost; removing a record from a set is not a miss.
    lost = sorted((old_hits & set(current.get("known_in_pubmed", []))) - new_hits)
    return {
        "from_version": previous.get("version"),
        "count_before": before.get("count"),
        "count_after": current.get("count"),
        "count_change": (current.get("count") or 0) - (before.get("count") or 0),
        "known_lost": lost,
        "known_gained": sorted(new_hits - old_hits),
        "changes": _term_diff(previous.get("strategy", {}), strategy),
        "regression": bool(lost),
    }

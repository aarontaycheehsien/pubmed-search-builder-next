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
from .progress import attribution, batches, decisions
from .strategy import Block, Strategy, block_query, core_query, full_query, lint, numbered_lines, query_with_optional
from .workspace import MINING_ROLES, ROLES, Workspace, now

# A known record is independent of the searcher's wording when no psb search led to it: the user
# supplied it, or it is on a review's reference list. A record found by a keyword search names the
# searched words by construction, and its similar and citing articles inherit that bias, so neither
# can show what a block built on those words would lose. The bound is computed on independent
# records only. With none lost out of n it is 1 - 0.05 ** (1 / n): 26% at 10, 14% at 20, 10% at 30.
# A reference list is chosen by the review's authors, whichever index holds it, so OpenAlex
# reference lists count exactly as PubMed's do.
INDEPENDENT_ROUTES = {"resolve", "neighbors:refs", "openalex:refs"}
REFERENCE_ROUTES = {"neighbors:refs", "openalex:refs"}
# Forward citations do not use the searcher's words either, but citing papers share a research
# community and its vocabulary and favour highly cited work. When every record they were linked
# from is independent they are reported as their own tier, never pooled into the recall bound.
FORWARD_ROUTES = {"neighbors:citedin", "openalex:citedin"}
# A seeded random sample from an OpenAlex frame, screened before retrieval is checked.
FRAME_ROUTES = {"openalex:frame"}
ANCHOR_CONCENTRATION = 60.0
ANCHOR_MIN_RECORDS = 5
SUPPLIED = "supplied directly"
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


def _route(attributed: dict[str, dict], pmid: str) -> str:
    return str((attributed.get(pmid) or {}).get("via") or "resolve")


def _origins(batch: dict, pmid: str) -> list[str]:
    return list((batch.get("origins") or {}).get(pmid) or batch.get("from") or [])


def citation_from_independent(ws: Workspace, pmids) -> set[str]:
    """Known records first seen as forward citations of records that are themselves independent."""
    attributed = attribution(ws)
    found = set()
    for pmid in pmids:
        batch = attributed.get(pmid)
        if not batch or str(batch.get("via")) not in FORWARD_ROUTES:
            continue
        origins = _origins(batch, pmid)
        # An origin that is not a PMID (a work outside PubMed) cannot be traced: treat it as not independent.
        if origins and all(o.isdigit() and _route(attributed, o) in INDEPENDENT_ROUTES for o in origins):
            found.add(pmid)
    return found


def anchor_profile(ws: Workspace, free: set[str]) -> dict:
    """Which reviews the independent records come from, and whether one review dominates."""
    attributed = attribution(ws)
    counts: dict[str, int] = {}
    listed = 0
    for pmid in free:
        batch = attributed.get(pmid)
        if not batch or str(batch.get("via")) not in REFERENCE_ROUTES:
            counts[SUPPLIED] = counts.get(SUPPLIED, 0) + 1
            continue
        listed += 1
        for origin in _origins(batch, pmid) or ["unknown review"]:
            counts[origin] = counts.get(origin, 0) + 1
    rows = sorted(({"anchor": a, "records": n} for a, n in counts.items()), key=lambda r: (-r["records"], r["anchor"]))
    reviews = [r for r in rows if r["anchor"] != SUPPLIED]
    profile: dict = {"from_reference_lists": listed, "supplied_directly": counts.get(SUPPLIED, 0), "rows": rows,
                     "concentrated": False}
    if reviews and listed:
        top = dict(reviews[0], share_percent=round(100 * reviews[0]["records"] / listed, 1))
        profile["top"] = top
        profile["concentrated"] = listed >= ANCHOR_MIN_RECORDS and top["share_percent"] > ANCHOR_CONCENTRATION
    return profile


def _anchor_reading(profile: dict) -> str | None:
    if not profile.get("concentrated"):
        return None
    top = profile["top"]
    return (f"{top['records']} of the {profile['from_reference_lists']} known records found through reference lists come from "
            f"one review ({top['anchor']}, {top['share_percent']}%). A benchmark built on one review takes that review's scope: "
            "add the reference list of a second review that covers a different searched concept.")


def _citation_tier(cited: set[str], held_out: set[str], hit: set[str]) -> dict:
    tested = cited & held_out
    return {"in_pubmed": len(cited), "retrieved": len(cited & hit),
            "held_out": {"in_pubmed": len(tested), "retrieved": len(tested & hit)},
            "reading": ("Forward citations of independent known records do not use the strategy's words, but citing papers "
                        "share a research community and its vocabulary. They are reported on their own and are not part "
                        "of the recall bound.") if cited else "No known record came from forward citations of independent records."}


def frame_estimate(ws: Workspace, sets: dict, in_pubmed: set[str], hit: set[str], mined: set[str]) -> dict | None:
    """Recall within an OpenAlex frame, from a random sample screened before retrieval was checked.

    Membership is any frame batch, not the earliest batch: a frame record that a pilot happened to
    show first must still count, or the sample would lose the records the wording already finds.
    """
    sampled: set[str] = set()
    for batch in batches(ws):
        if str(batch.get("via")) in FRAME_ROUTES:
            sampled.update(str(p) for p in batch.get("pmids") or [])
    if not sampled:
        return None
    screened = decisions(ws)
    included = {p for p in sampled if (screened.get(p) or {}).get("decision") == "include"}
    in_sets = {p for d in sets.values() for p in d.get("pmids", [])}
    present = included & in_pubmed
    tested = present - mined
    bound = loss_upper_bound(len(tested - hit), len(tested))
    estimate = {
        "sampled": len(sampled),
        "screened": sum(1 for p in sampled if p in screened),
        "unscreened": len(sampled - set(screened)),
        "uncertain": sum(1 for p in sampled if (screened.get(p) or {}).get("decision") == "uncertain"),
        "screened_in": len(included),
        "missing_from_sets": sorted(included - in_sets, key=int),
        "in_pubmed": len(present),
        "retrieved": len(present & hit),
        "recall_percent": _recall(len(present & hit), len(present)),
        "recall_lower_95_percent": None if bound is None else round(100 - bound, 1),
    }
    parts = []
    if estimate["unscreened"] or estimate["missing_from_sets"]:
        parts.append(f"{estimate['unscreened']} sampled records are unscreened and {len(estimate['missing_from_sets'])} "
                     "screened-in records are in no set, so the estimate is incomplete: screen every sampled record and add "
                     "every include to a held-out set, whether or not the strategy retrieves it.")
    if present:
        parts.append(f"{estimate['retrieved']} of the {len(present)} screened-in frame records are retrieved"
                     + (f"; within the frame recall is at least {estimate['recall_lower_95_percent']}% (95% bound)"
                        if estimate["recall_lower_95_percent"] is not None else "")
                     + ". The frame is an OpenAlex topic classification, so this estimates recall within that frame, "
                       "not overall.")
    if estimate["uncertain"]:
        parts.append(f"{estimate['uncertain']} uncertain records are left out of the estimate.")
    estimate["reading"] = " ".join(parts) or "No frame record has been screened in yet."
    return estimate


def citation_searches(ws: Workspace) -> list[dict]:
    """Each citation search run for known-record discovery, in TARCiS terms, for the audit."""
    screened = decisions(ws)
    rows = []
    for batch in batches(ws):
        via = str(batch.get("via") or "")
        index, _, links = via.partition(":")
        if index not in {"neighbors", "openalex"} or links in {"prior-reviews", "frame"}:
            continue
        kinds = links.split(",")
        directions = sorted({"backward" if k == "refs" else "forward" if k == "citedin" else "similar articles" for k in kinds})
        pmids = [str(p) for p in batch.get("pmids") or []]
        rows.append({"batch": batch.get("batch"), "at": batch.get("at"), "index": "OpenAlex" if index == "openalex" else "PubMed",
                     "direction": " + ".join(directions), "seed_records": len(batch.get("from") or []),
                     "candidates": batch.get("total"), "shown": len(pmids),
                     "screened_in": sum(1 for p in pmids if (screened.get(p) or {}).get("decision") == "include")})
    return rows


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


IMPACT_SAMPLES = 8
# Above this, a result is unlikely to be screened as it stands, and which terms carry it is worth two
# requests a term to know. The figure is a prompt, not a limit: the user's capacity decides.
LARGE_RESULT = 10_000


def _term_impact(ws: Workspace, strategy: Strategy, result: dict, hit_full: set[str]) -> dict:
    """What each term alone adds to the final result: records only it retrieves, known records only it retrieves.

    A term's own count says little: most of what it finds, other terms or other blocks find or
    exclude. The records that leave the result when the term is removed are the ones it costs.
    """
    pm = ws.pubmed
    count = result["count"]
    rows = []
    for block in strategy.blocks:
        if len(block.terms) < 2:
            continue  # the block's only term: removing it removes the block, which ablation covers
        for index, term in enumerate(block.terms):
            blocks = [Block(b.id, b.name, [t for i, t in enumerate(b.terms) if b.id != block.id or i != index]) for b in strategy.blocks]
            without = effective_query(full_query(Strategy(blocks, strategy.combine, strategy.limits)), pm.as_of)
            remaining = pm.count(without)
            rows.append({"block": block.id, "term": term, "records_only_here": max(count - remaining, 0),
                         "share_percent": round(100 * max(count - remaining, 0) / count, 1) if count else None,
                         "known_only_here": sorted(hit_full - pm.among(without, hit_full), key=int) if hit_full else [],
                         "without": without})
    rows.sort(key=lambda r: (-r["records_only_here"], r["block"], r["term"]))
    folder = ws.root / "impact"
    folder.mkdir(exist_ok=True)
    for old in folder.glob("*.txt"):
        old.unlink()
    suspects = [r for r in rows if r["records_only_here"] and not r["known_only_here"]]
    for rank, row in enumerate(suspects[:IMPACT_SAMPLES], 1):
        path = folder / f"{rank:02d}-{row['block']}.txt"
        path.write_text(f"({result['query']}) NOT ({row['without']})\n", encoding="utf-8")
        row["sample_file"] = str(path)
    for row in rows:
        del row["without"]
    share = round(sum(r["records_only_here"] for r in suspects[:IMPACT_SAMPLES]) * 100 / count, 1) if count else 0.0
    reading = ("No term adds records that nothing else finds without also being the only route to a known record."
               if not suspects else
               f"{len(suspects)} terms each add records nothing else finds and are the only route to no known record; the top "
               f"{min(len(suspects), IMPACT_SAMPLES)} account for {share}% of the result. That marks a term as a candidate, "
               "not as noise: look at what it alone finds (psb sample --purpose noise-check --file <sample_file> --random) "
               "and drop it only if that is off-topic. Keep any term with known_only_here.")
    return {"count": count, "terms": rows, "reading": reading}


def effective_query(query: str, as_of: str | None) -> str:
    if not as_of:
        return query
    import datetime
    bound = datetime.date.fromisoformat(as_of).strftime("%Y/%m/%d")
    return f'({query}) AND ("1800/01/01"[edat] : "{bound}"[edat])'


def evaluate(ws: Workspace, *, term_counts: bool = True, term_impact: bool = False) -> dict:
    inputs = validation.input_snapshot(ws)
    result = {"inputs": inputs, "input_sha256": validation.digest(inputs), "run_date": now(),
              "lint": lint(ws.strategy(), concepts=inputs["protocol"].get("concepts") or []),
              "lines": [], "vocabulary": [], "ok": False, "citation_searches": citation_searches(ws)}
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
            if term_impact:
                try:
                    result["term_impact"] = _term_impact(ws, ws.strategy(), result, set(result.get("retrieved_known") or []))
                except NcbiError as exc:  # a diagnostic: it must not stop the evaluation
                    result["term_impact"] = {"error": str(exc), "reading": "Not measured: PubMed did not answer."}
            elif (result.get("count") or 0) > LARGE_RESULT:
                measured = any((ws.root / "impact").glob("*.txt"))
                restructured = any(e.get("type") == "restructure" and not e.get("dry_run") for e in ws.log_entries())
                result["large_result"] = {
                    "count": result["count"], "threshold": LARGE_RESULT, "term_impact_measured": measured,
                    "advice": ("The result is still large. Term impact was measured for an earlier version of the "
                               "strategy: run psb eval --term-impact again only if the blocks have changed much since."
                               if measured else
                               "The result is large and term impact has not been measured in this workspace. Run "
                               "psb eval --term-impact once before the critic step: it shows which terms alone add the "
                               "most records and whether any known record depends on them. Cut only what its samples "
                               "show to be off-topic.")
                              + ("" if restructured else
                                 " Before dropping a high-impact term or AND-ing an optional block for workload, try "
                                 "psb restructure --qualifier <optional block id>: it narrows the five terms that alone "
                                 "add the most records to title mentions or mentions with the qualifier, and keeps each "
                                 "change only if no known record is lost.")}
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
    anchors = anchor_profile(ws, free_known)
    result["known_without_keyword_search"]["anchors"] = anchors
    if _anchor_reading(anchors):
        result["known_without_keyword_search"]["reading"] += " " + _anchor_reading(anchors)
    cited = citation_from_independent(ws, in_pubmed) - free_known
    result["known_from_citation_of_independent"] = _citation_tier(cited, in_pubmed - mined, hit_full)
    frame = frame_estimate(ws, sets, in_pubmed, hit_full, mined)
    if frame:
        result["known_from_frame_sample"] = frame
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

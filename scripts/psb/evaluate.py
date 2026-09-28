"""Evaluate a strategy: one command for every measurement the build loop needs.

- lint and PubMed's translation of the whole query
- counts for every line (term, block, combination, limit)
- recall on every PMID set, labelled by how independent that set is
- for each missed known record, the blocks that fail to retrieve it
- leave-one-block-out ablation
- optional concepts: what AND-ing each candidate block would cost and save
- category concepts: whether a screened probe covers the current block
- the change since the previous evaluated version, including known records it lost

The numbers are recomputed every time; nothing here is read back from an earlier report
except the previous version's retrieved PMIDs, used for the diff.
"""

from __future__ import annotations

from .ncbi import NcbiError
from . import validation, mesh, optional, probe, syntax
from .strategy import block_query, core_query, full_query, lint, numbered_lines
from .workspace import ROLES, Workspace, now


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
    return changes


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
            collected.extend(optional.issues(ws.pubmed, result.get("optional", []), inputs["protocol"], result.get("count")))
            result["categories"] = probe.measure(ws, ws.strategy(), inputs["protocol"])
            collected.extend(probe.issues(result["categories"], inputs["protocol"]))
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
        result["optional"] = optional.measure(pm, strategy, ws.protocol(), set(), sets)
        return

    in_pubmed = pm.existing(known)
    hit_full = pm.among(full, in_pubmed)
    hit_core = pm.among(core, in_pubmed) if strategy.limits else hit_full
    hit_block = {b.id: pm.among(block_query(b), in_pubmed) for b in strategy.blocks}

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
    result["optional"] = optional.measure(pm, strategy, ws.protocol(), in_pubmed, sets)


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

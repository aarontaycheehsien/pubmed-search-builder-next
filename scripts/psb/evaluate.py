"""Evaluate a strategy: one command for every measurement the build loop needs.

- lint and PubMed's translation of the whole query
- counts for every line (term, block, combination, limit)
- recall on every PMID set, labelled by how independent that set is
- for each missed known record, the blocks that fail to retrieve it
- leave-one-block-out ablation
- the change since the previous evaluated version, including known records it lost

The numbers are recomputed every time; nothing here is read back from an earlier report
except the previous version's retrieved PMIDs, used for the diff.
"""

from __future__ import annotations

from .ncbi import PubMed
from .strategy import Strategy, block_query, core_query, full_query, lint, numbered_lines
from .workspace import ROLES, Workspace


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


def evaluate(ws: Workspace, *, term_counts: bool = True) -> dict:
    strategy: Strategy = ws.strategy()
    protocol = ws.protocol()
    issues = lint(strategy, concepts=protocol.get("concepts") or [])
    result: dict = {"lint": issues}
    if strategy.structural_errors():
        result["ok"] = False
        result["message"] = "fix the structural errors before evaluating"
        return result

    pm: PubMed = ws.pubmed
    full = full_query(strategy)
    core = core_query(strategy)
    search = pm.search(full)
    result.update(
        ok=True,
        as_of=pm.as_of,
        query=full,
        count=search["count"],
        translation_issues=search["issues"],
    )
    if strategy.limits:
        result["count_without_limits"] = pm.count(core)

    lines = []
    for line in numbered_lines(strategy):
        if line["kind"] == "term" and not term_counts:
            continue
        found = pm.search(line["query"])
        entry = {"n": line["n"], "text": line["text"], "kind": line["kind"], "block": line["block"], "count": found["count"]}
        if found["issues"] and line["kind"] == "term":
            entry["issues"] = [i["code"] + (f": {i['evidence']}" if i.get("evidence") else "") for i in found["issues"]]
        lines.append(entry)
    result["lines"] = lines

    sets = ws.sets()
    known = sorted({p for data in sets.values() for p in data.get("pmids", [])})
    if not known:
        result["sets"] = {}
        result["note"] = "no PMID sets: recall not measured (add seeds, relevant, validation or benchmark sets)"
        return result

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
    return result


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

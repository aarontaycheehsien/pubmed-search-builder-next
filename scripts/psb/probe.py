"""Category probes: look for relevant records that a category block misses because they name only a member.

A concept is a category when relevant records often name one of its members instead of the category
("environmental health" -> phthalates, arsenic, shift work, traffic noise). Mark it ``"category":
true`` in ``protocol.json``. A probe samples the records that the rest of the strategy and a broader
query retrieve but the category block does not::

    (other blocks) AND (broader query) NOT (category block)

The agent screens the sample. Relevant records go into a known set (so ``psb eval`` reports them
as misses until the block covers them) and are recorded with ``psb probe record``. At ``standard``
and ``thorough`` depth, delivery needs, for every category concept, a screened probe on the current
block that found no relevant record, or the probe budget spent with its findings reviewed.
"""

from __future__ import annotations

import json

from . import validation
from .optional import SAMPLE_SIZE, draw, validation_now
from .strategy import Block, Strategy, StrategyError, apply_limits, block_query, core_query

PROBE_BUDGET = {"quick": 0, "standard": 2, "thorough": 3}


def category_concepts(protocol: dict) -> list[dict]:
    return [c for c in protocol.get("concepts") or [] if c.get("category") and c.get("role") in {"search", "optional"}]


def _block(strategy: Strategy, concept_id: str) -> Block | None:
    return next((b for b in [*strategy.blocks, *strategy.candidates] if b.id == concept_id), None)


def _base(strategy: Strategy, concept_id: str) -> str | None:
    """The other AND-ed blocks (None when the category block is the only one)."""
    if strategy.combine:
        raise StrategyError("category probes need the default AND combination")
    others = [b for b in strategy.blocks if b.id != concept_id]
    return core_query(strategy, exclude=concept_id) if others else None


def probe_query(strategy: Strategy, concept_id: str, broader: str) -> str:
    block = _block(strategy, concept_id)
    if block is None:
        raise StrategyError(f"no block or candidate for {concept_id!r}")
    base = _base(strategy, concept_id)
    scope = f"({base}) AND ({broader})" if base else f"({broader})"
    return apply_limits(f"{scope} NOT {block_query(block)}", strategy.limits)


def _binding(strategy: Strategy, concept_id: str) -> dict:
    block = _block(strategy, concept_id)
    base = _base(strategy, concept_id)
    return {"terms": list(block.terms) if block else [],
            "base_sha256": validation.digest({"base": base, "limits": [l.clause for l in strategy.limits]})[:16]}


def probes(ws, concept_id: str) -> list[dict]:
    folder = ws.root / "probes"
    if not folder.is_dir():
        return []
    found = []
    for path in sorted(folder.glob(f"{concept_id}-*.json"), key=lambda p: int(p.stem.rsplit("-", 1)[1])):
        found.append(json.loads(path.read_text(encoding="utf-8-sig")))
    return found


def draw_probe(ws, concept_id: str, broader: str, *, n: int | None = None, seed: int = 1) -> dict:
    protocol = ws.protocol()
    if concept_id not in {str(c.get("id")) for c in category_concepts(protocol)}:
        raise StrategyError(f"{concept_id!r} is not a category concept (\"category\": true) in protocol.json")
    if not broader.strip():
        raise StrategyError("give a broader query: the category's members, its MeSH tree, or generic wording for it")
    strategy = ws.strategy()
    query = probe_query(strategy, concept_id, broader)
    size = n or SAMPLE_SIZE.get(protocol.get("depth") or "standard") or SAMPLE_SIZE["standard"]
    drawn = draw(ws.pubmed, query, size, seed=seed)
    number = len(probes(ws, concept_id)) + 1
    probe = {"concept": concept_id, "number": number, "broader": broader, "query": query,
             "outside_count": drawn["count"], "frame": drawn["frame"], "seed": seed, "sample": drawn["pmids"],
             "screened": None, "relevant": None, "drawn": validation_now(), **_binding(strategy, concept_id)}
    path = ws.root / "probes" / f"{concept_id}-{number}.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(probe, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    records = ws.ensure_records(drawn["pmids"])
    return {**probe, "probe_file": str(path),
            "records": [{"pmid": p, "year": r.get("year"), "title": r.get("title")} for p, r in records.items()],
            "next": "screen every record against the eligibility criteria (psb fetch --abstracts); add relevant ones "
                    "to a relevant set, then psb probe record <concept> --relevant ..."}


def record_probe(ws, concept_id: str, relevant: list[str], *, note: str = "") -> dict:
    found = probes(ws, concept_id)
    if not found:
        raise StrategyError(f"no probe drawn for {concept_id!r}: run psb probe draw first")
    probe = found[-1]
    relevant = sorted(set(relevant), key=int)
    if not set(relevant) <= set(probe["sample"]):
        raise StrategyError("relevant records must come from the probe's sample")
    known = {p for data in ws.sets().values() for p in data.get("pmids", [])}
    missing = [p for p in relevant if p not in known]
    if missing:
        raise StrategyError(f"add the relevant records to a known set first (psb set add relevant ...): {', '.join(missing)}")
    probe.update(screened=list(probe["sample"]), relevant=relevant, note=note.strip(), recorded=validation_now())
    path = ws.root / "probes" / f"{concept_id}-{probe['number']}.json"
    path.write_text(json.dumps(probe, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"concept": concept_id, "probe": probe["number"], "screened": len(probe["screened"]), "relevant": relevant,
            "next": ("add the members these records name to the block, psb eval, then draw another probe"
                     if relevant else "the current block passed this probe")}


def measure(ws, strategy: Strategy, protocol: dict) -> list[dict]:
    """One row per category concept: its probes and whether the latest one covers the current block."""
    rows = []
    for concept in category_concepts(protocol):
        cid = str(concept.get("id"))
        found = probes(ws, cid)
        latest = next((p for p in reversed(found) if p.get("screened") is not None), None)
        row = {"concept": cid, "name": concept.get("name") or cid, "probes": len(found),
               "budget": PROBE_BUDGET.get(protocol.get("depth") or "standard", 2),
               "history": [{"number": p["number"], "broader": p["broader"], "outside_count": p["outside_count"],
                            "screened": len(p["screened"]) if p.get("screened") is not None else None,
                            "relevant": p.get("relevant")} for p in found]}
        if latest is None:
            row["status"] = "unprobed"
        else:
            now = _binding(strategy, cid) if _block(strategy, cid) else {"terms": [], "base_sha256": None}
            # Adding terms only shrinks what the block misses, so a probe stays valid while the block
            # keeps every term it had and the rest of the strategy is unchanged.
            covered = set(latest["terms"]) <= set(now["terms"]) and latest["base_sha256"] == now["base_sha256"]
            row["status"] = ("stale" if not covered else "found_relevant" if latest.get("relevant") else "clean")
        rows.append(row)
    return rows


def issues(rows: list[dict], protocol: dict) -> list[dict]:
    depth = protocol.get("depth") or "standard"
    if not PROBE_BUDGET.get(depth):
        return []
    found = []
    # Recognising a category is the step that fails silently, so every searched concept must
    # declare it: true (probe it) or false (its records name the concept itself).
    for concept in protocol.get("concepts") or []:
        if concept.get("role") in {"search", "optional"} and not isinstance(concept.get("category"), bool):
            found.append(validation.issue(
                "category_undeclared", "Declare \"category\": true or false: do relevant records often name only a "
                "member of this concept (a specific exposure, condition, drug or behaviour) and never the concept?",
                location=f"concept:{concept.get('id')}"))
    for row in rows:
        location = f"concept:{row['concept']}"
        if row["status"] in {"unprobed", "stale"}:
            found.append(validation.issue(
                "category_unprobed" if row["status"] == "unprobed" else "category_probe_stale",
                "Category concept needs a screened probe on its current block (psb probe draw / record)", location=location))
        elif row["status"] == "found_relevant":
            if row["probes"] < row["budget"]:
                found.append(validation.issue("category_probe_found_relevant",
                                              "The latest probe found relevant records: widen the block, then probe again",
                                              location=location))
            else:
                found.append(validation.issue("category_probe_budget_spent",
                                              "Probe budget spent while the latest probe still found relevant records",
                                              severity="warning", location=location,
                                              pmids=row["history"][-1]["relevant"]))
    return found

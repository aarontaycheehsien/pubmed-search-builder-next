"""Per-term structure: narrow the terms that carry a large result without losing a known record.

The terms that alone add the most records are usually generic words that mean the concept only in
some contexts. Each such term is replaced by (the term in the title) OR (the term AND a
qualifier): a concept from the question that the strategy does not search, taken from an optional
block. A replacement is kept only if no known record the strategy retrieves is lost.
"""

from __future__ import annotations

import re

from .evaluate import effective_query
from .strategy import Block, Strategy, block_query, full_query
from .workspace import Workspace, write_json

TIAB = re.compile(r"^(?P<body>.*)\[(?:tiab|title/abstract)(?P<prox>:~\d+)?\]$", re.IGNORECASE)
MESH = re.compile(r"\[(?:mesh|mh|majr|mesh:noexp|mh:noexp)\]", re.IGNORECASE)
TEXT = re.compile(r"\[(?:tiab|ti|title/abstract|title)(?::~\d+)?\]", re.IGNORECASE)
MARK = "AND ("  # a restructured term contains its qualifier after this


class RestructureError(ValueError):
    pass


def title_form(term: str) -> str | None:
    match = TIAB.match(term.strip())
    return f"{match.group('body')}[ti{match.group('prox') or ''}]" if match else None


def replacement(term: str, qualifier: Block) -> str:
    qualified = f"({term} AND {block_query(qualifier)})"
    title = title_form(term)
    return f"({title} OR {qualified})" if title else qualified


def qualifier_block(strategy: Strategy, block_id: str) -> Block:
    for block in strategy.optional:
        if block.id == block_id:
            terms = " ".join(block.terms)
            missing = [layer for layer, pattern in (("MeSH", MESH), ("title/abstract text-word", TEXT)) if not pattern.search(terms)]
            if missing:
                raise RestructureError(f"qualifier {block_id!r} has no {' or '.join(missing)} layer; a qualifier needs both, "
                                       "or records indexed only one way are lost")
            return block
    raise RestructureError(f"no optional block {block_id!r}: draft the qualifier as an optional block first")


def _with(strategy: Strategy, changes: dict[tuple[str, int], str]) -> Strategy:
    blocks = [Block(b.id, b.name, [changes.get((b.id, i), t) for i, t in enumerate(b.terms)]) for b in strategy.blocks]
    return Strategy(blocks, strategy.combine, strategy.limits, strategy.optional)


def restructure(ws: Workspace, qualifier_id: str, *, top: int = 5, dry_run: bool = False) -> dict:
    strategy = ws.strategy()
    strategy.validate()
    qualifier = qualifier_block(strategy, qualifier_id)
    pm = ws.pubmed
    query = effective_query(full_query(strategy), pm.as_of)
    count = pm.count(query)
    known = sorted({p for data in ws.sets().values() for p in data.get("pmids", [])}, key=int)
    hits = pm.among(query, known) if known else set()
    if not hits:
        raise RestructureError("the strategy retrieves no known record, so a restructure cannot be checked: "
                               "add seeds or screened relevant records first")

    impact = []
    for block in strategy.blocks:
        if len(block.terms) < 2:
            continue
        for index, term in enumerate(block.terms):
            if MARK in term and block_query(qualifier) in term:
                continue  # already restructured
            without = Strategy([Block(b.id, b.name, [t for i, t in enumerate(b.terms) if b.id != block.id or i != index])
                                for b in strategy.blocks], strategy.combine, strategy.limits, strategy.optional)
            only = count - pm.count(effective_query(full_query(without), pm.as_of))
            if only > 0:
                impact.append((only, block.id, index, term))
    impact.sort(key=lambda row: (-row[0], row[1], row[2]))

    accepted: dict[tuple[str, int], str] = {}
    rows = []
    for only, block_id, index, term in impact[:top]:
        trial = _with(strategy, {**accepted, (block_id, index): replacement(term, qualifier)})
        lost = sorted(hits - pm.among(effective_query(full_query(trial), pm.as_of), hits), key=int) if hits else []
        row = {"block": block_id, "term": term, "records_only_here": only}
        if lost:
            row.update(decision="refused", known_lost=lost)
        else:
            accepted[(block_id, index)] = replacement(term, qualifier)
            row.update(decision="restructured", replacement=accepted[(block_id, index)])
        rows.append(row)

    result = _with(strategy, accepted)
    after = pm.count(effective_query(full_query(result), pm.as_of)) if accepted else count
    if accepted and not dry_run:
        write_json(ws.root / "strategy.json", result.to_dict())
    ws.log({"type": "restructure", "qualifier": qualifier_id, "top": top, "dry_run": dry_run,
            "accepted": len(accepted), "refused": sum(r["decision"] == "refused" for r in rows), "before": count, "after": after})
    reading = (f"Restructured {len(accepted)} of {len(rows)} high-impact terms with qualifier {qualifier_id!r}: "
               f"{count:,} to {after:,} records, no known record lost"
               + (f"; {len(rows) - len(accepted)} refused because they would lose a known record." if len(rows) > len(accepted) else ".")
               + ("" if dry_run or not accepted else " strategy.json is updated: run psb eval with a note."))
    return {"ok": True, "dry_run": dry_run, "qualifier": qualifier_id, "count_before": count, "count_after": after,
            "known_records_checked": len(hits), "terms": rows, "reading": reading}

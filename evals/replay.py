#!/usr/bin/env python3
"""Replay a scored development strategy through psb's own diagnostics. No agent, no model.

    python evals/replay.py miss TOPIC --card evals/results/TOPIC/<card>.json
    python evals/replay.py optional TOPIC --card <card>.json --blocks blocks.json
    python evals/replay.py impact TOPIC --card <card>.json

``miss`` runs ``psb terms miss`` on the gold records the card's strategy missed, and tallies the
cause it gives for each failing block. ``optional`` measures candidate blocks (a JSON list of
``{"id", "name", "terms"}``) as optional blocks of that strategy, with the gold set as the known
records: what AND-ing each would do to the count and to recall. ``impact`` runs
``psb eval --term-impact``: the records, and the gold records, that each term alone retrieves.

Both read the answer key, so they refuse anything but a development topic. They show what the
tools would have told an agent on a strategy an agent really delivered: a test of the tools that
costs NCBI requests only, to run before any agent run is paid for.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import harness  # noqa: E402
from psb import terms  # noqa: E402
from psb.evaluate import evaluate  # noqa: E402
from psb.workspace import Workspace, write_json  # noqa: E402

DATE_BOUND = re.compile(r"\[(edat|dp|crdt|pdat|date - publication|entry date)\]", re.I)


def split_top(text: str, operator: str) -> list[str]:
    """Split on a Boolean operator at parenthesis depth 0, outside quotes and field tags."""
    parts, depth, start, i = [], 0, 0, 0
    quoted = tagged = False
    needle = f" {operator} "
    while i < len(text):
        char = text[i]
        if char == '"' and not tagged:
            quoted = not quoted
        elif not quoted and char == "[":
            tagged = True
        elif not quoted and char == "]":
            tagged = False
        elif not quoted and not tagged:
            depth += char == "("
            depth -= char == ")"
            if depth == 0 and text.startswith(needle, i):
                parts.append(text[start:i])
                start = i + len(needle)
                i = start
                continue
        i += 1
    return [part.strip() for part in parts + [text[start:]] if part.strip()]


def unwrap(text: str) -> str:
    text = text.strip()
    while text.startswith("(") and text.endswith(")"):
        depth = 0
        for index, char in enumerate(text):
            depth += char == "("
            depth -= char == ")"
            if depth == 0 and index < len(text) - 1:
                return text  # the opening parenthesis closes early: not one wrapping pair
        text = text[1:-1].strip()
    return text


def is_date_bound(part: str) -> bool:
    inner = unwrap(part)
    return bool(DATE_BOUND.search(inner)) and ":" in inner and len(split_top(inner, "AND")) == len(split_top(inner, "OR")) == 1


def blocks_of(query: str) -> list[dict]:
    """A delivered single-line query as AND-ed blocks of OR-ed terms, without its date bound."""
    text = unwrap(" ".join(query.split()))
    while True:
        parts = [p for p in split_top(text, "AND") if not is_date_bound(p)]
        if len(parts) != 1 or unwrap(parts[0]) == text:
            break
        text = unwrap(parts[0])
    if any(split_top(unwrap(p), "NOT")[1:] for p in parts):
        raise SystemExit("the strategy has a top-level NOT; replay handles AND-ed blocks only")
    return [{"id": f"b{n}", "name": f"Block {n}", "terms": split_top(unwrap(part), "OR")} for n, part in enumerate(parts, 1)]


def workspace(fixture: dict, card: dict, optional: list[dict]) -> Workspace:
    ws = Workspace.create(Path(tempfile.mkdtemp(prefix="psb-replay-")), fixture["question"])
    blocks = blocks_of(card["strategy"])
    protocol = ws.protocol()
    protocol["concepts"] = ([{"id": b["id"], "name": b["name"], "role": "search"} for b in blocks]
                            + [{"id": b["id"], "name": b.get("name", ""), "role": "optional"} for b in optional])
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", {"blocks": blocks, "combine": None, "limits": [], "optional": optional})
    ws.save_set("gold", "benchmark", [str(p) for p in fixture["gold_pmids"]], source="fixture answer key (replay)")
    return ws


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["miss", "optional", "impact"])
    parser.add_argument("topic")
    parser.add_argument("--card", required=True, help="a scorecard under evals/results/ with a delivered strategy")
    parser.add_argument("--blocks", help="optional: JSON list of candidate blocks {id, name, terms}")
    args = parser.parse_args()
    fixture = harness.load_fixture(args.topic)
    if harness.split_of(fixture["id"]) != "dev":
        raise SystemExit(f"{fixture['id']} is not a development topic: replay reads the answer key")
    card = json.loads(Path(args.card).read_text(encoding="utf-8"))
    optional = json.loads(Path(args.blocks).read_text(encoding="utf-8")) if args.blocks else []
    if args.command == "optional" and not optional:
        raise SystemExit("optional needs --blocks")
    if fixture.get("as_of"):
        os.environ["PSB_AS_OF"] = fixture["as_of"]
    ws = workspace(fixture, card, optional)
    evaluation = evaluate(ws, term_counts=False, term_impact=args.command == "impact")
    if not evaluation["ok"]:
        print(json.dumps(evaluation["validation"]["blockers"], indent=2))
        return 1
    gold = evaluation["sets"]["gold"]
    out = {"topic": fixture["id"], "card": Path(args.card).name, "as_of": fixture.get("as_of"), "count": evaluation["count"],
           "blocks": [len(b.terms) for b in ws.strategy().blocks],
           "gold": {k: gold[k] for k in ("in_pubmed", "retrieved", "recall_percent")}}
    if args.command == "optional":
        out["optional_blocks"] = evaluation["optional_blocks"]
    elif args.command == "impact":
        out["term_impact"] = evaluation["term_impact"]
    else:
        records = list(ws.ensure_records(gold["missed"]).values())
        report = terms.miss_report(records, evaluation, ws.strategy())
        tally: dict[str, int] = {}
        for row in report:
            for found in row["diagnosis"]:
                tally[found["cause"]] = tally.get(found["cause"], 0) + 1
        out["causes"] = tally
        out["ablation"] = evaluation.get("ablation")
        out["misses"] = [{"pmid": r["pmid"], "title": r["title"], "has_abstract": r["has_abstract"],
                          "has_mesh": r["has_mesh"], "diagnosis": r["diagnosis"]} for r in report]
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Robustness of idea 6 (per-term structure) on development topics only.

    python evals/experiments/idea6_robustness.py [--out PATH]

For every distinct delivered strategy of each development topic, with the qualifiers of
ideas_6b_2b.py:
  - k: restructure the 3, 5 or 10 terms that alone add the most records;
  - weak qualifier: only the first third of the qualifier's terms (at least two), a stand-in for
    a qualifier written less well;
  - guard: with 30% of the gold standing in for the agent's known records, restructure the five
    terms one at a time and keep a change only if no known record is lost, as an agent would.
Reports records kept and gold lost (all gold and, for the guard, gold outside the known records).
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import harness  # noqa: E402
import replay  # noqa: E402
from ideas_126 import Lab, title_form  # noqa: E402
from ideas_6b_2b import DATE_TERM, QUALIFIERS, cards_for  # noqa: E402

KS = (3, 5, 10)
SEED = 1
KNOWN_SHARE = 0.3


def weak(q: str) -> str:
    parts = replay.split_top(q, "OR")
    keep = max(2, len(parts) // 3)
    return " OR ".join(parts[:keep])


def query(blocks: list[list[str]]) -> str:
    return " AND ".join(f"({' OR '.join(b)})" for b in blocks)


def restructure(blocks, chosen, q):
    out = [list(b) for b in blocks]
    for _, bi, ti, term in chosen:
        tf = title_form(term)
        out[bi][ti] = f"({tf} OR (({term}) AND ({q})))" if tf else f"(({term}) AND ({q}))"
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(ROOT / "experiments" / "results" / f"idea6_robustness-{date.today()}.json"))
    args = parser.parse_args()
    rows = []
    for topic in harness.load_splits()["dev"]:
        if topic not in QUALIFIERS:
            continue
        q, seen = QUALIFIERS[topic]
        fixture = harness.load_fixture(topic)
        if harness.split_of(fixture["id"]) != "dev":
            raise SystemExit("development topics only")
        lab = Lab(fixture)
        gold = sorted(lab.among("", [str(p) for p in fixture["gold_pmids"]]))
        rng = random.Random(SEED)
        known = set(rng.sample(gold, max(3, round(KNOWN_SHARE * len(gold)))))
        print(topic, file=sys.stderr)
        for label, card in cards_for(topic):
            try:
                blocks = [b["terms"] for b in replay.blocks_of(card["strategy"])]
            except SystemExit:
                continue
            delivered = query(blocks)
            base_gold = lab.among(delivered, gold)
            base_count = lab.count(delivered)
            impact = []
            for bi, block in enumerate(blocks):
                for ti, term in enumerate(block):
                    if DATE_TERM.search(term) or len(block) == 1:
                        continue
                    without = [list(b) for b in blocks]
                    without[bi] = [t for j, t in enumerate(block) if j != ti]
                    impact.append((lab.count(f"({delivered}) NOT ({query(without)})"), bi, ti, term))
            impact.sort(reverse=True)

            def measure(bs) -> dict:
                text = query(bs)
                hit = lab.among(text, gold)
                return {"kept": round(lab.count(text) / base_count, 3), "gold_lost": len(base_gold - hit),
                        "unseen_gold_lost": len((base_gold - hit) - known)}

            row = {"topic": topic, "card": label, "seen": seen, "delivered_count": base_count,
                   "gold_retrieved": len(base_gold)}
            for k in KS:
                row[f"k{k}"] = measure(restructure(blocks, impact[:k], q))
            row["k5_weak_qualifier"] = measure(restructure(blocks, impact[:5], weak(q)))
            accepted, refused = [], 0
            for item in impact[:5]:
                trial = restructure(blocks, accepted + [item], q)
                if known & base_gold - lab.among(query(trial), known & base_gold):
                    refused += 1
                    continue
                accepted.append(item)
            row["k5_guarded"] = {**measure(restructure(blocks, accepted, q)), "terms_refused": refused}
            rows.append(row)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps({"date": str(date.today()), "rows": rows}, indent=2) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

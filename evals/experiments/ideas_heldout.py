#!/usr/bin/env python3
"""Ideas 6, 2 and 1 on the held-out (frozen) suite, under the held-out rules.

    python evals/experiments/ideas_heldout.py --heldout [--out PATH]

The rules are fixed by evals/README.md: every topic touched is logged in heldout-ledger.jsonl,
and only aggregate counts are kept: no PMIDs, no missed records, no ranks of lost records and no
words drawn from gold abstracts. The qualifiers and the grid below were written from each
question and its eligibility criteria and committed before this script was first run.
healthcare-nudging is reported separately: its source review was read while these ideas were
developed, so it is not a blind test.
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
from ideas_126 import Lab, naive_detect  # noqa: E402
from ideas_6b_2b import KNOWN_SHARE, SEED, cards_for, rank_terms, structure  # noqa: E402

TRIALS = ('"Randomized Controlled Trial"[pt] OR "Controlled Clinical Trial"[pt] OR random*[tiab] OR trial*[tiab] '
          'OR placebo[tiab] OR compar*[tiab] OR "Treatment Outcome"[Mesh] OR outcome*[tiab] OR mortality[tiab] '
          'OR adverse[tiab] OR safety[tiab] OR harm*[tiab]')

QUALIFIERS = {
    "Cohen_2006_ACEInhibitors": TRIALS,
    "Cohen_2006_ADHD": TRIALS,
    "Cohen_2006_Antihistamines": TRIALS,
    "Cohen_2006_Estrogens": TRIALS,
    "Cohen_2006_UrinaryIncontinence": TRIALS,
    "housing-first-criminal-justice": ('"Criminal Law"[Mesh] OR "Crime"[Mesh] OR "Prisons"[Mesh] OR "Police"[Mesh] OR arrest*[tiab] '
                                       'OR incarcerat*[tiab] OR jail*[tiab] OR prison*[tiab] OR crime*[tiab] OR criminal*[tiab] '
                                       'OR police[tiab] OR justice[tiab] OR offend*[tiab] OR "Mental Disorders"[Mesh] '
                                       'OR "mental illness*"[tiab] OR psychiatric[tiab]'),
    "school-restorative-practice": ('effect*[tiab] OR outcome*[tiab] OR evaluat*[tiab] OR impact*[tiab] OR implement*[tiab] '
                                    'OR suspension*[tiab] OR exclusion*[tiab] OR disciplin*[tiab] OR behavio*[tiab] OR climate[tiab]'),
    "social-prescribing-older-adults": ('"Aged"[Mesh] OR older[tiab] OR elderly[tiab] OR "later life"[tiab] OR seniors[tiab] '
                                        'OR aged[tiab] OR "Loneliness"[Mesh] OR loneliness[tiab] OR "social isolation"[tiab] '
                                        'OR wellbeing[tiab] OR well-being[tiab]'),
    "work-directed-return-to-work": ('"Sick Leave"[Mesh] OR "Absenteeism"[Mesh] OR "sick leave"[tiab] OR "sickness absence"[tiab] '
                                     'OR "sick-listed"[tiab] OR absenteeism[tiab] OR "work disability"[tiab] OR employee*[tiab] '
                                     'OR worker*[tiab] OR employ*[tiab]'),
    "healthcare-nudging": ('"Guideline Adherence"[Mesh] OR "Practice Patterns, Physicians\'"[Mesh] OR guideline*[tiab] '
                           'OR "evidence-based"[tiab] OR appropriate*[tiab] OR inappropriate*[tiab] OR adherence[tiab] '
                           'OR complian*[tiab] OR recommend*[tiab] OR prescrib*[tiab] OR ordering[tiab]'),
}
NOT_BLIND = {"healthcare-nudging"}

GRID = {
    "social-prescribing-older-adults": {
        "rows": {
            "link worker or navigator": '"link worker*"[tiab] OR "community navigator*"[tiab] OR "care navigator*"[tiab] OR "Patient Navigation"[Mesh] OR "community connector*"[tiab]',
            "social or community referral": '"social prescri*"[tiab] OR "community referral*"[tiab] OR "non-medical referral*"[tiab] OR "referral to community"[tiab] OR "community-based referral*"[tiab]',
            "arts or culture": '"arts on prescription"[tiab] OR "arts-based"[tiab] OR "arts for health"[tiab] OR museum*[tiab] OR singing[tiab] OR choir*[tiab] OR "creative arts"[tiab]',
            "nature or green": '"green prescription*"[tiab] OR "nature-based"[tiab] OR gardening[tiab] OR "ecotherapy"[tiab] OR "blue prescription*"[tiab]',
            "exercise referral": '"exercise referral*"[tiab] OR "exercise on prescription"[tiab] OR "physical activity referral*"[tiab]',
            "befriending or volunteering": 'befriend*[tiab] OR volunteer*[tiab] OR "peer support"[tiab] OR "lunch club*"[tiab] OR "men\'s shed*"[tiab]',
        },
        "columns": {
            "older adults with loneliness or wellbeing outcomes": ('("Aged"[Mesh] OR older[tiab] OR elderly[tiab] OR "later life"[tiab] OR seniors[tiab]) '
                                                                   'AND ("Loneliness"[Mesh] OR loneliness[tiab] OR "social isolation"[tiab] OR wellbeing[tiab] '
                                                                   'OR well-being[tiab] OR "quality of life"[tiab] OR "mental health"[tiab])'),
        },
    },
}


def held_out(topic: str) -> dict:
    fixture = harness.load_fixture(topic)
    if harness.split_of(fixture["id"]) != "heldout":
        raise SystemExit(f"{topic} is not a held-out topic")
    return fixture


def run_topic(topic: str, q: str) -> dict:
    fixture = held_out(topic)
    harness.record_heldout_look({"topic": fixture["id"], "command": "experiment ideas_heldout (ideas 6 and 2)",
                                 "kept": "aggregate counts only"})
    lab = Lab(fixture)
    gold = sorted(lab.among("", [str(p) for p in fixture["gold_pmids"]]))
    rows, last = [], None
    for label, card in cards_for(topic):
        try:
            result = structure(lab, card, q, gold)
        except SystemExit as exc:
            rows.append({"card": label, "skipped": str(exc)})
            continue
        queries = result.pop("_queries")
        result["generic_terms"] = [g["term"] for g in result["generic_terms"]]
        rows.append({"card": label, "gold": len(gold), **result})
        last = queries
    cuts = []
    if last:
        rng = random.Random(SEED)
        known = rng.sample(gold, max(3, round(KNOWN_SHARE * len(gold))))
        unseen = set(gold) - set(known)
        words = rank_terms(lab, known)
        named = {"AND the qualifier": last["and_qualifier"]}
        named.update({f"drop the term with rank {i + 1} by records only it retrieves": text
                      for i, (_, _, text) in enumerate(last["drops"])})
        for name, after in named.items():
            cut = f"({last['delivered']}) NOT ({after})"
            lost = lab.among(cut, unseen)
            ordered = lab.pm.search(f"({cut}) AND ({' OR '.join(chr(34) + w + chr(34) + '[tiab]' for w in words)})",
                                    retmax=200, sort="relevance")["pmids"]
            found = [ordered.index(p) + 1 for p in lost if p in ordered]
            size = lab.count(cut)
            cuts.append({"cut": name, "records_cut": size, "gold_lost_true": len(lost),
                         "lost_found_in_top_50": sum(r <= 50 for r in found), "lost_found_in_top_200": len(found),
                         "random_10_shows_any_loss_probability": round(naive_detect(size, len(lost)), 3)})
    return {"topic": fixture["id"], "blind": topic not in NOT_BLIND, "strategies": rows, "cuts": cuts}


def run_grid(topic: str, spec: dict) -> list[dict]:
    fixture = held_out(topic)
    harness.record_heldout_look({"topic": fixture["id"], "command": "experiment ideas_heldout (idea 1 grid)",
                                 "kept": "aggregate counts only"})
    lab = Lab(fixture)
    gold = sorted(lab.among("", [str(p) for p in fixture["gold_pmids"]]))
    from ideas_126 import strip_date
    out = []
    for label, card in cards_for(topic):
        delivered = strip_date(card["strategy"])
        missed = set(gold) - lab.among(delivered, gold)
        parts = [f"(({r}) AND ({c}))" for r in spec["rows"].values() for c in spec["columns"].values()]
        union = f"({' OR '.join(parts)}) NOT ({delivered})"
        found = lab.among(union, missed) if missed else set()
        out.append({"card": label, "delivered_count": lab.count(delivered), "gold": len(gold), "missed": len(missed),
                    "grid_records": lab.count(union), "misses_found": len(found)})
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--heldout", action="store_true", help="required: this script reads held-out answer keys")
    parser.add_argument("--out", default=str(ROOT / "experiments" / "results" / f"ideas_heldout-{date.today()}.json"))
    args = parser.parse_args()
    if not args.heldout:
        raise SystemExit("pass --heldout: every topic touched is logged in heldout-ledger.jsonl")
    out = {"date": str(date.today()), "idea_6_and_2": [], "idea_1": {}}
    for topic, q in QUALIFIERS.items():
        print(f"ideas 6 and 2: {topic}", file=sys.stderr)
        out["idea_6_and_2"].append(run_topic(topic, q))
    for topic, spec in GRID.items():
        print(f"idea 1: {topic}", file=sys.stderr)
        out["idea_1"][topic] = run_grid(topic, spec)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

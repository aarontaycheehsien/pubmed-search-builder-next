#!/usr/bin/env python3
"""Second tests of idea 6 (per-term structure) and idea 2 (ranked cut estimates). Development
topics only: both read the answer key.

    python evals/experiments/ideas_6b_2b.py [--out PATH] [--only 6|2]

Idea 6, every development card: in each delivered strategy, the five terms that alone add the most
records, wherever they sit, are each replaced by (term in the title) OR (term AND qualifier),
where the qualifier is a concept from the question the strategy does not search. The rule is
automatic; only the qualifiers are written by hand, from each question and its eligibility
criteria. Qualifiers for the five topics of the first run (marked seen=True) were written before
that run; the other thirteen were written before this one, before any result for them was seen.

Idea 2, a text ranker: 30% of the gold stands in for an agent's known records. Words that are
common in those records and rare in PubMed become a ranking query; each cut is ranked by
PubMed's own relevance order on that query, the top 50 and top 200 are inspected, and 30 more
records are drawn at random from the rest. Run on the latest card of each topic, for the cut made
by AND-ing the qualifier and the cuts made by dropping each of the three highest-impact terms.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import harness  # noqa: E402
import replay  # noqa: E402
from ideas_126 import QUALIFIERS as FIRST, Lab, clopper_upper, naive_detect, title_form  # noqa: E402

GENERIC_K = 5
SEED = 1
KNOWN_SHARE = 0.3
TAIL_N = 30
RANK_TERMS = 20

QUALIFIERS = {name: (q, True) for name, q in FIRST.items()}
QUALIFIERS.update({
    "Appenzeller-Herzog_2019": ('"Treatment Outcome"[Mesh] OR "Comparative Effectiveness Research"[Mesh] OR treat*[tiab] '
                                'OR therap*[tiab] OR outcome*[tiab] OR efficacy[tiab] OR effective*[tiab] OR survival[tiab] '
                                'OR adverse[tiab] OR cohort*[tiab] OR trial*[tiab]', False),
    "Brouwer_2019": ('"Psychological Theory"[Mesh] OR "Cognition"[Mesh] OR "Personality"[Mesh] OR "Stress, Psychological"[Mesh] '
                     'OR cognit*[tiab] OR psycholog*[tiab] OR theor*[tiab] OR model*[tiab] OR rumination[tiab] OR schema*[tiab] '
                     'OR personality[tiab] OR stress*[tiab] OR predict*[tiab] OR "risk factor*"[tiab] OR vulnerab*[tiab]', False),
    "CD010657": ('"Urinary Tract Infections"[Mesh] OR "urinary tract infection*"[tiab] OR UTI[tiab] OR UTIs[tiab] '
                 'OR pyelonephritis[tiab] OR "Child"[Mesh] OR "Infant"[Mesh] OR child*[tiab] OR infant*[tiab] OR pediatric*[tiab] '
                 'OR paediatric*[tiab]', False),
    "CD011431": ('"Sensitivity and Specificity"[Mesh] OR sensitivity[tiab] OR specificity[tiab] OR accuracy[tiab] '
                 'OR "predictive value*"[tiab] OR microscop*[tiab] OR PCR[tiab] OR "reference standard"[tiab] OR diagnos*[ti]', False),
    "CD011926": ('"Sensitivity and Specificity"[Mesh] OR sensitivity[tiab] OR specificity[tiab] OR accuracy[tiab] '
                 'OR "predictive value*"[tiab] OR "blood culture*"[tiab] OR "reference standard"[tiab] OR diagnos*[ti]', False),
    "Donners_2021": ('"Pharmacokinetics"[Mesh] OR pharmacokinetic*[tiab] OR PK[tiab] OR concentration*[tiab] OR exposure[tiab] '
                     'OR "bleeding rate*"[tiab] OR bleed*[tiab] OR efficacy[tiab] OR trial*[tiab] OR "Hemophilia A"[Mesh] '
                     'OR haemophilia[tiab] OR hemophilia[tiab]', False),
    "Kwok_2020": ('"High-Throughput Nucleotide Sequencing"[Mesh] OR "Metagenomics"[Mesh] OR metagenom*[tiab] OR sequenc*[tiab] '
                  'OR virom*[tiab] OR "next-generation"[tiab] OR NGS[tiab] OR "deep sequencing"[tiab]', False),
    "Liu_2023_VR_nursing": ('"Educational Measurement"[Mesh] OR knowledge[tiab] OR skill*[tiab] OR performance[tiab] '
                            'OR satisfaction[tiab] OR "critical thinking"[tiab] OR random*[tiab] OR trial*[tiab] '
                            'OR "control group"[tiab] OR "quasi-experimental"[tiab] OR compar*[tiab]', False),
    "Meijboom_2021": ('originator*[tiab] OR "reference product*"[tiab] OR "reference medicin*"[tiab] OR "back to"[tiab] '
                      'OR retransition*[tiab] OR re-switch*[tiab] OR reverse*[tiab] OR discontinu*[tiab] OR retention[tiab] '
                      'OR "Drug Substitution"[Mesh] OR switch*[tiab]', False),
    "Muthu_2022": ('"Wound Healing"[Mesh] OR "Treatment Outcome"[Mesh] OR heal*[tiab] OR retear*[tiab] OR re-tear*[tiab] '
                   'OR repair*[tiab] OR augment*[tiab] OR outcome*[tiab] OR random*[tiab] OR trial*[tiab] OR control*[tiab]', False),
    "Oud_2018": ('"Randomized Controlled Trial"[pt] OR random*[tiab] OR trial*[tiab] OR controlled[tiab] '
                 'OR "Treatment Outcome"[Mesh] OR efficacy[tiab] OR effective*[tiab] OR outcome*[tiab]', False),
    "Smid_2020": ('"small sample*"[tiab] OR "sample size*"[tiab] OR simulation*[tiab] OR "Monte Carlo"[tiab] '
                  'OR "maximum likelihood"[tiab] OR frequentist[tiab] OR bias[tiab] OR "Computer Simulation"[Mesh] '
                  'OR "Sample Size"[Mesh] OR estimat*[tiab]', False),
    "gao-2026-Immune checkpoint inhibitors": ('"Neoadjuvant Therapy"[Mesh] OR neoadjuvant[tiab] OR "neo-adjuvant"[tiab] '
                                              'OR adjuvant[tiab] OR early[tiab] OR "early-stage"[tiab] OR "stage II"[tiab] '
                                              'OR "stage III"[tiab] OR operable[tiab] OR "pathological complete response"[tiab] '
                                              'OR pCR[tiab] OR perioperative[tiab]', False),
})

DATE_TERM = re.compile(r"\[(date - |edat|dp|pdat|crdt)", re.I)
STOP = set("""about above after again against also among an and any are because been before being below between both but by
can could did does doing during each from further had has have having here how into its itself more most other our out over
own same should some such than that their them then there these they this those through under until very was were what when
where which while who whom why will with would your study studies patients results methods conclusions background using used
based between total compared group groups however among within were more than including include included years year data
analysis associated associations significant significantly showed show shown found two three four one also well high higher low
lower may might new non per use participants after during whether vs versus objective objectives aim aims purpose""".split())


def cards_for(topic: str) -> list[tuple[str, dict]]:
    folder = ROOT / "results" / topic.replace(" ", "_")
    out, seen = [], set()
    for path in sorted(folder.glob("*.json")):
        card = json.loads(path.read_text(encoding="utf-8"))
        if not card.get("strategy") or not str(card.get("source", "")).startswith("generated:"):
            continue
        key = " ".join(card["strategy"].split())
        if key in seen:
            continue
        seen.add(key)
        out.append((path.stem, card))
    return out


def structure(lab: Lab, card: dict, q: str, gold: list[str]) -> dict:
    blocks = [b["terms"] for b in replay.blocks_of(card["strategy"])]

    def query(bs: list[list[str]]) -> str:
        return " AND ".join(f"({' OR '.join(b)})" for b in bs)

    delivered = query(blocks)
    impact = []
    for bi, block in enumerate(blocks):
        for ti, term in enumerate(block):
            if DATE_TERM.search(term) or len(block) == 1:
                continue
            without = [list(b) for b in blocks]
            without[bi] = [t for j, t in enumerate(block) if j != ti]
            impact.append((lab.count(f"({delivered}) NOT ({query(without)})"), bi, ti, term))
    impact.sort(reverse=True)
    chosen = impact[:GENERIC_K]
    hybrid = [list(b) for b in blocks]
    no_title = [list(b) for b in blocks]
    for _, bi, ti, term in chosen:
        tf = title_form(term)
        hybrid[bi][ti] = f"({tf} OR (({term}) AND ({q})))" if tf else f"(({term}) AND ({q}))"
        no_title[bi][ti] = f"(({term}) AND ({q}))"

    def measure(text: str) -> dict:
        hit = lab.among(text, gold)
        return {"count": lab.count(text), "gold_retrieved": len(hit)}

    return {"delivered": measure(delivered), "hybrid": measure(query(hybrid)), "hybrid_no_title": measure(query(no_title)),
            "and_qualifier": measure(f"({delivered}) AND ({q})"),
            "generic_terms": [{"term": t, "records_only_it_retrieves": u} for u, _, _, t in chosen],
            "_queries": {"delivered": delivered, "and_qualifier": f"({delivered}) AND ({q})",
                         "drops": [(t, u, query([[x for j, x in enumerate(b) if not (i == bi and j == ti)]
                                                 for i, b in enumerate(blocks)]))
                                   for u, bi, ti, t in chosen[:3]]}}


def rank_terms(lab: Lab, known: list[str]) -> list[str]:
    records = lab.pm.fetch(known)
    docs = []
    for r in records:
        text = f"{r.get('title') or ''} {r.get('abstract') or ''}".lower()
        words = [w for w in re.findall(r"[a-z][a-z-]{3,}", text) if w not in STOP]
        grams = set(words) | {f"{a} {b}" for a, b in zip(words, words[1:])}
        docs.append(grams)
    df: dict[str, int] = {}
    for grams in docs:
        for g in grams:
            df[g] = df.get(g, 0) + 1
    k = max(1, len(docs))
    floor = max(2, math.ceil(0.2 * k))
    candidates = sorted((g for g, n in df.items() if n >= floor), key=lambda g: -df[g])[:60]
    total = lab.count("all[sb]")
    scored = []
    for g in candidates:
        bg = lab.count(f'"{g}"[tiab]')
        scored.append((math.log((df[g] + 0.5) / (k + 1)) - math.log((bg + 1) / total), g))
    scored.sort(reverse=True)
    return [g for _, g in scored[:RANK_TERMS]]


def ranked_cut(lab: Lab, before: str, after: str, unseen: set[str], words: list[str], rng: random.Random) -> dict:
    cut = f"({before}) NOT ({after})"
    size = lab.count(cut)
    lost = lab.among(cut, unseen)
    rank_q = f"({cut}) AND ({' OR '.join(chr(34) + w + chr(34) + '[tiab]' for w in words)})"
    ordered = lab.pm.search(rank_q, retmax=200, sort="relevance")["pmids"]
    matched = lab.count(rank_q)
    ranks = sorted(ordered.index(p) + 1 for p in lost if p in ordered)
    out = {"records_cut": size, "gold_lost_true": len(lost), "records_matching_rank_words": matched,
           "lost_in_rank_word_set": len(lab.among(rank_q, lost)) if lost else 0,
           "lost_found_in_top_50": sum(r <= 50 for r in ranks), "lost_found_in_top_200": len(ranks), "ranks": ranks,
           "random_10_shows_any_loss_probability": round(naive_detect(size, len(lost)), 3)}
    if lost:
        top = set(ordered[:50])
        sample = lab.random_sample(cut, TAIL_N, rng, top)
        found_tail = sum(p in unseen for p in sample)
        tail = size - len(top)
        found_top = sum(p in unseen for p in ordered[:50])
        share = found_tail / len(sample) if sample else 0.0
        out["estimate_gold_lost_top50_plus_tail"] = round(found_top + share * tail, 1)
        out["upper_95"] = round(found_top + clopper_upper(found_tail, len(sample)) * tail, 1)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(ROOT / "experiments" / "results" / f"ideas_6b_2b-{date.today()}.json"))
    parser.add_argument("--only", choices=["6", "2"])
    args = parser.parse_args()
    dev = harness.load_splits()["dev"]
    out = {"date": str(date.today()), "settings": {"generic_k": GENERIC_K, "seed": SEED, "known_share": KNOWN_SHARE,
                                                   "rank_terms": RANK_TERMS, "tail_n": TAIL_N},
           "idea_6": [], "idea_2": []}
    for topic in dev:
        if topic not in QUALIFIERS:
            print(f"skip {topic}: no qualifier", file=sys.stderr)
            continue
        q, seen = QUALIFIERS[topic]
        fixture = harness.load_fixture(topic)
        lab = Lab(fixture)
        gold = sorted(lab.among("", [str(p) for p in fixture["gold_pmids"]]))
        cards = cards_for(topic)
        print(f"{topic}: {len(cards)} distinct strategies", file=sys.stderr)
        last = None
        for label, card in cards:
            try:
                result = structure(lab, card, q, gold)
            except SystemExit as exc:
                out["idea_6"].append({"topic": topic, "card": label, "skipped": str(exc)})
                continue
            queries = result.pop("_queries")
            if args.only != "2":
                out["idea_6"].append({"topic": topic, "card": label, "qualifier_written_after_seeing_results": seen,
                                      "gold": len(gold), **result})
            last = (label, queries)
        if args.only == "6" or last is None:
            continue
        rng = random.Random(SEED)
        known = rng.sample(gold, max(3, round(KNOWN_SHARE * len(gold))))
        unseen = set(gold) - set(known)
        words = rank_terms(lab, known)
        label, queries = last
        cuts = {"AND the qualifier": queries["and_qualifier"]}
        for term, unique, text in queries["drops"]:
            cuts[f"drop {term} ({unique})"] = text
        out["idea_2"].append({"topic": topic, "card": label, "known": len(known), "unseen": len(unseen), "rank_words": words,
                              "cuts": {name: ranked_cut(lab, queries["delivered"], after, unseen, words, rng)
                                       for name, after in cuts.items()}})
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

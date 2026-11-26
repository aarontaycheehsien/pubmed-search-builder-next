#!/usr/bin/env python3
"""Prototype tests of three ideas on development topics only (they read the answer key).

    python evals/experiments/ideas_126.py [--out PATH]

Idea 6, per-term structure: in one block, the terms that alone add the most records ("generic")
are kept in the title alone, or in title or abstract only together with a qualifier concept;
the other terms are unchanged. Compared with the delivered strategy and with AND-ing the
qualifier to the whole strategy.

Idea 2, ranked difference sampling: for a cut (records the narrower strategy no longer
retrieves), estimate the gold records it loses without the answer key, from 30% of the gold
standing in for an agent's known records: rank the cut by PubMed similar-article scores of those
records, screen the top 50, add a random sample of 30 from the rest, and estimate. Compared with
the truth and with the chance that a random sample of 10 shows any loss at all.

Idea 1, grid probes: cells of concept-member x concept-member queries, excluding the delivered
strategy, for strategies that miss gold records. Reports how many misses the cells hold and
how many records they cost to screen.

Qualifiers and grid cells were written from each question before any miss was inspected.
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

import harness  # noqa: E402
import replay  # noqa: E402

UID_LIMIT = 9999
TOP_K = 50
TAIL_N = 30
NAIVE_N = 10
KNOWN_SHARE = 0.3
SEED = 1

CARDS = {
    "Bos_2018": "pubmed-search-builder-next-codex-noseed-20260927T002230Z",
    "Medeiros-2022-School-based food and nutrition education interventions for adolescent food consumption":
        "lean-fixes-codex-noseed-20261002T140005Z",
    "van_de_Schoot_2018": "ours-codex-noseed-20260927T152747Z",
    "Welling_2021": "ours-codex-noseed-20260927T145733Z",
    "van_Dis_2020": "ours-codex-noseed-20260928T030852Z",
}

QUALIFIERS = {
    "Bos_2018": ('"Dementia"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] '
                 'OR "Neuropsychological Tests"[Mesh] OR dementia*[tiab] OR alzheimer*[tiab] OR cognit*[tiab] OR memory[tiab] '
                 'OR "executive function*"[tiab] OR "processing speed"[tiab] OR "mild cognitive impairment"[tiab]'),
    "Medeiros-2022-School-based food and nutrition education interventions for adolescent food consumption":
        ('"Schools"[Mesh] OR "School Health Services"[Mesh] OR school*[tiab] OR classroom*[tiab] OR curricul*[tiab] '
         'OR student*[tiab] OR pupil*[tiab]'),
    "van_de_Schoot_2018": ('trajector*[tiab] OR "growth mixture"[tiab] OR "latent class growth"[tiab] OR "latent growth"[tiab] '
                           'OR "growth curve*"[tiab] OR course[tiab] OR longitudinal[tiab] OR "Longitudinal Studies"[Mesh]'),
    "Welling_2021": ('"Life Style"[Mesh] OR "Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Sleep"[Mesh] OR "Diet"[Mesh] '
                     'OR "Feeding Behavior"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Smoking"[Mesh] OR "Mental Health"[Mesh] '
                     'OR "Quality of Life"[Mesh] OR lifestyle*[tiab] OR "physical activit*"[tiab] OR exercis*[tiab] '
                     'OR sedentar*[tiab] OR sleep*[tiab] OR diet*[tiab] OR eating[tiab] OR food[tiab] OR alcohol*[tiab] '
                     'OR drinking[tiab] OR smok*[tiab] OR tobacco[tiab] OR "screen time"[tiab] OR well-being[tiab] '
                     'OR wellbeing[tiab] OR "mental health"[tiab] OR "quality of life"[tiab] OR weight[tiab]'),
    "van_Dis_2020": ('"Follow-Up Studies"[Mesh] OR "follow-up"[tiab] OR "long-term"[tiab] OR "long term"[tiab] OR months[tiab] '
                     'OR years[tiab] OR maintenance[tiab] OR durab*[tiab] OR relapse[tiab]'),
}

PANDEMIC = ('lockdown*[tiab] OR "lock-down"[tiab] OR quarantine*[tiab] OR confinement[tiab] OR "stay-at-home"[tiab] '
            'OR "stay at home"[tiab] OR "social distancing"[tiab] OR pandemic[tiab] OR covid*[tiab] OR "SARS-CoV-2"[tiab] '
            'OR coronavirus[tiab]')
TRAJECTORY = ('trajector*[tiab] OR "growth mixture"[tiab] OR "latent class growth"[tiab] OR "latent growth"[tiab] '
              'OR "growth curve*"[tiab]')
LONGTERM_TRIAL = (f'({QUALIFIERS["van_Dis_2020"]}) AND (random*[tiab] OR trial*[tiab] OR "Randomized Controlled Trial"[pt])')
BAYES = ('"Bayes Theorem"[Mesh] OR bayes*[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "Gibbs sampl*"[tiab] '
         'OR "prior distribution*"[tiab] OR "informative prior*"[tiab]')
SWITCH = ('switch*[tiab] OR transition*[tiab] OR discontinu*[tiab] OR retention[tiab] OR "back to"[tiab] OR reverse*[tiab] '
          'OR re-switch*[tiab] OR retransition*[tiab] OR substitut*[tiab]')

GRIDS = {
    "van_de_Schoot_2018": {
        "card": "ours-codex-noseed-20260927T152747Z", "blind": False,
        "note": "docs/recall-precision-plan.md already says this topic's misses use 'distress' or 'acute stress' and name trajectories",
        "rows": {
            "injury or accident": '"Wounds and Injuries"[Mesh] OR injur*[tiab] OR accident*[tiab] OR trauma*[tiab] OR burn*[tiab]',
            "military": '"Military Personnel"[Mesh] OR "Veterans"[Mesh] OR military[tiab] OR veteran*[tiab] OR soldier*[tiab] OR combat[tiab] OR deploy*[tiab]',
            "disaster or terrorism": '"Disasters"[Mesh] OR disaster*[tiab] OR earthquake*[tiab] OR hurricane*[tiab] OR tsunami*[tiab] OR flood*[tiab] OR terror*[tiab]',
            "violence": '"Violence"[Mesh] OR "Crime Victims"[Mesh] OR assault*[tiab] OR violen*[tiab] OR abuse*[tiab] OR rape[tiab]',
            "medical event": '"Critical Illness"[Mesh] OR "Intensive Care Units"[Mesh] OR "intensive care"[tiab] OR cancer[tiab] OR "myocardial infarction"[tiab] OR surgery[tiab]',
        },
        "columns": {"distress or stress symptoms": '"Stress, Psychological"[Mesh] OR distress[tiab] OR "acute stress"[tiab] OR "stress symptom*"[tiab] OR posttraumatic[tiab] OR post-traumatic[tiab] OR "psychological symptom*"[tiab] OR resilien*[tiab]'},
        "extra": TRAJECTORY,
    },
    "Welling_2021": {
        "card": "lean-optimal-codex-noseed-20260927T150952Z", "blind": True, "note": "",
        "rows": {
            "physical activity": '"Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "physical activit*"[tiab] OR exercis*[tiab] OR sedentar*[tiab] OR sitting[tiab] OR steps[tiab]',
            "sleep": '"Sleep"[Mesh] OR sleep*[tiab] OR insomnia*[tiab]',
            "diet": '"Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR diet*[tiab] OR eating[tiab] OR food*[tiab] OR snack*[tiab] OR nutrition*[tiab]',
            "alcohol": '"Alcohol Drinking"[Mesh] OR alcohol*[tiab] OR drinking[tiab] OR binge*[tiab]',
            "smoking": '"Smoking"[Mesh] OR smok*[tiab] OR tobacco[tiab] OR cigarette*[tiab] OR vaping[tiab]',
            "screen time": '"Screen Time"[Mesh] OR "screen time"[tiab] OR "media use"[tiab] OR "social media"[tiab] OR gaming[tiab] OR television[tiab]',
            "well-being": '"Mental Health"[Mesh] OR well-being[tiab] OR wellbeing[tiab] OR "mental health"[tiab] OR loneliness[tiab] OR "life satisfaction"[tiab] OR "psychological distress"[tiab]',
            "body weight": '"Body Weight"[Mesh] OR weight[tiab] OR BMI[tiab] OR obesity[tiab]',
        },
        "columns": {"pandemic or lockdown": PANDEMIC},
        "extra": None,
    },
    "van_Dis_2020": {
        "card": "lean-optimal-codex-noseed-20260927T151732Z", "blind": True, "note": "",
        "rows": {
            "panic or agoraphobia": '"Panic Disorder"[Mesh] OR "Agoraphobia"[Mesh] OR panic[tiab] OR agoraphob*[tiab]',
            "social anxiety": '"Phobia, Social"[Mesh] OR "social anxiety"[tiab] OR "social phobia"[tiab]',
            "generalised anxiety": '"generalized anxiety"[tiab] OR "generalised anxiety"[tiab] OR GAD[tiab] OR worry[tiab]',
            "specific phobia": '"Phobic Disorders"[Mesh] OR phobi*[tiab] OR fear*[tiab]',
            "OCD": '"Obsessive-Compulsive Disorder"[Mesh] OR obsessive*[tiab] OR OCD[tiab]',
            "PTSD": '"Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR posttraumatic[tiab] OR post-traumatic[tiab]',
            "health anxiety": '"Hypochondriasis"[Mesh] OR "health anxiety"[tiab] OR hypochondri*[tiab]',
        },
        "columns": {
            "cognitive behavioural therapy": '"Cognitive Behavioral Therapy"[Mesh] OR "cognitive behavio*"[tiab] OR CBT[tiab] OR "cognitive therap*"[tiab] OR "cognitive restructuring"[tiab]',
            "exposure-based therapy": '"Implosive Therapy"[Mesh] OR exposure[tiab] OR "response prevention"[tiab] OR desensiti*[tiab]',
        },
        "extra": LONGTERM_TRIAL,
    },
    "Smid_2020": {
        "card": "ours-codex-noseed-20260927T145334Z", "blind": False,
        "note": "references/anti-patterns.md (mistake 16) already names the SEM family members for this kind of question",
        "rows": {
            "confirmatory factor analysis": '"confirmatory factor"[tiab] OR CFA[tiab] OR "factor analy*"[tiab] OR "Factor Analysis, Statistical"[Mesh]',
            "latent growth": '"latent growth"[tiab] OR "growth curve*"[tiab] OR "growth model*"[tiab]',
            "latent class or mixture": '"latent class"[tiab] OR "mixture model*"[tiab] OR "finite mixture"[tiab]',
            "multilevel": 'multilevel[tiab] OR multi-level[tiab] OR hierarchical[tiab] OR "random effect*"[tiab] OR "Multilevel Analysis"[Mesh]',
            "mediation": 'mediation[tiab] OR "indirect effect*"[tiab]',
            "item response": '"item response"[tiab] OR IRT[tiab]',
        },
        "columns": {"Bayesian estimation": BAYES},
        "extra": None,
    },
    "Meijboom_2021": {
        "card": "ours-codex-noseed-20260927T111214Z", "blind": False,
        "note": "references/anti-patterns.md (mistake 15) is about this kind of question",
        "rows": {
            "infliximab": 'infliximab[tiab] OR "CT-P13"[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR Flixabi[tiab] OR SB2[tiab]',
            "etanercept": 'etanercept[tiab] OR SB4[tiab] OR Benepali[tiab] OR GP2015[tiab] OR Erelzi[tiab]',
            "adalimumab": 'adalimumab[tiab] OR "ABP 501"[tiab] OR Amgevita[tiab] OR SB5[tiab] OR Imraldi[tiab] OR GP2017[tiab] OR Hyrimoz[tiab]',
        },
        "columns": {"switching or discontinuation": SWITCH},
        "extra": None,
    },
}


def load(topic: str, label: str) -> tuple[dict, dict]:
    fixture = harness.load_fixture(topic)
    if harness.split_of(fixture["id"]) != "dev":
        raise SystemExit(f"{topic} is not a development topic")
    folder = ROOT / "results" / fixture["id"].replace(" ", "_")
    card = json.loads(next(folder.glob(f"{label}*.json")).read_text(encoding="utf-8"))
    return fixture, card


def strip_date(query: str) -> str:
    blocks = replay.blocks_of(query)
    return " AND ".join(f"({' OR '.join(b['terms'])})" for b in blocks)


def title_form(term: str) -> str | None:
    match = re.match(r"^(.*)\[(tiab|title/abstract)(:~\d+)?\]$", term.strip(), re.I)
    if not match:
        return None
    return f"{match.group(1)}[ti{match.group(3) or ''}]"


class Lab:
    def __init__(self, fixture: dict):
        self.fixture = fixture
        self.pm = harness.client(fixture)
        self.counts: dict[str, int] = {}

    def count(self, query: str) -> int:
        if query not in self.counts:
            self.counts[query] = self.pm.count(query)
        return self.counts[query]

    def among(self, query: str, pmids) -> set[str]:
        pmids = sorted(set(pmids))
        return self.pm.among(query, pmids) if pmids else set()

    def ids(self, query: str) -> list[str]:
        return self.pm.search(query, retmax=UID_LIMIT)["pmids"]

    def slices(self, query: str) -> list[tuple[str, int]]:
        """Entry-date slices of a query, each small enough to list in full."""
        end_year = int((self.fixture.get("as_of") or str(date.today()))[:4])
        out: list[tuple[str, int]] = []

        def visit(lo: date, hi: date, step: str) -> None:
            bound = f'("{lo:%Y/%m/%d}"[edat] : "{hi:%Y/%m/%d}"[edat])'
            n = self.count(f"({query}) AND {bound}")
            if n == 0:
                return
            if n <= UID_LIMIT or step == "day":
                out.append((bound, n))
                return
            if step == "decade":
                for y in range(lo.year, hi.year + 1):
                    visit(date(y, 1, 1), date(y, 12, 31), "year")
            elif step == "year":
                for m in range(1, 13):
                    last = (date(lo.year + (m == 12), m % 12 + 1, 1) - date.resolution)
                    visit(date(lo.year, m, 1), last, "month")
            else:
                days = (hi - lo).days + 1
                for k in range(0, days, 7):
                    a = lo + k * date.resolution
                    b = min(hi, a + 6 * date.resolution)
                    visit(a, b, "day")

        for decade in range(1940, end_year + 1, 10):
            visit(date(decade, 1, 1), date(min(decade + 9, end_year), 12, 31), "decade")
        return out

    def random_sample(self, query: str, n: int, rng: random.Random, exclude: set[str]) -> list[str]:
        total = self.count(query)
        if total <= UID_LIMIT:
            pool = [p for p in self.ids(query) if p not in exclude]
            return rng.sample(pool, min(n, len(pool)))
        parts = self.slices(query)
        weights = [c for _, c in parts]
        picks: dict[int, int] = {}
        for _ in range(n * 2):
            k = rng.choices(range(len(parts)), weights=weights)[0]
            picks[k] = picks.get(k, 0) + 1
        chosen: list[str] = []
        for k, m in picks.items():
            pool = [p for p in self.ids(f"({query}) AND {parts[k][0]}") if p not in exclude and p not in chosen]
            chosen.extend(rng.sample(pool, min(m, len(pool))))
        rng.shuffle(chosen)
        return chosen[:n]


def clopper_upper(k: int, n: int, alpha: float = 0.05) -> float:
    if n == 0:
        return 1.0
    if k == n:
        return 1.0
    lo, hi = k / n, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        tail = sum(math.comb(n, i) * mid**i * (1 - mid) ** (n - i) for i in range(k + 1))
        lo, hi = (mid, hi) if tail > alpha else (lo, mid)
    return hi


def naive_detect(total: int, gold: int, n: int = NAIVE_N) -> float:
    if gold == 0 or total == 0:
        return 0.0
    p_none = 1.0
    for i in range(min(n, total)):
        p_none *= max(0, total - gold - i) / (total - i)
    return 1 - p_none


def estimate_cut(lab: Lab, before: str, after: str, known: list[str], unseen: set[str], pool: dict[str, int],
                 rng: random.Random) -> dict:
    cut = f"({before}) NOT ({after})"
    size = lab.count(cut)
    truth = lab.among(cut, unseen)
    ranked = sorted(lab.among(cut, pool), key=lambda p: -pool[p])
    top = ranked[:TOP_K]
    found_top = [p for p in top if p in unseen]
    tail_size = size - len(top)
    sample = lab.random_sample(cut, TAIL_N, rng, set(top)) if tail_size > 0 else []
    found_tail = [p for p in sample if p in unseen]
    share = len(found_tail) / len(sample) if sample else 0.0
    upper = clopper_upper(len(found_tail), len(sample)) if sample else 0.0
    return {"records_cut": size, "gold_lost_true": len(truth),
            "ranked_pool_in_cut": len(ranked), "screened": len(top) + len(sample),
            "gold_found_in_top": len(found_top), "gold_found_in_random_tail": len(found_tail),
            "estimate_gold_lost": round(len(found_top) + share * tail_size, 1),
            "upper_95_gold_lost": round(len(found_top) + upper * tail_size, 1),
            "random_10_shows_any_loss_probability": round(naive_detect(size, len(truth)), 3)}


def idea_6_and_2(topic: str, label: str, block_index: int = 0, generic_k: int = 5) -> dict:
    fixture, card = load(topic, label)
    lab = Lab(fixture)
    blocks = replay.blocks_of(card["strategy"])
    gold = sorted(lab.among("", [str(p) for p in fixture["gold_pmids"]]))
    rng = random.Random(SEED)
    known = rng.sample(gold, max(3, round(KNOWN_SHARE * len(gold))))
    unseen = set(gold) - set(known)
    q = QUALIFIERS[topic]
    target = blocks[block_index]["terms"]
    others = [f"({' OR '.join(b['terms'])})" for i, b in enumerate(blocks) if i != block_index]
    rest = " AND ".join(others)

    def full(block_terms_or_clause: str) -> str:
        return f"({block_terms_or_clause})" + (f" AND {rest}" if rest else "")

    delivered = full(" OR ".join(target))
    impact = []
    for term in target:
        rest_terms = [t for t in target if t != term]
        unique = lab.count(f"({full(term)}) NOT ({full(' OR '.join(rest_terms))})") if rest_terms else lab.count(full(term))
        impact.append((unique, term))
    impact.sort(reverse=True)
    generic = [t for _, t in impact[:generic_k]]
    specific = [t for t in target if t not in generic]
    titled = [tf for tf in (title_form(t) for t in generic) if tf]
    hybrid = full(" OR ".join(specific + titled + [f"(({' OR '.join(generic)}) AND ({q}))"]))
    hybrid_no_title = full(" OR ".join(specific + [f"(({' OR '.join(generic)}) AND ({q}))"]))
    and_q = f"({delivered}) AND ({q})"

    def measure(query: str) -> dict:
        hit = lab.among(query, gold)
        return {"count": lab.count(query), "gold_retrieved": len(hit), "gold": len(gold),
                "recall_percent": round(100 * len(hit) / len(gold), 1)}

    pool: dict[str, int] = {}
    for pmid in known:
        for row in lab.pm.links(pmid, "similar"):
            if row["score"]:
                pool[row["pmid"]] = max(pool.get(row["pmid"], 0), row["score"])
    cuts = {"AND the qualifier": and_q, "hybrid with title tier": hybrid}
    for unique, term in impact[:3]:
        cuts[f"drop {term} ({unique} records only it retrieves)"] = full(" OR ".join(t for t in target if t != term))
    return {
        "topic": fixture["id"], "card": label, "as_of": fixture.get("as_of"), "qualifier": q,
        "generic_terms": [{"term": t, "records_only_it_retrieves": u} for u, t in impact[:generic_k]],
        "structures": {"delivered": measure(delivered), "hybrid with title tier": measure(hybrid),
                       "hybrid without title tier": measure(hybrid_no_title), "AND the qualifier": measure(and_q)},
        "known_records_used": len(known), "unseen_gold": len(unseen), "ranking_pool": len(pool),
        "cuts": {name: estimate_cut(lab, delivered, after, known, unseen, pool, rng) for name, after in cuts.items()},
    }


def idea_1(topic: str, spec: dict) -> dict:
    fixture, card = load(topic, spec["card"])
    lab = Lab(fixture)
    delivered = strip_date(card["strategy"])
    gold = sorted(lab.among("", [str(p) for p in fixture["gold_pmids"]]))
    missed = sorted(set(gold) - lab.among(delivered, gold))
    extra = f" AND ({spec['extra']})" if spec.get("extra") else ""
    cells, union_parts = [], []
    for rname, rq in spec["rows"].items():
        for cname, cq in spec["columns"].items():
            cell = f"(({rq}) AND ({cq}){extra}) NOT ({delivered})"
            union_parts.append(f"(({rq}) AND ({cq}){extra})")
            hit = lab.among(cell, missed)
            cells.append({"row": rname, "column": cname, "records": lab.count(cell), "misses_found": len(hit)})
    union = f"({' OR '.join(union_parts)}) NOT ({delivered})"
    union_hit = lab.among(union, missed)
    return {"topic": fixture["id"], "card": spec["card"], "blind": spec["blind"], "note": spec["note"],
            "delivered_count": lab.count(delivered), "gold": len(gold), "missed": len(missed),
            "grid_records": lab.count(union), "misses_found": len(union_hit),
            "records_per_miss_found": round(lab.count(union) / len(union_hit), 1) if union_hit else None,
            "delivered_records_per_gold": round(lab.count(delivered) / max(1, len(gold) - len(missed)), 1),
            "cells": cells}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(ROOT / "experiments" / "results" / f"ideas_126-{date.today()}.json"))
    parser.add_argument("--only", choices=["1", "6"], help="run one part only")
    args = parser.parse_args()
    out: dict = {"date": str(date.today()), "settings": {"top_k": TOP_K, "tail_n": TAIL_N, "naive_n": NAIVE_N,
                                                         "known_share": KNOWN_SHARE, "seed": SEED}}
    if args.only in (None, "6"):
        out["idea_6_and_2"] = []
        for topic, label in CARDS.items():
            print(f"idea 6 and 2: {topic}", file=sys.stderr)
            out["idea_6_and_2"].append(idea_6_and_2(topic, label))
    if args.only in (None, "1"):
        out["idea_1"] = []
        for topic, spec in GRIDS.items():
            print(f"idea 1: {topic}", file=sys.stderr)
            out["idea_1"].append(idea_1(topic, spec))
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

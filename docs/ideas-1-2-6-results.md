# Grid probes, per-term structure and ranked cut estimates: first results

Prototype: `evals/experiments/ideas_126.py`. Development topics only; it reads the answer key.
Results: `evals/experiments/results/ideas_1-2026-11-26.json` and `ideas_6_2-2026-11-26.json`.
Each idea was prompted by the held-out healthcare-nudging topic, so only development-topic
results count as evidence. Qualifiers and grid cells were written from each question before any
miss was inspected. Three grids (van_de_Schoot_2018, Smid_2020, Meijboom_2021) are not blind:
the project docs already describe the misses or the lesson for those topics.

## Idea 6: per-term structure (promising)

In one block, the five terms that alone add the most records stay in the title alone, or in title
or abstract only together with a qualifier written from the question; other terms are unchanged.

| Topic (delivered card) | Delivered | Hybrid with title tier | Hybrid, no title tier | AND the qualifier |
|---|---:|---:|---:|---:|
| Bos_2018 | 91,189 (9/9) | 48,754 (9/9) | 48,059 (9/9) | 12,590 (9/9) |
| Medeiros-2022 | 36,366 (9/9) | 21,173 (9/9) | 18,929 (9/9) | 15,204 (9/9) |
| van_de_Schoot_2018 | 32,074 (35/38) | 22,497 (35/38) | 21,098 (35/38) | 2,684 (35/38) |
| Welling_2021 | 155,667 (53/53) | 115,610 (53/53) | 98,881 (53/53) | 17,021 (48/53) |
| van_Dis_2020 | 16,407 (57/61) | 12,644 (57/61) | 11,430 (57/61) | 6,368 (50/61) |

The hybrid lost no gold record on any topic and cut the count by 23% to 47%. AND-ing the
qualifier outright cut far more but lost 5 of 53 (Welling) and 7 of 61 (van_Dis). The title tier
cost records here without saving a gold record; on healthcare-nudging it kept three known records
whose only signal was "reminder" in the title. Five topics, one card each: the next test is the
same rule across all development cards, with the qualifier taken from the agent's own optional
block rather than written by hand.

## Idea 1: grid probes (promising where a concept is fragmented)

Cells are a member of one concept AND a member of another, excluding the delivered strategy.

| Topic (card) | Blind | Misses | Grid records | Misses found | Records per miss found | Delivered records per gold found |
|---|---|---:|---:|---:|---:|---:|
| van_Dis_2020 (lean-optimal, 59.0%) | yes | 25 | 1,289 | 18 | 72 | 283 |
| Welling_2021 (lean-optimal, 83.0%) | yes | 9 | 7,977 | 6 | 1,330 | 477 |
| van_de_Schoot_2018 (ours, 92.1%) | no | 3 | 519 | 3 | 173 | 916 |
| Smid_2020 (ours, 64.3%) | no | 5 | 5,777 | 4 | 1,444 | 97 |
| Meijboom_2021 (ours, 74.3%) | no | 9 | 2,979 | 8 | 372 | 17 |

On van_Dis, 1,289 extra records would have raised recall from 59% to 89%, at a quarter of the
delivered search's cost per gold record. Cell sizes vary widely, and the yield sits in the small
cells: screening cells under about 300 records first is the obvious policy. Large cells (Welling
body weight, Smid multilevel x Bayesian, the Meijboom drug cells) are where the grid becomes a
second broad search.

## Idea 2: ranked cut estimates (failed as built)

For each cut, 30% of the gold stood in for an agent's known records; the cut was ranked by PubMed
similar-article scores of those records, the top 50 screened, and 30 more drawn at random. In all
five cuts that really lost gold (1 to 5 records), the estimate was 0. The lost records were mostly
not among the similar articles at all (van_Dis: 4 of 5 in the pool at ranks 125 to 453 of 802;
Welling: 1 of 4, at rank 58; van_de_Schoot: 0 of 1). A random sample of 10 would have shown any
loss with probability 0.000 to 0.036, which confirms that small random samples cannot justify a
cut, but the ranked sample did no better. The sampling design is not the problem; the ranker is.
Next: a text classifier over the cut's titles and abstracts, trained on the known records against
a background sample, or the cut screened in order of a stronger ranker before any random tail.

## Second test (ideas 6 and 2): `evals/experiments/ideas_6b_2b.py`

Qualifiers for the thirteen topics not in the first test were committed (1e256e7) before the run.
Results: `evals/experiments/results/ideas_6b_2b-2026-11-27.json`.

### Idea 6 on every development strategy on record (73 distinct strategies, 18 topics)

Rule, applied automatically: the five terms that alone add the most records, wherever they sit,
each become (term in the title) OR (term AND qualifier).

| Subset | Strategies | Hybrid: strategies losing gold | Gold lost | Pooled records kept | AND qualifier outright: gold lost, records kept |
|---|---:|---:|---:|---:|---:|
| Qualifier written blind | 50 | 6 | 6 of 1,602 (0.4%) | 66% | 13 (0.8%), 55% |
| Qualifier written after the first test | 23 | 2 | 3 of 708 (0.4%) | 68% | 39 (5.5%), 20% |
| Delivered 10,000 or more records | 27 | 5 | 6 of 940 (0.6%) | 67% | 44 (4.7%), 24% |
| Delivered under 10,000 | 46 | 3 | 3 of 1,370 (0.2%) | 78% | 8 (0.6%), 62% |

Across all 73, the hybrid removed 435,538 records and 9 gold records: about 48,000 records removed
per gold record lost, against about 590 records per gold record in the delivered strategies. The
title tier mattered here: without it, 14 gold records were lost. AND-ing the qualifier outright
removed twice as many records but lost 52 gold records. The hybrid is not lossless; an agent would
see a loss only on its own known records, so the rule needs the same check as any other cut.

### Idea 2 with a text ranker

Words common in the stand-in known records and rare in PubMed became a ranking query, and each cut
was ranked by PubMed's relevance order on it. 19 of 72 cuts lost gold (65 records in all).

- Cuts of 1,000 records or fewer (11): the top 200 held at least one lost record in 10, and the top
  50 in 5. Across them, 41 of 47 lost records were in the top 200.
- Cuts of more than 1,000 records (8): none of 18 lost records was in the top 200. Nearly every
  record in these cuts matched a ranking word, so the ranking did not separate them.
- The estimate from the top 50 plus a random 30 was close to the truth only where the top 50 held
  the loss (Kwok_2020: 18.8 against 18); elsewhere it was 0, with 95% upper bounds in the hundreds.

So the ranker detects losses in small cuts, where screening the whole cut is often affordable
anyway, and fails on the large cuts where an estimate is most needed. A random sample of 10 would
have shown any loss with a median probability of about 0.03. Next: train a real classifier on
titles and abstracts of the known records against a background sample, and fetch and score a
large random sample of each big cut, rather than relying on PubMed's relevance order.

## Held-out (frozen) suite: `evals/experiments/ideas_heldout.py`

Qualifiers and the grid were committed (3df46a1) before the first run; every topic touched is in
`heldout-ledger.jsonl`; only aggregate counts are kept
(`evals/experiments/results/ideas_heldout-2026-11-27.json`). healthcare-nudging is reported
separately because its source review was read while these ideas were developed.

### Idea 6 holds on held-out topics

| Topics | Strategies | Hybrid: gold lost | Records kept (pooled) | AND qualifier outright: gold lost, records kept |
|---|---:|---:|---:|---:|
| Nine blind held-out topics | 69 | 0 of 1,623 | 71% | 19 (1.2%), 44% |
| healthcare-nudging (not blind) | 8 | 5 of 348 (1.4%) | 50% | 18 (5.2%), 39% |

On the nine blind topics the hybrid lost no gold record in any of 69 strategies and removed 29% of
records, against about 510 records per gold record in the delivered strategies. Without the title
tier one gold record was lost. AND-ing the qualifier outright lost gold on two Cohen topics and
social prescribing.

### Idea 2: mixed

Seven cuts on blind topics lost gold (1 to 6 records). The top 200 of the text ranking held a lost
record in 4: all three cuts of under 1,000 records (133, 334 and 965 records), and two of four larger
ones (Estrogens, 4 of 6 lost records in the top 200 of a 3,568-record cut; social prescribing, the
one lost record in the top 50 of 33,763). Two larger cuts (1,149 and 3,342 records) showed nothing.
Better than on the development topics for large cuts, but not reliable enough to justify a cut alone.

### Idea 1: no gain on the one held-out grid

The social-prescribing grid (six component rows by an older-adult and outcome column, about 1,750
records outside each strategy) found none of the six misses in any of the four strategies that
missed gold. Its rows named programme types; the misses evidently describe social prescribing in
other terms. The grid works when its rows follow how studies describe themselves, which a grid
written from the question alone cannot guarantee.

## Idea 6 robustness (development topics): `evals/experiments/idea6_robustness.py`, `idea6_weak_guard.py`

73 distinct development strategies, 2,310 gold records retrieved; qualifiers as in the second test.
The guard stands in for the agent's check: 30% of the gold acts as its known records, terms are
restructured one at a time, and a change is kept only if no known record is lost.

| Variant | Strategies losing gold | Gold lost | Records kept (pooled) |
|---|---:|---:|---:|
| 3 terms restructured | 2 | 3 | 72% |
| 5 terms | 8 | 9 | 68% |
| 10 terms | 12 | 13 | 64% |
| 5 terms, guarded | 5 | 6 | 68% |
| 5 terms, weak qualifier | 25 | 161 | 59% |
| 5 terms, weak qualifier, guarded | 13 | 15 | 61% |

- More terms cut more and lose more; five is a reasonable middle, three the cautious choice.
- The qualifier is the main risk. The weak version (first third of each qualifier's terms) lost 161
  gold records, 121 of them on Kwok_2020, where the shortened qualifier was two MeSH headings with
  no text words. A qualifier needs both a MeSH and a text-word layer, as any block does.
- The guard is what makes the rule safe. With good qualifiers it caught 3 of 9 losses at the cost
  of 3 refused terms; the rest were records the agent would not have known. With weak qualifiers
  it cut the loss from 161 to 15 by refusing 20 restructures, and still kept 61% of records.

## Agent runs with `psb restructure` (development topics, a cheaper model, one run per arm)

Patched skill: a22d9dd (rule in SKILL.md only), then e1729e1 (rule also named in `psb eval`'s
large-result advice, the progress summary and the workload rule in `scope.md`). Baseline: 8df69b9.
Scorecards are under `evals/results/<topic>/` as `patch-cheap`, `patch2-cheap` and `main-cheap`
(model field removed). Many runs stopped on the account's five-hour and weekly usage limits; those
cards were deleted, so several topics have no pair.

| Topic | Baseline | Patch v1 (a22d9dd) | Patch v2 (e1729e1) | Restructure used (v2) |
|---|---|---|---|---|
| van_de_Schoot_2018 | 94.7%, 14,450 | 94.7%, 33,577 | 94.7%, 10,336 | dry run only (10,336 to 10,234), not applied |
| Bos_2018 | 100%, 7,947 | 100%, 9,540 | 100%, 22,482 | yes: 29,664 to 22,482 (outcome qualifier) |
| Welling_2021 | 96.2%, 20,951 | none | 98.1%, 27,450 | yes, twice: 124,269 to 98,327 before other cuts |
| Brouwer_2019 | none | 96.3%, 18,503 | none | |
| Medeiros-2022 | none | none | none | |

- With the rule only in SKILL.md, no agent used the command. Named in `psb eval`'s output, the
  agents used it in all three v2 runs.
- It did not yet help. On Bos the agent restructured instead of AND-ing the outcome block, which the
  baseline agent AND-ed with no loss (7,947 records): the instruction "AND the block only if the
  restructured result is still too large" let the agent stop at a larger result. On Welling the
  patched run kept one more gold record (52 against 51 of 53) for 31% more records. With one run
  per arm and runs that vary this much, none of these differences is evidence either way.
- Next change to test: after restructuring, still measure the qualifier as an optional block and
  take whichever loses no known record at the smaller count, then three or more runs per arm.

### Patch v3 (9e3f666): compare restructure with AND-ing, take the smaller lossless result

Round 1 of a planned three per arm, same five topics and model. Scorecards are `patch3-cheap` and
`main-cheap`. Rounds 2 and 3 did not run: the account's five-hour usage limit stopped them, then the
session's worker restarted and ended the batch.

| Topic | Gold | Baseline | Patch v3 | Restructure applied during the run | In the delivered strategy |
|---|---|---|---|---|---|
| van_de_Schoot_2018 | 38 | 36, 14,450 | 36, 35,734 | twice (6% and 5% fewer) | no: reverted ("6% gain not worth risk"); trajectory left optional |
| Bos_2018 | 9 | 9, 7,947 | 9, 19,533 | yes (15% fewer) | no: reverted after the critic; outcome left optional |
| Welling_2021 | 53 | 51, 20,951 | 52, 26,473 | yes (17% fewer) | no: reverted, outcomes block AND-ed instead |
| Brouwer_2019 | 54 | 52, 20,887 | 52, 19,139 | yes (51% fewer) | no: critic called it a "hidden theory gate"; reverted |
| Medeiros-2022 | 9 | 8, 8,292 | 9, 8,885 | yes (79% fewer) | no: reverted, school block AND-ed instead |
| Total | 163 | 156, 72,527 | 158, 109,764 | 5 of 5 runs | 0 of 5 runs |

- The agents now use the command (5 of 5) and, where AND-ing the qualifier was lossless, compared
  the two and took the AND (Welling, Medeiros), as the v3 rule asks.
- No restructure survived to delivery. Two causes, both visible in the run logs: the PRESS critic
  reads a restructured term as an undocumented restriction of the concept and asks for the bare
  term back; and the agents judged small reductions not worth the added structure.
- The skill change has a side effect that costs records. On van de Schoot and Bos the patched agent
  drafted the second concept as an optional block from the start (the form restructure needs), found
  AND-ing it lost a known record, and delivered one block: 2.5 times the baseline's records for the
  same recall. The baseline agents wrote a broader second block and AND-ed it with no loss.
- Net, round 1: 2 more gold of 163 for 51% more records. One run per arm; not evidence of a recall
  gain, but the mechanism is clear enough that more runs of v3 would mostly measure the side effect.

Next change, if pursued: tell the critic (`references/critic.md`) that a guard-checked restructure is
a documented structure to judge on its log entry, not a hidden restriction; and keep the advice to
draft the second concept as a full block first, offering restructure only after AND-ing it has been
measured and refused for losing a known record.

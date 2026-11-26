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
was ranked by PubMed's relevance order on it. 19 of 72 cuts lost gold (68 records in all).

- Cuts of 1,000 records or fewer (11): the top 200 held at least one lost record in 10, and the top
  50 in 5. Across them, 41 of 50 lost records were in the top 200.
- Cuts of more than 1,000 records (8): none of 18 lost records was in the top 200. Nearly every
  record in these cuts matched a ranking word, so the ranking did not separate them.
- The estimate from the top 50 plus a random 30 was close to the truth only where the top 50 held
  the loss (Kwok_2020: 18.8 against 18); elsewhere it was 0, with 95% upper bounds in the hundreds.

So the ranker detects losses in small cuts, where screening the whole cut is often affordable
anyway, and fails on the large cuts where an estimate is most needed. A random sample of 10 would
have shown any loss with a median probability of about 0.03. Next: train a real classifier on
titles and abstracts of the known records against a background sample, and fetch and score a
large random sample of each big cut, rather than relying on PubMed's relevance order.

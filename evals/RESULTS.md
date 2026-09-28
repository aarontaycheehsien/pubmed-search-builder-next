# Evaluation results

Generated 20260928T204037Z by `python evals/run.py report`.

Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) over `ok` runs.

Version is a hash of the skill as staged into the run (`legacy`: scored before versions were recorded). Only the latest version of each skill and driver is shown; `--all-versions` shows the rest. Runs is ok/attempted; infrastructure failures (quota, rate limits) are not attempts. † fewer than 3 ok runs. ⚠ result counts differ by more than 2×.

## Development topics

Skill changes may be motivated only by these topics.

| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---|---:|---|---|---:|---:|---:|
| Bos_2018 | generated:pubmed-search-builder-next (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 12495 | 1388.3 | 2.6 |
| Bos_2018 | generated:pubmed-search-builder-next (codex) | noseed | legacy | 2/3 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 68692 (54277-83107) | 7632.5 (6030.8-9234.1) | n/a |
| Bos_2018 | naive | noseed | baseline | 1/1 | 66.7 | n/a | 2339 | 389.8 | n/a |
| Bos_2018 | naive | seeded | baseline | 1/1 | 66.7 | n/a | 2339 | 584.8 | n/a |
| CD010657 | naive | noseed | baseline | 1/1 | 91.4 | n/a | 644 | 20.1 | n/a |
| CD010657 | naive | seeded | baseline | 1/1 | 90.6 | n/a | 644 | 22.2 | n/a |
| CD011431 | naive | noseed | baseline | 1/1 | 80.8 | n/a | 502 | 23.9 | n/a |
| CD011431 | naive | seeded | baseline | 1/1 | 78.3 | n/a | 502 | 27.9 | n/a |
| CD011926 | generated:lean-optimal (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 2179 | 75.1 | 1.7 |
| CD011926 | generated:pubmed-search-builder-next (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 2055 | 70.9 | 2.2 |
| CD011926 | generated:pubmed-search-builder-next (codex) | noseed | legacy | 1/1 † | 96.6 | 95.0 | 1479 | 52.8 | n/a |
| CD011926 | naive | noseed | baseline | 1/1 | 62.1 | n/a | 117 | 6.5 | n/a |
| CD011926 | naive | seeded | baseline | 1/1 | 57.7 | n/a | 117 | 7.8 | n/a |
| CD011926 | reference | noseed | baseline | 1/1 | 96.6 | n/a | 1001 | 35.8 | n/a |
| CD011926 | reference | seeded | baseline | 1/1 | 96.2 | n/a | 1001 | 40.0 | n/a |
| Donners_2021 | naive | noseed | baseline | 1/1 | 100.0 | n/a | 1614 | 107.6 | n/a |
| Donners_2021 | naive | seeded | baseline | 1/1 | 100.0 | n/a | 1614 | 134.5 | n/a |
| Liu_2023_VR_nursing | naive | noseed | baseline | 1/1 | 100.0 | n/a | 374 | 62.3 | n/a |
| Medeiros-2022-School-based food and nutr | naive | noseed | baseline | 1/1 | 11.1 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | seeded | baseline | 1/1 | 16.7 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | noseed | baseline | 1/1 | 88.9 | n/a | 24320 | 3040.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | seeded | baseline | 1/1 | 83.3 | n/a | 24320 | 4864.0 | n/a |
| Muthu_2022 | generated:quota-check (codex) | noseed | legacy | 0/1 † | n/a | n/a | n/a | n/a | n/a |
| Muthu_2022 | naive | noseed | baseline | 1/1 | 100.0 | n/a | 505 | 84.2 | n/a |
| Smid_2020 | naive | noseed | baseline | 1/1 | 78.6 | n/a | 1369 | 124.5 | n/a |
| Smid_2020 | naive | seeded | baseline | 1/1 | 72.7 | n/a | 1369 | 171.1 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | noseed | baseline | 1/1 | 72.7 | n/a | 1599 | 199.9 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | seeded | baseline | 1/1 | 62.5 | n/a | 1599 | 319.8 | n/a |

## Held-out topics

Frozen before their first run; misses and audits are never kept. Claim an improvement only from the latest version with at least 3 ok runs a side. Every use is logged in `evals/heldout-ledger.jsonl`.

| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---|---:|---|---|---:|---:|---:|
| Cohen_2006_ACEInhibitors | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 20936.7 (20591-21375) | 510.6 (502.2-521.3) | n/a |
| Cohen_2006_ADHD | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 95.0 (95.0-95.0) | 95.0 (95.0-95.0) | 2769.7 (2620-2960) | 145.8 (137.9-155.8) | n/a |
| Cohen_2006_Antihistamines | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 81.2 (81.2-81.2) | 81.2 (81.2-81.2) | 1359.3 (955-2153) | 104.6 (73.5-165.6) | n/a |
| Cohen_2006_Estrogens | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 91.6 (82.5-96.2) | 91.6 (82.5-96.2) | 29672.3 (28843-30163) | 406.2 (389.8-437.0) | n/a |
| Cohen_2006_UrinaryIncontinence | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 80.0 (80.0-80.0) | 80.0 (80.0-80.0) | 1094.7 (594-1841) | 34.2 (18.6-57.5) | n/a |
| healthcare-nudging | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 38.0 (34.9-44.2) | 38.0 (34.9-44.2) | 4998 (3319-6352) | 154.1 (110.6-211.7) | n/a |
| housing-first-criminal-justice | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 86.7 (80.0-100.0) | 86.7 (80.0-100.0) | 385 (361-432) | 90.2 (72.4-108.0) | n/a |
| school-restorative-practice | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 94.4 (83.3-100.0) | 94.4 (83.3-100.0) | 1397.3 (263-2989) | 235.8 (52.6-498.2) | n/a |
| social-prescribing-older-adults | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 40.0 (40.0-40.0) | 40.0 (40.0-40.0) | 1805 (981-3056) | 451.2 (245.2-764.0) | n/a |
| work-directed-return-to-work | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 8121.7 (7394-8690) | 738.3 (672.2-790.0) | n/a |

## Retired topics

- Jeyaraman_2020: gold set is mostly chondrocyte-implantation and microfracture trials outside the question (mesenchymal stem cells for knee osteoarthritis)
- Menon_2022: gold set counts diet, opioid use, food insecurity and vitamin D reviews as environmental health, which the question's plain reading excludes; probes against that reading found little while recall stayed near 57%

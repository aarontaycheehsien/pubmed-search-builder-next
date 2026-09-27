# Evaluation results

Generated 20260927T004215Z by `python evals/run.py report`.

Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) over valid runs.

| Topic | Source | Condition | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---:|---|---|---:|---:|---:|
| Bos_2018 | generated:pubmed-search-builder-next (claude) | noseed | 1/1 | 100.0 | 100.0 | 12495 | 1388.3 | 2.6 |
| Bos_2018 | generated:pubmed-search-builder-next (codex) | noseed | 0/1 | n/a | n/a | n/a | n/a | n/a |
| Bos_2018 | naive | noseed | 1/1 | 66.7 | n/a | 2339 | 389.8 | n/a |
| Bos_2018 | naive | seeded | 1/1 | 66.7 | n/a | 2339 | 584.8 | n/a |
| CD010657 | naive | noseed | 1/1 | 91.4 | n/a | 644 | 20.1 | n/a |
| CD010657 | naive | seeded | 1/1 | 90.6 | n/a | 644 | 22.2 | n/a |
| CD011431 | naive | noseed | 1/1 | 80.8 | n/a | 502 | 23.9 | n/a |
| CD011431 | naive | seeded | 1/1 | 78.3 | n/a | 502 | 27.9 | n/a |
| CD011926 | generated:lean-optimal (claude) | noseed | 1/1 | 100.0 | 100.0 | 2179 | 75.1 | 1.7 |
| CD011926 | generated:pubmed-search-builder-next (claude) | noseed | 1/1 | 100.0 | 100.0 | 2055 | 70.9 | 2.2 |
| CD011926 | generated:pubmed-search-builder-next (codex) | noseed | 1/1 | 96.6 | 95.0 | 1479 | 52.8 | n/a |
| CD011926 | naive | noseed | 1/1 | 62.1 | n/a | 117 | 6.5 | n/a |
| CD011926 | naive | seeded | 1/1 | 57.7 | n/a | 117 | 7.8 | n/a |
| CD011926 | reference | noseed | 1/1 | 96.6 | n/a | 1001 | 35.8 | n/a |
| CD011926 | reference | seeded | 1/1 | 96.2 | n/a | 1001 | 40.0 | n/a |
| Donners_2021 | naive | noseed | 1/1 | 100.0 | n/a | 1614 | 107.6 | n/a |
| Donners_2021 | naive | seeded | 1/1 | 100.0 | n/a | 1614 | 134.5 | n/a |
| Liu_2023_VR_nursing | naive | noseed | 1/1 | 100.0 | n/a | 374 | 62.3 | n/a |
| Medeiros-2022-School-based food and nutr | naive | noseed | 1/1 | 11.1 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | seeded | 1/1 | 16.7 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | noseed | 1/1 | 88.9 | n/a | 24320 | 3040.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | seeded | 1/1 | 83.3 | n/a | 24320 | 4864.0 | n/a |
| Muthu_2022 | naive | noseed | 1/1 | 100.0 | n/a | 505 | 84.2 | n/a |
| Smid_2020 | naive | noseed | 1/1 | 78.6 | n/a | 1369 | 124.5 | n/a |
| Smid_2020 | naive | seeded | 1/1 | 72.7 | n/a | 1369 | 171.1 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | noseed | 1/1 | 72.7 | n/a | 1599 | 199.9 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | seeded | 1/1 | 62.5 | n/a | 1599 | 319.8 | n/a |

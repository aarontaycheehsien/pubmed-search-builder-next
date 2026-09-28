# Evaluation results

Generated 20260928T041650Z by `python evals/run.py report`.

Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) over valid runs.

| Topic | Source | Condition | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---:|---|---|---:|---:|---:|
| Appenzeller-Herzog_2019 | generated:lean-optimal (codex) | noseed | 1/1 | 100.0 | 100.0 | 7579 | 360.9 | n/a |
| Appenzeller-Herzog_2019 | generated:ours (codex) | noseed | 1/1 | 100.0 | 100.0 | 4062 | 193.4 | n/a |
| Bos_2018 | generated:lean-optimal (codex) | noseed | 1/1 | 100.0 | 100.0 | 5313 | 590.3 | n/a |
| Bos_2018 | generated:pubmed-search-builder-next (claude) | noseed | 1/1 | 100.0 | 100.0 | 12495 | 1388.3 | 2.6 |
| Bos_2018 | generated:pubmed-search-builder-next (codex) | noseed | 2/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 68692 (54277-83107) | 7632.5 (6030.8-9234.1) | n/a |
| Bos_2018 | naive | noseed | 1/1 | 66.7 | n/a | 2339 | 389.8 | n/a |
| Bos_2018 | naive | seeded | 1/1 | 66.7 | n/a | 2339 | 584.8 | n/a |
| Brouwer_2019 | generated:lean-optimal (codex) | noseed | 1/1 | 96.3 | 96.3 | 17550 | 337.5 | n/a |
| Brouwer_2019 | generated:ours (codex) | noseed | 1/1 | 96.3 | 96.2 | 17383 | 334.3 | n/a |
| CD010657 | generated:lean-optimal (codex) | noseed | 1/1 | 97.1 | 97.1 | 993 | 29.2 | n/a |
| CD010657 | generated:ours (codex) | noseed | 2/2 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 1922 (1783-2061) | 54.9 (50.9-58.9) | n/a |
| CD010657 | naive | noseed | 1/1 | 91.4 | n/a | 644 | 20.1 | n/a |
| CD010657 | naive | seeded | 1/1 | 90.6 | n/a | 644 | 22.2 | n/a |
| CD011431 | generated:lean-optimal (codex) | noseed | 1/1 | 100.0 | 100.0 | 1864 | 71.7 | n/a |
| CD011431 | generated:ours (codex) | noseed | 1/1 | 100.0 | 100.0 | 6099 | 234.6 | n/a |
| CD011431 | naive | noseed | 1/1 | 80.8 | n/a | 502 | 23.9 | n/a |
| CD011431 | naive | seeded | 1/1 | 78.3 | n/a | 502 | 27.9 | n/a |
| CD011926 | generated:lean-optimal (claude) | noseed | 1/1 | 100.0 | 100.0 | 2179 | 75.1 | 1.7 |
| CD011926 | generated:lean-optimal (codex) | noseed | 1/1 | 96.6 | 96.6 | 1985 | 70.9 | n/a |
| CD011926 | generated:pubmed-search-builder-next (claude) | noseed | 1/1 | 100.0 | 100.0 | 2055 | 70.9 | 2.2 |
| CD011926 | generated:pubmed-search-builder-next (codex) | noseed | 1/1 | 96.6 | 95.0 | 1479 | 52.8 | n/a |
| CD011926 | naive | noseed | 1/1 | 62.1 | n/a | 117 | 6.5 | n/a |
| CD011926 | naive | seeded | 1/1 | 57.7 | n/a | 117 | 7.8 | n/a |
| CD011926 | reference | noseed | 1/1 | 96.6 | n/a | 1001 | 35.8 | n/a |
| CD011926 | reference | seeded | 1/1 | 96.2 | n/a | 1001 | 40.0 | n/a |
| Donners_2021 | generated:lean-optimal (codex) | noseed | 1/1 | 93.3 | 93.3 | 231 | 16.5 | n/a |
| Donners_2021 | generated:ours (codex) | noseed | 2/2 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 238 (234-242) | 15.9 (15.6-16.1) | n/a |
| Donners_2021 | naive | noseed | 1/1 | 100.0 | n/a | 1614 | 107.6 | n/a |
| Donners_2021 | naive | seeded | 1/1 | 100.0 | n/a | 1614 | 134.5 | n/a |
| Jeyaraman_2020 | generated:lean-optimal (codex) | noseed | 1/1 | 16.5 | 16.5 | 762 | 50.8 | n/a |
| Jeyaraman_2020 | generated:ours (codex) | noseed | 2/2 | 18.7 (17.6-19.8) | 18.7 (17.6-19.8) | 2657 (2577-2737) | 157.1 (143.2-171.1) | n/a |
| Kwok_2020 | generated:lean-optimal (codex) | noseed | 1/1 | 90.5 | 90.5 | 755 | 7.2 | n/a |
| Kwok_2020 | generated:ours (codex) | noseed | 1/1 | 90.5 | 89.9 | 822 | 7.8 | n/a |
| Liu_2023_VR_nursing | generated:lean-optimal (codex) | noseed | 1/1 | 100.0 | 100.0 | 737 | 122.8 | n/a |
| Liu_2023_VR_nursing | generated:ours (codex) | noseed | 1/1 | 100.0 | 100.0 | 2600 | 433.3 | n/a |
| Liu_2023_VR_nursing | naive | noseed | 1/1 | 100.0 | n/a | 374 | 62.3 | n/a |
| Medeiros-2022-School-based food and nutr | generated:lean-optimal (codex) | noseed | 1/1 | 88.9 | 88.9 | 23351 | 2918.9 | n/a |
| Medeiros-2022-School-based food and nutr | generated:ours (codex) | noseed | 1/1 | 88.9 | 88.9 | 25088 | 3136.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | noseed | 1/1 | 11.1 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | seeded | 1/1 | 16.7 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | noseed | 1/1 | 88.9 | n/a | 24320 | 3040.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | seeded | 1/1 | 83.3 | n/a | 24320 | 4864.0 | n/a |
| Meijboom_2021 | generated:lean-optimal (codex) | noseed | 1/2 | 88.6 | 88.6 | 515 | 16.6 | n/a |
| Meijboom_2021 | generated:ours (codex) | noseed | 3/3 | 91.4 (74.3-100.0) | 91.4 (74.3-100.0) | 719 (443-1056) | 22.0 (17.0-30.2) | n/a |
| Menon_2022 | generated:lean-optimal (codex) | noseed | 1/2 | 10.8 | 10.8 | 1006 | 125.8 | n/a |
| Menon_2022 | generated:ours (codex) | noseed | 2/3 | 68.2 (64.9-71.6) | 67.8 (64.9-70.8) | 7521.5 (5260-9783) | 147.1 (109.6-184.6) | n/a |
| Muthu_2022 | generated:lean-optimal (codex) | noseed | 1/2 | 100.0 | 100.0 | 591 | 98.5 | n/a |
| Muthu_2022 | generated:ours (codex) | noseed | 1/3 | 100.0 | 100.0 | 583 | 97.2 | n/a |
| Muthu_2022 | generated:quota-check (codex) | noseed | 0/1 | n/a | n/a | n/a | n/a | n/a |
| Muthu_2022 | naive | noseed | 1/1 | 100.0 | n/a | 505 | 84.2 | n/a |
| Oud_2018 | generated:lean-optimal (codex) | noseed | 1/2 | 94.1 | 94.1 | 1880 | 117.5 | n/a |
| Oud_2018 | generated:ours (codex) | noseed | 1/2 | 94.1 | 90.9 | 1880 | 117.5 | n/a |
| Smid_2020 | generated:lean-optimal (codex) | noseed | 1/2 | 78.6 | 78.6 | 1069 | 97.2 | n/a |
| Smid_2020 | generated:ours (codex) | noseed | 3/4 | 83.4 (64.3-92.9) | 77.0 (50.0-90.9) | 1494.7 (870-2184) | 124.9 (96.7-168.0) | n/a |
| Smid_2020 | naive | noseed | 1/1 | 78.6 | n/a | 1369 | 124.5 | n/a |
| Smid_2020 | naive | seeded | 1/1 | 72.7 | n/a | 1369 | 171.1 | n/a |
| Welling_2021 | generated:lean-optimal (codex) | noseed | 1/2 | 83.0 | 83.0 | 20531 | 466.6 | n/a |
| Welling_2021 | generated:ours (codex) | noseed | 2/3 | 94.3 (90.6-98.1) | 94.2 (90.4-98.1) | 82722.5 (13793-151652) | 1601.9 (287.4-2916.4) | n/a |
| gao-2026-Immune checkpoint inhibitors | generated:lean-optimal (codex) | noseed | 1/1 | 72.7 | 72.7 | 1220 | 152.5 | n/a |
| gao-2026-Immune checkpoint inhibitors | generated:ours (codex) | noseed | 2/2 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 1186 (785-1587) | 107.9 (71.4-144.3) | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | noseed | 1/1 | 72.7 | n/a | 1599 | 199.9 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | seeded | 1/1 | 62.5 | n/a | 1599 | 319.8 | n/a |
| van_Dis_2020 | generated:lean-optimal (codex) | noseed | 1/2 | 59.0 | 59.0 | 10137 | 281.6 | n/a |
| van_Dis_2020 | generated:ours (codex) | noseed | 2/3 | 93.4 (93.4-93.4) | 93.3 (93.3-93.4) | 16072.5 (15738-16407) | 282.0 (276.1-287.8) | n/a |
| van_de_Schoot_2018 | generated:lean-optimal (codex) | noseed | 1/2 | 92.1 | 92.1 | 7025 | 200.7 | n/a |
| van_de_Schoot_2018 | generated:ours (codex) | noseed | 1/2 | 92.1 | 92.1 | 31980 | 913.7 | n/a |

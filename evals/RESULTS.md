# Evaluation results

Generated 20260928T052340Z by `python evals/run.py report`.

Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) over `ok` runs.

Version is a hash of the skill as staged into the run (`legacy`: scored before versions were recorded). Only the latest version of each skill and driver is shown; `--all-versions` shows the rest. Runs is ok/attempted; infrastructure failures (quota, rate limits) are not attempts. † fewer than 3 ok runs. ⚠ result counts differ by more than 2×.

## Development topics

Skill changes may be motivated only by these topics.

**A = generated:ours vs B = generated:lean-optimal** (codex, noseed): 8 win, 9 tie, 0 loss on recall; 5 topic(s) where A returns more than 2× B's results; 17 topic(s) with fewer than 3 ok runs a side.

| Topic | Recall A | Recall B | Recall | Results A | Results B | Ratio A/B | Runs A/B |
|---|---:|---:|---|---:|---:|---:|---:|
| Appenzeller-Herzog_2019 | 100.0 | 100.0 | tie | 4,062 | 7,579 | 0.54 | 1/1 † |
| Brouwer_2019 | 96.3 | 96.3 | tie | 17,383 | 17,550 | 0.99 | 1/1 † |
| CD010657 | 100.0 | 97.1 | win | 1,922 | 993 | 1.94 | 2/1 † |
| CD011431 | 100.0 | 100.0 | tie | 6,099 | 1,864 | 3.27 ⚠ | 1/1 † |
| Donners_2021 | 100.0 | 93.3 | win | 238 | 231 | 1.03 | 2/1 † |
| Kwok_2020 | 90.5 | 90.5 | tie | 822 | 755 | 1.09 | 1/1 † |
| Liu_2023_VR_nursing | 100.0 | 100.0 | tie | 2,600 | 737 | 3.53 ⚠ | 1/1 † |
| Medeiros-2022-School-based food and nutr | 88.9 | 88.9 | tie | 25,088 | 23,351 | 1.07 | 1/1 † |
| Meijboom_2021 | 91.4 | 88.6 | win | 719 | 515 | 1.4 | 3/1 † |
| Menon_2022 | 68.2 | 10.8 | win | 7,522 | 1,006 | 7.48 ⚠ | 2/1 † |
| Muthu_2022 | 100.0 | 100.0 | tie | 583 | 591 | 0.99 | 1/1 † |
| Oud_2018 | 94.1 | 94.1 | tie | 1,880 | 1,880 | 1.0 | 1/1 † |
| Smid_2020 | 83.4 | 78.6 | win | 1,495 | 1,069 | 1.4 | 3/1 † |
| Welling_2021 | 94.3 | 83.0 | win | 82,722 | 20,531 | 4.03 ⚠ | 2/1 † |
| gao-2026-Immune checkpoint inhibitors | 100.0 | 72.7 | win | 1,186 | 1,220 | 0.97 | 2/1 † |
| van_Dis_2020 | 93.4 | 59.0 | win | 16,072 | 10,137 | 1.59 | 2/1 † |
| van_de_Schoot_2018 | 92.1 | 92.1 | tie | 31,980 | 7,025 | 4.55 ⚠ | 1/1 † |

| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---|---:|---|---|---:|---:|---:|
| Appenzeller-Herzog_2019 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 7579 | 360.9 | n/a |
| Appenzeller-Herzog_2019 | generated:ours (codex) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 4062 | 193.4 | n/a |
| Bos_2018 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 5313 | 590.3 | n/a |
| Bos_2018 | generated:pubmed-search-builder-next (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 12495 | 1388.3 | 2.6 |
| Bos_2018 | generated:pubmed-search-builder-next (codex) | noseed | legacy | 2/3 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 68692 (54277-83107) | 7632.5 (6030.8-9234.1) | n/a |
| Bos_2018 | naive | noseed | baseline | 1/1 | 66.7 | n/a | 2339 | 389.8 | n/a |
| Bos_2018 | naive | seeded | baseline | 1/1 | 66.7 | n/a | 2339 | 584.8 | n/a |
| Brouwer_2019 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 96.3 | 96.3 | 17550 | 337.5 | n/a |
| Brouwer_2019 | generated:ours (codex) | noseed | legacy | 1/1 † | 96.3 | 96.2 | 17383 | 334.3 | n/a |
| CD010657 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 97.1 | 97.1 | 993 | 29.2 | n/a |
| CD010657 | generated:ours (codex) | noseed | legacy | 2/2 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 1922 (1783-2061) | 54.9 (50.9-58.9) | n/a |
| CD010657 | naive | noseed | baseline | 1/1 | 91.4 | n/a | 644 | 20.1 | n/a |
| CD010657 | naive | seeded | baseline | 1/1 | 90.6 | n/a | 644 | 22.2 | n/a |
| CD011431 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 1864 | 71.7 | n/a |
| CD011431 | generated:ours (codex) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 6099 | 234.6 | n/a |
| CD011431 | naive | noseed | baseline | 1/1 | 80.8 | n/a | 502 | 23.9 | n/a |
| CD011431 | naive | seeded | baseline | 1/1 | 78.3 | n/a | 502 | 27.9 | n/a |
| CD011926 | generated:lean-optimal (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 2179 | 75.1 | 1.7 |
| CD011926 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 96.6 | 96.6 | 1985 | 70.9 | n/a |
| CD011926 | generated:pubmed-search-builder-next (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 2055 | 70.9 | 2.2 |
| CD011926 | generated:pubmed-search-builder-next (codex) | noseed | legacy | 1/1 † | 96.6 | 95.0 | 1479 | 52.8 | n/a |
| CD011926 | naive | noseed | baseline | 1/1 | 62.1 | n/a | 117 | 6.5 | n/a |
| CD011926 | naive | seeded | baseline | 1/1 | 57.7 | n/a | 117 | 7.8 | n/a |
| CD011926 | reference | noseed | baseline | 1/1 | 96.6 | n/a | 1001 | 35.8 | n/a |
| CD011926 | reference | seeded | baseline | 1/1 | 96.2 | n/a | 1001 | 40.0 | n/a |
| Donners_2021 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 93.3 | 93.3 | 231 | 16.5 | n/a |
| Donners_2021 | generated:ours (codex) | noseed | legacy | 2/2 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 238 (234-242) | 15.9 (15.6-16.1) | n/a |
| Donners_2021 | naive | noseed | baseline | 1/1 | 100.0 | n/a | 1614 | 107.6 | n/a |
| Donners_2021 | naive | seeded | baseline | 1/1 | 100.0 | n/a | 1614 | 134.5 | n/a |
| Kwok_2020 | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 90.5 | 90.5 | 755 | 7.2 | n/a |
| Kwok_2020 | generated:ours (codex) | noseed | legacy | 1/1 † | 90.5 | 89.9 | 822 | 7.8 | n/a |
| Liu_2023_VR_nursing | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 737 | 122.8 | n/a |
| Liu_2023_VR_nursing | generated:ours (codex) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 2600 | 433.3 | n/a |
| Liu_2023_VR_nursing | naive | noseed | baseline | 1/1 | 100.0 | n/a | 374 | 62.3 | n/a |
| Medeiros-2022-School-based food and nutr | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 88.9 | 88.9 | 23351 | 2918.9 | n/a |
| Medeiros-2022-School-based food and nutr | generated:ours (codex) | noseed | legacy | 1/1 † | 88.9 | 88.9 | 25088 | 3136.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | noseed | baseline | 1/1 | 11.1 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | seeded | baseline | 1/1 | 16.7 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | noseed | baseline | 1/1 | 88.9 | n/a | 24320 | 3040.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | seeded | baseline | 1/1 | 83.3 | n/a | 24320 | 4864.0 | n/a |
| Meijboom_2021 | generated:lean-optimal (codex) | noseed | legacy | 1/2 † | 88.6 | 88.6 | 515 | 16.6 | n/a |
| Meijboom_2021 | generated:ours (codex) | noseed | legacy | 3/3 | 91.4 (74.3-100.0) | 91.4 (74.3-100.0) | 719 (443-1056) | 22.0 (17.0-30.2) | n/a |
| Menon_2022 | generated:lean-optimal (codex) | noseed | legacy | 1/2 † | 10.8 | 10.8 | 1006 | 125.8 | n/a |
| Menon_2022 | generated:ours (codex) | noseed | legacy | 2/3 † | 68.2 (64.9-71.6) | 67.8 (64.9-70.8) | 7521.5 (5260-9783) | 147.1 (109.6-184.6) | n/a |
| Muthu_2022 | generated:lean-optimal (codex) | noseed | legacy | 1/1 +1 infra † | 100.0 | 100.0 | 591 | 98.5 | n/a |
| Muthu_2022 | generated:ours (codex) | noseed | legacy | 1/1 +2 infra † | 100.0 | 100.0 | 583 | 97.2 | n/a |
| Muthu_2022 | generated:quota-check (codex) | noseed | legacy | 0/1 † | n/a | n/a | n/a | n/a | n/a |
| Muthu_2022 | naive | noseed | baseline | 1/1 | 100.0 | n/a | 505 | 84.2 | n/a |
| Oud_2018 | generated:lean-optimal (codex) | noseed | legacy | 1/1 +1 infra † | 94.1 | 94.1 | 1880 | 117.5 | n/a |
| Oud_2018 | generated:ours (codex) | noseed | legacy | 1/1 +1 infra † | 94.1 | 90.9 | 1880 | 117.5 | n/a |
| Smid_2020 | generated:lean-optimal (codex) | noseed | legacy | 1/1 +1 infra † | 78.6 | 78.6 | 1069 | 97.2 | n/a |
| Smid_2020 | generated:ours (codex) | noseed | legacy | 3/3 +1 infra | 83.4 (64.3-92.9) | 77.0 (50.0-90.9) | 1494.7 (870-2184) | 124.9 (96.7-168.0) | n/a |
| Smid_2020 | naive | noseed | baseline | 1/1 | 78.6 | n/a | 1369 | 124.5 | n/a |
| Smid_2020 | naive | seeded | baseline | 1/1 | 72.7 | n/a | 1369 | 171.1 | n/a |
| Welling_2021 | generated:lean-optimal (codex) | noseed | legacy | 1/1 +1 infra † | 83.0 | 83.0 | 20531 | 466.6 | n/a |
| Welling_2021 | generated:ours (codex) | noseed | legacy | 2/2 +1 infra † | 94.3 (90.6-98.1) | 94.2 (90.4-98.1) | 82722.5 (13793-151652) | 1601.9 (287.4-2916.4) | n/a |
| gao-2026-Immune checkpoint inhibitors | generated:lean-optimal (codex) | noseed | legacy | 1/1 † | 72.7 | 72.7 | 1220 | 152.5 | n/a |
| gao-2026-Immune checkpoint inhibitors | generated:ours (codex) | noseed | legacy | 2/2 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 1186 (785-1587) | 107.9 (71.4-144.3) | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | noseed | baseline | 1/1 | 72.7 | n/a | 1599 | 199.9 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | seeded | baseline | 1/1 | 62.5 | n/a | 1599 | 319.8 | n/a |
| van_Dis_2020 | generated:lean-optimal (codex) | noseed | legacy | 1/1 +1 infra † | 59.0 | 59.0 | 10137 | 281.6 | n/a |
| van_Dis_2020 | generated:ours (codex) | noseed | legacy | 2/2 +1 infra † | 93.4 (93.4-93.4) | 93.3 (93.3-93.4) | 16072.5 (15738-16407) | 282.0 (276.1-287.8) | n/a |
| van_de_Schoot_2018 | generated:lean-optimal (codex) | noseed | legacy | 1/1 +1 infra † | 92.1 | 92.1 | 7025 | 200.7 | n/a |
| van_de_Schoot_2018 | generated:ours (codex) | noseed | legacy | 1/1 +1 infra † | 92.1 | 92.1 | 31980 | 913.7 | n/a |

## Retired topics

- Jeyaraman_2020: gold set is mostly chondrocyte-implantation and microfracture trials outside the question (mesenchymal stem cells for knee osteoarthritis)

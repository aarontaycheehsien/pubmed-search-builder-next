# Evaluation results

Generated 20260930T180137Z by `python evals/run.py report`.

Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) over `ok` runs.

Version is a hash of the skill as staged into the run (`legacy`: scored before versions were recorded). Only the latest version of each skill and driver is shown; `--all-versions` shows the rest. Runs is ok/attempted; infrastructure failures (quota, rate limits) are not attempts. † fewer than 3 ok runs. ⚠ result counts differ by more than 2×.

## Development topics

Skill changes may be motivated only by these topics.

| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---|---:|---|---|---:|---:|---:|
| Appenzeller-Herzog_2019 | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 5023.7 (3365-7600) | 239.2 (160.2-361.9) | n/a |
| Appenzeller-Herzog_2019 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 5690.7 (1958-7801) | 271.0 (93.2-371.5) | n/a |
| Bos_2018 | generated:ours (codex) | noseed | 4e852a8e95 | 2/2 +1 infra † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 36514.5 (20767-52262) | 4057.1 (2307.4-5806.9) | n/a |
| Bos_2018 | generated:pubmed-search-builder-next (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 12495 | 1388.3 | 2.6 |
| Bos_2018 | generated:pubmed-search-builder-next (codex) | noseed | legacy | 2/3 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 68692 (54277-83107) | 7632.5 (6030.8-9234.1) | n/a |
| Bos_2018 | naive | noseed | baseline | 1/1 | 66.7 | n/a | 2339 | 389.8 | n/a |
| Bos_2018 | naive | seeded | baseline | 1/1 | 66.7 | n/a | 2339 | 584.8 | n/a |
| Brouwer_2019 | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 97.5 (96.3-100.0) | 97.5 (96.2-100.0) | 160769 (16856-439310) | 2987.4 (324.2-8135.4) | n/a |
| Brouwer_2019 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 96.3 (96.3-96.3) | 96.2 (96.2-96.2) | 21948.5 (17169-26728) | 422.1 (330.2-514.0) | n/a |
| CD010657 | naive | noseed | baseline | 1/1 | 91.4 | n/a | 644 | 20.1 | n/a |
| CD010657 | naive | seeded | baseline | 1/1 | 90.6 | n/a | 644 | 22.2 | n/a |
| CD011431 | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 98.7 (96.2-100.0) | 97.9 (93.8-100.0) | 6281 (1101-9304) | 246.3 (42.3-372.2) | n/a |
| CD011431 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 4565.7 (1742-7725) | 175.6 (67.0-297.1) | n/a |
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
| Kwok_2020 | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 +1 infra | 87.6 (72.4-95.7) | 86.9 (71.2-94.8) | 2707 (1079-5924) | 25.5 (10.2-53.4) | n/a |
| Kwok_2020 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 3/3 | 95.1 (94.0-95.7) | 94.6 (93.1-95.6) | 4959.7 (910-8180) | 44.7 (8.3-73.7) | n/a |
| Liu_2023_VR_nursing | naive | noseed | baseline | 1/1 | 100.0 | n/a | 374 | 62.3 | n/a |
| Medeiros-2022-School-based food and nutr | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 74.1 (66.7-88.9) | 73.6 (66.7-87.5) | 32122.3 (5776-69329) | 5058.4 (962.7-11554.8) | n/a |
| Medeiros-2022-School-based food and nutr | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 14713 (13229-16197) | 1634.8 (1469.9-1799.7) | n/a |
| Medeiros-2022-School-based food and nutr | naive | noseed | baseline | 1/1 | 11.1 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | seeded | baseline | 1/1 | 16.7 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | noseed | baseline | 1/1 | 88.9 | n/a | 24320 | 3040.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | seeded | baseline | 1/1 | 83.3 | n/a | 24320 | 4864.0 | n/a |
| Muthu_2022 | generated:quota-check (codex) | noseed | legacy | 0/1 † | n/a | n/a | n/a | n/a | n/a |
| Muthu_2022 | naive | noseed | baseline | 1/1 | 100.0 | n/a | 505 | 84.2 | n/a |
| Smid_2020 | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 92.9 (92.9-92.9) | 89.9 (88.9-90.9) | 2876.3 (1346-4869) | 221.2 (103.5-374.5) | n/a |
| Smid_2020 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 92.9 (92.9-92.9) | 91.7 (91.7-91.7) | 2053 (1407-2699) | 157.9 (108.2-207.6) | n/a |
| Smid_2020 | naive | noseed | baseline | 1/1 | 78.6 | n/a | 1369 | 124.5 | n/a |
| Smid_2020 | naive | seeded | baseline | 1/1 | 72.7 | n/a | 1369 | 171.1 | n/a |
| Welling_2021 | generated:ours (codex) | noseed | 4e852a8e95 | 3/4 | 91.2 (88.7-92.5) | 91.2 (88.7-92.5) | 16323 (12854-20244) | 336.8 (273.5-413.1) | n/a |
| Welling_2021 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 93.4 (86.8-100.0) | 93.4 (86.8-100.0) | 68084 (13167-123001) | 1303.5 (286.2-2320.8) | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | noseed | baseline | 1/1 | 72.7 | n/a | 1599 | 199.9 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | seeded | baseline | 1/1 | 62.5 | n/a | 1599 | 319.8 | n/a |
| van_de_Schoot_2018 | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 92.1 (92.1-92.1) | 90.3 (87.0-92.1) | 32403.3 (32074-32908) | 925.8 (916.4-940.2) | n/a |
| van_de_Schoot_2018 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 3/3 | 92.1 (92.1-92.1) | 91.7 (91.4-91.9) | 17903.7 (10603-32459) | 511.5 (302.9-927.4) | n/a |

## Held-out topics

Frozen before their first run; misses and audits are never kept. Claim an improvement only from the latest version with at least 3 ok runs a side. Every use is logged in `evals/heldout-ledger.jsonl`.

**A = generated:ours vs B = generated:lean-optimal** (codex, noseed): 4 win, 5 tie, 1 loss on recall; 6 topic(s) where A returns more than 2× B's results; 1 topic(s) with fewer than 3 ok runs a side.

| Topic | Recall A | Recall B | Recall | Results A | Results B | Ratio A/B | Runs A/B |
|---|---:|---:|---|---:|---:|---:|---:|
| Cohen_2006_ACEInhibitors | 100.0 | 100.0 | tie | 19,023 | 20,937 | 0.91 | 3/3 |
| Cohen_2006_ADHD | 95.0 | 95.0 | tie | 6,560 | 2,770 | 2.37 ⚠ | 3/3 |
| Cohen_2006_Antihistamines | 83.3 | 81.2 | win | 1,458 | 1,359 | 1.07 | 3/3 |
| Cohen_2006_Estrogens | 95.4 | 91.6 | win | 23,828 | 29,672 | 0.8 | 3/3 |
| Cohen_2006_UrinaryIncontinence | 80.0 | 80.0 | tie | 1,359 | 1,095 | 1.24 | 1/3 † |
| healthcare-nudging | 45.7 | 38.0 | win | 64,420 | 4,998 | 12.89 ⚠ | 3/3 |
| housing-first-criminal-justice | 100.0 | 86.7 | win | 1,662 | 385 | 4.32 ⚠ | 3/3 |
| school-restorative-practice | 88.9 | 94.4 | loss | 58,698 | 1,397 | 42.01 ⚠ | 3/3 |
| social-prescribing-older-adults | 40.0 | 40.0 | tie | 29,771 | 1,805 | 16.49 ⚠ | 3/3 |
| work-directed-return-to-work | 100.0 | 100.0 | tie | 23,011 | 8,122 | 2.83 ⚠ | 3/3 |

| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---|---:|---|---|---:|---:|---:|
| Cohen_2006_ACEInhibitors | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 20936.7 (20591-21375) | 510.6 (502.2-521.3) | n/a |
| Cohen_2006_ACEInhibitors | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 19023.3 (18551-19709) | 464.0 (452.5-480.7) | n/a |
| Cohen_2006_ADHD | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 95.0 (95.0-95.0) | 95.0 (95.0-95.0) | 2769.7 (2620-2960) | 145.8 (137.9-155.8) | n/a |
| Cohen_2006_ADHD | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 95.0 (95.0-95.0) | 93.5 (93.3-93.8) | 6559.7 (2745-9178) | 345.3 (144.5-483.1) | n/a |
| Cohen_2006_Antihistamines | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 81.2 (81.2-81.2) | 81.2 (81.2-81.2) | 1359.3 (955-2153) | 104.6 (73.5-165.6) | n/a |
| Cohen_2006_Antihistamines | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 83.3 (81.2-87.5) | 82.6 (80.0-86.7) | 1457.7 (1119-1985) | 110.1 (79.9-152.7) | n/a |
| Cohen_2006_Estrogens | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 91.6 (82.5-96.2) | 91.6 (82.5-96.2) | 29672.3 (28843-30163) | 406.2 (389.8-437.0) | n/a |
| Cohen_2006_Estrogens | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 95.4 (95.0-96.2) | 94.9 (94.5-95.5) | 23827.7 (19908-30977) | 311.7 (261.9-402.3) | n/a |
| Cohen_2006_UrinaryIncontinence | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 80.0 (80.0-80.0) | 80.0 (80.0-80.0) | 1094.7 (594-1841) | 34.2 (18.6-57.5) | n/a |
| Cohen_2006_UrinaryIncontinence | generated:ours (codex) | noseed | 4e852a8e95 | 1/3 † | 80.0 | 74.2 | 1359 | 42.5 | n/a |
| healthcare-nudging | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 38.0 (34.9-44.2) | 38.0 (34.9-44.2) | 4998 (3319-6352) | 154.1 (110.6-211.7) | n/a |
| healthcare-nudging | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 45.7 (16.3-67.4) | 42.9 (12.2-65.9) | 64420 (5871-151535) | 1443.9 (419.4-3294.2) | n/a |
| housing-first-criminal-justice | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 86.7 (80.0-100.0) | 86.7 (80.0-100.0) | 385 (361-432) | 90.2 (72.4-108.0) | n/a |
| housing-first-criminal-justice | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 1662.3 (1492-1930) | 332.5 (298.4-386.0) | n/a |
| school-restorative-practice | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 94.4 (83.3-100.0) | 94.4 (83.3-100.0) | 1397.3 (263-2989) | 235.8 (52.6-498.2) | n/a |
| school-restorative-practice | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 88.9 (83.3-100.0) | 80.6 (66.7-100.0) | 58698 (1170-99509) | 11726.6 (195.0-19901.8) | n/a |
| social-prescribing-older-adults | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 40.0 (40.0-40.0) | 40.0 (40.0-40.0) | 1805 (981-3056) | 451.2 (245.2-764.0) | n/a |
| social-prescribing-older-adults | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 40.0 (40.0-40.0) | 33.3 (33.3-33.3) | 29770.7 (937-86309) | 7442.6 (234.2-21577.2) | n/a |
| work-directed-return-to-work | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 8121.7 (7394-8690) | 738.3 (672.2-790.0) | n/a |
| work-directed-return-to-work | generated:ours (codex) | noseed | 4e852a8e95 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 23011.3 (11988-39536) | 2091.9 (1089.8-3594.2) | n/a |

## Retired topics

- Jeyaraman_2020: gold set is mostly chondrocyte-implantation and microfracture trials outside the question (mesenchymal stem cells for knee osteoarthritis)
- Menon_2022: gold set counts diet, opioid use, food insecurity and vitamin D reviews as environmental health, which the question's plain reading excludes; probes against that reading found little while recall stayed near 57%

# Evaluation results

Generated 20261002T074017Z by `python evals/run.py report`.

Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) over `ok` runs.

Version is a hash of the skill as staged into the run (`legacy`: scored before versions were recorded). Only the latest version of each skill and driver is shown; `--all-versions` shows the rest. Runs is ok/attempted; infrastructure failures (quota, rate limits) are not attempts. † fewer than 3 ok runs. ⚠ result counts differ by more than 2×.

## Development topics

Skill changes may be motivated only by these topics.

| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---|---:|---|---|---:|---:|---:|
| Appenzeller-Herzog_2019 | generated:ours (codex) | noseed | d521c529ed | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 2970.3 (1904-3981) | 141.5 (90.7-189.6) | n/a |
| Appenzeller-Herzog_2019 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 5690.7 (1958-7801) | 271.0 (93.2-371.5) | n/a |
| Bos_2018 | generated:pubmed-search-builder-next (claude) | noseed | legacy | 1/1 † | 100.0 | 100.0 | 12495 | 1388.3 | 2.6 |
| Bos_2018 | generated:pubmed-search-builder-next (codex) | noseed | legacy | 2/3 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 68692 (54277-83107) | 7632.5 (6030.8-9234.1) | n/a |
| Bos_2018 | naive | noseed | baseline | 1/1 | 66.7 | n/a | 2339 | 389.8 | n/a |
| Bos_2018 | naive | seeded | baseline | 1/1 | 66.7 | n/a | 2339 | 584.8 | n/a |
| Brouwer_2019 | generated:ours (codex) | noseed | d521c529ed | 3/3 | 98.8 (96.3-100.0) | 98.7 (96.2-100.0) | 177599.7 (25059-460729) | 3294.8 (481.9-8532.0) | n/a |
| Brouwer_2019 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 96.3 (96.3-96.3) | 96.2 (96.2-96.2) | 21948.5 (17169-26728) | 422.1 (330.2-514.0) | n/a |
| CD010657 | naive | noseed | baseline | 1/1 | 91.4 | n/a | 644 | 20.1 | n/a |
| CD010657 | naive | seeded | baseline | 1/1 | 90.6 | n/a | 644 | 22.2 | n/a |
| CD011431 | generated:ours (codex) | noseed | d521c529ed | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 3066 (1244-6046) | 117.9 (47.8-232.5) | n/a |
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
| Kwok_2020 | generated:ours (codex) | noseed | d521c529ed | 3/3 | 88.5 (74.1-95.7) | 87.6 (72.7-95.5) | 2516 (326-6236) | 23.0 (3.8-56.2) | n/a |
| Kwok_2020 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 3/3 | 95.1 (94.0-95.7) | 94.6 (93.1-95.6) | 4959.7 (910-8180) | 44.7 (8.3-73.7) | n/a |
| Liu_2023_VR_nursing | naive | noseed | baseline | 1/1 | 100.0 | n/a | 374 | 62.3 | n/a |
| Medeiros-2022-School-based food and nutr | generated:ours (codex) | noseed | d521c529ed | 3/3 | 85.2 (66.7-100.0) | 84.7 (66.7-100.0) | 20924.3 (6539-38870) | 2676.8 (817.4-4318.9) | n/a |
| Medeiros-2022-School-based food and nutr | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 14713 (13229-16197) | 1634.8 (1469.9-1799.7) | n/a |
| Medeiros-2022-School-based food and nutr | naive | noseed | baseline | 1/1 | 11.1 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | naive | seeded | baseline | 1/1 | 16.7 | n/a | 767 | 767.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | noseed | baseline | 1/1 | 88.9 | n/a | 24320 | 3040.0 | n/a |
| Medeiros-2022-School-based food and nutr | reference | seeded | baseline | 1/1 | 83.3 | n/a | 24320 | 4864.0 | n/a |
| Muthu_2022 | generated:quota-check (codex) | noseed | legacy | 0/1 † | n/a | n/a | n/a | n/a | n/a |
| Muthu_2022 | naive | noseed | baseline | 1/1 | 100.0 | n/a | 505 | 84.2 | n/a |
| Smid_2020 | generated:ours (codex) | noseed | d521c529ed | 3/3 | 92.9 (92.9-92.9) | 87.7 (85.7-90.0) | 5959.7 (2985-11582) | 458.4 (229.6-890.9) | n/a |
| Smid_2020 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 92.9 (92.9-92.9) | 91.7 (91.7-91.7) | 2053 (1407-2699) | 157.9 (108.2-207.6) | n/a |
| Smid_2020 | naive | noseed | baseline | 1/1 | 78.6 | n/a | 1369 | 124.5 | n/a |
| Smid_2020 | naive | seeded | baseline | 1/1 | 72.7 | n/a | 1369 | 171.1 | n/a |
| Welling_2021 | generated:ours (codex) | noseed | d521c529ed | 3/3 | 90.6 (90.6-90.6) | 90.4 (90.2-90.6) | 25519 (15705-43927) | 531.6 (327.2-915.1) | n/a |
| Welling_2021 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 2/3 † | 93.4 (86.8-100.0) | 93.4 (86.8-100.0) | 68084 (13167-123001) | 1303.5 (286.2-2320.8) | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | noseed | baseline | 1/1 | 72.7 | n/a | 1599 | 199.9 | n/a |
| gao-2026-Immune checkpoint inhibitors | naive | seeded | baseline | 1/1 | 62.5 | n/a | 1599 | 319.8 | n/a |
| van_de_Schoot_2018 | generated:ours (codex) | noseed | d521c529ed | 3/3 | 91.2 (89.5-92.1) | 89.7 (87.1-91.7) | 17872.7 (10252-32255) | 513.5 (301.5-921.6) | n/a |
| van_de_Schoot_2018 | generated:ours-noprobe (codex) | noseed | 8817bab45a | 3/3 | 92.1 (92.1-92.1) | 91.7 (91.4-91.9) | 17903.7 (10603-32459) | 511.5 (302.9-927.4) | n/a |

## Held-out topics

Frozen before their first run; misses and audits are never kept. Claim an improvement only from the latest version with at least 3 ok runs a side. Every use is logged in `evals/heldout-ledger.jsonl`.

**A = generated:ours vs B = generated:lean-optimal** (codex, noseed): 4 win, 3 tie, 3 loss on recall; 4 topic(s) where A returns more than 2× B's results; 10 topic(s) with fewer than 3 ok runs a side.

| Topic | Recall A | Recall B | Recall | Results A | Results B | Ratio A/B | Runs A/B |
|---|---:|---:|---|---:|---:|---:|---:|
| Cohen_2006_ACEInhibitors | 100.0 | 100.0 | tie | 23,118 | 20,937 | 1.1 | 2/3 † |
| Cohen_2006_ADHD | 95.0 | 95.0 | tie | 3,744 | 2,770 | 1.35 | 2/3 † |
| Cohen_2006_Antihistamines | 87.5 | 81.2 | win | 1,203 | 1,359 | 0.88 | 2/3 † |
| Cohen_2006_Estrogens | 96.2 | 91.6 | win | 30,298 | 29,672 | 1.02 | 2/3 † |
| Cohen_2006_UrinaryIncontinence | 80.0 | 80.0 | tie | 1,238 | 1,095 | 1.13 | 2/3 † |
| healthcare-nudging | 67.5 | 38.0 | win | 31,353 | 4,998 | 6.27 ⚠ | 2/3 † |
| housing-first-criminal-justice | 80.0 | 86.7 | loss | 1,180 | 385 | 3.06 ⚠ | 2/3 † |
| school-restorative-practice | 91.7 | 94.4 | loss | 24,322 | 1,397 | 17.41 ⚠ | 2/3 † |
| social-prescribing-older-adults | 70.0 | 40.0 | win | 20,274 | 1,805 | 11.23 ⚠ | 2/3 † |
| work-directed-return-to-work | 95.5 | 100.0 | loss | 4,918 | 8,122 | 0.61 | 2/3 † |

| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |
|---|---|---|---|---:|---|---|---:|---:|---:|
| Cohen_2006_ACEInhibitors | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 20936.7 (20591-21375) | 510.6 (502.2-521.3) | n/a |
| Cohen_2006_ACEInhibitors | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 23118 (19850-26386) | 563.9 (484.1-643.6) | n/a |
| Cohen_2006_ADHD | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 95.0 (95.0-95.0) | 95.0 (95.0-95.0) | 2769.7 (2620-2960) | 145.8 (137.9-155.8) | n/a |
| Cohen_2006_ADHD | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 95.0 (95.0-95.0) | 93.8 (92.9-94.7) | 3744 (3317-4171) | 197.1 (174.6-219.5) | n/a |
| Cohen_2006_Antihistamines | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 81.2 (81.2-81.2) | 81.2 (81.2-81.2) | 1359.3 (955-2153) | 104.6 (73.5-165.6) | n/a |
| Cohen_2006_Antihistamines | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 87.5 (87.5-87.5) | 87.5 (87.5-87.5) | 1203 (1063-1343) | 85.9 (75.9-95.9) | n/a |
| Cohen_2006_Estrogens | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 91.6 (82.5-96.2) | 91.6 (82.5-96.2) | 29672.3 (28843-30163) | 406.2 (389.8-437.0) | n/a |
| Cohen_2006_Estrogens | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 96.2 (96.2-96.2) | 95.7 (95.6-95.8) | 30298.5 (29909-30688) | 393.4 (388.4-398.5) | n/a |
| Cohen_2006_UrinaryIncontinence | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 80.0 (80.0-80.0) | 80.0 (80.0-80.0) | 1094.7 (594-1841) | 34.2 (18.6-57.5) | n/a |
| Cohen_2006_UrinaryIncontinence | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 80.0 (77.5-82.5) | 71.9 (67.9-75.9) | 1237.5 (884-1591) | 38.4 (28.5-48.2) | n/a |
| healthcare-nudging | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 38.0 (34.9-44.2) | 38.0 (34.9-44.2) | 4998 (3319-6352) | 154.1 (110.6-211.7) | n/a |
| healthcare-nudging | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 67.5 (64.0-70.9) | 64.5 (58.7-70.2) | 31353 (24054-38652) | 548.5 (394.3-702.8) | n/a |
| housing-first-criminal-justice | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 86.7 (80.0-100.0) | 86.7 (80.0-100.0) | 385 (361-432) | 90.2 (72.4-108.0) | n/a |
| housing-first-criminal-justice | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 80.0 (60.0-100.0) | 80.0 (60.0-100.0) | 1179.5 (873-1486) | 294.1 (291.0-297.2) | n/a |
| school-restorative-practice | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 94.4 (83.3-100.0) | 94.4 (83.3-100.0) | 1397.3 (263-2989) | 235.8 (52.6-498.2) | n/a |
| school-restorative-practice | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 91.7 (83.3-100.0) | 83.3 (66.7-100.0) | 24322.5 (10499-38146) | 4689.5 (1749.8-7629.2) | n/a |
| social-prescribing-older-adults | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 40.0 (40.0-40.0) | 40.0 (40.0-40.0) | 1805 (981-3056) | 451.2 (245.2-764.0) | n/a |
| social-prescribing-older-adults | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 70.0 (40.0-100.0) | 66.7 (33.3-100.0) | 20273.5 (10006-30541) | 4317.9 (1000.6-7635.2) | n/a |
| work-directed-return-to-work | generated:lean-optimal (codex) | noseed | b2569259e8 | 3/3 | 100.0 (100.0-100.0) | 100.0 (100.0-100.0) | 8121.7 (7394-8690) | 738.3 (672.2-790.0) | n/a |
| work-directed-return-to-work | generated:ours (codex) | noseed | d521c529ed | 2/2 † | 95.5 (90.9-100.0) | 93.8 (87.5-100.0) | 4917.5 (4435-5400) | 467.2 (443.5-490.9) | n/a |

## Retired topics

- Jeyaraman_2020: gold set is mostly chondrocyte-implantation and microfracture trials outside the question (mesenchymal stem cells for knee osteoarthritis)
- Menon_2022: gold set counts diet, opioid use, food insecurity and vitamin D reviews as environmental health, which the question's plain reading excludes; probes against that reading found little while recall stayed near 57%

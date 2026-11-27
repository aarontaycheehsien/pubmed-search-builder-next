# PubMed search strategy: audit

Generated 2026-11-27T16:48:49+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (Run non-interactive: user unavailable; defaults used (standard depth, no seeds, no limits); scope not confirmed by user, continuing. Benchmark records are title-screened reference lists of 4 reviews (33162910, 33207689, 32872154, 32799105). Covid-only count 128,606; with outcomes block ~26,500. Pandemics and Betacoronavirus MeSH kept for recall (non-COVID records removed at screening). Most 2020 records unindexed at cutoff so recall relies on tiab. The whole search carries an Entrez-date [edat] bound to 2020/11/22 (not a publication-date limit; rerun without it for a current search). Date bound is an Entrez-date cutoff via PSB_AS_OF=2020-11-22. Recall bound is not overall recall. Electronic Cigarettes heading does not exist (removed); vaping covered by Vaping MeSH and text. Result (~26,500) exceeds the assumed 10,000 screening limit; accepted for recall, reviewer to decide on narrowing generic terms (distress, behavio*, stress).)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and lockdown measures | search | exposure; every relevant record involves it; named reliably in title/abstract and MeSH |
| Lifestyle behaviors (physical activity, diet, sleep, screen time, smoking, alcohol) | optional | outcome; fragile. Tested alone as optional: AND-ing would lose 24 of 49 benchmark records (95% bound on loss 61.5%), so it is not AND-ed alone; superseded by the combined outcomes block |
| Well-being (mental health, distress, quality of life) | optional | outcome; broad. Tested alone as optional: AND-ing would lose 7 of 49 benchmark records (95% bound 25.2%), so it is not AND-ed alone; superseded by the combined outcomes block |
| Lifestyle behaviors or well-being (combined) | search | AND-ed on evidence and workload: covid-only result 128,606 records is too large to screen (assumed limit ~10,000); with the block ~26,500. Tested on 49 benchmark records from reference lists of 4 reviews (33162910: 5 records, 33207689: 14, 32872154: 8, 32799105: 22; top anchor ~45%): 0 lost, recall lower bound 94.1%. Benchmark skews to mental health, so lifestyle-only adult records are under-represented. Term impact measured: term impact re-measured on the current block: one benchmark record (32227671, school closure and weight gain) is retrieved in the outcomes block only through "weight gain"[tiab]/covid terms, so specific terms are kept; no known record depends on the generic terms alone, but the benchmark skews to mental health and cannot show lifestyle-only generic terms are unnecessary; generic terms (distress, behavio*, stress) were kept for recall and reviewer may narrow them. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T16:47:14+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 26,473
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"COVID-19"[Mesh]` | 57,100 | none |
| 2 | `"SARS-CoV-2"[Mesh]` | 45,940 | none |
| 3 | `"Pandemics"[Mesh]` | 50,286 | none |
| 4 | `"Quarantine"[Mesh]` | 3,938 | none |
| 5 | `"Physical Distancing"[Mesh]` | 579 | none |
| 6 | `covid*[tiab]` | 68,970 | none |
| 7 | `coronavirus*[tiab]` | 43,051 | none |
| 8 | `"corona virus*"[tiab]` | 1,355 | none |
| 9 | `sars-cov-2[tiab]` | 23,501 | none |
| 10 | `"sars cov 2"[tiab]` | 23,501 | none |
| 11 | `sarscov2[tiab]` | 19,857 | none |
| 12 | `"2019-ncov"[tiab]` | 1,287 | none |
| 13 | `ncov[tiab]` | 1,406 | none |
| 14 | `"novel coronavirus"[tiab]` | 6,186 | none |
| 15 | `"severe acute respiratory syndrome coronavirus 2"[tiab]` | 7,984 | none |
| 16 | `"nCoV-2019"[tiab]` | 40 | none |
| 17 | `pandemic*[tiab]` | 58,451 | none |
| 18 | `lockdown*[tiab]` | 3,419 | none |
| 19 | `"lock down*"[tiab]` | 179 | none |
| 20 | `"stay at home"[tiab]` | 815 | none |
| 21 | `"stay-at-home"[tiab]` | 815 | none |
| 22 | `"shelter in place"[tiab]` | 210 | none |
| 23 | `quarantin*[tiab]` | 6,954 | none |
| 24 | `"self-isolat*"[tiab]` | 400 | none |
| 25 | `"social distanc*"[tiab]` | 3,813 | none |
| 26 | `"physical distanc*"[tiab]` | 1,606 | none |
| 27 | `"home confinement"[tiab]` | 121 | none |
| 28 | `"school closure*"[tiab]` | 442 | none |
| 29 | `"movement restriction*"[tiab]` | 568 | none |
| 30 | `"containment measure*"[tiab]` | 636 | none |
| 31 | `"Betacoronavirus"[Mesh]` | 52,568 | none |
| 32 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31` | 128,606 | none |
| 33 | `"Life Style"[Mesh]` | 99,996 | none |
| 34 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 35 | `"Exercise"[Mesh]` | 212,861 | none |
| 36 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 37 | `"Diet"[Mesh]` | 296,759 | none |
| 38 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 39 | `"Sleep"[Mesh]` | 85,170 | none |
| 40 | `"Smoking"[Mesh]` | 152,983 | none |
| 41 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 42 | `"Screen Time"[Mesh]` | 608 | none |
| 43 | `lifestyle*[tiab]` | 108,843 | none |
| 44 | `"life style*"[tiab]` | 12,649 | none |
| 45 | `"health behavio*"[tiab]` | 25,773 | none |
| 46 | `behavio*[tiab]` | 1,306,377 | none |
| 47 | `"physical activit*"[tiab]` | 118,105 | none |
| 48 | `exercis*[tiab]` | 307,814 | none |
| 49 | `sedentary[tiab]` | 32,470 | none |
| 50 | `"screen time"[tiab]` | 2,454 | none |
| 51 | `diet*[tiab]` | 587,707 | none |
| 52 | `eating[tiab]` | 77,768 | none |
| 53 | `nutrition*[tiab]` | 299,564 | none |
| 54 | `sleep*[tiab]` | 188,557 | none |
| 55 | `smok*[tiab]` | 287,925 | none |
| 56 | `alcohol*[tiab]` | 346,001 | none |
| 57 | `"substance use"[tiab]` | 37,853 | none |
| 58 | `"social media"[tiab]` | 13,598 | none |
| 59 | `internet[tiab]` | 55,550 | none |
| 60 | `"Mental Health"[Mesh]` | 44,674 | none |
| 61 | `"Mental Disorders"[Mesh]` | 1,316,811 | none |
| 62 | `"Psychological Distress"[Mesh]` | 4,500 | none |
| 63 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 64 | `"Anxiety"[Mesh]` | 93,322 | none |
| 65 | `"Depression"[Mesh]` | 129,618 | none |
| 66 | `"Quality of Life"[Mesh]` | 215,485 | none |
| 67 | `"Loneliness"[Mesh]` | 4,443 | none |
| 68 | `"Affect"[Mesh]` | 34,956 | none |
| 69 | `"well-being"[tiab]` | 80,677 | none |
| 70 | `wellbeing[tiab]` | 91,509 | none |
| 71 | `"mental health"[tiab]` | 159,660 | none |
| 72 | `psycholog*[tiab]` | 295,977 | none |
| 73 | `distress[tiab]` | 119,019 | none |
| 74 | `anxiety[tiab]` | 199,914 | none |
| 75 | `depress*[tiab]` | 474,404 | none |
| 76 | `stress[tiab]` | 779,124 | none |
| 77 | `"quality of life"[tiab]` | 282,519 | none |
| 78 | `loneliness[tiab]` | 6,825 | none |
| 79 | `mood[tiab]` | 76,261 | none |
| 80 | `"life satisfaction"[tiab]` | 8,061 | none |
| 81 | `mental[tiab]` | 368,972 | none |
| 82 | `"Mental Health Services"[Mesh]` | 99,775 | none |
| 83 | `"Emotions"[Mesh]` | 353,591 | none |
| 84 | `"Fear"[Mesh]` | 35,258 | none |
| 85 | `"Sleep Initiation and Maintenance Disorders"[Mesh]` | 14,522 | none |
| 86 | `"Obesity"[Mesh]` | 228,277 | none |
| 87 | `"Weight Gain"[Mesh]` | 33,330 | none |
| 88 | `"Social Support"[Mesh]` | 74,920 | none |
| 89 | `"Adaptation, Psychological"[Mesh]` | 132,259 | none |
| 90 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 35,611 | none |
| 91 | `"health-related behavio*"[tiab]` | 3,877 | none |
| 92 | `wellness[tiab]` | 10,646 | none |
| 93 | `psychosocial[tiab]` | 102,027 | none |
| 94 | `emotion*[tiab]` | 205,757 | none |
| 95 | `fear*[tiab]` | 84,832 | none |
| 96 | `worr*[tiab]` | 23,643 | none |
| 97 | `insomnia[tiab]` | 22,051 | none |
| 98 | `"weight gain"[tiab]` | 63,432 | none |
| 99 | `obesity[tiab]` | 258,895 | none |
| 100 | `"food intake"[tiab]` | 45,992 | none |
| 101 | `"food consumption"[tiab]` | 14,333 | none |
| 102 | `"eating habit*"[tiab]` | 5,697 | none |
| 103 | `"physical inactivity"[tiab]` | 8,195 | none |
| 104 | `"mental illness*"[tiab]` | 32,711 | none |
| 105 | `"mental disorder*"[tiab]` | 48,627 | none |
| 106 | `resilien*[tiab]` | 35,816 | none |
| 107 | `coping[tiab]` | 56,356 | none |
| 108 | `suicid*[tiab]` | 80,380 | none |
| 109 | `"social support"[tiab]` | 40,802 | none |
| 110 | `"social connect*"[tiab]` | 2,195 | none |
| 111 | `"social isolation"[tiab]` | 7,931 | none |
| 112 | `anxious[tiab]` | 17,082 | none |
| 113 | `"post-traumatic"[tiab]` | 31,780 | none |
| 114 | `ptsd[tiab]` | 25,928 | none |
| 115 | `"daily routine*"[tiab]` | 4,302 | none |
| 116 | `"daily life"[tiab]` | 20,183 | none |
| 117 | `"cigarette*"[tiab]` | 73,787 | none |
| 118 | `"substance abuse"[tiab]` | 25,726 | none |
| 119 | `"binge"[tiab]` | 13,938 | none |
| 120 | `"gaming"[tiab]` | 3,672 | none |
| 121 | `"physical fitness"[tiab]` | 10,559 | none |
| 122 | `walking[tiab]` | 73,722 | none |
| 123 | `"mental wellbeing"[tiab]` | 803 | none |
| 124 | `"Motor Activity"[Mesh]` | 309,968 | none |
| 125 | `"Social Isolation"[Mesh]` | 22,365 | none |
| 126 | `"Video Games"[Mesh]` | 6,114 | none |
| 127 | `"Vaping"[Mesh]` | 1,993 | none |
| 128 | `e-cigarette*[tiab]` | 4,975 | none |
| 129 | `vaping[tiab]` | 1,632 | none |
| 130 | `"video game*"[tiab]` | 3,660 | none |
| 131 | `television[tiab]` | 14,192 | none |
| 132 | `sitting[tiab]` | 23,130 | none |
| 133 | `"screen use"[tiab]` | 173 | none |
| 134 | `"physical exercise"[tiab]` | 16,291 | none |
| 135 | `#33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96 OR #97 OR #98 OR #99 OR #100 OR #101 OR #102 OR #103 OR #104 OR #105 OR #106 OR #107 OR #108 OR #109 OR #110 OR #111 OR #112 OR #113 OR #114 OR #115 OR #116 OR #117 OR #118 OR #119 OR #120 OR #121 OR #122 OR #123 OR #124 OR #125 OR #126 OR #127 OR #128 OR #129 OR #130 OR #131 OR #132 OR #133 OR #134` | 6,316,011 | none |
| 136 | `#32 AND #135` | 26,473 | none |

### Strategy (single line, for copying into PubMed)

```text
(("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR "Pandemics"[Mesh] OR "Quarantine"[Mesh] OR "Physical Distancing"[Mesh] OR covid*[tiab] OR coronavirus*[tiab] OR "corona virus*"[tiab] OR sars-cov-2[tiab] OR "sars cov 2"[tiab] OR sarscov2[tiab] OR "2019-ncov"[tiab] OR ncov[tiab] OR "novel coronavirus"[tiab] OR "severe acute respiratory syndrome coronavirus 2"[tiab] OR "nCoV-2019"[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR "lock down*"[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "shelter in place"[tiab] OR quarantin*[tiab] OR "self-isolat*"[tiab] OR "social distanc*"[tiab] OR "physical distanc*"[tiab] OR "home confinement"[tiab] OR "school closure*"[tiab] OR "movement restriction*"[tiab] OR "containment measure*"[tiab] OR "Betacoronavirus"[Mesh]) AND ("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Sleep"[Mesh] OR "Smoking"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Screen Time"[Mesh] OR lifestyle*[tiab] OR "life style*"[tiab] OR "health behavio*"[tiab] OR behavio*[tiab] OR "physical activit*"[tiab] OR exercis*[tiab] OR sedentary[tiab] OR "screen time"[tiab] OR diet*[tiab] OR eating[tiab] OR nutrition*[tiab] OR sleep*[tiab] OR smok*[tiab] OR alcohol*[tiab] OR "substance use"[tiab] OR "social media"[tiab] OR internet[tiab] OR "Mental Health"[Mesh] OR "Mental Disorders"[Mesh] OR "Psychological Distress"[Mesh] OR "Stress, Psychological"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR "Quality of Life"[Mesh] OR "Loneliness"[Mesh] OR "Affect"[Mesh] OR "well-being"[tiab] OR wellbeing[tiab] OR "mental health"[tiab] OR psycholog*[tiab] OR distress[tiab] OR anxiety[tiab] OR depress*[tiab] OR stress[tiab] OR "quality of life"[tiab] OR loneliness[tiab] OR mood[tiab] OR "life satisfaction"[tiab] OR mental[tiab] OR "Mental Health Services"[Mesh] OR "Emotions"[Mesh] OR "Fear"[Mesh] OR "Sleep Initiation and Maintenance Disorders"[Mesh] OR "Obesity"[Mesh] OR "Weight Gain"[Mesh] OR "Social Support"[Mesh] OR "Adaptation, Psychological"[Mesh] OR "Stress Disorders, Post-Traumatic"[Mesh] OR "health-related behavio*"[tiab] OR wellness[tiab] OR psychosocial[tiab] OR emotion*[tiab] OR fear*[tiab] OR worr*[tiab] OR insomnia[tiab] OR "weight gain"[tiab] OR obesity[tiab] OR "food intake"[tiab] OR "food consumption"[tiab] OR "eating habit*"[tiab] OR "physical inactivity"[tiab] OR "mental illness*"[tiab] OR "mental disorder*"[tiab] OR resilien*[tiab] OR coping[tiab] OR suicid*[tiab] OR "social support"[tiab] OR "social connect*"[tiab] OR "social isolation"[tiab] OR anxious[tiab] OR "post-traumatic"[tiab] OR ptsd[tiab] OR "daily routine*"[tiab] OR "daily life"[tiab] OR "cigarette*"[tiab] OR "substance abuse"[tiab] OR "binge"[tiab] OR "gaming"[tiab] OR "physical fitness"[tiab] OR walking[tiab] OR "mental wellbeing"[tiab] OR "Motor Activity"[Mesh] OR "Social Isolation"[Mesh] OR "Video Games"[Mesh] OR "Vaping"[Mesh] OR e-cigarette*[tiab] OR vaping[tiab] OR "video game*"[tiab] OR television[tiab] OR sitting[tiab] OR "screen use"[tiab] OR "physical exercise"[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 49 | 49 | 100.0% | 49 / 49 |

49 of the 49 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 94.1% (95% bound; it is as wide as the number of such records makes it).

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 14 | 14 | 5 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 14 | 14 | 5 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 14 |
| C6 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 14 |
| C8 | 2026-11-27 | PubMed | backward | 1 | 49 | 49 | 9 |
| C9 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 23 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid | 6,316,011 | 0 |
| outcomes | 128,606 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Lifestyle behaviors (lifestyle) | 26,473 | 11,925 | 24 / 49 | 24 / 49 | 61.5% |
| Well-being and mental health (wellbeing) | 26,473 | 13,822 | 7 / 49 | 7 / 49 | 25.2% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 332,549 | initial | none | initial covid block + optional outcome blocks |
| 2 | 128,606 | covid: +1 / -5 | none | removed generic epidemic/outbreak/confinement/social isolation, Coronavirus Infections to cut non-COVID noise |
| 3 | 106,103 | covid: +5 / -5 | none | restructured top5 generic covid terms (pandemic*, coronavirus*, covid*, quarantin*, Betacoronavirus) with combined outcomes qualifier; no known record lost |
| 4 | 126,604 | covid: +4 / -4 | none | reverted restructure; broadened outcomes optional block to test AND-ing |
| 5 | 26,108 | covid: +1 / -1; outcomes: +92 / -0 | none | AND outcomes block for workload (0/19 known lost, bound 14.6%); fixed Betacoronavirus term |
| 6 | 26,108 | limits/combination | none | removed duplicate Health Behavior MeSH |
| 7 | 26,473 | outcomes: +12 / -0 | none | added Motor Activity, Social Isolation, Video Games, vaping/e-cig MeSH and vaping, e-cigarette*, video game*, television, sitting, screen use, physical exercise (critic F4/F5); term impact on current block |
| 8 | 26,473 | outcomes: +0 / -1 | none | removed nonexistent Electronic Cigarettes MeSH; rationales corrected (critic F1,F2); generic outcome terms retained after term-impact (no known record depends solely on them) |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 6: 7 findings; F1 must-fix open, F2 must-fix open, F3 should-fix open, F4 should-fix open, F5 should-fix open, F6 document accepted-risk, F7 document accepted-risk
- Round 2 on version 8: 9 findings; F1 must-fix resolved, F2 must-fix open, F3 should-fix open, F4 should-fix resolved, F5 should-fix resolved, F6 document accepted-risk, F7 document accepted-risk, F8 must-fix open, F9 document open
- Round 3 on version 8: 9 findings; F1 must-fix resolved, F2 must-fix resolved, F3 should-fix accepted-risk, F4 should-fix resolved, F5 should-fix resolved, F6 document accepted-risk, F7 document accepted-risk, F8 must-fix resolved, F9 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 3507 NCBI requests logged (1895 from cache); strategy sha256 037bb0318044._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [],
    "issues": []
  },
  "vocabulary": [
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000086382",
          "name": "COVID-19",
          "type": "descriptor",
          "scope_note": "A viral disorder generally characterized by high FEVER; COUGH; DYSPNEA; CHILLS; PERSISTENT TREMOR; MUSCLE PAIN; HEADACHE; SORE THROAT; a new loss of taste and/or smell (see AGEUSIA and ANOSMIA) and other symptoms of a VIRAL PNEUMONIA. A coronavirus, SARS-CoV-2 VIRUS, in the genus BETACORONAVIRUS is the causative agent.",
          "tree_numbers": [
            "C01.748.610.763.500",
            "C01.925.705.500",
            "C01.925.782.600.550.200.163",
            "C08.381.677.807.500",
            "C08.730.610.763.500"
          ],
          "entry_terms": 36,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000086382",
      "preferred_label": "COVID-19",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"COVID-19\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "SARS-CoV-2",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000086402",
          "name": "SARS-CoV-2",
          "type": "descriptor",
          "scope_note": "A species of BETACORONAVIRUS causing atypical respiratory disease (COVID-19) in humans. The organism was first identified in 2019 in Wuhan, China. The natural host is the Chinese intermediate horseshoe bat, RHINOLOPHUS affinis.",
          "tree_numbers": [
            "B04.820.578.500.540.150.113.937.500"
          ],
          "entry_terms": 24,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000086402",
      "preferred_label": "SARS-CoV-2",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"SARS-CoV-2\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D058873",
          "name": "Pandemics",
          "type": "descriptor",
          "scope_note": "Epidemics of infectious disease that have spread to many countries, often more than one continent, and usually affecting a large number of people.",
          "tree_numbers": [
            "N06.850.290.200.600"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D058873",
      "preferred_label": "Pandemics",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Pandemics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011790",
          "name": "Quarantine",
          "type": "descriptor",
          "scope_note": "Limited freedom of movement of individuals to reduce the risk of spread of communicable disease by those who have been exposed to infectious or communicable disease in order to prevent its spread; a period of detention of vessels, vehicles, or travelers coming from infected or suspected places; and detention or isolation on account of suspected contagion. It includes government regulations on t...",
          "tree_numbers": [
            "N06.850.780.200.725"
          ],
          "entry_terms": 28,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011790",
      "preferred_label": "Quarantine",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Quarantine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Physical Distancing",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000085762",
          "name": "Physical Distancing",
          "type": "descriptor",
          "scope_note": "Maintaining recommended amount of spatial separation between self and others.",
          "tree_numbers": [
            "N06.850.780.200.688"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000085762",
      "preferred_label": "Physical Distancing",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "\"Physical Distancing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Betacoronavirus",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000073640",
          "name": "Betacoronavirus",
          "type": "descriptor",
          "scope_note": "A genus of the family CORONAVIRIDAE which causes respiratory or gastrointestinal disease in a variety of mostly mammals. Human betacoronaviruses include HUMAN ENTERIC CORONAVIRUS; HUMAN CORONAVIRUS OC43; MERS VIRUS; and SEVERE ACUTE RESPIRATORY SYNDROME-RELATED CORONAVIRUS. Members have either core transcription regulatory sequences of 5’-CUAAAC-3’ or 5’-CUAAAC-3’ and mostly have no ORF downstr...",
          "tree_numbers": [
            "B04.820.578.500.540.150.113"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000073640",
      "preferred_label": "Betacoronavirus",
      "type": "descriptor",
      "location": "vocabulary:31",
      "term": {
        "text": "\"Betacoronavirus\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008019",
          "name": "Life Style",
          "type": "descriptor",
          "scope_note": "Typical way of life or manner of living characteristic of an individual or group. (From APA, Thesaurus of Psychological Index Terms, 8th ed)",
          "tree_numbers": [
            "F01.829.458"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008019",
      "preferred_label": "Life Style",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015438",
          "name": "Health Behavior",
          "type": "descriptor",
          "scope_note": "Combination of HEALTH KNOWLEDGE, ATTITUDES, PRACTICE which underlie actions taken by individuals regarding their health.",
          "tree_numbers": [
            "F01.145.488"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015438",
      "preferred_label": "Health Behavior",
      "type": "descriptor",
      "location": "vocabulary:33",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015444",
          "name": "Exercise",
          "type": "descriptor",
          "scope_note": "Physical activity which is usually regular and done with the intention of improving or maintaining PHYSICAL FITNESS or HEALTH. Contrast with PHYSICAL EXERTION which is concerned largely with the physiologic and metabolic response to energy expenditure.",
          "tree_numbers": [
            "G11.427.410.698.277",
            "I03.350"
          ],
          "entry_terms": 27,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015444",
      "preferred_label": "Exercise",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D057185",
          "name": "Sedentary Behavior",
          "type": "descriptor",
          "scope_note": "Behaviors during waking hours that have low energy expenditure and are often performed in a sitting or reclining POSTURE.",
          "tree_numbers": [
            "F01.145.749",
            "F01.829.458.705"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D057185",
      "preferred_label": "Sedentary Behavior",
      "type": "descriptor",
      "location": "vocabulary:35",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004032",
          "name": "Diet",
          "type": "descriptor",
          "scope_note": "Regular course of eating and drinking adopted by a person or animal.",
          "tree_numbers": [
            "G07.203.650.240"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004032",
      "preferred_label": "Diet",
      "type": "descriptor",
      "location": "vocabulary:36",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005247",
          "name": "Feeding Behavior",
          "type": "descriptor",
          "scope_note": "Behavioral responses or sequences associated with eating including modes of feeding, rhythmic patterns of eating, and time intervals.",
          "tree_numbers": [
            "F01.145.113.547",
            "F01.145.407",
            "G07.203.650.353"
          ],
          "entry_terms": 35,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005247",
      "preferred_label": "Feeding Behavior",
      "type": "descriptor",
      "location": "vocabulary:37",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012890",
          "name": "Sleep",
          "type": "descriptor",
          "scope_note": "A readily reversible suspension of sensorimotor interaction with the environment, usually associated with recumbency and immobility.",
          "tree_numbers": [
            "F02.830.855",
            "G11.561.803"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012890",
      "preferred_label": "Sleep",
      "type": "descriptor",
      "location": "vocabulary:38",
      "term": {
        "text": "\"Sleep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012907",
          "name": "Smoking",
          "type": "descriptor",
          "scope_note": "Willful or deliberate act of inhaling and exhaling SMOKE from burning substances or agents held by hand.",
          "tree_numbers": [
            "F01.145.805"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012907",
      "preferred_label": "Smoking",
      "type": "descriptor",
      "location": "vocabulary:39",
      "term": {
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000428",
          "name": "Alcohol Drinking",
          "type": "descriptor",
          "scope_note": "Behaviors associated with the ingesting of ALCOHOLIC BEVERAGES, including social drinking.",
          "tree_numbers": [
            "F01.145.317.269"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000428",
      "preferred_label": "Alcohol Drinking",
      "type": "descriptor",
      "location": "vocabulary:40",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Screen Time",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000077705",
          "name": "Screen Time",
          "type": "descriptor",
          "scope_note": "Period of activities done in front of an electronic screen, such as watching TV, working on a computer, or playing video games.",
          "tree_numbers": [
            "I03.723"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000077705",
      "preferred_label": "Screen Time",
      "type": "descriptor",
      "location": "vocabulary:41",
      "term": {
        "text": "\"Screen Time\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008603",
          "name": "Mental Health",
          "type": "descriptor",
          "scope_note": "Emotional, psychological, and social well-being of an individual or group.",
          "tree_numbers": [
            "F02.418",
            "N01.400.500"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008603",
      "preferred_label": "Mental Health",
      "type": "descriptor",
      "location": "vocabulary:59",
      "term": {
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001523",
          "name": "Mental Disorders",
          "type": "descriptor",
          "scope_note": "Psychiatric illness or diseases manifested by breakdowns in the adaptational process expressed primarily as abnormalities of thought, feeling, and behavior producing either distress or impairment of function.",
          "tree_numbers": [
            "F03"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001523",
      "preferred_label": "Mental Disorders",
      "type": "descriptor",
      "location": "vocabulary:60",
      "term": {
        "text": "\"Mental Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000079225",
          "name": "Psychological Distress",
          "type": "descriptor",
          "scope_note": "Negative emotional state characterized by physical and/or emotional discomfort, pain, or anguish.",
          "tree_numbers": [
            "F01.470.315"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000079225",
      "preferred_label": "Psychological Distress",
      "type": "descriptor",
      "location": "vocabulary:61",
      "term": {
        "text": "\"Psychological Distress\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013315",
          "name": "Stress, Psychological",
          "type": "descriptor",
          "scope_note": "Stress wherein emotional factors predominate.",
          "tree_numbers": [
            "F01.145.126.990",
            "F02.830.900"
          ],
          "entry_terms": 47,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013315",
      "preferred_label": "Stress, Psychological",
      "type": "descriptor",
      "location": "vocabulary:62",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001007",
          "name": "Anxiety",
          "type": "descriptor",
          "scope_note": "Feelings or emotions of dread, apprehension, and impending disaster but not disabling as with ANXIETY DISORDERS.",
          "tree_numbers": [
            "F01.470.132"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001007",
      "preferred_label": "Anxiety",
      "type": "descriptor",
      "location": "vocabulary:63",
      "term": {
        "text": "\"Anxiety\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003863",
          "name": "Depression",
          "type": "descriptor",
          "scope_note": "Depressive states usually of moderate intensity in contrast with MAJOR DEPRESSIVE DISORDER present in neurotic and psychotic disorders.",
          "tree_numbers": [
            "F01.145.126.350",
            "F01.470.282"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003863",
      "preferred_label": "Depression",
      "type": "descriptor",
      "location": "vocabulary:64",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011788",
          "name": "Quality of Life",
          "type": "descriptor",
          "scope_note": "A generic concept reflecting concern with the modification and enhancement of life attributes, e.g., physical, political, moral, social environment as well as health and disease.",
          "tree_numbers": [
            "I01.800",
            "K01.752.400.750",
            "N06.850.505.400.425.837"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011788",
      "preferred_label": "Quality of Life",
      "type": "descriptor",
      "location": "vocabulary:65",
      "term": {
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Loneliness",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008132",
          "name": "Loneliness",
          "type": "descriptor",
          "scope_note": "The state of feeling sad or dejected as a result of lack of companionship or being separated from others.",
          "tree_numbers": [
            "F01.470.713",
            "I01.880.853.748.435"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008132",
      "preferred_label": "Loneliness",
      "type": "descriptor",
      "location": "vocabulary:66",
      "term": {
        "text": "\"Loneliness\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Affect",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000339",
          "name": "Affect",
          "type": "descriptor",
          "scope_note": "The feeling-tone accompaniment of an idea or mental representation. It is the most direct psychic derivative of instinct and the psychic representative of the various bodily changes by means of which instincts manifest themselves.",
          "tree_numbers": [
            "F01.470.047"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000339",
      "preferred_label": "Affect",
      "type": "descriptor",
      "location": "vocabulary:67",
      "term": {
        "text": "\"Affect\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008605",
          "name": "Mental Health Services",
          "type": "descriptor",
          "scope_note": "Organized services to provide mental health care.",
          "tree_numbers": [
            "F04.408",
            "N02.421.461"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008605",
      "preferred_label": "Mental Health Services",
      "type": "descriptor",
      "location": "vocabulary:81",
      "term": {
        "text": "\"Mental Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Emotions",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004644",
          "name": "Emotions",
          "type": "descriptor",
          "scope_note": "Those affective states which can be experienced and have arousing and motivational properties.",
          "tree_numbers": [
            "F01.470"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004644",
      "preferred_label": "Emotions",
      "type": "descriptor",
      "location": "vocabulary:82",
      "term": {
        "text": "\"Emotions\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fear",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005239",
          "name": "Fear",
          "type": "descriptor",
          "scope_note": "The affective response to an actual current external danger which subsides with the elimination of the threatening condition.",
          "tree_numbers": [
            "F01.470.361"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005239",
      "preferred_label": "Fear",
      "type": "descriptor",
      "location": "vocabulary:83",
      "term": {
        "text": "\"Fear\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep Initiation and Maintenance Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007319",
          "name": "Sleep Initiation and Maintenance Disorders",
          "type": "descriptor",
          "scope_note": "Disorders characterized by impairment of the ability to initiate or maintain sleep. This may occur as a primary disorder or in association with another medical or psychiatric condition.",
          "tree_numbers": [
            "C10.886.425.800.800",
            "F03.870.400.800.800"
          ],
          "entry_terms": 27,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007319",
      "preferred_label": "Sleep Initiation and Maintenance Disorders",
      "type": "descriptor",
      "location": "vocabulary:84",
      "term": {
        "text": "\"Sleep Initiation and Maintenance Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Obesity",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009765",
          "name": "Obesity",
          "type": "descriptor",
          "scope_note": "A status with BODY WEIGHT that is grossly above the recommended standards, usually due to accumulation of excess FATS in the body. The standards may vary with age, sex, genetic or cultural background. In the BODY MASS INDEX, a BMI greater than 30.0 kg/m2 is considered obese, and a BMI greater than 40.0 kg/m2 is considered morbidly obese (MORBID OBESITY).",
          "tree_numbers": [
            "C18.654.726.750.500",
            "C23.888.144.699.500"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009765",
      "preferred_label": "Obesity",
      "type": "descriptor",
      "location": "vocabulary:85",
      "term": {
        "text": "\"Obesity\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Weight Gain",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015430",
          "name": "Weight Gain",
          "type": "descriptor",
          "scope_note": "Increase in BODY WEIGHT over existing weight.",
          "tree_numbers": [
            "C23.888.144.243.926",
            "G07.345.249.314.120.200.926"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015430",
      "preferred_label": "Weight Gain",
      "type": "descriptor",
      "location": "vocabulary:86",
      "term": {
        "text": "\"Weight Gain\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Support",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012944",
          "name": "Social Support",
          "type": "descriptor",
          "scope_note": "Support systems that provide assistance and encouragement to individuals with physical or emotional disabilities in order that they may better cope. Informal social support is usually provided by friends, relatives, or peers, while formal assistance such as COMMUNITY SUPPORT is provided by churches, groups, etc.",
          "tree_numbers": [
            "I01.880.853.500.600"
          ],
          "entry_terms": 14,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012944",
      "preferred_label": "Social Support",
      "type": "descriptor",
      "location": "vocabulary:87",
      "term": {
        "text": "\"Social Support\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adaptation, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000223",
          "name": "Adaptation, Psychological",
          "type": "descriptor",
          "scope_note": "A state of harmony between internal needs and external demands and the processes used in achieving this condition. (From APA Thesaurus of Psychological Index Terms, 8th ed).",
          "tree_numbers": [
            "F01.058"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000223",
      "preferred_label": "Adaptation, Psychological",
      "type": "descriptor",
      "location": "vocabulary:88",
      "term": {
        "text": "\"Adaptation, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013313",
          "name": "Stress Disorders, Post-Traumatic",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders with symptoms that last more than one month.",
          "tree_numbers": [
            "F03.950.750.500"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013313",
      "preferred_label": "Stress Disorders, Post-Traumatic",
      "type": "descriptor",
      "location": "vocabulary:89",
      "term": {
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009043",
          "name": "Motor Activity",
          "type": "descriptor",
          "scope_note": "Body movements of a human or an animal as a behavioral phenomenon.",
          "tree_numbers": [
            "F01.145.632",
            "G11.427.410.698"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009043",
      "preferred_label": "Motor Activity",
      "type": "descriptor",
      "location": "vocabulary:123",
      "term": {
        "text": "\"Motor Activity\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012934",
          "name": "Social Isolation",
          "type": "descriptor",
          "scope_note": "The separation of individuals or groups resulting in the lack of or minimizing of social contact and/or communication. This separation may be accomplished by physical separation, by social barriers and by psychological mechanisms. In the latter, there may be interaction but no real communication.",
          "tree_numbers": [
            "F01.145.813.781",
            "I01.880.853.748"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012934",
      "preferred_label": "Social Isolation",
      "type": "descriptor",
      "location": "vocabulary:124",
      "term": {
        "text": "\"Social Isolation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Video Games",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D018910",
          "name": "Video Games",
          "type": "descriptor",
          "scope_note": "A form of interactive entertainment in which the player controls electronically generated images that appear on a video display screen. This includes video games played in the home on special machines or home computers, and those played in arcades.",
          "tree_numbers": [
            "I03.450.642.693.930",
            "L01.224.900.930"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D018910",
      "preferred_label": "Video Games",
      "type": "descriptor",
      "location": "vocabulary:125",
      "term": {
        "text": "\"Video Games\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Vaping",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:47:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000072137",
          "name": "Vaping",
          "type": "descriptor",
          "scope_note": "Inhaling of vapors produced by ELECTRONIC NICOTINE DELIVERY SYSTEMS such as E-CIGARETTES.",
          "tree_numbers": [
            "F01.145.805.500"
          ],
          "entry_terms": 29,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000072137",
      "preferred_label": "Vaping",
      "type": "descriptor",
      "location": "vocabulary:126",
      "term": {
        "text": "\"Vaping\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"sars cov 2\"[MeSH Terms] OR \"Pandemics\"[MeSH Terms] OR \"Quarantine\"[MeSH Terms] OR \"Physical Distancing\"[MeSH Terms] OR \"covid*\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"corona virus*\"[Title/Abstract] OR \"sars cov 2\"[Title/Abstract] OR \"sars cov 2\"[Title/Abstract] OR \"sarscov2\"[Title/Abstract] OR \"2019-ncov\"[Title/Abstract] OR \"ncov\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"severe acute respiratory syndrome coronavirus 2\"[Title/Abstract] OR \"nCoV-2019\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter in place\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"social distanc*\"[Title/Abstract] OR \"physical distanc*\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"school closure*\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"containment measure*\"[Title/Abstract] OR \"Betacoronavirus\"[MeSH Terms]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Screen Time\"[MeSH Terms] OR \"lifestyle*\"[Title/Abstract] OR \"life style*\"[Title/Abstract] OR \"health behavio*\"[Title/Abstract] OR \"behavio*\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"Screen Time\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"sleep*\"[Title/Abstract] OR \"smok*\"[Title/Abstract] OR \"alcohol*\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"social media\"[Title/Abstract] OR \"internet\"[Title/Abstract] OR \"Mental Health\"[MeSH Terms] OR \"Mental Disorders\"[MeSH Terms] OR \"Psychological Distress\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"Loneliness\"[MeSH Terms] OR \"Affect\"[MeSH Terms] OR \"well-being\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"psycholog*\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"Loneliness\"[Title/Abstract] OR \"mood\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"mental\"[Title/Abstract] OR \"Mental Health Services\"[MeSH Terms] OR \"Emotions\"[MeSH Terms] OR \"Fear\"[MeSH Terms] OR \"Sleep Initiation and Maintenance Disorders\"[MeSH Terms] OR \"Obesity\"[MeSH Terms] OR \"Weight Gain\"[MeSH Terms] OR \"Social Support\"[MeSH Terms] OR \"adaptation, psychological\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"health related behavio*\"[Title/Abstract] OR \"wellness\"[Title/Abstract] OR \"psychosocial\"[Title/Abstract] OR \"emotion*\"[Title/Abstract] OR \"fear*\"[Title/Abstract] OR \"worr*\"[Title/Abstract] OR \"insomnia\"[Title/Abstract] OR \"Weight Gain\"[Title/Abstract] OR \"Obesity\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"eating habit*\"[Title/Abstract] OR \"physical inactivity\"[Title/Abstract] OR \"mental illness*\"[Title/Abstract] OR \"mental disorder*\"[Title/Abstract] OR \"resilien*\"[Title/Abstract] OR \"coping\"[Title/Abstract] OR \"suicid*\"[Title/Abstract] OR \"Social Support\"[Title/Abstract] OR \"social connect*\"[Title/Abstract] OR \"Social Isolation\"[Title/Abstract] OR \"anxious\"[Title/Abstract] OR \"post-traumatic\"[Title/Abstract] OR \"ptsd\"[Title/Abstract] OR \"daily routine*\"[Title/Abstract] OR \"daily life\"[Title/Abstract] OR \"cigarette*\"[Title/Abstract] OR \"substance abuse\"[Title/Abstract] OR \"binge\"[Title/Abstract] OR \"gaming\"[Title/Abstract] OR \"physical fitness\"[Title/Abstract] OR \"walking\"[Title/Abstract] OR \"mental wellbeing\"[Title/Abstract] OR \"Motor Activity\"[MeSH Terms] OR \"Social Isolation\"[MeSH Terms] OR \"Video Games\"[MeSH Terms] OR \"Vaping\"[MeSH Terms] OR \"e cigarette*\"[Title/Abstract] OR \"Vaping\"[Title/Abstract] OR \"video game*\"[Title/Abstract] OR \"television\"[Title/Abstract] OR \"sitting\"[Title/Abstract] OR \"screen use\"[Title/Abstract] OR \"physical exercise\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 6,
      "review_sha256": "6c07e238d590d6ecb014e254ed6266fff5fe04d8a2792c8ec1c46c5df844d140",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All lines ran with no warnings. Every named concept has its own bare term. Lines 9/10 and 20/21 redundant but harmless."
        },
        "operators": {
          "verdict": "pass",
          "note": "(covid OR-block) AND (outcomes OR-block). Outcomes AND lost 0 of 49 benchmark records. Each optional block alone would lose records (lifestyle 24/49, well-being 7/49), so the union is right."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Pandemics and Betacoronavirus pull non-COVID records (precision only). Motor Activity, Social Isolation, Communicable Disease Control not tried/documented. 2020 literature largely unindexed at cutoff so recall relies on tiab."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Outcomes block very broad (behavio*, stress, mental, internet, eating, walking, gaming, binge, exercis*); result 26,108 above assumed 10,000 limit. Rerun term-impact on current block. Missing synonyms: vaping, e-cigarette, video game*, television, sitting, screen use, physical exercise."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags, parentheses, line numbering correct; no phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only the entry-date cutoff from PSB_AS_OF; document that edat differs from publication date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Rationales for lifestyle and well-being quote stale figures (7/19, 1/19) from an earlier benchmark; current is 24/49 and 7/49.",
          "recommendation": "Update both rationales to current values.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Benchmark set source names only 2 of 4 reviews; covid-only count quoted as ~126,600/126,604 but measured 128,606.",
          "recommendation": "Reconcile source field with four anchors; correct count to 128,606; note top anchor share.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Result 26,108 exceeds assumed 10,000 limit; outcomes block dominated by non-specific terms; term-impact measured on earlier version only.",
          "recommendation": "Rerun term-impact on current block; test dropping generic terms with 0 benchmark loss; keep retained generic terms with reasons.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Lifestyle synonyms not searched: vaping/e-cigarette, television/video game, sitting, screen use, physical exercise.",
          "recommendation": "Add and test them.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F5",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Motor Activity, Social Isolation, Communicable Disease Control headings not included or documented; Pandemics/Betacoronavirus add non-COVID records.",
          "recommendation": "Test Motor Activity and Social Isolation in outcomes; document Pandemics/Betacoronavirus kept for recall.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "Recall bound 94.1% rests on 49 title-screened reference-list records skewed to mental health and children; scope not user-confirmed.",
          "recommendation": "Report with these limits; not overall recall.",
          "status": "accepted-risk",
          "response": "Stated in notes and rationale; kept in final report."
        },
        {
          "id": "F7",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "Redundant variants (sars cov 2, stay at home).",
          "recommendation": "Optional removal.",
          "status": "accepted-risk",
          "response": "Kept: no recall or count effect."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 8,
      "review_sha256": "7f7b807945d8c5ed4e3689d0479c0999ce58452f0e8d1a6dd11cb3a6310a17fc",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All lines ran with no warnings; bare names covered."
        },
        "operators": {
          "verdict": "pass",
          "note": "(covid) AND (combined outcomes); lifestyle/well-being optional blocks correctly left out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Motor Activity, Social Isolation, Vaping, Video Games added; Electronic Cigarettes removed; Pandemics/Betacoronavirus documented."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Result 26,473 about 2.6x assumed limit; term impact measured on earlier version; generic terms kept without tested alternative."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags and parentheses correct."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Anchor counts swapped in rationale; benchmark source names 2 of 4 reviews; as_of null while edat bound applied."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Stale rationale figures.",
          "recommendation": "Update.",
          "status": "resolved",
          "response": "Rationales now state 24/49 and 7/49."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Benchmark source field names only 2 of 4 reviews.",
          "recommendation": "Name all four.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Result 26,473 vs assumed 10,000; term impact measured on earlier version; generic terms kept without tested alternative.",
          "recommendation": "Rerun term impact on current block; state evidence for kept generic terms; record decision if large result accepted.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Lifestyle synonyms not searched.",
          "recommendation": "Add and test.",
          "status": "resolved",
          "response": "Added and tested; no known record lost."
        },
        {
          "id": "F5",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Headings missing/undocumented.",
          "recommendation": "Add and document.",
          "status": "resolved",
          "response": "Added; documented in notes."
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "Recall bound limits.",
          "recommendation": "Report with limits.",
          "status": "accepted-risk",
          "response": "Stated in notes and rationale."
        },
        {
          "id": "F7",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "Redundant variants.",
          "recommendation": "Optional.",
          "status": "accepted-risk",
          "response": "Kept; no effect."
        },
        {
          "id": "F8",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Anchor record counts swapped in rationale.",
          "recommendation": "Correct to 32799105: 22, 32872154: 8.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F9",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "Protocol as_of null but edat bound applied.",
          "recommendation": "State cutoff in report.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 8,
      "review_sha256": "5df23cd32cd06febf387a8714966311af3ee2e8068ec4c40df189dd9602e16f5",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Closing round: verified against current strategy; no blocking issue."
        },
        "operators": {
          "verdict": "pass",
          "note": "Closing round: verified against current strategy; no blocking issue."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Closing round: verified against current strategy; no blocking issue."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Closing round: verified against current strategy; no blocking issue."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Closing round: verified against current strategy; no blocking issue."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Closing round: verified against current strategy; no blocking issue."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Stale rationale figures.",
          "recommendation": "Update.",
          "status": "resolved",
          "response": "Rationales state current figures 24/49 and 7/49."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Benchmark source field names only 2 of 4 reviews.",
          "recommendation": "Name all four.",
          "status": "resolved",
          "response": "Source field lists all four reviews with counts."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Result 26,473 vs assumed 10,000; term impact measured on earlier version; generic terms kept without tested alternative.",
          "recommendation": "Rerun term impact on current block; state evidence for kept generic terms; record decision if large result accepted.",
          "status": "accepted-risk",
          "response": "Term impact re-measured on current block: only 'weight gain'/covid* routes depend on a known record, none depend on generic terms alone. Large result (~26,500) accepted for recall and recorded in notes; reviewer may narrow distress, behavio*, stress."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Lifestyle synonyms not searched.",
          "recommendation": "Add and test.",
          "status": "resolved",
          "response": "Added and tested; no known record lost."
        },
        {
          "id": "F5",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Headings missing/undocumented.",
          "recommendation": "Add and document.",
          "status": "resolved",
          "response": "Added and documented."
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "Recall bound limits.",
          "recommendation": "Report with limits.",
          "status": "accepted-risk",
          "response": "Stated in notes and rationale."
        },
        {
          "id": "F7",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "Redundant variants.",
          "recommendation": "Optional.",
          "status": "accepted-risk",
          "response": "Kept; no effect."
        },
        {
          "id": "F8",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "Anchor record counts swapped in rationale.",
          "recommendation": "Correct to 32799105: 22, 32872154: 8.",
          "status": "resolved",
          "response": "Rationale corrected to 32872154: 8, 32799105: 22."
        },
        {
          "id": "F9",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "Protocol as_of null but edat bound applied.",
          "recommendation": "State cutoff in report.",
          "status": "resolved",
          "response": "edat cutoff documented in notes."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


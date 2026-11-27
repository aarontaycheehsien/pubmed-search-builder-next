# PubMed search strategy: audit

Generated 2026-11-27T06:40:37+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: yes (User unavailable; proceeded with defaults. No seeds, standard depth, no limits. Scope confirmation message relayed, continuing without waiting. Outcomes initially optional and measured. Benchmark from two prior-review reference lists only; the reviews' scopes (physical activity; child mental health) skew the benchmark. Recall is a lower bound on those scopes only; not independent of OpenAlex (unavailable, API budget exhausted). The [edat] bound to 2020-11-22 is the harness as-of date (not a protocol limit): the search is a snapshot as of 2020-11-22. PubMed only; OpenAlex unavailable (API budget exhausted).)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and lockdown measures | search | exposure; defines the topic, reliably named in title/abstract/MeSH |
| Lifestyle behaviors or well-being (outcomes) | search | AND-ed on evidence: union of lifestyle and well-being terms tested as optional against 20 independent known records from reference lists of 2 reviews (32872154: 8; 33207689: 12); 0 lost, 95% upper bound on loss 13.9%. Count without the block 157,987; with it 27,450 (v9). Unvalidated for diet, sleep, substance use, quality of life (benchmark skewed to physical activity and child mental health). Single-outcome blocks each lost records alone. Reversible by moving the block to optional. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T06:39:40+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 27,450
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"COVID-19"[Mesh]` | 57,100 | none |
| 2 | `"SARS-CoV-2"[Mesh]` | 45,940 | none |
| 3 | `"Pandemics"[Mesh]` | 50,286 | none |
| 4 | `"Quarantine"[Mesh]` | 3,938 | none |
| 5 | `covid*[tiab]` | 68,970 | none |
| 6 | `"corona virus disease"[tiab]` | 522 | none |
| 7 | `"coronavirus disease 2019"[tiab]` | 14,609 | none |
| 8 | `"coronavirus disease 19"[tiab]` | 776 | none |
| 9 | `coronavirus*[tiab]` | 43,051 | none |
| 10 | `"corona virus"[tiab]` | 1,299 | none |
| 11 | `"2019-nCoV"[tiab]` | 1,287 | none |
| 12 | `nCoV[tiab]` | 1,406 | none |
| 13 | `"SARS-CoV-2"[tiab]` | 23,501 | none |
| 14 | `"SARS-CoV2"[tiab]` | 1,050 | none |
| 15 | `"severe acute respiratory syndrome coronavirus 2"[tiab]` | 7,984 | none |
| 16 | `"novel coronavirus"[tiab]` | 6,186 | none |
| 17 | `pandemic*[tiab]` | 58,451 | none |
| 18 | `lockdown*[tiab]` | 3,419 | none |
| 19 | `"lock down"[tiab]` | 164 | none |
| 20 | `quarantin*[tiab]` | 6,954 | none |
| 21 | `"stay at home"[tiab]` | 815 | none |
| 22 | `"stay-at-home"[tiab]` | 815 | none |
| 23 | `"shelter in place"[tiab]` | 210 | none |
| 24 | `"home confinement"[tiab]` | 121 | none |
| 25 | `confinement[tiab]` | 20,191 | none |
| 26 | `"social distancing"[tiab]` | 2,657 | none |
| 27 | `"physical distancing"[tiab]` | 436 | none |
| 28 | `"self-isolation"[tiab]` | 289 | none |
| 29 | `"self isolation"[tiab]` | 289 | none |
| 30 | `"school closure*"[tiab]` | 442 | none |
| 31 | `"school closing*"[tiab]` | 31 | none |
| 32 | `"movement restriction*"[tiab]` | 568 | none |
| 33 | `"containment measure*"[tiab]` | 636 | none |
| 34 | `"public health measure*"[tiab]` | 2,597 | none |
| 35 | `"Physical Distancing"[Mesh]` | 579 | none |
| 36 | `curfew*[tiab]` | 170 | none |
| 37 | `"mobility restriction*"[tiab]` | 265 | none |
| 38 | `containment[tiab]` | 13,279 | none |
| 39 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 157,987 | none |
| 40 | `"Life Style"[Mesh]` | 99,996 | none |
| 41 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 42 | `"Exercise"[Mesh]` | 212,861 | none |
| 43 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 44 | `"Diet"[Mesh]` | 296,759 | none |
| 45 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 46 | `"Sleep"[Mesh]` | 85,170 | none |
| 47 | `"Smoking"[Mesh]` | 152,983 | none |
| 48 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 49 | `"Screen Time"[Mesh]` | 608 | none |
| 50 | `lifestyle*[tiab]` | 108,843 | none |
| 51 | `"life style"[tiab]` | 11,282 | none |
| 52 | `"health behavio*"[tiab]` | 25,773 | none |
| 53 | `"physical activit*"[tiab]` | 118,105 | none |
| 54 | `exercis*[tiab]` | 307,814 | none |
| 55 | `sedentar*[tiab]` | 33,158 | none |
| 56 | `"screen time"[tiab]` | 2,454 | none |
| 57 | `diet[tiab]` | 339,570 | none |
| 58 | `dietary[tiab]` | 260,594 | none |
| 59 | `eating[tiab]` | 77,768 | none |
| 60 | `nutrition*[tiab]` | 299,564 | none |
| 61 | `sleep*[tiab]` | 188,557 | none |
| 62 | `smoking[tiab]` | 228,898 | none |
| 63 | `alcohol[tiab]` | 263,050 | none |
| 64 | `"weight gain"[tiab]` | 63,432 | none |
| 65 | `"Mental Health"[Mesh]` | 44,674 | none |
| 66 | `"Psychological Distress"[Mesh]` | 4,500 | none |
| 67 | `"Quality of Life"[Mesh]` | 215,485 | none |
| 68 | `"Anxiety"[Mesh]` | 93,322 | none |
| 69 | `"Depression"[Mesh]` | 129,618 | none |
| 70 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 71 | `"Loneliness"[Mesh]` | 4,443 | none |
| 72 | `wellbeing[tiab]` | 91,509 | none |
| 73 | `"well-being"[tiab]` | 80,677 | none |
| 74 | `"mental health"[tiab]` | 159,660 | none |
| 75 | `"psychological"[tiab]` | 229,132 | none |
| 76 | `distress[tiab]` | 119,019 | none |
| 77 | `anxiety[tiab]` | 199,914 | none |
| 78 | `depress*[tiab]` | 474,404 | none |
| 79 | `stress[tiab]` | 779,124 | none |
| 80 | `"quality of life"[tiab]` | 282,519 | none |
| 81 | `loneliness[tiab]` | 6,825 | none |
| 82 | `"life satisfaction"[tiab]` | 8,061 | none |
| 83 | `"substance use"[tiab]` | 37,853 | none |
| 84 | `"drug use"[tiab]` | 46,742 | none |
| 85 | `cannabis[tiab]` | 18,505 | none |
| 86 | `vaping[tiab]` | 1,632 | none |
| 87 | `"e-cigarette*"[tiab]` | 4,975 | none |
| 88 | `drinking[tiab]` | 114,397 | none |
| 89 | `"Substance-Related Disorders"[Mesh]` | 291,305 | none |
| 90 | `inactivity[tiab]` | 15,458 | none |
| 91 | `sport*[tiab]` | 81,228 | none |
| 92 | `walking[tiab]` | 73,722 | none |
| 93 | `fitness[tiab]` | 77,700 | none |
| 94 | `obesity[tiab]` | 258,895 | none |
| 95 | `"body weight"[tiab]` | 211,537 | none |
| 96 | `tobacco[tiab]` | 104,255 | none |
| 97 | `cigarette*[tiab]` | 73,787 | none |
| 98 | `"substance abuse"[tiab]` | 25,726 | none |
| 99 | `addict*[tiab]` | 67,928 | none |
| 100 | `opioid*[tiab]` | 93,910 | none |
| 101 | `gambling[tiab]` | 7,878 | none |
| 102 | `mood[tiab]` | 76,261 | none |
| 103 | `emotion*[tiab]` | 205,757 | none |
| 104 | `suicid*[tiab]` | 80,380 | none |
| 105 | `resilience[tiab]` | 27,035 | none |
| 106 | `burnout[tiab]` | 13,018 | none |
| 107 | `"social media"[tiab]` | 13,598 | none |
| 108 | `"screen use"[tiab]` | 173 | none |
| 109 | `"internet use"[tiab]` | 2,812 | none |
| 110 | `gaming[tiab]` | 3,672 | none |
| 111 | `"Obesity"[Mesh]` | 228,277 | none |
| 112 | `"Suicide"[Mesh]` | 66,911 | none |
| 113 | `"Emotions"[Mesh]` | 353,591 | none |
| 114 | `"Social Isolation"[Mesh]` | 22,365 | none |
| 115 | `"Mental Disorders"[Mesh]` | 1,316,811 | none |
| 116 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 35,611 | none |
| 117 | `"Sleep Initiation and Maintenance Disorders"[Mesh]` | 14,522 | none |
| 118 | `insomnia[tiab]` | 22,051 | none |
| 119 | `PTSD[tiab]` | 25,928 | none |
| 120 | `post-traumatic[tiab]` | 31,780 | none |
| 121 | `"social isolation"[tiab]` | 7,931 | none |
| 122 | `"physical inactivity"[tiab]` | 8,195 | none |
| 123 | `#40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96 OR #97 OR #98 OR #99 OR #100 OR #101 OR #102 OR #103 OR #104 OR #105 OR #106 OR #107 OR #108 OR #109 OR #110 OR #111 OR #112 OR #113 OR #114 OR #115 OR #116 OR #117 OR #118 OR #119 OR #120 OR #121 OR #122` | 5,495,200 | none |
| 124 | `#39 AND #123` | 27,450 | none |

### Strategy (single line, for copying into PubMed)

```text
(("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR "Pandemics"[Mesh] OR "Quarantine"[Mesh] OR covid*[tiab] OR "corona virus disease"[tiab] OR "coronavirus disease 2019"[tiab] OR "coronavirus disease 19"[tiab] OR coronavirus*[tiab] OR "corona virus"[tiab] OR "2019-nCoV"[tiab] OR nCoV[tiab] OR "SARS-CoV-2"[tiab] OR "SARS-CoV2"[tiab] OR "severe acute respiratory syndrome coronavirus 2"[tiab] OR "novel coronavirus"[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR "lock down"[tiab] OR quarantin*[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "shelter in place"[tiab] OR "home confinement"[tiab] OR confinement[tiab] OR "social distancing"[tiab] OR "physical distancing"[tiab] OR "self-isolation"[tiab] OR "self isolation"[tiab] OR "school closure*"[tiab] OR "school closing*"[tiab] OR "movement restriction*"[tiab] OR "containment measure*"[tiab] OR "public health measure*"[tiab] OR "Physical Distancing"[Mesh] OR curfew*[tiab] OR "mobility restriction*"[tiab] OR containment[tiab]) AND ("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Sleep"[Mesh] OR "Smoking"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Screen Time"[Mesh] OR lifestyle*[tiab] OR "life style"[tiab] OR "health behavio*"[tiab] OR "physical activit*"[tiab] OR exercis*[tiab] OR sedentar*[tiab] OR "screen time"[tiab] OR diet[tiab] OR dietary[tiab] OR eating[tiab] OR nutrition*[tiab] OR sleep*[tiab] OR smoking[tiab] OR alcohol[tiab] OR "weight gain"[tiab] OR "Mental Health"[Mesh] OR "Psychological Distress"[Mesh] OR "Quality of Life"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR "Stress, Psychological"[Mesh] OR "Loneliness"[Mesh] OR wellbeing[tiab] OR "well-being"[tiab] OR "mental health"[tiab] OR "psychological"[tiab] OR distress[tiab] OR anxiety[tiab] OR depress*[tiab] OR stress[tiab] OR "quality of life"[tiab] OR loneliness[tiab] OR "life satisfaction"[tiab] OR "substance use"[tiab] OR "drug use"[tiab] OR cannabis[tiab] OR vaping[tiab] OR "e-cigarette*"[tiab] OR drinking[tiab] OR "Substance-Related Disorders"[Mesh] OR inactivity[tiab] OR sport*[tiab] OR walking[tiab] OR fitness[tiab] OR obesity[tiab] OR "body weight"[tiab] OR tobacco[tiab] OR cigarette*[tiab] OR "substance abuse"[tiab] OR addict*[tiab] OR opioid*[tiab] OR gambling[tiab] OR mood[tiab] OR emotion*[tiab] OR suicid*[tiab] OR resilience[tiab] OR burnout[tiab] OR "social media"[tiab] OR "screen use"[tiab] OR "internet use"[tiab] OR gaming[tiab] OR "Obesity"[Mesh] OR "Suicide"[Mesh] OR "Emotions"[Mesh] OR "Social Isolation"[Mesh] OR "Mental Disorders"[Mesh] OR "Stress Disorders, Post-Traumatic"[Mesh] OR "Sleep Initiation and Maintenance Disorders"[Mesh] OR insomnia[tiab] OR PTSD[tiab] OR post-traumatic[tiab] OR "social isolation"[tiab] OR "physical inactivity"[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 20 | 20 | 100.0% | 20 / 20 |

20 of the 20 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 86.1% (95% bound; it is as wide as the number of such records makes it).

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C2 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 0 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 49 | 49 | 8 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 37 | 37 | 0 |
| C7 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 12 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid | 5,495,200 | 0 |
| outcomes | 157,987 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 602,594 | initial | none | initial: covid block only searched; lifestyle/wellbeing optional |
| 2 | 124,269 | covid: +1 / -5 | none | dropped epidemic*, communicable disease control, social isolation, confinement, public health measure* as noisy; term impact |
| 3 | 105,909 | covid: +3 / -3 | none | restructure top3 generic covid terms with outcomes qualifier |
| 4 | 98,327 | covid: +6 / -6 | none | restructure: more generic covid terms narrowed with outcomes qualifier |
| 5 | 35,869 | covid: +12 / -10; outcomes: +43 / -0 | none | AND outcomes block on evidence (0/20 lost); un-restructured covid block restored with broader terms |
| 6 | 41,212 | covid: +3 / -0; outcomes: +7 / -0 | none | critic R1: added Physical Distancing MeSH, curfew, mobility restriction, substance use terms; term impact re-run |
| 7 | 19,920 | covid: +0 / -1; outcomes: +0 / -1 | none | dropped epidemic* (21k unique records, 0 known) and Substance-Related Disorders MeSH (2.9k unique, clinical, 0 known); recall unchanged |
| 8 | 24,205 | outcomes: +25 / -0 | none | critic R1: added outcome terms (inactivity, sport, obesity, tobacco, substance abuse, mood, suicid*, social media etc.), restored Substance-Related Disorders MeSH |
| 9 | 27,450 | covid: +1 / -0; outcomes: +9 / -0 | none | critic R1 v8: added containment, social isolation, mental disorders, PTSD, insomnia, physical inactivity |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 8: 7 findings; F1 should-fix open, F2 should-fix open, F3 should-fix open, F4 document open, F5 document open, F6 should-fix open, F7 document open
- Round 2 on version 9: 9 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix accepted-risk, F4 document resolved, F5 document resolved, F6 should-fix resolved, F7 document accepted-risk, F8 should-fix resolved, F9 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2561 NCBI requests logged (1141 from cache); strategy sha256 addedaabf479._

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
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Physical Distancing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "\"Sleep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:47",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Screen Time",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:48",
      "term": {
        "text": "\"Screen Time\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:64",
      "term": {
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:65",
      "term": {
        "text": "\"Psychological Distress\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:66",
      "term": {
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:67",
      "term": {
        "text": "\"Anxiety\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:68",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:69",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Loneliness",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:70",
      "term": {
        "text": "\"Loneliness\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Substance-Related Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019966",
          "name": "Substance-Related Disorders",
          "type": "descriptor",
          "scope_note": "Disorders related to substance use or abuse.",
          "tree_numbers": [
            "C25.775",
            "F03.900"
          ],
          "entry_terms": 38,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019966",
      "preferred_label": "Substance-Related Disorders",
      "type": "descriptor",
      "location": "vocabulary:88",
      "term": {
        "text": "\"Substance-Related Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Obesity",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:110",
      "term": {
        "text": "\"Obesity\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Suicide",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013405",
          "name": "Suicide",
          "type": "descriptor",
          "scope_note": "The act of killing oneself.",
          "tree_numbers": [
            "F01.145.126.980.875",
            "I01.880.735.856"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013405",
      "preferred_label": "Suicide",
      "type": "descriptor",
      "location": "vocabulary:111",
      "term": {
        "text": "\"Suicide\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Emotions",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:112",
      "term": {
        "text": "\"Emotions\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:113",
      "term": {
        "text": "\"Social Isolation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:114",
      "term": {
        "text": "\"Mental Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:115",
      "term": {
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep Initiation and Maintenance Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:39:40+00:00",
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
      "location": "vocabulary:116",
      "term": {
        "text": "\"Sleep Initiation and Maintenance Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"Pandemics\"[MeSH Terms] OR \"Quarantine\"[MeSH Terms] OR \"covid*\"[Title/Abstract] OR \"corona virus disease\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"coronavirus disease 19\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"corona virus\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"nCoV\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV2\"[Title/Abstract] OR \"severe acute respiratory syndrome coronavirus 2\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter in place\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"confinement\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"Physical Distancing\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract] OR \"school closure*\"[Title/Abstract] OR \"school closing*\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"containment measure*\"[Title/Abstract] OR \"public health measure*\"[Title/Abstract] OR \"Physical Distancing\"[MeSH Terms] OR \"curfew*\"[Title/Abstract] OR \"mobility restriction*\"[Title/Abstract] OR \"containment\"[Title/Abstract]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Screen Time\"[MeSH Terms] OR \"lifestyle*\"[Title/Abstract] OR \"Life Style\"[Title/Abstract] OR \"health behavio*\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentar*\"[Title/Abstract] OR \"Screen Time\"[Title/Abstract] OR \"Diet\"[Title/Abstract] OR \"dietary\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"sleep*\"[Title/Abstract] OR \"Smoking\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"weight gain\"[Title/Abstract] OR \"Mental Health\"[MeSH Terms] OR \"Psychological Distress\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Loneliness\"[MeSH Terms] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"psychological\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"Loneliness\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"drug use\"[Title/Abstract] OR \"cannabis\"[Title/Abstract] OR \"vaping\"[Title/Abstract] OR \"e cigarette*\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"Substance-Related Disorders\"[MeSH Terms] OR \"inactivity\"[Title/Abstract] OR \"sport*\"[Title/Abstract] OR \"walking\"[Title/Abstract] OR \"fitness\"[Title/Abstract] OR \"Obesity\"[Title/Abstract] OR \"body weight\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"cigarette*\"[Title/Abstract] OR \"substance abuse\"[Title/Abstract] OR \"addict*\"[Title/Abstract] OR \"opioid*\"[Title/Abstract] OR \"gambling\"[Title/Abstract] OR \"mood\"[Title/Abstract] OR \"emotion*\"[Title/Abstract] OR \"suicid*\"[Title/Abstract] OR \"resilience\"[Title/Abstract] OR \"burnout\"[Title/Abstract] OR \"social media\"[Title/Abstract] OR \"screen use\"[Title/Abstract] OR \"internet use\"[Title/Abstract] OR \"gaming\"[Title/Abstract] OR \"Obesity\"[MeSH Terms] OR \"Suicide\"[MeSH Terms] OR \"Emotions\"[MeSH Terms] OR \"Social Isolation\"[MeSH Terms] OR \"Mental Disorders\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"Sleep Initiation and Maintenance Disorders\"[MeSH Terms] OR \"insomnia\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"post-traumatic\"[Title/Abstract] OR \"Social Isolation\"[Title/Abstract] OR \"physical inactivity\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 8,
      "review_sha256": "320864152eecd6d3d54ae8643de6533867efcdac6b78c1d70e28c686f2b45bd9",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "containment bare term; missing well-being outcomes; stale rationale"
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within blocks, AND between; outcomes AND measured 0/20 lost"
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "missing Social Isolation, Mental Disorders, PTSD, insomnia headings"
        },
        "text_words": {
          "verdict": "revise",
          "note": "missing insomnia, PTSD, social isolation, physical inactivity; noisy confinement/pandemic*"
        },
        "syntax": {
          "verdict": "pass",
          "note": "valid; no warnings"
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "only harness edat snapshot bound"
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "bare 'containment' not searched",
          "recommendation": "add containment[tiab] tested",
          "status": "open",
          "response": "Addressing in v9: containment[tiab] added."
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "outcomes lack Social Isolation, Mental Disorders, PTSD, insomnia terms",
          "recommendation": "add",
          "status": "open",
          "response": "Addressing in v9: headings and text words added."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "confinement and pandemic* non-specific",
          "recommendation": "restrict or justify",
          "status": "open",
          "response": "Kept for sensitivity; both are AND-ed with the outcomes block so noise is bounded; documented."
        },
        {
          "id": "F4",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "scope",
          "finding": "Pandemics/Quarantine MeSH broad; no lower date bound",
          "recommendation": "document",
          "status": "open",
          "response": "Documented; no lower date bound added to keep recall-first."
        },
        {
          "id": "F5",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "snapshot date, PubMed only",
          "recommendation": "report",
          "status": "open",
          "response": "Reported in notes and narrative."
        },
        {
          "id": "F6",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "stale rationale; AND unvalidated for diet/sleep etc.",
          "recommendation": "update",
          "status": "open",
          "response": "Rationale rewritten with current counts; risk stated."
        },
        {
          "id": "F7",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "duplicate variants",
          "recommendation": "none",
          "status": "open",
          "response": "Harmless; retained."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 9,
      "review_sha256": "a46554b6fca910bcb36b1fba4475a06036009ec6b51999633cf0d2baba098100",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All named concepts covered by bare names; no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within, AND between; outcomes AND measured 0/20 lost, 95% loss bound 13.9%; residual risks documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Added headings present; broad Pandemics/Quarantine documented."
        },
        "text_words": {
          "verdict": "pass",
          "note": "F1/F2 text words added; noisy terms retained deliberately and bounded by the AND."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Lint empty; no warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only the harness edat snapshot bound; PubMed only, documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Bare 'containment' not searched.",
          "recommendation": "see response",
          "status": "resolved",
          "response": "containment[tiab] is in the covid block of v9."
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Outcomes lacked social isolation, mental disorders, PTSD, insomnia terms.",
          "recommendation": "see response",
          "status": "resolved",
          "response": "Headings and text words added in v9."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "confinement and pandemic* non-specific.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Kept for recall; AND-ed with the outcomes block; no known record lost; residual noise left to screening."
        },
        {
          "id": "F4",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "scope",
          "finding": "Pandemics and Quarantine MeSH broad, no lower date bound.",
          "recommendation": "see response",
          "status": "resolved",
          "response": "Documented as a recall-first choice."
        },
        {
          "id": "F5",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "Dated snapshot, PubMed only.",
          "recommendation": "see response",
          "status": "resolved",
          "response": "Reported in protocol notes."
        },
        {
          "id": "F6",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Stale rationale; AND unvalidated for diet/sleep etc.",
          "recommendation": "see response",
          "status": "resolved",
          "response": "Rationale updated with v9 counts and stated risk."
        },
        {
          "id": "F7",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "Duplicate term variants.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Harmless; retained."
        },
        {
          "id": "F8",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Rationale claim that single-outcome blocks each lost records lacks measurement in packet.",
          "recommendation": "see response",
          "status": "resolved",
          "response": "Measured in earlier evaluations of this workspace: lifestyle-only AND lost 11 of 20 known records and well-being-only lost 6 of 8 (psb eval optional_blocks, versions 4-5); only the union lost none. Not in the packet, but recorded in eval history."
        },
        {
          "id": "F9",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "Recall evidence is 20 records skewed to two topics, 2020 only; term impact measured on an earlier version.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Recall reported as a lower bound on this benchmark only; fallback is moving outcomes to optional. Term impact on v9 not re-run; result 27,450 is judged screenable for a COVID-era review at this scale."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


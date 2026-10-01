# PubMed search strategy: audit

Generated 2026-10-01T11:59:13+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without clarification; scope roles and eligibility were operationalized from the question alone. No seed articles, population, language, geography, study design, or publication-date limits were supplied. PSB_AS_OF=2020-11-22 is the Entrez-date cutoff; no [dp] limit is used. The outcome concept is tested as one optional OR block because records may examine lifestyle behavior or well-being without naming both.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The exposure is central to the question and is likely named in titles, abstracts, or MeSH; category probe will assess records described only through measures such as lockdown or quarantine. |
| Lifestyle behaviors and well-being outcomes | optional | These are topic-defining and often searchable outcomes, but requiring them may miss studies with outcome labels absent from titles/abstracts; test one broad OR block before deciding. |
| Population and subgroup | screen | No population is specified, and age, geography, or other subgroup restrictions are not required by the question. |
| Study design | screen | The question does not specify a design; screen designs for eligibility. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:57:40+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 16,925
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,931 | none |
| 3 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 4 | `Pandemics[Mesh]` | 50,277 | none |
| 5 | `Quarantine[Mesh]` | 3,936 | none |
| 6 | `Disease Outbreaks[Mesh]` | 144,124 | none |
| 7 | `COVID-19[tiab]` | 67,388 | none |
| 8 | `COVID19[tiab]` | 64,206 | none |
| 9 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 10 | `SARS CoV 2[tiab]` | 23,503 | none |
| 11 | `2019-nCoV[tiab]` | 1,288 | none |
| 12 | `2019 novel coronavirus[tiab]` | 1,176 | none |
| 13 | `novel coronavirus[tiab]` | 6,179 | none |
| 14 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 15 | `coronavirus disease-19[tiab]` | 777 | none |
| 16 | `COVID-19 pandemic[tiab]` | 20,381 | none |
| 17 | `coronavirus pandemic[tiab]` | 1,011 | none |
| 18 | `coronavirus outbreak[tiab]` | 337 | none |
| 19 | `lockdown*[tiab]` | 3,416 | none |
| 20 | `quarantine*[tiab]` | 6,745 | none |
| 21 | `self-quarantine[tiab]` | 92 | none |
| 22 | `self isolation[tiab]` | 289 | none |
| 23 | `self-isolation[tiab]` | 289 | none |
| 24 | `social distancing[tiab]` | 2,657 | none |
| 25 | `physical distancing[tiab]` | 436 | none |
| 26 | `stay-at-home[tiab]` | 815 | none |
| 27 | `stay at home[tiab]` | 815 | none |
| 28 | `home confinement[tiab]` | 121 | none |
| 29 | `movement restriction*[tiab]` | 568 | none |
| 30 | `mobility restriction*[tiab]` | 265 | none |
| 31 | `containment measure*[tiab]` | 636 | none |
| 32 | `isolation measure*[tiab]` | 332 | none |
| 33 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32` | 191,637 | none |
| 34 | `Life Style[Mesh]` | 99,996 | none |
| 35 | `Healthy Lifestyle[Mesh]` | 8,656 | none |
| 36 | `Health Behavior[Mesh]` | 333,508 | none |
| 37 | `Exercise[Mesh]` | 212,859 | none |
| 38 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 39 | `Sleep[Mesh]` | 85,169 | none |
| 40 | `Sleep Wake Disorders[Mesh]` | 96,238 | none |
| 41 | `Diet[Mesh]` | 296,758 | none |
| 42 | `Feeding Behavior[Mesh]` | 178,421 | none |
| 43 | `Mental Health[Mesh]` | 44,674 | none |
| 44 | `Psychological Distress[Mesh]` | 4,500 | none |
| 45 | `Anxiety[Mesh]` | 93,320 | none |
| 46 | `Depression[Mesh]` | 230,067 | none |
| 47 | `Stress, Psychological[Mesh]` | 139,617 | none |
| 48 | `Quality of Life[Mesh]` | 215,482 | none |
| 49 | `Emotions[Mesh]` | 353,589 | none |
| 50 | `lifestyle*[tiab]` | 108,849 | none |
| 51 | `health behavior*[tiab]` | 18,620 | none |
| 52 | `health behaviour*[tiab]` | 7,323 | none |
| 53 | `physical activit*[tiab]` | 118,111 | none |
| 54 | `exercise[tiab]` | 272,207 | none |
| 55 | `movement behavio*[tiab]` | 1,286 | none |
| 56 | `play behavio*[tiab]` | 793 | none |
| 57 | `sedentary behavio*[tiab]` | 7,188 | none |
| 58 | `sedentary time[tiab]` | 2,607 | none |
| 59 | `screen time[tiab]` | 2,454 | none |
| 60 | `sleep[tiab]` | 171,185 | none |
| 61 | `insomnia[tiab]` | 22,051 | none |
| 62 | `sleep quality[tiab]` | 15,610 | none |
| 63 | `sleep duration[tiab]` | 8,298 | none |
| 64 | `diet*[tiab]` | 587,723 | none |
| 65 | `eating behavio*[tiab]` | 10,745 | none |
| 66 | `food intake[tiab]` | 45,992 | none |
| 67 | `alcohol consum*[tiab]` | 44,699 | none |
| 68 | `substance use[tiab]` | 37,851 | none |
| 69 | `mental health[tiab]` | 159,665 | none |
| 70 | `psychological well-being[tiab]` | 9,542 | none |
| 71 | `psychological wellbeing[tiab]` | 1,436 | none |
| 72 | `well-being[tiab]` | 80,676 | none |
| 73 | `wellbeing[tiab]` | 91,505 | none |
| 74 | `emotional well-being[tiab]` | 4,383 | none |
| 75 | `psychological distress[tiab]` | 20,154 | none |
| 76 | `distress[tiab]` | 119,022 | none |
| 77 | `anxiety[tiab]` | 199,917 | none |
| 78 | `depress*[tiab]` | 474,400 | none |
| 79 | `stress[tiab]` | 779,146 | none |
| 80 | `loneliness[tiab]` | 6,825 | none |
| 81 | `quality of life[tiab]` | 282,526 | none |
| 82 | `life satisfaction[tiab]` | 8,062 | none |
| 83 | `emotions[tiab]` | 34,392 | none |
| 84 | `#34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83` | 3,561,017 | none |
| 85 | `#33 AND #84` | 16,925 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR Coronavirus Infections[Mesh] OR Pandemics[Mesh] OR Quarantine[Mesh] OR Disease Outbreaks[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR 2019-nCoV[tiab] OR 2019 novel coronavirus[tiab] OR novel coronavirus[tiab] OR coronavirus disease 2019[tiab] OR coronavirus disease-19[tiab] OR COVID-19 pandemic[tiab] OR coronavirus pandemic[tiab] OR coronavirus outbreak[tiab] OR lockdown*[tiab] OR quarantine*[tiab] OR self-quarantine[tiab] OR self isolation[tiab] OR self-isolation[tiab] OR social distancing[tiab] OR physical distancing[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR home confinement[tiab] OR movement restriction*[tiab] OR mobility restriction*[tiab] OR containment measure*[tiab] OR isolation measure*[tiab]) AND (Life Style[Mesh] OR Healthy Lifestyle[Mesh] OR Health Behavior[Mesh] OR Exercise[Mesh] OR Sedentary Behavior[Mesh] OR Sleep[Mesh] OR Sleep Wake Disorders[Mesh] OR Diet[Mesh] OR Feeding Behavior[Mesh] OR Mental Health[Mesh] OR Psychological Distress[Mesh] OR Anxiety[Mesh] OR Depression[Mesh] OR Stress, Psychological[Mesh] OR Quality of Life[Mesh] OR Emotions[Mesh] OR lifestyle*[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR physical activit*[tiab] OR exercise[tiab] OR movement behavio*[tiab] OR play behavio*[tiab] OR sedentary behavio*[tiab] OR sedentary time[tiab] OR screen time[tiab] OR sleep[tiab] OR insomnia[tiab] OR sleep quality[tiab] OR sleep duration[tiab] OR diet*[tiab] OR eating behavio*[tiab] OR food intake[tiab] OR alcohol consum*[tiab] OR substance use[tiab] OR mental health[tiab] OR psychological well-being[tiab] OR psychological wellbeing[tiab] OR well-being[tiab] OR wellbeing[tiab] OR emotional well-being[tiab] OR psychological distress[tiab] OR distress[tiab] OR anxiety[tiab] OR depress*[tiab] OR stress[tiab] OR loneliness[tiab] OR quality of life[tiab] OR life satisfaction[tiab] OR emotions[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 19 | 19 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being outcomes | AND-ed | 191,637 / 16,925 | 91.2% | none | 0/30 (up to 10% of removed records could be relevant) | The block retained all 19 screened development records (meeting the 15-record threshold), and the 30-record random loss sample contained no eligible lifestyle or well-being study. It cuts the exposure-only count by 91.2%; the remaining count still exceeds the default workload budget and is documented for review. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| COVID-19 pandemic and related lockdown measures | 1 | `(corona virus[tiab] OR 2019 novel coronavirus infection[tiab] OR novel coronavirus pneumonia[tiab] OR COVID*[tiab] OR SARS 2[tiab] OR lockdown*[tiab] OR school closure[tiab] OR stay home order[tiab] OR shelter in place[tiab] OR curfew*[tiab] OR confinement[tiab] OR social restriction[tiab] OR community restriction[tiab] OR movement control[tiab] OR public health measure[tiab])` | 3,730 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| pandemic_measures | 3,561,017 | 0 |
| lifestyle_wellbeing | 191,637 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 191,637 | initial | none | Initial recall-first COVID-19 exposure block with a broad lifestyle and well-being optional candidate; terms cover categories reflected in 19 screened original-study abstracts. |
| 2 | 16,925 | lifestyle_wellbeing: +50 / -0 | none | AND the tested broad lifestyle/well-being candidate after all 19 relevant known records were retained and no eligible study was found in the 30-record loss sample. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1050 NCBI requests logged (392 from cache); strategy sha256 a1bfe15ed4c9._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "over_workload_budget",
        "message": "16,925 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "16,925 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
        "text": "COVID-19",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "SARS-CoV-2",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
        "text": "SARS-CoV-2",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D018352",
          "name": "Coronavirus Infections",
          "type": "descriptor",
          "scope_note": "Virus diseases caused by the CORONAVIRUS genus. Some specifics include transmissible enteritis of turkeys (ENTERITIS, TRANSMISSIBLE, OF TURKEYS); FELINE INFECTIOUS PERITONITIS; and transmissible gastroenteritis of swine (GASTROENTERITIS, TRANSMISSIBLE, OF SWINE).",
          "tree_numbers": [
            "C01.925.782.600.550.200"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D018352",
      "preferred_label": "Coronavirus Infections",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Coronavirus Infections",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "Pandemics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "Quarantine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Disease Outbreaks",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004196",
          "name": "Disease Outbreaks",
          "type": "descriptor",
          "scope_note": "Sudden increase in the incidence of a disease. The concept includes EPIDEMICS and PANDEMICS.",
          "tree_numbers": [
            "N06.850.290"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004196",
      "preferred_label": "Disease Outbreaks",
      "type": "descriptor",
      "location": "vocabulary:6",
      "term": {
        "text": "Disease Outbreaks",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Life Style",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Healthy Lifestyle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000070497",
          "name": "Healthy Lifestyle",
          "type": "descriptor",
          "scope_note": "A pattern of behavior involving LIFE STYLE choices which ensure optimum health. Examples are eating right; maintaining physical, emotional, and spiritual wellness, and taking preemptive steps against communicable diseases.",
          "tree_numbers": [
            "F01.829.458.205"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000070497",
      "preferred_label": "Healthy Lifestyle",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "Healthy Lifestyle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Health Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Sedentary Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
        "text": "Sleep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep Wake Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012893",
          "name": "Sleep Wake Disorders",
          "type": "descriptor",
          "scope_note": "Abnormal sleep-wake schedule or pattern associated with the CIRCADIAN RHYTHM which affect the length, timing, and/or rigidity of the sleep-wake cycle relative to the day-night cycle.",
          "tree_numbers": [
            "C10.886",
            "C23.888.592.796",
            "F03.870"
          ],
          "entry_terms": 37,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012893",
      "preferred_label": "Sleep Wake Disorders",
      "type": "descriptor",
      "location": "vocabulary:39",
      "term": {
        "text": "Sleep Wake Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "Psychological Distress",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "Stress, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:47",
      "term": {
        "text": "Quality of Life",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Emotions",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:40+00:00",
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
      "location": "vocabulary:48",
      "term": {
        "text": "Emotions",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"pandemics\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"disease outbreaks\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"coronavirus disease 19\"[Title/Abstract] OR \"covid 19 pandemic\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract] OR \"coronavirus outbreak\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"self-quarantine\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"physical distancing\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"mobility restriction*\"[Title/Abstract] OR \"containment measure*\"[Title/Abstract] OR \"isolation measure*\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"healthy lifestyle\"[MeSH Terms] OR \"health behavior\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"sleep wake disorders\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"psychological distress\"[MeSH Terms] OR \"anxiety\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"stress, psychological\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR \"emotions\"[MeSH Terms] OR \"lifestyle*\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"movement behavio*\"[Title/Abstract] OR \"play behavio*\"[Title/Abstract] OR \"sedentary behavio*\"[Title/Abstract] OR \"sedentary time\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"insomnia\"[Title/Abstract] OR \"sleep quality\"[Title/Abstract] OR \"sleep duration\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating behavio*\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"alcohol consum*\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"psychological well being\"[Title/Abstract] OR \"psychological wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"emotional well being\"[Title/Abstract] OR \"psychological distress\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"anxiety\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"emotions\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "526ec786a7fe7f9f37696796372a54adc2c75fd0b4614ba05b06abf36c08bab3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Each named behavior or well-being member has corresponding MeSH and/or title/abstract vocabulary; all 19 known development records were retrieved."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms and outcome terms are OR-ed within blocks, and the two concepts are AND-ed after optional testing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Live validation verified the MeSH headings with no vocabulary issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include COVID-19 and lockdown-measure terminology and the named lifestyle and well-being outcomes; the category probe screened 30 outside records and found none eligible."
        },
        "syntax": {
          "verdict": "pass",
          "note": "PubMed translation returned no syntax errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date cutoff is required by the task instructions to model PubMed as of 2020-11-22 and exclude later-added records. The generated query applies [edat], not [dp]."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits records to those entered in PubMed by 2020-11-22. The scope notes say no publication-date limits were supplied, and the question does not specify this retrieval cutoff.",
          "recommendation": "Remove the Entrez date-of-entry limit, or document and confirm that the review is intentionally restricted to records entered by 2020-11-22; then rerun the complete evaluation.",
          "status": "rejected",
          "response": "The task explicitly instructs us to work as if the date were 2020-11-22, exclude literature added to PubMed after that date, and keep PSB_AS_OF set for every command. This mandates an Entrez date-of-entry bound; it is not an added publication-date limit. The generated syntax uses [edat] and contains no [dp] limit. The protocol records the same as_of date."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional outcome block was tested and legitimately AND-ed. All 19 known development records were retained, the 30-record loss sample contained no eligible record, and the reduction was material. The remaining 16,925-record set exceeds the standard workload budget and is reported as a screening burden for the review team.",
          "evidence": "PSB evaluation reports 19/19 relevant records retrieved, 0 relevant among 30 sampled records removed by the outcome block, a 91.2% reduction from 191,637 to 16,925 records, with the default budget at 10,000."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-28T14:20:19+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO (pandemic/lockdown exposure; outcomes tested as optional)
- Scope confirmed by user: no (User asked to proceed without clarification. Scope assumptions: general human populations, all study designs at search stage, English and other languages without restriction; assess pandemic/restriction-related changes in the listed lifestyle or well-being outcomes. No known relevant articles were supplied. Entrez date cutoff is 2020-11-22 via PSB_AS_OF and protocol as_of; do not use a publication-date limit. No user scope confirmation was possible. A PubMed systematic-review pilot identified reviews on physical activity and quarantine/social consequences, but the abstracted physical-activity overview stated that no studies had examined home physical activity during COVID-19 isolation, and no matching included-study benchmark was assembled. A precise primary-study pilot yielded nine abstract-screened development records; a separate Google Trends query-volume study was not counted as a direct behavior outcome. Proximity review for the final strategy: PubMed returned each clause with its explicit [tiab:~1] or [tiab:~2] operator and no translation issues. The stay-at-home, social-distancing, shelter-in-place, home-confinement, screen-use, and use-of-screens clauses use ~1; food-intake, screen-time, and substance-use use ~2; health-behavior, physical-activity, and eating-behavior variants use ~1. These settings allow either word order and up to the stated number of intervening words. This is acceptable because each pair names a concept whose wording may vary in order; no exact phrase order is required. Counts and current translations are recorded per clause in the current evaluation and final audit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related restrictions | search | The COVID-19 pandemic defines the exposure and is required. Search COVID-19/SARS-CoV-2 headings and text, plus Quarantine MeSH and named quarantine, lockdown, distancing, stay-at-home, shelter-in-place, movement-restriction, and confinement terms. Generic pandemic-only wording was excluded after it admitted unrelated outbreaks. |
| Lifestyle behaviors and well-being | optional | Topic-defining outcomes are often named but are inconsistently reported; test a broad outcome block empirically before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T14:18:56+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 15,792
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 3 | `COVID-19[tiab]` | 67,388 | none |
| 4 | `COVID19[tiab]` | 64,206 | none |
| 5 | `"COVID 19"[tiab]` | 67,388 | none |
| 6 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 7 | `SARS CoV 2[tiab]` | 23,503 | none |
| 8 | `2019-nCoV[tiab]` | 1,288 | none |
| 9 | `2019nCoV[tiab]` | 926 | none |
| 10 | `"novel coronavirus"[tiab]` | 6,179 | none |
| 11 | `"coronavirus disease 2019"[tiab]` | 14,613 | none |
| 12 | `lockdown*[tiab]` | 3,416 | none |
| 13 | `"stay at home"[tiab:~1]` | 869 | none |
| 14 | `"social distancing"[tiab:~1]` | 2,679 | none |
| 15 | `"shelter in place"[tiab:~1]` | 212 | none |
| 16 | `"movement restriction*"[tiab]` | 568 | none |
| 17 | `confinement[tiab]` | 20,190 | none |
| 18 | `"home confinement"[tiab:~1]` | 138 | none |
| 19 | `Quarantine[Mesh]` | 3,936 | none |
| 20 | `quarantin*[tiab]` | 6,954 | none |
| 21 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 115,041 | none |
| 22 | `Life Style[Mesh]` | 99,996 | none |
| 23 | `Healthy Lifestyle[Mesh]` | 8,656 | none |
| 24 | `Exercise[Mesh]` | 212,859 | none |
| 25 | `Motor Activity[Mesh]` | 309,966 | none |
| 26 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 27 | `Feeding Behavior[Mesh]` | 178,421 | none |
| 28 | `Food Preferences[Mesh]` | 15,161 | none |
| 29 | `Mental Health[Mesh]` | 44,674 | none |
| 30 | `Quality of Life[Mesh]` | 215,482 | none |
| 31 | `Social Isolation[Mesh]` | 22,365 | none |
| 32 | `Smoking[Mesh]` | 152,983 | none |
| 33 | `Tobacco Use[Mesh]` | 6,633 | none |
| 34 | `Alcohol Drinking[Mesh]` | 72,506 | none |
| 35 | `lifestyle*[tiab]` | 108,849 | none |
| 36 | `"life style"[tiab]` | 11,282 | none |
| 37 | `exercis*[tiab]` | 307,827 | none |
| 38 | `sedentary[tiab]` | 32,472 | none |
| 39 | `sitting[tiab]` | 23,133 | none |
| 40 | `diet*[tiab]` | 587,723 | none |
| 41 | `"food intake"[tiab:~2]` | 52,298 | none |
| 42 | `nutrition*[tiab]` | 299,576 | none |
| 43 | `sleep*[tiab]` | 188,562 | none |
| 44 | `"screen time"[tiab:~2]` | 3,109 | none |
| 45 | `smoking[tiab]` | 228,902 | none |
| 46 | `tobacco[tiab]` | 104,259 | none |
| 47 | `alcohol[tiab]` | 263,050 | none |
| 48 | `"substance use"[tiab:~2]` | 38,871 | none |
| 49 | `wellbeing[tiab]` | 91,505 | none |
| 50 | `"well-being"[tiab]` | 80,676 | none |
| 51 | `"well being"[tiab]` | 80,676 | none |
| 52 | `"mental health"[tiab]` | 159,665 | none |
| 53 | `psychological[tiab]` | 229,134 | none |
| 54 | `anxiety[tiab]` | 199,917 | none |
| 55 | `depression[tiab]` | 348,632 | none |
| 56 | `stress[tiab]` | 779,146 | none |
| 57 | `distress[tiab]` | 119,022 | none |
| 58 | `"quality of life"[tiab]` | 282,526 | none |
| 59 | `loneliness[tiab]` | 6,825 | none |
| 60 | `"life satisfaction"[tiab]` | 8,062 | none |
| 61 | `"health behavior"[tiab:~1]` | 13,664 | none |
| 62 | `"health behaviors"[tiab:~1]` | 16,516 | none |
| 63 | `"health behaviour"[tiab:~1]` | 7,104 | none |
| 64 | `"health behaviours"[tiab:~1]` | 5,542 | none |
| 65 | `"physical activity"[tiab:~1]` | 115,542 | none |
| 66 | `"physical activities"[tiab:~1]` | 7,601 | none |
| 67 | `"eating behavior"[tiab:~1]` | 5,556 | none |
| 68 | `"eating behaviors"[tiab:~1]` | 4,050 | none |
| 69 | `"eating behaviour"[tiab:~1]` | 2,167 | none |
| 70 | `"eating behaviours"[tiab:~1]` | 1,325 | none |
| 71 | `insomnia[tiab]` | 22,051 | none |
| 72 | `"Anxiety"[Mesh]` | 93,320 | none |
| 73 | `"Depression"[Mesh]` | 129,618 | none |
| 74 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 75 | `"Sleep Initiation and Maintenance Disorders"[Mesh]` | 14,522 | none |
| 76 | `"screen use"[tiab:~1]` | 611 | none |
| 77 | `"use of screens"[tiab:~1]` | 158 | none |
| 78 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77` | 3,839,121 | none |
| 79 | `#21 AND #78` | 15,792 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR Coronavirus Infections[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR "COVID 19"[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR 2019-nCoV[tiab] OR 2019nCoV[tiab] OR "novel coronavirus"[tiab] OR "coronavirus disease 2019"[tiab] OR lockdown*[tiab] OR "stay at home"[tiab:~1] OR "social distancing"[tiab:~1] OR "shelter in place"[tiab:~1] OR "movement restriction*"[tiab] OR confinement[tiab] OR "home confinement"[tiab:~1] OR Quarantine[Mesh] OR quarantin*[tiab]) AND (Life Style[Mesh] OR Healthy Lifestyle[Mesh] OR Exercise[Mesh] OR Motor Activity[Mesh] OR Sedentary Behavior[Mesh] OR Feeding Behavior[Mesh] OR Food Preferences[Mesh] OR Mental Health[Mesh] OR Quality of Life[Mesh] OR Social Isolation[Mesh] OR Smoking[Mesh] OR Tobacco Use[Mesh] OR Alcohol Drinking[Mesh] OR lifestyle*[tiab] OR "life style"[tiab] OR exercis*[tiab] OR sedentary[tiab] OR sitting[tiab] OR diet*[tiab] OR "food intake"[tiab:~2] OR nutrition*[tiab] OR sleep*[tiab] OR "screen time"[tiab:~2] OR smoking[tiab] OR tobacco[tiab] OR alcohol[tiab] OR "substance use"[tiab:~2] OR wellbeing[tiab] OR "well-being"[tiab] OR "well being"[tiab] OR "mental health"[tiab] OR psychological[tiab] OR anxiety[tiab] OR depression[tiab] OR stress[tiab] OR distress[tiab] OR "quality of life"[tiab] OR loneliness[tiab] OR "life satisfaction"[tiab] OR "health behavior"[tiab:~1] OR "health behaviors"[tiab:~1] OR "health behaviour"[tiab:~1] OR "health behaviours"[tiab:~1] OR "physical activity"[tiab:~1] OR "physical activities"[tiab:~1] OR "eating behavior"[tiab:~1] OR "eating behaviors"[tiab:~1] OR "eating behaviour"[tiab:~1] OR "eating behaviours"[tiab:~1] OR insomnia[tiab] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR "Stress, Psychological"[Mesh] OR "Sleep Initiation and Maintenance Disorders"[Mesh] OR "screen use"[tiab:~1] OR "use of screens"[tiab:~1])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being | AND-ed | 115,041 / 15,792 | 86.3% | none | 0/30 (up to 10% of removed records could be relevant) | After adding the explicit screen-use and quarantine wording requested by the critic, the refreshed outcome-block test reduced the exposure-only count by 86.3% (115,041 to 15,792), lost none of the nine development records, and found no eligible study in the refreshed 30-record loss sample. Keep the block AND-ed; the final count remains above budget and outcome-label omissions remain a recall risk. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_context | 3,839,121 | 0 |
| lifestyle_wellbeing | 115,041 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad COVID-19 exposure block; outcome block is optional and will be tested because outcomes are variably named. No known articles were supplied. |
| 2 | 120,410 | limits/combination | none | Initial broad COVID-19 exposure block; outcome block is optional and will be tested because outcomes are variably named. No known articles were supplied. |
| 3 | 109,291 | covid_context: +2 / -3 | none | Added confinement terminology and vocabulary observed in the screened relevant set; narrowed non-COVID-specific exposure alternatives that inflated retrieval while retaining COVID and SARS-CoV-2 MeSH/text coverage. |
| 4 | 15,360 | lifestyle_wellbeing: +54 / -0 | none | Moved the tested lifestyle/well-being optional block into the query based on 85.9% reduction, zero development-record loss, and a 0/30 eligible loss sample. |
| 5 | 15,792 | covid_context: +2 / -0; lifestyle_wellbeing: +2 / -0 | none | Addressed critic wording gaps by searching screen use and quarantine as explicit members of the eligibility scope; rerun the complete evaluation and check retrieval before deciding final terms. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 3 findings; P1-01 must-fix open, P1-02 should-fix open, P1-03 should-fix open
- Round 2 on version 5: 3 findings; P1-01 must-fix resolved, P1-02 should-fix resolved, P1-03 should-fix open
- Round 3 on version 5: 3 findings; P1-01 must-fix resolved, P1-02 should-fix resolved, P1-03 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1802 NCBI requests logged (972 from cache); strategy sha256 ad3b91e5dd1c._

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
        "message": "15,792 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "15,792 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Coronavirus Infections",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "Quarantine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Life Style",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Healthy Lifestyle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "Healthy Lifestyle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "Motor Activity",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Sedentary Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005518",
          "name": "Food Preferences",
          "type": "descriptor",
          "scope_note": "The selection of one food over another.",
          "tree_numbers": [
            "F01.145.407.516",
            "G07.203.650.353.516"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005518",
      "preferred_label": "Food Preferences",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "Food Preferences",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Quality of Life",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Social Isolation",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "Smoking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Tobacco Use",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D064424",
          "name": "Tobacco Use",
          "type": "descriptor",
          "scope_note": "Use of TOBACCO (Nicotiana tabacum L) and TOBACCO PRODUCTS.",
          "tree_numbers": [
            "F01.145.958"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D064424",
      "preferred_label": "Tobacco Use",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "Tobacco Use",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Alcohol Drinking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:71",
      "term": {
        "text": "\"Anxiety\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:72",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:73",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep Initiation and Maintenance Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:18:56+00:00",
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
      "location": "vocabulary:74",
      "term": {
        "text": "\"Sleep Initiation and Maintenance Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"covid 19\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"covid 19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"covid 19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019nCoV\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"stay at home\"[Title/Abstract:~1] OR \"social distancing\"[Title/Abstract:~1] OR \"shelter in place\"[Title/Abstract:~1] OR \"movement restriction*\"[Title/Abstract] OR \"confinement\"[Title/Abstract] OR \"home confinement\"[Title/Abstract:~1] OR \"quarantine\"[MeSH Terms] OR \"quarantin*\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"healthy lifestyle\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"motor activity\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"food preferences\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR \"social isolation\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"tobacco use\"[MeSH Terms] OR \"alcohol drinking\"[MeSH Terms] OR \"lifestyle*\"[Title/Abstract] OR \"life style\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"food intake\"[Title/Abstract:~2] OR \"nutrition*\"[Title/Abstract] OR \"sleep*\"[Title/Abstract] OR \"screen time\"[Title/Abstract:~2] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"substance use\"[Title/Abstract:~2] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"psychological\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"Depression\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"health behavior\"[Title/Abstract:~1] OR \"health behaviors\"[Title/Abstract:~1] OR \"health behaviour\"[Title/Abstract:~1] OR \"health behaviours\"[Title/Abstract:~1] OR \"physical activity\"[Title/Abstract:~1] OR \"physical activities\"[Title/Abstract:~1] OR \"eating behavior\"[Title/Abstract:~1] OR \"eating behaviors\"[Title/Abstract:~1] OR \"eating behaviour\"[Title/Abstract:~1] OR \"eating behaviours\"[Title/Abstract:~1] OR \"insomnia\"[Title/Abstract] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Sleep Initiation and Maintenance Disorders\"[MeSH Terms] OR \"screen use\"[Title/Abstract:~1] OR \"use of screens\"[Title/Abstract:~1]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "595ee80058faa8c3b800698a012f06f8e0e6563d4750c5a5d2ee857a352132a6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues or PubMed syntax errors. The displayed translations retain the intended fields and concepts."
        },
        "operators": {
          "verdict": "pass",
          "note": "The COVID and outcome terms are ORed within their blocks, and the two blocks are ANDed. The optional outcome block was tested and its workload tradeoff is documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH descriptors for the selected headings; the final query uses them in the MeSH field."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Eligibility explicitly includes screen use, but the text-word block has only screen time. The scope rationale also names quarantine terminology, but the exposure block has no quarantine term."
        },
        "syntax": {
          "verdict": "revise",
          "note": "The query has no reported syntax errors, but the packet does not provide clause-specific interpretation review for its proximity expressions. Those expressions allow words in either order, so their retrieval meaning should be reviewed and documented."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The query uses the stated Entrez date-entry cutoff of 2020-11-22 and no publication-date, language, design, or population filter."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "Eligibility names screen use, but the outcome block includes only screen time[tiab:~2]. That narrower expression does not cover the named outcome by its own bare wording.",
          "recommendation": "Add and test an explicit screen-use expression, such as screen use[tiab], and reassess the complete strategy and its known-record retrieval.",
          "status": "open",
          "response": ""
        },
        {
          "id": "P1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The exposure rationale calls for quarantine terminology, but the block has no quarantine term. Confinement and distancing terms do not explicitly cover that named restriction concept.",
          "recommendation": "Add and test a quarantine term such as quarantin*[tiab], then reassess the complete strategy and its known-record retrieval.",
          "status": "open",
          "response": ""
        },
        {
          "id": "P1-03",
          "domain": "syntax",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome and exposure blocks contain multiple proximity expressions, including screen time[tiab:~2], physical activity[tiab:~1], and health behavior[tiab:~1]. The packet does not document clause-specific interpretation review. As the packet notes, ~0 permits either word order.",
          "recommendation": "Document the intended interpretation and acceptability of each proximity clause, including the stay-at-home, distancing, shelter-in-place, food-intake, screen-time, substance-use, health-behavior, physical-activity, eating-behavior, and home-confinement expressions. If any expression is changed or removed, run another complete evaluation.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the documented workload tradeoff for this version. The optional lifestyle and well-being block was tested and retained; the packet reports that it reduced retrieval by 85.9%, lost none of the nine development records, and had no relevant records in the 30-record loss sample. The remaining count still exceeds the 10,000-record budget and should remain visible as a limitation.",
          "evidence": "The packet reports 109,291 records without the outcome block and 15,360 with it, with 0 of 30 sampled removed records relevant and all 9 known development records retrieved. The outcome block is the only optional concept tested in the packet."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "32458b71ff8ce076cabd8e808ede8e1d2769363df630cd0055ebcbe58ee46868",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Current translations retain the intended MeSH and Title/Abstract fields; the evaluation reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are ORed internally and ANDed; the optional outcome block has a current tested decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Selected headings are verified descriptors with no reported vocabulary or translation blockers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Screen-use text and quarantine heading/text were added and re-evaluated; all nine development records remain retrieved."
        },
        "syntax": {
          "verdict": "revise",
          "note": "P1-03 remains open until clause-specific interpretation is included in the workspace packet and verified in a new round."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The only effective date restriction is the Entrez cutoff; no publication-date or ad hoc filters are applied."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "Eligibility names screen use, but the original outcome block included only screen time[tiab:~2].",
          "recommendation": "Add and test an explicit screen-use expression, then reassess the complete strategy and known-record retrieval.",
          "status": "resolved",
          "response": "The current block adds \"screen use\"[tiab:~1] and \"use of screens\"[tiab:~1]. The refreshed strategy has 15,792 results and retrieves all nine development records."
        },
        {
          "id": "P1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The exposure rationale calls for quarantine terminology, but the original exposure block had no quarantine term.",
          "recommendation": "Add and test a quarantine term such as quarantin*[tiab], then reassess the complete strategy and known-record retrieval.",
          "status": "resolved",
          "response": "The current exposure block includes Quarantine[Mesh] and quarantin*[tiab]. The refreshed strategy has 15,792 results and retrieves all nine development records."
        },
        {
          "id": "P1-03",
          "domain": "syntax",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome and exposure blocks contain multiple proximity expressions, but the packet does not document clause-specific interpretation review. Proximity permits words in either order.",
          "recommendation": "Document the intended interpretation and acceptability of each proximity clause, including the stay-at-home, distancing, shelter-in-place, food-intake, screen-time, substance-use, health-behavior, physical-activity, eating-behavior, and home-confinement expressions. If any expression is changed or removed, run another complete evaluation.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the documented workload tradeoff for this version. The outcome block was tested and retained; the remaining retrieval count exceeds the 10,000-record budget and should remain visible as a limitation.",
          "evidence": "The current packet reports 115,041 records without the outcome block and 15,792 with it, an 86.3% reduction. It reports no known development records lost and 0 relevant records in the refreshed 30-record loss sample. The outcome block is the only optional concept tested."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "1849f34ebe588885691870c3c8e3d04d3734310d4bbb65996b58eb1eafb9bf88",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues; the current evaluation retains the intended fields and concepts."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure and outcome terms are ORed within blocks, and the blocks are ANDed. The optional outcome block has a current test and documented tradeoff."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH descriptors and no vocabulary or translation blockers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current blocks include screen-use expressions and Quarantine[Mesh] plus quarantin*[tiab]. The refreshed strategy retrieves all nine development records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The protocol documents the proximity clauses, their distances, acceptance of either word order, and where each clause's translation and count are recorded."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The packet reports the Entrez cutoff and no publication-date, language, design, or population filter."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "Eligibility names screen use, while the earlier strategy had only screen-time wording.",
          "recommendation": "Add and test an explicit screen-use expression, then reassess the complete strategy and known-record retrieval.",
          "status": "resolved",
          "response": "The current outcome block includes \"screen use\"[tiab:~1] and \"use of screens\"[tiab:~1]. The refreshed strategy retrieves all nine development records."
        },
        {
          "id": "P1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The exposure rationale calls for quarantine terminology, which was absent from the earlier strategy.",
          "recommendation": "Add and test a quarantine term, then reassess the complete strategy and known-record retrieval.",
          "status": "resolved",
          "response": "The current exposure block includes Quarantine[Mesh] and quarantin*[tiab]. The refreshed strategy retrieves all nine development records."
        },
        {
          "id": "P1-03",
          "domain": "syntax",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The earlier packet did not document clause-specific interpretation review for the proximity expressions, which permit either word order.",
          "recommendation": "Document the intended interpretation and acceptability of each proximity clause. If any expression is changed or removed, run another complete evaluation.",
          "status": "resolved",
          "response": "The protocol notes specify each clause's ~1 or ~2 distance, state that either word order and up to that number of intervening words are acceptable, and explain that exact phrase order is not required. They identify the clauses reviewed, report no translation issues, and state that current translations and counts are recorded per clause in the evaluation and final audit."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the documented workload tradeoff for this version. The optional outcome block was tested and retained; the remaining count exceeds the 10,000-record budget.",
          "evidence": "The packet reports 115,041 records without the outcome block and 15,792 with it, an 86.3% reduction, no known development records lost, and 0 relevant records in the refreshed 30-record loss sample."
        }
      ]
    }
  ]
}
```


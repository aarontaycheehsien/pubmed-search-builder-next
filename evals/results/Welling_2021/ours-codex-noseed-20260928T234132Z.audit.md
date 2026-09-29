# PubMed search strategy: audit

Generated 2026-09-29T00:09:36+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User requested no follow-up questions and standard depth. Proceeding with reasonable assumptions: studies reporting at least one listed lifestyle behavior OR well-being outcome are in scope; any population and study design are eligible if outcome data are reported. COVID-19/pandemic/lockdown is the required exposure block. Lifestyle behaviors/well-being is tested as an optional topic-defining outcome block. No language, age, geography, or publication-date restriction. PubMed Entrez entry-date cutoff 2020-11-22 is applied through as_of, not [dp]. No user-supplied known records; standard-depth discovery will be attempted within the skill's candidate-screening budget. Scope shown in the run conversation but not confirmed because user asked not to pause.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | A specific named COVID-19 pandemic exposure, not a broad category whose members should be independently searched; COVID-19, SARS-CoV-2, 2019-nCoV, and quarantine/lockdown terminology are represented directly in this block. Two broader virus/pneumonia probes found no in-scope records outside it. |
| Lifestyle behaviors or well-being | optional | These topic-defining outcomes may reduce screening load but may be inconsistently named; test the outcome block before deciding whether to require it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T00:07:51+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 12,650
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 3 | `Pandemics[Mesh]` | 50,277 | none |
| 4 | `Quarantine[Mesh]` | 3,936 | none |
| 5 | `COVID-19[tiab]` | 67,388 | none |
| 6 | `COVID19[tiab]` | 64,206 | none |
| 7 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 8 | `2019 novel coronavirus[tiab]` | 1,176 | none |
| 9 | `2019-nCoV[tiab]` | 1,288 | none |
| 10 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 11 | `SARS CoV 2[tiab]` | 23,503 | none |
| 12 | `severe acute respiratory syndrome coronavirus 2[tiab]` | 7,988 | none |
| 13 | `coronavirus*[tiab]` | 43,050 | none |
| 14 | `pandemic*[tiab]` | 58,444 | none |
| 15 | `lockdown*[tiab]` | 3,416 | none |
| 16 | `lock down[tiab]` | 163 | none |
| 17 | `stay-at-home[tiab]` | 815 | none |
| 18 | `stay at home[tiab]` | 815 | none |
| 19 | `quarantine*[tiab]` | 6,745 | none |
| 20 | `social distanc*[tiab]` | 3,813 | none |
| 21 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 128,132 | none |
| 22 | `Life Style[Mesh]` | 99,996 | none |
| 23 | `Healthy Lifestyle[Mesh]` | 8,656 | none |
| 24 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 25 | `Motor Activity[Mesh]` | 309,966 | none |
| 26 | `Exercise[Mesh]` | 212,859 | none |
| 27 | `Physical Fitness[Mesh]` | 32,635 | none |
| 28 | `Sleep[Mesh]` | 85,169 | none |
| 29 | `Sleep Wake Disorders[Mesh]` | 96,238 | none |
| 30 | `Feeding Behavior[Mesh]` | 178,421 | none |
| 31 | `Diet[Mesh]` | 296,758 | none |
| 32 | `Eating[Mesh]` | 75,131 | none |
| 33 | `Alcohol Drinking[Mesh]` | 72,506 | none |
| 34 | `Smoking[Mesh]` | 152,983 | none |
| 35 | `Tobacco Use[Mesh]` | 6,633 | none |
| 36 | `Mental Health[Mesh]` | 44,674 | none |
| 37 | `Depression[Mesh]` | 230,067 | none |
| 38 | `Anxiety[Mesh]` | 93,320 | none |
| 39 | `Stress, Psychological[Mesh]` | 139,617 | none |
| 40 | `Quality of Life[Mesh]` | 215,482 | none |
| 41 | `physical activ*[tiab]` | 118,342 | none |
| 42 | `exercise[tiab]` | 272,206 | none |
| 43 | `sedentary[tiab]` | 32,472 | none |
| 44 | `sitting[tiab]` | 23,133 | none |
| 45 | `sleep[tiab]` | 171,185 | none |
| 46 | `diet*[tiab]` | 587,723 | none |
| 47 | `eating[tiab]` | 77,769 | none |
| 48 | `nutrition[tiab]` | 181,193 | none |
| 49 | `food intake[tiab]` | 45,992 | none |
| 50 | `alcohol[tiab]` | 263,050 | none |
| 51 | `drinking[tiab]` | 114,398 | none |
| 52 | `smoking[tiab]` | 228,902 | none |
| 53 | `tobacco[tiab]` | 104,259 | none |
| 54 | `lifestyle[tiab]` | 99,644 | none |
| 55 | `life style[tiab]` | 11,282 | none |
| 56 | `health behavior*[tiab]` | 18,620 | none |
| 57 | `health behaviour*[tiab]` | 7,323 | none |
| 58 | `well-being[tiab]` | 80,676 | none |
| 59 | `wellbeing[tiab]` | 91,505 | none |
| 60 | `psychological well-being[tiab]` | 9,542 | none |
| 61 | `mental health[tiab]` | 159,665 | none |
| 62 | `depress*[tiab]` | 474,400 | none |
| 63 | `anxiet*[tiab]` | 201,789 | none |
| 64 | `psychological distress[tiab]` | 20,154 | none |
| 65 | `stress[tiab]` | 779,146 | none |
| 66 | `quality of life[tiab]` | 282,526 | none |
| 67 | `life satisfaction[tiab]` | 8,062 | none |
| 68 | `happiness[tiab]` | 7,214 | none |
| 69 | `Psychological Distress[Mesh]` | 4,500 | none |
| 70 | `Loneliness[Mesh]` | 4,443 | none |
| 71 | `loneliness[tiab]` | 6,825 | none |
| 72 | `lonely[tiab]` | 1,688 | none |
| 73 | `mental well-being[tiab]` | 2,604 | none |
| 74 | `mental wellbeing[tiab]` | 803 | none |
| 75 | `social well-being[tiab]` | 1,903 | none |
| 76 | `social wellbeing[tiab]` | 335 | none |
| 77 | `subjective well-being[tiab]` | 3,343 | none |
| 78 | `subjective wellbeing[tiab]` | 372 | none |
| 79 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78` | 3,830,750 | none |
| 80 | `#21 AND #79` | 12,650 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR Coronavirus Infections[Mesh] OR Pandemics[Mesh] OR Quarantine[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR coronavirus disease 2019[tiab] OR 2019 novel coronavirus[tiab] OR 2019-nCoV[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR severe acute respiratory syndrome coronavirus 2[tiab] OR coronavirus*[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR lock down[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR quarantine*[tiab] OR social distanc*[tiab]) AND (Life Style[Mesh] OR Healthy Lifestyle[Mesh] OR Sedentary Behavior[Mesh] OR Motor Activity[Mesh] OR Exercise[Mesh] OR Physical Fitness[Mesh] OR Sleep[Mesh] OR Sleep Wake Disorders[Mesh] OR Feeding Behavior[Mesh] OR Diet[Mesh] OR Eating[Mesh] OR Alcohol Drinking[Mesh] OR Smoking[Mesh] OR Tobacco Use[Mesh] OR Mental Health[Mesh] OR Depression[Mesh] OR Anxiety[Mesh] OR Stress, Psychological[Mesh] OR Quality of Life[Mesh] OR physical activ*[tiab] OR exercise[tiab] OR sedentary[tiab] OR sitting[tiab] OR sleep[tiab] OR diet*[tiab] OR eating[tiab] OR nutrition[tiab] OR food intake[tiab] OR alcohol[tiab] OR drinking[tiab] OR smoking[tiab] OR tobacco[tiab] OR lifestyle[tiab] OR life style[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR well-being[tiab] OR wellbeing[tiab] OR psychological well-being[tiab] OR mental health[tiab] OR depress*[tiab] OR anxiet*[tiab] OR psychological distress[tiab] OR stress[tiab] OR quality of life[tiab] OR life satisfaction[tiab] OR happiness[tiab] OR Psychological Distress[Mesh] OR Loneliness[Mesh] OR loneliness[tiab] OR lonely[tiab] OR mental well-being[tiab] OR mental wellbeing[tiab] OR social well-being[tiab] OR social wellbeing[tiab] OR subjective well-being[tiab] OR subjective wellbeing[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors or well-being | AND-ed | 128,132 / 12,650 | 90.1% | none | 0/30 (up to 10% of removed records could be relevant) | The revised wording sample contains the same 30 PMIDs as the immediately previous sample, which were screened after the block's meaning and eligibility criteria were fixed. None met the criteria: the records concerned earlier non-COVID pandemics, clinical/service impacts without eligible outcomes, or COVID prevention practices rather than lifestyle or well-being outcomes. The outcome block retains all known eligible records and reduces the count by approximately 90%. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_exposure | 3,830,750 | 0 |
| outcomes | 128,132 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 128,132 | initial | none | Initial broad COVID-19/lockdown exposure block with a separate optional lifestyle/well-being outcome block, based on the plain-language question; no known records supplied. |
| 2 | 12,561 | outcomes: +47 / -0 | none | Recorded the optional outcome loss sample decision (AND after screening 30 excluded records with zero relevant) and screened the COVID exposure category probe (30 unrelated generic virus/pneumonia records). |
| 3 | 12,650 | outcomes: +4 / -0 | none | Added MeSH and free-text terms for psychological distress and loneliness based on topic scope and term ranking from the development records; maintained the outcome AND decision. |
| 4 | 12,650 | outcomes: +6 / -0 | none | Addressed critic F1 by adding explicit hyphenated and unhyphenated mental, social, and subjective well-being text phrases named in the eligibility criteria. Reclassified the specific COVID-19 exposure as not a member category (COVID/SARS-CoV-2 are direct synonyms, and two broad category probes found no eligible member-only records); maintained the two-block PECO search. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1 should-fix open
- Round 2 on version 4: 1 findings; F1 should-fix resolved
- Round 3 on version 4: 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1613 NCBI requests logged (742 from cache); strategy sha256 34f3dce33edb._

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
        "message": "12,650 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "12,650 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
        "text": "Pandemics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
        "text": "Quarantine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "Sedentary Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Physical Fitness",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010809",
          "name": "Physical Fitness",
          "type": "descriptor",
          "scope_note": "The ability to carry out daily tasks and perform physical activities in a highly functional state, often as a result of physical conditioning.",
          "tree_numbers": [
            "G11.427.685",
            "I03.450.642.845.054.800",
            "N01.400.545"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010809",
      "preferred_label": "Physical Fitness",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "Physical Fitness",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "Sleep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep Wake Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Sleep Wake Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Eating",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004435",
          "name": "Eating",
          "type": "descriptor",
          "scope_note": "The consumption of edible substances.",
          "tree_numbers": [
            "G07.203.650.283",
            "G10.261.330"
          ],
          "entry_terms": 21,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004435",
      "preferred_label": "Eating",
      "type": "descriptor",
      "location": "vocabulary:31",
      "term": {
        "text": "Eating",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Alcohol Drinking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Smoking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Tobacco Use",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "Tobacco Use",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Stress, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Quality of Life",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:68",
      "term": {
        "text": "Psychological Distress",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Loneliness",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:07:51+00:00",
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
      "location": "vocabulary:69",
      "term": {
        "text": "Loneliness",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"pandemics\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"severe acute respiratory syndrome coronavirus 2\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"social distanc*\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"healthy lifestyle\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"motor activity\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"physical fitness\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"sleep wake disorders\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"eating\"[MeSH Terms] OR \"alcohol drinking\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"tobacco use\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"anxiety\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR \"physical activ*\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"nutrition\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"lifestyle\"[Title/Abstract] OR \"life style\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"psychological well being\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"anxiet*\"[Title/Abstract] OR \"psychological distress\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"happiness\"[Title/Abstract] OR \"psychological distress\"[MeSH Terms] OR \"loneliness\"[MeSH Terms] OR \"loneliness\"[Title/Abstract] OR \"lonely\"[Title/Abstract] OR \"mental well being\"[Title/Abstract] OR \"mental wellbeing\"[Title/Abstract] OR \"social well being\"[Title/Abstract] OR \"social wellbeing\"[Title/Abstract] OR \"subjective well being\"[Title/Abstract] OR \"subjective wellbeing\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "7bfe7305bd37bb7880886291ffc850ee5b266c49e4b13159938e3c62a21ce4a6",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The exposure and outcome blocks are combined appropriately, but the text-word list does not explicitly cover every well-being member named in the eligibility criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure synonyms and outcome terms are ORed within their blocks, and the blocks are ANDed as intended."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant headings for COVID-19, pandemic and quarantine concepts, lifestyle behaviors, and mental and subjective well-being outcomes."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The eligibility names mental, psychological, social, and subjective well-being. The strategy includes psychological well-being and generic well-being terms, but lacks explicit mental well-being, social well-being, and subjective well-being expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed translations show recognized fields and no reported translation issues or syntax warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, or geography limits are applied. The as-of entry-date cutoff is documented in the scope notes."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria explicitly name mental, social, and subjective well-being, but the outcome block does not include those expressions. Generic well-being terms may retrieve them, but the packet's translation check calls for coverage of each named member by its own name.",
          "recommendation": "Add and test explicit text-word expressions for mental well-being, social well-being, and subjective well-being, including unhyphenated variants where appropriate; then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count remains above the workload budget after testing and retaining the outcome block. The packet documents the only optional searchable concept and its 90.1% reduction, with no relevant records in the 30-record loss sample or among known records. Further narrowing could lose eligible records.",
          "evidence": "12,650 records remain against a 10,000-record budget; 128,132 without versus 12,650 with the outcome block; 0/30 sampled removed records relevant; no known records lost."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "5c356ca4cbdc90fb0f59e736f0a84b055ea24098357859c6a524f1db025686e9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure and outcome blocks are combined as intended. Each well-being type named in eligibility now has explicit text-word coverage, including hyphenated and unhyphenated mental, social, and subjective well-being expressions."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms and outcome terms are ORed within their blocks, and the two blocks are ANDed. No proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for COVID-19, coronavirus infections, pandemics, and quarantine, and for lifestyle behaviors and mental, psychological distress, and quality-of-life outcomes."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word list covers the named lifestyle behaviors and well-being outcomes, including the previously missing explicit mental, social, and subjective well-being expressions and unhyphenated variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final PubMed query has no reported warning or error diagnostics. The displayed translations use recognized fields and the date-entry range."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, or geography filters are applied. The 2020-11-22 cutoff is implemented as an Entrez entry-date range and documented in the scope notes."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria explicitly name mental, social, and subjective well-being, but the outcome block does not include those expressions. Generic well-being terms may retrieve them, but the packet's translation check calls for coverage of each named member by its own name.",
          "recommendation": "Add and test explicit text-word expressions for mental well-being, social well-being, and subjective well-being, including unhyphenated variants where appropriate; then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current outcome block includes mental well-being, mental wellbeing, social well-being, social wellbeing, subjective well-being, and subjective wellbeing as text-word terms. The complete evaluation was rerun for strategy version 4."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count remains above the workload budget after testing the outcome block as an optional concept. The packet documents the reduction and the screened loss sample; adding further restrictions could exclude eligible records.",
          "evidence": "The outcome block reduces results from 128,132 to 12,650 (90.1%); none of the 30 sampled removed records met eligibility criteria, and no known eligible records were lost."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "5c356ca4cbdc90fb0f59e736f0a84b055ea24098357859c6a524f1db025686e9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block now explicitly covers mental, social, and subjective well-being, including hyphenated and unhyphenated forms."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each block, and the exposure and outcome blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for COVID-19, coronavirus infections, pandemics, quarantine, lifestyle behaviors, and well-being outcomes."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover the named lifestyle behaviors and well-being outcomes, including the expressions added to address F1."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no diagnostics or syntax warnings for the current strategy."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, or geography filters are applied; the entry-date cutoff is documented in the scope notes."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria explicitly name mental, social, and subjective well-being, but the outcome block does not include those expressions. Generic well-being terms may retrieve them, but the packet's translation check calls for coverage of each named member by its own name.",
          "recommendation": "Add and test explicit text-word expressions for mental well-being, social well-being, and subjective well-being, including unhyphenated variants where appropriate; then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current outcome block includes mental well-being, mental wellbeing, social well-being, social wellbeing, subjective well-being, and subjective wellbeing as text-word terms. The complete evaluation was rerun for strategy version 4."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count remains above the workload budget after testing and retaining the outcome block. The packet documents the optional concept's reduction and screened loss sample; further narrowing could exclude eligible records.",
          "evidence": "12,650 records remain against a 10,000-record budget; the outcome block reduces results from 128,132 to 12,650 (90.1%); 0 of 30 sampled removed records were relevant, and no known eligible records were lost."
        }
      ]
    }
  ]
}
```


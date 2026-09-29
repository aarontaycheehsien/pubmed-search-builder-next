# PubMed search strategy: audit

Generated 2026-09-29T19:04:43+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without questions; scope roles and eligibility are working assumptions. No user-supplied known articles were available. Twenty-one records were screened in from precise PubMed pilot samples as a development set. Historical PubMed snapshot required by harness: retain records indexed in PubMed on or before 2020-11-22 via PSB_AS_OF for every command; do not apply a publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related public health restrictions | search | The pandemic/restriction context is the exposure that defines the review and should be named or indexed in eligible reports; COVID, lockdown, quarantine, and stay-at-home wording are exposure variants. |
| Lifestyle behavior and well-being outcomes | optional | Lifestyle behavior and well-being outcomes together define the topic, but eligible articles may not reliably name them; one OR-ed outcome block will be tested against relevant pilot records and a loss sample before any decision to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T19:03:00+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 15,871
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,931 | none |
| 3 | `covid[tiab]` | 67,980 | none |
| 4 | `COVID19[tiab]` | 64,206 | none |
| 5 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 6 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 7 | `2019-nCoV[tiab]` | 1,288 | none |
| 8 | `"novel coronavirus"[tiab]` | 6,179 | none |
| 9 | `"COVID-19 pandemic"[tiab]` | 20,381 | none |
| 10 | `lockdown*[tiab]` | 3,416 | none |
| 11 | `quarantine*[tiab]` | 6,745 | none |
| 12 | `"stay at home"[tiab]` | 815 | none |
| 13 | `"stay-at-home"[tiab]` | 815 | none |
| 14 | `"shelter in place"[tiab]` | 210 | none |
| 15 | `"social distancing"[tiab]` | 2,657 | none |
| 16 | `"physical distancing"[tiab]` | 436 | none |
| 17 | `"home isolation"[tiab]` | 109 | none |
| 18 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 84,063 | none |
| 19 | `"Life Style"[Mesh]` | 99,996 | none |
| 20 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 21 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 22 | `Exercise[Mesh]` | 212,859 | none |
| 23 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 24 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 25 | `Smoking[Mesh]` | 152,983 | none |
| 26 | `Sleep[Mesh]` | 85,169 | none |
| 27 | `"Mental Health"[Mesh]` | 44,674 | none |
| 28 | `Anxiety[Mesh]` | 93,320 | none |
| 29 | `Depression[Mesh]` | 230,067 | none |
| 30 | `"Quality of Life"[Mesh]` | 215,482 | none |
| 31 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 32 | `Affect[Mesh]` | 34,956 | none |
| 33 | `Resilience, Psychological[Mesh]` | 6,980 | none |
| 34 | `substance use[tiab]` | 37,851 | none |
| 35 | `subjective wellbeing[tiab]` | 372 | none |
| 36 | `"Substance-Related Disorders"[Mesh]` | 291,305 | none |
| 37 | `"drug use"[tiab]` | 46,742 | none |
| 38 | `"drug consumption"[tiab]` | 2,891 | none |
| 39 | `"subjective well-being"[tiab]` | 3,343 | none |
| 40 | `"subjective well being"[tiab]` | 3,343 | none |
| 41 | `lifestyle*[tiab]` | 108,849 | none |
| 42 | `behavior*[tiab]` | 1,024,043 | none |
| 43 | `behaviour*[tiab]` | 293,760 | none |
| 44 | `habit*[tiab]` | 183,165 | none |
| 45 | `"health behavior"[tiab]` | 9,149 | none |
| 46 | `"health behaviour"[tiab]` | 4,329 | none |
| 47 | `"physical activity"[tiab]` | 114,494 | none |
| 48 | `physical inactivity[tiab]` | 8,195 | none |
| 49 | `inactivity[tiab]` | 15,458 | none |
| 50 | `exercise[tiab]` | 272,207 | none |
| 51 | `sedentary[tiab]` | 32,472 | none |
| 52 | `"screen time"[tiab]` | 2,454 | none |
| 53 | `sitting[tiab]` | 23,133 | none |
| 54 | `walking[tiab]` | 73,723 | none |
| 55 | `step count*[tiab]` | 1,994 | none |
| 56 | `diet*[tiab]` | 587,723 | none |
| 57 | `eating[tiab]` | 77,769 | none |
| 58 | `eating habits[tiab]` | 5,564 | none |
| 59 | `"food intake"[tiab]` | 45,992 | none |
| 60 | `"food consumption"[tiab]` | 14,333 | none |
| 61 | `sleep*[tiab]` | 188,562 | none |
| 62 | `insomnia[tiab]` | 22,051 | none |
| 63 | `smoking[tiab]` | 228,902 | none |
| 64 | `tobacco[tiab]` | 104,259 | none |
| 65 | `alcohol[tiab]` | 263,050 | none |
| 66 | `drinking[tiab]` | 114,398 | none |
| 67 | `wellbeing[tiab]` | 91,505 | none |
| 68 | `well-being[tiab]` | 80,676 | none |
| 69 | `"psychological well-being"[tiab]` | 9,542 | none |
| 70 | `"mental well-being"[tiab]` | 2,604 | none |
| 71 | `"quality of life"[tiab]` | 282,526 | none |
| 72 | `"mental health"[tiab]` | 159,665 | none |
| 73 | `psychological[tiab]` | 229,134 | none |
| 74 | `anxiety[tiab]` | 199,917 | none |
| 75 | `depression[tiab]` | 348,632 | none |
| 76 | `stress[tiab]` | 779,147 | none |
| 77 | `distress[tiab]` | 119,022 | none |
| 78 | `affect[tiab]` | 682,159 | none |
| 79 | `mood*[tiab]` | 78,062 | none |
| 80 | `loneliness[tiab]` | 6,825 | none |
| 81 | `resilien*[tiab]` | 35,817 | none |
| 82 | `emotional[tiab]` | 159,221 | none |
| 83 | `"life satisfaction"[tiab]` | 8,062 | none |
| 84 | `happiness[tiab]` | 7,214 | none |
| 85 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84` | 5,538,970 | none |
| 86 | `#18 AND #85` | 15,871 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR covid[tiab] OR COVID19[tiab] OR coronavirus disease 2019[tiab] OR SARS-CoV-2[tiab] OR 2019-nCoV[tiab] OR "novel coronavirus"[tiab] OR "COVID-19 pandemic"[tiab] OR lockdown*[tiab] OR quarantine*[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "shelter in place"[tiab] OR "social distancing"[tiab] OR "physical distancing"[tiab] OR "home isolation"[tiab]) AND ("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Sedentary Behavior"[Mesh] OR Exercise[Mesh] OR "Feeding Behavior"[Mesh] OR "Alcohol Drinking"[Mesh] OR Smoking[Mesh] OR Sleep[Mesh] OR "Mental Health"[Mesh] OR Anxiety[Mesh] OR Depression[Mesh] OR "Quality of Life"[Mesh] OR "Stress, Psychological"[Mesh] OR Affect[Mesh] OR Resilience, Psychological[Mesh] OR substance use[tiab] OR subjective wellbeing[tiab] OR "Substance-Related Disorders"[Mesh] OR "drug use"[tiab] OR "drug consumption"[tiab] OR "subjective well-being"[tiab] OR "subjective well being"[tiab] OR lifestyle*[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR habit*[tiab] OR "health behavior"[tiab] OR "health behaviour"[tiab] OR "physical activity"[tiab] OR physical inactivity[tiab] OR inactivity[tiab] OR exercise[tiab] OR sedentary[tiab] OR "screen time"[tiab] OR sitting[tiab] OR walking[tiab] OR step count*[tiab] OR diet*[tiab] OR eating[tiab] OR eating habits[tiab] OR "food intake"[tiab] OR "food consumption"[tiab] OR sleep*[tiab] OR insomnia[tiab] OR smoking[tiab] OR tobacco[tiab] OR alcohol[tiab] OR drinking[tiab] OR wellbeing[tiab] OR well-being[tiab] OR "psychological well-being"[tiab] OR "mental well-being"[tiab] OR "quality of life"[tiab] OR "mental health"[tiab] OR psychological[tiab] OR anxiety[tiab] OR depression[tiab] OR stress[tiab] OR distress[tiab] OR affect[tiab] OR mood*[tiab] OR loneliness[tiab] OR resilien*[tiab] OR emotional[tiab] OR "life satisfaction"[tiab] OR happiness[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 21 | 21 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behavior and well-being outcomes | AND-ed | 84,063 / 15,871 | 81.1% | none | 0/30 (up to 10% of removed records could be relevant) | The updated outcome block explicitly searches substance use and subjective well-being and their main variants. It retains all 21 screened development records; after the vocabulary additions, the current random loss sample of 30 records was screened and contained no eligible articles. The measured reduction is 81.1%, though the count remains above the standard workload budget and the loss sample has limited power. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_exposure | 5,538,970 | 0 |
| outcomes | 84,063 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 133,258 | initial | none | Initial exposure block with a broad lifestyle/well-being optional outcome candidate; relevant pilot records added after title/abstract screening. |
| 2 | 152,205 | covid_exposure: +3 / -0 | none | Expanded the exposure MeSH layer with COVID-19 terms found on pilot records and broadened the optional outcome vocabulary to include common lifestyle/behavior, sleep, diet, substance-use, and psychological outcome wording; tested before deciding its role. |
| 3 | 84,063 | covid_exposure: +2 / -7 | none | Removed historical generic coronavirus, pandemics, quarantine, and social-isolation headings that expanded the exposure query beyond the COVID-19/related-lockdown scope; retained COVID-specific headings and text variants plus explicit restriction terms. |
| 4 | 15,658 | outcomes: +61 / -0 | none | AND-ed the optional OR-ed outcome block after retaining all 21 development records and screening the full 30-record loss sample with no relevant finds. |
| 5 | 15,658 | outcomes: +0 / -1 | none | Removed the noncanonical MeSH label Physical Activity after live authority validation mapped it to the canonical Exercise heading already present in the block; reevaluating the revised query. |
| 6 | 15,658 | outcomes: +0 / -1 | none | Removed the Psychological Well-Being descriptor from the 2020-bounded strategy because the verified heading was introduced in 2023 and has zero records in the specified Entrez-date window; retained explicit title/abstract well-being and mental-health wording. This invalidates the optional decision, so it will be resampled. |
| 7 | 15,871 | outcomes: +7 / -0 | none | Resolved critic finding R1-F1 by adding the named bare outcome concepts substance use and subjective well-being with MeSH/text-word coverage and spelling variants; the optional outcome decision must be refreshed and the revised block checked for new known-record loss. |
| 8 | 15,871 | outcomes: +5 / -5 | none | Resolved critic finding R1-F1 by adding the named bare outcome concepts substance use and subjective well-being with MeSH/text-word coverage and spelling variants; the optional outcome decision must be refreshed and the revised block checked for new known-record loss. |
| 9 | 15,871 | limits/combination | none | Removed duplicate copies of critic-requested bare outcome terms before refreshing the optional-block sample. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 6: 1 findings; R1-F1 must-fix open
- Round 2 on version 9: 1 findings; R1-F1 must-fix resolved
- Round 3 on version 9: 1 findings; R1-F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2194 NCBI requests logged (1354 from cache); strategy sha256 604cf98c976b._

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
        "message": "15,871 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "15,871 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "Smoking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Sleep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Affect",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "Affect",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Resilience, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D055500",
          "name": "Resilience, Psychological",
          "type": "descriptor",
          "scope_note": "The human ability to adapt in the face of tragedy, trauma, adversity, hardship, and ongoing significant life stressors.",
          "tree_numbers": [
            "F02.940"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D055500",
      "preferred_label": "Resilience, Psychological",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "Resilience, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Substance-Related Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:03:00+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Substance-Related Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"covid 19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"covid\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"COVID-19 pandemic\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter in place\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"physical distancing\"[Title/Abstract] OR \"home isolation\"[Title/Abstract]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"Mental Health\"[MeSH Terms] OR \"anxiety\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"Quality of Life\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"affect\"[MeSH Terms] OR \"resilience, psychological\"[MeSH Terms] OR \"substance use\"[Title/Abstract] OR \"subjective wellbeing\"[Title/Abstract] OR \"Substance-Related Disorders\"[MeSH Terms] OR \"drug use\"[Title/Abstract] OR \"drug consumption\"[Title/Abstract] OR \"subjective well-being\"[Title/Abstract] OR \"subjective well-being\"[Title/Abstract] OR \"lifestyle*\"[Title/Abstract] OR \"behavior*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract] OR \"habit*\"[Title/Abstract] OR \"Health Behavior\"[Title/Abstract] OR \"health behaviour\"[Title/Abstract] OR \"physical activity\"[Title/Abstract] OR \"physical inactivity\"[Title/Abstract] OR \"inactivity\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"sitting\"[Title/Abstract] OR \"walking\"[Title/Abstract] OR \"step count*\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"eating habits\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"sleep*\"[Title/Abstract] OR \"insomnia\"[Title/Abstract] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"psychological well-being\"[Title/Abstract] OR \"mental well-being\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"psychological\"[Title/Abstract] OR \"anxiety\"[Title/Abstract] OR \"depression\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"affect\"[Title/Abstract] OR \"mood*\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"resilien*\"[Title/Abstract] OR \"emotional\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"happiness\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 6,
      "review_sha256": "6636ec1b689e3e3b5deebb3a344b2ae4acc49a0bbc3e8227bdcf919b927b3ed2",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The exposure and most outcome concepts are represented. The eligibility names substance use and subjective well-being, but the outcome block does not include either bare phrase; alcohol/tobacco terms and broader well-being terms do not satisfy the packet’s clause-specific translation check."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are OR-ed internally and AND-ed together. The optional outcome block was tested against the development set and a 30-record loss sample; the limited power and over-budget result are disclosed. Retain the block provisionally while addressing the named-term gaps."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed headings are reported as verified, and no heading translation issues or PubMed warnings are reported. Human eligibility is handled at screening rather than by an unexplained population filter."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add the eligibility’s bare-name outcome terms substance use and subjective well-being, with spelling variants as appropriate. The existing broader terms do not directly cover these named members under the packet’s translation check."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is balanced and the Boolean structure is explicit. The packet reports no lint errors, translation issues, or PubMed warnings; the duplicated stay-at-home mapping is harmless."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unexplained limits are applied. The as-of date is implemented as an entry-date cutoff, consistent with the stated historical snapshot instruction, rather than as a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility explicitly includes substance use and subjective well-being, but the outcome block does not search either member by its own bare name. Existing terms for alcohol, tobacco, well-being, and mental health do not ensure retrieval of records using those exact concepts.",
          "recommendation": "Add substance use[tiab] and a bare subjective well-being phrase in the appropriate spelling variants, then rerun the complete evaluation and check the known records and workload.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional outcome block was tested and retained, and the packet identifies no additional searchable concept that can be safely added as an AND block. The final count still exceeds the stated workload budget, so this remains a documented screening workload risk.",
          "evidence": "The outcome block reduces the exposure-only set from 84,063 to 15,658 (81.4%); the loss sample found 0 relevant records among 30, while all 21 development records remain retrievable. The packet notes the sample’s limited power."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 9,
      "review_sha256": "9290261d68bde86ddffa4245ea138d1f3e11b640b7f1b918e32a0f3999f08852",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block now includes substance use[tiab] and subjective well-being in hyphenated and unhyphenated forms, addressing the named-member gaps from round 1. The listed exposure and outcome concepts are represented."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure and outcome terms are OR-ed within their blocks and the blocks are AND-ed. The optional outcome block retains all 21 screened development records; the current loss sample found 0 relevant records among 30, with limited power disclosed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified headings and no heading translation issues or PubMed warnings. Human eligibility is addressed at screening without an unexplained population filter."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The required bare-name terms substance use and subjective well-being are now present, alongside the listed behavior and well-being vocabulary."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query structure is explicit and the packet reports no lint errors, translation issues, or PubMed warnings. The duplicate stay-at-home and subjective well-being mappings are redundant but do not change the Boolean result."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The packet reports an entry-date cutoff through 2020-11-22 and no unexplained limits."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility explicitly includes substance use and subjective well-being, but the outcome block does not search either member by its own bare name. Existing terms for alcohol, tobacco, well-being, and mental health do not ensure retrieval of records using those exact concepts.",
          "recommendation": "Add substance use[tiab] and a bare subjective well-being phrase in the appropriate spelling variants, then rerun the complete evaluation and check the known records and workload.",
          "status": "resolved",
          "response": "The current outcome block includes substance use[tiab], subjective wellbeing[tiab], and quoted hyphenated and unhyphenated subjective well-being phrases. The complete evaluation reports no known records lost and retains all 21 screened development records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional outcome block has been tested and retained. The remaining excess over the 10,000-record workload budget is documented as a screening workload risk.",
          "evidence": "The current block reduces the exposure-only set from 84,063 to 15,871 records (81.1%). No known records are lost, and the current loss sample found 0 relevant records among 30; the packet notes the sample has limited power. The final count remains above budget."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 9,
      "review_sha256": "9290261d68bde86ddffa4245ea138d1f3e11b640b7f1b918e32a0f3999f08852",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block includes the named substance-use and subjective-well-being terms and their stated variants. The round 1 translation finding is resolved."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-ed within each block, and the exposure and outcome blocks are AND-ed. The outcome block retains all 21 development records; the loss sample found 0 relevant records among 30, with limited power disclosed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified headings and no heading translation issues or PubMed warnings. Human eligibility is handled at screening without an unexplained population filter."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The listed exposure and outcome concepts are represented, including the named substance-use and subjective-well-being terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query structure is explicit, with no reported lint errors, translation issues, or PubMed warnings. Redundant term mappings do not change the Boolean result."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unexplained limits are applied. The packet reports an entry-date cutoff through 2020-11-22."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility explicitly includes substance use and subjective well-being, but the outcome block does not search either member by its own bare name. Existing terms for alcohol, tobacco, well-being, and mental health do not ensure retrieval of records using those exact concepts.",
          "recommendation": "Add substance use[tiab] and a bare subjective well-being phrase in the appropriate spelling variants, then rerun the complete evaluation and check the known records and workload.",
          "status": "resolved",
          "response": "The current outcome block includes substance use[tiab], subjective wellbeing[tiab], and quoted hyphenated and unhyphenated subjective well-being phrases. The complete evaluation reports no known records lost and retains all 21 screened development records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional outcome block has been tested and retained. The remaining excess over the 10,000-record workload budget is documented as a screening workload risk.",
          "evidence": "The current block reduces the exposure-only set from 84,063 to 15,871 records (81.1%). No known records are lost, and the current loss sample found 0 relevant records among 30; the packet notes the sample has limited power. The final count remains above budget."
        }
      ]
    }
  ]
}
```


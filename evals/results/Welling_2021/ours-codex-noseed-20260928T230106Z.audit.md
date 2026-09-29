# PubMed search strategy: audit

Generated 2026-09-28T23:40:29+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User supplied no known relevant articles and asked not to be queried during this run. Proceeding with these assumptions. PubMed coverage is bounded by Entrez date 2020-11-22 via PSB_AS_OF; no publication-date limit is used. COVID-19 terminology is retained as the required exposure context; related lockdown/restriction terms are included for records describing the exposure by its measure. Either lifestyle behavior or well-being outcomes can qualify. No population, language, geography, age, or study-design limit is assumed.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 and related lockdown or public health restrictions | search | The COVID-19 context defines the exposure and is expected to be named; lockdown, quarantine and stay-at-home restrictions are included as related exposure terminology. |
| Lifestyle behaviors and well-being outcomes | optional | These outcomes define the topic and are searchable, but reporting is variable; test an inclusive outcome block before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:38:58+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 14,477
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Coronavirus Infections"[Mesh]` | 67,535 | none |
| 2 | `"Quarantine"[Mesh]` | 3,936 | none |
| 3 | `"COVID-19"[tiab]` | 67,388 | none |
| 4 | `COVID19[tiab]` | 64,206 | none |
| 5 | `"2019 novel coronavirus"[tiab]` | 1,176 | none |
| 6 | `"novel coronavirus"[tiab]` | 6,179 | none |
| 7 | `"SARS-CoV-2"[tiab]` | 23,503 | none |
| 8 | `SARSCoV2[tiab]` | 19,859 | none |
| 9 | `"2019-nCoV"[tiab]` | 1,288 | none |
| 10 | `"2019 nCoV"[tiab]` | 1,288 | none |
| 11 | `coronavirus*[tiab]` | 43,050 | none |
| 12 | `lockdown*[tiab]` | 3,416 | none |
| 13 | `"stay at home"[tiab]` | 815 | none |
| 14 | `"stay-at-home"[tiab]` | 815 | none |
| 15 | `"shelter in place"[tiab]` | 210 | none |
| 16 | `"social distancing"[tiab]` | 2,657 | none |
| 17 | `quarantin*[tiab]` | 6,954 | none |
| 18 | `confinement[tiab]` | 20,190 | none |
| 19 | `"self-isolation"[tiab]` | 289 | none |
| 20 | `"self isolation"[tiab]` | 289 | none |
| 21 | `movement restrict*[tiab]` | 592 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 121,984 | none |
| 23 | `"Exercise"[Mesh]` | 212,859 | none |
| 24 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 25 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 26 | `"Sleep"[Mesh]` | 85,169 | none |
| 27 | `"Mental Health"[Mesh]` | 44,674 | none |
| 28 | `"Quality of Life"[Mesh]` | 215,482 | none |
| 29 | `"Anxiety"[Mesh]` | 93,320 | none |
| 30 | `"Depression"[Mesh]` | 129,618 | none |
| 31 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 32 | `"Loneliness"[Mesh]` | 4,443 | none |
| 33 | `"Personal Satisfaction"[Mesh]` | 20,683 | none |
| 34 | `"Smoking"[Mesh]` | 152,983 | none |
| 35 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 36 | `lifestyle[tiab]` | 99,644 | none |
| 37 | `"health behavior"[tiab]` | 9,149 | none |
| 38 | `"health behaviors"[tiab]` | 11,055 | none |
| 39 | `"health behaviour"[tiab]` | 4,329 | none |
| 40 | `"health behaviours"[tiab]` | 3,546 | none |
| 41 | `physical activit*[tiab]` | 118,110 | none |
| 42 | `exercis*[tiab]` | 307,827 | none |
| 43 | `sedentar*[tiab]` | 33,160 | none |
| 44 | `"screen time"[tiab]` | 2,454 | none |
| 45 | `"diet quality"[tiab]` | 4,283 | none |
| 46 | `dietary[tiab]` | 260,599 | none |
| 47 | `eating[tiab]` | 77,769 | none |
| 48 | `"food consumption"[tiab]` | 14,333 | none |
| 49 | `sleep[tiab]` | 171,185 | none |
| 50 | `"sleep quality"[tiab]` | 15,610 | none |
| 51 | `smoking[tiab]` | 228,902 | none |
| 52 | `tobacco[tiab]` | 104,259 | none |
| 53 | `alcohol[tiab]` | 263,050 | none |
| 54 | `"substance use"[tiab]` | 37,851 | none |
| 55 | `"mental health"[tiab]` | 159,665 | none |
| 56 | `"psychological well-being"[tiab]` | 9,542 | none |
| 57 | `"psychological wellbeing"[tiab]` | 1,436 | none |
| 58 | `"well-being"[tiab]` | 80,676 | none |
| 59 | `wellbeing[tiab]` | 91,505 | none |
| 60 | `"quality of life"[tiab]` | 282,526 | none |
| 61 | `"life satisfaction"[tiab]` | 8,062 | none |
| 62 | `loneliness[tiab]` | 6,825 | none |
| 63 | `anxiety[tiab]` | 199,917 | none |
| 64 | `depress*[tiab]` | 474,400 | none |
| 65 | `stress[tiab]` | 779,146 | none |
| 66 | `distress[tiab]` | 119,022 | none |
| 67 | `diet[tiab]` | 339,581 | none |
| 68 | `"alcohol use"[tiab]` | 36,813 | none |
| 69 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68` | 3,481,717 | none |
| 70 | `#22 AND #69` | 14,477 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Coronavirus Infections"[Mesh] OR "Quarantine"[Mesh] OR "COVID-19"[tiab] OR COVID19[tiab] OR "2019 novel coronavirus"[tiab] OR "novel coronavirus"[tiab] OR "SARS-CoV-2"[tiab] OR SARSCoV2[tiab] OR "2019-nCoV"[tiab] OR "2019 nCoV"[tiab] OR coronavirus*[tiab] OR lockdown*[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "shelter in place"[tiab] OR "social distancing"[tiab] OR quarantin*[tiab] OR confinement[tiab] OR "self-isolation"[tiab] OR "self isolation"[tiab] OR movement restrict*[tiab]) AND ("Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Feeding Behavior"[Mesh] OR "Sleep"[Mesh] OR "Mental Health"[Mesh] OR "Quality of Life"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR "Stress, Psychological"[Mesh] OR "Loneliness"[Mesh] OR "Personal Satisfaction"[Mesh] OR "Smoking"[Mesh] OR "Alcohol Drinking"[Mesh] OR lifestyle[tiab] OR "health behavior"[tiab] OR "health behaviors"[tiab] OR "health behaviour"[tiab] OR "health behaviours"[tiab] OR physical activit*[tiab] OR exercis*[tiab] OR sedentar*[tiab] OR "screen time"[tiab] OR "diet quality"[tiab] OR dietary[tiab] OR eating[tiab] OR "food consumption"[tiab] OR sleep[tiab] OR "sleep quality"[tiab] OR smoking[tiab] OR tobacco[tiab] OR alcohol[tiab] OR "substance use"[tiab] OR "mental health"[tiab] OR "psychological well-being"[tiab] OR "psychological wellbeing"[tiab] OR "well-being"[tiab] OR wellbeing[tiab] OR "quality of life"[tiab] OR "life satisfaction"[tiab] OR loneliness[tiab] OR anxiety[tiab] OR depress*[tiab] OR stress[tiab] OR distress[tiab] OR diet[tiab] OR "alcohol use"[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
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
| Lifestyle behaviors and well-being outcomes | AND-ed | 121,984 / 14,477 | 88.1% | none | 0/30 (up to 10% of removed records could be relevant) | AND the topic-defining outcomes block: the updated block reduces the COVID/restriction result count by 88.1% (121,984 to 14,477), loses none of the 9 screened relevant development records, and none of the refreshed 30-record loss sample met eligibility. The sample was screened by title and abstract; it consisted of old non-COVID material, clinical COVID studies, and non-empirical records. The block retains lifestyle and well-being outcomes as OR alternatives, including the explicitly named diet and alcohol use examples. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| COVID-19 and related lockdown or public health restrictions | 1 | `communicable disease[tiab] OR public health measure[tiab] OR movement restriction[tiab] OR stay at home[tiab]` | 5,741 | 0/30 |
| COVID-19 and related lockdown or public health restrictions | 2 | `Social Isolation[Mesh] OR Public Health Emergency[tiab] OR stay home orders[tiab] OR isolation[tiab] OR closure*[tiab]` | 37,775 | 0/30 |
| Lifestyle behaviors and well-being outcomes | 1 | `health[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR well-being[tiab]` | 28,495 | 0/30 |
| Lifestyle behaviors and well-being outcomes | 2 | `health[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR well-being[tiab] OR daily life[tiab]` | 21,713 | not screened |
| Lifestyle behaviors and well-being outcomes | 3 | `health[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR well-being[tiab] OR daily life[tiab]` | 21,713 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_context | 3,481,717 | 0 |
| lifestyle_wellbeing | 121,984 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 147,546 | initial | none | Initial exposure block plus optional outcome candidate, drafted from the question and MeSH/free-text vocabulary; no seeds were supplied. |
| 2 | 121,984 | covid_context: +1 / -3 | none | Removed generic pandemic indexing and standalone pandemic wording after the cutoff-bounded loss sample included many pre-COVID or out-of-scope records; retained COVID-specific terms and related lockdown wording. Corrected truncated phrase syntax. Added no seed terms; 9 screened pilot records are in the relevant development set. |
| 3 | 14,243 | lifestyle_wellbeing: +44 / -0 | none | Placed the topic-defining lifestyle/well-being outcome block in the strategy after its 30-record loss sample found no eligible record and it cut the current COVID/restriction result count by 88.3%; the 9 screened development records remain retrieved. |
| 4 | 121,984 | lifestyle_wellbeing: +0 / -44 | none | Corrected the outcome MeSH heading from the unrecognized Life Satisfaction label to the canonical Personal Satisfaction heading returned by NCBI; re-opening the outcome block candidate so its loss sample and optional decision can be refreshed. |
| 5 | 14,268 | lifestyle_wellbeing: +44 / -0 | none | Refreshed outcome decision after canonical MeSH correction; selected the outcome block using 0/30 relevant in the current loss sample and no known losses. |
| 6 | 121,984 | lifestyle_wellbeing: +0 / -44 | none | Addressed critic F1 by adding the bare-name terms diet[tiab] and alcohol use[tiab] to the optional outcome block. The block is re-opened as a candidate because this change invalidates its prior optional decision. |
| 7 | 14,477 | lifestyle_wellbeing: +46 / -0 | none | Re-evaluated after the critic's lexical repair; the refreshed optional outcome sample found no eligible removed records and the updated block remains AND-ed. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 1 findings; F1 must-fix open
- Round 2 on version 7: 1 findings; F1 must-fix resolved
- Round 3 on version 7: 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1905 NCBI requests logged (788 from cache); strategy sha256 84d3d5818ca5._

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
        "message": "14,477 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:covid_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-afe7e67af69d3bb89b5e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "14,477 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:covid_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-afe7e67af69d3bb89b5e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"Coronavirus Infections\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Quarantine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
        "text": "\"Sleep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Anxiety\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "requested": "Loneliness",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Loneliness\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Personal Satisfaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010549",
          "name": "Personal Satisfaction",
          "type": "descriptor",
          "scope_note": "The individual's experience of a sense of fulfillment of a need or want and the quality or state of being satisfied.",
          "tree_numbers": [
            "F01.145.677"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010549",
      "preferred_label": "Personal Satisfaction",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "\"Personal Satisfaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:38:58+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Coronavirus Infections\"[MeSH Terms] OR \"Quarantine\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARSCoV2\"[Title/Abstract] OR \"2019 ncov\"[Title/Abstract] OR \"2019 ncov\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter in place\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"confinement\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract] OR \"movement restrict*\"[Title/Abstract]) AND (\"Exercise\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"Mental Health\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Loneliness\"[MeSH Terms] OR \"Personal Satisfaction\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"health behavior\"[Title/Abstract] OR \"health behaviors\"[Title/Abstract] OR \"health behaviour\"[Title/Abstract] OR \"health behaviours\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentar*\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"diet quality\"[Title/Abstract] OR \"dietary\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"Sleep\"[Title/Abstract] OR \"sleep quality\"[Title/Abstract] OR \"Smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"psychological well-being\"[Title/Abstract] OR \"psychological wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"Loneliness\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"diet\"[Title/Abstract] OR \"alcohol use\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "f65047766623f52dd3aeba345f656e46f398c17a1271fa57a060629050ab10af",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The outcome block does not include the eligibility examples diet and alcohol use under their own bare names."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required exposure and optional outcome blocks are OR-combined internally and AND-combined; either behavior or well-being can qualify."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant headings are included for COVID-related infection and quarantine, lifestyle behaviors, and well-being outcomes."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The block includes dietary and alcohol, but not the eligibility examples diet and alcohol use as bare expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported translation has no syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, language, geography, age, or study-design limits are applied. The stated Entrez-date cutoff is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria name diet and alcohol use, but the outcome block contains dietary and alcohol rather than those named expressions. The translation check requires each named member of a searched concept to be covered by its own bare name.",
          "recommendation": "Add explicit bare-name expressions such as diet[tiab] and alcohol use[tiab], then run another complete evaluation of the revised strategy.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final count remains above the stated workload budget, but the only optional searchable concept was tested as an AND-ed block and reduced the count substantially. The resulting count is a documented workload risk.",
          "evidence": "The lifestyle and well-being block reduced results from 121,984 to 14,268 (88.3%); none of nine known relevant development records were lost and 0/30 sampled removed records were relevant. The final count of 14,268 still exceeds the 10,000-record budget."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 7,
      "review_sha256": "65ef341780f4d10068b3ee6e94a9a52df63e177b55cdf3ac3208a39d197fb31a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The current outcome block includes diet[tiab] and \"alcohol use\"[tiab] as standalone expressions, addressing the named eligibility examples."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are OR-combined, the lifestyle and well-being outcomes are OR-combined, and the two blocks are AND-combined. Either eligible outcome type can qualify."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant MeSH headings cover coronavirus infection, quarantine, lifestyle behaviors, and well-being outcomes."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current text-word block covers the named examples, including diet and alcohol use, alongside the other listed behavior and well-being terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current PubMed translation reports no syntax errors, translation issues, or warning list."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, language, geography, age, or study-design filters are applied. The Entrez-date cutoff is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The earlier version omitted diet and alcohol use as their own expressions.",
          "recommendation": "Add diet[tiab] and \"alcohol use\"[tiab], then run a complete evaluation.",
          "status": "resolved",
          "response": "The current version includes both expressions, and the complete version 7 evaluation retains all nine known relevant development records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the documented workload risk: the final count remains above the 10,000-record budget after testing the only optional searchable concept as an AND-ed block.",
          "evidence": "The outcome block reduced results from 121,984 to 14,477 (88.1%); no known relevant development records were lost and 0/30 sampled removed records met eligibility."
        },
        {
          "issue_id": "I-afe7e67af69d3bb89b5e",
          "status": "accepted-risk",
          "response": "Accept the remaining uncertainty because the COVID-context block changed after its latest probe and the probe budget is spent; the prior sample cannot establish coverage for the current block.",
          "evidence": "Two earlier probes sampled 30 records each and found none eligible, but the warning identifies the COVID-context probe as stale. No current-block probe evidence is available."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 7,
      "review_sha256": "65ef341780f4d10068b3ee6e94a9a52df63e177b55cdf3ac3208a39d197fb31a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block now includes the named examples diet and alcohol use as standalone expressions, alongside the other eligible behavior and well-being outcomes."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms are OR-combined, outcome terms are OR-combined, and the two blocks are AND-combined, allowing either eligible outcome type."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant MeSH headings cover coronavirus infection, quarantine, lifestyle behaviors, and well-being outcomes."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover the named lifestyle and well-being examples, including diet and alcohol use."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported translation has no syntax errors, translation issues, or warning list."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, language, geography, age, or study-design limits are applied; the Entrez-date cutoff is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The earlier version omitted diet and alcohol use as their own expressions.",
          "recommendation": "Add diet[tiab] and \"alcohol use\"[tiab], then run a complete evaluation.",
          "status": "resolved",
          "response": "The current version includes both expressions, and the complete version 7 evaluation retains all nine known relevant development records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the documented workload risk: the final count remains above the 10,000-record budget after testing the only optional searchable concept as an AND-ed block.",
          "evidence": "The outcome block reduced results from 121,984 to 14,477 (88.1%); no known relevant development records were lost and 0/30 sampled removed records met eligibility."
        },
        {
          "issue_id": "I-afe7e67af69d3bb89b5e",
          "status": "accepted-risk",
          "response": "Accept the remaining uncertainty because the COVID-context block changed after its latest probe and the probe budget is spent; the prior sample cannot establish coverage for the current block.",
          "evidence": "Two earlier probes sampled 30 records each and found none eligible, but the warning identifies the COVID-context probe as stale. No current-block probe evidence is available."
        }
      ]
    }
  ]
}
```


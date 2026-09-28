# PubMed search strategy: audit

Generated 2026-09-28T13:45:39+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without clarification. Assumed PECO with COVID-19 pandemic/lockdown disruption as the required exposure and the combined lifestyle behavior/well-being family as optional for empirical testing. Either lifestyle behavior or well-being qualifies at screening; no age, language, geography, design, or publication-date limits. Database snapshot is bounded by Entrez date 2020-11-22 via PSB_AS_OF for every command; no [dp] limit. No known relevant articles were supplied. Standard-depth discovery will be attempted, subject to PubMed availability and the approximately 150-record screening budget.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The pandemic and its control measures are the exposure defining the question, and are searchable by names for COVID-19, SARS-CoV-2, pandemic and lockdown restrictions. |
| Lifestyle behaviors and well-being | optional | These are topic-defining outcomes that authors often name but may report inconsistently; test a broad outcome block and a screened loss sample before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T13:44:02+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 82,131
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"COVID-19"[Mesh]` | 57,089 | none |
| 2 | `"Coronavirus Infections"[Mesh]` | 67,535 | none |
| 3 | `"SARS-CoV-2"[Mesh]` | 45,931 | none |
| 4 | `COVID-19[tiab]` | 67,388 | none |
| 5 | `COVID19[tiab]` | 64,206 | none |
| 6 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 7 | `SARS-CoV2[tiab]` | 1,049 | none |
| 8 | `2019-nCoV[tiab]` | 1,288 | none |
| 9 | `coronavirus[tiab]` | 41,791 | none |
| 10 | `pandemic*[tiab]` | 58,444 | none |
| 11 | `restriction*[tiab]` | 198,508 | none |
| 12 | `lockdown*[tiab]` | 3,416 | none |
| 13 | `quarantin*[tiab]` | 6,954 | none |
| 14 | `confinement[tiab]` | 20,190 | none |
| 15 | `stay-at-home[tiab]` | 815 | none |
| 16 | `"social distancing"[tiab:~1]` | 2,679 | none |
| 17 | `"physical distancing"[tiab:~1]` | 446 | none |
| 18 | `"stay at home"[tiab:~2]` | 912 | none |
| 19 | `"shelter in place"[tiab:~2]` | 215 | none |
| 20 | `"movement restriction"[tiab:~2]` | 866 | none |
| 21 | `"school closure"[tiab:~1]` | 254 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 340,954 | none |
| 23 | `"Life Style"[Mesh]` | 99,996 | none |
| 24 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 25 | `"Exercise"[Mesh]` | 212,859 | none |
| 26 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 27 | `"Screen Time"[Mesh]` | 608 | none |
| 28 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 29 | `"Eating"[Mesh]` | 75,131 | none |
| 30 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 31 | `"Smoking"[Mesh]` | 152,983 | none |
| 32 | `"Mental Health"[Mesh]` | 44,674 | none |
| 33 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 34 | `"Anxiety Disorders"[Mesh]` | 83,410 | none |
| 35 | `"Depressive Disorder"[Mesh]` | 113,641 | none |
| 36 | `"Quality of Life"[Mesh]` | 215,482 | none |
| 37 | `lifestyle[tiab]` | 99,644 | none |
| 38 | `"life style"[tiab]` | 11,282 | none |
| 39 | `behavior*[tiab]` | 1,024,043 | none |
| 40 | `behaviour*[tiab]` | 293,760 | none |
| 41 | `"health behavior"[tiab:~1]` | 13,664 | none |
| 42 | `"health behaviour"[tiab:~1]` | 7,104 | none |
| 43 | `"physical activity"[tiab:~1]` | 115,542 | none |
| 44 | `exercise*[tiab]` | 304,257 | none |
| 45 | `"sedentary behavior"[tiab:~1]` | 4,105 | none |
| 46 | `"sedentary behaviour"[tiab:~1]` | 2,214 | none |
| 47 | `sedentar*[tiab]` | 33,160 | none |
| 48 | `inactiv*[tiab]` | 308,257 | none |
| 49 | `"screen time"[tiab:~1]` | 2,786 | none |
| 50 | `"television viewing"[tiab:~1]` | 1,585 | none |
| 51 | `"dietary behavior"[tiab:~1]` | 1,288 | none |
| 52 | `"dietary behaviour"[tiab:~1]` | 668 | none |
| 53 | `diet*[tiab]` | 587,723 | none |
| 54 | `eating[tiab]` | 77,769 | none |
| 55 | `eats[tiab]` | 548 | none |
| 56 | `feeding[tiab]` | 202,365 | none |
| 57 | `nutrition*[tiab]` | 299,576 | none |
| 58 | `"food consumption"[tiab:~1]` | 16,295 | none |
| 59 | `"food intake"[tiab:~1]` | 48,631 | none |
| 60 | `sleep*[tiab]` | 188,562 | none |
| 61 | `insomnia[tiab]` | 22,051 | none |
| 62 | `"sleep quality"[tiab:~1]` | 17,830 | none |
| 63 | `smok*[tiab]` | 287,931 | none |
| 64 | `tobacco[tiab]` | 104,259 | none |
| 65 | `alcohol[tiab]` | 263,050 | none |
| 66 | `drinking[tiab]` | 114,398 | none |
| 67 | `substance use[tiab]` | 37,851 | none |
| 68 | `cannabis[tiab]` | 18,505 | none |
| 69 | `wellbeing[tiab]` | 91,505 | none |
| 70 | `"well being"[tiab:~1]` | 86,423 | none |
| 71 | `"mental health"[tiab:~1]` | 161,078 | none |
| 72 | `"psychological health"[tiab:~1]` | 7,710 | none |
| 73 | `"psychological well-being"[tiab:~1]` | 10,142 | none |
| 74 | `"psychological wellbeing"[tiab:~1]` | 2,255 | none |
| 75 | `"quality of life"[tiab:~1]` | 286,598 | none |
| 76 | `"social well-being"[tiab:~1]` | 3,130 | none |
| 77 | `"social wellbeing"[tiab:~1]` | 617 | none |
| 78 | `psychosocial[tiab]` | 102,025 | none |
| 79 | `distress[tiab]` | 119,022 | none |
| 80 | `anxiet*[tiab]` | 201,789 | none |
| 81 | `depress*[tiab]` | 474,400 | none |
| 82 | `stress[tiab]` | 779,146 | none |
| 83 | `loneliness[tiab]` | 6,825 | none |
| 84 | `lonely[tiab]` | 1,688 | none |
| 85 | `emotional[tiab]` | 159,221 | none |
| 86 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85` | 5,348,262 | none |
| 87 | `#22 AND #86` | 82,131 | none |

### Strategy (single line, for copying into PubMed)

```text
(("COVID-19"[Mesh] OR "Coronavirus Infections"[Mesh] OR "SARS-CoV-2"[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR SARS-CoV-2[tiab] OR SARS-CoV2[tiab] OR 2019-nCoV[tiab] OR coronavirus[tiab] OR pandemic*[tiab] OR restriction*[tiab] OR lockdown*[tiab] OR quarantin*[tiab] OR confinement[tiab] OR stay-at-home[tiab] OR "social distancing"[tiab:~1] OR "physical distancing"[tiab:~1] OR "stay at home"[tiab:~2] OR "shelter in place"[tiab:~2] OR "movement restriction"[tiab:~2] OR "school closure"[tiab:~1]) AND ("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Screen Time"[Mesh] OR "Feeding Behavior"[Mesh] OR "Eating"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Smoking"[Mesh] OR "Mental Health"[Mesh] OR "Stress, Psychological"[Mesh] OR "Anxiety Disorders"[Mesh] OR "Depressive Disorder"[Mesh] OR "Quality of Life"[Mesh] OR lifestyle[tiab] OR "life style"[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR "health behavior"[tiab:~1] OR "health behaviour"[tiab:~1] OR "physical activity"[tiab:~1] OR exercise*[tiab] OR "sedentary behavior"[tiab:~1] OR "sedentary behaviour"[tiab:~1] OR sedentar*[tiab] OR inactiv*[tiab] OR "screen time"[tiab:~1] OR "television viewing"[tiab:~1] OR "dietary behavior"[tiab:~1] OR "dietary behaviour"[tiab:~1] OR diet*[tiab] OR eating[tiab] OR eats[tiab] OR feeding[tiab] OR nutrition*[tiab] OR "food consumption"[tiab:~1] OR "food intake"[tiab:~1] OR sleep*[tiab] OR insomnia[tiab] OR "sleep quality"[tiab:~1] OR smok*[tiab] OR tobacco[tiab] OR alcohol[tiab] OR drinking[tiab] OR substance use[tiab] OR cannabis[tiab] OR wellbeing[tiab] OR "well being"[tiab:~1] OR "mental health"[tiab:~1] OR "psychological health"[tiab:~1] OR "psychological well-being"[tiab:~1] OR "psychological wellbeing"[tiab:~1] OR "quality of life"[tiab:~1] OR "social well-being"[tiab:~1] OR "social wellbeing"[tiab:~1] OR psychosocial[tiab] OR distress[tiab] OR anxiet*[tiab] OR depress*[tiab] OR stress[tiab] OR loneliness[tiab] OR lonely[tiab] OR emotional[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being | AND-ed | 340,954 / 82,131 | 75.9% | none | 0/30 (up to 10% of removed records could be relevant) | Retain the lifestyle/wellbeing block: it reduces the current exposure-only set from 340954 to 82131 (75.9%) and retains all 10 known eligible records; none of 30 sampled and screened exposure-only records was eligible. Search remains above the standard 10000 workload budget, accepted as a sensitivity-first tradeoff. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_disruption | 5,348,262 | 0 |
| lifestyle_wellbeing | 340,954 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 568,166 | initial | none | Initial high-sensitivity draft: COVID/pandemic/lockdown exposure as required; broad lifestyle and well-being vocabulary is an optional block to measure workload and loss. |
| 2 | 120,791 | covid_disruption: +1 / -8 | none | Removed generic pandemic, epidemic, outbreak, and isolation-only exposure terms after the optional-loss sample returned historical non-COVID records; retained COVID-specific MeSH/text plus lockdown and distancing labels. |
| 3 | 0 | lifestyle_wellbeing: +63 / -0 | none | AND-ed the optional lifestyle/well-being block after its required 30-record loss sample contained no relevant records; material count reduction and no known losses. |
| 4 | 21,367 | lifestyle_wellbeing: +64 / -0 | none | Fixed the PubMed short-wildcard lint error by enumerating eating/eats instead of eat*; recall-first wording retained. |
| 5 | 21,367 | lifestyle_wellbeing: +0 / -1 | none | Removed the MeSH heading Psychological Well-Being because PSB showed it was introduced in 2023 and returned zero records under the 2020-11-22 Entrez bound; title/abstract well-being terms remain. Replaced the invalid eat* wildcard with eating/eats variants. |
| 6 | 82,131 | covid_disruption: +2 / -0 | none | Added explicit pandemic* and restriction* title/abstract terms in response to the internal critic; all existing known records should remain covered, but recheck outcome-block losses and count. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 2 findings; R1-F1 must-fix open, R1-F2 must-fix open
- Round 2 on version 6: 2 findings; R1-F1 must-fix resolved, R1-F2 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1748 NCBI requests logged (686 from cache); strategy sha256 9be177553f9d._

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
        "message": "82,131 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "82,131 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
        "text": "\"Coronavirus Infections\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "SARS-CoV-2",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"SARS-CoV-2\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Screen Time",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Screen Time\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Eating",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Eating\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001008",
          "name": "Anxiety Disorders",
          "type": "descriptor",
          "scope_note": "Persistent and disabling ANXIETY.",
          "tree_numbers": [
            "F03.080"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001008",
      "preferred_label": "Anxiety Disorders",
      "type": "descriptor",
      "location": "vocabulary:33",
      "term": {
        "text": "\"Anxiety Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003866",
          "name": "Depressive Disorder",
          "type": "descriptor",
          "scope_note": "An affective disorder manifested by either a dysphoric mood or loss of interest or pleasure in usual activities. The mood disturbance is prominent and relatively persistent.",
          "tree_numbers": [
            "F03.600.300"
          ],
          "entry_terms": 20,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003866",
      "preferred_label": "Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "\"Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:44:02+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"Coronavirus Infections\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"coronavirus\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"restriction*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"confinement\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"social distancing\"[Title/Abstract:~1] OR \"physical distancing\"[Title/Abstract:~1] OR \"stay-at-home\"[Title/Abstract:~2] OR \"shelter in place\"[Title/Abstract:~2] OR \"movement restriction\"[Title/Abstract:~2] OR \"school closure\"[Title/Abstract:~1]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Screen Time\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Eating\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Mental Health\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Anxiety Disorders\"[MeSH Terms] OR \"Depressive Disorder\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"Life Style\"[Title/Abstract] OR \"behavior*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract] OR \"Health Behavior\"[Title/Abstract:~1] OR \"health behaviour\"[Title/Abstract:~1] OR \"physical activity\"[Title/Abstract:~1] OR \"exercise*\"[Title/Abstract] OR \"Sedentary Behavior\"[Title/Abstract:~1] OR \"sedentary behaviour\"[Title/Abstract:~1] OR \"sedentar*\"[Title/Abstract] OR \"inactiv*\"[Title/Abstract] OR \"Screen Time\"[Title/Abstract:~1] OR \"television viewing\"[Title/Abstract:~1] OR \"dietary behavior\"[Title/Abstract:~1] OR \"dietary behaviour\"[Title/Abstract:~1] OR \"diet*\"[Title/Abstract] OR \"Eating\"[Title/Abstract] OR \"eats\"[Title/Abstract] OR \"feeding\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"food consumption\"[Title/Abstract:~1] OR \"food intake\"[Title/Abstract:~1] OR \"sleep*\"[Title/Abstract] OR \"insomnia\"[Title/Abstract] OR \"sleep quality\"[Title/Abstract:~1] OR \"smok*\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"cannabis\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"well being\"[Title/Abstract:~1] OR \"Mental Health\"[Title/Abstract:~1] OR \"psychological health\"[Title/Abstract:~1] OR \"psychological well-being\"[Title/Abstract:~1] OR \"psychological wellbeing\"[Title/Abstract:~1] OR \"Quality of Life\"[Title/Abstract:~1] OR \"social well-being\"[Title/Abstract:~1] OR \"social wellbeing\"[Title/Abstract:~1] OR \"psychosocial\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"anxiet*\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"lonely\"[Title/Abstract] OR \"emotional\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "692d06b45073c550e5c8367e6fe268daafe1f28f6832d773447fb86c5dcf255c",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The exposure block covers COVID-19 and several control measures but lacks the bare names pandemic and restriction, which the question and concept rationale identify."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks use OR within concepts and AND between concepts; no restrictive NOT clause is present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant MeSH headings are included for COVID-19 and the named lifestyle and well-being outcomes; the packet reports no translation errors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add explicit bare-name coverage for pandemic and restriction in the exposure block. The named outcome examples are represented in the current terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query parsed with no errors or translation issues in the supplied evidence."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The query is limited to records entered through 2020-11-22, but the question and eligibility provide no end date or rationale for that cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "block": "covid_disruption",
          "finding": "The searched exposure concept names the COVID-19 pandemic and lockdown restrictions, but the block has no standalone pandemic term and represents restriction only in the phrase movement restriction.",
          "recommendation": "Add and test explicit bare-name terms such as pandemic[tiab] and restriction*[tiab], then rerun the complete evaluation.",
          "status": "open"
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an entry-date cutoff of 2020-11-22. No such date limit appears in the question or eligibility, so later eligible studies would be excluded.",
          "recommendation": "Remove the entry-date limit unless the review protocol supplies and justifies a date boundary; then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains valid: the final count of 21,367 exceeds the 10,000-record budget. The optional outcome block was tested and AND-ed, reducing retrieval by 82.3%; the loss sample found 0 relevant records among 30 and all 10 known records were retained. Accept the excess workload provisionally to retain broad outcome coverage, while recognizing that the small loss sample does not rule out missed eligible records.",
          "evidence": "Packet reports 120,791 records without and 21,367 with the outcome block, 0/30 relevant in the loss sample, and 10/10 known records retrieved."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "8bae7ff84528275d9240d95dc331cd713c7092373ef495b214d35376c46c8924",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block now includes standalone pandemic*[tiab] and restriction*[tiab] terms, addressing the prior missing bare-name coverage."
        },
        "operators": {
          "verdict": "pass",
          "note": "The terms are OR-combined within each concept block and the two blocks are AND-combined. No restrictive NOT clause is present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant COVID-19 and lifestyle or well-being MeSH headings are included alongside text-word coverage."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the named exposure and outcome concepts, including pandemic, restrictions, physical activity, diet, sleep, smoking, alcohol, and well-being."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied diagnostics report no syntax or translation errors. The proximity expressions contain no wildcards, and no phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The date recommendation is rejected because the user and harness explicitly require the PubMed/Entrez snapshot to be pinned as if 2020-11-22 for every PSB command. The effective restriction is an Entrez entry-date bound, not a publication-date filter; no [dp] limit is present."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The earlier concern about missing standalone pandemic and restriction terms is addressed in version 6 by pandemic*[tiab] and restriction*[tiab].",
          "recommendation": "No further change for this finding.",
          "status": "resolved",
          "response": "Both bare-name terms are present and tested in the current exposure block; evaluation found no loss among the 10 known eligible records."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The strategy applies an entry-date cutoff of 2020-11-22. The independent reviewer recommended removing it, but the harness instruction requires this historical snapshot for every PubMed command.",
          "recommendation": "No strategy change: retain the required PSB_AS_OF bound for this run, and do not add a publication-date filter.",
          "status": "rejected",
          "response": "The cutoff is an explicit task constraint: PubMed is pinned as if 2020-11-22 and PSB_AS_OF must remain set for every command. This is not an arbitrary review eligibility limit. It uses Entrez entry date and avoids [dp], as required, so the reviewer recommendation cannot be followed within this run."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the excess workload provisionally: the outcome block is the only tested optional concept, was AND-ed, and the stated rationale prioritizes sensitivity. The remaining search exceeds the workload budget substantially, so this is a documented tradeoff.",
          "evidence": "The current search returns 82,131 records against a 10,000-record budget. The outcome block reduces the exposure-only set from 340,954 by 75.9%; all 10 known eligible records are retained and 0 of 30 sampled removed records were eligible."
        }
      ]
    }
  ]
}
```


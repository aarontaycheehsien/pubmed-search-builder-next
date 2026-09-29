# PubMed search strategy: audit

Generated 2026-09-29T20:21:09+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User requested no questions during this run; proceeded with the stated interpretation. Assumed any human population and any one eligible lifestyle behavior or well-being outcome qualifies. The exposure includes broad COVID-19 pandemic context and related restrictions; specific policy terms are screening context, not a required sub-block. No language or publication-date limit; PSB_AS_OF and protocol entry-date bound are 2020-11-22 and no [dp] restriction is used. No user-supplied known records. PubMed-only review and pilot discovery were screened; 15 relevant records were retained as development checks. The optional outcome block loss sample screened 30 records, with none eligible. No independent validation or benchmark set was available.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related restrictions | search | COVID-19-specific wording defines the required exposure and is searched broadly. Lockdown, stay-at-home, quarantine, confinement, isolation, and distancing are within the screening scope but are not individually required, because relevant studies may assess pandemic-era effects without naming a particular policy. |
| Lifestyle behaviors and well-being | optional | These topic-defining outcomes are usually searchable but may be absent from records describing population-level pandemic effects; test a comprehensive outcome block before deciding whether to AND it. |
| Human populations affected by COVID-19 | screen | No age, country or risk subgroup is specified; population details are screened and no population block is justified. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T20:19:46+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 12,854
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"COVID-19"[Mesh]` | 57,089 | none |
| 2 | `"SARS-CoV-2"[Mesh]` | 45,931 | none |
| 3 | `"Pandemics"[Mesh]` | 50,277 | none |
| 4 | `COVID-19[tiab]` | 67,388 | none |
| 5 | `COVID19[tiab]` | 64,206 | none |
| 6 | `COVID[tiab]` | 67,980 | none |
| 7 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 8 | `SARS CoV 2[tiab]` | 23,503 | none |
| 9 | `2019-nCoV[tiab]` | 1,288 | none |
| 10 | `2019 nCoV[tiab]` | 1,288 | none |
| 11 | `"2019 novel coronavirus"[tiab]` | 1,176 | none |
| 12 | `"novel coronavirus 2019"[tiab]` | 576 | none |
| 13 | `"coronavirus disease 2019"[tiab]` | 14,613 | none |
| 14 | `"COVID-19 pandemic"[tiab]` | 20,381 | none |
| 15 | `"coronavirus pandemic"[tiab]` | 1,011 | none |
| 16 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 83,452 | none |
| 17 | `"Life Style"[Mesh]` | 99,996 | none |
| 18 | `"Healthy Lifestyle"[Mesh]` | 8,656 | none |
| 19 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 20 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 21 | `"Exercise"[Mesh]` | 212,859 | none |
| 22 | `"Diet"[Mesh]` | 296,758 | none |
| 23 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 24 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 25 | `"Smoking"[Mesh]` | 152,983 | none |
| 26 | `"Sleep"[Mesh]` | 85,169 | none |
| 27 | `"Mental Health"[Mesh]` | 44,674 | none |
| 28 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 29 | `"Anxiety"[Mesh]` | 93,320 | none |
| 30 | `"Depression"[Mesh]` | 129,618 | none |
| 31 | `"Quality of Life"[Mesh]` | 215,482 | none |
| 32 | `"Social Isolation"[Mesh]` | 22,365 | none |
| 33 | `lifestyle[tiab]` | 99,644 | none |
| 34 | `"life style"[tiab]` | 11,282 | none |
| 35 | `"health behavior"[tiab]` | 9,149 | none |
| 36 | `"health behaviours"[tiab]` | 3,546 | none |
| 37 | `"health behaviors"[tiab]` | 11,055 | none |
| 38 | `"lifestyle behavior"[tiab]` | 575 | none |
| 39 | `"lifestyle behaviours"[tiab]` | 942 | none |
| 40 | `"lifestyle behaviors"[tiab]` | 2,141 | none |
| 41 | `"behavioral change"[tiab]` | 3,662 | none |
| 42 | `"behavioural change"[tiab]` | 1,861 | none |
| 43 | `"physical activity"[tiab]` | 114,494 | none |
| 44 | `exercis*[tiab]` | 307,828 | none |
| 45 | `sedentary[tiab]` | 32,472 | none |
| 46 | `"sitting time"[tiab]` | 1,295 | none |
| 47 | `diet*[tiab]` | 587,723 | none |
| 48 | `"eating habit"[tiab]` | 189 | none |
| 49 | `nutrition*[tiab]` | 299,576 | none |
| 50 | `"food consumption"[tiab]` | 14,333 | none |
| 51 | `sleep[tiab]` | 171,185 | none |
| 52 | `insomnia[tiab]` | 22,051 | none |
| 53 | `alcohol[tiab]` | 263,050 | none |
| 54 | `smoking[tiab]` | 228,902 | none |
| 55 | `tobacco[tiab]` | 104,259 | none |
| 56 | `"substance use"[tiab]` | 37,851 | none |
| 57 | `wellbeing[tiab]` | 91,505 | none |
| 58 | `well-being[tiab]` | 80,676 | none |
| 59 | `wellness[tiab]` | 10,646 | none |
| 60 | `"mental health"[tiab]` | 159,665 | none |
| 61 | `"psychological well-being"[tiab]` | 9,542 | none |
| 62 | `"psychological distress"[tiab]` | 20,154 | none |
| 63 | `"quality of life"[tiab]` | 282,526 | none |
| 64 | `"life satisfaction"[tiab]` | 8,062 | none |
| 65 | `anxiety[tiab]` | 199,917 | none |
| 66 | `depression[tiab]` | 348,632 | none |
| 67 | `stress[tiab]` | 779,147 | none |
| 68 | `mood[tiab]` | 76,259 | none |
| 69 | `loneliness[tiab]` | 6,825 | none |
| 70 | `"social isolation"[tiab]` | 7,931 | none |
| 71 | `"sense of coherence"[tiab]` | 2,143 | none |
| 72 | `"daily routine"[tiab]` | 3,308 | none |
| 73 | `distress[tiab]` | 119,022 | none |
| 74 | `#17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73` | 3,916,582 | none |
| 75 | `#16 AND #74` | 12,854 | none |

### Strategy (single line, for copying into PubMed)

```text
(("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR "Pandemics"[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR COVID[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR 2019-nCoV[tiab] OR 2019 nCoV[tiab] OR "2019 novel coronavirus"[tiab] OR "novel coronavirus 2019"[tiab] OR "coronavirus disease 2019"[tiab] OR "COVID-19 pandemic"[tiab] OR "coronavirus pandemic"[tiab]) AND ("Life Style"[Mesh] OR "Healthy Lifestyle"[Mesh] OR "Health Behavior"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Exercise"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Smoking"[Mesh] OR "Sleep"[Mesh] OR "Mental Health"[Mesh] OR "Stress, Psychological"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR "Quality of Life"[Mesh] OR "Social Isolation"[Mesh] OR lifestyle[tiab] OR "life style"[tiab] OR "health behavior"[tiab] OR "health behaviours"[tiab] OR "health behaviors"[tiab] OR "lifestyle behavior"[tiab] OR "lifestyle behaviours"[tiab] OR "lifestyle behaviors"[tiab] OR "behavioral change"[tiab] OR "behavioural change"[tiab] OR "physical activity"[tiab] OR exercis*[tiab] OR sedentary[tiab] OR "sitting time"[tiab] OR diet*[tiab] OR "eating habit"[tiab] OR nutrition*[tiab] OR "food consumption"[tiab] OR sleep[tiab] OR insomnia[tiab] OR alcohol[tiab] OR smoking[tiab] OR tobacco[tiab] OR "substance use"[tiab] OR wellbeing[tiab] OR well-being[tiab] OR wellness[tiab] OR "mental health"[tiab] OR "psychological well-being"[tiab] OR "psychological distress"[tiab] OR "quality of life"[tiab] OR "life satisfaction"[tiab] OR anxiety[tiab] OR depression[tiab] OR stress[tiab] OR mood[tiab] OR loneliness[tiab] OR "social isolation"[tiab] OR "sense of coherence"[tiab] OR "daily routine"[tiab] OR distress[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 15 | 15 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being | AND-ed | 83,452 / 12,854 | 84.6% | none | 0/30 (up to 10% of removed records could be relevant) | After adding distress[tiab] to cover an explicit eligible outcome, the refreshed loss sample was screened and none of its 30 records met the scope. The revised block retained all 15 screened relevant development records and reduced the COVID-context set from 83,452 to 12,854 (84.6%). It remains 2,854 over the standard 10,000-record budget; accept this workload risk for critic review rather than adding an unsupported population block. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_context | 3,916,582 | 0 |
| outcomes | 83,452 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 83,452 | initial | none | Initial strategy uses COVID-19 pandemic context as required and evaluates lifestyle/well-being outcomes as an optional block; outcome vocabulary combines MeSH headings and title/abstract terms. |
| 2 | 10,582 | outcomes: +56 / -0 | none | Promoted the outcome candidate to an AND block after its measured 87.3% reduction, complete retrieval of 15 screened relevant records, and a 0/30 relevant optional-loss sample; kept the small residual workload overrun explicit for critic review. |
| 3 | 12,854 | outcomes: +1 / -0 | none | Added bare distress[tiab] per the internal critic because distress is an explicit eligibility outcome. Recorded the required 2020-11-22 PubMed entry-date cutoff in protocol.as_of; retained no publication-date [dp] limit. Outcome block changed, so its loss-sample decision must be refreshed. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-01 must-fix open, R1-02 must-fix open
- Round 2 on version 3: 2 findings; R1-01 must-fix resolved, R1-02 must-fix rejected
- Round 3 on version 3: 2 findings; R1-01 must-fix resolved, R1-02 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1697 NCBI requests logged (719 from cache); strategy sha256 46f23bd18f1b._

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
        "message": "12,854 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "12,854 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Healthy Lifestyle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "\"Healthy Lifestyle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "checked_at": "2026-09-29T20:19:46+00:00",
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
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:19:46+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Social Isolation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"Pandemics\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"COVID\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus 2019\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"COVID-19 pandemic\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract]) AND (\"Life Style\"[MeSH Terms] OR \"Healthy Lifestyle\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"Mental Health\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"Social Isolation\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"Life Style\"[Title/Abstract] OR \"Health Behavior\"[Title/Abstract] OR \"health behaviours\"[Title/Abstract] OR \"health behaviors\"[Title/Abstract] OR \"lifestyle behavior\"[Title/Abstract] OR \"lifestyle behaviours\"[Title/Abstract] OR \"lifestyle behaviors\"[Title/Abstract] OR \"behavioral change\"[Title/Abstract] OR \"behavioural change\"[Title/Abstract] OR \"physical activity\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting time\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating habit\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"Sleep\"[Title/Abstract] OR \"insomnia\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"Smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"wellness\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"psychological well-being\"[Title/Abstract] OR \"psychological distress\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"Depression\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"mood\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"Social Isolation\"[Title/Abstract] OR \"sense of coherence\"[Title/Abstract] OR \"daily routine\"[Title/Abstract] OR \"distress\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "28a75cbe99d830c107469d17d953ea6d580d6d4307f0ff48a8fec5e148b3ffc8",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility criteria name distress as an outcome, but the text-word block searches only the narrower phrase psychological distress."
        },
        "operators": {
          "verdict": "pass",
          "note": "The COVID context and outcome blocks are combined with AND, and terms within each block are combined with OR. No operator issue is evident."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant COVID-19, lifestyle, behavior, and well-being MeSH headings. The supplied translation shows them mapped as MeSH terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add the bare text word distress to cover an outcome explicitly named in the eligibility criteria."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed query has balanced grouping and valid field tags; the packet reports no syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final query limits entry dates to 2020-11-22, but the question and eligibility criteria specify no end date. This excludes later COVID-19 evidence without a stated scope rationale."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria explicitly include distress, but the outcome block contains only the phrase psychological distress and does not search distress by its bare name.",
          "recommendation": "Add distress[tiab] to the outcome block and rerun the complete evaluation.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an entry-date limit from 1800-01-01 through 2020-11-22. No date cutoff appears in the review question or eligibility criteria, so the filter excludes later pandemic evidence without a stated justification.",
          "recommendation": "Remove the entry-date limit unless the review scope is explicitly restricted to records entered by 2020-11-22, then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The strategy tested the only searchable optional outcome concept and found that AND-ing it retained all 15 development records and yielded no eligible records in the 30-record loss sample. The remaining count is 582 above budget; accept that workload risk rather than adding an unsupported population block.",
          "evidence": "The scope says population details are screened and no population block is justified. The optional-concept evaluation reports 10,582 results after the outcome block, against a 10,000-record budget, with all 15 known relevant development records retained and 0/30 sampled losses relevant."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "b4d84abe05ec429a05b72098d7df9be236ee3c9a9895426dda837fa8495dd715",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block includes distress[tiab] by its bare name, covering the explicitly eligible outcome. Specific restriction wording is screening context rather than a required search sub-block."
        },
        "operators": {
          "verdict": "pass",
          "note": "COVID context and outcomes are combined with AND, and terms within each block are combined with OR, consistent with the stated concept roles."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant COVID-19, lifestyle, behavior, and well-being MeSH headings, which the supplied translations map as MeSH terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word block covers the listed lifestyle and well-being outcomes and searches distress independently of the narrower phrase psychological distress."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current query has balanced grouping, and the packet reports no syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date cutoff is explicitly required by the user's simulated-date instruction and is recorded as protocol.as_of. It is not a publication-date [dp] filter."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria explicitly include distress, but the earlier outcome block searched only the narrower phrase psychological distress.",
          "recommendation": "Add distress[tiab] to the outcome block and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current outcome block includes distress[tiab], and the packet records a fresh complete evaluation."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an entry-date limit from 1800-01-01 through 2020-11-22. No date cutoff appears in the review question or eligibility criteria, so this excludes later pandemic evidence without a stated justification.",
          "recommendation": "Remove the entry-date limit unless the review scope is explicitly restricted to records entered by 2020-11-22, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "Rejected because the user explicitly instructed that this run represent literature in PubMed by 2020-11-22 and that PSB_AS_OF remain set for every command. The same entry-date cutoff is now recorded in protocol.as_of. Removing it would violate the requested run frame. This is an Entrez entry-date bound, not a publication-date [dp] limit."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the remaining workload above budget for critic review. The searchable optional outcome concept was tested as an AND-ed block; all 15 development records were retained and no relevant records appeared among the 30 sampled losses. Population details remain screened because the question specifies no target subgroup.",
          "evidence": "The current evaluation reduces the COVID-context set from 83,452 to 12,854, retains all 15 screened relevant development records, and reports 0/30 relevant in the refreshed loss sample. The final count exceeds the 10,000-record budget by 2,854."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "b4d84abe05ec429a05b72098d7df9be236ee3c9a9895426dda837fa8495dd715",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block searches distress[tiab] by its bare name, covering the explicitly eligible outcome. Restriction wording is within screening scope and is not individually required in the search."
        },
        "operators": {
          "verdict": "pass",
          "note": "COVID context and outcomes are combined with AND, with terms within each block combined with OR, consistent with the stated concept roles."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant COVID-19, lifestyle, behavior, and well-being MeSH headings are present and mapped as MeSH terms in the supplied translation."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The outcome text-word block covers the listed lifestyle and well-being outcomes and includes distress independently of the narrower phrase psychological distress."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current query has balanced grouping, and the packet reports no syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff is required by the simulated-date instruction and recorded as protocol.as_of; it is an Entrez entry-date bound, not a publication-date filter."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria explicitly include distress, but the earlier outcome block searched only the narrower phrase psychological distress.",
          "recommendation": "Add distress[tiab] to the outcome block and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current outcome block includes distress[tiab], and the packet records a fresh complete evaluation."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an entry-date limit from 1800-01-01 through 2020-11-22. No date cutoff appears in the review question or eligibility criteria, so this excludes later pandemic evidence without a stated justification.",
          "recommendation": "Remove the entry-date limit unless the review scope is explicitly restricted to records entered by 2020-11-22, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "The user explicitly instructed that this run represent literature in PubMed by 2020-11-22 and that PSB_AS_OF remain set for every command. The cutoff is recorded in protocol.as_of and is an Entrez entry-date bound, not a publication-date limit."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the remaining workload above budget for critic review. The searchable optional outcome concept was tested as an AND-ed block, and population details remain screened because no target subgroup is specified.",
          "evidence": "The outcome block reduces the COVID-context set from 83,452 to 12,854, retains all 15 screened relevant development records, and the refreshed loss sample contains 0 relevant records out of 30. The final count exceeds the 10,000-record budget by 2,854."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-30T14:42:04+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO (exposure-focused; broad population)
- Scope confirmed by user: no (User supplied no known articles, chose standard depth, and cannot answer questions during the run; proceeded with these assumptions without waiting. Population is unrestricted. Lifestyle behaviors are interpreted broadly (physical activity, sedentary/screen behavior, diet, sleep, smoking and alcohol), and well-being includes mental health, stress, quality of life and related psychosocial outcomes. No language or study-design restriction. Harness applies PubMed Entrez-date cutoff 2020-11-22 through PSB_AS_OF; no publication-date limit is added. Final outcome-category probing used both standard-depth samples (30 records each, none eligible); subsequently adding SARS-CoV-2 MeSH and coronavirus[tiab] made the probe technically stale, and its 2-probe budget is exhausted. This residual coverage risk is disclosed for internal critique and human PRESS review. The evaluation date bound is intentionally fixed at 2020-11-22 because the user-provided harness explicitly requires a historical PubMed snapshot through that date using Entrez entry date. This is a run constraint, not a substantive review eligibility cutoff; no publication-date ([dp]) limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related restrictions | search | The pandemic/restriction exposure defines the topic and should be named or indexed in relevant reports; include both infection and public-health restriction terminology. |
| Lifestyle behaviors and well-being outcomes | optional | Topic-defining outcomes are searchable but heterogeneous and may be named by individual behaviors or well-being measures; test as one OR block before deciding whether to AND. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:40:32+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 20,244
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,931 | none |
| 3 | `Pandemics[Mesh]` | 50,277 | none |
| 4 | `Quarantine[Mesh]` | 3,936 | none |
| 5 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 6 | `COVID-19[tiab]` | 67,388 | none |
| 7 | `COVID19[tiab]` | 64,206 | none |
| 8 | `2019-nCoV[tiab]` | 1,288 | none |
| 9 | `2019 novel coronavirus[tiab]` | 1,176 | none |
| 10 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 11 | `novel coronavirus[tiab]` | 6,179 | none |
| 12 | `coronavirus pandemic[tiab]` | 1,011 | none |
| 13 | `COVID pandemic[tiab]` | 183 | none |
| 14 | `coronavirus[tiab]` | 41,791 | none |
| 15 | `pandemic[tiab]` | 56,058 | none |
| 16 | `lockdown*[tiab]` | 3,416 | none |
| 17 | `quarantine*[tiab]` | 6,745 | none |
| 18 | `stay-at-home[tiab]` | 815 | none |
| 19 | `stay at home[tiab]` | 815 | none |
| 20 | `shelter-in-place[tiab]` | 210 | none |
| 21 | `shelter in place[tiab]` | 210 | none |
| 22 | `social distanc*[tiab]` | 3,813 | none |
| 23 | `physical distanc*[tiab]` | 1,606 | none |
| 24 | `self-isolat*[tiab]` | 400 | none |
| 25 | `self isolat*[tiab]` | 400 | none |
| 26 | `confinement[tiab]` | 20,190 | none |
| 27 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 141,692 | none |
| 28 | `Life Style[Mesh]` | 99,996 | none |
| 29 | `Health Behavior[Mesh]` | 333,508 | none |
| 30 | `Exercise[Mesh]` | 212,859 | none |
| 31 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 32 | `Sleep[Mesh]` | 85,169 | none |
| 33 | `Feeding Behavior[Mesh]` | 178,421 | none |
| 34 | `Diet[Mesh]` | 296,758 | none |
| 35 | `Alcohol Drinking[Mesh]` | 72,506 | none |
| 36 | `Smoking[Mesh]` | 152,983 | none |
| 37 | `Mental Health[Mesh]` | 44,674 | none |
| 38 | `Quality of Life[Mesh]` | 215,482 | none |
| 39 | `Depression[Mesh]` | 230,067 | none |
| 40 | `Anxiety[Mesh]` | 93,320 | none |
| 41 | `Stress, Psychological[Mesh]` | 139,617 | none |
| 42 | `Loneliness[Mesh]` | 4,443 | none |
| 43 | `Social Isolation[Mesh]` | 22,365 | none |
| 44 | `Resilience, Psychological[Mesh]` | 6,980 | none |
| 45 | `wellbeing[tiab]` | 91,505 | none |
| 46 | `well-being[tiab]` | 80,676 | none |
| 47 | `well being[tiab]` | 80,676 | none |
| 48 | `mental health[tiab]` | 159,665 | none |
| 49 | `psychological[tiab]` | 229,134 | none |
| 50 | `psychosocial[tiab]` | 102,025 | none |
| 51 | `quality of life[tiab]` | 282,526 | none |
| 52 | `health-related quality of life[tiab]` | 46,267 | none |
| 53 | `HRQoL[tiab]` | 18,041 | none |
| 54 | `life satisfaction[tiab]` | 8,062 | none |
| 55 | `mood[tiab]` | 76,259 | none |
| 56 | `loneliness[tiab]` | 6,825 | none |
| 57 | `social isolation[tiab]` | 7,931 | none |
| 58 | `social connectedness[tiab]` | 934 | none |
| 59 | `stress[tiab]` | 779,147 | none |
| 60 | `anxiety[tiab]` | 199,917 | none |
| 61 | `depress*[tiab]` | 474,400 | none |
| 62 | `distress[tiab]` | 119,022 | none |
| 63 | `resilien*[tiab]` | 35,817 | none |
| 64 | `physical activ*[tiab]` | 118,343 | none |
| 65 | `exercise[tiab]` | 272,207 | none |
| 66 | `sedentary[tiab]` | 32,472 | none |
| 67 | `screen time[tiab]` | 2,454 | none |
| 68 | `sleep[tiab]` | 171,185 | none |
| 69 | `diet*[tiab]` | 587,723 | none |
| 70 | `eating[tiab]` | 77,769 | none |
| 71 | `nutrition*[tiab]` | 299,576 | none |
| 72 | `alcohol[tiab]` | 263,050 | none |
| 73 | `smoking[tiab]` | 228,902 | none |
| 74 | `tobacco[tiab]` | 104,259 | none |
| 75 | `substance use[tiab]` | 37,851 | none |
| 76 | `health behavior*[tiab]` | 18,620 | none |
| 77 | `lifestyle[tiab]` | 99,644 | none |
| 78 | `life style[tiab]` | 11,282 | none |
| 79 | `daily activit*[tiab]` | 17,886 | none |
| 80 | `#28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79` | 4,125,144 | none |
| 81 | `#27 AND #80` | 20,244 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR Pandemics[Mesh] OR Quarantine[Mesh] OR SARS-CoV-2[tiab] OR COVID-19[tiab] OR COVID19[tiab] OR 2019-nCoV[tiab] OR 2019 novel coronavirus[tiab] OR coronavirus disease 2019[tiab] OR novel coronavirus[tiab] OR coronavirus pandemic[tiab] OR COVID pandemic[tiab] OR coronavirus[tiab] OR pandemic[tiab] OR lockdown*[tiab] OR quarantine*[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR shelter in place[tiab] OR social distanc*[tiab] OR physical distanc*[tiab] OR self-isolat*[tiab] OR self isolat*[tiab] OR confinement[tiab]) AND (Life Style[Mesh] OR Health Behavior[Mesh] OR Exercise[Mesh] OR Sedentary Behavior[Mesh] OR Sleep[Mesh] OR Feeding Behavior[Mesh] OR Diet[Mesh] OR Alcohol Drinking[Mesh] OR Smoking[Mesh] OR Mental Health[Mesh] OR Quality of Life[Mesh] OR Depression[Mesh] OR Anxiety[Mesh] OR Stress, Psychological[Mesh] OR Loneliness[Mesh] OR Social Isolation[Mesh] OR Resilience, Psychological[Mesh] OR wellbeing[tiab] OR well-being[tiab] OR well being[tiab] OR mental health[tiab] OR psychological[tiab] OR psychosocial[tiab] OR quality of life[tiab] OR health-related quality of life[tiab] OR HRQoL[tiab] OR life satisfaction[tiab] OR mood[tiab] OR loneliness[tiab] OR social isolation[tiab] OR social connectedness[tiab] OR stress[tiab] OR anxiety[tiab] OR depress*[tiab] OR distress[tiab] OR resilien*[tiab] OR physical activ*[tiab] OR exercise[tiab] OR sedentary[tiab] OR screen time[tiab] OR sleep[tiab] OR diet*[tiab] OR eating[tiab] OR nutrition*[tiab] OR alcohol[tiab] OR smoking[tiab] OR tobacco[tiab] OR substance use[tiab] OR health behavior*[tiab] OR lifestyle[tiab] OR life style[tiab] OR daily activit*[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being outcomes | AND-ed | 141,692 / 20,244 | 85.7% | none | 0/30 (up to 10% of removed records could be relevant) | The block remains central to the question and retains all 15 known records across development and held-out validation. In the refreshed 30-record sample removed by this current query, no item met eligibility; it reduces the COVID/restriction query by over 80%. Final count remains over the default 10,000 workload budget; the critic should assess this burden and the fact that the two clean category probes predate the last exposure-term additions. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Lifestyle behaviors and well-being outcomes | 1 | `movement[tiab] OR cooking[tiab] OR food intake[tiab] OR eating habit*[tiab] OR coping[tiab] OR affect[tiab] OR boredom[tiab] OR home routine*[tiab] OR social contact[tiab]` | 3,279 | 0/30 |
| Lifestyle behaviors and well-being outcomes | 2 | `movement[tiab] OR cooking[tiab] OR food intake[tiab] OR eating habit*[tiab] OR coping[tiab] OR affect[tiab] OR boredom[tiab] OR home routine*[tiab] OR social contact[tiab]` | 3,100 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_exposure | 4,125,144 | 0 |
| lifestyle_wellbeing | 141,692 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 140,992 | initial | none | Initial concept blocks set from question; built broad outcome candidate and added screened pilot discoveries as development records. |
| 2 | 20,445 | lifestyle_wellbeing: +53 / -0 | none | ANDed tested topic-defining outcome block after 15 known records were retained and optional loss sample (0/30 relevant) plus category probe were screened. |
| 3 | 20,445 | lifestyle_wellbeing: +0 / -1 | none | Removed noncanonical Physical Activity MeSH alias; canonical Exercise heading already represents the concept; free text still searches physical activity variants. |
| 4 | 19,842 | covid_exposure: +0 / -1 | none | Removed the non-specific Coronavirus Infections heading, which covers multiple pre-COVID coronavirus diseases; COVID-specific MeSH and text terms plus restriction terminology remain. |
| 5 | 20,244 | covid_exposure: +2 / -0 | none | Added SARS-CoV-2 MeSH and coronavirus[tiab] from frequent, relevant development-set terms, adding indexed and free-text exposure coverage. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 2 findings; F1 must-fix open, F2 should-fix open
- Round 2 on version 5: 2 findings; F1 must-fix rejected, F2 should-fix accepted-risk
- Round 3 on version 5: 2 findings; F1 must-fix rejected, F2 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1817 NCBI requests logged (984 from cache); strategy sha256 98377ca49939._

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
        "message": "20,244 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:lifestyle_wellbeing",
        "blocking": false,
        "requires_review": true,
        "id": "I-f47897d33dddf6144e78"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "20,244 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:lifestyle_wellbeing",
        "blocking": false,
        "requires_review": true,
        "id": "I-f47897d33dddf6144e78"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "Life Style",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Health Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Sedentary Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "Sleep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
        "text": "Alcohol Drinking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Smoking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Quality of Life",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "Stress, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Loneliness",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "Loneliness",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "Social Isolation",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Resilience, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:32+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "Resilience, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"pandemics\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"SARS-CoV-2\"[Title/Abstract] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract] OR \"covid pandemic\"[Title/Abstract] OR \"coronavirus\"[Title/Abstract] OR \"pandemic\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"social distanc*\"[Title/Abstract] OR \"physical distanc*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"confinement\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"health behavior\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"alcohol drinking\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"anxiety\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"loneliness\"[MeSH Terms] OR \"social isolation\"[MeSH Terms] OR \"resilience, psychological\"[MeSH Terms] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"psychological\"[Title/Abstract] OR \"psychosocial\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"health related quality of life\"[Title/Abstract] OR \"HRQoL\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"mood\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"social isolation\"[Title/Abstract] OR \"social connectedness\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"anxiety\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"resilien*\"[Title/Abstract] OR \"physical activ*\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"lifestyle\"[Title/Abstract] OR \"life style\"[Title/Abstract] OR \"daily activit*\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "0bdec931cbd3b709d2a3d17896cb373b5cb2784b55ac2ca35aeacdec4a6519c2",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two blocks represent the stated exposure and broad outcome concepts; the packet names no required member that is covered only by a narrower phrase."
        },
        "operators": {
          "verdict": "revise",
          "note": "The OR blocks and AND combination are structurally clear, but the outcome block's decision evidence is incomplete: its category probes are stale after exposure terms were added."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied MeSH translations show recognized headings, and the packet reports no translation errors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The outcome block is broad, but the category probes that tested terms outside it predate the final exposure-term additions; its coverage evidence is therefore incomplete."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized, uses explicit Boolean operators and field tags, and has no reported PubMed warnings or errors."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The question lacks a temporal cutoff, but the harness explicitly requires a historical 2020-11-22 PubMed snapshot via Entrez date. No publication-date limit should be added."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query restricts records to Entrez entry dates through 2020-11-22. The question and eligibility criteria specify no temporal cutoff, so later-indexed studies are excluded.",
          "recommendation": "Remove the entry-date cutoff for an unrestricted search, or state and justify the historical cutoff in the review scope.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome block is AND-ed based in part on category probes that are explicitly stale: the exposure block changed after those probes, and the probe budget is exhausted. The refreshed 0/30 loss sample tests records removed by the outcome block; it does not refresh the category probes of records the block may miss.",
          "recommendation": "Run a fresh category probe against the current exposure block before relying on the outcome block's coverage; if that cannot be done, document the residual coverage risk and treat the AND decision as provisional.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final count exceeds the stated workload budget, but the outcome block represents an eligibility requirement and substantially reduces the exposure query. Retaining the block is defensible while its coverage limitation is disclosed.",
          "evidence": "The query returns 20,244 records against a 10,000-record budget; the block reduces the base from 141,692 by 85.7%, retains all 15 known records, and the refreshed loss sample found 0 relevant records among 30 screened."
        },
        {
          "issue_id": "I-f47897d33dddf6144e78",
          "status": "accepted-risk",
          "response": "The stale status is supported and the remaining category-coverage uncertainty is accepted provisionally because the packet discloses the stale probes and exhausted probe budget. This does not establish that the current block has complete coverage.",
          "evidence": "Both category probes screened 30 records with no relevant items, but the packet says they predate the final SARS-CoV-2 MeSH and coronavirus[tiab] additions; the probe budget is spent."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "aacfce6111ac93c28fdb6cf51908852560adbfca75fc084fc134c17849b01719",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The blocks cover the named pandemic and restriction exposure and the broad lifestyle and well-being outcomes. The packet identifies no required member covered only through a phrase narrowed by its parent wording."
        },
        "operators": {
          "verdict": "pass",
          "note": "The OR blocks and their AND combination are explicit. The outcome block's stale category probes leave residual coverage uncertainty, which is disclosed and accepted provisionally."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied translations verify the MeSH headings, and no translation issues are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words broadly represent the named exposure and outcome concepts. The category probes predate the last exposure additions, so they do not establish current coverage; this limitation is disclosed and accepted provisionally."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query uses explicit Boolean operators, parentheses, and field tags. No PubMed warnings or errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date bound is an explicit harness requirement for the historical snapshot through 2020-11-22, not a substantive eligibility cutoff. No publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query restricts records to Entrez entry dates through 2020-11-22. The question and eligibility criteria specify no temporal cutoff, so later-indexed studies are excluded.",
          "recommendation": "Remove the entry-date cutoff for an unrestricted search, or state and justify the historical cutoff in the review scope.",
          "status": "rejected",
          "response": "The packet says the user-provided harness explicitly requires a historical PubMed snapshot through 2020-11-22 using Entrez entry date. It also clarifies that this is a run constraint, not a substantive review eligibility cutoff."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome block is AND-ed based in part on category probes that are explicitly stale: the exposure block changed after those probes, and the probe budget is exhausted. The refreshed 0/30 loss sample tests records removed by the outcome block; it does not refresh the category probes of records the block may miss.",
          "recommendation": "Run a fresh category probe against the current exposure block before relying on the outcome block's coverage; if that cannot be done, document the residual coverage risk and treat the AND decision as provisional.",
          "status": "accepted-risk",
          "response": "The stale probes do not establish current category coverage. The packet discloses that limitation and the exhausted probe budget, so the residual uncertainty is accepted provisionally.",
          "evidence": "Both category probes screened 30 records with no eligible items, but they predate the final SARS-CoV-2 MeSH and coronavirus[tiab] additions. The refreshed loss sample screened 30 records removed by the current outcome block and found 0 relevant; it does not test records the current block may miss."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The outcome block is defensible because outcomes are central to eligibility and it substantially reduces the exposure query. The final count remains above the workload budget, so this burden is accepted.",
          "evidence": "The block reduces 141,692 records to 20,244 (85.7%), retains all 15 known records, and the refreshed loss sample found 0 relevant records among 30 screened. The final count exceeds the 10,000-record budget."
        },
        {
          "issue_id": "I-f47897d33dddf6144e78",
          "status": "accepted-risk",
          "response": "The stale-probe warning is valid. The remaining category-coverage uncertainty is accepted provisionally because the packet discloses it and the probe budget is exhausted; this does not establish complete current coverage.",
          "evidence": "Both 30-record category probes predate the final SARS-CoV-2 MeSH and coronavirus[tiab] additions, and the packet reports that the two-probe budget is spent."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "aacfce6111ac93c28fdb6cf51908852560adbfca75fc084fc134c17849b01719",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure and outcome blocks cover the concepts named in the question and eligibility criteria; no required member is covered only through a phrase narrowed by its parent wording."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Boolean blocks are explicit. The outcome block’s stale category probes leave residual coverage uncertainty, which is disclosed and accepted provisionally."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied translations verify the MeSH headings, with no unresolved translation issues reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words broadly represent the exposure and outcome concepts. Stale category probes do not establish current coverage, and that limitation is disclosed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query uses explicit Boolean operators, parentheses, and field tags, with no reported PubMed warnings or errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date bound is an explicit harness requirement for the historical snapshot through 2020-11-22, not a substantive eligibility cutoff. No publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query restricts records to Entrez entry dates through 2020-11-22. The question and eligibility criteria specify no temporal cutoff, so later-indexed studies are excluded.",
          "recommendation": "Remove the entry-date cutoff for an unrestricted search, or state and justify the historical cutoff in the review scope.",
          "status": "rejected",
          "response": "The packet specifies that the user-provided harness requires a historical PubMed snapshot through 2020-11-22 using Entrez entry date. This is a run constraint, not a substantive review eligibility cutoff."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome block is AND-ed based in part on category probes that are explicitly stale: the exposure block changed after those probes, and the probe budget is exhausted. The refreshed 0/30 loss sample tests records removed by the outcome block; it does not refresh the category probes of records the block may miss.",
          "recommendation": "Run a fresh category probe against the current exposure block before relying on the outcome block's coverage; if that cannot be done, document the residual coverage risk and treat the AND decision as provisional.",
          "status": "accepted-risk",
          "response": "The stale probes do not establish current category coverage. The packet discloses that limitation and the exhausted probe budget, so the residual uncertainty is accepted provisionally.",
          "evidence": "Both 30-record category probes predate the final SARS-CoV-2 MeSH and coronavirus[tiab] additions. The refreshed loss sample screened 30 records removed by the current outcome block and found 0 relevant; it does not test records the current block may miss."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The outcome block represents an eligibility requirement and substantially reduces the exposure query, so retaining it is defensible. The final count exceeds the stated workload budget, and that burden is accepted.",
          "evidence": "The query returns 20,244 records against a 10,000-record budget; the outcome block reduces 141,692 records by 85.7%, retains all 15 known records, and the refreshed loss sample found 0 relevant records among 30 screened."
        },
        {
          "issue_id": "I-f47897d33dddf6144e78",
          "status": "accepted-risk",
          "response": "The stale-probe warning is valid. The remaining category-coverage uncertainty is accepted provisionally because it is disclosed and the probe budget is exhausted; this does not establish complete current coverage.",
          "evidence": "Both 30-record category probes predate the final SARS-CoV-2 MeSH and coronavirus[tiab] additions, and the packet reports that the two-probe budget is spent."
        }
      ]
    }
  ]
}
```


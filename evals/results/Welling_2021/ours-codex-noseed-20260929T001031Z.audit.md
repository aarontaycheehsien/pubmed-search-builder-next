# PubMed search strategy: audit

Generated 2026-09-29T01:24:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User has no known relevant articles and cannot answer questions during this run; proceeded with the above scope assumption. No language, age, geography, or study-design search limits. COVID-19 is treated as the exposure; either lifestyle behavior or well-being outcomes can qualify. Empirical evidence available in PubMed by Entrez date 2020-11-22 is in scope. Reviewer response: human participation and empirical status remain screening criteria; no human-only or study-design block is used because MeSH completeness varies for newly indexed records and mixed empirical designs have no single appropriate validated filter for this broad impact question.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related restrictions | search | The pandemic is the common exposure; COVID-19 and SARS-CoV-2 are named in records. Related lockdown, quarantine and distancing measures are included in this exposure block. |
| Lifestyle behaviors and well-being outcomes | optional | These define the review topic, but papers may report specific outcomes without naming the umbrella terms; test a broad outcome block before deciding whether to require it. |
| Human participants and empirical study status | screen | These are screening eligibility properties, not a reliably named topic block. Human MeSH indexing is absent on unindexed records, and eligible evidence spans observational and other empirical designs; screen these properties rather than impose a human-only or ad hoc study-design filter. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T01:23:28+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 16,619
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR "Coronavirus Infections"[Mesh] OR "Pandemics"[Mesh] OR "Quarantine"[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR COVID[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR 2019-nCoV[tiab] OR 2019 novel coronavirus[tiab] OR novel coronavirus 2019[tiab] OR coronavirus disease 2019[tiab] OR coronavirus pandemic[tiab] OR pandemic lockdown*[tiab] OR lockdown*[tiab] OR lock-down*[tiab] OR quarantine*[tiab] OR social distanc*[tiab] OR physical distanc*[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR shelter in place[tiab] OR movement restriction*[tiab])` | 102,790 | none |
| 2 | `#1` | 102,790 | none |
| 3 | `("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Behavior"[Mesh] OR "Health Promotion"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Motor Activity"[Mesh] OR "Exercise"[Mesh] OR "Sleep"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Mental Health"[Mesh] OR "Psychological Well-Being"[Mesh] OR "Quality of Life"[Mesh] OR "Stress, Psychological"[Mesh] OR "Psychological Distress"[Mesh] OR "Smoking"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Loneliness"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR lifestyle[tiab] OR life style[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR lifestyle behavior*[tiab] OR lifestyle behaviour*[tiab] OR physical activit*[tiab] OR exercise[tiab] OR sedentary[tiab] OR sitting time[tiab] OR sleep[tiab] OR diet*[tiab] OR nutrition*[tiab] OR eating behavior*[tiab] OR eating behaviour*[tiab] OR smoking[tiab] OR tobacco[tiab] OR alcohol[tiab] OR substance use[tiab] OR well-being[tiab] OR wellbeing[tiab] OR subjective well-being[tiab] OR subjective wellbeing[tiab] OR mental health[tiab] OR psychological distress[tiab] OR depression[tiab] OR anxiety[tiab] OR stress[tiab] OR quality of life[tiab] OR life satisfaction[tiab] OR happiness[tiab] OR loneliness[tiab] OR social support[tiab] OR mobility[tiab] OR "distance traveled"[tiab] OR "distance travelled"[tiab] OR "home time"[tiab] OR "time at home"[tiab] OR "time spent at home"[tiab])` | 5,417,125 | none |
| 4 | `#3` | 5,417,125 | none |
| 5 | `#2 AND #4` | 16,619 | none |

### Strategy (single line, for copying into PubMed)

```text
((("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR "Coronavirus Infections"[Mesh] OR "Pandemics"[Mesh] OR "Quarantine"[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR COVID[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR 2019-nCoV[tiab] OR 2019 novel coronavirus[tiab] OR novel coronavirus 2019[tiab] OR coronavirus disease 2019[tiab] OR coronavirus pandemic[tiab] OR pandemic lockdown*[tiab] OR lockdown*[tiab] OR lock-down*[tiab] OR quarantine*[tiab] OR social distanc*[tiab] OR physical distanc*[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR shelter in place[tiab] OR movement restriction*[tiab])) AND (("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Behavior"[Mesh] OR "Health Promotion"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Motor Activity"[Mesh] OR "Exercise"[Mesh] OR "Sleep"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Mental Health"[Mesh] OR "Psychological Well-Being"[Mesh] OR "Quality of Life"[Mesh] OR "Stress, Psychological"[Mesh] OR "Psychological Distress"[Mesh] OR "Smoking"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Loneliness"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR lifestyle[tiab] OR life style[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR lifestyle behavior*[tiab] OR lifestyle behaviour*[tiab] OR physical activit*[tiab] OR exercise[tiab] OR sedentary[tiab] OR sitting time[tiab] OR sleep[tiab] OR diet*[tiab] OR nutrition*[tiab] OR eating behavior*[tiab] OR eating behaviour*[tiab] OR smoking[tiab] OR tobacco[tiab] OR alcohol[tiab] OR substance use[tiab] OR well-being[tiab] OR wellbeing[tiab] OR subjective well-being[tiab] OR subjective wellbeing[tiab] OR mental health[tiab] OR psychological distress[tiab] OR depression[tiab] OR anxiety[tiab] OR stress[tiab] OR quality of life[tiab] OR life satisfaction[tiab] OR happiness[tiab] OR loneliness[tiab] OR social support[tiab] OR mobility[tiab] OR "distance traveled"[tiab] OR "distance travelled"[tiab] OR "home time"[tiab] OR "time at home"[tiab] OR "time spent at home"[tiab]))) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 16 | 16 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being outcomes | AND-ed | 102,790 / 16,619 | 83.8% | none | 0/30 (up to 10% of removed records could be relevant) | After widening the block to include general behavior/behaviour and mobility/home-time/travel measures, a screened loss-sample record on COVID-related home time and travel among people with ALS was added as relevant and is now retrieved. The fresh 30-record sample contained no eligible studies, and all 16 known relevant development records are retrieved; the block still reduces the COVID/restriction set by about 84%, though the result count is above budget. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid19 | 5,417,125 | 0 |
| lifestyle_wellbeing | 102,790 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial scope-led draft: COVID-19 and related restrictions are the required exposure block; lifestyle behavior and well-being are tested as one broad optional outcome block because umbrella outcome labels are inconsistent. |
| 2 | 102,790 | covid19: +1 / -0 | none | Initial scope-led draft: COVID-19 and related restrictions are the required exposure block; lifestyle behavior and well-being are tested as one broad optional outcome block because umbrella outcome labels are inconsistent. |
| 3 | 102,790 | limits/combination | none | Added Psychological Distress and Loneliness MeSH terms mined from the screened relevant development records; their existing title/abstract wording is retained. |
| 4 | 11,698 | lifestyle_wellbeing: +1 / -0 | none | Moved the measured lifestyle/well-being candidate into the query because it reduced retrieval by 88.6%, lost no known relevant record, and its 30-record loss sample had no eligible studies; final count remains above the 10,000 default budget. |
| 5 | 11,765 | lifestyle_wellbeing: +1 / -1 | none | Addressed critic lexical findings: added subjective well-being wording and Smoking/Alcohol Drinking MeSH headings. Documented human participant and empirical study status as screening eligibility properties because human-only MeSH can miss unindexed records and the scope spans mixed empirical designs. |
| 6 | 102,790 | lifestyle_wellbeing: +0 / -1 | none | Temporarily returned the updated outcome block to candidate status so its optional decision can be remeasured after adding critic-requested terms. |
| 7 | 102,790 | limits/combination | none | Widened the outcome block after the loss sample identified a relevant COVID-related mobility study (33118628): added behavior/behaviour, behavior MeSH, mobility, home-time, and travel-distance terms; added the screened record to the relevant development set. |
| 8 | 16,619 | lifestyle_wellbeing: +1 / -0 | none | Re-included the outcome block after its updated loss sample (zero relevant among 30) and verified the newly identified ALS mobility study is now retrieved; all 16 relevant development records remain retrieved. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 3 findings; F1 should-fix open, F2 should-fix open, F3 should-fix open
- Round 2 on version 8: 3 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix accepted-risk
- Round 3 on version 8: 3 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 989 NCBI requests logged (483 from cache); strategy sha256 151addc73cab._

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
        "message": "16,619 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "16,619 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
        "text": "\"Coronavirus Infections\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
        "text": "\"Pandemics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
        "text": "\"Quarantine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001519",
          "name": "Behavior",
          "type": "descriptor",
          "scope_note": "The observable response of a man or animal to a situation.",
          "tree_numbers": [
            "F01.145"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001519",
      "preferred_label": "Behavior",
      "type": "descriptor",
      "location": "vocabulary:29",
      "term": {
        "text": "\"Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Promotion",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006293",
          "name": "Health Promotion",
          "type": "descriptor",
          "scope_note": "Encouraging consumer behaviors most likely to optimize health potentials (physical and psychosocial) through health information, preventive programs, and access to medical care.",
          "tree_numbers": [
            "H02.403.720.750.380.579",
            "N02.421.726.407.579"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006293",
      "preferred_label": "Health Promotion",
      "type": "descriptor",
      "location": "vocabulary:30",
      "term": {
        "text": "\"Health Promotion\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Motor Activity\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Sleep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Well-Being",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000092862",
          "name": "Psychological Well-Being",
          "type": "descriptor",
          "scope_note": "Condition of existence, or state of awareness, in which psychological needs are satisfied",
          "tree_numbers": [
            "F01.145.677.500",
            "I01.800.500",
            "K01.752.400.750.500",
            "N06.850.505.400.425.837.500"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000092862",
      "preferred_label": "Psychological Well-Being",
      "type": "descriptor",
      "location": "vocabulary:38",
      "term": {
        "text": "\"Psychological Well-Being\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "\"Psychological Distress\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Loneliness",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "\"Loneliness\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "\"Anxiety\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:23:28+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"Coronavirus Infections\"[MeSH Terms] OR \"Pandemics\"[MeSH Terms] OR \"Quarantine\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"COVID\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus 2019\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract] OR \"pandemic lockdown*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down*\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"social distanc*\"[Title/Abstract] OR \"physical distanc*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Behavior\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Motor Activity\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Mental Health\"[MeSH Terms] OR \"Psychological Well-Being\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Psychological Distress\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Loneliness\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"Life Style\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"behavior*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract] OR \"lifestyle behavior*\"[Title/Abstract] OR \"lifestyle behaviour*\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"Exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting time\"[Title/Abstract] OR \"Sleep\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"eating behavior*\"[Title/Abstract] OR \"eating behaviour*\"[Title/Abstract] OR \"Smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"subjective well being\"[Title/Abstract] OR \"subjective wellbeing\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"Psychological Distress\"[Title/Abstract] OR \"Depression\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"happiness\"[Title/Abstract] OR \"Loneliness\"[Title/Abstract] OR \"social support\"[Title/Abstract] OR \"mobility\"[Title/Abstract] OR \"distance traveled\"[Title/Abstract] OR \"distance travelled\"[Title/Abstract] OR \"home time\"[Title/Abstract] OR \"time at home\"[Title/Abstract] OR \"time spent at home\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "c5a0be1da12a0175f2ecd482a2159e683c8cd04ba058e0f417feb75281070973",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility examples explicitly include subjective well-being, but the text-word block does not name that phrase directly. Add the phrase and relevant spelling variant, then rerun the complete evaluation."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are ORed within one block and combined with the optional outcome block using AND. The development set retains all 15 known relevant records."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The outcome block has broad behavior and well-being headings, but lacks specific headings for named behaviors such as smoking and alcohol use. Add relevant controlled headings and reevaluate."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add explicit subjective well-being wording to cover an eligibility example by its own name. The existing well-being terms and behavior examples otherwise cover much of the stated scope."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported searches and final query are parenthesized and combine the blocks correctly. Diagnostics report no syntax or translation errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date limit matches the stated 2020-11-22 evidence cutoff. No language, age, geography, or study-design limits are applied."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names subjective well-being as an example outcome, but the block has no explicit subjective well-being text expression. The general well-being wording does not demonstrate clause-specific coverage of this named member.",
          "recommendation": "Add explicit text expressions for subjective well-being and subjective wellbeing, then rerun the complete evaluation and check retrieval.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility examples include smoking and alcohol use, but the subject-heading block does not include specific headings for smoking or alcohol consumption; it relies on broader headings and text words.",
          "recommendation": "Add relevant specific MeSH headings for smoking or tobacco use and alcohol use, verifying their preferred labels and rerunning the complete evaluation.",
          "status": "open"
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final set has 11,698 records, above the 10,000-record workload budget. The outcome block was tested, but the packet does not show a test of other searchable eligibility concepts, such as humans or empirical-study status, as optional blocks.",
          "recommendation": "Document why other eligibility concepts are not suitable search blocks, or test them as optional blocks with loss assessment; then reassess the workload warning.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "The warning remains unresolved because the final set exceeds the stated workload budget and the packet does not document that every searchable eligibility concept has been considered as an optional block.",
          "evidence": "The final count is 11,698 against a budget of 10,000. The packet documents testing the lifestyle and well-being block, but no optional-block assessment for human or empirical-study eligibility."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 8,
      "review_sha256": "fc6ea6e67725c4d267ded2967dc4bf58cc1e13defa0642806798db28bcfaa139",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block now names subjective well-being and subjective wellbeing explicitly. The listed behavior and well-being examples are covered by their own text terms or headings, and the added mobility, distance, and home-time terms cover the identified relevant record."
        },
        "operators": {
          "verdict": "pass",
          "note": "COVID-19 and restriction terms are ORed within the exposure block; the optional outcome block is ORed internally and ANDed with exposure. All 16 known relevant development records are retrieved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The outcome block now includes the specific Smoking and Alcohol Drinking MeSH headings requested in round 1, alongside broader behavior and outcome headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Explicit subjective well-being variants and broad behavior, mobility, distance, and home-time wording are present. The fresh loss sample found no eligible studies among 30 screened records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported searches and combined query are parenthesized and combine the blocks correctly. Diagnostics and lint report no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date limit matches the stated 2020-11-22 cutoff, and no language, age, geography, human-only, or study-design filter is applied. The 16,619-result set remains above the 10,000 budget; the packet documents why human and empirical status remain screening criteria and records the optional outcome-block test, so retain the workload warning as an accepted risk."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names subjective well-being as an example outcome, but the earlier block did not include explicit text expressions for it.",
          "recommendation": "Add explicit text expressions for subjective well-being and subjective wellbeing, then rerun the complete evaluation and check retrieval.",
          "status": "resolved",
          "response": "Both subjective well-being variants are now in the outcome block. The complete evaluation is recorded at strategy version 8, and all 16 known relevant records are retrieved."
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility examples include smoking and alcohol use, but the earlier subject-heading block lacked specific headings for them.",
          "recommendation": "Add relevant specific MeSH headings for smoking or tobacco use and alcohol use, verifying their preferred labels and rerunning the complete evaluation.",
          "status": "resolved",
          "response": "The current outcome block includes the verified MeSH headings Smoking and Alcohol Drinking. The complete evaluation is recorded at strategy version 8."
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The result set exceeds the 10,000-record workload budget; the earlier packet did not document consideration of human-participant or empirical-study eligibility as optional blocks.",
          "recommendation": "Document why other eligibility concepts are not suitable search blocks, or test them as optional blocks with loss assessment; then reassess the workload warning.",
          "status": "accepted-risk",
          "response": "The packet now documents that human MeSH indexing is absent for some unindexed records and that eligible evidence spans empirical designs without a single appropriate validated study-design filter, so these remain screening criteria. The optional outcome block was tested with a fresh 30-record loss sample and retrieves all 16 known relevant records. The final count still exceeds budget at 16,619, so the workload warning is retained as an accepted risk."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains because the final set exceeds the stated 10,000-record budget. The packet documents the optional outcome-block test and why human-participant and empirical-study status remain screening criteria.",
          "evidence": "The final count is 16,619. The outcome block reduces the COVID/restriction set by 83.8%; its fresh loss sample contained 0 relevant records among 30 screened, and all 16 known relevant development records are retrieved. The protocol explains that human MeSH indexing is absent on unindexed records and eligible studies span empirical designs."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 8,
      "review_sha256": "fc6ea6e67725c4d267ded2967dc4bf58cc1e13defa0642806798db28bcfaa139",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "F1 is resolved: the outcome block explicitly includes both subjective well-being spellings. The stated examples are represented in the current terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure block terms are ORed, as are outcome terms; the two blocks are combined with AND. All 16 known relevant development records are retrieved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "F2 is resolved: the outcome block includes the specific Smoking and Alcohol Drinking MeSH headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block includes explicit subjective well-being variants and behavior, mobility, distance, and home-time wording. The fresh loss sample contained no eligible studies among 30 screened."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported searches are parenthesized and combine the blocks correctly; diagnostics report no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The stated date cutoff is applied, with no language, age, geography, human-only, or study-design filter. F3 and the workload warning remain accepted risks: the packet documents why human and empirical-study status remain screening criteria and records the optional outcome-block test."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names subjective well-being as an example outcome, but the earlier block did not include explicit text expressions for it.",
          "recommendation": "Add explicit text expressions for subjective well-being and subjective wellbeing, then rerun the complete evaluation and check retrieval.",
          "status": "resolved",
          "response": "Both variants are in the current outcome block. The complete evaluation is recorded at strategy version 8, and all 16 known relevant records are retrieved."
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility examples include smoking and alcohol use, but the earlier subject-heading block lacked specific headings for them.",
          "recommendation": "Add relevant specific MeSH headings for smoking or tobacco use and alcohol use, verifying their preferred labels and rerunning the complete evaluation.",
          "status": "resolved",
          "response": "The current outcome block includes the requested Smoking and Alcohol Drinking MeSH headings. The complete evaluation is recorded at strategy version 8."
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The result set exceeds the 10,000-record workload budget; the earlier packet did not document consideration of human-participant or empirical-study eligibility as optional blocks.",
          "recommendation": "Document why other eligibility concepts are not suitable search blocks, or test them as optional blocks with loss assessment; then reassess the workload warning.",
          "status": "accepted-risk",
          "response": "The packet documents that human MeSH indexing is absent on some unindexed records and that eligible evidence spans empirical designs without a single appropriate validated study-design filter, so these remain screening criteria. The optional outcome block was tested with a fresh 30-record loss sample and retrieves all 16 known relevant records. The final count remains above budget at 16,619, so the workload warning is retained as an accepted risk."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains because the final set exceeds the 10,000-record budget. The packet documents the optional outcome-block test and why human-participant and empirical-study status remain screening criteria.",
          "evidence": "The final count is 16,619. The outcome block reduces the COVID/restriction set by 83.8%; its fresh loss sample contained 0 relevant records among 30 screened, and all 16 known relevant development records are retrieved. The protocol explains that human MeSH indexing is absent on unindexed records and eligible studies span empirical designs."
        }
      ]
    }
  ]
}
```


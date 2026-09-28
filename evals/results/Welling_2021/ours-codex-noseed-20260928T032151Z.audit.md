# PubMed search strategy: audit

Generated 2026-09-28T03:59:26+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: yes (User asked to proceed without clarification. The task instructions explicitly require treating 2020-11-22 as the simulated search date, excluding literature added to PubMed after that date, keeping PSB_AS_OF set for every command, and avoiding publication-date limits. Scope is interpreted broadly: COVID-19 pandemic and a broad union of lifestyle/well-being outcomes are searched; lockdown measures are screening details. No language, age, or geography limits. No user-supplied known articles. Standard-depth discovery included targeted systematic-review searches, a broad quarantine/social consequences systematic review, precise pilot searches, and cited-reference candidate screening. Fifteen primary studies met the question's title/abstract criteria; 11 are in the development set and four are held out as validation. Outcome block is admitted because lifestyle/well-being outcomes define the topic; terms cover a broad OR-union rather than requiring each member.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic | search | The pandemic is the defining exposure and should be named in eligible records; lockdown is a related measure but not reliably named in every pandemic impact study. |
| Lockdown and related public health restrictions | screen | Related restrictions are eligible exposure details but are inconsistently named and should not be a required block. |
| Lifestyle behaviors and well-being outcomes | search | These outcomes define the topic of the review. They are searched as a broad union of behavior, lifestyle, sleep, activity, diet, and psychosocial well-being terms; no single behavior or outcome is required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T03:57:53+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 13,793
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,931 | none |
| 3 | `COVID-19[tiab]` | 67,388 | none |
| 4 | `COVID19[tiab]` | 64,206 | none |
| 5 | `COVID[tiab]` | 67,980 | none |
| 6 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 7 | `SARS CoV 2[tiab]` | 23,503 | none |
| 8 | `2019-nCoV[tiab]` | 1,288 | none |
| 9 | `2019 nCoV[tiab]` | 1,288 | none |
| 10 | `"coronavirus disease 2019"[tiab:~2]` | 15,475 | none |
| 11 | `"2019 novel coronavirus"[tiab:~2]` | 2,393 | none |
| 12 | `"novel coronavirus 2019"[tiab:~2]` | 2,393 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 77,808 | none |
| 14 | `Life Style[Mesh]` | 99,996 | none |
| 15 | `Healthy Lifestyle[Mesh]` | 8,656 | none |
| 16 | `Health Behavior[Mesh]` | 333,508 | none |
| 17 | `Health Risk Behaviors[Mesh]` | 780 | none |
| 18 | `Exercise[Mesh]` | 212,859 | none |
| 19 | `Motor Activity[Mesh]` | 309,966 | none |
| 20 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 21 | `Diet[Mesh]` | 296,758 | none |
| 22 | `Feeding Behavior[Mesh]` | 178,421 | none |
| 23 | `Sleep[Mesh]` | 85,169 | none |
| 24 | `Mental Health[Mesh]` | 44,674 | none |
| 25 | `Psychological Well-Being[Mesh]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 26 | `Quality of Life[Mesh]` | 215,482 | none |
| 27 | `Personal Satisfaction[Mesh]` | 20,683 | none |
| 28 | `Social Isolation[Mesh]` | 22,365 | none |
| 29 | `Stress, Psychological[Mesh]` | 139,617 | none |
| 30 | `Anxiety[Mesh]` | 93,320 | none |
| 31 | `Depression[Mesh]` | 230,067 | none |
| 32 | `Life Style[tiab]` | 11,282 | none |
| 33 | `Lifestyle[tiab]` | 99,644 | none |
| 34 | `lifestyle*[tiab]` | 108,849 | none |
| 35 | `behavior*[tiab]` | 1,024,043 | none |
| 36 | `behaviour*[tiab]` | 293,760 | none |
| 37 | `Health Behavior[tiab]` | 9,149 | none |
| 38 | `Health Behaviour[tiab]` | 4,329 | none |
| 39 | `health behaviors[tiab]` | 11,055 | none |
| 40 | `health behaviours[tiab]` | 3,546 | none |
| 41 | `Physical Activity[tiab]` | 114,493 | none |
| 42 | `Physical Activities[tiab]` | 6,751 | none |
| 43 | `Exercise[tiab]` | 272,206 | none |
| 44 | `Sedentary[tiab]` | 32,472 | none |
| 45 | `Inactive[tiab]` | 96,568 | none |
| 46 | `Inactivity[tiab]` | 15,458 | none |
| 47 | `Diet[tiab]` | 339,581 | none |
| 48 | `Dietary[tiab]` | 260,599 | none |
| 49 | `Nutrition[tiab]` | 181,193 | none |
| 50 | `Eating[tiab]` | 77,769 | none |
| 51 | `Food intake[tiab]` | 45,992 | none |
| 52 | `Sleep[tiab]` | 171,185 | none |
| 53 | `Sleeping[tiab]` | 20,409 | none |
| 54 | `Insomnia[tiab]` | 22,051 | none |
| 55 | `Alcohol[tiab]` | 263,050 | none |
| 56 | `Drinking[tiab]` | 114,398 | none |
| 57 | `Smoking[tiab]` | 228,902 | none |
| 58 | `Tobacco[tiab]` | 104,259 | none |
| 59 | `Substance Use[tiab]` | 37,851 | none |
| 60 | `Wellbeing[tiab]` | 91,505 | none |
| 61 | `Well-being[tiab]` | 80,676 | none |
| 62 | `Well being[tiab]` | 80,676 | none |
| 63 | `Wellness[tiab]` | 10,646 | none |
| 64 | `Mental Health[tiab]` | 159,665 | none |
| 65 | `Psychological[tiab]` | 229,134 | none |
| 66 | `Emotional[tiab]` | 159,221 | none |
| 67 | `Quality of Life[tiab]` | 282,526 | none |
| 68 | `Life Satisfaction[tiab]` | 8,062 | none |
| 69 | `Personal Satisfaction[tiab]` | 682 | none |
| 70 | `Social Isolation[tiab]` | 7,931 | none |
| 71 | `Social Participation[tiab]` | 3,171 | none |
| 72 | `Social Activity[tiab]` | 1,826 | none |
| 73 | `Anxiety[tiab]` | 199,917 | none |
| 74 | `Depression[tiab]` | 348,632 | none |
| 75 | `Distress[tiab]` | 119,022 | none |
| 76 | `Stress[tiab]` | 779,146 | none |
| 77 | `Loneliness[tiab]` | 6,825 | none |
| 78 | `#14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77` | 4,935,217 | none |
| 79 | `#13 AND #78` | 13,793 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR COVID[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR 2019-nCoV[tiab] OR 2019 nCoV[tiab] OR "coronavirus disease 2019"[tiab:~2] OR "2019 novel coronavirus"[tiab:~2] OR "novel coronavirus 2019"[tiab:~2]) AND (Life Style[Mesh] OR Healthy Lifestyle[Mesh] OR Health Behavior[Mesh] OR Health Risk Behaviors[Mesh] OR Exercise[Mesh] OR Motor Activity[Mesh] OR Sedentary Behavior[Mesh] OR Diet[Mesh] OR Feeding Behavior[Mesh] OR Sleep[Mesh] OR Mental Health[Mesh] OR Psychological Well-Being[Mesh] OR Quality of Life[Mesh] OR Personal Satisfaction[Mesh] OR Social Isolation[Mesh] OR Stress, Psychological[Mesh] OR Anxiety[Mesh] OR Depression[Mesh] OR Life Style[tiab] OR Lifestyle[tiab] OR lifestyle*[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR Health Behavior[tiab] OR Health Behaviour[tiab] OR health behaviors[tiab] OR health behaviours[tiab] OR Physical Activity[tiab] OR Physical Activities[tiab] OR Exercise[tiab] OR Sedentary[tiab] OR Inactive[tiab] OR Inactivity[tiab] OR Diet[tiab] OR Dietary[tiab] OR Nutrition[tiab] OR Eating[tiab] OR Food intake[tiab] OR Sleep[tiab] OR Sleeping[tiab] OR Insomnia[tiab] OR Alcohol[tiab] OR Drinking[tiab] OR Smoking[tiab] OR Tobacco[tiab] OR Substance Use[tiab] OR Wellbeing[tiab] OR Well-being[tiab] OR Well being[tiab] OR Wellness[tiab] OR Mental Health[tiab] OR Psychological[tiab] OR Emotional[tiab] OR Quality of Life[tiab] OR Life Satisfaction[tiab] OR Personal Satisfaction[tiab] OR Social Isolation[tiab] OR Social Participation[tiab] OR Social Activity[tiab] OR Anxiety[tiab] OR Depression[tiab] OR Distress[tiab] OR Stress[tiab] OR Loneliness[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid | 4,935,217 | 0 |
| outcomes | 77,808 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial one-block COVID-19 strategy using specific MeSH headings and disease-name text variants; outcomes and restrictions remain screening criteria to avoid unnecessary AND blocks. |
| 2 | 77,808 | covid: +3 / -3 | none | Fixed proximity syntax by quoting each multiword COVID-19 name; the block remains one broad exposure concept. |
| 3 | 12,087 | outcomes: +51 / -0 | none | Added a broad union outcome block because lifestyle and well-being define the review topic; grouped many behavior and psychosocial outcome alternatives with OR to improve screening efficiency while retaining high recall. |
| 4 | 13,793 | outcomes: +13 / -0 | none | After screening cited-reference candidates, expanded the text-word variants for lifestyle and behavior morphology and added indexed social well-being alternatives; retained COVID and broad outcome blocks, with lockdown details screened. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 2 findings; R1-01 should-fix resolved, R1-02 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 805 NCBI requests logged (439 from cache); strategy sha256 d855ae23fa1c._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:25",
        "blocking": false,
        "requires_review": true,
        "id": "I-958af6280cc49a278186"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:25",
        "blocking": false,
        "requires_review": true,
        "id": "I-ed1d8b1b327f0f22acfe"
      }
    ],
    "issues": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:25",
        "blocking": false,
        "requires_review": true,
        "id": "I-958af6280cc49a278186"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:25",
        "blocking": false,
        "requires_review": true,
        "id": "I-ed1d8b1b327f0f22acfe"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "Life Style",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Healthy Lifestyle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Healthy Lifestyle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "Health Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Risk Behaviors",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000073599",
          "name": "Health Risk Behaviors",
          "type": "descriptor",
          "scope_note": "Pattern of behavior which predisposes certain individuals to increased risk for contracting disease or sustaining personal injury. These behaviors may cluster into a risky lifestyle.",
          "tree_numbers": [
            "F01.145.488.250"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000073599",
      "preferred_label": "Health Risk Behaviors",
      "type": "descriptor",
      "location": "vocabulary:16",
      "term": {
        "text": "Health Risk Behaviors",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "Motor Activity",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
        "text": "Sedentary Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "Sleep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Well-Being",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "Psychological Well-Being",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Quality of Life",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Personal Satisfaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "Personal Satisfaction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "Social Isolation",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Stress, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:57:53+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"COVID\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract:~2] OR \"2019 novel coronavirus\"[Title/Abstract:~2] OR \"novel coronavirus 2019\"[Title/Abstract:~2]) AND (\"life style\"[MeSH Terms] OR \"healthy lifestyle\"[MeSH Terms] OR \"health behavior\"[MeSH Terms] OR \"health risk behaviors\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"motor activity\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"psychological well being\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR \"personal satisfaction\"[MeSH Terms] OR \"social isolation\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"Depression\"[MeSH Terms]) OR \"life style\"[Title/Abstract] OR \"Lifestyle\"[Title/Abstract] OR \"lifestyle*\"[Title/Abstract] OR \"behavior*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract] OR \"health behavior\"[Title/Abstract] OR \"health behaviour\"[Title/Abstract] OR \"health behaviors\"[Title/Abstract] OR \"health behaviours\"[Title/Abstract] OR \"physical activity\"[Title/Abstract] OR \"physical activities\"[Title/Abstract] OR \"Exercise\"[Title/Abstract] OR \"Sedentary\"[Title/Abstract] OR \"Inactive\"[Title/Abstract] OR \"Inactivity\"[Title/Abstract] OR \"Diet\"[Title/Abstract] OR \"Dietary\"[Title/Abstract] OR \"Nutrition\"[Title/Abstract] OR \"Eating\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"Sleep\"[Title/Abstract] OR \"Sleeping\"[Title/Abstract] OR \"Insomnia\"[Title/Abstract] OR \"Alcohol\"[Title/Abstract] OR \"Drinking\"[Title/Abstract] OR \"Smoking\"[Title/Abstract] OR \"Tobacco\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"Wellbeing\"[Title/Abstract] OR \"Well-being\"[Title/Abstract] OR \"Well-being\"[Title/Abstract] OR \"Wellness\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"Psychological\"[Title/Abstract] OR \"Emotional\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"personal satisfaction\"[Title/Abstract] OR \"social isolation\"[Title/Abstract] OR \"social participation\"[Title/Abstract] OR \"social activity\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"Depression\"[Title/Abstract] OR \"Distress\"[Title/Abstract] OR \"Stress\"[Title/Abstract] OR \"Loneliness\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "f46d2dc9966ec8a467f49ec307074dfe8badc8c35085f649434e1c345ef27525",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues. Proximity expressions are explicitly tested, and the PubMed translation preserves the intended COVID-19 and outcome concepts. The verified Psychological Well-Being descriptor translates to a MeSH term, though its date-bounded query returns zero hits; see the warning dispositions."
        },
        "operators": {
          "verdict": "pass",
          "note": "COVID-19 and outcomes are joined with AND, with synonyms joined by OR. Lockdown is appropriately a screening detail rather than a required search block. No fragile one-direction process terms appear in the search."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet's authority checks identify the searched MeSH headings as verified descriptors. Psychological Well-Being is verified as a descriptor despite zero hits under the simulated search cutoff."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words provide a broad OR-union across lifestyle, behaviors, activity, diet, sleep, substance use, and psychosocial well-being. The scope requires at least one such outcome, not every outcome individually."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The tested strategy uses balanced Boolean groups, field tags, and explicit proximity syntax. The packet reports no lint issues or PubMed errors; the translated combined query reflects the intended grouping."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The strategy stops at the required simulated date, 2020-11-22, using an entry-date range. It applies no publication-date, language, age, geography, or human-only filter. The protocol explicitly explains the required simulated cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The retained Psychological Well-Being[Mesh] term has zero hits and a PubMed warning. Its authority is verified, but the packet gives no term-specific reason for retaining it after the required warning review.",
          "recommendation": "Record the clause-specific review: the heading is a verified descriptor, the date-bounded query returns zero hits, and whether it is retained as a no-effect sensitivity term or removed. If changed, rerun the complete evaluation.",
          "status": "resolved",
          "response": "Resolved by documenting the clause-specific decision in narrative.md. The exact MeSH descriptor is authority-verified and semantically matches the outcome concept; the warning indicates no hits under the mandated Entrez cutoff, not an invalid heading. It remains in the OR block as a no-effect sensitivity alternative. The block also has related Mental Health and Quality of Life headings plus free-text well-being and psychological terms."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The four validation records are described as semi-independent and held out from term mining, and the packet says they were split from the same 15-record relevant set. This is transparent, but it is not an external independent validation set.",
          "recommendation": "Keep the validation claim explicitly limited to a semi-independent held-out split; do not describe its 100% recall as independent validation.",
          "status": "resolved",
          "response": "Preserve the qualification that the four records were held out from the same discovery-assembled pool and are semi-independent relative-recall checks, not an external validation sample. The limitation is stated in narrative.md and will be reported with the recall results."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-958af6280cc49a278186",
          "status": "rejected",
          "response": "The warning says no items were found, but the authority evidence verifies Psychological Well-Being as a MeSH descriptor and the translation maps it to MeSH Terms. The warning alone does not indicate a failed heading translation.",
          "evidence": "The vocabulary evidence lists descriptor D000092862, preferred label Psychological Well-Being, status verified; the line 25 translation is \"psychological well being\"[MeSH Terms]."
        },
        {
          "issue_id": "I-ed1d8b1b327f0f22acfe",
          "status": "accepted-risk",
          "response": "The zero-hit result is real under the simulated cutoff. The heading is verified and semantically exact, but contributes no records in this date-bounded search. It is retained only as a no-effect OR alternative; other well-being headings and free-text terms remain in the block.",
          "evidence": "Line 25 has count 0 for the query bounded by entry date through 2020-11-22; the verified vocabulary record identifies Psychological Well-Being as descriptor D000092862. The outcome block also contains Mental Health[Mesh], Quality of Life[Mesh], Wellbeing[tiab], Well-being[tiab], and Psychological[tiab]."
        }
      ]
    }
  ]
}
```


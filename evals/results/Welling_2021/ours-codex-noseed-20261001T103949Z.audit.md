# PubMed search strategy: audit

Generated 2026-10-01T11:27:07+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User requested proceeding without clarification and did not explicitly confirm the scope. Scope roles and assumptions were set from the question alone. No known relevant articles were supplied. The evaluation date is bounded by PubMed Entrez date using PSB_AS_OF=2020-11-22 on every command; no publication-date limit is used. The exposure concept is not a category concept: the block explicitly covers COVID-19/SARS-CoV-2/pandemic terminology and named restriction measures; no member-only disease category probe applies. After screening a second precision pilot, 14 additional eligible records were added (26 total); the outcomes block then passed the optional-concept criteria and was AND-ed.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The pandemic or its restrictions define the exposure and should be named or indexed in eligible reports; COVID-19 and lockdown terminology will both be represented. |
| Lifestyle behaviors and well-being | search | Lifestyle and well-being outcomes define eligibility and are sufficiently searchable for a required block after testing: 26 screened development records were all retrieved, none of 30 sampled loss records was eligible, and the block reduced retrieval by 91.2%. |
| People affected by the pandemic | screen | No age or subgroup restriction is specified and population details may be reported inconsistently. |
| Impact or change attributable to pandemic measures | screen | Causal language and direction of change are inconsistently indexed; assess the relationship at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:25:29+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 43,927
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,931 | none |
| 3 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 4 | `Pandemics[Mesh]` | 50,277 | none |
| 5 | `Quarantine[Mesh]` | 3,936 | none |
| 6 | `Communicable Disease Control[Mesh]` | 369,222 | none |
| 7 | `COVID-19[tiab]` | 67,388 | none |
| 8 | `COVID19[tiab]` | 64,206 | none |
| 9 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 10 | `2019-nCoV[tiab]` | 1,288 | none |
| 11 | `2019 novel coronavirus[tiab]` | 1,176 | none |
| 12 | `novel coronavirus[tiab]` | 6,179 | none |
| 13 | `coronavirus*[tiab]` | 43,050 | none |
| 14 | `pandemic*[tiab]` | 58,444 | none |
| 15 | `lockdown*[tiab]` | 3,416 | none |
| 16 | `lock-down*[tiab]` | 178 | none |
| 17 | `confinement[tiab]` | 20,190 | none |
| 18 | `quarantine*[tiab]` | 6,745 | none |
| 19 | `self-isolat*[tiab]` | 400 | none |
| 20 | `stay-at-home[tiab]` | 815 | none |
| 21 | `stay at home[tiab]` | 815 | none |
| 22 | `shelter-in-place[tiab]` | 210 | none |
| 23 | `shelter in place[tiab]` | 210 | none |
| 24 | `social distancing[tiab]` | 2,657 | none |
| 25 | `movement restriction*[tiab]` | 568 | none |
| 26 | `movement control order*[tiab]` | 23 | none |
| 27 | `home confinement[tiab]` | 121 | none |
| 28 | `travel ban*[tiab]` | 86 | none |
| 29 | `travel restriction*[tiab]` | 335 | none |
| 30 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 501,843 | none |
| 31 | `Life Style[Mesh]` | 99,996 | none |
| 32 | `Healthy Lifestyle[Mesh]` | 8,656 | none |
| 33 | `Health Behavior[Mesh]` | 333,508 | none |
| 34 | `Health Risk Behaviors[Mesh]` | 780 | none |
| 35 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 36 | `Exercise[Mesh]` | 212,859 | none |
| 37 | `Diet[Mesh]` | 296,758 | none |
| 38 | `Feeding Behavior[Mesh]` | 178,421 | none |
| 39 | `Alcohol Drinking[Mesh]` | 72,506 | none |
| 40 | `Smoking[Mesh]` | 152,983 | none |
| 41 | `Sleep[Mesh]` | 85,169 | none |
| 42 | `Mental Health[Mesh]` | 44,674 | none |
| 43 | `Quality of Life[Mesh]` | 215,482 | none |
| 44 | `Anxiety[Mesh]` | 93,320 | none |
| 45 | `Depression[Mesh]` | 230,067 | none |
| 46 | `Stress, Psychological[Mesh]` | 139,617 | none |
| 47 | `Social Isolation[Mesh]` | 22,365 | none |
| 48 | `lifestyle[tiab]` | 99,644 | none |
| 49 | `life style[tiab]` | 11,282 | none |
| 50 | `health behavior*[tiab]` | 18,620 | none |
| 51 | `health behaviour*[tiab]` | 7,323 | none |
| 52 | `health-related behavior*[tiab]` | 2,478 | none |
| 53 | `health-related behaviour*[tiab]` | 1,417 | none |
| 54 | `physical activ*[tiab]` | 118,343 | none |
| 55 | `exercise[tiab]` | 272,207 | none |
| 56 | `sedentary[tiab]` | 32,472 | none |
| 57 | `sitting time[tiab]` | 1,295 | none |
| 58 | `screen time[tiab]` | 2,454 | none |
| 59 | `sleep[tiab]` | 171,185 | none |
| 60 | `sleeping[tiab]` | 20,409 | none |
| 61 | `diet*[tiab]` | 587,723 | none |
| 62 | `eating behavio*[tiab]` | 10,745 | none |
| 63 | `feeding behavio*[tiab]` | 10,847 | none |
| 64 | `food consumption[tiab]` | 14,333 | none |
| 65 | `alcohol[tiab]` | 263,050 | none |
| 66 | `drinking[tiab]` | 114,398 | none |
| 67 | `smoking[tiab]` | 228,902 | none |
| 68 | `tobacco[tiab]` | 104,259 | none |
| 69 | `wellbeing[tiab]` | 91,505 | none |
| 70 | `well-being[tiab]` | 80,676 | none |
| 71 | `well being[tiab]` | 80,676 | none |
| 72 | `quality of life[tiab]` | 282,526 | none |
| 73 | `mental health[tiab]` | 159,665 | none |
| 74 | `psychological well-being[tiab]` | 9,542 | none |
| 75 | `psychological wellbeing[tiab]` | 1,436 | none |
| 76 | `psychological distress[tiab]` | 20,154 | none |
| 77 | `anxiety[tiab]` | 199,917 | none |
| 78 | `depression[tiab]` | 348,632 | none |
| 79 | `stress[tiab]` | 779,146 | none |
| 80 | `loneliness[tiab]` | 6,825 | none |
| 81 | `social isolation[tiab]` | 7,931 | none |
| 82 | `happiness[tiab]` | 7,214 | none |
| 83 | `resilience[tiab]` | 27,036 | none |
| 84 | `#31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83` | 3,739,889 | none |
| 85 | `#30 AND #84` | 43,927 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR Coronavirus Infections[Mesh] OR Pandemics[Mesh] OR Quarantine[Mesh] OR Communicable Disease Control[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR SARS-CoV-2[tiab] OR 2019-nCoV[tiab] OR 2019 novel coronavirus[tiab] OR novel coronavirus[tiab] OR coronavirus*[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR lock-down*[tiab] OR confinement[tiab] OR quarantine*[tiab] OR self-isolat*[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR shelter in place[tiab] OR social distancing[tiab] OR movement restriction*[tiab] OR movement control order*[tiab] OR home confinement[tiab] OR travel ban*[tiab] OR travel restriction*[tiab]) AND (Life Style[Mesh] OR Healthy Lifestyle[Mesh] OR Health Behavior[Mesh] OR Health Risk Behaviors[Mesh] OR Sedentary Behavior[Mesh] OR Exercise[Mesh] OR Diet[Mesh] OR Feeding Behavior[Mesh] OR Alcohol Drinking[Mesh] OR Smoking[Mesh] OR Sleep[Mesh] OR Mental Health[Mesh] OR Quality of Life[Mesh] OR Anxiety[Mesh] OR Depression[Mesh] OR Stress, Psychological[Mesh] OR Social Isolation[Mesh] OR lifestyle[tiab] OR life style[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR health-related behavior*[tiab] OR health-related behaviour*[tiab] OR physical activ*[tiab] OR exercise[tiab] OR sedentary[tiab] OR sitting time[tiab] OR screen time[tiab] OR sleep[tiab] OR sleeping[tiab] OR diet*[tiab] OR eating behavio*[tiab] OR feeding behavio*[tiab] OR food consumption[tiab] OR alcohol[tiab] OR drinking[tiab] OR smoking[tiab] OR tobacco[tiab] OR wellbeing[tiab] OR well-being[tiab] OR well being[tiab] OR quality of life[tiab] OR mental health[tiab] OR psychological well-being[tiab] OR psychological wellbeing[tiab] OR psychological distress[tiab] OR anxiety[tiab] OR depression[tiab] OR stress[tiab] OR loneliness[tiab] OR social isolation[tiab] OR happiness[tiab] OR resilience[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 26 | 26 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| exposure | 3,739,889 | 0 |
| outcomes | 501,843 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial exposure block with MeSH and broad pandemic/restriction text terms; broad lifestyle and well-being outcome concept tested as optional. Terms informed by screened pilot records. |
| 2 | 501,843 | exposure: +0 / -1 | none | Removed malformed proximity syntax for the fixed virus name; ordinary tagged text term already covers SARS-CoV-2. |
| 3 | 43,927 | outcomes: +54 / -0 | none | Moved the outcomes concept into the required search after adding screened pilot records: 26 of 26 development records were retained, the measured loss sample had 0 eligible records, and retrieval fell from 501,843 to 43,927. This reduces screening burden while retaining all known eligible records. |
| 4 | 43,927 | outcomes: +0 / -1 | none | Removed Psychological Well-Being[Mesh] because NCBI reports it was introduced in 2023 and it had zero retrieval under the 2020-11-22 Entrez cutoff; its previous indexing was Quality of Life, which remains in the block, alongside free-text well-being variants. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 0 findings; 
- Round 2 on version 4: 0 findings; 
- Round 3 on version 4: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1221 NCBI requests logged (454 from cache); strategy sha256 71f45ad7c97e._

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
        "message": "43,927 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "43,927 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "requested": "Communicable Disease Control",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003140",
          "name": "Communicable Disease Control",
          "type": "descriptor",
          "scope_note": "Programs of surveillance designed to prevent the transmission of disease by any means from person to person or from animal to man.",
          "tree_numbers": [
            "N06.850.780.200"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003140",
      "preferred_label": "Communicable Disease Control",
      "type": "descriptor",
      "location": "vocabulary:6",
      "term": {
        "text": "Communicable Disease Control",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Life Style",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Healthy Lifestyle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "Healthy Lifestyle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Health Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Risk Behaviors",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Health Risk Behaviors",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "Sedentary Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Alcohol Drinking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Smoking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "Sleep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "Quality of Life",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "Stress, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:25:29+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "Social Isolation",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"pandemics\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"communicable disease control\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down*\"[Title/Abstract] OR \"confinement\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"movement control order*\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"travel ban*\"[Title/Abstract] OR \"travel restriction*\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"healthy lifestyle\"[MeSH Terms] OR \"health behavior\"[MeSH Terms] OR \"health risk behaviors\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"alcohol drinking\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR \"anxiety\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"stress, psychological\"[MeSH Terms] OR \"social isolation\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"life style\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"health related behavior*\"[Title/Abstract] OR \"health related behaviour*\"[Title/Abstract] OR \"physical activ*\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting time\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"sleeping\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating behavio*\"[Title/Abstract] OR \"feeding behavio*\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"psychological well being\"[Title/Abstract] OR \"psychological wellbeing\"[Title/Abstract] OR \"psychological distress\"[Title/Abstract] OR \"anxiety\"[Title/Abstract] OR \"depression\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"social isolation\"[Title/Abstract] OR \"happiness\"[Title/Abstract] OR \"resilience\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "79eb464681ea5746ebbf0fb861e5985bd2349e4cbe2bacd36d81a81a14223ada",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The final translation retains both concept blocks and the date-entry range. Hyphenated and unhyphenated restriction phrases translate to equivalent expressions in some cases, but no translation issue is reported and the variants do not remove coverage."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR is used within the exposure and outcome blocks, and the blocks are ANDed. The packet documents 26/26 development records retrieved, 30 sampled loss records with none eligible, and a 91.2% reduction from the exposure-only set. This meets the packet’s stated threshold for requiring the outcome block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes verified MeSH headings spanning COVID-19, pandemic and restriction concepts, lifestyle behaviors, and well-being outcomes. The packet reports no heading or translation blockers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover COVID-19 and common restriction wording, plus behavior and well-being outcomes. No specific missing searchable member is identified by the scope or packet evidence."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is reported as valid, with no lint errors, syntax errors, or blocking diagnostics. Repeated phrase variants in the translation are harmless."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit or population filter is imposed. The packet explicitly bounds the evaluation by entry date through 2020-11-22. Retrieval exceeds the workload budget, but the diagnostic is addressed below: population and impact remain screening concepts for the stated scope reasons, and the outcome block already provides a tested workload reduction."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is acknowledged. The searchable outcome concept was tested and ANDed under the packet’s rules: all 26 development records were retrieved, none of 30 sampled loss records was eligible, and retrieval fell 91.2%. The remaining screen-only concepts have been considered: population has no specified age or subgroup restriction and may be reported inconsistently; impact or change is inconsistently indexed, so its relationship and direction are better assessed during screening. Adding either as a required block is not supported by the packet’s evidence and could reduce recall. The 43,927-record workload remains above the 10,000 budget as an accepted risk.",
          "query": "((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR Coronavirus Infections[Mesh] OR Pandemics[Mesh] OR Quarantine[Mesh] OR Communicable Disease Control[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR SARS-CoV-2[tiab] OR 2019-nCoV[tiab] OR 2019 novel coronavirus[tiab] OR novel coronavirus[tiab] OR coronavirus*[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR lock-down*[tiab] OR confinement[tiab] OR quarantine*[tiab] OR self-isolat*[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR shelter in place[tiab] OR social distancing[tiab] OR movement restriction*[tiab] OR movement control order*[tiab] OR home confinement[tiab] OR travel ban*[tiab] OR travel restriction*[tiab]) AND (Life Style[Mesh] OR Healthy Lifestyle[Mesh] OR Health Behavior[Mesh] OR Health Risk Behaviors[Mesh] OR Sedentary Behavior[Mesh] OR Exercise[Mesh] OR Diet[Mesh] OR Feeding Behavior[Mesh] OR Alcohol Drinking[Mesh] OR Smoking[Mesh] OR Sleep[Mesh] OR Mental Health[Mesh] OR Quality of Life[Mesh] OR Anxiety[Mesh] OR Depression[Mesh] OR Stress, Psychological[Mesh] OR Social Isolation[Mesh] OR lifestyle[tiab] OR life style[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR health-related behavior*[tiab] OR health-related behaviour*[tiab] OR physical activ*[tiab] OR exercise[tiab] OR sedentary[tiab] OR sitting time[tiab] OR screen time[tiab] OR sleep[tiab] OR sleeping[tiab] OR diet*[tiab] OR eating behavio*[tiab] OR feeding behavio*[tiab] OR food consumption[tiab] OR alcohol[tiab] OR drinking[tiab] OR smoking[tiab] OR tobacco[tiab] OR wellbeing[tiab] OR well-being[tiab] OR well being[tiab] OR quality of life[tiab] OR mental health[tiab] OR psychological well-being[tiab] OR psychological wellbeing[tiab] OR psychological distress[tiab] OR anxiety[tiab] OR depression[tiab] OR stress[tiab] OR loneliness[tiab] OR social isolation[tiab] OR happiness[tiab] OR resilience[tiab])) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
          "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"pandemics\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"communicable disease control\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down*\"[Title/Abstract] OR \"confinement\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"movement control order*\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"travel ban*\"[Title/Abstract] OR \"travel restriction*\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"healthy lifestyle\"[MeSH Terms] OR \"health behavior\"[MeSH Terms] OR \"health risk behaviors\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"alcohol drinking\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR \"anxiety\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"stress, psychological\"[MeSH Terms] OR \"social isolation\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"life style\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"health related behavior*\"[Title/Abstract] OR \"health related behaviour*\"[Title/Abstract] OR \"physical activ*\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting time\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"sleeping\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"eating behavio*\"[Title/Abstract] OR \"feeding behavio*\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"psychological well being\"[Title/Abstract] OR \"psychological wellbeing\"[Title/Abstract] OR \"psychological distress\"[Title/Abstract] OR \"anxiety\"[Title/Abstract] OR \"depression\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"social isolation\"[Title/Abstract] OR \"happiness\"[Title/Abstract] OR \"resilience\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
          "evidence": "Diagnostic code over_workload_budget; severity warning, final location, budget 10,000, nonblocking and requires review. The query count is 43,927. The packet reports 26/26 known development records retrieved, 30 screened loss records with zero eligible records, and outcome-block reduction from 501,843 to 43,927 (91.2%). The scope rationale assigns population and impact to screening because population details may be inconsistent and causal language/direction are inconsistently indexed.",
          "note": "Accept the workload exceedance after considering the remaining screen-only concepts. The packet supports retaining them as screening criteria rather than adding unevidenced required blocks."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "79eb464681ea5746ebbf0fb861e5985bd2349e4cbe2bacd36d81a81a14223ada",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues. The exposure and outcome blocks retain the named searched concepts, including pandemic restrictions, lifestyle behaviors, and well-being."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each block and the exposure and outcome blocks are ANDed. The packet supports the outcome block under its rules: 26 of 26 development records retrieved, none of 30 sampled loss records eligible, and retrieval reduced by 91.2%."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes MeSH headings for COVID-19, pandemics, restrictions, lifestyle behaviors, and well-being outcomes; the packet reports no translation blockers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title and abstract terms cover COVID-19 and restriction wording alongside lifestyle behaviors and well-being outcomes. The packet identifies no uncovered searched concept member."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint errors, translation issues, or blocking diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population filter or publication-date limit is applied; the evaluation is bounded by entry date through 2020-11-22. The over-budget warning remains documented as an accepted risk after considering the screen-only concepts."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 43,927-record retrieval exceeds the 10,000-record workload budget. The outcome block was tested and ANDed with 26 of 26 development records retrieved and no eligible records among 30 sampled losses, reducing retrieval by 91.2%. Population and impact remain screening concepts for the scope reasons documented in the packet.",
          "evidence": "The validation warning is nonblocking and requires review. The packet reports 43,927 results, 26 of 26 known development records retrieved, zero eligible studies among 30 screened loss records, and a reduction from 501,843 to 43,927 results."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "79eb464681ea5746ebbf0fb861e5985bd2349e4cbe2bacd36d81a81a14223ada",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy covers the named exposure and outcome concepts with MeSH and title/abstract terms. The packet reports no translation blocker."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within blocks and exposure is ANDed with outcomes. The outcome block retrieved all 26 development records, none of 30 sampled losses was eligible, and reduced retrieval by 91.2%."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings cover COVID-19, pandemic restrictions, lifestyle behaviors, and well-being outcomes; the packet reports no heading blocker."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title and abstract terms cover COVID-19 and restriction wording alongside lifestyle behavior and well-being terms. The packet identifies no uncovered searched concept."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports a valid query with no lint errors, syntax errors, or blocking diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population filter is imposed; the entry-date range bounds evaluation through 2020-11-22. The workload warning is carried forward as accepted risk, with the tested outcome block applied and the remaining population and impact concepts retained for screening."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains applicable: 43,927 records exceed the 10,000-record budget. The outcome block was tested and ANDed under the packet’s rules. Population and impact remain screening concepts because subgroup details and causal language or direction may be reported inconsistently. The workload exceedance is therefore accepted with the screen-only concepts retained.",
          "evidence": "The packet reports 26 of 26 development records retrieved, no eligible studies among 30 sampled losses, and a 91.2% reduction from 501,843 to 43,927 records. It identifies the workload diagnostic as nonblocking and requiring review."
        }
      ]
    }
  ]
}
```


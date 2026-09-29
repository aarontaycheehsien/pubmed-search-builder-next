# PubMed search strategy: audit

Generated 2026-09-29T03:56:51+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (No known relevant articles were supplied. The user asked to proceed without clarification; scope and eligibility are operational assumptions. COVID-19/pandemic and related restrictions are treated as one exposure block. Lifestyle behavior and well-being are grouped as a single optional outcome block because either can define an eligible study. No population, language, geography, design, or publication-date restriction is imposed. The harness applies the PubMed Entrez-date cutoff via PSB_AS_OF=2020-11-22; no publication-date limit is intended.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The exposure is essential to the question and has recognizable disease, virus, pandemic, and restriction terminology; search these together in one broad block. |
| Lifestyle behaviors and well-being outcomes | optional | These topic-defining outcomes are searchable but may be inconsistently named in abstracts; test their combined broad block before deciding whether to require it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:55:21+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 12,601
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"SARS-CoV-2"[Mesh]` | 45,931 | none |
| 2 | `"COVID-19"[Mesh]` | 57,089 | none |
| 3 | `"Physical Distancing"[Mesh]` | 579 | none |
| 4 | `physical distancing[tiab]` | 436 | none |
| 5 | `"home confinement"[tiab]` | 121 | none |
| 6 | `COVID-19[tiab]` | 67,388 | none |
| 7 | `COVID19[tiab]` | 64,206 | none |
| 8 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 9 | `SARS-CoV2[tiab]` | 1,049 | none |
| 10 | `"2019-nCoV"[tiab]` | 1,288 | none |
| 11 | `2019nCoV[tiab]` | 926 | none |
| 12 | `"2019 novel coronavirus"[tiab]` | 1,176 | none |
| 13 | `"2019 novel coronavirus disease"[tiab]` | 338 | none |
| 14 | `"severe acute respiratory syndrome coronavirus 2"[tiab]` | 7,988 | none |
| 15 | `lockdown*[tiab]` | 3,416 | none |
| 16 | `lock-down*[tiab]` | 178 | none |
| 17 | `"stay-at-home"[tiab]` | 815 | none |
| 18 | `"stay at home"[tiab]` | 815 | none |
| 19 | `"social distancing"[tiab]` | 2,657 | none |
| 20 | `quarantine*[tiab]` | 6,745 | none |
| 21 | `"self-isolation"[tiab]` | 289 | none |
| 22 | `"self isolation"[tiab]` | 289 | none |
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 83,332 | none |
| 24 | `"Life Style"[Mesh]` | 99,996 | none |
| 25 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 26 | `"Exercise"[Mesh]` | 212,859 | none |
| 27 | `"Motor Activity"[Mesh]` | 309,966 | none |
| 28 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 29 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 30 | `"Diet"[Mesh]` | 296,758 | none |
| 31 | `"Sleep"[Mesh]` | 85,169 | none |
| 32 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 33 | `"Smoking"[Mesh]` | 152,983 | none |
| 34 | `"Mental Health"[Mesh]` | 44,674 | none |
| 35 | `"Psychological Distress"[Mesh]` | 4,500 | none |
| 36 | `"Quality of Life"[Mesh]` | 215,482 | none |
| 37 | `lifestyle[tiab]` | 99,644 | none |
| 38 | `"life style"[tiab]` | 11,282 | none |
| 39 | `"lifestyle behavior*"[tiab]` | 2,657 | none |
| 40 | `"health behavior*"[tiab]` | 18,620 | none |
| 41 | `"health behaviour*"[tiab]` | 7,323 | none |
| 42 | `behavior change[tiab]` | 10,479 | none |
| 43 | `behaviour change[tiab]` | 5,426 | none |
| 44 | `"physical activit*"[tiab]` | 118,110 | none |
| 45 | `exercis*[tiab]` | 307,827 | none |
| 46 | `sedentary[tiab]` | 32,472 | none |
| 47 | `"screen time"[tiab]` | 2,454 | none |
| 48 | `sleep[tiab]` | 171,185 | none |
| 49 | `diet*[tiab]` | 587,723 | none |
| 50 | `nutrition*[tiab]` | 299,576 | none |
| 51 | `eating[tiab]` | 77,769 | none |
| 52 | `alcohol[tiab]` | 263,050 | none |
| 53 | `smoking[tiab]` | 228,902 | none |
| 54 | `tobacco[tiab]` | 104,259 | none |
| 55 | `"substance use"[tiab]` | 37,851 | none |
| 56 | `"mental health"[tiab]` | 159,665 | none |
| 57 | `wellbeing[tiab]` | 91,505 | none |
| 58 | `well-being[tiab]` | 80,676 | none |
| 59 | `"quality of life"[tiab]` | 282,526 | none |
| 60 | `anxiety[tiab]` | 199,917 | none |
| 61 | `depression[tiab]` | 348,632 | none |
| 62 | `stress[tiab]` | 779,146 | none |
| 63 | `distress[tiab]` | 119,022 | none |
| 64 | `loneliness[tiab]` | 6,825 | none |
| 65 | `resilience[tiab]` | 27,036 | none |
| 66 | `"Cannabis"[Mesh]` | 10,216 | none |
| 67 | `cannabis[tiab]` | 18,505 | none |
| 68 | `"drug use"[tiab]` | 46,742 | none |
| 69 | `"Sexual Behavior"[Mesh]` | 113,383 | none |
| 70 | `"sexual behavior"[tiab]` | 15,691 | none |
| 71 | `"sexual behaviour"[tiab]` | 5,621 | none |
| 72 | `#24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71` | 4,035,358 | none |
| 73 | `#23 AND #72` | 12,601 | none |

### Strategy (single line, for copying into PubMed)

```text
(("SARS-CoV-2"[Mesh] OR "COVID-19"[Mesh] OR "Physical Distancing"[Mesh] OR physical distancing[tiab] OR "home confinement"[tiab] OR COVID-19[tiab] OR COVID19[tiab] OR SARS-CoV-2[tiab] OR SARS-CoV2[tiab] OR "2019-nCoV"[tiab] OR 2019nCoV[tiab] OR "2019 novel coronavirus"[tiab] OR "2019 novel coronavirus disease"[tiab] OR "severe acute respiratory syndrome coronavirus 2"[tiab] OR lockdown*[tiab] OR lock-down*[tiab] OR "stay-at-home"[tiab] OR "stay at home"[tiab] OR "social distancing"[tiab] OR quarantine*[tiab] OR "self-isolation"[tiab] OR "self isolation"[tiab]) AND ("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Exercise"[Mesh] OR "Motor Activity"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Feeding Behavior"[Mesh] OR "Diet"[Mesh] OR "Sleep"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Smoking"[Mesh] OR "Mental Health"[Mesh] OR "Psychological Distress"[Mesh] OR "Quality of Life"[Mesh] OR lifestyle[tiab] OR "life style"[tiab] OR "lifestyle behavior*"[tiab] OR "health behavior*"[tiab] OR "health behaviour*"[tiab] OR behavior change[tiab] OR behaviour change[tiab] OR "physical activit*"[tiab] OR exercis*[tiab] OR sedentary[tiab] OR "screen time"[tiab] OR sleep[tiab] OR diet*[tiab] OR nutrition*[tiab] OR eating[tiab] OR alcohol[tiab] OR smoking[tiab] OR tobacco[tiab] OR "substance use"[tiab] OR "mental health"[tiab] OR wellbeing[tiab] OR well-being[tiab] OR "quality of life"[tiab] OR anxiety[tiab] OR depression[tiab] OR stress[tiab] OR distress[tiab] OR loneliness[tiab] OR resilience[tiab] OR "Cannabis"[Mesh] OR cannabis[tiab] OR "drug use"[tiab] OR "Sexual Behavior"[Mesh] OR "sexual behavior"[tiab] OR "sexual behaviour"[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 17 | 17 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being outcomes | AND-ed | 83,332 / 12,601 | 84.9% | none | 0/30 (up to 10% of removed records could be relevant) | The refreshed loss sample for the current block was title/abstract screened; none met the lifestyle/well-being impact criteria. The previously missed eligible cohort study was recovered by adding drug use and sexual behavior vocabulary; all 17 screened-in records are now retained. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| COVID-19 pandemic and related lockdown measures | 1 | `2019-nCoV[tiab] OR 2019nCoV[tiab] OR 2019 novel coronavirus[tiab] OR SARS coronavirus 2[tiab] OR epidemic*[tiab] OR outbreak*[tiab]` | 177,780 | not screened |
| COVID-19 pandemic and related lockdown measures | 2 | `2019-nCoV[tiab] OR 2019nCoV[tiab] OR 2019 novel coronavirus[tiab] OR epidemic*[tiab] OR outbreak*[tiab]` | 177,775 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| pandemic_exposure | 4,035,358 | 0 |
| lifestyle_wellbeing | 83,332 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first draft: COVID-19 and related containment measures form the required exposure block; broad lifestyle and well-being outcomes are candidates for optional AND-testing. No known studies supplied; candidate terms drafted from question and MeSH lookup. |
| 2 | 126,406 | pandemic_exposure: +19 / -0 | none | Initial recall-first draft: broad COVID-19 and related containment exposure vocabulary; lifestyle and well-being outcomes are optional and being empirically tested. No known records supplied. |
| 3 | 108,958 | pandemic_exposure: +5 / -5 | none | Revised the exposure block to remove generic coronavirus-infection and pandemic/quarantine MeSH headings and unqualified coronavirus text, which broadened retrieval beyond COVID-19. Kept COVID-specific terms plus named pandemic and restriction wording for recall. |
| 4 | 15,293 | lifestyle_wellbeing: +42 / -0 | none | Added 16 screened relevant records from the topic-focused pilot; outcome block passed optional test (16 known in base, 0/30 relevant in loss sample, 86% reduction) and was AND-ed. |
| 5 | 12,426 | pandemic_exposure: +0 / -1 | none | Removed broad pandemic*[tiab] because its high count retrieves many unrelated historic outbreaks; COVID-specific terms and lockdown/quarantine/social-distancing terms remain. Checking the effect against the 16 screened relevant pilot records. |
| 6 | 12,429 | pandemic_exposure: +1 / -0 | none | Added the SARS-CoV-2 MeSH descriptor after term ranking showed it on 12 of 16 screened relevant records and MeSH authority lookup confirmed the descriptor. Retained COVID-19 MeSH and title/abstract variants; did not add broad Pandemics MeSH because it inflated retrieval with unrelated historic outbreaks. |
| 7 | 12,443 | pandemic_exposure: +3 / -0 | none | Expanded the exposure text/MeSH vocabulary with Physical Distancing and home confinement as pandemic restriction variants; these are not represented by the existing lockdown/social-distancing wording in all records. |
| 8 | 12,601 | lifestyle_wellbeing: +6 / -0 | none | The optional loss sample identified an eligible cohort comparison of drug use and sexual behavior before/during COVID-19, revealing a vocabulary gap. Added drug, cannabis and sexual behavior terms to the outcome block; the missed record is now a development benchmark. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 8 (same-context critic; no fresh-context reviewer available in this run): 0 findings; 
- Round 2 on version 8 (same-context critic; final pre-delivery review found no additional revision): 0 findings; 
- Round 3 on version 8 (same-context closing review; prior issue dispositions and risks are carried forward): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2225 NCBI requests logged (1261 from cache); strategy sha256 7fddff445115._

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
        "message": "12,601 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:pandemic_exposure",
        "blocking": false,
        "requires_review": true,
        "id": "I-40099a2294dce925346d"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "12,601 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:pandemic_exposure",
        "blocking": false,
        "requires_review": true,
        "id": "I-40099a2294dce925346d"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "SARS-CoV-2",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"SARS-CoV-2\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"COVID-19\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Physical Distancing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000085762",
          "name": "Physical Distancing",
          "type": "descriptor",
          "scope_note": "Maintaining recommended amount of spatial separation between self and others.",
          "tree_numbers": [
            "N06.850.780.200.688"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000085762",
      "preferred_label": "Physical Distancing",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Physical Distancing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Motor Activity\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Sleep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Psychological Distress\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
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
    },
    {
      "requested": "Cannabis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002188",
          "name": "Cannabis",
          "type": "descriptor",
          "scope_note": "The plant genus in the Cannabaceae plant family, Urticales order, Hamamelidae subclass. The flowering tops are called many slang terms including pot, marijuana, hashish, bhang, and ganja. The stem is an important source of hemp fiber.",
          "tree_numbers": [
            "B01.875.800.575.912.250.859.937.055.500"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002188",
      "preferred_label": "Cannabis",
      "type": "descriptor",
      "location": "vocabulary:65",
      "term": {
        "text": "\"Cannabis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sexual Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:55:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012725",
          "name": "Sexual Behavior",
          "type": "descriptor",
          "scope_note": "Sexual activities of humans.",
          "tree_numbers": [
            "F01.145.802"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012725",
      "preferred_label": "Sexual Behavior",
      "type": "descriptor",
      "location": "vocabulary:68",
      "term": {
        "text": "\"Sexual Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"SARS-CoV-2\"[MeSH Terms] OR \"COVID-19\"[MeSH Terms] OR \"Physical Distancing\"[MeSH Terms] OR \"Physical Distancing\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"2019 novel coronavirus disease\"[Title/Abstract] OR \"severe acute respiratory syndrome coronavirus 2\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"quarantine*\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract] OR \"self-isolation\"[Title/Abstract]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Motor Activity\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Mental Health\"[MeSH Terms] OR \"Psychological Distress\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"Life Style\"[Title/Abstract] OR \"lifestyle behavior*\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"behavior change\"[Title/Abstract] OR \"behaviour change\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"Sleep\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"Smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"anxiety\"[Title/Abstract] OR \"depression\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"resilience\"[Title/Abstract] OR \"Cannabis\"[MeSH Terms] OR \"Cannabis\"[Title/Abstract] OR \"drug use\"[Title/Abstract] OR \"Sexual Behavior\"[MeSH Terms] OR \"Sexual Behavior\"[Title/Abstract] OR \"sexual behaviour\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 8,
      "review_sha256": "842b27f511063e825fe5afb589804ac630320647a02a24020969c383c6bdf226",
      "note": "same-context critic; no fresh-context reviewer available in this run",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The COVID-19 exposure and the lifestyle/well-being outcome block reflect the broad question. The outcome block was empirically tested and AND-ed with 17 screened relevant records retained; note the remaining category probe risk below."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR joins synonyms within blocks and AND joins exposure with the empirically tested outcome block. No NOT clauses or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "COVID-19 and SARS-CoV-2 headings were checked; lifestyle, physical activity, diet, sleep, substance, mental health and quality-of-life headings match the searched outcomes. Broad Pandemics MeSH was excluded after it inflated unrelated historic results."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes spelling and morphology variants for COVID-19 and restrictions, plus broad outcome language and explicit drug/sexual behavior after a screened miss. All 17 screened relevant records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no syntax, field, truncation, phrase or PubMed translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, language, geography, design or publication-date limits are imposed. The 2020-11-22 Entrez-date cutoff is applied through PSB_AS_OF and the query does not add a publication-date filter."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional lifestyle/well-being outcome block was considered and tested; no additional searchable concept remains only at screening that can be safely AND-ed. It reduces the base count by 85.1% and retains all 17 screened relevant pilot records. The remaining 12,601 records exceed the standard default workload budget of 10,000, so the search requires a larger screening allocation or later protocol-approved refinement.",
          "evidence": "The current PSB evaluation reports 83,267 records without the outcome block, 12,601 with it, 17/17 development records retrieved, no known records lost, and a refreshed loss sample of 0/30 eligible records."
        },
        {
          "issue_id": "I-40099a2294dce925346d",
          "status": "accepted-risk",
          "response": "The category probe was screened before later changes to the exposure/outcome blocks, so it is stale for the final combination and cannot certify the final exposure block. The standard probe budget is exhausted. Retain this as an open sensitivity limitation for human PRESS review; the sample did not identify eligible records outside the exposure vocabulary at the time it was drawn.",
          "evidence": "The second probe sampled 30 records from a broader virus/epidemic/outbreak query outside the then-current exposure block; all 30 titles/abstracts were screened and 0 met eligibility. Later outcome-block adoption and exposure vocabulary additions changed the probe frame; no current probe is available within the configured two-probe budget."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 8,
      "review_sha256": "842b27f511063e825fe5afb589804ac630320647a02a24020969c383c6bdf226",
      "note": "same-context critic; final pre-delivery review found no additional revision",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required exposure block and optional-tested outcome block align with the question; 17 development records are retained. The screened miss in drug/sexual behavior was recovered by adding terms before this bound review."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are OR-expanded internally and AND-combined. Boolean logic and grouping are correct; there are no NOT or proximity clauses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "COVID-19, SARS-CoV-2 and physical-distancing headings are relevant; outcome headings cover lifestyle behavior and well-being dimensions. Broad Pandemics MeSH was excluded because it retrieved unrelated historic outbreaks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "COVID-specific disease variants, lockdown/social/physical distancing and home-confinement terms are present. Outcomes include diet, physical activity, sleep, mental health, substance and sexual behavior, quality of life, and well-being variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete current evaluation reports no PubMed syntax, translation, phrase, field or truncation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unnecessary eligibility filters or publication-date limit are present. The requested as-of date is applied via Entrez date."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "All searchable topic-defining concepts were examined and the outcome block was tested and AND-ed; no further screen-only concept can safely be required. The final count remains above the standard 10,000-record default, which must be considered when allocating screening capacity.",
          "evidence": "PSB reports 83,332 records without the outcome block, 12,601 with it, 17/17 screened relevant pilot records retrieved, no known losses, and 0 eligible records among the latest 30-record loss sample."
        },
        {
          "issue_id": "I-40099a2294dce925346d",
          "status": "accepted-risk",
          "response": "The final exposure block was not probed after all terms and blocks were finalized because the standard two-probe budget was exhausted. Keep this as a sensitivity limitation for information-specialist review; do not interpret the earlier probe as validation of the final search.",
          "evidence": "The screened probe found 0/30 relevant records outside the exposure block before later outcome and exposure revisions. The probe is explicitly marked stale by the current PSB evaluation."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 8,
      "review_sha256": "842b27f511063e825fe5afb589804ac630320647a02a24020969c383c6bdf226",
      "note": "same-context closing review; prior issue dispositions and risks are carried forward",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure and outcome blocks follow the stated question. The user-confirmation ambiguity remains documented as an operational assumption, and the high-sensitivity outcome block has recorded testing."
        },
        "operators": {
          "verdict": "pass",
          "note": "Boolean structure remains sound: synonyms are OR-ed within blocks and the two blocks are AND-ed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The controlled vocabulary is consistent with the COVID-19, SARS-CoV-2 and lifestyle/well-being concepts; broad headings that caused unrelated retrieval were removed."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text variants include disease names, containment measures and broad lifestyle/well-being outcomes, including added drug and sexual behavior terms after a screened miss."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No technical syntax or translation blockers remain."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date cutoff is applied without a publication-date limit; no other filters are used."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The outcome block was considered and tested, but the count remains above the default screening budget. The 12,601-record count and need for a larger screening allocation remain explicit in the narrative and handoff.",
          "evidence": "Current PSB evaluation: 83,332 without the outcome block; 12,601 with it; 17 relevant development records retrieved; the latest loss sample contains 0/30 eligible records."
        },
        {
          "issue_id": "I-40099a2294dce925346d",
          "status": "accepted-risk",
          "response": "The final exposure query lacks a current category probe because the two-probe standard budget was spent before later query revisions. This limitation is carried into the narrative for human PRESS review.",
          "evidence": "The earlier screened probe found 0/30 eligible records but the current PSB evaluation marks the probe stale after later block changes; no claim of current category validation is made."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-30T13:52:53+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User requested proceeding without questions; scope assumptions are provisional. No known relevant articles supplied. Treat lifestyle and well-being as a combined optional OR concept, rather than requiring both outcomes. Apply the harness Entrez-date cutoff PSB_AS_OF=2020-11-22 on every command; do not impose a publication-date limit. Provisional population is broad (general population and specific groups including students, patients, caregivers, and health workers); in a screened pilot, COVID protective-behavior compliance is treated as a relevant health behavior. Include policy-related changes in mobility and protective-behavior adherence as health-related behaviors; the outcome block remains optional because sampled records also report well-being constructs outside a compact reliable term family. MeSH heading Psychological Well-Being (introduced 2023) is excluded under the 2020-11-22 Entrez cutoff; psychological well-being wording remains in [tiab]. The malformed Food and Nutrition[Mesh] phrase was removed; Diet[Mesh] and dietary words remain.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The pandemic exposure defines the review topic and is consistently named with COVID-19 or pandemic terminology; lockdown terms will be included as variants within the same exposure block. |
| Lifestyle behaviors and well-being | optional | These are topic-defining outcomes and are usually named in records, but terminology varies; test a combined OR block to avoid requiring both outcome families. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:51:04+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 13,167
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,931 | none |
| 3 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 4 | `COVID-19[tiab]` | 67,388 | none |
| 5 | `COVID19[tiab]` | 64,206 | none |
| 6 | `COVID[tiab]` | 67,980 | none |
| 7 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 8 | `2019-nCoV[tiab]` | 1,288 | none |
| 9 | `novel coronavirus[tiab]` | 6,179 | none |
| 10 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 11 | `coronavirus pandemic[tiab]` | 1,011 | none |
| 12 | `lockdown*[tiab]` | 3,416 | none |
| 13 | `self-quarantine[tiab]` | 92 | none |
| 14 | `stay-at-home[tiab]` | 815 | none |
| 15 | `stay at home[tiab]` | 815 | none |
| 16 | `shelter-in-place[tiab]` | 210 | none |
| 17 | `shelter in place[tiab]` | 210 | none |
| 18 | `social distancing[tiab]` | 2,657 | none |
| 19 | `physical distancing[tiab]` | 436 | none |
| 20 | `movement restriction*[tiab]` | 568 | none |
| 21 | `movement control[tiab]` | 2,096 | none |
| 22 | `coronavirus[tiab]` | 41,791 | none |
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 97,901 | none |
| 24 | `Life Style[Mesh]` | 99,996 | none |
| 25 | `Healthy Lifestyle[Mesh]` | 8,656 | none |
| 26 | `Exercise[Mesh]` | 212,859 | none |
| 27 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 28 | `Sleep[Mesh]` | 85,169 | none |
| 29 | `Diet[Mesh]` | 296,758 | none |
| 30 | `Alcohol Drinking[Mesh]` | 72,506 | none |
| 31 | `Smoking[Mesh]` | 152,983 | none |
| 32 | `Mental Health[Mesh]` | 44,674 | none |
| 33 | `Quality of Life[Mesh]` | 215,482 | none |
| 34 | `Depression[Mesh]` | 230,067 | none |
| 35 | `Anxiety[Mesh]` | 93,320 | none |
| 36 | `Stress, Psychological[Mesh]` | 139,617 | none |
| 37 | `Social Isolation[Mesh]` | 22,365 | none |
| 38 | `lifestyle[tiab]` | 99,644 | none |
| 39 | `life style[tiab]` | 11,282 | none |
| 40 | `health behavior*[tiab]` | 18,620 | none |
| 41 | `health behaviour*[tiab]` | 7,323 | none |
| 42 | `health habit*[tiab]` | 1,418 | none |
| 43 | `physical activit*[tiab]` | 118,111 | none |
| 44 | `exercise[tiab]` | 272,207 | none |
| 45 | `sedentary[tiab]` | 32,472 | none |
| 46 | `sitting time[tiab]` | 1,295 | none |
| 47 | `inactivit*[tiab]` | 15,483 | none |
| 48 | `diet[tiab]` | 339,581 | none |
| 49 | `dietary[tiab]` | 260,599 | none |
| 50 | `eating behavior*[tiab]` | 7,924 | none |
| 51 | `eating behaviour*[tiab]` | 2,938 | none |
| 52 | `food consumption[tiab]` | 14,333 | none |
| 53 | `nutrition[tiab]` | 181,193 | none |
| 54 | `sleep[tiab]` | 171,185 | none |
| 55 | `sleep quality[tiab]` | 15,610 | none |
| 56 | `sleep duration[tiab]` | 8,298 | none |
| 57 | `alcohol[tiab]` | 263,050 | none |
| 58 | `drinking[tiab]` | 114,398 | none |
| 59 | `smoking[tiab]` | 228,902 | none |
| 60 | `tobacco[tiab]` | 104,259 | none |
| 61 | `well-being[tiab]` | 80,676 | none |
| 62 | `wellbeing[tiab]` | 91,505 | none |
| 63 | `mental health[tiab]` | 159,665 | none |
| 64 | `psychological well-being[tiab]` | 9,542 | none |
| 65 | `quality of life[tiab]` | 282,526 | none |
| 66 | `life satisfaction[tiab]` | 8,062 | none |
| 67 | `psychological distress[tiab]` | 20,154 | none |
| 68 | `depress*[tiab]` | 474,400 | none |
| 69 | `anxiet*[tiab]` | 201,789 | none |
| 70 | `stress[tiab]` | 779,147 | none |
| 71 | `loneliness[tiab]` | 6,825 | none |
| 72 | `social isolation[tiab]` | 7,931 | none |
| 73 | `Obsessive-Compulsive Disorder[Mesh]` | 16,085 | none |
| 74 | `mobility[tiab]` | 146,471 | none |
| 75 | `protective behavio*[tiab]` | 1,948 | none |
| 76 | `protective behaviour*[tiab]` | 462 | none |
| 77 | `compliance[tiab]` | 119,586 | none |
| 78 | `OCD[tiab]` | 9,920 | none |
| 79 | `obsessive-compulsive[tiab]` | 18,147 | none |
| 80 | `obsessive compulsive[tiab]` | 18,147 | none |
| 81 | `behavior*[tiab]` | 1,024,042 | none |
| 82 | `behaviour*[tiab]` | 293,760 | none |
| 83 | `substance use[tiab]` | 37,851 | none |
| 84 | `substance-use[tiab]` | 37,851 | none |
| 85 | `substance misuse[tiab]` | 2,696 | none |
| 86 | `drug use[tiab]` | 46,742 | none |
| 87 | `drug-use[tiab]` | 46,742 | none |
| 88 | `#24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87` | 4,701,688 | none |
| 89 | `#23 AND #88` | 13,167 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR Coronavirus Infections[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR COVID[tiab] OR SARS-CoV-2[tiab] OR 2019-nCoV[tiab] OR novel coronavirus[tiab] OR coronavirus disease 2019[tiab] OR coronavirus pandemic[tiab] OR lockdown*[tiab] OR self-quarantine[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR shelter in place[tiab] OR social distancing[tiab] OR physical distancing[tiab] OR movement restriction*[tiab] OR movement control[tiab] OR coronavirus[tiab]) AND (Life Style[Mesh] OR Healthy Lifestyle[Mesh] OR Exercise[Mesh] OR Sedentary Behavior[Mesh] OR Sleep[Mesh] OR Diet[Mesh] OR Alcohol Drinking[Mesh] OR Smoking[Mesh] OR Mental Health[Mesh] OR Quality of Life[Mesh] OR Depression[Mesh] OR Anxiety[Mesh] OR Stress, Psychological[Mesh] OR Social Isolation[Mesh] OR lifestyle[tiab] OR life style[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR health habit*[tiab] OR physical activit*[tiab] OR exercise[tiab] OR sedentary[tiab] OR sitting time[tiab] OR inactivit*[tiab] OR diet[tiab] OR dietary[tiab] OR eating behavior*[tiab] OR eating behaviour*[tiab] OR food consumption[tiab] OR nutrition[tiab] OR sleep[tiab] OR sleep quality[tiab] OR sleep duration[tiab] OR alcohol[tiab] OR drinking[tiab] OR smoking[tiab] OR tobacco[tiab] OR well-being[tiab] OR wellbeing[tiab] OR mental health[tiab] OR psychological well-being[tiab] OR quality of life[tiab] OR life satisfaction[tiab] OR psychological distress[tiab] OR depress*[tiab] OR anxiet*[tiab] OR stress[tiab] OR loneliness[tiab] OR social isolation[tiab] OR Obsessive-Compulsive Disorder[Mesh] OR mobility[tiab] OR protective behavio*[tiab] OR protective behaviour*[tiab] OR compliance[tiab] OR OCD[tiab] OR obsessive-compulsive[tiab] OR obsessive compulsive[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR substance use[tiab] OR substance-use[tiab] OR substance misuse[tiab] OR drug use[tiab] OR drug-use[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 23 | 23 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being | AND-ed | 97,901 / 13,167 | 86.6% | none | 0/30 (up to 10% of removed records could be relevant) | The current 30-record loss sample had no eligible study: it included one cross-sectional COVID-19 knowledge survey that mentioned awareness of preventive measures but did not measure behavior/compliance or well-being; the remaining records were clinical/biomedical, commentary, or unrelated coronavirus studies. The block retains all 23 screened relevant development records and cuts the base query by 86.6% (97,901 to 13,167), materially reducing screening. The count remains 3,167 over the 10,000-record workload budget; no independent validation set was held out. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid | 4,701,688 | 0 |
| outcomes | 97,901 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 122,880 | initial | none | Initial recall-first exposure block; combined OR outcome block retained as optional for measurement because outcomes are named variably. |
| 2 | 91,779 | covid: +0 / -4 | none | Narrowed exposure vocabulary by removing generic pandemic and quarantine headings/words that admitted unrelated outbreaks; screened 60 candidate records and included in-scope studies in relevant set; an optional-block loss sample included a protective-health-behavior study. |
| 3 | 97,901 | covid: +2 / -0 | none | Added SARS-CoV-2[Mesh], a heading observed in screened relevant records via term ranking, and coronavirus[tiab] to broaden the exposure wording; no known record should be lost. Outcome block remains optional and excluded after documented losses. |
| 4 | 97,901 | limits/combination | none | Removed an accidental duplicate MeSH term while retaining the ranked SARS-CoV-2 heading and coronavirus text word; current optional decision requires a refreshed sample. |
| 5 | 97,901 | limits/combination | none | Expanded optional outcome vocabulary after screening current loss samples: mobility restriction impact and behavior/adherence phrasing were missing, and a relevant OCD symptom study lacked common well-being labels. These terms improve measurement of the optional concept; its prior decision is stale and will be refreshed. |
| 6 | 0 | outcomes: +61 / -0 | none | AND-ed the expanded optional lifestyle/well-being block after a current 30-record loss sample had no relevant records, 23 development records were retained, and the block reduced count 86.6%. Final count is still over the workload budget; retain high sensitivity and ask critic to disposition this. |
| 7 | 13,065 | outcomes: +60 / -0 | none | Removed the malformed Food and Nutrition[Mesh] term flagged by lint; Diet[Mesh] and dietary text vocabulary remain. Optional decision is stale after this block correction and will be refreshed. |
| 8 | 13,065 | outcomes: +0 / -1 | none | Removed Psychological Well-Being[Mesh] because the authority record says it was introduced in 2023, after the run cutoff, and its tested query returned zero records; free-text well-being terms remain. Removed malformed Food and Nutrition[Mesh], preserving Diet[Mesh] and dietary words. Refresh optional decision after these changes. |
| 9 | 13,167 | outcomes: +5 / -0 | none |  |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 8: 1 findings; F1 must-fix resolved
- Round 2 on version 9: 1 findings; F1 must-fix resolved
- Round 3 on version 9: 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2296 NCBI requests logged (947 from cache); strategy sha256 2df596cefb36._

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
        "message": "13,167 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "13,167 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
        "text": "Life Style",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Healthy Lifestyle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "Healthy Lifestyle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "Sedentary Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
        "text": "Alcohol Drinking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
        "text": "Smoking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Quality of Life",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Stress, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Social Isolation",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Obsessive-Compulsive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:51:04+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009771",
          "name": "Obsessive-Compulsive Disorder",
          "type": "descriptor",
          "scope_note": "An anxiety disorder characterized by recurrent, persistent obsessions or compulsions. Obsessions are the intrusive ideas, thoughts, or images that are experienced as senseless or repugnant. Compulsions are repetitive and seemingly purposeful behavior which the individual generally recognizes as senseless and from which the individual does not derive pleasure although it may provide a release fr...",
          "tree_numbers": [
            "F03.080.600"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009771",
      "preferred_label": "Obsessive-Compulsive Disorder",
      "type": "descriptor",
      "location": "vocabulary:72",
      "term": {
        "text": "Obsessive-Compulsive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"COVID\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"self-quarantine\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"physical distancing\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"movement control\"[Title/Abstract] OR \"coronavirus\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"healthy lifestyle\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"alcohol drinking\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"anxiety\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"social isolation\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"life style\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"health habit*\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting time\"[Title/Abstract] OR \"inactivit*\"[Title/Abstract] OR \"diet\"[Title/Abstract] OR \"dietary\"[Title/Abstract] OR \"eating behavior*\"[Title/Abstract] OR \"eating behaviour*\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"nutrition\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"sleep quality\"[Title/Abstract] OR \"sleep duration\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"psychological well being\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"psychological distress\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"anxiet*\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"social isolation\"[Title/Abstract] OR \"obsessive compulsive disorder\"[MeSH Terms] OR \"mobility\"[Title/Abstract] OR \"protective behavio*\"[Title/Abstract] OR \"protective behaviour*\"[Title/Abstract] OR \"compliance\"[Title/Abstract] OR \"OCD\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"behavior*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract] OR \"substance-use\"[Title/Abstract] OR \"substance-use\"[Title/Abstract] OR \"substance misuse\"[Title/Abstract] OR \"drug-use\"[Title/Abstract] OR \"drug-use\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 8,
      "review_sha256": "0e829e6d8466f0d5d6e3278975db4bdd0221db982f3b79312be97ece7b7fc167",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility names substance use as an outcome, but the text-word block has no bare substance-use term; alcohol and tobacco terms do not cover that named member."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within blocks, AND across two blocks."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Headings cover areas; newer well-being heading excluded for cutoff."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add bare phrase substance use and spelling or hyphenation variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax diagnostics; valid tags/parentheses/date entry."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Entrez cutoff, no [dp] or filters."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes substance use but block has alcohol, drinking, smoking, tobacco without bare substance use term.",
          "recommendation": "Add substance use[tiab] and relevant spelling/hyphenation variants then rerun complete evaluation.",
          "status": "resolved",
          "response": "Added substance use, substance-use, substance misuse, drug use, and drug-use text-word terms. Re-evaluation increased retrieval by 102 and retained all 23 known relevant development records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional outcome block was tested and adopted; excess over workload budget is documented. The updated vocabulary slightly increases the count but does not change this disposition.",
          "evidence": "Block reduces 97,901 to 13,167 (86.6%), retains all 23 screened relevant development records, refreshed 30-record loss sample found 0 eligible. Final count remains 3,167 above 10,000 budget."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 9,
      "review_sha256": "e6b81ae3c3258644fcddae1b9de68329d7e523285225d8e6407d92a7a649e2c7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The outcome block now includes the bare substance use term and related variants. The other named eligibility outcomes are represented; no directional process term needs expansion."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure and outcome terms are OR-combined within blocks, and the blocks are AND-combined."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings cover the listed lifestyle and well-being areas, and the packet documents the cutoff rationale for excluding the newer Psychological Well-Being heading."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The outcome terms include the named behavior and well-being concepts, including substance use and drug use variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query diagnostics; the final strategy uses valid field tags, Boolean grouping, and date-entry syntax."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date cutoff is applied, with no publication-date limit or other unsupported filter."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes substance use but the earlier outcome block had alcohol, drinking, smoking, and tobacco terms without the bare substance use term.",
          "recommendation": "Add substance use[tiab] and relevant spelling or hyphenation variants, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The strategy adds substance use, substance-use, substance misuse, drug use, and drug-use text-word terms. Re-evaluation increased retrieval by 102 records and retained all 23 known relevant development records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional outcome block was tested and adopted. The remaining excess over the workload budget is documented; narrowing further could exclude eligible records.",
          "evidence": "The block reduces retrieval from 97,901 to 13,167 (86.6%), retains all 23 screened relevant development records, and the refreshed 30-record loss sample found no eligible studies. The final count is 3,167 above the 10,000-record budget; no independent validation set was held out."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 9,
      "review_sha256": "e6b81ae3c3258644fcddae1b9de68329d7e523285225d8e6407d92a7a649e2c7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The current outcome block contains the bare substance use term and related variants, resolving F1. The other named eligibility outcomes are represented."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within exposure and outcome blocks, with the blocks AND-combined."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings cover the listed lifestyle and well-being areas. The packet documents the cutoff rationale for excluding the newer Psychological Well-Being heading."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover the named behavior and well-being concepts, including substance use."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax diagnostics; the final query uses field tags, Boolean grouping, and date-entry syntax."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date cutoff is applied without a publication-date limit or other unsupported filter."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes substance use, which was absent as a bare text-word term in the earlier strategy.",
          "recommendation": "Add substance use[tiab] and relevant spelling or hyphenation variants, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current strategy includes substance use, substance-use, substance misuse, drug use, and drug-use terms. The re-evaluation increased retrieval by 102 and retained all 23 known relevant development records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional outcome block was tested and adopted. Its remaining excess over the workload budget is documented.",
          "evidence": "The block reduces retrieval from 97,901 to 13,167 (86.6%), retains all 23 screened relevant development records, and the current 30-record loss sample found no eligible studies. The final count is 3,167 above the 10,000-record budget; no independent validation set was held out."
        }
      ]
    }
  ]
}
```


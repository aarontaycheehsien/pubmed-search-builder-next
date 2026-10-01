# PubMed search strategy: audit

Generated 2026-10-01T13:01:59+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Delivered over an open critic objection

The internal critic's closing round left these must-fix findings open. The query was delivered with them overridden; the peer reviewer should decide each one.

- **R2-F1** (translation, lexical): The current exposure block adds bare lockdown*[tiab] and lock-down*[tiab], but restriction wording remains limited to phrases; bare restrict*[tiab] is absent.
  - Critic recommended: Add bare restriction wording such as restrict*[tiab] and run a complete evaluation.
  - Reason for overriding: I tested the critic's suggested bare restrict*[tiab] term in the exposure block and fully evaluated it. PSB eval increased the final count from 15,705 to 118,555 (+102,850) with no newly retrieved known relevant records; the generic stem is highly nonspecific and returns restrictions in unrelated clinical contexts. The delivered block includes bare lockdown*[tiab] and lock-down*[tiab], stay-at-home and shelter-in-place variants, plus explicit movement/pandemic/public-health restriction phrases alongside COVID-19 and coronavirus terms. I therefore reject bare restrict*[tiab] on the measured retrieval burden while preserving restriction vocabulary that is tied to the review's topic.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: yes (Proceeding without clarification at user's request. Assumed population is humans generally; eligible impacts may be measured during any pandemic phase and may concern lifestyle behaviors and/or well-being. No language, age, geography or publication-date limit. PubMed is bounded by Entrez date through PSB_AS_OF=2020-11-22 on every command; no publication-date limit is applied. No user-supplied seeds or matching prior-review benchmark were available. Eighteen records from title/abstract pilot samples were screened and used as a development set; recall against them is not independent validation.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related restrictions | search | The exposure is central and must be present; the review is specifically about COVID-19, so a COVID-19/SARS-CoV-2/coronavirus block is required. Generic pandemic and isolation wording is not used alone because it retrieves unrelated historical epidemics and isolates. |
| Lifestyle behaviors or well-being | optional | The question includes either lifestyle behavior changes or well-being outcomes. The composite OR block is tested as an optional outcome concept because these topic-defining outcomes may be named inconsistently and forcing both would lose eligible records. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T13:00:10+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 15,705
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"COVID-19"[Mesh]` | 57,089 | none |
| 2 | `"SARS-CoV-2"[Mesh]` | 45,931 | none |
| 3 | `"Coronavirus Infections"[Mesh]` | 67,535 | none |
| 4 | `"Coronavirus"[Mesh]` | 58,220 | none |
| 5 | `COVID-19[tiab]` | 67,388 | none |
| 6 | `COVID19[tiab]` | 64,206 | none |
| 7 | `"COVID 19"[tiab]` | 67,388 | none |
| 8 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 9 | `"SARS CoV 2"[tiab]` | 23,503 | none |
| 10 | `2019-nCoV[tiab]` | 1,288 | none |
| 11 | `"2019 novel coronavirus"[tiab]` | 1,176 | none |
| 12 | `"novel coronavirus"[tiab]` | 6,179 | none |
| 13 | `coronavirus*[tiab]` | 43,050 | none |
| 14 | `"COVID-19 pandemic"[tiab]` | 20,381 | none |
| 15 | `"COVID-19 lockdown"[tiab]` | 616 | none |
| 16 | `"coronavirus lockdown"[tiab]` | 23 | none |
| 17 | `"COVID-19 confinement"[tiab]` | 46 | none |
| 18 | `"COVID-19 quarantine"[tiab]` | 100 | none |
| 19 | `lockdown*[tiab]` | 3,416 | none |
| 20 | `lock-down*[tiab]` | 178 | none |
| 21 | `"stay at home"[tiab]` | 815 | none |
| 22 | `"stay-at-home"[tiab]` | 815 | none |
| 23 | `"shelter in place"[tiab]` | 210 | none |
| 24 | `"shelter-in-place"[tiab]` | 210 | none |
| 25 | `"movement restriction*"[tiab]` | 568 | none |
| 26 | `"pandemic restriction*"[tiab]` | 26 | none |
| 27 | `"public health restriction*"[tiab]` | 16 | none |
| 28 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27` | 98,285 | none |
| 29 | `"Life Style"[Mesh]` | 99,996 | none |
| 30 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 31 | `"Health Risk Behaviors"[Mesh]` | 780 | none |
| 32 | `"Motor Activity"[Mesh]` | 309,966 | none |
| 33 | `"Exercise"[Mesh]` | 212,859 | none |
| 34 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 35 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 36 | `"Hygiene"[Mesh]` | 42,917 | none |
| 37 | `"Mental Health"[Mesh]` | 44,674 | none |
| 38 | `"Quality of Life"[Mesh]` | 215,482 | none |
| 39 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 40 | `"Anxiety"[Mesh]` | 93,320 | none |
| 41 | `"Depression"[Mesh]` | 129,618 | none |
| 42 | `"Psychological Distress"[Mesh]` | 4,500 | none |
| 43 | `"Sleep Wake Disorders"[Mesh]` | 96,238 | none |
| 44 | `"Smoking"[Mesh]` | 152,983 | none |
| 45 | `"Diet"[Mesh]` | 296,758 | none |
| 46 | `lifestyle[tiab]` | 99,644 | none |
| 47 | `"life style"[tiab]` | 11,282 | none |
| 48 | `"health behavio*"[tiab]` | 25,773 | none |
| 49 | `"health practice*"[tiab]` | 6,617 | none |
| 50 | `"health habit*"[tiab]` | 1,418 | none |
| 51 | `"physical activ*"[tiab]` | 118,343 | none |
| 52 | `exercise[tiab]` | 272,207 | none |
| 53 | `exercis*[tiab]` | 307,828 | none |
| 54 | `sedentary[tiab]` | 32,472 | none |
| 55 | `inactiv*[tiab]` | 308,257 | none |
| 56 | `"screen time"[tiab]` | 2,454 | none |
| 57 | `diet*[tiab]` | 587,723 | none |
| 58 | `nutrition*[tiab]` | 299,576 | none |
| 59 | `eating[tiab]` | 77,769 | none |
| 60 | `food consum*[tiab]` | 15,783 | none |
| 61 | `sleep[tiab]` | 171,185 | none |
| 62 | `insomnia[tiab]` | 22,051 | none |
| 63 | `smok*[tiab]` | 287,931 | none |
| 64 | `tobacco[tiab]` | 104,259 | none |
| 65 | `alcohol[tiab]` | 263,050 | none |
| 66 | `drinking[tiab]` | 114,398 | none |
| 67 | `substance use[tiab]` | 37,851 | none |
| 68 | `addict*[tiab]` | 67,929 | none |
| 69 | `daily routin*[tiab]` | 4,302 | none |
| 70 | `hygien*[tiab]` | 81,734 | none |
| 71 | `handwash*[tiab]` | 2,902 | none |
| 72 | `"hand washing"[tiab]` | 2,697 | none |
| 73 | `"personal care"[tiab]` | 5,310 | none |
| 74 | `wellbeing[tiab]` | 91,505 | none |
| 75 | `well-being[tiab]` | 80,676 | none |
| 76 | `"well being"[tiab]` | 80,676 | none |
| 77 | `"mental health"[tiab]` | 159,665 | none |
| 78 | `"psychological health"[tiab]` | 5,521 | none |
| 79 | `"psychological well-being"[tiab]` | 9,542 | none |
| 80 | `"quality of life"[tiab]` | 282,526 | none |
| 81 | `distress[tiab]` | 119,022 | none |
| 82 | `stress[tiab]` | 779,146 | none |
| 83 | `anxiet*[tiab]` | 201,789 | none |
| 84 | `depress*[tiab]` | 474,400 | none |
| 85 | `mood[tiab]` | 76,259 | none |
| 86 | `loneliness[tiab]` | 6,825 | none |
| 87 | `social support[tiab]` | 40,801 | none |
| 88 | `psychosocial[tiab]` | 102,025 | none |
| 89 | `resilien*[tiab]` | 35,817 | none |
| 90 | `#29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89` | 4,511,786 | none |
| 91 | `#28 AND #90` | 15,705 | none |

### Strategy (single line, for copying into PubMed)

```text
(("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR "Coronavirus Infections"[Mesh] OR "Coronavirus"[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR "COVID 19"[tiab] OR SARS-CoV-2[tiab] OR "SARS CoV 2"[tiab] OR 2019-nCoV[tiab] OR "2019 novel coronavirus"[tiab] OR "novel coronavirus"[tiab] OR coronavirus*[tiab] OR "COVID-19 pandemic"[tiab] OR "COVID-19 lockdown"[tiab] OR "coronavirus lockdown"[tiab] OR "COVID-19 confinement"[tiab] OR "COVID-19 quarantine"[tiab] OR lockdown*[tiab] OR lock-down*[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "shelter in place"[tiab] OR "shelter-in-place"[tiab] OR "movement restriction*"[tiab] OR "pandemic restriction*"[tiab] OR "public health restriction*"[tiab]) AND ("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Health Risk Behaviors"[Mesh] OR "Motor Activity"[Mesh] OR "Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Hygiene"[Mesh] OR "Mental Health"[Mesh] OR "Quality of Life"[Mesh] OR "Stress, Psychological"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR "Psychological Distress"[Mesh] OR "Sleep Wake Disorders"[Mesh] OR "Smoking"[Mesh] OR "Diet"[Mesh] OR lifestyle[tiab] OR "life style"[tiab] OR "health behavio*"[tiab] OR "health practice*"[tiab] OR "health habit*"[tiab] OR "physical activ*"[tiab] OR exercise[tiab] OR exercis*[tiab] OR sedentary[tiab] OR inactiv*[tiab] OR "screen time"[tiab] OR diet*[tiab] OR nutrition*[tiab] OR eating[tiab] OR food consum*[tiab] OR sleep[tiab] OR insomnia[tiab] OR smok*[tiab] OR tobacco[tiab] OR alcohol[tiab] OR drinking[tiab] OR substance use[tiab] OR addict*[tiab] OR daily routin*[tiab] OR hygien*[tiab] OR handwash*[tiab] OR "hand washing"[tiab] OR "personal care"[tiab] OR wellbeing[tiab] OR well-being[tiab] OR "well being"[tiab] OR "mental health"[tiab] OR "psychological health"[tiab] OR "psychological well-being"[tiab] OR "quality of life"[tiab] OR distress[tiab] OR stress[tiab] OR anxiet*[tiab] OR depress*[tiab] OR mood[tiab] OR loneliness[tiab] OR social support[tiab] OR psychosocial[tiab] OR resilien*[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 19 | 19 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors or well-being | AND-ed | 98,285 / 15,705 | 84.0% | none | 0/30 (up to 10% of removed records could be relevant) | The composite outcome block still covers either lifestyle behavior or well-being. The revised outcome test retains all 19 screened development records, including the hygiene record, and reduces the revised core exposure set to 15,705; the fresh 30-record loss sample contained no eligible record. The outcome block remains necessary to limit retrieval after adding bare lockdown and specific restriction terms. The count is above the 10,000 budget, and the spent category probe's 45-record residual estimate remains an accepted-risk item for the peer reviewer. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Lifestyle behaviors or well-being | 1 | `(health behavio*[tiab] OR physical activ*[tiab] OR sedentary[tiab] OR diet*[tiab] OR sleep[tiab] OR smok*[tiab] OR alcohol[tiab] OR addiction*[tiab] OR routine*[tiab] OR stress[tiab] OR anxiety[tiab] OR depression[tiab] OR psychosocial[tiab] OR mental health[tiab] OR quality of life[tiab] OR social support[tiab])` | 1,352 | 0/30 |
| Lifestyle behaviors or well-being | 2 | `(health behavio*[tiab] OR physical activ*[tiab] OR sedentary[tiab] OR diet*[tiab] OR sleep[tiab] OR smok*[tiab] OR alcohol[tiab] OR addiction*[tiab] OR routine*[tiab] OR stress[tiab] OR anxiety[tiab] OR depression[tiab] OR psychosocial[tiab] OR mental health[tiab] OR quality of life[tiab] OR social support[tiab])` | 1,352 | 1/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| pandemic_exposure | 4,511,786 | 0 |
| impact_outcomes | 98,285 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 515,823 | initial | none | Initial recall-first strategy: COVID/pandemic/restriction exposure is the core search block; lifestyle and well-being are separately tested optional outcome blocks, left out of the query pending optional tests. |
| 2 | 97,141 | pandemic_exposure: +6 / -17 | none | Revised the core to require explicit COVID-19/coronavirus exposure wording, removing stand-alone generic epidemic, pandemic, isolation and quarantine terms that inflated retrieval with unrelated history. Combined lifestyle and well-being into one OR outcome candidate because either outcome can qualify; it is tested as optional. |
| 3 | 14,407 | impact_outcomes: +57 / -0 | none | Applied measured decision to AND the combined optional outcome block; 18 screened development records are retained and the loss sample has no eligible record. |
| 4 | 14,407 | impact_outcomes: +0 / -1 | none | Removed the Psychological Well-Being MeSH heading after PubMed returned no records and warned 'No items found' under the Entrez cutoff; free-text well-being, mental health, psychological health and quality-of-life terms remain. The development set remains fully retrieved. |
| 5 | 15,357 | impact_outcomes: +5 / -0 | none | Added Hygiene[Mesh] and hygiene/handwashing text terms after category probe 2 identified a relevant pre/post pandemic hygiene-habit study outside the outcome block. |
| 6 | 118,555 | pandemic_exposure: +7 / -0 | none | Addressed critic round 2 must-fix: added explicit lockdown, restriction, stay-at-home and shelter-in-place terms to the exposure block. This broadens retrieval to measures named without adjacent COVID wording; optional decision and category evidence are reassessed because the query changed. |
| 7 | 15,705 | pandemic_exposure: +3 / -1 | none | Refined the critic-requested exposure wording: retained bare lockdown/lock-down and stay-at-home/shelter-in-place terms, while replacing the highly nonspecific restrict* stem with specific movement, pandemic and public-health restriction phrases to limit irrelevant retrieval. Re-evaluate all measures and optional evidence. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 0 findings; 
- Round 2 on version 5: 2 findings; R2-F1 must-fix open, R2-F2 should-fix open
- Round 3 on version 7: 2 findings; R2-F1 must-fix open, R2-F2 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2302 NCBI requests logged (1315 from cache); strategy sha256 aa66c3938f8b._

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
        "message": "15,705 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:impact_outcomes",
        "blocking": false,
        "requires_review": true,
        "id": "I-2025cc2bc155e76700f8"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "15,705 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:impact_outcomes",
        "blocking": false,
        "requires_review": true,
        "id": "I-2025cc2bc155e76700f8"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "requested": "Coronavirus",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017934",
          "name": "Coronavirus",
          "type": "descriptor",
          "scope_note": "A member of CORONAVIRIDAE which causes respiratory or gastrointestinal disease in a variety of vertebrates.",
          "tree_numbers": [
            "B04.820.578.500.540.150"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017934",
      "preferred_label": "Coronavirus",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Coronavirus\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Risk Behaviors",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Health Risk Behaviors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Motor Activity\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
    },
    {
      "requested": "Hygiene",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006920",
          "name": "Hygiene",
          "type": "descriptor",
          "scope_note": "The science dealing with the establishment and maintenance of health in the individual and the group. It includes the conditions and practices conducive to health. (Webster, 3d ed)",
          "tree_numbers": [
            "E02.547",
            "N06.850.670"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006920",
      "preferred_label": "Hygiene",
      "type": "descriptor",
      "location": "vocabulary:35",
      "term": {
        "text": "\"Hygiene\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
        "text": "\"Anxiety\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "requested": "Sleep Wake Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012893",
          "name": "Sleep Wake Disorders",
          "type": "descriptor",
          "scope_note": "Abnormal sleep-wake schedule or pattern associated with the CIRCADIAN RHYTHM which affect the length, timing, and/or rigidity of the sleep-wake cycle relative to the day-night cycle.",
          "tree_numbers": [
            "C10.886",
            "C23.888.592.796",
            "F03.870"
          ],
          "entry_terms": 37,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012893",
      "preferred_label": "Sleep Wake Disorders",
      "type": "descriptor",
      "location": "vocabulary:42",
      "term": {
        "text": "\"Sleep Wake Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T13:00:10+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"covid 19\"[MeSH Terms] OR \"sars cov 2\"[MeSH Terms] OR \"Coronavirus Infections\"[MeSH Terms] OR \"Coronavirus\"[MeSH Terms] OR \"covid 19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"covid 19\"[Title/Abstract] OR \"sars cov 2\"[Title/Abstract] OR \"sars cov 2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"COVID-19 pandemic\"[Title/Abstract] OR \"COVID-19 lockdown\"[Title/Abstract] OR \"coronavirus lockdown\"[Title/Abstract] OR \"COVID-19 confinement\"[Title/Abstract] OR \"COVID-19 quarantine\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"pandemic restriction*\"[Title/Abstract] OR \"public health restriction*\"[Title/Abstract]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Health Risk Behaviors\"[MeSH Terms] OR \"Motor Activity\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Hygiene\"[MeSH Terms] OR \"Mental Health\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"Psychological Distress\"[MeSH Terms] OR \"Sleep Wake Disorders\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"Life Style\"[Title/Abstract] OR \"health behavio*\"[Title/Abstract] OR \"health practice*\"[Title/Abstract] OR \"health habit*\"[Title/Abstract] OR \"physical activ*\"[Title/Abstract] OR \"Exercise\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"inactiv*\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"food consum*\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"insomnia\"[Title/Abstract] OR \"smok*\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"drinking\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"addict*\"[Title/Abstract] OR \"daily routin*\"[Title/Abstract] OR \"hygien*\"[Title/Abstract] OR \"handwash*\"[Title/Abstract] OR \"hand washing\"[Title/Abstract] OR \"personal care\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"psychological health\"[Title/Abstract] OR \"psychological well-being\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"distress\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"anxiet*\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"mood\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"social support\"[Title/Abstract] OR \"psychosocial\"[Title/Abstract] OR \"resilien*\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "532dfa1d7c0c3f12ffb99b2ac0e93a2ab93240f6ea8d455247f43f15b3915f9e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The COVID-19 exposure block and lifestyle or well-being outcome block cover the defined concepts. The outcome alternatives are joined with OR; all 19 known records are retrieved by both blocks."
        },
        "operators": {
          "verdict": "pass",
          "note": "The COVID-19 exposure block is AND-ed with the composite optional outcome block; synonyms within each block are OR-ed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant disease, behavior, activity, and well-being MeSH headings appear alongside free-text terms. The packet reports no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover COVID-19 and coronavirus variants, restrictions, lifestyle behaviors, and well-being outcomes. The known set is fully retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or geography limit is applied. The Entrez date bound is documented as a PubMed environment constraint, not a review limit."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Retain the optional outcome block and screen the resulting set. The strategy is within the rules for AND-ing the block, and the workload excess is a review burden rather than a reason to force a narrower search.",
          "evidence": "The block reduces results from 97,141 to 15,357; it retains all 19 known records with none lost, and the loss sample found 0 relevant records among 30. The final count exceeds the 10,000 workload budget."
        },
        {
          "issue_id": "I-c527fc7d783c4da67933",
          "status": "accepted-risk",
          "response": "Keep the broadened outcome block and screen the retrieved records. The probe finding warrants caution about recall, but no further specific term change can be assessed within the spent standard-depth probe budget.",
          "evidence": "The second probe found PMID 32573966 among 30 screened records. Hygiene[Mesh] and hygiene/handwashing terms were added; the current block retrieves the record and all 19 known records. The probe budget is spent. The probe estimated 45 relevant records outside the block after widening."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "532dfa1d7c0c3f12ffb99b2ac0e93a2ab93240f6ea8d455247f43f15b3915f9e",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The exposure block covers COVID-19 and coronavirus wording, but represents lockdown only in phrases tied to COVID-19 or coronavirus. The question explicitly names related lockdown measures; add their bare wording to meet the translation check."
        },
        "operators": {
          "verdict": "revise",
          "note": "The blocks are combined as intended, but the category probe estimated relevant records may remain outside the outcome block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant COVID-19, behavior, activity, and well-being MeSH headings alongside free-text terms. The packet reports verified headings and no translation issues."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The exposure text words lack standalone lockdown or restriction wording. Add explicit terms for the named measures and evaluate the revised search."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or geography limits are applied. The Entrez date bound is documented as a PubMed environment constraint."
        }
      },
      "findings": [
        {
          "id": "R2-F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The question names related lockdown measures, but the exposure block represents lockdown only in phrases such as COVID-19 lockdown and coronavirus lockdown. It contains no bare lockdown or restriction wording.",
          "recommendation": "Add explicit terms such as lockdown*[tiab] and restrict*[tiab] to the exposure block, then run a complete evaluation of the revised strategy.",
          "status": "open"
        },
        {
          "id": "R2-F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The optional outcome block is AND-ed despite probe evidence of residual recall risk: the second category probe found a relevant record among 30 screened, and the packet estimates 45 relevant records outside the widened outcome block.",
          "recommendation": "Consider leaving the optional outcome block out and screening the larger COVID-19 set, or broaden/reword the block and fully reevaluate it.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Screening above the workload budget is a documented choice; the outcome block controls a far larger result set while preserving the known development set.",
          "evidence": "The then-current result count exceeded 10,000, and the tested outcome block retained all known records with none lost in a 30-record loss sample."
        },
        {
          "issue_id": "I-c527fc7d783c4da67933",
          "status": "rejected",
          "response": "The earlier acceptance of residual category risk is inadequate for a recall-first search; the probe finding calls for adding the named behavior to the block and reevaluating it.",
          "evidence": "The second probe found PMID 32573966 among 30 records outside the then-current outcome block. The probe budget was spent and the packet estimated additional relevant records might remain outside."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 7,
      "review_sha256": "33a282dda121505a5728b44f6764e3255c4546eabb3c41a07cfa022c1ca34904",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "R2-F1 remains open: bare lockdown wording was added, but no unrestricted restrict*[tiab] term is present."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concepts are combined as intended. The residual category risk is accepted with the probe limitation documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant COVID-19, behavior, activity, hygiene and well-being MeSH headings, and the packet reports verified headings."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Bare lockdown wording was added, resolving part of R2-F1; only phrase-specific restriction wording remains."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The evaluation reports no PubMed query errors, warnings or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age or geography review limit is applied; the Entrez date bound is an environment constraint."
        }
      },
      "findings": [
        {
          "id": "R2-F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The current exposure block adds bare lockdown*[tiab] and lock-down*[tiab], but restriction wording remains limited to phrases; bare restrict*[tiab] is absent.",
          "recommendation": "Add bare restriction wording such as restrict*[tiab] and run a complete evaluation.",
          "status": "open"
        },
        {
          "id": "R2-F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The optional outcome block remains AND-ed while the category probe budget is spent and estimated relevant records might remain outside it.",
          "recommendation": "Accept the residual risk and screen the retrieved set; the optional block is permissible given 19 known records retained and the current loss sample.",
          "status": "accepted-risk",
          "response": "Added hygiene and handwashing terms after the probe found a relevant hygiene-habit study and fully reevaluated the strategy. The current block retains all 19 screened development records and the fresh 30-record optional loss sample found no eligible records. The remaining estimate of 45 relevant records outside the widened block and inability to run another probe are documented; the 15,705-record workload is accepted for peer-review consideration."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Retain the outcome block to reduce the COVID-19 set and screen the resulting records despite the workload excess.",
          "evidence": "The block reduces the exposure set from 98,285 to 15,705, retains all 19 known records with none lost, and the current 30-record loss sample found 0 relevant records. The final count exceeds the 10,000 budget."
        },
        {
          "issue_id": "I-2025cc2bc155e76700f8",
          "status": "accepted-risk",
          "response": "The category probe budget is spent and the block changed after the final recorded probe. The exact current version could not be probed again; retain the limitation and screen the retrieved set.",
          "evidence": "The second probe found PMID 32573966 among 30 records, prompting Hygiene[Mesh] and hygiene/handwashing terms. The revised block retrieves all 19 known records; its current optional loss sample found 0 eligible records among 30. The probe budget prevents another draw, and the previous probe estimated 45 relevant records could remain outside."
        }
      ]
    }
  ]
}
```


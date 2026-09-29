# PubMed search strategy: audit

Generated 2026-09-29T03:23:12+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User said they cannot answer questions during this run and asked us to proceed with reasonable assumptions. Scope was not confirmed. Interpreted the question as exposure (PECO), with no age, geography, design, language, or publication-date limits. Used the requested historical PubMed Entrez-date cutoff 2020-11-22; no [dp] limit. No known relevant articles were supplied. Search is an initial draft requiring PRESS review. A category probe identified a potentially relevant study of hygiene habits and mobility patterns; these named lifestyle members were added to the outcome vocabulary and criteria.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown or public health restrictions | search | The exposure defines eligibility; COVID-19 terms and restriction terminology should be searchable, with member-only lockdown language checked by probing. |
| Lifestyle behaviors and well-being outcomes | optional | Outcomes define the review topic but may be described through individual behaviors or well-being measures; test a broad outcome block before requiring it. |
| Any population | screen | No population restriction was specified. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:21:27+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 15,446
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,931 | none |
| 3 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 4 | `COVID-19[tiab]` | 67,388 | none |
| 5 | `COVID19[tiab]` | 64,206 | none |
| 6 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 7 | `SARS-CoV2[tiab]` | 1,049 | none |
| 8 | `2019-nCoV[tiab]` | 1,288 | none |
| 9 | `2019 novel coronavirus[tiab]` | 1,176 | none |
| 10 | `novel coronavirus[tiab]` | 6,179 | none |
| 11 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 12 | `COVID pandemic[tiab]` | 183 | none |
| 13 | `coronavirus pandemic[tiab]` | 1,011 | none |
| 14 | `lockdown*[tiab]` | 3,416 | none |
| 15 | `lock-down*[tiab]` | 178 | none |
| 16 | `quarantin*[tiab]` | 6,954 | none |
| 17 | `self-isolat*[tiab]` | 400 | none |
| 18 | `social distanc*[tiab]` | 3,813 | none |
| 19 | `physical distanc*[tiab]` | 1,606 | none |
| 20 | `stay-at-home[tiab]` | 815 | none |
| 21 | `stay at home[tiab]` | 815 | none |
| 22 | `shelter-in-place[tiab]` | 210 | none |
| 23 | `shelter in place[tiab]` | 210 | none |
| 24 | `home confin*[tiab]` | 140 | none |
| 25 | `home restrict*[tiab]` | 20 | none |
| 26 | `movement restrict*[tiab]` | 592 | none |
| 27 | `mobility restrict*[tiab]` | 298 | none |
| 28 | `public health measure*[tiab]` | 2,597 | none |
| 29 | `public health restriction*[tiab]` | 16 | none |
| 30 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 99,255 | none |
| 31 | `Life Style[Mesh]` | 99,996 | none |
| 32 | `Health Behavior[Mesh]` | 333,508 | none |
| 33 | `Motor Activity[Mesh]` | 309,966 | none |
| 34 | `Exercise[Mesh]` | 212,859 | none |
| 35 | `Sedentary Behavior[Mesh]` | 10,986 | none |
| 36 | `Feeding Behavior[Mesh]` | 178,421 | none |
| 37 | `Diet[Mesh]` | 296,758 | none |
| 38 | `Sleep[Mesh]` | 85,169 | none |
| 39 | `Smoking[Mesh]` | 152,983 | none |
| 40 | `Alcohol Drinking[Mesh]` | 72,506 | none |
| 41 | `Mental Health[Mesh]` | 44,674 | none |
| 42 | `Psychological Well-Being[Mesh]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 43 | `Quality of Life[Mesh]` | 215,482 | none |
| 44 | `Depression[Mesh]` | 230,067 | none |
| 45 | `Anxiety[Mesh]` | 93,320 | none |
| 46 | `Stress, Psychological[Mesh]` | 139,617 | none |
| 47 | `Substance-Related Disorders[Mesh]` | 291,305 | none |
| 48 | `lifestyle[tiab]` | 99,644 | none |
| 49 | `life style[tiab]` | 11,282 | none |
| 50 | `health behavior*[tiab]` | 18,620 | none |
| 51 | `health behaviour*[tiab]` | 7,323 | none |
| 52 | `physical activit*[tiab]` | 118,110 | none |
| 53 | `exercise[tiab]` | 272,206 | none |
| 54 | `sedentary[tiab]` | 32,472 | none |
| 55 | `sitting time[tiab]` | 1,295 | none |
| 56 | `screen time[tiab]` | 2,454 | none |
| 57 | `physical inactivity[tiab]` | 8,195 | none |
| 58 | `diet[tiab]` | 339,581 | none |
| 59 | `dietary habit*[tiab]` | 9,880 | none |
| 60 | `eating behavio*[tiab]` | 10,745 | none |
| 61 | `food intake[tiab]` | 45,992 | none |
| 62 | `nutrition*[tiab]` | 299,576 | none |
| 63 | `sleep[tiab]` | 171,185 | none |
| 64 | `sleeping[tiab]` | 20,409 | none |
| 65 | `smoking[tiab]` | 228,902 | none |
| 66 | `tobacco[tiab]` | 104,259 | none |
| 67 | `alcohol[tiab]` | 263,050 | none |
| 68 | `substance use[tiab]` | 37,851 | none |
| 69 | `mental health[tiab]` | 159,665 | none |
| 70 | `well-being[tiab]` | 80,676 | none |
| 71 | `wellbeing[tiab]` | 91,505 | none |
| 72 | `psychological well-being[tiab]` | 9,542 | none |
| 73 | `psychological distress[tiab]` | 20,154 | none |
| 74 | `quality of life[tiab]` | 282,526 | none |
| 75 | `life satisfaction[tiab]` | 8,062 | none |
| 76 | `depression[tiab]` | 348,632 | none |
| 77 | `anxiety[tiab]` | 199,917 | none |
| 78 | `stress[tiab]` | 779,146 | none |
| 79 | `loneliness[tiab]` | 6,825 | none |
| 80 | `Hygiene[Mesh]` | 42,917 | none |
| 81 | `Hand Disinfection[Mesh]` | 5,915 | none |
| 82 | `hygiene[tiab]` | 63,335 | none |
| 83 | `hygiene habit*[tiab]` | 1,001 | none |
| 84 | `handwash*[tiab]` | 2,902 | none |
| 85 | `mobility[tiab]` | 146,471 | none |
| 86 | `mobility pattern*[tiab]` | 638 | none |
| 87 | `affect[tiab]` | 682,159 | none |
| 88 | `positive affect[tiab]` | 5,963 | none |
| 89 | `negative affect[tiab]` | 10,515 | none |
| 90 | `affective well-being[tiab]` | 191 | none |
| 91 | `wellness[tiab]` | 10,646 | none |
| 92 | `psychosocial[tiab]` | 102,025 | none |
| 93 | `psychosocial adjustment[tiab]` | 2,160 | none |
| 94 | `mental state[tiab]` | 20,376 | none |
| 95 | `mental well-being[tiab]` | 2,604 | none |
| 96 | `weight gain[tiab]` | 63,433 | none |
| 97 | `sexual health[tiab]` | 10,551 | none |
| 98 | `sexual behavio*[tiab]` | 25,777 | none |
| 99 | `#31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96 OR #97 OR #98` | 4,699,340 | none |
| 100 | `#30 AND #99` | 15,446 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR Coronavirus Infections[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR SARS-CoV-2[tiab] OR SARS-CoV2[tiab] OR 2019-nCoV[tiab] OR 2019 novel coronavirus[tiab] OR novel coronavirus[tiab] OR coronavirus disease 2019[tiab] OR COVID pandemic[tiab] OR coronavirus pandemic[tiab] OR lockdown*[tiab] OR lock-down*[tiab] OR quarantin*[tiab] OR self-isolat*[tiab] OR social distanc*[tiab] OR physical distanc*[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR shelter in place[tiab] OR home confin*[tiab] OR home restrict*[tiab] OR movement restrict*[tiab] OR mobility restrict*[tiab] OR public health measure*[tiab] OR public health restriction*[tiab]) AND (Life Style[Mesh] OR Health Behavior[Mesh] OR Motor Activity[Mesh] OR Exercise[Mesh] OR Sedentary Behavior[Mesh] OR Feeding Behavior[Mesh] OR Diet[Mesh] OR Sleep[Mesh] OR Smoking[Mesh] OR Alcohol Drinking[Mesh] OR Mental Health[Mesh] OR Psychological Well-Being[Mesh] OR Quality of Life[Mesh] OR Depression[Mesh] OR Anxiety[Mesh] OR Stress, Psychological[Mesh] OR Substance-Related Disorders[Mesh] OR lifestyle[tiab] OR life style[tiab] OR health behavior*[tiab] OR health behaviour*[tiab] OR physical activit*[tiab] OR exercise[tiab] OR sedentary[tiab] OR sitting time[tiab] OR screen time[tiab] OR physical inactivity[tiab] OR diet[tiab] OR dietary habit*[tiab] OR eating behavio*[tiab] OR food intake[tiab] OR nutrition*[tiab] OR sleep[tiab] OR sleeping[tiab] OR smoking[tiab] OR tobacco[tiab] OR alcohol[tiab] OR substance use[tiab] OR mental health[tiab] OR well-being[tiab] OR wellbeing[tiab] OR psychological well-being[tiab] OR psychological distress[tiab] OR quality of life[tiab] OR life satisfaction[tiab] OR depression[tiab] OR anxiety[tiab] OR stress[tiab] OR loneliness[tiab] OR Hygiene[Mesh] OR Hand Disinfection[Mesh] OR hygiene[tiab] OR hygiene habit*[tiab] OR handwash*[tiab] OR mobility[tiab] OR mobility pattern*[tiab] OR affect[tiab] OR positive affect[tiab] OR negative affect[tiab] OR affective well-being[tiab] OR wellness[tiab] OR psychosocial[tiab] OR psychosocial adjustment[tiab] OR mental state[tiab] OR mental well-being[tiab] OR weight gain[tiab] OR sexual health[tiab] OR sexual behavio*[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 20 | 20 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being outcomes | AND-ed | 99,255 / 15,446 | 84.4% | none | 0/30 (up to 10% of removed records could be relevant) | AND the outcome block after current remeasurement: 28 known relevant records are available, the block loses none, the refreshed 30-record sample contains no relevant record, and the count falls by about 84%. The result still exceeds the assumed 10,000-record screening budget; document this workload risk. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| COVID-19 pandemic and related lockdown or public health restrictions | 1 | `coronavirus[tiab] OR SARS[tiab] OR pandemic[tiab] OR outbreak[tiab] OR lockdown[tiab] OR quarantine[tiab] OR confinement[tiab]` | 106,144 | 0/30 |
| COVID-19 pandemic and related lockdown or public health restrictions | 2 | `coronavirus[tiab] OR SARS[tiab] OR pandemic[tiab] OR outbreak[tiab] OR lockdown[tiab] OR quarantine[tiab] OR confinement[tiab]` | 12,184 | 0/30 |
| Lifestyle behaviors and well-being outcomes | 1 | `behavior*[tiab] OR behaviour*[tiab] OR activity[tiab] OR activities[tiab] OR lifestyle[tiab] OR health[tiab] OR affect[tiab] OR distress[tiab] OR wellbeing[tiab] OR well-being[tiab] OR quality[tiab]` | 26,753 | 1/30 |
| Lifestyle behaviors and well-being outcomes | 2 | `behavior*[tiab] OR behaviour*[tiab] OR activity[tiab] OR activities[tiab] OR lifestyle[tiab] OR health[tiab] OR affect[tiab] OR distress[tiab] OR wellbeing[tiab] OR well-being[tiab] OR quality[tiab]` | 24,370 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid_exposure | 4,699,340 | 0 |
| lifestyle_wellbeing | 99,255 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 557,195 | initial | none | First draft from the question; COVID/pandemic and public-health restrictions are the exposure block. Lifestyle and well-being are a broad optional candidate to test because they define outcomes but are named inconsistently. No supplied or screened known records. |
| 2 | 99,253 | covid_exposure: +0 / -8 | none | Revised exposure block to remove generic pandemic, epidemic, isolation and broad disease-outbreak headings that retrieved pre-COVID literature; retain COVID-19 language and pandemic restriction terms. No verified known records. |
| 3 | 99,253 | limits/combination | none | Expanded outcome candidate after the category probe identified a potentially in-scope record about hygiene habits and mobility patterns; screened PMID 32971081 as relevant. These behaviors fit the question's broad lifestyle scope. |
| 4 | 99,253 | limits/combination | none | Expanded outcome candidate with hygiene, mobility, and affect terms identified from screened category-probe records; candidate remains optional and the two relevant records are development evidence only. |
| 5 | 99,253 | limits/combination | none | Added 25 clearly in-scope records after screening a focused pilot query on COVID, restrictions, and lifestyle/well-being; expanded candidate vocabulary with psychosocial, mental state, diet/weight, and sexual health terms. All remain development records; no change to eligibility. |
| 6 | 15,445 | lifestyle_wellbeing: +69 / -0 | none | Applied the measured optional outcome decision: AND lifestyle/well-being with the COVID exposure block after discovery yielded 28 known relevant records (20 development, 8 validation), zero known losses, zero relevant records in the 30-record loss sample, and an 84.4% count reduction. |
| 7 | 15,445 | lifestyle_wellbeing: +0 / -1 | none | Removed unverified Personal Hygiene[Mesh], which PubMed translated through All Fields; retained the valid Hygiene and Hand Disinfection headings plus hygiene text words. This fixes a technical field-fallback defect. |
| 8 | 99,253 | lifestyle_wellbeing: +0 / -68 | none | Temporarily returned the outcome block to candidate status to refresh its loss sample after adding vocabulary and removing the invalid Personal Hygiene heading; the measured outcome decision will be reapplied after screening. |
| 9 | 15,445 | lifestyle_wellbeing: +68 / -0 | none | Reapplied the outcome AND decision using the current sampled loss set after correcting MeSH verification; confirms performance against 28 known studies. |
| 10 | 15,446 | covid_exposure: +1 / -0 | none | Added the critic-recommended public health restriction*[tiab] phrase to the exposure block; test its translation and whether it recovers additional eligible records. |
| 11 | 99,255 | lifestyle_wellbeing: +0 / -68 | none | Returned the outcome block to candidate status to refresh its optional-concept measurement after revising the exposure block as the critic requested. |
| 12 | 15,446 | lifestyle_wellbeing: +68 / -0 | none | Final evaluation after adding the critic-recommended public health restriction phrase and refreshing the optional outcome sample/decision. Recheck all 28 known records and current translation diagnostics. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 9: 4 findings; F-01 should-fix resolved, F-02 should-fix accepted-risk, F-03 document accepted-risk, F-04 should-fix accepted-risk
- Round 2 on version 12: 4 findings; F-01 should-fix resolved, F-02 should-fix accepted-risk, F-03 document accepted-risk, F-04 should-fix accepted-risk
- Round 3 on version 12: 4 findings; F-01 should-fix resolved, F-02 should-fix accepted-risk, F-03 document accepted-risk, F-04 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 3581 NCBI requests logged (1856 from cache); strategy sha256 a11f7afd673c._

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
        "message": "15,446 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:42",
        "blocking": false,
        "requires_review": true,
        "id": "I-614f0ed98a6554a7e384"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:42",
        "blocking": false,
        "requires_review": true,
        "id": "I-9de67529c3134d370a97"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "15,446 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:42",
        "blocking": false,
        "requires_review": true,
        "id": "I-614f0ed98a6554a7e384"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(Psychological Well-Being[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"psychological well being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:42",
        "blocking": false,
        "requires_review": true,
        "id": "I-9de67529c3134d370a97"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "Health Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
        "text": "Motor Activity",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
        "text": "Exercise",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Sleep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Smoking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Alcohol Drinking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "Mental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Well-Being",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "Psychological Well-Being",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "requested": "Substance-Related Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019966",
          "name": "Substance-Related Disorders",
          "type": "descriptor",
          "scope_note": "Disorders related to substance use or abuse.",
          "tree_numbers": [
            "C25.775",
            "F03.900"
          ],
          "entry_terms": 38,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019966",
      "preferred_label": "Substance-Related Disorders",
      "type": "descriptor",
      "location": "vocabulary:46",
      "term": {
        "text": "Substance-Related Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Hygiene",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
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
      "location": "vocabulary:79",
      "term": {
        "text": "Hygiene",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Hand Disinfection",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:21:27+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006235",
          "name": "Hand Disinfection",
          "type": "descriptor",
          "scope_note": "The act of cleansing the hands with water or other liquid, with or without the inclusion of soap or other detergent, for the purpose of destroying infectious microorganisms.",
          "tree_numbers": [
            "N06.850.670.150.500"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006235",
      "preferred_label": "Hand Disinfection",
      "type": "descriptor",
      "location": "vocabulary:80",
      "term": {
        "text": "Hand Disinfection",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"covid pandemic\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down*\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"social distanc*\"[Title/Abstract] OR \"physical distanc*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"home confin*\"[Title/Abstract] OR \"home restrict*\"[Title/Abstract] OR \"movement restrict*\"[Title/Abstract] OR \"mobility restrict*\"[Title/Abstract] OR \"public health measure*\"[Title/Abstract] OR \"public health restriction*\"[Title/Abstract]) AND (\"life style\"[MeSH Terms] OR \"health behavior\"[MeSH Terms] OR \"motor activity\"[MeSH Terms] OR \"exercise\"[MeSH Terms] OR \"sedentary behavior\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"sleep\"[MeSH Terms] OR \"smoking\"[MeSH Terms] OR \"alcohol drinking\"[MeSH Terms] OR \"mental health\"[MeSH Terms] OR \"psychological well being\"[MeSH Terms] OR \"quality of life\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"anxiety\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"substance related disorders\"[MeSH Terms] OR \"lifestyle\"[Title/Abstract] OR \"life style\"[Title/Abstract] OR \"health behavior*\"[Title/Abstract] OR \"health behaviour*\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercise\"[Title/Abstract] OR \"sedentary\"[Title/Abstract] OR \"sitting time\"[Title/Abstract] OR \"screen time\"[Title/Abstract] OR \"physical inactivity\"[Title/Abstract] OR \"diet\"[Title/Abstract] OR \"dietary habit*\"[Title/Abstract] OR \"eating behavio*\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"sleep\"[Title/Abstract] OR \"sleeping\"[Title/Abstract] OR \"smoking\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"alcohol\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"mental health\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"wellbeing\"[Title/Abstract] OR \"psychological well being\"[Title/Abstract] OR \"psychological distress\"[Title/Abstract] OR \"quality of life\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"depression\"[Title/Abstract] OR \"anxiety\"[Title/Abstract] OR \"stress\"[Title/Abstract] OR \"loneliness\"[Title/Abstract] OR \"hygiene\"[MeSH Terms] OR \"hand disinfection\"[MeSH Terms] OR \"hygiene\"[Title/Abstract] OR \"hygiene habit*\"[Title/Abstract] OR \"handwash*\"[Title/Abstract] OR \"mobility\"[Title/Abstract] OR \"mobility pattern*\"[Title/Abstract] OR \"affect\"[Title/Abstract] OR \"positive affect\"[Title/Abstract] OR \"negative affect\"[Title/Abstract] OR \"affective well being\"[Title/Abstract] OR \"wellness\"[Title/Abstract] OR \"psychosocial\"[Title/Abstract] OR \"psychosocial adjustment\"[Title/Abstract] OR \"mental state\"[Title/Abstract] OR \"mental well being\"[Title/Abstract] OR \"weight gain\"[Title/Abstract] OR \"sexual health\"[Title/Abstract] OR \"sexual behavio*\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 9,
      "review_sha256": "a37f94aec113886c91c876ab918f6bb326ad24448ab5c885f2160a720318c6ae",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The critic recommended an explicit public-health restriction expression; add and test a focused phrase."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR is used within concept blocks and AND between blocks; no NOT was used."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Psychological Well-Being[Mesh] is translated but has zero hits under the Entrez cutoff; document its MeSH-layer role and warning."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add and evaluate an explicit public-health restriction phrase."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Grouped clauses and field tags are valid; no syntax defect was identified."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final count exceeds the assumed workload budget; retain as a documented workload risk after optional block testing."
        }
      },
      "findings": [
        {
          "id": "F-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The exposure block lacks an explicit public health restriction expression.",
          "recommendation": "Add and evaluate public health restriction*[tiab].",
          "status": "resolved",
          "response": "Added public health restriction*[tiab] to the COVID exposure block and re-evaluated its translation, counts, and known-record retrieval."
        },
        {
          "id": "F-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The lifestyle_wellbeing category probe is stale because terms were added after the last probe and the probe budget is spent.",
          "recommendation": "Document the terms added and whether the existing samples remain informative.",
          "status": "accepted-risk",
          "response": "The second probe was screened after adding hygiene, mobility and affect terms and found no additional relevant records. Later additions came from screened relevant records (psychosocial adjustment, mental state, weight gain, sexual health and related wording). They only widened the block; consequently the unsampled remainder became smaller. The probe budget of two was spent, so this limitation is retained for PRESS review."
        },
        {
          "id": "F-03",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "reporting",
          "finding": "Psychological Well-Being[Mesh] translates but returns zero hits with a PubMed No items found warning under this date bound.",
          "recommendation": "Document the reason for retaining the heading.",
          "status": "accepted-risk",
          "response": "Retained as a valid MeSH descriptor to cover indexed well-being terminology if present. NCBI authority validation verifies the descriptor, but the PubMed query has zero records through the 2020-11-22 Entrez cutoff; free-text mental well-being, psychological well-being, and related terms provide coverage. It is an OR term and does not alter the tested result count."
        },
        {
          "id": "F-04",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "15,445 results exceed the assumed workload budget of 10,000.",
          "recommendation": "State the remaining workload risk.",
          "status": "accepted-risk",
          "response": "The optional outcome block retained 28 known relevant records, lost none, had 0 relevant records in its fresh 30-record loss sample, and cut the base count by 84.4%. The remaining 15,445 records still exceed the assumed 10,000-record budget; this is reported as an open workload risk."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The tested outcome block reduced the base count by 84.4%, retained all 28 known relevant records and had 0 relevant among the 30 screened loss records. The remaining count still exceeds the assumed workload budget.",
          "evidence": "Current diagnostic reports 15,445 versus a 10,000 budget; optional test reports 28 known records retained and 0/30 relevant in the loss sample."
        },
        {
          "issue_id": "I-f47897d33dddf6144e78",
          "status": "accepted-risk",
          "response": "The outcome-category probe budget is spent and the warning remains a limitation. The last screened probe occurred after the initial outcome vocabulary expansion; subsequent additions came from relevant records and only widened the term block.",
          "evidence": "The probe history contains two screened 30-record samples; probe 2 had zero relevant, followed by terms added from screened development records."
        },
        {
          "issue_id": "I-13b19a026497dfeb6d26",
          "status": "accepted-risk",
          "response": "Retain this valid MeSH descriptor as an OR alternative for indexed well-being terminology; the Entrez-cutoff query reports no items, while the block includes related free-text terms.",
          "evidence": "NCBI authority check verified the descriptor and PubMed translation; term count is zero as of Entrez date 2020-11-22; free-text well-being terms remain in the outcome block."
        },
        {
          "issue_id": "I-d99ff0f07b58ca68dfac",
          "status": "accepted-risk",
          "response": "The zero-hit result is documented and is not treated as evidence of invalid syntax or heading. It is a valid optional OR term supported by related text words.",
          "evidence": "The clause translates as Psychological Well-Being[MeSH Terms] with zero results for the stated Entrez cutoff; adjacent mental-health and well-being text terms are present."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 12,
      "review_sha256": "0554d1d200643b2b0eca33731ac23771c610de3e5ac89ed2e009ed91fcf1eea6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block includes the tested public-health restriction expression. The outcome block covers the named behaviors and well-being measures, including hygiene and mobility; no one-way process term was identified."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final strategy ORs terms within blocks and ANDs the exposure and optional outcome blocks. No NOT operator is used in the final query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings are translated. Psychological Well-Being[Mesh] returns zero records for the stated Entrez cutoff, but its validity and role are documented and related text-word coverage remains."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The restriction phrase requested in round 1 was added and tested. The outcome probe warning remains documented because the probe budget is spent."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final grouped query has no reported translation issues. Duplicate translated alternatives are harmless."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unintended limits are applied. The optional outcome block was tested and retains all 28 known relevant records; the remaining 15,446 records exceed the stated 10,000-record workload budget, which is documented as a risk."
        }
      },
      "findings": [
        {
          "id": "F-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The exposure block lacked an explicit public-health restriction expression.",
          "recommendation": "Add and evaluate public health restriction*[tiab].",
          "status": "resolved",
          "response": "Added public health restriction*[tiab] to the exposure block and re-evaluated the strategy."
        },
        {
          "id": "F-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The lifestyle_wellbeing probe is stale after later vocabulary additions, and the probe budget is spent.",
          "recommendation": "Document the vocabulary additions and the remaining sampling limitation.",
          "status": "accepted-risk",
          "response": "The last screened probe followed the initial vocabulary expansion; subsequent terms came from screened relevant records and widened the block. The two-probe budget is spent, so unsampled coverage remains a limitation."
        },
        {
          "id": "F-03",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "reporting",
          "finding": "Psychological Well-Being[Mesh] returns zero hits with a PubMed No items found warning under the stated date bound.",
          "recommendation": "Document why the heading is retained.",
          "status": "accepted-risk",
          "response": "Retained as a valid MeSH alternative for indexed well-being terminology. It returns zero records through the 2020-11-22 Entrez cutoff; related free-text terms remain in the outcome block."
        },
        {
          "id": "F-04",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final count of 15,446 exceeds the assumed 10,000-record workload budget.",
          "recommendation": "State the remaining workload risk.",
          "status": "accepted-risk",
          "response": "The optional outcome block reduced the base count by 84.4%, retained all 28 known relevant records, and had zero relevant records in the refreshed 30-record loss sample. The remaining count still exceeds the assumed budget."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The outcome block was tested as an optional AND block and substantially reduced the count while retaining known records and yielding no relevant records in the refreshed loss sample. The remaining excess is reported as a workload risk.",
          "evidence": "15,446 records remain against a 10,000-record budget; the block reduced the count by 84.4%, lost no known relevant records, and the loss sample had 0 relevant among 30."
        },
        {
          "issue_id": "I-f47897d33dddf6144e78",
          "status": "accepted-risk",
          "response": "The probe budget is spent. The final vocabulary additions came from screened relevant records and widened the block, but the stale-probe limitation remains.",
          "evidence": "Two probes were screened; probe 2 found 0 relevant records. Later additions came from screened development records."
        },
        {
          "issue_id": "I-614f0ed98a6554a7e384",
          "status": "accepted-risk",
          "response": "The heading is retained as a valid MeSH alternative for indexed well-being terminology; zero hits under the cutoff are documented and related text words provide coverage.",
          "evidence": "The packet documents authority validation and PubMed translation; the heading returns zero records through 2020-11-22, while mental well-being and psychological well-being text terms remain."
        },
        {
          "issue_id": "I-9de67529c3134d370a97",
          "status": "accepted-risk",
          "response": "Zero hits under the date bound do not establish an invalid heading. Retain the optional OR term with its documented role and rely on adjacent free-text coverage.",
          "evidence": "Psychological Well-Being[Mesh] translates as a MeSH term but returns zero records through 2020-11-22; related mental-health and well-being text terms are present."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 12,
      "review_sha256": "0554d1d200643b2b0eca33731ac23771c610de3e5ac89ed2e009ed91fcf1eea6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block includes COVID-19 and related restriction terms. The outcome block covers the named behavior and well-being areas, including hygiene and mobility."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query ORs synonyms within blocks and ANDs the exposure and outcome blocks. It uses no NOT operator."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings are translated. The zero-hit Psychological Well-Being heading is retained with its role and cutoff limitation documented; related text words remain."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The requested public-health restriction expression was added and evaluated. The spent outcome-probe budget and subsequent vocabulary additions are documented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final grouped query has no reported translation errors. Duplicate translated alternatives are harmless."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The stated Entrez date cutoff is applied without a population restriction. The tested outcome block retains all 28 known relevant records and reduces the count, while the remaining 15,446 records exceed the assumed 10,000-record budget; this is documented as a workload risk."
        }
      },
      "findings": [
        {
          "id": "F-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The exposure block lacked an explicit public-health restriction expression.",
          "recommendation": "Add and evaluate public health restriction*[tiab].",
          "status": "resolved",
          "response": "Added public health restriction*[tiab] to the exposure block and re-evaluated the strategy."
        },
        {
          "id": "F-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome probe is stale after later vocabulary additions, and the probe budget is spent.",
          "recommendation": "Document the vocabulary additions and remaining sampling limitation.",
          "status": "accepted-risk",
          "response": "The two-probe budget is spent. Later terms came from screened relevant records and widened the block; unsampled coverage remains a documented limitation."
        },
        {
          "id": "F-03",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "reporting",
          "finding": "Psychological Well-Being[Mesh] returns zero hits with a PubMed warning under the stated date bound.",
          "recommendation": "Document why the heading is retained.",
          "status": "accepted-risk",
          "response": "Retained as a valid MeSH alternative for indexed well-being terminology. It returns zero records through the 2020-11-22 Entrez cutoff; related free-text terms remain in the outcome block."
        },
        {
          "id": "F-04",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final count of 15,446 exceeds the assumed 10,000-record workload budget.",
          "recommendation": "State the remaining workload risk.",
          "status": "accepted-risk",
          "response": "The optional outcome block reduced the base count by 84.4%, retained all 28 known relevant records, and had zero relevant records in the refreshed 30-record loss sample. The remaining excess is documented as a workload risk."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The tested outcome block substantially reduced the count while retaining known records and yielding no relevant records in the refreshed loss sample. The remaining excess is documented as a workload risk.",
          "evidence": "15,446 records remain against a 10,000-record budget; the block reduced the count by 84.4%, lost no known relevant records, and the loss sample had 0 relevant among 30."
        },
        {
          "issue_id": "I-f47897d33dddf6144e78",
          "status": "accepted-risk",
          "response": "The probe budget is spent. Later additions came from screened relevant records and widened the block; the stale-probe limitation remains documented.",
          "evidence": "Two probes were screened; probe 2 found 0 relevant records. Later vocabulary additions came from screened development records."
        },
        {
          "issue_id": "I-614f0ed98a6554a7e384",
          "status": "accepted-risk",
          "response": "The heading is retained as a valid MeSH alternative for indexed well-being terminology; zero hits under the cutoff are documented and related text words provide coverage.",
          "evidence": "The packet documents authority validation and PubMed translation; the heading returns zero records through 2020-11-22, while mental-health and well-being text terms remain."
        },
        {
          "issue_id": "I-9de67529c3134d370a97",
          "status": "accepted-risk",
          "response": "Zero hits under the date bound do not establish an invalid heading. Retain the optional OR term with its documented role and rely on adjacent free-text coverage.",
          "evidence": "Psychological Well-Being[Mesh] translates as a MeSH term but returns zero records through 2020-11-22; related mental-health and well-being text terms are present."
        }
      ]
    }
  ]
}
```


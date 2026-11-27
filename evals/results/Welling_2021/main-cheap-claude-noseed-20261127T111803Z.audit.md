# PubMed search strategy: audit

Generated 2026-11-27T11:34:47+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: yes (User unavailable; proceeded with defaults (standard depth, no seeds, no limits). Scope not paused for confirmation. Outcomes handled as optional blocks to be measured. Outcome block AND-ed for workload (see concept rationale). OpenAlex was unavailable (daily budget exhausted), so only PubMed reference lists were used for known records. No user seeds; recall is not independently estimated. Search date cutoff 2020-11-22 (entry-date bound) is deliberate, per the run's as-of date; it is a snapshot and must be re-run for updates. Removed 'public health measure*' (sampled records were off-topic non-COVID public-health papers) and bare food/stress* (sampled records were COVID clinical papers); replaced by specific phrases. SARSCoV2[tiab] count is high because PubMed normalises it with the SARS-CoV-2 hyphen form; harmless variant. Limitations: PubMed only (no PsycINFO/Embase/preprint servers), OpenAlex unavailable, no user seeds, recall rests on 15 reference-list records (73% from one review). Bare 'distress' not searched (matches respiratory distress/ARDS); psychological/emotional/mental distress phrases and Psychological Distress[Mesh] used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and lockdown/confinement measures | search | the exposure; every relevant record involves it; reliably named and indexed |
| Lifestyle behaviors and well-being (outcomes) | search | AND-ed for workload, not on evidence: the COVID block alone returns 116,429 records, too large to screen (assumed; user unavailable). Tested on 15 records found without a keyword search (reference lists of reviews 32872154 and 33207689); none lost, but 95% upper bound on loss is 18.1%, below the 20-record evidence threshold, so loss is effectively unmeasured and the benchmark reviews are themselves outcome-focused. With the block the result is 20,951. To reverse, remove this block from the query. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T11:33:45+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 20,951
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"COVID-19"[Mesh]` | 57,100 | none |
| 2 | `"SARS-CoV-2"[Mesh]` | 45,940 | none |
| 3 | `"Pandemics"[Mesh]` | 50,286 | none |
| 4 | `"Quarantine"[Mesh]` | 3,938 | none |
| 5 | `COVID*[tiab]` | 68,970 | none |
| 6 | `"corona virus disease"[tiab]` | 522 | none |
| 7 | `"coronavirus disease"[tiab]` | 18,413 | none |
| 8 | `"corona virus"[tiab]` | 1,299 | none |
| 9 | `SARS-CoV-2[tiab]` | 23,501 | none |
| 10 | `SARS-CoV2[tiab]` | 1,050 | none |
| 11 | `SARSCoV2[tiab]` | 19,857 | none |
| 12 | `"severe acute respiratory syndrome coronavirus 2"[tiab]` | 7,984 | none |
| 13 | `nCoV[tiab]` | 1,406 | none |
| 14 | `2019-nCoV[tiab]` | 1,287 | none |
| 15 | `"novel coronavirus"[tiab]` | 6,186 | none |
| 16 | `"new coronavirus"[tiab]` | 927 | none |
| 17 | `pandemic*[tiab]` | 58,451 | none |
| 18 | `lockdown*[tiab]` | 3,419 | none |
| 19 | `"lock down"[tiab]` | 164 | none |
| 20 | `"locked down"[tiab]` | 61 | none |
| 21 | `quarantin*[tiab]` | 6,954 | none |
| 22 | `"home confinement"[tiab]` | 121 | none |
| 23 | `"stay at home"[tiab]` | 815 | none |
| 24 | `"stay-at-home"[tiab]` | 815 | none |
| 25 | `"shelter in place"[tiab]` | 210 | none |
| 26 | `"shelter-in-place"[tiab]` | 210 | none |
| 27 | `"social distanc*"[tiab]` | 3,813 | none |
| 28 | `"physical distanc*"[tiab]` | 1,606 | none |
| 29 | `"school closure*"[tiab]` | 442 | none |
| 30 | `"school closing*"[tiab]` | 31 | none |
| 31 | `"self-isolat*"[tiab]` | 400 | none |
| 32 | `"self isolat*"[tiab]` | 400 | none |
| 33 | `"movement restriction*"[tiab]` | 568 | none |
| 34 | `"containment measure*"[tiab]` | 636 | none |
| 35 | `"coronavirus 2019"[tiab]` | 1,052 | none |
| 36 | `"coronavirus disease 2019"[tiab]` | 14,609 | none |
| 37 | `"2019 novel coronavirus"[tiab]` | 1,176 | none |
| 38 | `"covid-19 outbreak"[tiab]` | 3,314 | none |
| 39 | `"coronavirus outbreak"[tiab]` | 337 | none |
| 40 | `"coronavirus epidemic"[tiab]` | 126 | none |
| 41 | `"coronavirus pandemic"[tiab]` | 1,012 | none |
| 42 | `"home isolation"[tiab]` | 109 | none |
| 43 | `curfew*[tiab]` | 170 | none |
| 44 | `"non-pharmaceutical intervention*"[tiab]` | 336 | none |
| 45 | `"nonpharmaceutical intervention*"[tiab]` | 168 | none |
| 46 | `"social restriction*"[tiab]` | 275 | none |
| 47 | `"Physical Distancing"[Mesh]` | 579 | none |
| 48 | `"confinement measure*"[tiab]` | 41 | none |
| 49 | `"covid-19 confinement"[tiab]` | 46 | none |
| 50 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49` | 116,429 | none |
| 51 | `"Life Style"[Mesh]` | 99,996 | none |
| 52 | `"Health Behavior"[Mesh]` | 333,508 | none |
| 53 | `"Exercise"[Mesh]` | 212,861 | none |
| 54 | `"Sedentary Behavior"[Mesh]` | 10,986 | none |
| 55 | `"Sleep"[Mesh]` | 85,170 | none |
| 56 | `"Sleep Wake Disorders"[Mesh]` | 96,242 | none |
| 57 | `"Diet"[Mesh]` | 296,759 | none |
| 58 | `"Feeding Behavior"[Mesh]` | 178,421 | none |
| 59 | `"Motor Activity"[Mesh]` | 309,968 | none |
| 60 | `"Screen Time"[Mesh]` | 608 | none |
| 61 | `"Alcohol Drinking"[Mesh]` | 72,506 | none |
| 62 | `"Smoking"[Mesh]` | 152,983 | none |
| 63 | `"Body Weight"[Mesh]` | 485,630 | none |
| 64 | `lifestyle*[tiab]` | 108,843 | none |
| 65 | `"life style*"[tiab]` | 12,649 | none |
| 66 | `behavior*[tiab]` | 1,024,046 | none |
| 67 | `behaviour*[tiab]` | 293,759 | none |
| 68 | `"physical activit*"[tiab]` | 118,105 | none |
| 69 | `exercis*[tiab]` | 307,814 | none |
| 70 | `sedentar*[tiab]` | 33,158 | none |
| 71 | `sitting[tiab]` | 23,130 | none |
| 72 | `sleep*[tiab]` | 188,557 | none |
| 73 | `insomnia[tiab]` | 22,051 | none |
| 74 | `diet[tiab]` | 339,570 | none |
| 75 | `diets[tiab]` | 97,812 | none |
| 76 | `dietary[tiab]` | 260,594 | none |
| 77 | `eating[tiab]` | 77,768 | none |
| 78 | `nutrition*[tiab]` | 299,564 | none |
| 79 | `"screen time"[tiab]` | 2,454 | none |
| 80 | `alcohol*[tiab]` | 346,001 | none |
| 81 | `smok*[tiab]` | 287,925 | none |
| 82 | `tobacco[tiab]` | 104,255 | none |
| 83 | `"weight gain"[tiab]` | 63,432 | none |
| 84 | `habit*[tiab]` | 183,163 | none |
| 85 | `"daily routine*"[tiab]` | 4,302 | none |
| 86 | `"daily life"[tiab]` | 20,183 | none |
| 87 | `"daily living"[tiab]` | 34,578 | none |
| 88 | `"activity levels"[tiab]` | 19,033 | none |
| 89 | `"internet use"[tiab]` | 2,812 | none |
| 90 | `gaming[tiab]` | 3,672 | none |
| 91 | `"Mental Health"[Mesh]` | 44,674 | none |
| 92 | `"Mental Disorders"[Mesh]` | 1,316,811 | none |
| 93 | `"Psychological Well-Being"[Mesh]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 94 | `"Quality of Life"[Mesh]` | 215,485 | none |
| 95 | `"Stress, Psychological"[Mesh]` | 139,617 | none |
| 96 | `"Anxiety"[Mesh]` | 93,322 | none |
| 97 | `"Depression"[Mesh]` | 129,618 | none |
| 98 | `"Loneliness"[Mesh]` | 4,443 | none |
| 99 | `"Social Isolation"[Mesh]` | 22,365 | none |
| 100 | `"Affect"[Mesh]` | 34,956 | none |
| 101 | `"Adaptation, Psychological"[Mesh]` | 132,259 | none |
| 102 | `"Psychological Distress"[Mesh]` | 4,500 | none |
| 103 | `wellbeing[tiab]` | 91,509 | none |
| 104 | `"well-being"[tiab]` | 80,677 | none |
| 105 | `"well being"[tiab]` | 80,677 | none |
| 106 | `"mental health"[tiab]` | 159,660 | none |
| 107 | `psycholog*[tiab]` | 295,977 | none |
| 108 | `anxiety[tiab]` | 199,914 | none |
| 109 | `anxious[tiab]` | 17,082 | none |
| 110 | `depress*[tiab]` | 474,404 | none |
| 111 | `lonel*[tiab]` | 7,863 | none |
| 112 | `"life satisfaction"[tiab]` | 8,061 | none |
| 113 | `"quality of life"[tiab]` | 282,519 | none |
| 114 | `mood[tiab]` | 76,261 | none |
| 115 | `emotion*[tiab]` | 205,757 | none |
| 116 | `burnout[tiab]` | 13,018 | none |
| 117 | `"mental disorder*"[tiab]` | 48,627 | none |
| 118 | `psychiatr*[tiab]` | 251,946 | none |
| 119 | `"post-traumatic"[tiab]` | 31,780 | none |
| 120 | `"posttraumatic"[tiab]` | 65,176 | none |
| 121 | `happiness[tiab]` | 7,214 | none |
| 122 | `resilience[tiab]` | 27,035 | none |
| 123 | `fear[tiab]` | 66,845 | none |
| 124 | `worry[tiab]` | 9,914 | none |
| 125 | `wellness[tiab]` | 10,646 | none |
| 126 | `"psychological distress"[tiab]` | 20,155 | none |
| 127 | `"emotional distress"[tiab]` | 6,857 | none |
| 128 | `"mental distress"[tiab]` | 1,930 | none |
| 129 | `"substance use"[tiab]` | 37,853 | none |
| 130 | `"substance abuse"[tiab]` | 25,726 | none |
| 131 | `"drug use"[tiab]` | 46,742 | none |
| 132 | `vaping[tiab]` | 1,632 | none |
| 133 | `"e-cigarette*"[tiab]` | 4,975 | none |
| 134 | `cannabis[tiab]` | 18,505 | none |
| 135 | `"Substance-Related Disorders"[Mesh]` | 291,305 | none |
| 136 | `"food intake"[tiab]` | 45,992 | none |
| 137 | `"food consumption"[tiab]` | 14,333 | none |
| 138 | `"food insecurity"[tiab]` | 4,307 | none |
| 139 | `"food habit*"[tiab]` | 2,306 | none |
| 140 | `"psychological stress"[tiab]` | 8,192 | none |
| 141 | `"perceived stress"[tiab]` | 7,723 | none |
| 142 | `"mental stress"[tiab]` | 3,336 | none |
| 143 | `"emotional stress"[tiab]` | 4,610 | none |
| 144 | `"stress level*"[tiab]` | 8,953 | none |
| 145 | `"traumatic stress"[tiab]` | 15,988 | none |
| 146 | `#51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96 OR #97 OR #98 OR #99 OR #100 OR #101 OR #102 OR #103 OR #104 OR #105 OR #106 OR #107 OR #108 OR #109 OR #110 OR #111 OR #112 OR #113 OR #114 OR #115 OR #116 OR #117 OR #118 OR #119 OR #120 OR #121 OR #122 OR #123 OR #124 OR #125 OR #126 OR #127 OR #128 OR #129 OR #130 OR #131 OR #132 OR #133 OR #134 OR #135 OR #136 OR #137 OR #138 OR #139 OR #140 OR #141 OR #142 OR #143 OR #144 OR #145` | 5,803,288 | none |
| 147 | `#50 AND #146` | 20,951 | none |

### Strategy (single line, for copying into PubMed)

```text
(("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR "Pandemics"[Mesh] OR "Quarantine"[Mesh] OR COVID*[tiab] OR "corona virus disease"[tiab] OR "coronavirus disease"[tiab] OR "corona virus"[tiab] OR SARS-CoV-2[tiab] OR SARS-CoV2[tiab] OR SARSCoV2[tiab] OR "severe acute respiratory syndrome coronavirus 2"[tiab] OR nCoV[tiab] OR 2019-nCoV[tiab] OR "novel coronavirus"[tiab] OR "new coronavirus"[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR "lock down"[tiab] OR "locked down"[tiab] OR quarantin*[tiab] OR "home confinement"[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "shelter in place"[tiab] OR "shelter-in-place"[tiab] OR "social distanc*"[tiab] OR "physical distanc*"[tiab] OR "school closure*"[tiab] OR "school closing*"[tiab] OR "self-isolat*"[tiab] OR "self isolat*"[tiab] OR "movement restriction*"[tiab] OR "containment measure*"[tiab] OR "coronavirus 2019"[tiab] OR "coronavirus disease 2019"[tiab] OR "2019 novel coronavirus"[tiab] OR "covid-19 outbreak"[tiab] OR "coronavirus outbreak"[tiab] OR "coronavirus epidemic"[tiab] OR "coronavirus pandemic"[tiab] OR "home isolation"[tiab] OR curfew*[tiab] OR "non-pharmaceutical intervention*"[tiab] OR "nonpharmaceutical intervention*"[tiab] OR "social restriction*"[tiab] OR "Physical Distancing"[Mesh] OR "confinement measure*"[tiab] OR "covid-19 confinement"[tiab]) AND ("Life Style"[Mesh] OR "Health Behavior"[Mesh] OR "Exercise"[Mesh] OR "Sedentary Behavior"[Mesh] OR "Sleep"[Mesh] OR "Sleep Wake Disorders"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Motor Activity"[Mesh] OR "Screen Time"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Smoking"[Mesh] OR "Body Weight"[Mesh] OR lifestyle*[tiab] OR "life style*"[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR "physical activit*"[tiab] OR exercis*[tiab] OR sedentar*[tiab] OR sitting[tiab] OR sleep*[tiab] OR insomnia[tiab] OR diet[tiab] OR diets[tiab] OR dietary[tiab] OR eating[tiab] OR nutrition*[tiab] OR "screen time"[tiab] OR alcohol*[tiab] OR smok*[tiab] OR tobacco[tiab] OR "weight gain"[tiab] OR habit*[tiab] OR "daily routine*"[tiab] OR "daily life"[tiab] OR "daily living"[tiab] OR "activity levels"[tiab] OR "internet use"[tiab] OR gaming[tiab] OR "Mental Health"[Mesh] OR "Mental Disorders"[Mesh] OR "Psychological Well-Being"[Mesh] OR "Quality of Life"[Mesh] OR "Stress, Psychological"[Mesh] OR "Anxiety"[Mesh] OR "Depression"[Mesh] OR "Loneliness"[Mesh] OR "Social Isolation"[Mesh] OR "Affect"[Mesh] OR "Adaptation, Psychological"[Mesh] OR "Psychological Distress"[Mesh] OR wellbeing[tiab] OR "well-being"[tiab] OR "well being"[tiab] OR "mental health"[tiab] OR psycholog*[tiab] OR anxiety[tiab] OR anxious[tiab] OR depress*[tiab] OR lonel*[tiab] OR "life satisfaction"[tiab] OR "quality of life"[tiab] OR mood[tiab] OR emotion*[tiab] OR burnout[tiab] OR "mental disorder*"[tiab] OR psychiatr*[tiab] OR "post-traumatic"[tiab] OR "posttraumatic"[tiab] OR happiness[tiab] OR resilience[tiab] OR fear[tiab] OR worry[tiab] OR wellness[tiab] OR "psychological distress"[tiab] OR "emotional distress"[tiab] OR "mental distress"[tiab] OR "substance use"[tiab] OR "substance abuse"[tiab] OR "drug use"[tiab] OR vaping[tiab] OR "e-cigarette*"[tiab] OR cannabis[tiab] OR "Substance-Related Disorders"[Mesh] OR "food intake"[tiab] OR "food consumption"[tiab] OR "food insecurity"[tiab] OR "food habit*"[tiab] OR "psychological stress"[tiab] OR "perceived stress"[tiab] OR "mental stress"[tiab] OR "emotional stress"[tiab] OR "stress level*"[tiab] OR "traumatic stress"[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 15 | 15 | 100.0% | 15 / 15 |

15 of the 15 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 81.9% (95% bound; it is as wide as the number of such records makes it). 11 of the 15 known records found through reference lists come from one review (33207689, 73.3%). A benchmark built on one review takes that review's scope: add the reference list of a second review that covers a different searched concept.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 0 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 49 | 49 | 4 |
| C6 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 11 |
| C7 | 2026-11-27 | PubMed | backward | 1 | 14 | 14 | 0 |
| C8 | 2026-11-27 | PubMed | backward | 1 | 49 | 49 | 4 |
| C9 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 11 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| covid | 5,803,288 | 0 |
| outcomes | 116,429 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 572,727 | initial | none | initial draft |
| 2 | 124,048 | covid: +9 / -7 | none | tightened covid block: dropped generic epidemic/outbreak/isolation/confinement and non-COVID coronavirus MeSH |
| 3 | 115,982 | covid: +0 / -1 | none | merged outcome blocks into one optional block; removed social isolation proximity from covid |
| 4 | 24,895 | outcomes: +78 / -0 | none | AND outcome block for workload; 0/15 benchmark lost |
| 5 | 31,409 | covid: +7 / -0; outcomes: +12 / -2 | none | critic round 1: add confinement/measure terms, substance use terms, Physical Distancing MeSH; distress* -> distress phrases; quote activity levels |
| 6 | 23,788 | covid: +3 / -1; outcomes: +0 / -1 | none | drop bare confinement and bare distress for noise; add specific confinement phrases |
| 7 | 23,788 | covid: +0 / -1 | none | remove phrase not in index: confined at home |
| 8 | 20,951 | covid: +0 / -1; outcomes: +10 / -2 | none | noise-check samples: dropped public health measure*, food, stress* (off-topic); added specific food/stress phrases |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 8 findings; F1 must-fix open, F2 should-fix open, F3 should-fix open, F4 should-fix open, F5 should-fix open, F6 document open, F7 document open, F8 document open
- Round 2 on version 8: 12 findings; F1 must-fix resolved, F2 should-fix accepted-risk, F3 should-fix resolved, F4 should-fix resolved, F5 should-fix resolved, F6 document accepted-risk, F7 document accepted-risk, F8 document resolved, F9 should-fix resolved, F10 should-fix accepted-risk, F11 document resolved, F12 document resolved
- Round 3 on version 8: 13 findings; F1 must-fix resolved, F2 should-fix accepted-risk, F3 should-fix resolved, F4 should-fix resolved, F5 should-fix resolved, F6 document accepted-risk, F7 document accepted-risk, F8 document resolved, F9 should-fix resolved, F10 should-fix accepted-risk, F11 document resolved, F12 document resolved, F13 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 3043 NCBI requests logged (1575 from cache); strategy sha256 e623ff89a873._

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
        "query": "(\"Psychological Well-Being\"[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"Psychological Well-Being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:93",
        "blocking": false,
        "requires_review": true,
        "id": "I-36de042c5db2685346a3"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"Psychological Well-Being\"[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"Psychological Well-Being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:93",
        "blocking": false,
        "requires_review": true,
        "id": "I-d26c12e93341c50b7bfb"
      }
    ],
    "issues": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"Psychological Well-Being\"[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"Psychological Well-Being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:93",
        "blocking": false,
        "requires_review": true,
        "id": "I-36de042c5db2685346a3"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"Psychological Well-Being\"[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/11/22\"[edat])",
        "translation": "\"Psychological Well-Being\"[MeSH Terms] AND 1800/01/01:2020/11/22[Date - Entry]",
        "location": "line:93",
        "blocking": false,
        "requires_review": true,
        "id": "I-d26c12e93341c50b7bfb"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
        "text": "\"Quarantine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Physical Distancing",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:47",
      "term": {
        "text": "\"Physical Distancing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Life Style",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:50",
      "term": {
        "text": "\"Life Style\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:51",
      "term": {
        "text": "\"Health Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Exercise",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:52",
      "term": {
        "text": "\"Exercise\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sedentary Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:53",
      "term": {
        "text": "\"Sedentary Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:54",
      "term": {
        "text": "\"Sleep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sleep Wake Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:55",
      "term": {
        "text": "\"Sleep Wake Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:56",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:57",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Motor Activity",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:58",
      "term": {
        "text": "\"Motor Activity\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Screen Time",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:59",
      "term": {
        "text": "\"Screen Time\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alcohol Drinking",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:60",
      "term": {
        "text": "\"Alcohol Drinking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Smoking",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:61",
      "term": {
        "text": "\"Smoking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Body Weight",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001835",
          "name": "Body Weight",
          "type": "descriptor",
          "scope_note": "The mass or quantity of heaviness of an individual. It is expressed by units of pounds or kilograms.",
          "tree_numbers": [
            "C23.888.144",
            "E01.370.600.115.100.160.120",
            "E01.370.600.115.450.375",
            "E05.041.124.160.750",
            "G07.100.100.160.120",
            "G07.100.175.313",
            "G07.345.249.314.120"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001835",
      "preferred_label": "Body Weight",
      "type": "descriptor",
      "location": "vocabulary:62",
      "term": {
        "text": "\"Body Weight\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:90",
      "term": {
        "text": "\"Mental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mental Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001523",
          "name": "Mental Disorders",
          "type": "descriptor",
          "scope_note": "Psychiatric illness or diseases manifested by breakdowns in the adaptational process expressed primarily as abnormalities of thought, feeling, and behavior producing either distress or impairment of function.",
          "tree_numbers": [
            "F03"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001523",
      "preferred_label": "Mental Disorders",
      "type": "descriptor",
      "location": "vocabulary:91",
      "term": {
        "text": "\"Mental Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Well-Being",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:92",
      "term": {
        "text": "\"Psychological Well-Being\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quality of Life",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:93",
      "term": {
        "text": "\"Quality of Life\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:94",
      "term": {
        "text": "\"Stress, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:95",
      "term": {
        "text": "\"Anxiety\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:96",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Loneliness",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:97",
      "term": {
        "text": "\"Loneliness\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Social Isolation",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:98",
      "term": {
        "text": "\"Social Isolation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Affect",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000339",
          "name": "Affect",
          "type": "descriptor",
          "scope_note": "The feeling-tone accompaniment of an idea or mental representation. It is the most direct psychic derivative of instinct and the psychic representative of the various bodily changes by means of which instincts manifest themselves.",
          "tree_numbers": [
            "F01.470.047"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000339",
      "preferred_label": "Affect",
      "type": "descriptor",
      "location": "vocabulary:99",
      "term": {
        "text": "\"Affect\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adaptation, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000223",
          "name": "Adaptation, Psychological",
          "type": "descriptor",
          "scope_note": "A state of harmony between internal needs and external demands and the processes used in achieving this condition. (From APA Thesaurus of Psychological Index Terms, 8th ed).",
          "tree_numbers": [
            "F01.058"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000223",
      "preferred_label": "Adaptation, Psychological",
      "type": "descriptor",
      "location": "vocabulary:100",
      "term": {
        "text": "\"Adaptation, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Distress",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:101",
      "term": {
        "text": "\"Psychological Distress\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Substance-Related Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T11:33:45+00:00",
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
      "location": "vocabulary:134",
      "term": {
        "text": "\"Substance-Related Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"Pandemics\"[MeSH Terms] OR \"Quarantine\"[MeSH Terms] OR \"covid*\"[Title/Abstract] OR \"corona virus disease\"[Title/Abstract] OR \"coronavirus disease\"[Title/Abstract] OR \"corona virus\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV2\"[Title/Abstract] OR \"SARSCoV2\"[Title/Abstract] OR \"severe acute respiratory syndrome coronavirus 2\"[Title/Abstract] OR \"nCoV\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"new coronavirus\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down\"[Title/Abstract] OR \"locked down\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"social distanc*\"[Title/Abstract] OR \"physical distanc*\"[Title/Abstract] OR \"school closure*\"[Title/Abstract] OR \"school closing*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"containment measure*\"[Title/Abstract] OR \"coronavirus 2019\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"covid-19 outbreak\"[Title/Abstract] OR \"coronavirus outbreak\"[Title/Abstract] OR \"coronavirus epidemic\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract] OR \"home isolation\"[Title/Abstract] OR \"curfew*\"[Title/Abstract] OR \"non pharmaceutical intervention*\"[Title/Abstract] OR \"nonpharmaceutical intervention*\"[Title/Abstract] OR \"social restriction*\"[Title/Abstract] OR \"Physical Distancing\"[MeSH Terms] OR \"confinement measure*\"[Title/Abstract] OR \"covid-19 confinement\"[Title/Abstract]) AND (\"Life Style\"[MeSH Terms] OR \"Health Behavior\"[MeSH Terms] OR \"Exercise\"[MeSH Terms] OR \"Sedentary Behavior\"[MeSH Terms] OR \"Sleep\"[MeSH Terms] OR \"Sleep Wake Disorders\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Motor Activity\"[MeSH Terms] OR \"Screen Time\"[MeSH Terms] OR \"Alcohol Drinking\"[MeSH Terms] OR \"Smoking\"[MeSH Terms] OR \"Body Weight\"[MeSH Terms] OR \"lifestyle*\"[Title/Abstract] OR \"life style*\"[Title/Abstract] OR \"behavior*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract] OR \"physical activit*\"[Title/Abstract] OR \"exercis*\"[Title/Abstract] OR \"sedentar*\"[Title/Abstract] OR \"sitting\"[Title/Abstract] OR \"sleep*\"[Title/Abstract] OR \"insomnia\"[Title/Abstract] OR \"Diet\"[Title/Abstract] OR \"diets\"[Title/Abstract] OR \"dietary\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"Screen Time\"[Title/Abstract] OR \"alcohol*\"[Title/Abstract] OR \"smok*\"[Title/Abstract] OR \"tobacco\"[Title/Abstract] OR \"weight gain\"[Title/Abstract] OR \"habit*\"[Title/Abstract] OR \"daily routine*\"[Title/Abstract] OR \"daily life\"[Title/Abstract] OR \"daily living\"[Title/Abstract] OR \"activity levels\"[Title/Abstract] OR \"internet use\"[Title/Abstract] OR \"gaming\"[Title/Abstract] OR \"Mental Health\"[MeSH Terms] OR \"Mental Disorders\"[MeSH Terms] OR \"Psychological Well-Being\"[MeSH Terms] OR \"Quality of Life\"[MeSH Terms] OR \"stress, psychological\"[MeSH Terms] OR \"Anxiety\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"Loneliness\"[MeSH Terms] OR \"Social Isolation\"[MeSH Terms] OR \"Affect\"[MeSH Terms] OR \"adaptation, psychological\"[MeSH Terms] OR \"Psychological Distress\"[MeSH Terms] OR \"wellbeing\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"well-being\"[Title/Abstract] OR \"Mental Health\"[Title/Abstract] OR \"psycholog*\"[Title/Abstract] OR \"Anxiety\"[Title/Abstract] OR \"anxious\"[Title/Abstract] OR \"depress*\"[Title/Abstract] OR \"lonel*\"[Title/Abstract] OR \"life satisfaction\"[Title/Abstract] OR \"Quality of Life\"[Title/Abstract] OR \"mood\"[Title/Abstract] OR \"emotion*\"[Title/Abstract] OR \"burnout\"[Title/Abstract] OR \"mental disorder*\"[Title/Abstract] OR \"psychiatr*\"[Title/Abstract] OR \"post-traumatic\"[Title/Abstract] OR \"posttraumatic\"[Title/Abstract] OR \"happiness\"[Title/Abstract] OR \"resilience\"[Title/Abstract] OR \"fear\"[Title/Abstract] OR \"worry\"[Title/Abstract] OR \"wellness\"[Title/Abstract] OR \"Psychological Distress\"[Title/Abstract] OR \"emotional distress\"[Title/Abstract] OR \"mental distress\"[Title/Abstract] OR \"substance use\"[Title/Abstract] OR \"substance abuse\"[Title/Abstract] OR \"drug use\"[Title/Abstract] OR \"vaping\"[Title/Abstract] OR \"e cigarette*\"[Title/Abstract] OR \"cannabis\"[Title/Abstract] OR \"Substance-Related Disorders\"[MeSH Terms] OR \"food intake\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"food insecurity\"[Title/Abstract] OR \"food habit*\"[Title/Abstract] OR \"psychological stress\"[Title/Abstract] OR \"perceived stress\"[Title/Abstract] OR \"mental stress\"[Title/Abstract] OR \"emotional stress\"[Title/Abstract] OR \"stress level*\"[Title/Abstract] OR \"traumatic stress\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "cb21fdd8ea1e8438b615c46a5a888b8cfcccd30e836e92560fe0469fc9557411",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Outcomes block AND-ed for workload; substance use not named. See F2, F3."
        },
        "operators": {
          "verdict": "revise",
          "note": "Syntax correct; outcome terms broad. See F2, F5."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "No substance-use heading; related exposure headings undocumented. See F3, F7."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Gaps in confinement/measure wording; distress*/stress* noise. See F3, F4, F5."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors; unquoted activity levels (F8)."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Entry-date bound at 2020/11/22 (F1)."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "All lines carry an [edat] range ending 2020/11/22 while protocol.as_of is null and limits is empty.",
          "recommendation": "Remove the date limit or record it explicitly as the search cutoff.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Outcomes block AND-ed for workload; loss unmeasured; benchmark mostly from one review.",
          "recommendation": "Document trade-off and reversal; add second benchmark.",
          "status": "open"
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Eligibility names substance use but no bare-name text word or heading in the outcomes block.",
          "recommendation": "Add substance use, substance abuse, drug use, vaping, cannabis and Substance-Related Disorders.",
          "status": "open"
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Confinement only as home confinement; no curfew, public health measure, non-pharmaceutical intervention, social restriction.",
          "recommendation": "Test and add.",
          "status": "open"
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "distress*, behavior*, food, stress*, Body Weight, fear are broad with high unique yield and no known-only record.",
          "recommendation": "Sample noise; replace distress* with psychological/emotional distress if off-topic.",
          "status": "open"
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "PubMed only; no PsycINFO/Embase; OpenAlex unavailable; no independent seeds.",
          "recommendation": "State limitation.",
          "status": "open"
        },
        {
          "id": "F7",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "finding": "No Physical Distancing, Communicable Disease Control or Coronavirus Infections heading assessed.",
          "recommendation": "Document or test.",
          "status": "open"
        },
        {
          "id": "F8",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "activity levels[tiab] unquoted; duplicate hyphen variants.",
          "recommendation": "Quote it.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-14cfc6af9ba22f0341e3",
          "status": "accepted-risk",
          "response": "Valid verified descriptor (D000092862) with zero hits at the cutoff because it is new; text words wellbeing, well-being and wellness cover the concept.",
          "evidence": "line 87 returns 0 with 'No items found'; term_impact records_only_here 0, known_only_here []; no known record depends on it."
        },
        {
          "issue_id": "I-947dcd1513e4d925977b",
          "status": "accepted-risk",
          "response": "Zero hits inspected: spelling is the verified preferred label, tagged [Mesh], inside an OR group; zero is due to indexing date, not an error.",
          "evidence": "Translation clean, translationset empty; combined query still returns 24,895 with 15 of 15 known records."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 8,
      "review_sha256": "9f8f069fa69aa3e3ed7e623db8203ac27100a322997cea1397b697940a153f57",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Outcomes block AND-ed for workload (F2); stale counts (F9); bare distress (F10)."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within blocks, AND between; structure correct."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Physical Distancing and Substance-Related Disorders added; Psychological Well-Being returns 0 at cutoff, dispositioned."
        },
        "text_words": {
          "verdict": "revise",
          "note": "F4/F5 resolved; F10, F11, F12 raised."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Date cutoff now recorded as as_of and limit (F1 resolved)."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "Undeclared [edat] bound ending 2020/11/22.",
          "recommendation": "Record the bound as the search cutoff.",
          "status": "resolved",
          "response": "protocol.limits lists an entry-date limit through 2020-11-22 with reason; as_of set; notes say snapshot."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Outcomes block AND-ed for workload; loss unmeasured; 73.3% of known records from one review.",
          "recommendation": "Keep as documented reversible decision; add second benchmark.",
          "status": "accepted-risk",
          "response": "Deliberate workload decision (116,429 without block versus 20,951 with it), documented in the concept rationale with its reversal instruction. A second benchmark from a non-outcome review was not found within this run (OpenAlex unavailable; PubMed lists of other reviews are outcome-focused). Loss is reported as unmeasured with an 18.1% upper bound."
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Substance use not searched.",
          "recommendation": "Add terms.",
          "status": "resolved",
          "response": "Substance use, substance abuse, drug use, vaping, e-cigarette*, cannabis and Substance-Related Disorders[Mesh] added."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Confinement wording narrow.",
          "recommendation": "Add measure terms.",
          "status": "resolved",
          "response": "curfew*, non-pharmaceutical intervention*, social restriction*, confinement measure*, covid-19 confinement added."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Broad outcome terms.",
          "recommendation": "Replace with phrases.",
          "status": "resolved",
          "response": "Noise-check samples showed food and stress* retrieved mostly COVID clinical papers; replaced by specific phrases; no known record lost."
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "PubMed only; no independent seeds.",
          "recommendation": "State limitations.",
          "status": "accepted-risk",
          "response": "Stated in protocol notes and narrative; recommend PsycINFO/Embase translation at peer review."
        },
        {
          "id": "F7",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "finding": "Related headings not assessed.",
          "recommendation": "Document or test.",
          "status": "accepted-risk",
          "response": "Physical Distancing added; Communicable Disease Control too broad; Coronavirus Infections covered by specific headings."
        },
        {
          "id": "F8",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "activity levels unquoted.",
          "recommendation": "Quote it.",
          "status": "resolved",
          "response": "Now quoted."
        },
        {
          "id": "F9",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Rationale quotes stale counts.",
          "recommendation": "Update to v8 counts.",
          "status": "resolved",
          "response": "Rationale updated to 116,429 and 20,951."
        },
        {
          "id": "F10",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "No bare distress term.",
          "recommendation": "Add distress[tiab] or tested alternative.",
          "status": "accepted-risk",
          "response": "Bare distress[tiab] (distress* earlier had 2,452 records only it retrieved, no known-only record) mostly matches respiratory distress/ARDS in COVID clinical papers, which eligibility excludes. Covered by psychological/emotional/mental distress phrases, Psychological Distress[Mesh], stress/anxiety/depression terms. Flagged for the PRESS reviewer."
        },
        {
          "id": "F11",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "public health measure* removed without reason.",
          "recommendation": "Record reason.",
          "status": "resolved",
          "response": "Noise-check sample of its unique records was off-topic pre-pandemic public health papers; recorded in notes."
        },
        {
          "id": "F12",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "SARSCoV2[tiab] count unexpectedly high.",
          "recommendation": "Check translation.",
          "status": "resolved",
          "response": "PubMed normalises it with the SARS-CoV-2 form; harmless variant; no change."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-36de042c5db2685346a3",
          "status": "accepted-risk",
          "response": "Psychological Well-Being[Mesh] is a valid descriptor returning 0 under the 2020-11-22 bound; inside an OR group; text words cover the concept.",
          "evidence": "Line 93 returns 0 with 'No items found'; translation clean, empty translationset; combined query 20,951 with 15 of 15 known records retrieved."
        },
        {
          "issue_id": "I-d26c12e93341c50b7bfb",
          "status": "accepted-risk",
          "response": "Zero hits inspected: spelling is the preferred label, tagged [Mesh], in an OR group; zero comes from the cutoff date not an error.",
          "evidence": "Line 93 returns 0 at the cutoff; translation clean; 20,951 result unaffected."
        }
      ]
    },
    {
      "round": 3,
      "strategy_version": 8,
      "review_sha256": "75717a7fbf040bbb0ff716f9cc5ce57d2d41e7a04b98c35a7a2bcf644b56be24",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Documented reversible workload AND; loss unmeasured (F2 accepted)."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within blocks, AND between; structure correct."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Physical Distancing and Substance-Related Disorders added; Psychological Well-Being returns 0 at cutoff, dispositioned."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Earlier findings resolved or accepted; F13 document only."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Date cutoff now recorded as as_of and limit (F1 resolved)."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "Undeclared [edat] bound ending 2020/11/22.",
          "recommendation": "Record the bound as the search cutoff.",
          "status": "resolved",
          "response": "protocol.limits lists an entry-date limit through 2020-11-22 with reason; as_of set; notes say snapshot."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Outcomes block AND-ed for workload; loss unmeasured; 73.3% of known records from one review.",
          "recommendation": "Keep as documented reversible decision; add second benchmark.",
          "status": "accepted-risk",
          "response": "Deliberate workload decision (116,429 without block versus 20,951 with it), documented in the concept rationale with its reversal instruction. A second benchmark from a non-outcome review was not found within this run (OpenAlex unavailable; PubMed lists of other reviews are outcome-focused). Loss is reported as unmeasured with an 18.1% upper bound."
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Substance use not searched.",
          "recommendation": "Add terms.",
          "status": "resolved",
          "response": "Substance use, substance abuse, drug use, vaping, e-cigarette*, cannabis and Substance-Related Disorders[Mesh] added."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Confinement wording narrow.",
          "recommendation": "Add measure terms.",
          "status": "resolved",
          "response": "curfew*, non-pharmaceutical intervention*, social restriction*, confinement measure*, covid-19 confinement added."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Broad outcome terms.",
          "recommendation": "Replace with phrases.",
          "status": "resolved",
          "response": "Noise-check samples showed food and stress* retrieved mostly COVID clinical papers; replaced by specific phrases; no known record lost."
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "PubMed only; no independent seeds.",
          "recommendation": "State limitations.",
          "status": "accepted-risk",
          "response": "Stated in protocol notes and narrative; recommend PsycINFO/Embase translation at peer review."
        },
        {
          "id": "F7",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "finding": "Related headings not assessed.",
          "recommendation": "Document or test.",
          "status": "accepted-risk",
          "response": "Physical Distancing added; Communicable Disease Control too broad; Coronavirus Infections covered by specific headings."
        },
        {
          "id": "F8",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "activity levels unquoted.",
          "recommendation": "Quote it.",
          "status": "resolved",
          "response": "Now quoted."
        },
        {
          "id": "F9",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Rationale quotes stale counts.",
          "recommendation": "Update to v8 counts.",
          "status": "resolved",
          "response": "Rationale updated to 116,429 and 20,951."
        },
        {
          "id": "F10",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "No bare distress term.",
          "recommendation": "Add distress[tiab] or tested alternative.",
          "status": "accepted-risk",
          "response": "Bare distress[tiab] (distress* earlier had 2,452 records only it retrieved, no known-only record) mostly matches respiratory distress/ARDS in COVID clinical papers, which eligibility excludes. Covered by psychological/emotional/mental distress phrases, Psychological Distress[Mesh], stress/anxiety/depression terms. Flagged for the PRESS reviewer."
        },
        {
          "id": "F11",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "public health measure* removed without reason.",
          "recommendation": "Record reason.",
          "status": "resolved",
          "response": "Noise-check sample of its unique records was off-topic pre-pandemic public health papers; recorded in notes."
        },
        {
          "id": "F12",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "SARSCoV2[tiab] count unexpectedly high.",
          "recommendation": "Check translation.",
          "status": "resolved",
          "response": "PubMed normalises it with the SARS-CoV-2 form; harmless variant; no change."
        },
        {
          "id": "F13",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "Result 20,951 exceeds the 10,000 threshold; term impact not re-measured on v8 after the final noise edits.",
          "recommendation": "Note that broad outcome terms (behavior*, habit*, emotion*, psycholog*, fear) drive volume; re-run term impact if screening load is a concern.",
          "status": "accepted-risk",
          "response": "Term impact was measured on v7 (the same strategy apart from three noise edits that were sampled); broad outcome terms flagged for the PRESS reviewer in narrative.md."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-36de042c5db2685346a3",
          "status": "accepted-risk",
          "response": "Psychological Well-Being[Mesh] is a valid descriptor returning 0 under the 2020-11-22 bound; inside an OR group; text words cover the concept.",
          "evidence": "Line 93 returns 0 with 'No items found'; translation clean, empty translationset; combined query 20,951 with 15 of 15 known records retrieved."
        },
        {
          "issue_id": "I-d26c12e93341c50b7bfb",
          "status": "accepted-risk",
          "response": "Zero hits inspected: spelling is the preferred label, tagged [Mesh], in an OR group; zero comes from the cutoff date not an error.",
          "evidence": "Line 93 returns 0 at the cutoff; translation clean; 20,951 result unaffected."
        }
      ],
      "closing": true
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-27T09:36:34+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User asked not to be questioned during this run. Working scope assumptions: PICO; search intervention and population blocks; screen school delivery and food-consumption outcome; no comparator or study-design block; no language or age restriction. The as_of date is 2017-12-14 per harness instruction. No user-supplied known relevant records. Discovery: candidate systematic reviews PMID 27122145 and 27720105 matched school dietary-intake/adolescent topics; their included-study lists were not accessible through the configured psb neighbors interface, so no review-derived benchmark was assembled. Two focused PubMed pilot samples were screened by title/abstract (PubMed records retrieved before the publication cutoff); clearly eligible primary records were added as a relevant development set. Records with publication dates after 2017-12-14 were excluded from known sets. After initial pilot, school delivery was promoted from screen to search because it is a defining context in the question and an explicit inclusion criterion; a broad MeSH/text block was tested against all nine screened records.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food and nutrition education intervention | search | Core intervention topic, described through education, nutrition education, dietary education, and related school programs. |
| Adolescents or school students | search | The target age/student group is central and searchable, while no age filter will be used because age indexing and reporting vary. |
| Delivered through a school | search | School delivery is explicit in the topic and eligibility criteria; a broad school block is searchable through MeSH and title/abstract wording, while consumption outcomes remain screened. |
| Eligible food-consumption outcome | screen | Food consumption outcomes are inconsistently worded and will be assessed during screening rather than required as an AND block. |
| Comparator | screen | No comparator was specified; handle at screening. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2017-12-14
- Total records: 25,088 (25,151 before limits)
- Limits and filters: `1800:2017/12/14[dp]` (Historical publication cutoff required by the user harness; protocol as_of additionally bounds PubMed entry date.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Health Education"[Mesh]` | 221,709 |
| 2 | `"Health Promotion"[Mesh]` | 70,478 |
| 3 | `"nutrition education"[tiab]` | 3,866 |
| 4 | `"diet education"[tiab]` | 115 |
| 5 | `"dietary education"[tiab]` | 252 |
| 6 | `"food education"[tiab]` | 84 |
| 7 | `"food and nutrition education"[tiab]` | 105 |
| 8 | `"nutrition instruction"[tiab]` | 46 |
| 9 | `"nutrition training"[tiab]` | 175 |
| 10 | `"nutrition promotion"[tiab]` | 129 |
| 11 | `"nutrition intervention"[tiab]` | 1,150 |
| 12 | `"nutrition interventions"[tiab]` | 873 |
| 13 | `"dietary intervention"[tiab]` | 4,247 |
| 14 | `"dietary interventions"[tiab]` | 2,009 |
| 15 | `"nutrition program"[tiab]` | 1,227 |
| 16 | `"nutrition programs"[tiab]` | 970 |
| 17 | `"nutrition programme"[tiab]` | 119 |
| 18 | `"nutrition programmes"[tiab]` | 162 |
| 19 | `"healthy eating education"[tiab]` | 7 |
| 20 | `"food literacy"[tiab]` | 34 |
| 21 | `"nutrition literacy"[tiab]` | 48 |
| 22 | `"eating education"[tiab]` | 12 |
| 23 | `"dietary behavior intervention"[tiab]` | 4 |
| 24 | `"health promotion"[tiab]` | 26,990 |
| 25 | `"dietary habits"[tiab]` | 7,468 |
| 26 | `nutrition[tiab]` | 147,533 |
| 27 | `cooking[tiab]` | 12,112 |
| 28 | `"Cooking"[Mesh]` | 10,657 |
| 29 | `gardening[tiab]` | 1,088 |
| 30 | `"Gardening"[Mesh]` | 811 |
| 31 | `"nutrition curriculum"[tiab]` | 87 |
| 32 | `"nutrition curricula"[tiab]` | 11 |
| 33 | `"nutrition counseling"[tiab]` | 559 |
| 34 | `"nutrition counselling"[tiab]` | 148 |
| 35 | `"dietary counseling"[tiab]` | 836 |
| 36 | `"dietary counselling"[tiab]` | 386 |
| 37 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36` | 401,357 |
| 38 | `"Adolescent"[Mesh]` | 1,895,608 |
| 39 | `"Child"[Mesh]` | 1,797,170 |
| 40 | `"Students"[Mesh]` | 112,971 |
| 41 | `adolescen*[tiab]` | 248,945 |
| 42 | `teen*[tiab]` | 26,895 |
| 43 | `youth*[tiab]` | 64,596 |
| 44 | `child*[tiab]` | 1,257,861 |
| 45 | `student*[tiab]` | 234,078 |
| 46 | `schoolchild*[tiab]` | 13,052 |
| 47 | `pupil*[tiab]` | 26,074 |
| 48 | `"high school"[tiab]` | 24,231 |
| 49 | `"middle school"[tiab]` | 3,885 |
| 50 | `"secondary school"[tiab]` | 5,609 |
| 51 | `"primary school"[tiab]` | 7,222 |
| 52 | `"school student"[tiab]` | 519 |
| 53 | `"school students"[tiab]` | 14,131 |
| 54 | `"school children"[tiab]` | 20,662 |
| 55 | `"schoolchild"[tiab]` | 157 |
| 56 | `"schoolchildren"[tiab]` | 12,947 |
| 57 | `"school aged"[tiab]` | 7,648 |
| 58 | `"school-aged"[tiab]` | 7,648 |
| 59 | `#38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58` | 3,400,169 |
| 60 | `"School Health Services"[Mesh]` | 21,872 |
| 61 | `"Schools"[Mesh]` | 107,820 |
| 62 | `school*[tiab]` | 246,627 |
| 63 | `classroom*[tiab]` | 14,159 |
| 64 | `"school-based"[tiab]` | 10,873 |
| 65 | `"school based"[tiab]` | 10,873 |
| 66 | `"school setting"[tiab]` | 1,684 |
| 67 | `"school settings"[tiab]` | 1,086 |
| 68 | `"school-delivered"[tiab]` | 13 |
| 69 | `"school delivered"[tiab]` | 13 |
| 70 | `#60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69` | 316,648 |
| 71 | `#37 AND #59 AND #70` | 25,151 |
| 72 | `#71 AND 1800:2017/12/14[dp]` | 25,088 |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR "nutrition education"[tiab] OR "diet education"[tiab] OR "dietary education"[tiab] OR "food education"[tiab] OR "food and nutrition education"[tiab] OR "nutrition instruction"[tiab] OR "nutrition training"[tiab] OR "nutrition promotion"[tiab] OR "nutrition intervention"[tiab] OR "nutrition interventions"[tiab] OR "dietary intervention"[tiab] OR "dietary interventions"[tiab] OR "nutrition program"[tiab] OR "nutrition programs"[tiab] OR "nutrition programme"[tiab] OR "nutrition programmes"[tiab] OR "healthy eating education"[tiab] OR "food literacy"[tiab] OR "nutrition literacy"[tiab] OR "eating education"[tiab] OR "dietary behavior intervention"[tiab] OR "health promotion"[tiab] OR "dietary habits"[tiab] OR nutrition[tiab] OR cooking[tiab] OR "Cooking"[Mesh] OR gardening[tiab] OR "Gardening"[Mesh] OR "nutrition curriculum"[tiab] OR "nutrition curricula"[tiab] OR "nutrition counseling"[tiab] OR "nutrition counselling"[tiab] OR "dietary counseling"[tiab] OR "dietary counselling"[tiab]) AND ("Adolescent"[Mesh] OR "Child"[Mesh] OR "Students"[Mesh] OR adolescen*[tiab] OR teen*[tiab] OR youth*[tiab] OR child*[tiab] OR student*[tiab] OR schoolchild*[tiab] OR pupil*[tiab] OR "high school"[tiab] OR "middle school"[tiab] OR "secondary school"[tiab] OR "primary school"[tiab] OR "school student"[tiab] OR "school students"[tiab] OR "school children"[tiab] OR "schoolchild"[tiab] OR "schoolchildren"[tiab] OR "school aged"[tiab] OR "school-aged"[tiab]) AND ("School Health Services"[Mesh] OR "Schools"[Mesh] OR school*[tiab] OR classroom*[tiab] OR "school-based"[tiab] OR "school based"[tiab] OR "school setting"[tiab] OR "school settings"[tiab] OR "school-delivered"[tiab] OR "school delivered"[tiab])) AND (1800:2017/12/14[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 222,784 | 0 |
| population | 29,968 | 0 |
| school_delivery | 111,755 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 69,482 | initial | none | Initial broad two-block search with explicit PubMed MeSH and title/abstract terms; screened school delivery and dietary-consumption outcome; date bound required by historical run. |
| 2 | 111,302 | education: +7 / -1; population: +2 / -1 | none | Removed PubMed phrase and truncation warnings; added recurrent screened-record wording from term mining (nutrition, health promotion, dietary habits, cooking, gardening); replaced invalid school-age truncation with explicit spelling variants. |
| 3 | 25,070 | school_delivery: +10 / -0 | none | Promoted school delivery to a broad required block because it defines the topic and eligibility; added MeSH and text variants; explicitly measured effect on screened development records. |
| 4 | 25,088 | education: +8 / -0 | none | Added nutrition/food/diet curriculum and US/UK counseling phrases requested by round-1 internal critic; direct MeSH lookup found no dedicated Nutrition Education heading, so the closest Health Education heading remains and this limitation will be documented. |
| 5 | 25,088 | education: +0 / -2 | none | Removed two curriculum phrases that PubMed flagged as phrase-not-found/no-result; retained nutrition curriculum and counseling variants from critic. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 3 findings; F1 should-fix open, F2 should-fix open, F3 document open
- Round 2 on version 5: 3 findings; F1 should-fix accepted-risk, F2 should-fix resolved, F3 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 692 NCBI requests logged (373 from cache); strategy sha256 9dd17d8661e6._

## Rationale

The strategy searches three required concepts: food/nutrition education, adolescents or school students, and school delivery. The Health Education heading (exploded) is the closest broad education descriptor. The MeSH lookup returned no dedicated Nutrition Education heading. Health Promotion is also exploded and retained because school nutrition programs may be indexed as health promotion. For school delivery, School Health Services and Schools are exploded; text words cover school, classroom, school-based, school setting, and school-delivered phrasing. The population block combines Adolescent, Child, and Students headings with age and school-level wording; no age filter is applied because the question also includes school students and PubMed age indexing is variable.

Text terms include nutrition/diet/food education, instruction, training, interventions and programs; curriculum and US/UK counseling variants were added after internal critique. Nutrition, cooking, and gardening wording is retained to catch educational interventions described through their activities. These broad terms increase noise but preserve recall. Food-consumption outcomes and comparator are screened rather than AND-ed. No study-design filter is used. The publication-date limit through 2017-12-14 implements the required historical cutoff; `as_of` also limits records by PubMed entry date.

## How known records were found

No seed articles were supplied. PubMed systematic-review searches found relevant discovery leads, including PMID 27122145 (school-based interventions to modify dietary behavior) and PMID 27720105 (multi-strategy nutrition education for adolescents). The review candidates were not used as benchmark sets because their included-study lists could not be retrieved through the configured citation-neighbor interface. Three focused pilot samples returned 130 result entries in total; records may overlap across samples. Fifteen likely candidates were fetched with abstracts and screened more closely. Nine primary studies were clearly eligible and added to the `relevant` development set. No independent validation set was available. The reported 100% relative recall is development recall only; it is not an estimate of sensitivity.

## Critic dispositions

Two rounds of fresh-context PRESS-structured internal critique were completed. F1 (no dedicated nutrition-education MeSH heading) is accepted risk after `psb mesh lookup` returned no match for Nutrition Education; the closest Health Education and Health Promotion headings remain, alongside nutrition-specific text terms. F2 was resolved by adding nutrition curriculum/curricula and nutrition/dietary counseling/counselling terms, then removing two curriculum phrases that PubMed flagged as unavailable. F3 was resolved in the audit by explicitly documenting that all nine records are development records and there is no independent validation. The critic is internal QA, not PRESS peer review.

## Open risks for the peer reviewer

The school-delivery block is required and may miss eligible records whose title/abstract and indexing omit the school setting. All nine development records were retrieved by this block, but that is not independent evidence of recall. The broad Health Education and Health Promotion headings and general terms such as `nutrition[tiab]` contribute substantial noise; the final result contains 25,088 records through the cutoff, and a small sample included many off-topic health-education records. The interpretation of “school students” may include younger children, as reflected in the broad population block. Confirm the eligible consumption outcomes and school-delivery rule against the protocol, inspect the noisy result sample, and obtain PRESS peer review from an information specialist before use.
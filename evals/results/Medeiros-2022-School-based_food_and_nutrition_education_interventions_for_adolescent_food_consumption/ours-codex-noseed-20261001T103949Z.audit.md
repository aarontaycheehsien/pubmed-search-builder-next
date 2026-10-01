# PubMed search strategy: audit

Generated 2026-10-01T11:21:12+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User requested standard depth and asked that work proceed without clarification. Scope was not confirmed by the user (scope_confirmed=false). Assumptions: school-age pupils qualify when exact age is unstated; eligible outcomes include actual food/dietary intake, consumption frequency, dietary behavior, or food choice; knowledge, attitudes, preferences alone, and BMI alone do not qualify. No language, publication-date, age, or study-design limits. PubMed entry-date cutoff is 2017-12-14 per harness (PSB_AS_OF retained for every command), with no publication-date limit. No user-supplied known records. Prior-review search found candidate reviews but no included-study list; citation-neighbour retrieval returned no records. Two precise pilot samples screened against the criteria produced five development records; the optional loss samples and category probes were also screened.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food or nutrition education intervention | search | The intervention is central to the question and should be named or indexed; related named members include nutrition education, nutrition instruction, dietary education, and food education. |
| Adolescents or school students | search | The review is limited to adolescents or school students. Use broad age and student vocabulary plus exploded headings; school-age populations may be indexed under child, adolescent, or students. |
| Delivery through a school | optional | School delivery defines eligibility and authors often name schools, but setting may be absent from abstracts; test its yield before deciding whether to AND it. |
| Eligible food-consumption outcomes | optional | Food consumption defines the topic, but outcome reporting is inconsistent; test an outcome block with a loss sample before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:20:21+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 17,364
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("Health Education"[Mesh] AND ("Eating"[Mesh] OR "Feeding Behavior"[Mesh] OR "Food Preferences"[Mesh]))` | 9,175 | none |
| 2 | `"nutrition education"[tiab]` | 3,866 | none |
| 3 | `(nutrition[tiab] AND educat*[tiab])` | 15,639 | none |
| 4 | `"nutrition instruction"[tiab]` | 46 | none |
| 5 | `(food[tiab] AND educat*[tiab])` | 14,084 | none |
| 6 | `"food education"[tiab]` | 84 | none |
| 7 | `"dietary education"[tiab]` | 252 | none |
| 8 | `(diet*[tiab] AND educat*[tiab])` | 18,660 | none |
| 9 | `"healthy eating education"[tiab]` | 7 | none |
| 10 | `("healthy eating"[tiab] AND educat*[tiab])` | 1,246 | none |
| 11 | `"nutrition curriculum"[tiab]` | 87 | none |
| 12 | `"nutrition program"[tiab]` | 1,227 | none |
| 13 | `"nutrition programs"[tiab]` | 970 | none |
| 14 | `"nutrition intervention"[tiab]` | 1,150 | none |
| 15 | `"nutrition interventions"[tiab]` | 873 | none |
| 16 | `"nutrition counseling"[tiab]` | 559 | none |
| 17 | `"nutrition counselling"[tiab]` | 148 | none |
| 18 | `"cooking education"[tiab]` | 6 | none |
| 19 | `(cook*[tiab] AND educat*[tiab])` | 1,510 | none |
| 20 | `(food[tiab] AND literac*[tiab])` | 511 | none |
| 21 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 47,292 | none |
| 22 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 23 | `"Child"[Mesh]` | 1,797,170 | none |
| 24 | `"Students"[Mesh]` | 112,971 | none |
| 25 | `adolescent*[tiab]` | 213,221 | none |
| 26 | `teen*[tiab]` | 26,895 | none |
| 27 | `youth*[tiab]` | 64,596 | none |
| 28 | `schoolchild*[tiab]` | 13,052 | none |
| 29 | `"school children"[tiab]` | 20,666 | none |
| 30 | `"school child"[tiab]` | 495 | none |
| 31 | `student*[tiab]` | 234,078 | none |
| 32 | `pupil*[tiab]` | 26,074 | none |
| 33 | `schoolboy*[tiab]` | 469 | none |
| 34 | `schoolgirl*[tiab]` | 785 | none |
| 35 | `"young people"[tiab]` | 23,082 | none |
| 36 | `"young person"[tiab]` | 1,094 | none |
| 37 | `"young persons"[tiab]` | 2,277 | none |
| 38 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 3,090,080 | none |
| 39 | `#21 AND #38` | 17,364 | none |

### Strategy (single line, for copying into PubMed)

```text
((("Health Education"[Mesh] AND ("Eating"[Mesh] OR "Feeding Behavior"[Mesh] OR "Food Preferences"[Mesh])) OR "nutrition education"[tiab] OR (nutrition[tiab] AND educat*[tiab]) OR "nutrition instruction"[tiab] OR (food[tiab] AND educat*[tiab]) OR "food education"[tiab] OR "dietary education"[tiab] OR (diet*[tiab] AND educat*[tiab]) OR "healthy eating education"[tiab] OR ("healthy eating"[tiab] AND educat*[tiab]) OR "nutrition curriculum"[tiab] OR "nutrition program"[tiab] OR "nutrition programs"[tiab] OR "nutrition intervention"[tiab] OR "nutrition interventions"[tiab] OR "nutrition counseling"[tiab] OR "nutrition counselling"[tiab] OR "cooking education"[tiab] OR (cook*[tiab] AND educat*[tiab]) OR (food[tiab] AND literac*[tiab])) AND ("Adolescent"[Mesh] OR "Child"[Mesh] OR "Students"[Mesh] OR adolescent*[tiab] OR teen*[tiab] OR youth*[tiab] OR schoolchild*[tiab] OR "school children"[tiab] OR "school child"[tiab] OR student*[tiab] OR pupil*[tiab] OR schoolboy*[tiab] OR schoolgirl*[tiab] OR "young people"[tiab] OR "young person"[tiab] OR "young persons"[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Delivery through a school | left out | 17,364 / 5,619 | 67.6% | none | 0/30 (up to 10% of removed records could be relevant) | The 30-record loss sample had no eligible records and this block reduces the base count by 67.6%, but only 2 development records are known, below the skill's minimum of 15 required to justify AND-ing an optional block; leave it out to protect recall. |
| Eligible food-consumption outcomes | left out | 17,364 / 11,973 | 31.0% | none | 0/30 (up to 10% of removed records could be relevant) | The 30-record loss sample had no eligible records and this block reduces the base count by 31.0%, but only 2 development records are known, below the skill's minimum of 15 required to justify AND-ing an optional block; leave it out to protect recall. Food-consumption outcomes will be screened. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food or nutrition education intervention | 1 | `nutrition[tiab] OR food[tiab] OR diet*[tiab] OR cook*[tiab] OR Food Habits[Mesh]` | 106,322 | not screened |
| Food or nutrition education intervention | 2 | `nutrition[tiab] OR food[tiab] OR diet*[tiab] OR cook*[tiab] OR Food Habits[Mesh]` | 106,322 | 0/30 |
| Adolescents or school students | 1 | `school*[tiab] OR grade*[tiab] OR child*[tiab] OR teen*[tiab] OR student*[tiab] OR youth*[tiab] OR adolescent*[tiab] OR elementary[tiab] OR primary[tiab] OR secondary[tiab]` | 7,988 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| food_education | 3,090,080 | 0 |
| population | 47,292 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 71,522 | initial | none | Initial broad intervention and population blocks; school setting and food-consumption outcome retained as candidates pending optional-block testing. Terms informed by MeSH lookup/show and screened pilot records. |
| 2 | 17,364 | food_education: +1 / -2 | none | Refined the MeSH layer: constrain broad Health Education indexing to food/eating-related headings; removed food curriculum after PubMed returned zero hits. Retained text synonyms. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (Same-context critic: no fresh-context reviewer session was available in this host. Reviewed only the current packet against the six PRESS domains.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 885 NCBI requests logged (505 from cache); strategy sha256 fa18fede1479._

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
        "message": "17,364 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:school_setting",
        "blocking": false,
        "requires_review": true,
        "id": "I-2309f5c601b2ba2cb81e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:food_consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-63abf816ed820cb2628e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "17,364 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:school_setting",
        "blocking": false,
        "requires_review": true,
        "id": "I-2309f5c601b2ba2cb81e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:food_consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-63abf816ed820cb2628e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006266",
          "name": "Health Education",
          "type": "descriptor",
          "scope_note": "Education that increases the awareness and favorably influences the knowledge, attitudes, and behaviors relating to the improvement of health on a personal or community basis.",
          "tree_numbers": [
            "H02.403.720.750.380",
            "N02.421.726.407"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006266",
      "preferred_label": "Health Education",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Health Education\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Eating",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004435",
          "name": "Eating",
          "type": "descriptor",
          "scope_note": "The consumption of edible substances.",
          "tree_numbers": [
            "G07.203.650.283",
            "G10.261.330"
          ],
          "entry_terms": 21,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004435",
      "preferred_label": "Eating",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Eating\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:21+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005518",
          "name": "Food Preferences",
          "type": "descriptor",
          "scope_note": "The selection of one food over another.",
          "tree_numbers": [
            "F01.145.407.516",
            "G07.203.650.353.516"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005518",
      "preferred_label": "Food Preferences",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000293",
          "name": "Adolescent",
          "type": "descriptor",
          "scope_note": "A person 13 to 18 years of age.",
          "tree_numbers": [
            "M01.060.057"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000293",
      "preferred_label": "Adolescent",
      "type": "descriptor",
      "location": "vocabulary:30",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002648",
          "name": "Child",
          "type": "descriptor",
          "scope_note": "A person 6 to 12 years of age. An individual 2 to 5 years old is CHILD, PRESCHOOL.",
          "tree_numbers": [
            "M01.060.406"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002648",
      "preferred_label": "Child",
      "type": "descriptor",
      "location": "vocabulary:31",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013334",
          "name": "Students",
          "type": "descriptor",
          "scope_note": "Individuals enrolled in a school or formal educational program.",
          "tree_numbers": [
            "M01.848"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013334",
      "preferred_label": "Students",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "((\"Health Education\"[MeSH Terms] AND (\"Eating\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms])) OR \"nutrition education\"[Title/Abstract] OR (\"nutrition\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR \"nutrition instruction\"[Title/Abstract] OR (\"food\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR \"food education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR (\"diet*\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR \"healthy eating education\"[Title/Abstract] OR (\"healthy eating\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR \"nutrition curriculum\"[Title/Abstract] OR \"nutrition program\"[Title/Abstract] OR \"nutrition programs\"[Title/Abstract] OR \"nutrition intervention\"[Title/Abstract] OR \"nutrition interventions\"[Title/Abstract] OR \"nutrition counseling\"[Title/Abstract] OR \"nutrition counselling\"[Title/Abstract] OR \"cooking education\"[Title/Abstract] OR (\"cook*\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR (\"food\"[Title/Abstract] AND \"literac*\"[Title/Abstract])) AND (\"Adolescent\"[MeSH Terms] OR \"Child\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"adolescent*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"school children\"[Title/Abstract] OR \"school child\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"schoolboy*\"[Title/Abstract] OR \"schoolgirl*\"[Title/Abstract] OR \"young people\"[Title/Abstract] OR \"young person\"[Title/Abstract] OR \"young persons\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "6e46572bb3df1a6a7ae7ac3a5262f65a08f8d12feeb5fb87a66c6dd16a49b510",
      "note": "Same-context critic: no fresh-context reviewer session was available in this host. Reviewed only the current packet against the six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two AND-ed blocks represent the named intervention and adolescent/school-student population. School delivery and food-consumption outcomes remain screening criteria after optional tests; both optional blocks were left out because five known records are below the minimum of 15."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within blocks and the intervention and population blocks are AND-ed. No NOT or unvalidated study-design filter is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Health Education is paired with Eating, Feeding Behavior, and Food Preferences headings to keep the broad education heading topic-relevant. Adolescent, Child, and Students headings cover the population; all headings were verified by the tool."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover nutrition, food, dietary, healthy-eating, cooking, literacy, instruction, curriculum, programs/interventions, counseling/counselling, and adolescent/student variants. All five development records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Every term is field-tagged, syntax lint is clean, and current evaluation reports no PubMed translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or study-design filter is applied. The harness entry-date bound is 2017-12-14, without a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 17,364-record result exceeds the default 10,000 screening budget. The optional school-setting and food-consumption blocks were tested and left out to protect recall because only five development records are known; the report should flag the larger screening workload for the human peer reviewer.",
          "evidence": "Current evaluation count 17,364; both optional blocks reduce the count (school setting 67.6%, food consumption 31.0%) but only five relevant development records are available. Loss samples found 0/30 eligible records for each block. The main query retrieves all five development records."
        },
        {
          "issue_id": "I-2309f5c601b2ba2cb81e",
          "status": "accepted-risk",
          "response": "A benchmark search, citation-neighbour attempt, and two precise pilot samples were tried. The evidence remains too small to justify AND-ing the school-setting block; retain it for screening and flag the unresolved recall/workload tradeoff for PRESS peer review.",
          "evidence": "The prior-review search returned 27 candidates; sampled/fetched review abstracts did not provide an included-study list. The citation-neighbour command returned 0 candidates. Two pilot samples yielded five screened relevant records in total. The school-setting loss sample contained 0/30 relevant records, but the five known records are below the required 15."
        },
        {
          "issue_id": "I-63abf816ed820cb2628e",
          "status": "accepted-risk",
          "response": "A benchmark search, citation-neighbour attempt, and two precise pilot samples were tried. The evidence remains too small to justify AND-ing the food-consumption outcome block; retain outcomes for screening and flag the unresolved recall/workload tradeoff for PRESS peer review.",
          "evidence": "The prior-review search returned 27 candidates; sampled/fetched review abstracts did not provide an included-study list. The citation-neighbour command returned 0 candidates. Two pilot samples yielded five screened relevant records in total. The outcome loss sample contained 0/30 relevant records, but the five known records are below the required 15."
        }
      ]
    }
  ]
}
```


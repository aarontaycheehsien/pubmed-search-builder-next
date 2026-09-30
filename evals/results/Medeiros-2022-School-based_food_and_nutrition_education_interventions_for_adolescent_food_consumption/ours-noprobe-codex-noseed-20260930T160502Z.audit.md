# PubMed search strategy: audit

Generated 2026-09-30T17:11:34+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User requested no questions and asked to proceed with reasonable decisions. Scope roles are provisional operational choices; the user asked not to pause, so proceeded without scope confirmation. No known relevant articles supplied. Work as of 2017-12-14 using the PSB_AS_OF Entrez-date bound for every PubMed command; no publication-date limit. Search setting and outcome as optional candidates; no limits. The 2017-12-14 Entrez entry-date bound is required by the task harness to exclude records added to PubMed after the as-of date; do not use a publication-date ([dp]) limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food or nutrition education intervention | search | The intervention defines the topic; use a broad education and nutrition education vocabulary. |
| Adolescents or school students | search | Population is central and can be searched through age and student language, while screening retains broader school-student records. |
| School delivery setting | optional | School delivery is an eligibility criterion and setting labels are searchable but may be omitted in abstracts; test before deciding to AND. |
| Eligible food-consumption outcome | optional | The topic is about food consumption, but outcome reporting is inconsistent; test a broad food intake/diet behavior block before deciding. |
| Intervention delivered through a school and study design | screen | Confirm delivery route and design at screening; do not use an ad hoc study-design filter. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T17:10:06+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 13,229
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Health Education[Mesh]` | 221,709 | none |
| 2 | `Health Promotion[Mesh]` | 70,478 | none |
| 3 | `Child Nutrition Sciences[Mesh]` | 1,076 | none |
| 4 | `nutrition education[tiab]` | 3,866 | none |
| 5 | `dietary education[tiab]` | 252 | none |
| 6 | `food education[tiab]` | 84 | none |
| 7 | `healthy eating education[tiab]` | 7 | none |
| 8 | `nutrition intervention*[tiab]` | 1,929 | none |
| 9 | `dietary intervention*[tiab]` | 5,988 | none |
| 10 | `intervention*[tiab]` | 788,474 | none |
| 11 | `food[tiab]` | 349,337 | none |
| 12 | `nutrition[tiab]` | 147,533 | none |
| 13 | `education[tiab]` | 397,711 | none |
| 14 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 1,687,797 | none |
| 15 | `Adolescent[Mesh]` | 1,895,608 | none |
| 16 | `Child[Mesh]` | 1,797,170 | none |
| 17 | `Students[Mesh]` | 112,971 | none |
| 18 | `adolescent*[tiab]` | 213,221 | none |
| 19 | `teen*[tiab]` | 26,895 | none |
| 20 | `youth[tiab]` | 57,369 | none |
| 21 | `young people[tiab]` | 23,082 | none |
| 22 | `child*[tiab]` | 1,257,861 | none |
| 23 | `student*[tiab]` | 234,078 | none |
| 24 | `schoolchild*[tiab]` | 13,052 | none |
| 25 | `pupil*[tiab]` | 26,074 | none |
| 26 | `#15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 3,394,293 | none |
| 27 | `Schools[Mesh]` | 107,820 | none |
| 28 | `School Health Services[Mesh]` | 21,872 | none |
| 29 | `school*[tiab]` | 246,627 | none |
| 30 | `school-based[tiab]` | 10,873 | none |
| 31 | `classroom*[tiab]` | 14,159 | none |
| 32 | `schoolchild*[tiab]` | 13,052 | none |
| 33 | `primary school*[tiab]` | 10,360 | none |
| 34 | `secondary school*[tiab]` | 8,822 | none |
| 35 | `middle school*[tiab]` | 4,703 | none |
| 36 | `high school*[tiab]` | 27,028 | none |
| 37 | `in-school[tiab]` | 17,617 | none |
| 38 | `#27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 316,648 | none |
| 39 | `Eating[Mesh]` | 68,536 | none |
| 40 | `Feeding Behavior[Mesh]` | 156,434 | none |
| 41 | `Diet[Mesh]` | 254,824 | none |
| 42 | `Food Preferences[Mesh]` | 13,063 | none |
| 43 | `Diet Surveys[Mesh]` | 7,796 | none |
| 44 | `eating[tiab]` | 61,958 | none |
| 45 | `diet*[tiab]` | 494,942 | none |
| 46 | `food intake[tiab]` | 39,819 | none |
| 47 | `dietary intake[tiab]` | 20,267 | none |
| 48 | `food consumption[tiab]` | 11,651 | none |
| 49 | `consum*[tiab]` | 389,559 | none |
| 50 | `fruit*[tiab]` | 87,538 | none |
| 51 | `vegetable*[tiab]` | 46,125 | none |
| 52 | `beverage*[tiab]` | 21,544 | none |
| 53 | `sugar-sweetened beverage*[tiab]` | 1,699 | none |
| 54 | `#39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53` | 1,136,952 | none |
| 55 | `#14 AND #26 AND #38 AND #54` | 13,229 | none |

### Strategy (single line, for copying into PubMed)

```text
((Health Education[Mesh] OR Health Promotion[Mesh] OR Child Nutrition Sciences[Mesh] OR nutrition education[tiab] OR dietary education[tiab] OR food education[tiab] OR healthy eating education[tiab] OR nutrition intervention*[tiab] OR dietary intervention*[tiab] OR intervention*[tiab] OR food[tiab] OR nutrition[tiab] OR education[tiab]) AND (Adolescent[Mesh] OR Child[Mesh] OR Students[Mesh] OR adolescent*[tiab] OR teen*[tiab] OR youth[tiab] OR young people[tiab] OR child*[tiab] OR student*[tiab] OR schoolchild*[tiab] OR pupil*[tiab]) AND (Schools[Mesh] OR School Health Services[Mesh] OR school*[tiab] OR school-based[tiab] OR classroom*[tiab] OR schoolchild*[tiab] OR primary school*[tiab] OR secondary school*[tiab] OR middle school*[tiab] OR high school*[tiab] OR in-school[tiab]) AND (Eating[Mesh] OR Feeding Behavior[Mesh] OR Diet[Mesh] OR Food Preferences[Mesh] OR Diet Surveys[Mesh] OR eating[tiab] OR diet*[tiab] OR food intake[tiab] OR dietary intake[tiab] OR food consumption[tiab] OR consum*[tiab] OR fruit*[tiab] OR vegetable*[tiab] OR beverage*[tiab] OR sugar-sweetened beverage*[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
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
| School delivery setting | AND-ed | 69,616 / 13,229 | 81.0% | none | 0/30 (up to 10% of removed records could be relevant) | Re-tested after adding bare food, nutrition and education terms: 0 relevant records among 30 screened from the current loss sample. All 19 known relevant records remain retrieved; the school block reduces the no-school count from 69,616 to 13,229 (81.0%). School delivery is an explicit eligibility criterion. |
| Eligible food-consumption outcome | AND-ed | 80,298 / 13,229 | 83.5% | none | 0/30 (up to 10% of removed records could be relevant) | Re-tested after adding bare food, nutrition and education terms: 0 relevant records among 30 screened from the current loss sample. All 19 known relevant records remain retrieved; the outcome block reduces the no-outcome count from 80,298 to 13,229 (83.5%). Food consumption is an explicit eligibility criterion. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nutrition_education | 21,568 | 0 |
| adolescents_students | 15,015 | 0 |
| school_setting | 69,616 | 0 |
| food_consumption | 80,298 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 68,022 | initial | none | Initial two-block intervention and school-age population strategy; school setting and consumption outcome added as optional candidates for measured testing. Scope and terms set before reading candidates. User supplied no known articles; identified 27720105 as a matching prior review but NCBI reference links returned no records. Screened related PubMed candidates; two primary reports met stated eligibility and entered the relevant set. |
| 2 | 223,524 | nutrition_education: +6 / -0 | none | Added Child Nutrition Sciences[Mesh] and high-coverage title/abstract terms nutrition and education based on psb terms rank for 19 screened relevant records; no known records should be lost. |
| 3 | 68,438 | nutrition_education: +0 / -4 | none | Removed duplicate entries and removed standalone nutrition and education terms after psb eval showed they inflated the base count from 68,022 to 223,524; retained specific intervention terms and Child Nutrition Sciences[Mesh]. No relevant known record is expected to be lost; verify against all 19 screened records. |
| 4 | 18,155 | school_setting: +11 / -0 | none | Applied the school_setting optional decision as AND based on 19 known records, no loss in the screened 30-record sample, and 73.9% count reduction. |
| 5 | 3,893 | food_consumption: +15 / -0 | none | Applied the food_consumption optional decision as AND after re-sampling the loss set under the current school-setting query: 0 relevant in 30, all 19 known retained, 78.6% reduction and final count 3,893. |
| 6 | 7,125 | nutrition_education: +1 / -0 | none | Added intervention*[tiab] per critic finding R1-F2. R1-F1's suggested Nutrition Education[Mesh] remains rejected: live PSB lookup/show found no record and count revealed All Fields fallback. Verify no known records lost and inspect refreshed optional decisions. |
| 7 | 13,229 | nutrition_education: +3 / -0 | none | Added bare food[tiab], nutrition[tiab], and education[tiab] to the intervention block per critic R2-F1; explicitly recorded the harness-mandated Entrez entry-date rationale in protocol notes. Measure count, recall and refresh optional decisions. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 2 findings; R1-F1 should-fix rejected, R1-F2 should-fix resolved
- Round 2 on version 6: 4 findings; R1-F1 should-fix rejected, R1-F2 should-fix resolved, R2-F1 should-fix open, R2-F2 must-fix rejected
- Round 3 on version 7: 4 findings; R1-F1 should-fix rejected, R1-F2 should-fix resolved, R2-F1 should-fix resolved, R2-F2 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1931 NCBI requests logged (1090 from cache); strategy sha256 92d7e1541814._

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
        "message": "13,229 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "13,229 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
        "text": "Health Education",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Promotion",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Health Promotion",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D053198",
          "name": "Child Nutrition Sciences",
          "type": "descriptor",
          "scope_note": "The study of NUTRITION PROCESSES as well as the components of food, their actions, interaction, and balance in relation to health and disease of children, infants or adolescents.",
          "tree_numbers": [
            "H02.533.252"
          ],
          "entry_terms": 35,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D053198",
      "preferred_label": "Child Nutrition Sciences",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Child Nutrition Sciences",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Adolescent",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "Child",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "Students",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012574",
          "name": "Schools",
          "type": "descriptor",
          "scope_note": "Educational institutions.",
          "tree_numbers": [
            "I02.783",
            "J03.832"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012574",
      "preferred_label": "Schools",
      "type": "descriptor",
      "location": "vocabulary:25",
      "term": {
        "text": "Schools",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012572",
          "name": "School Health Services",
          "type": "descriptor",
          "scope_note": "Preventive health services provided for students. It excludes college or university students.",
          "tree_numbers": [
            "N02.421.726.809"
          ],
          "entry_terms": 23,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012572",
      "preferred_label": "School Health Services",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "School Health Services",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Eating",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Eating",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Food Preferences",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet Surveys",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:10:06+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004034",
          "name": "Diet Surveys",
          "type": "descriptor",
          "scope_note": "Systematic collections of factual data pertaining to the diet of a human population within a given geographic area.",
          "tree_numbers": [
            "E05.318.308.980.485.350",
            "N05.715.360.300.800.469.300",
            "N06.850.505.616.300",
            "N06.850.520.308.980.469.350"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004034",
      "preferred_label": "Diet Surveys",
      "type": "descriptor",
      "location": "vocabulary:40",
      "term": {
        "text": "Diet Surveys",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"health education\"[MeSH Terms] OR \"health promotion\"[MeSH Terms] OR \"child nutrition sciences\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"healthy eating education\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"dietary intervention*\"[Title/Abstract] OR \"intervention*\"[Title/Abstract] OR \"food\"[Title/Abstract] OR \"nutrition\"[Title/Abstract] OR \"education\"[Title/Abstract]) AND (\"adolescent\"[MeSH Terms] OR \"child\"[MeSH Terms] OR \"students\"[MeSH Terms] OR \"adolescent*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth\"[Title/Abstract] OR \"young people\"[Title/Abstract] OR \"child*\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract]) AND (\"schools\"[MeSH Terms] OR \"school health services\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"primary school*\"[Title/Abstract] OR \"secondary school*\"[Title/Abstract] OR \"middle school*\"[Title/Abstract] OR \"high school*\"[Title/Abstract] OR \"in-school\"[Title/Abstract]) AND (\"eating\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"diet\"[MeSH Terms] OR \"food preferences\"[MeSH Terms] OR \"diet surveys\"[MeSH Terms] OR \"eating\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"dietary intake\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"consum*\"[Title/Abstract] OR \"fruit*\"[Title/Abstract] OR \"vegetable*\"[Title/Abstract] OR \"beverage*\"[Title/Abstract] OR \"sugar sweetened beverage*\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "b16473bdf892eea1befdd43a34978be028e356a136aa65c56ee6edb06abbb3ed",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Intervention wording under review; the next strategy version adds intervention*[tiab]."
        },
        "operators": {
          "verdict": "pass",
          "note": "The four concept blocks are combined with AND; terms within blocks use OR."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The proposed Nutrition Education heading was checked live and no MeSH record was found."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The bare intervention term is being added in the next strategy version."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors or translation issues were present in the packet."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unnecessary limits or ad hoc study design filter were used; optional blocks were tested."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block omits a Nutrition Education MeSH heading.",
          "recommendation": "Add Nutrition Education[Mesh].",
          "status": "rejected",
          "response": "Rejected because the current PSB MeSH lookup returned no matching descriptor, mesh show reported no MeSH record for Nutrition Education, and count of the proposed expression translated to All Fields (an unintended fallback). The verified Health Education descriptor is already included; its MeSH entry terms do not include Nutrition Education. No invalid heading will be added."
        },
        {
          "id": "R1-F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block lacks intervention as a bare text word.",
          "recommendation": "Add intervention*[tiab].",
          "status": "resolved",
          "response": "Added intervention*[tiab] to the nutrition_education block and will verify it through the complete current evaluation."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "143619a4b217275ccf53b88c2681300d31411a9d1ba6b60498d7d852ecaeee5d",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The closing strategy will test the bare food, nutrition and education text words as requested."
        },
        "operators": {
          "verdict": "pass",
          "note": "Concept blocks are combined with AND; terms within each block use OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The suggested Nutrition Education heading was rejected on live MeSH lookup evidence."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Bare food, nutrition and education text terms will be added and fully re-evaluated."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors or translation issues were present."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The Entrez entry-date bound is explicitly required by the user and documented in protocol.as_of and notes; no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block omits a Nutrition Education MeSH heading.",
          "recommendation": "Add Nutrition Education[Mesh].",
          "status": "rejected",
          "response": "Rejected because the current PSB MeSH lookup returned no matching descriptor, mesh show reported no MeSH record for Nutrition Education, and the proposed expression translated to All Fields. The verified Health Education descriptor is included; no invalid heading should be added."
        },
        {
          "id": "R1-F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block lacks intervention as a bare text word.",
          "recommendation": "Add intervention*[tiab].",
          "status": "resolved",
          "response": "intervention*[tiab] is included in the nutrition_education block and appears in the evaluated query."
        },
        {
          "id": "R2-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched intervention concept names food, nutrition, and education, but these are not each covered by their own bare text word.",
          "recommendation": "Add bare food[tiab], nutrition[tiab], and education[tiab] terms in the intervention block, retaining the existing specific terms.",
          "status": "open",
          "response": ""
        },
        {
          "id": "R2-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query applies an Entry Date cutoff of 2017-12-14 though the strategy declares no limits.",
          "recommendation": "Remove the cutoff or document and justify it; rerun evaluation.",
          "status": "rejected",
          "response": "Rejected because the task explicitly requires the search to be bounded to records present in PubMed by 2017-12-14 and requires PSB_AS_OF on every PubMed command. protocol.as_of is 2017-12-14 and notes document the user-mandated Entrez entry-date restriction. No [dp] publication-date limit is used; removing the entry-date bound would violate the task instructions."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 7,
      "review_sha256": "fdfae3de2940bac649c8c4e471681b30685ce3d9c100364acb55f3bda14dcb30",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The evaluated query includes intervention*[tiab] and bare food, nutrition, and education terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The four concept blocks are combined with AND and terms within blocks with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Nutrition Education was rejected with live lookup evidence; verified headings remain."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The intervention block includes the requested bare food, nutrition, education, and intervention terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The task-required entry-date bound is documented; no publication-date limit or ad hoc study-design filter is used."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block omits a Nutrition Education MeSH heading.",
          "recommendation": "Add Nutrition Education[Mesh].",
          "status": "rejected",
          "response": "Rejected based on the reported MeSH lookup: no matching descriptor was found, and the proposed expression translated to All Fields. Verified headings remain in the strategy."
        },
        {
          "id": "R1-F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block lacks intervention as a bare text word.",
          "recommendation": "Add intervention*[tiab].",
          "status": "resolved",
          "response": "intervention*[tiab] is in the current nutrition_education block and evaluated query."
        },
        {
          "id": "R2-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched intervention concept names food, nutrition, and education, but does not cover each with its own bare text word.",
          "recommendation": "Add bare food[tiab], nutrition[tiab], and education[tiab] terms while retaining the specific terms.",
          "status": "resolved",
          "response": "All three bare terms are in the current nutrition_education block and evaluated query; the specific terms remain."
        },
        {
          "id": "R2-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query applies an Entry Date cutoff of 2017-12-14 though the strategy declares no limits.",
          "recommendation": "Remove the cutoff or document and justify it; rerun evaluation.",
          "status": "rejected",
          "response": "The packet documents 2017-12-14 as the task-required Entrez entry-date bound in protocol.as_of and notes. The evaluated query applies that entry-date bound; no publication-date limit is used."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains because the final count is above the 10,000-record budget. Both searchable optional concepts were tested as AND-ed blocks; their current loss samples each had 0 relevant records among 30 screened, and all 19 known relevant records remain retrieved.",
          "evidence": "The final strategy retrieves 13,229 records. The school-setting block reduces 69,616 to 13,229; the food-consumption block reduces 80,298 to 13,229. Both report no known records lost and 0/30 relevant records in the loss sample."
        }
      ]
    }
  ]
}
```


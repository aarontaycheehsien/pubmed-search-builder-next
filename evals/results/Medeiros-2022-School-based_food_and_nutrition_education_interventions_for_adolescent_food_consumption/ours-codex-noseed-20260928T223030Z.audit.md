# PubMed search strategy: audit

Generated 2026-09-28T23:03:06+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions. Scope is an intervention-effectiveness PICO; comparators are screened. No language or publication-date limit. PSB_AS_OF bounds records by Entrez date at 2017-12-14. Assumptions: adolescent/school-student terms define population; school delivery and food-consumption outcome are optional blocks to test. User was unavailable to confirm scope.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food or nutrition education intervention | search | Core intervention concept; eligible programmes may be named through specific food, nutrition, dietary or healthy-eating education members. |
| Adolescents or school students | search | Population is explicit in the question and generally searchable through adolescent, youth and student headings and text words; school-grade terminology may stand for the population. |
| Delivered through a school | optional | Central setting but setting is not reliably described in titles/abstracts; test an explicit setting block before deciding. |
| Eligible food-consumption outcomes | optional | Topic-defining outcome that may reduce screening burden, but outcome terminology can be inconsistently indexed; test against screened relevant records and a loss sample. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:01:38+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 5,728
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 3 | `"Child Nutrition Sciences"[Mesh]` | 1,076 | none |
| 4 | `"nutrition education"[tiab]` | 3,866 | none |
| 5 | `"dietary education"[tiab]` | 252 | none |
| 6 | `"food education"[tiab]` | 84 | none |
| 7 | `"healthy eating education"[tiab]` | 7 | none |
| 8 | `"nutrition intervention*"[tiab]` | 1,929 | none |
| 9 | `"nutrition program*"[tiab]` | 2,437 | none |
| 10 | `(nutrition[tiab] AND educat*[tiab])` | 15,639 | none |
| 11 | `(dietary[tiab] AND educat*[tiab])` | 10,281 | none |
| 12 | `(food[tiab] AND educat*[tiab])` | 14,084 | none |
| 13 | `(nutrition[tiab] AND intervention*[tiab])` | 16,941 | none |
| 14 | `(nutrition[tiab] AND program*[tiab])` | 16,279 | none |
| 15 | `(dietary[tiab] AND intervention*[tiab])` | 22,923 | none |
| 16 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 279,494 | none |
| 17 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 18 | `"Students"[Mesh]` | 112,971 | none |
| 19 | `"Child"[Mesh]` | 1,797,170 | none |
| 20 | `adolescen*[tiab]` | 248,945 | none |
| 21 | `teen*[tiab]` | 26,895 | none |
| 22 | `youth[tiab]` | 57,369 | none |
| 23 | `young people[tiab]` | 23,082 | none |
| 24 | `student*[tiab]` | 234,078 | none |
| 25 | `schoolchild*[tiab]` | 13,052 | none |
| 26 | `school-aged[tiab]` | 7,648 | none |
| 27 | `school age[tiab]` | 11,579 | none |
| 28 | `schoolchildren[tiab]` | 12,947 | none |
| 29 | `pupil*[tiab]` | 26,074 | none |
| 30 | `teenager*[tiab]` | 13,059 | none |
| 31 | `#17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30` | 3,092,844 | none |
| 32 | `"Schools"[Mesh]` | 107,820 | none |
| 33 | `"School Health Services"[Mesh]` | 21,872 | none |
| 34 | `school*[tiab]` | 246,627 | none |
| 35 | `classroom*[tiab]` | 14,159 | none |
| 36 | `pupil*[tiab]` | 26,074 | none |
| 37 | `high school*[tiab]` | 27,028 | none |
| 38 | `secondary school*[tiab]` | 8,822 | none |
| 39 | `middle school*[tiab]` | 4,703 | none |
| 40 | `primary school*[tiab]` | 10,360 | none |
| 41 | `elementary school*[tiab]` | 8,563 | none |
| 42 | `#32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41` | 337,595 | none |
| 43 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 44 | `"Eating"[Mesh]` | 68,536 | none |
| 45 | `"Food Preferences"[Mesh]` | 13,063 | none |
| 46 | `"Diet"[Mesh]` | 254,824 | none |
| 47 | `"Fruit"[Mesh]` | 91,855 | none |
| 48 | `"Vegetables"[Mesh]` | 28,363 | none |
| 49 | `diet*[tiab]` | 494,942 | none |
| 50 | `dietary intake[tiab]` | 20,267 | none |
| 51 | `food intake[tiab]` | 39,819 | none |
| 52 | `food consumption[tiab]` | 11,651 | none |
| 53 | `eating behavio*[tiab]` | 7,930 | none |
| 54 | `feeding behavio*[tiab]` | 8,950 | none |
| 55 | `food behavio*[tiab]` | 339 | none |
| 56 | `fruit intake[tiab]` | 893 | none |
| 57 | `vegetable intake[tiab]` | 2,824 | none |
| 58 | `(fruit[tiab] AND vegetable*[tiab])` | 12,790 | none |
| 59 | `healthy eating[tiab]` | 5,052 | none |
| 60 | `food choice*[tiab]` | 3,666 | none |
| 61 | `food preference*[tiab]` | 2,104 | none |
| 62 | `dietary behavio*[tiab]` | 2,349 | none |
| 63 | `consumption[tiab]` | 242,645 | none |
| 64 | `#43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63` | 1,001,208 | none |
| 65 | `#16 AND #31 AND #42 AND #64` | 5,728 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR "Child Nutrition Sciences"[Mesh] OR "nutrition education"[tiab] OR "dietary education"[tiab] OR "food education"[tiab] OR "healthy eating education"[tiab] OR "nutrition intervention*"[tiab] OR "nutrition program*"[tiab] OR (nutrition[tiab] AND educat*[tiab]) OR (dietary[tiab] AND educat*[tiab]) OR (food[tiab] AND educat*[tiab]) OR (nutrition[tiab] AND intervention*[tiab]) OR (nutrition[tiab] AND program*[tiab]) OR (dietary[tiab] AND intervention*[tiab])) AND ("Adolescent"[Mesh] OR "Students"[Mesh] OR "Child"[Mesh] OR adolescen*[tiab] OR teen*[tiab] OR youth[tiab] OR young people[tiab] OR student*[tiab] OR schoolchild*[tiab] OR school-aged[tiab] OR school age[tiab] OR schoolchildren[tiab] OR pupil*[tiab] OR teenager*[tiab]) AND ("Schools"[Mesh] OR "School Health Services"[Mesh] OR school*[tiab] OR classroom*[tiab] OR pupil*[tiab] OR high school*[tiab] OR secondary school*[tiab] OR middle school*[tiab] OR primary school*[tiab] OR elementary school*[tiab]) AND ("Feeding Behavior"[Mesh] OR "Eating"[Mesh] OR "Food Preferences"[Mesh] OR "Diet"[Mesh] OR "Fruit"[Mesh] OR "Vegetables"[Mesh] OR diet*[tiab] OR dietary intake[tiab] OR food intake[tiab] OR food consumption[tiab] OR eating behavio*[tiab] OR feeding behavio*[tiab] OR food behavio*[tiab] OR fruit intake[tiab] OR vegetable intake[tiab] OR (fruit[tiab] AND vegetable*[tiab]) OR healthy eating[tiab] OR food choice*[tiab] OR food preference*[tiab] OR dietary behavio*[tiab] OR consumption[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Delivered through a school | AND-ed | 19,339 / 5,728 | 70.4% | none | 0/30 (up to 10% of removed records could be relevant) | School delivery is an explicit eligibility requirement. Re-screened current 30-record loss sample found no clearly eligible school-delivered food/nutrition education intervention. The query cut is material; this sample is only a risk check, not proof of zero missed eligible studies. |
| Eligible food-consumption outcomes | AND-ed | 21,363 / 5,728 | 73.2% | none | 0/30 (up to 10% of removed records could be relevant) | Food-consumption outcomes are an explicit review eligibility criterion and the topic-defining endpoint. Re-screened current 30-record loss sample found no clearly eligible intervention reporting such an outcome; the reduction is material and puts the final result below the standard workload budget. The sample does not establish zero recall loss; retain this decision for specialist review. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food or nutrition education intervention | 1 | `(food*[tiab] OR diet*[tiab] OR eating[tiab])` | 6,988 | 0/30 |
| Adolescents or school students | 1 | `(Schools[Mesh] OR school*[tiab] OR classroom*[tiab])` | 986 | 0/30 |
| Delivered through a school | 1 | `(curriculum[tiab] OR teacher*[tiab] OR lesson*[tiab] OR class*[tiab] OR educational setting[tiab])` | 1,107 | 0/30 |
| Eligible food-consumption outcomes | 1 | `(breakfast[tiab] OR snack*[tiab] OR beverage*[tiab] OR meal*[tiab] OR sugary[tiab])` | 266 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nutrition_education | 17,819 | 0 |
| adolescents_students | 6,727 | 0 |
| school_setting | 19,339 | 0 |
| food_consumption | 21,363 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 77,447 | initial | none | Initial two-block intervention/population draft; school delivery and food-consumption outcome retained as optional candidates because named but potentially inconsistently indexed. Removed short wildcard eat* after lint identified PubMed would not truncate it. |
| 2 | 21,363 | school_setting: +10 / -0 | none | Added the optional school-delivery block after screening its 30-record loss sample: no clearly eligible studies found; setting is an explicit eligibility criterion and sample does not prove zero loss. |
| 3 | 0 | food_consumption: +21 / -0 | none | Added food-consumption outcome block after screening its current 30-record loss sample: no clearly eligible studies found; outcome is an explicit eligibility criterion and the measured cut reduces the result below budget. |
| 4 | 5,728 | food_consumption: +21 / -0 | none | Rewrote fruit-and-vegetable outcome term as co-occurring tagged fruit/vegetable terms after lint found lowercase Boolean operator and field-tag ambiguity; rerun current full strategy. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4 (same-context critic; a separate reviewer could not access the packet in this environment): 1 findings; R1-1 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 940 NCBI requests logged (411 from cache); strategy sha256 7cd15b2fca43._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [],
    "issues": []
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "requested": "Health Promotion",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
        "text": "\"Health Promotion\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
        "text": "\"Child Nutrition Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Eating",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:47",
      "term": {
        "text": "\"Eating\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:48",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
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
      "location": "vocabulary:49",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fruit",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005638",
          "name": "Fruit",
          "type": "descriptor",
          "scope_note": "The fleshy or dry ripened ovary of a plant, enclosing the seed or seeds.",
          "tree_numbers": [
            "A18.024.500",
            "G07.203.300.562",
            "J02.500.562"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005638",
      "preferred_label": "Fruit",
      "type": "descriptor",
      "location": "vocabulary:50",
      "term": {
        "text": "\"Fruit\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Vegetables",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:01:38+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014675",
          "name": "Vegetables",
          "type": "descriptor",
          "scope_note": "A food group comprised of EDIBLE PLANTS or their parts.",
          "tree_numbers": [
            "B01.650.160.956",
            "B01.650.510.956",
            "G07.203.300.850",
            "J02.500.850"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014675",
      "preferred_label": "Vegetables",
      "type": "descriptor",
      "location": "vocabulary:51",
      "term": {
        "text": "\"Vegetables\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"Child Nutrition Sciences\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"healthy eating education\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR (\"nutrition\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR (\"dietary\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR (\"food\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR (\"nutrition\"[Title/Abstract] AND \"intervention*\"[Title/Abstract]) OR (\"nutrition\"[Title/Abstract] AND \"program*\"[Title/Abstract]) OR (\"dietary\"[Title/Abstract] AND \"intervention*\"[Title/Abstract])) AND (\"Adolescent\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"Child\"[MeSH Terms] OR \"adolescen*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth\"[Title/Abstract] OR \"young people\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"school-aged\"[Title/Abstract] OR \"school age\"[Title/Abstract] OR \"schoolchildren\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"teenager*\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"School Health Services\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"high school*\"[Title/Abstract] OR \"secondary school*\"[Title/Abstract] OR \"middle school*\"[Title/Abstract] OR \"primary school*\"[Title/Abstract] OR \"elementary school*\"[Title/Abstract]) AND (\"Feeding Behavior\"[MeSH Terms] OR \"Eating\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Fruit\"[MeSH Terms] OR \"Vegetables\"[MeSH Terms] OR \"diet*\"[Title/Abstract] OR \"dietary intake\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"eating behavio*\"[Title/Abstract] OR \"feeding behavio*\"[Title/Abstract] OR \"food behavio*\"[Title/Abstract] OR \"fruit intake\"[Title/Abstract] OR \"vegetable intake\"[Title/Abstract] OR (\"Fruit\"[Title/Abstract] AND \"vegetable*\"[Title/Abstract]) OR \"healthy eating\"[Title/Abstract] OR \"food choice*\"[Title/Abstract] OR \"food preference*\"[Title/Abstract] OR \"dietary behavio*\"[Title/Abstract] OR \"consumption\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "efd0718092b4ff1956fd66309aca1d52fd0630d5861795276862b7e11d082fe2",
      "note": "same-context critic; a separate reviewer could not access the packet in this environment",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The four blocks correspond to the intervention, population, school delivery, and food-consumption eligibility concepts. The two optional blocks were tested, AND-ed, and retained against their measured loss samples; both samples were 0/30, though this leaves residual recall uncertainty."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within concepts and AND combines concepts. No NOT or study-design filter is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings are relevant to education, population, school delivery, and diet/feeding outcomes. Diet, Healthy was excluded because its MeSH introduction date is after the historical cutoff; broad Diet and behavior headings remain."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover nutrition/food/diet education, adolescents/students, school settings, and dietary intake/behavior and food consumption. The development set is small and not independent validation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The latest evaluation reports clean lint, valid translation, no translation warnings, and PubMed syntax accepted. No phrase-review diagnostics remain."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limit is applied. The Entrez-date bound ends at 2017-12-14 as required; no [dp] filter is used."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "AND-ing the setting and outcome blocks materially reduces the result set. Their respective random loss samples were only 0/30 eligible records; this does not establish absence of recall loss. The known-record set contains only three records discovered from the pilot query, so its 3/3 retrieval is not independent validation.",
          "recommendation": "Retain the measured trade-off for human information-specialist/PRESS review and consider screening the outcome concept instead of requiring it if maximum recall takes priority over workload.",
          "status": "accepted-risk",
          "response": "Documented in the protocol and handoff. Both optional blocks reduce the result set by over 70% in the two-block comparisons and brought the total below the declared 10,000-record workload budget; neither loss sample found an eligible record. The small samples and pilot-derived relevant set leave residual recall risk, disclosed in the report."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


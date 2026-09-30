# PubMed search strategy: audit

Generated 2026-09-30T13:42:56+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without clarification or scope confirmation; roles are based on the stated eligibility. Assume no language or publication-date limits. PubMed records are bounded by Entrez date through PSB_AS_OF=2017-12-14, with no publication-date limit. No user-supplied known records. Standard screening budget is approximately 150 candidate records.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food and nutrition education intervention | search | Interventions define the review topic, are named and indexed, and every eligible record must include one. |
| Adolescents or school students | optional | Population is searchable but student age and adolescent status may be incompletely named; test its retrieval cost before deciding whether to AND it. |
| School delivery | optional | School delivery defines eligibility and is often named, but may be absent from titles and abstracts; test before deciding whether to AND it. |
| Eligible food-consumption outcomes | optional | The stated review topic is specifically food consumption, an outcome authors usually name in searchable records, but outcome terminology varies; test this concept as an optional block and screen outcomes if left out. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:41:34+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 16,197
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 3 | `"Curriculum"[Mesh]` | 78,491 | none |
| 4 | `"Child Nutrition Sciences"[Mesh]` | 1,076 | none |
| 5 | `"Diet"[Mesh]` | 254,824 | none |
| 6 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 7 | `"nutrition education"[tiab]` | 3,866 | none |
| 8 | `"food education"[tiab]` | 84 | none |
| 9 | `"dietary education"[tiab]` | 252 | none |
| 10 | `"nutrition intervention"[tiab]` | 1,150 | none |
| 11 | `"nutrition interventions"[tiab]` | 873 | none |
| 12 | `nutrition intervention*[tiab]` | 1,929 | none |
| 13 | `nutrition educat*[tiab]` | 4,029 | none |
| 14 | `dietary educat*[tiab]` | 263 | none |
| 15 | `food educat*[tiab]` | 91 | none |
| 16 | `nutrition program*[tiab]` | 2,437 | none |
| 17 | `nutrition programme*[tiab]` | 275 | none |
| 18 | `food program*[tiab]` | 485 | none |
| 19 | `food programme*[tiab]` | 95 | none |
| 20 | `nutrition promot*[tiab]` | 145 | none |
| 21 | `healthy eating program*[tiab]` | 36 | none |
| 22 | `healthy eating intervention*[tiab]` | 58 | none |
| 23 | `dietary intervention*[tiab]` | 5,988 | none |
| 24 | `nutrition curriculum*[tiab]` | 87 | none |
| 25 | `"nutrition instruction"[tiab]` | 46 | none |
| 26 | `"nutrition training"[tiab]` | 175 | none |
| 27 | `intervention*[tiab]` | 788,474 | none |
| 28 | `education*[tiab]` | 475,869 | none |
| 29 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 1,674,824 | none |
| 30 | `"Schools"[Mesh]` | 107,820 | none |
| 31 | `"School Health Services"[Mesh]` | 21,872 | none |
| 32 | `school*[tiab]` | 246,627 | none |
| 33 | `classroom*[tiab]` | 14,159 | none |
| 34 | `school-based[tiab]` | 10,873 | none |
| 35 | `"school based"[tiab]` | 10,873 | none |
| 36 | `"high school*"[tiab]` | 27,028 | none |
| 37 | `"middle school*"[tiab]` | 4,703 | none |
| 38 | `"secondary school*"[tiab]` | 8,822 | none |
| 39 | `"primary school*"[tiab]` | 10,360 | none |
| 40 | `"school-age*"[tiab]` | 18,888 | none |
| 41 | `#30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40` | 316,648 | none |
| 42 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 43 | `"Diet"[Mesh]` | 254,824 | none |
| 44 | `"Food Preferences"[Mesh]` | 13,063 | none |
| 45 | `"Fruit"[Mesh]` | 91,855 | none |
| 46 | `"Vegetables"[Mesh]` | 28,363 | none |
| 47 | `"Beverages"[Mesh]` | 129,606 | none |
| 48 | `"food consumption"[tiab]` | 11,651 | none |
| 49 | `"food intake"[tiab]` | 39,819 | none |
| 50 | `"dietary intake"[tiab]` | 20,267 | none |
| 51 | `"dietary behavior"[tiab]` | 822 | none |
| 52 | `"dietary behaviour"[tiab]` | 402 | none |
| 53 | `"eating behavior"[tiab]` | 3,945 | none |
| 54 | `"eating behaviour"[tiab]` | 1,553 | none |
| 55 | `"eating habit"[tiab]` | 140 | none |
| 56 | `"dietary habit"[tiab]` | 387 | none |
| 57 | `"food habit"[tiab]` | 139 | none |
| 58 | `diet*[tiab]` | 494,942 | none |
| 59 | `consum*[tiab]` | 389,559 | none |
| 60 | `intake[tiab]` | 229,738 | none |
| 61 | `"food choice"[tiab]` | 1,581 | none |
| 62 | `"fruit and vegetable intake"[tiab]` | 1,878 | none |
| 63 | `"fruit and vegetable consumption"[tiab]` | 2,040 | none |
| 64 | `"beverage consumption"[tiab]` | 1,132 | none |
| 65 | `#42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64` | 1,231,928 | none |
| 66 | `#29 AND #41 AND #65` | 16,197 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR "Curriculum"[Mesh] OR "Child Nutrition Sciences"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "nutrition education"[tiab] OR "food education"[tiab] OR "dietary education"[tiab] OR "nutrition intervention"[tiab] OR "nutrition interventions"[tiab] OR nutrition intervention*[tiab] OR nutrition educat*[tiab] OR dietary educat*[tiab] OR food educat*[tiab] OR nutrition program*[tiab] OR nutrition programme*[tiab] OR food program*[tiab] OR food programme*[tiab] OR nutrition promot*[tiab] OR healthy eating program*[tiab] OR healthy eating intervention*[tiab] OR dietary intervention*[tiab] OR nutrition curriculum*[tiab] OR "nutrition instruction"[tiab] OR "nutrition training"[tiab] OR intervention*[tiab] OR education*[tiab]) AND ("Schools"[Mesh] OR "School Health Services"[Mesh] OR school*[tiab] OR classroom*[tiab] OR school-based[tiab] OR "school based"[tiab] OR "high school*"[tiab] OR "middle school*"[tiab] OR "secondary school*"[tiab] OR "primary school*"[tiab] OR "school-age*"[tiab]) AND ("Feeding Behavior"[Mesh] OR "Diet"[Mesh] OR "Food Preferences"[Mesh] OR "Fruit"[Mesh] OR "Vegetables"[Mesh] OR "Beverages"[Mesh] OR "food consumption"[tiab] OR "food intake"[tiab] OR "dietary intake"[tiab] OR "dietary behavior"[tiab] OR "dietary behaviour"[tiab] OR "eating behavior"[tiab] OR "eating behaviour"[tiab] OR "eating habit"[tiab] OR "dietary habit"[tiab] OR "food habit"[tiab] OR diet*[tiab] OR consum*[tiab] OR intake[tiab] OR "food choice"[tiab] OR "fruit and vegetable intake"[tiab] OR "fruit and vegetable consumption"[tiab] OR "beverage consumption"[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 8 | 8 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Adolescents or school students | left out | 16,197 / 14,254 | 12.0% | none | 0/30 (up to 10% of removed records could be relevant) | Against the current school-and-consumption base, the 30-record loss sample contained no eligible record and all 17 known records remain in the strategy, but the population block removed only 1,943 of 16,197 records (12.0%), below the approximate 30% material-reduction criterion. Leave it out and screen population. |
| School delivery | AND-ed | 427,941 / 16,197 | 96.2% | none | 0/30 (up to 10% of removed records could be relevant) | Retain the school-delivery block: the current 30-record loss sample contained no eligible school-based adolescent food/nutrition education studies; AND-ing setting materially reduces screening burden while all 17 known relevant/benchmark records remain retrievable. |
| Eligible food-consumption outcomes | AND-ed | 123,578 / 16,197 | 86.9% | none | 0/30 (up to 10% of removed records could be relevant) | Food consumption is the topic-defining outcome and the stated eligibility requires it. All 17 known records are present in the base, the outcome block materially reduced the base from 123,578 to approximately 16,197 records, and screening its 30-record loss sample found no eligible record. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| intervention | 23,785 | 0 |
| setting | 427,941 | 0 |
| outcome | 123,578 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 308,035 | initial | none | Initial intervention block includes MeSH and broad education/intervention text synonyms. School delivery and adolescent/student population remain candidates for measured optional-block decisions; food-consumption outcomes remain screened due variable reporting. |
| 2 | 1,674,824 | intervention: +6 / -1 | none | Revised intervention block to address known misses with general intervention/education language and feeding/diet MeSH; replaced the dietary curriculum phrase that fell back to All Fields. Reclassified the topic-defining food-consumption outcome as optional and added an outcome candidate for measurement; test all three optional concepts. |
| 3 | 1,674,824 | intervention: +0 / -2 | none | Removed two quoted dietary-curriculum variants after clause tests showed no phrase index and zero retrieval; standard alternatives such as nutrition education and curriculum terms remain. All 17 screened known records are now recovered after adding broad intervention/education terms. |
| 4 | 123,578 | setting: +11 / -0 | none | AND the tested school-delivery block after its optional sample retrieved no eligible record among 30 removed records and preserved all 17 known records, with a material count reduction. Re-evaluate remaining optionals against this current base. |
| 5 | 16,197 | outcome: +23 / -0 | none | AND the tested food-consumption outcome block: it reduced the current school-based strategy materially and its screened loss sample contained no eligible record. Re-evaluate the population optional block against this narrower current query. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5 (same-context critic; no fresh-context reviewer was available): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2992 NCBI requests logged (586 from cache); strategy sha256 f94c2f4df5c0._

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
        "message": "16,197 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "16,197 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "requested": "Curriculum",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "Q000193",
          "name": "education",
          "type": "qualifier",
          "scope_note": "Used for education, training programs, and courses in various fields and disciplines, and for training groups of persons.",
          "tree_numbers": [
            "Y23"
          ],
          "entry_terms": 3,
          "mapped_to": null
        },
        {
          "ui": "D003479",
          "name": "Curriculum",
          "type": "descriptor",
          "scope_note": "A course of study offered by an educational institution.",
          "tree_numbers": [
            "I02.158"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003479",
      "preferred_label": "Curriculum",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Curriculum\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Child Nutrition Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fruit",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"Fruit\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Vegetables",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "\"Vegetables\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Beverages",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:41:34+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001628",
          "name": "Beverages",
          "type": "descriptor",
          "scope_note": "Liquids that are suitable for drinking. (From Merriam Webster Collegiate Dictionary, 10th ed)",
          "tree_numbers": [
            "G07.203.100",
            "J02.200"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001628",
      "preferred_label": "Beverages",
      "type": "descriptor",
      "location": "vocabulary:45",
      "term": {
        "text": "\"Beverages\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"Curriculum\"[MeSH Terms] OR \"Child Nutrition Sciences\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"nutrition intervention\"[Title/Abstract] OR \"nutrition interventions\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"nutrition educat*\"[Title/Abstract] OR \"dietary educat*\"[Title/Abstract] OR \"food educat*\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"nutrition programme*\"[Title/Abstract] OR \"food program*\"[Title/Abstract] OR \"food programme*\"[Title/Abstract] OR \"nutrition promot*\"[Title/Abstract] OR \"healthy eating program*\"[Title/Abstract] OR \"healthy eating intervention*\"[Title/Abstract] OR \"dietary intervention*\"[Title/Abstract] OR \"nutrition curriculum*\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"nutrition training\"[Title/Abstract] OR \"intervention*\"[Title/Abstract] OR \"education*\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"School Health Services\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"high school*\"[Title/Abstract] OR \"middle school*\"[Title/Abstract] OR \"secondary school*\"[Title/Abstract] OR \"primary school*\"[Title/Abstract] OR \"school age*\"[Title/Abstract]) AND (\"Feeding Behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms] OR \"Fruit\"[MeSH Terms] OR \"Vegetables\"[MeSH Terms] OR \"Beverages\"[MeSH Terms] OR \"food consumption\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"dietary intake\"[Title/Abstract] OR \"dietary behavior\"[Title/Abstract] OR \"dietary behaviour\"[Title/Abstract] OR \"eating behavior\"[Title/Abstract] OR \"eating behaviour\"[Title/Abstract] OR \"eating habit\"[Title/Abstract] OR \"dietary habit\"[Title/Abstract] OR \"food habit\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"consum*\"[Title/Abstract] OR \"intake\"[Title/Abstract] OR \"food choice\"[Title/Abstract] OR \"fruit and vegetable intake\"[Title/Abstract] OR \"fruit and vegetable consumption\"[Title/Abstract] OR \"beverage consumption\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "b3e94228eb6a60ef0f9f2f1410b982891ce1cf9852faceefadb965414ea19650",
      "note": "same-context critic; no fresh-context reviewer was available",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Intervention, school delivery, and eligible food-consumption outcomes are represented as separate OR blocks and ANDed; population is left to screening after an optional test. This follows the eligibility concepts and avoids an age/student restriction that had only a 12% measured reduction."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within concepts and AND combines the three selected concepts. No NOT or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected exploded MeSH headings cover health education/promotion, curriculum, nutrition, diet, school delivery, feeding behavior, food preferences, produce, and beverages. MeSH is paired with title/abstract terms; no :noexp restriction is applied."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include nutrition/food/diet education and intervention terms, school-setting variants, and food/diet/intake/consumption language, with spelling variants for behavior/behaviour and program/programme. Broad intervention, education, diet, and consum truncations are intentionally retained for recall and contribute noise."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current query is parenthesized, field-tagged, has no remaining translation warnings, and the packet reports no PubMed query diagnostics or syntax findings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or study-design filter is applied. The effective Entrez entry-date bound is 2017-12-14 as requested; no [dp] limit is used."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count remains above the 10,000-record workload budget. Every searchable concept otherwise left for screening was tested as an optional block: school delivery and food-consumption outcome were ANDed after material reductions and zero eligible records in their screened 30-record loss samples; adolescent/student population was left out because it reduced the current base by only 12.0%, below the approximate 30% materiality criterion. Screening population and the remaining 16,197 records is the documented workload risk.",
          "evidence": "Current evaluation version 5 reports 16,197 records; 8/8 benchmark and 9/9 development-relevant records retrieved; no known losses. Optional tests report setting 427,941 to 16,197 (96.2% reduction), outcome 123,578 to 16,197 (86.9%), and population 16,197 to 14,254 (12.0%), with 0/30 eligible records in each recorded loss sample. All three optional concepts have current decisions."
        }
      ]
    }
  ]
}
```


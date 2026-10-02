# PubMed search strategy: audit

Generated 2026-10-02T14:23:46+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO (intervention effectiveness/search; outcome screened)
- Scope confirmed by user: no (User asked to proceed without questions; these are operational scope assumptions, not user confirmation. No known relevant articles were supplied. PubMed is bounded by Entrez entry date 2017-12-14 via PSB_AS_OF, as the user and harness require; this is not a publication-date limit. MeSH lookup/show found no Nutrition Education heading; a direct Nutrition Education[Mesh] check fell back to All Fields and is unusable.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Education activity | search | Educational activity is a required, searchable facet of the intervention; separated from nutrition content so each facet has its own vocabulary. |
| Food or nutrition content | search | Food/nutrition content is a required, searchable facet of the intervention; separated from education activity so each facet has its own vocabulary. |
| Adolescents or school students | search | The stated population is a required, searchable concept; broad student terms preserve school-age papers whose abstracts omit adolescent labels. |
| Delivered through a school | screen | Delivery setting can be inconsistently described in abstracts and is safer to assess during screening. |
| Eligible food-consumption outcome | screen | Outcomes are inconsistently reported and indexed; screen for eligible consumption outcomes. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:22:39+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 36,367
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 3 | `"Teaching"[Mesh]` | 79,753 | none |
| 4 | `educat*[tiab]` | 513,190 | none |
| 5 | `intervention*[tiab]` | 788,474 | none |
| 6 | `teach*[tiab]` | 165,464 | none |
| 7 | `instruct*[tiab]` | 80,423 | none |
| 8 | `lesson*[tiab]` | 50,204 | none |
| 9 | `curricul*[tiab]` | 46,216 | none |
| 10 | `learn*[tiab]` | 319,328 | none |
| 11 | `program*[tiab]` | 750,384 | none |
| 12 | `"nutrition education"[tiab]` | 3,866 | none |
| 13 | `"food education"[tiab]` | 84 | none |
| 14 | `"dietary education"[tiab]` | 252 | none |
| 15 | `"nutrition instruction"[tiab]` | 46 | none |
| 16 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 2,285,266 | none |
| 17 | `"Child Nutrition Sciences"[Mesh]` | 1,076 | none |
| 18 | `"Child Nutritional Physiological Phenomena"[Mesh]` | 62,309 | none |
| 19 | `"Adolescent Nutritional Physiological Phenomena"[Mesh]` | 1,486 | none |
| 20 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 21 | `"Diet"[Mesh]` | 254,824 | none |
| 22 | `"Food Preferences"[Mesh]` | 13,063 | none |
| 23 | `"Fruit"[Mesh]` | 91,855 | none |
| 24 | `"Vegetables"[Mesh]` | 28,363 | none |
| 25 | `nutrition*[tiab]` | 244,227 | none |
| 26 | `food*[tiab]` | 387,680 | none |
| 27 | `diet*[tiab]` | 494,942 | none |
| 28 | `fruit*[tiab]` | 87,538 | none |
| 29 | `vegetable*[tiab]` | 46,125 | none |
| 30 | `eating[tiab]` | 61,958 | none |
| 31 | `"healthy eating"[tiab]` | 5,052 | none |
| 32 | `#17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31` | 1,243,641 | none |
| 33 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 34 | `"Students"[Mesh]` | 112,971 | none |
| 35 | `"Child"[Mesh] AND (school*[tiab] OR classroom*[tiab] OR grade*[tiab] OR student*[tiab] OR pupil*[tiab])` | 141,054 | none |
| 36 | `adolescen*[tiab]` | 248,945 | none |
| 37 | `teen*[tiab]` | 26,895 | none |
| 38 | `youth*[tiab]` | 64,596 | none |
| 39 | `student*[tiab]` | 234,078 | none |
| 40 | `schoolchild*[tiab]` | 13,052 | none |
| 41 | `school child*[tiab]` | 21,096 | none |
| 42 | `pupil*[tiab]` | 26,074 | none |
| 43 | `schoolgirl*[tiab]` | 785 | none |
| 44 | `schoolboy*[tiab]` | 469 | none |
| 45 | `secondary school*[tiab]` | 8,822 | none |
| 46 | `high school*[tiab]` | 27,028 | none |
| 47 | `middle school*[tiab]` | 4,703 | none |
| 48 | `junior high[tiab]` | 2,267 | none |
| 49 | `#33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48` | 2,237,865 | none |
| 50 | `#16 AND #32 AND #49` | 36,367 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR "Teaching"[Mesh] OR educat*[tiab] OR intervention*[tiab] OR teach*[tiab] OR instruct*[tiab] OR lesson*[tiab] OR curricul*[tiab] OR learn*[tiab] OR program*[tiab] OR "nutrition education"[tiab] OR "food education"[tiab] OR "dietary education"[tiab] OR "nutrition instruction"[tiab]) AND ("Child Nutrition Sciences"[Mesh] OR "Child Nutritional Physiological Phenomena"[Mesh] OR "Adolescent Nutritional Physiological Phenomena"[Mesh] OR "Feeding Behavior"[Mesh] OR "Diet"[Mesh] OR "Food Preferences"[Mesh] OR "Fruit"[Mesh] OR "Vegetables"[Mesh] OR nutrition*[tiab] OR food*[tiab] OR diet*[tiab] OR fruit*[tiab] OR vegetable*[tiab] OR eating[tiab] OR "healthy eating"[tiab]) AND ("Adolescent"[Mesh] OR "Students"[Mesh] OR ("Child"[Mesh] AND (school*[tiab] OR classroom*[tiab] OR grade*[tiab] OR student*[tiab] OR pupil*[tiab])) OR adolescen*[tiab] OR teen*[tiab] OR youth*[tiab] OR student*[tiab] OR schoolchild*[tiab] OR school child*[tiab] OR pupil*[tiab] OR schoolgirl*[tiab] OR schoolboy*[tiab] OR secondary school*[tiab] OR high school*[tiab] OR middle school*[tiab] OR junior high[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 114,153 | 0 |
| nutrition_content | 434,165 | 0 |
| population | 176,018 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 73,441 | initial | none | Initial high-sensitivity draft from question-defined intervention and population blocks; school delivery and food-consumption outcomes screened because they are inconsistently named/indexed. No supplied seeds. |
| 2 | 26,546 | education: +8 / -3 | none | Revised intervention block: constrained Health Education MeSH to nutrition/food behavior headings and added screened-record wording for feeding behavior and fruit/vegetable teaching programs; retained outcome as a screen criterion. |
| 3 | 36,718 | education: +10 / -14; nutrition_content: +13 / -0 | none | Split the defining intervention into separate required education-activity and nutrition-content blocks after lint flagged compound terms; removed two uncertain candidates whose abstracts did not clearly establish an education component. |
| 4 | 37,059 | nutrition_content: +2 / -0 | none | Added the screened Kahnawake Schools Diabetes Prevention Project study to the relevant development set and added its common child-nutrition MeSH heading, with the adolescent-nutrition heading as a related age-group term. |
| 5 | 28,715 | population: +1 / -1 | none | Restricted Child MeSH to school/student context within the population block; Child alone included many records outside the stated adolescent or school-student population. School setting remains a screening criterion. |
| 6 | 36,367 | education: +1 / -0 | none | Added intervention*[tiab] to address the internal critic's omitted bare intervention wording. Checked the requested Nutrition Education heading in MeSH; no authority record was found, and PubMed did not recognize the unsupported field-tagged heading. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 3 findings; R1-1 must-fix open, R1-2 should-fix open, R1-3 should-fix open
- Round 2 on version 6: 3 findings; R1-1 must-fix resolved, R1-2 should-fix rejected, R1-3 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 879 NCBI requests logged (467 from cache); strategy sha256 2a7fec081510._

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
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "requested": "Teaching",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
          "ui": "D013663",
          "name": "Teaching",
          "type": "descriptor",
          "scope_note": "A formal and organized process of transmitting knowledge to a person or group.",
          "tree_numbers": [
            "I02.903"
          ],
          "entry_terms": 28,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013663",
      "preferred_label": "Teaching",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Teaching\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Child Nutrition Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child Nutritional Physiological Phenomena",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002664",
          "name": "Child Nutritional Physiological Phenomena",
          "type": "descriptor",
          "scope_note": "Nutritional physiology of children aged 2-12 years.",
          "tree_numbers": [
            "G07.203.650.220"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002664",
      "preferred_label": "Child Nutritional Physiological Phenomena",
      "type": "descriptor",
      "location": "vocabulary:17",
      "term": {
        "text": "\"Child Nutritional Physiological Phenomena\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent Nutritional Physiological Phenomena",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017195",
          "name": "Adolescent Nutritional Physiological Phenomena",
          "type": "descriptor",
          "scope_note": "Nutritional physiology of children aged 13-18 years.",
          "tree_numbers": [
            "G07.203.650.220.060"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017195",
      "preferred_label": "Adolescent Nutritional Physiological Phenomena",
      "type": "descriptor",
      "location": "vocabulary:18",
      "term": {
        "text": "\"Adolescent Nutritional Physiological Phenomena\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fruit",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Fruit\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Vegetables",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Vegetables\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:22:39+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"Teaching\"[MeSH Terms] OR \"educat*\"[Title/Abstract] OR \"intervention*\"[Title/Abstract] OR \"teach*\"[Title/Abstract] OR \"instruct*\"[Title/Abstract] OR \"lesson*\"[Title/Abstract] OR \"curricul*\"[Title/Abstract] OR \"learn*\"[Title/Abstract] OR \"program*\"[Title/Abstract] OR \"nutrition education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract]) AND (\"Child Nutrition Sciences\"[MeSH Terms] OR \"Child Nutritional Physiological Phenomena\"[MeSH Terms] OR \"Adolescent Nutritional Physiological Phenomena\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms] OR \"Fruit\"[MeSH Terms] OR \"Vegetables\"[MeSH Terms] OR \"nutrition*\"[Title/Abstract] OR \"food*\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"fruit*\"[Title/Abstract] OR \"vegetable*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"healthy eating\"[Title/Abstract]) AND (\"Adolescent\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR (\"Child\"[MeSH Terms] AND (\"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"grade*\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract])) OR \"adolescen*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth*\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"school child*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"schoolgirl*\"[Title/Abstract] OR \"schoolboy*\"[Title/Abstract] OR \"secondary school*\"[Title/Abstract] OR \"high school*\"[Title/Abstract] OR \"middle school*\"[Title/Abstract] OR \"junior high\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "6c020e9bb1ba47df6adf024267aad6e3de75399696daf20e45b3ef6f843a8d19",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searchable intervention facet omits intervention/interventions as a bare text word although the question and eligibility explicitly name an intervention; the education block currently depends on education/activity synonyms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three required searchable facets are combined with AND and synonyms within each facet with OR. The child MeSH term is appropriately combined with school-context words, and parentheses are clear."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The strategy uses broad health education and health promotion headings but omits the directly relevant Nutrition Education heading. Verify its current MeSH form and test it in the education block."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add the bare intervention stem to represent an explicit eligibility term. Existing broad education words and three seed records do not establish that this omission is harmless."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors, warnings, or translation issues for the tested query; the translated Boolean structure is coherent."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The Entrez date limit ends at 2017-12-14 although the stated question and eligibility have no temporal restriction. The packet documents this as an operational snapshot, but scope is unconfirmed; explicitly retain it only if a historical cutoff is intended, otherwise remove it and rerun the evaluation."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The question and eligibility explicitly describe an intervention, but no bare intervention text word is searched in the education activity block. The block contains education, teaching, learning, lesson, curriculum, and program terms, but none necessarily matches records that describe an intervention without those words.",
          "recommendation": "Add intervention*[tiab] to the education activity block, test it, and rerun the complete evaluation, including the combined strategy and known-record checks.",
          "status": "open",
          "response": null
        },
        {
          "id": "R1-2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The education facet uses broad headings such as Health Education and Health Promotion but does not include the directly relevant Nutrition Education controlled heading. Phrase searching for nutrition education does not substitute for a controlled heading on indexed records whose abstracts may omit that phrase.",
          "recommendation": "Verify the applicable PubMed MeSH heading for Nutrition Education, add it if available and appropriate, and test the revised block and full strategy.",
          "status": "open",
          "response": null
        },
        {
          "id": "R1-3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The combined query imposes an Entrez date-of-entry upper bound of 2017-12-14, while the question and eligibility state no time restriction. The packet says this is an operational snapshot and scope remains unconfirmed, so the cutoff could exclude otherwise eligible records entered later.",
          "recommendation": "Confirm and document that a historical 2017 snapshot is the intended scope. If the review is intended to cover all dates, remove the EDAT cutoff and rerun all query and validation checks.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "72897ccb5b57fa9eebd6de5f78b73513eec722e27339d4f8763effb6ee0e09e2",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required searchable facets are represented with their bare terms, including intervention*[tiab], nutrition*[tiab], food*[tiab], adolescen*[tiab], and student*[tiab]. School delivery and consumption outcome are intentionally screened. No translation issues or PubMed warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within education, nutrition-content, and population blocks; the three required searchable blocks are ANDed. The child heading is qualified with school-context terms, and parentheses are coherent."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses verified relevant MeSH headings. The packet reports that no Nutrition Education heading was found and that a direct PubMed check fell back to All Fields, so that unavailable heading cannot be added as a valid controlled term."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The previously missing bare intervention stem is now present in the education block. Broad food, nutrition, diet, eating, and population wording supports recall; all three development records are retrieved, though that small set is not independent validation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The tested lines and combined query report no errors, warnings, or translation issues; PubMed's translated Boolean structure is coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population or study-design filter is applied. The EDAT upper bound is explicitly required by the packet's as-of instruction and is documented as an entry-date snapshot, not a publication-date eligibility limit; findings therefore cover records entered by 2017-12-14 only."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The question and eligibility explicitly describe an intervention, but no bare intervention text word is searched in the education activity block. The block contains education, teaching, learning, lesson, curriculum, and program terms, but none necessarily matches records that describe an intervention without those words.",
          "recommendation": "Add intervention*[tiab] to the education activity block, test it, and rerun the complete evaluation, including the combined strategy and known-record checks.",
          "status": "resolved",
          "response": "Version 6 includes intervention*[tiab] in the education block. The complete evaluation was rerun; the strategy retrieves all three known development records and reports no evaluation or translation issues."
        },
        {
          "id": "R1-2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The education facet uses broad headings such as Health Education and Health Promotion but does not include the directly relevant Nutrition Education controlled heading. Phrase searching for nutrition education does not substitute for a controlled heading on indexed records whose abstracts may omit that phrase.",
          "recommendation": "Verify the applicable PubMed MeSH heading for Nutrition Education, add it if available and appropriate, and test the revised block and full strategy.",
          "status": "rejected",
          "response": "The packet records that MeSH lookup/show found no Nutrition Education heading and that a direct Nutrition Education[Mesh] check fell back to All Fields and is unusable. There is no verified controlled heading to add; the text phrase remains in the strategy."
        },
        {
          "id": "R1-3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The combined query imposes an Entrez date-of-entry upper bound of 2017-12-14, while the question and eligibility state no time restriction. The packet says this is an operational snapshot and scope remains unconfirmed, so the cutoff could exclude otherwise eligible records entered later.",
          "recommendation": "Confirm and document that a historical 2017 snapshot is the intended scope. If the review is intended to cover all dates, remove the EDAT cutoff and rerun all query and validation checks.",
          "status": "accepted-risk",
          "response": "The packet explicitly requires the 2017-12-14 as-of bound as an operational snapshot and clarifies that it is an Entrez entry-date cutoff, not publication-date eligibility. It remains a scope limitation: records entered after that date are outside this run; the protocol's scope is still marked unconfirmed."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


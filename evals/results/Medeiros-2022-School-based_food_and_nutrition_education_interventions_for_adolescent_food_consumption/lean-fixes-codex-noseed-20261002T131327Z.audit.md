# PubMed search strategy: audit

Generated 2026-10-02T13:41:24+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User requested no follow-up questions and authorized reasonable assumptions. Search concepts are adolescents/school students, food/nutrition content, education/intervention activity, and school delivery; food-consumption outcome remains a screening criterion. User supplied no known relevant articles. Harness date bound is Entrez date 2017-12-14 via PSB_AS_OF on every command; no publication-date limit. The original compound intervention block was separated into nutrition-content and education-activity blocks to give each idea its own complete vocabulary layer. School delivery was moved into the strategy because it defines the review topic and is searchable as Schools or school/classroom wording; this assumption remains for human PRESS review.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Adolescents or school students | search | The eligible population is adolescents or school-age students. Child and adolescent headings plus school-age wording are searched without an age filter; the generic Students heading/word was omitted because it also retrieves university students, while school delivery has its own block. |
| Food or nutrition content | search | Every eligible intervention concerns food or nutrition; this orthogonal content block is separated from the educational activity to permit complete vocabulary for each idea. |
| Education or intervention activity | search | Every eligible record involves an educational intervention; terms include education, teaching, curriculum, and broader intervention/program descriptions because abstracts do not consistently label pedagogy. |
| Delivered through a school | search | School delivery is explicit and central to the question. Schools indexing and school/classroom wording make it searchable; delivery is still verified at screening. |
| Eligible food-consumption outcome | screen | Consumption outcomes are variably reported and should not be required in the search. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:39:42+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 12,411
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 2 | `"Child"[Mesh]` | 1,797,170 | none |
| 3 | `adolescen*[tiab]` | 248,945 | none |
| 4 | `teen*[tiab]` | 26,895 | none |
| 5 | `youth*[tiab]` | 64,596 | none |
| 6 | `child*[tiab]` | 1,257,861 | none |
| 7 | `schoolchild*[tiab]` | 13,052 | none |
| 8 | `"school children"[tiab]` | 20,666 | none |
| 9 | `"school students"[tiab]` | 14,140 | none |
| 10 | `"school-age"[tiab]` | 11,579 | none |
| 11 | `"school age"[tiab]` | 11,579 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 3,198,981 | none |
| 13 | `"Diet"[Mesh]` | 254,824 | none |
| 14 | `"Food"[Mesh]` | 557,708 | none |
| 15 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 16 | `"Food Preferences"[Mesh]` | 13,063 | none |
| 17 | `"Fruit"[Mesh]` | 91,855 | none |
| 18 | `"Vegetables"[Mesh]` | 28,363 | none |
| 19 | `nutrition*[tiab]` | 244,227 | none |
| 20 | `diet*[tiab]` | 494,942 | none |
| 21 | `food*[tiab]` | 387,680 | none |
| 22 | `eating[tiab]` | 61,958 | none |
| 23 | `fruit*[tiab]` | 87,538 | none |
| 24 | `vegetable*[tiab]` | 46,125 | none |
| 25 | `meal*[tiab]` | 63,467 | none |
| 26 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 1,478,162 | none |
| 27 | `"Health Education"[Mesh]` | 221,709 | none |
| 28 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 29 | `educat*[tiab]` | 513,190 | none |
| 30 | `teach*[tiab]` | 165,464 | none |
| 31 | `curricul*[tiab]` | 46,216 | none |
| 32 | `lesson*[tiab]` | 50,204 | none |
| 33 | `instruction*[tiab]` | 53,676 | none |
| 34 | `training[tiab]` | 332,315 | none |
| 35 | `pedagog*[tiab]` | 6,574 | none |
| 36 | `program*[tiab]` | 750,384 | none |
| 37 | `intervention*[tiab]` | 788,474 | none |
| 38 | `promot*[tiab]` | 823,253 | none |
| 39 | `"food literacy"[tiab]` | 34 | none |
| 40 | `"food skills"[tiab:~2]` | 152 | none |
| 41 | `#27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40` | 2,908,296 | none |
| 42 | `"Schools"[Mesh]` | 107,820 | none |
| 43 | `school*[tiab]` | 246,627 | none |
| 44 | `classroom*[tiab]` | 14,159 | none |
| 45 | `#42 OR #43 OR #44` | 311,646 | none |
| 46 | `#12 AND #26 AND #41 AND #45` | 12,411 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Adolescent"[Mesh] OR "Child"[Mesh] OR adolescen*[tiab] OR teen*[tiab] OR youth*[tiab] OR child*[tiab] OR schoolchild*[tiab] OR "school children"[tiab] OR "school students"[tiab] OR "school-age"[tiab] OR "school age"[tiab]) AND ("Diet"[Mesh] OR "Food"[Mesh] OR "Feeding Behavior"[Mesh] OR "Food Preferences"[Mesh] OR "Fruit"[Mesh] OR "Vegetables"[Mesh] OR nutrition*[tiab] OR diet*[tiab] OR food*[tiab] OR eating[tiab] OR fruit*[tiab] OR vegetable*[tiab] OR meal*[tiab]) AND ("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR educat*[tiab] OR teach*[tiab] OR curricul*[tiab] OR lesson*[tiab] OR instruction*[tiab] OR training[tiab] OR pedagog*[tiab] OR program*[tiab] OR intervention*[tiab] OR promot*[tiab] OR "food literacy"[tiab] OR "food skills"[tiab:~2]) AND ("Schools"[Mesh] OR school*[tiab] OR classroom*[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| population | 15,763 | 0 |
| nutrition_content | 83,564 | 0 |
| education_activity | 21,877 | 0 |
| school_delivery | 59,956 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 122,625 | initial | none | Initial two-block high-sensitivity strategy; kept school delivery and consumption outcome for screening and added MeSH plus broad population and nutrition-education vocabulary. |
| 2 | 63,175 | education: +0 / -15; nutrition_content: +13 / -0; education_activity: +14 / -0 | none | Revised the compound education topic into separate population, nutrition-content, and education/activity blocks; added explicit content and pedagogy vocabularies to control the broad Health Education-only retrieval while preserving screening for school delivery and consumption. |
| 3 | 13,459 | school_delivery: +3 / -0 | none | Added school delivery as a required search block because school-based defines the question and preliminary PubMed counting suggested the unscreened search was too broad; tested School MeSH and school/classroom text terms. Outcome remains screened. |
| 4 | 12,411 | population: +0 / -2 | none | Removed generic Students heading and student* title/abstract term after random sample surfaced university-student records; adolescents, children, and explicit school-age terms remain, and school delivery has a dedicated block. No age limit added. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; F1 should-fix rejected
- Round 2 on version 4: 1 findings; F1 should-fix rejected
- Round 3 on version 4: 1 findings; F1 should-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 866 NCBI requests logged (435 from cache); strategy sha256 cabf47a6437f._

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
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005502",
          "name": "Food",
          "type": "descriptor",
          "scope_note": "Substances taken in by the body to provide nourishment.",
          "tree_numbers": [
            "G07.203.300",
            "J02.500"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005502",
      "preferred_label": "Food",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"Food\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fruit",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Fruit\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Vegetables",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "\"Vegetables\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Health Education\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Promotion",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Health Promotion\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:39:42+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Adolescent\"[MeSH Terms] OR \"Child\"[MeSH Terms] OR \"adolescen*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth*\"[Title/Abstract] OR \"child*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"school children\"[Title/Abstract] OR \"school students\"[Title/Abstract] OR \"school-age\"[Title/Abstract] OR \"school-age\"[Title/Abstract]) AND (\"Diet\"[MeSH Terms] OR \"Food\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms] OR \"Fruit\"[MeSH Terms] OR \"Vegetables\"[MeSH Terms] OR \"nutrition*\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"food*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"fruit*\"[Title/Abstract] OR \"vegetable*\"[Title/Abstract] OR \"meal*\"[Title/Abstract]) AND (\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"educat*\"[Title/Abstract] OR \"teach*\"[Title/Abstract] OR \"curricul*\"[Title/Abstract] OR \"lesson*\"[Title/Abstract] OR \"instruction*\"[Title/Abstract] OR \"training\"[Title/Abstract] OR \"pedagog*\"[Title/Abstract] OR \"program*\"[Title/Abstract] OR \"intervention*\"[Title/Abstract] OR \"promot*\"[Title/Abstract] OR \"food literacy\"[Title/Abstract] OR \"food skills\"[Title/Abstract:~2]) AND (\"Schools\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "6bcab1787451a10f9e956c1832794ca5a07912cb1dbd7c205b1ac86e38222563",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Each searched concept has its own block, and consumption remains a screening outcome."
        },
        "operators": {
          "verdict": "pass",
          "note": "The four blocks are ANDed and terms within each are ORed."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The proposed Nutrition Education heading was checked against the NCBI MeSH lookup and PubMed translation; it is not a valid directly searchable MeSH descriptor in this context."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Population, food/nutrition, education/activity, and school vocabulary are represented in title/abstract terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The evaluated query had no syntax, translation, or phrase-index issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No protocol limits or study-design filters are applied; the effective date bound is Entrez-date based."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The education activity block lacks the directly relevant Nutrition Education MeSH heading.",
          "recommendation": "Add \"Nutrition Education\"[Mesh] to the education_activity block, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "Rejected because the proposed heading is not verified in NCBI MeSH. `psb mesh lookup Nutrition Education` returned no matches. A live PubMed count for `\"Nutrition Education\"[Mesh]` translated it as nutrition terms AND education terms, emitted an all_fields_fallback warning, and did not validate a MeSH descriptor. Adding it would introduce a field-translation defect. The verified Health Education and Health Promotion descriptors plus food/nutrition content terms supply the controlled-vocabulary layer."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "6bcab1787451a10f9e956c1832794ca5a07912cb1dbd7c205b1ac86e38222563",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Four required concepts have separate blocks; consumption outcome remains screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms within each concept are ORed and the four required concepts are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Included headings are verified, and the prior Nutrition Education recommendation was rejected with evidence."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover population, food/nutrition content, education/activity, and school delivery."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No current translation, syntax, or phrase-index issues are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No protocol limits or design filters are applied; the Entrez cutoff is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The education activity block lacks the directly relevant Nutrition Education MeSH heading.",
          "recommendation": "Add \"Nutrition Education\"[Mesh] to the education_activity block, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "Rejected because the proposed heading is not verified in NCBI MeSH. `psb mesh lookup Nutrition Education` returned no matches. A live PubMed count for `\"Nutrition Education\"[Mesh]` translated it as nutrition terms AND education terms, emitted an all_fields_fallback warning, and did not validate a MeSH descriptor. Adding it would introduce a field-translation defect. The verified Health Education and Health Promotion descriptors plus food/nutrition content terms supply the controlled-vocabulary layer."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "6bcab1787451a10f9e956c1832794ca5a07912cb1dbd7c205b1ac86e38222563",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The four required searchable concepts have separate blocks, and food-consumption outcomes remain a screening criterion."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms within each concept are ORed, and the four required concepts are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Included headings are verified. Earlier finding F1 was rejected with evidence that Nutrition Education is not a verified directly searchable MeSH descriptor in this context."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms represent population, food/nutrition content, education/intervention activity, and school delivery."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no syntax, translation, or phrase-index issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No protocol limits or study-design filters are applied; the Entrez date bound is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The education activity block lacks the directly relevant Nutrition Education MeSH heading.",
          "recommendation": "Add \"Nutrition Education\"[Mesh] to the education_activity block, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "Rejected because the proposed heading is not verified in NCBI MeSH. `psb mesh lookup Nutrition Education` returned no matches. A live PubMed count for `\"Nutrition Education\"[Mesh]` translated it as nutrition terms AND education terms, emitted an all_fields_fallback warning, and did not validate a MeSH descriptor. Adding it would introduce a field-translation defect. The verified Health Education and Health Promotion descriptors plus food/nutrition content terms supply the controlled-vocabulary layer."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


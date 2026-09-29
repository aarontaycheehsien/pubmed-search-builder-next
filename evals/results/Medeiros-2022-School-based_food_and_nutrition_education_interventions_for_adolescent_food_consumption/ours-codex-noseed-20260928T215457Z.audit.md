# PubMed search strategy: audit

Generated 2026-09-28T22:28:47+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: yes (User asked to proceed without further questions; roles are provisional assumptions for the required no-pause run. No known relevant articles supplied. PubMed availability is bounded by Entrez date 2017-12-14 via PSB_AS_OF; no publication-date limit is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food and nutrition education intervention | search | The intervention defines the review; education terms and indexing can retrieve it, while member-only intervention descriptions need probing. |
| Adolescents and school students | search | The review is limited to adolescent/student participants; age and student language and indexing are searchable, with member-only wording tested by probing. |
| School delivery setting | optional | School delivery is central and often named, but may be implicit or described only in full text; test its effect and loss sample. |
| Eligible food-consumption outcome | optional | Food consumption defines the topic, but outcomes may be inconsistently named; test a broad outcome block and screen its loss sample. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:27:11+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 5,861
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 3 | `"Counseling"[Mesh]` | 41,059 | none |
| 4 | `"nutrition education"[tiab]` | 3,866 | none |
| 5 | `"food education"[tiab]` | 84 | none |
| 6 | `"nutrition instruction"[tiab]` | 46 | none |
| 7 | `"nutrition counseling"[tiab]` | 559 | none |
| 8 | `"nutrition counselling"[tiab]` | 148 | none |
| 9 | `"nutrition program"[tiab]` | 1,227 | none |
| 10 | `"nutrition programs"[tiab]` | 970 | none |
| 11 | `"nutrition intervention"[tiab]` | 1,150 | none |
| 12 | `"nutrition interventions"[tiab]` | 873 | none |
| 13 | `"dietary education"[tiab]` | 252 | none |
| 14 | `"food and nutrition"[tiab:~2]` | 3,485 | none |
| 15 | `"nutrition behavior"[tiab]` | 143 | none |
| 16 | `"nutrition behaviour"[tiab]` | 64 | none |
| 17 | `counsel*[tiab]` | 91,341 | none |
| 18 | `nutritional[tiab]` | 119,911 | none |
| 19 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18` | 440,737 | none |
| 20 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 21 | `"Child"[Mesh]` | 1,797,170 | none |
| 22 | `"Students"[Mesh]` | 112,971 | none |
| 23 | `adolescent*[tiab]` | 213,221 | none |
| 24 | `teen*[tiab]` | 26,895 | none |
| 25 | `youth[tiab]` | 57,369 | none |
| 26 | `young people[tiab]` | 23,082 | none |
| 27 | `student*[tiab]` | 234,078 | none |
| 28 | `pupil*[tiab]` | 26,074 | none |
| 29 | `schoolchild*[tiab]` | 13,052 | none |
| 30 | `school children[tiab]` | 20,666 | none |
| 31 | `school student*[tiab]` | 14,516 | none |
| 32 | `child*[tiab]` | 1,257,861 | none |
| 33 | `grade*[tiab]` | 350,971 | none |
| 34 | `#20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 3,661,781 | none |
| 35 | `"Schools"[Mesh]` | 107,820 | none |
| 36 | `school*[tiab]` | 246,627 | none |
| 37 | `classroom*[tiab]` | 14,159 | none |
| 38 | `high school*[tiab]` | 27,028 | none |
| 39 | `secondary school*[tiab]` | 8,822 | none |
| 40 | `elementary school*[tiab]` | 8,563 | none |
| 41 | `primary school*[tiab]` | 10,360 | none |
| 42 | `school-based[tiab]` | 10,873 | none |
| 43 | `school based[tiab]` | 10,873 | none |
| 44 | `#35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43` | 311,646 | none |
| 45 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 46 | `"Diet"[Mesh]` | 254,824 | none |
| 47 | `"Eating"[Mesh]` | 68,536 | none |
| 48 | `"Food Preferences"[Mesh]` | 13,063 | none |
| 49 | `diet*[tiab]` | 494,942 | none |
| 50 | `eat[tiab]` | 16,588 | none |
| 51 | `eating[tiab]` | 61,958 | none |
| 52 | `ate[tiab]` | 9,651 | none |
| 53 | `food*[tiab]` | 387,680 | none |
| 54 | `breakfast*[tiab]` | 8,585 | none |
| 55 | `fast food*[tiab]` | 2,758 | none |
| 56 | `sugar*[tiab]` | 108,665 | none |
| 57 | `dietary intake[tiab]` | 20,267 | none |
| 58 | `food intake[tiab]` | 39,819 | none |
| 59 | `food consumption[tiab]` | 11,651 | none |
| 60 | `food eating[tiab]` | 145 | none |
| 61 | `eating behavior[tiab]` | 3,945 | none |
| 62 | `eating behaviour[tiab]` | 1,553 | none |
| 63 | `feeding behavior[tiab]` | 6,137 | none |
| 64 | `feeding behaviour[tiab]` | 2,023 | none |
| 65 | `food choice*[tiab]` | 3,666 | none |
| 66 | `dietary habit*[tiab]` | 7,763 | none |
| 67 | `fruit*[tiab]` | 87,538 | none |
| 68 | `vegetable*[tiab]` | 46,125 | none |
| 69 | `beverage*[tiab]` | 21,544 | none |
| 70 | `sugar-sweetened beverage*[tiab]` | 1,699 | none |
| 71 | `sugar sweetened beverage*[tiab]` | 1,699 | none |
| 72 | `diet quality[tiab]` | 2,540 | none |
| 73 | `#45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72` | 1,178,958 | none |
| 74 | `#19 AND #34 AND #44 AND #73` | 5,861 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR "Counseling"[Mesh] OR "nutrition education"[tiab] OR "food education"[tiab] OR "nutrition instruction"[tiab] OR "nutrition counseling"[tiab] OR "nutrition counselling"[tiab] OR "nutrition program"[tiab] OR "nutrition programs"[tiab] OR "nutrition intervention"[tiab] OR "nutrition interventions"[tiab] OR "dietary education"[tiab] OR "food and nutrition"[tiab:~2] OR "nutrition behavior"[tiab] OR "nutrition behaviour"[tiab] OR counsel*[tiab] OR nutritional[tiab]) AND ("Adolescent"[Mesh] OR "Child"[Mesh] OR "Students"[Mesh] OR adolescent*[tiab] OR teen*[tiab] OR youth[tiab] OR young people[tiab] OR student*[tiab] OR pupil*[tiab] OR schoolchild*[tiab] OR school children[tiab] OR school student*[tiab] OR child*[tiab] OR grade*[tiab]) AND ("Schools"[Mesh] OR school*[tiab] OR classroom*[tiab] OR high school*[tiab] OR secondary school*[tiab] OR elementary school*[tiab] OR primary school*[tiab] OR school-based[tiab] OR school based[tiab]) AND ("Feeding Behavior"[Mesh] OR "Diet"[Mesh] OR "Eating"[Mesh] OR "Food Preferences"[Mesh] OR diet*[tiab] OR eat[tiab] OR eating[tiab] OR ate[tiab] OR food*[tiab] OR breakfast*[tiab] OR fast food*[tiab] OR sugar*[tiab] OR dietary intake[tiab] OR food intake[tiab] OR food consumption[tiab] OR food eating[tiab] OR eating behavior[tiab] OR eating behaviour[tiab] OR feeding behavior[tiab] OR feeding behaviour[tiab] OR food choice*[tiab] OR dietary habit*[tiab] OR fruit*[tiab] OR vegetable*[tiab] OR beverage*[tiab] OR sugar-sweetened beverage*[tiab] OR sugar sweetened beverage*[tiab] OR diet quality[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| School delivery setting | AND-ed | 27,772 / 5,861 | 78.9% | none | 0/30 (up to 10% of removed records could be relevant) | School delivery is an explicit eligibility criterion; current optional evaluation shows a material reduction with no known relevant records lost, and none of the refreshed 30-record loss sample met scope. |
| Eligible food-consumption outcome | AND-ed | 24,525 / 5,861 | 76.1% | none | 0/30 (up to 10% of removed records could be relevant) | Food consumption is explicit eligibility; the outcome block materiality is 76.1% in current evaluation with no known relevant records lost, and none of the refreshed 30-record loss sample met scope. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food and nutrition education intervention | 1 | `(intervention*[tiab] OR program*[tiab] OR lesson*[tiab] OR curriculum[tiab] OR teach*[tiab] OR train*[tiab])` | 4,989 | 1/30 |
| Food and nutrition education intervention | 2 | `(intervention*[tiab] OR program*[tiab] OR lesson*[tiab] OR curriculum[tiab] OR teach*[tiab] OR train*[tiab])` | 4,376 | 0/30 |
| Adolescents and school students | 1 | `(child*[tiab] OR girl*[tiab] OR boy*[tiab] OR grade*[tiab] OR class*[tiab])` | 291 | 0/30 |
| Adolescents and school students | 2 | `(child*[tiab] OR girl*[tiab] OR boy*[tiab] OR grade*[tiab] OR class*[tiab])` | 393 | 2/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 19,467 | 0 |
| population | 6,526 | 0 |
| school | 27,772 | 0 |
| consumption | 24,525 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 63,158 | initial | none | Initial broad two-block draft with school setting and consumption outcome kept as candidates for mandatory testing; terms use screened relevant records plus MeSH and title/abstract synonyms. |
| 2 | 89,241 | education: +2 / -0 | none | Added Counseling MeSH and counseling/counselling terms after terms miss showed a known school nurse intervention with diet outcomes failed the intervention block; no eligibility change. |
| 3 | 20,442 | school: +9 / -0 | none | Broadened the optional food-consumption block with diet/eating/food and reported-food indicators after it missed a known school nurse counseling study; preserved required high recall. |
| 4 | 0 | consumption: +26 / -0 | none | Promoted the broad food-consumption outcome block after its 30-record loss sample contained no in-scope records and it retrieved all known relevant records. |
| 5 | 3,931 | consumption: +28 / -0 | none | Replaced invalid short truncation eat* with explicit forms eat, eating, and ate after lint identified PubMed's four-character wildcard rule. |
| 6 | 3,985 | education: +1 / -0 | none | Added the screened education-probe record's wording, nutritional education, to recover an otherwise missed eligible school program; no eligibility changes. |
| 7 | 5,554 | education: +1 / -1 | none | terms miss and PubMed tests showed the exact nutritional education phrase missed the record because its abstract separates the words; replaced the ineffective phrase with field-tagged nutritional to retrieve it. |
| 8 | 5,861 | population: +2 / -0 | none | Widened population block with child* and grade* after the category probe surfaced likely eligible classroom nutrition-education studies described by age/grade rather than adolescent/student wording; added both to development, one abstract unavailable. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 8 (Same-context PRESS-structured critic: no fresh-context reviewer was available in this run. Reviewed the packet across the six specified domains and checked PubMed translations and diagnostics.): 0 findings; 
- Round 2 on version 8 (Same-context second PRESS-structured review round. No fresh-context reviewer was available. The diagnostic report revalidated the final strategy live with zero technical blockers; no strategy changes are planned.): 0 findings; 
- Round 3 on version 8 (Same-context closing review. No fresh-context information specialist was available. The final live diagnostic found no technical blockers; the two revision rounds carried the documented category risks forward as accepted risks.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1744 NCBI requests logged (968 from cache); strategy sha256 bb51b9b247c3._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:education",
        "blocking": false,
        "requires_review": true,
        "id": "I-dbf95b02a2f5650da634"
      },
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:population",
        "pmids": [
          "15415210",
          "27382638"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-d1cede3eac8fca350d4c"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:education",
        "blocking": false,
        "requires_review": true,
        "id": "I-dbf95b02a2f5650da634"
      },
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:population",
        "pmids": [
          "15415210",
          "27382638"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-d1cede3eac8fca350d4c"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "requested": "Counseling",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003376",
          "name": "Counseling",
          "type": "descriptor",
          "scope_note": "The giving of advice and assistance to individuals with educational or personal problems.",
          "tree_numbers": [
            "F02.784.176",
            "F04.408.413",
            "N02.421.143.303",
            "N02.421.461.363"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003376",
      "preferred_label": "Counseling",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Counseling\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Eating",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "\"Eating\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:11+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"Counseling\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"nutrition counseling\"[Title/Abstract] OR \"nutrition counselling\"[Title/Abstract] OR \"nutrition program\"[Title/Abstract] OR \"nutrition programs\"[Title/Abstract] OR \"nutrition intervention\"[Title/Abstract] OR \"nutrition interventions\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"food and nutrition\"[Title/Abstract:~2] OR \"nutrition behavior\"[Title/Abstract] OR \"nutrition behaviour\"[Title/Abstract] OR \"counsel*\"[Title/Abstract] OR \"nutritional\"[Title/Abstract]) AND (\"Adolescent\"[MeSH Terms] OR \"Child\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"adolescent*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth\"[Title/Abstract] OR \"young people\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"school children\"[Title/Abstract] OR \"school student*\"[Title/Abstract] OR \"child*\"[Title/Abstract] OR \"grade*\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"high school*\"[Title/Abstract] OR \"secondary school*\"[Title/Abstract] OR \"elementary school*\"[Title/Abstract] OR \"primary school*\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"school-based\"[Title/Abstract]) AND (\"Feeding Behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Eating\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms] OR \"diet*\"[Title/Abstract] OR \"eat\"[Title/Abstract] OR \"Eating\"[Title/Abstract] OR \"ate\"[Title/Abstract] OR \"food*\"[Title/Abstract] OR \"breakfast*\"[Title/Abstract] OR \"fast food*\"[Title/Abstract] OR \"sugar*\"[Title/Abstract] OR \"dietary intake\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"food eating\"[Title/Abstract] OR \"eating behavior\"[Title/Abstract] OR \"eating behaviour\"[Title/Abstract] OR \"Feeding Behavior\"[Title/Abstract] OR \"feeding behaviour\"[Title/Abstract] OR \"food choice*\"[Title/Abstract] OR \"dietary habit*\"[Title/Abstract] OR \"fruit*\"[Title/Abstract] OR \"vegetable*\"[Title/Abstract] OR \"beverage*\"[Title/Abstract] OR \"sugar sweetened beverage*\"[Title/Abstract] OR \"sugar sweetened beverage*\"[Title/Abstract] OR \"diet quality\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 8,
      "review_sha256": "d88820980ec9c65407325c4230ec26ceb0be3b314529f9eefaea9b2f22ae42ba",
      "note": "Same-context PRESS-structured critic: no fresh-context reviewer was available in this run. Reviewed the packet across the six specified domains and checked PubMed translations and diagnostics.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The four AND-ed blocks correspond to the eligibility concepts. School setting and consumption outcome were tested as optional concepts; both passed current loss samples with zero relevant records and material reductions. Category probes caused vocabulary expansion."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines alternatives within concepts; AND combines the four concepts. No NOT operator is used in the search. The food-and-nutrition proximity term uses a tested two-word distance for order variation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings are valid PubMed MeSH descriptors checked in the packet and live authority checks: Health Education, Health Promotion, Counseling, Adolescent, Child, Students, Schools, Feeding Behavior, Diet, Eating, and Food Preferences. All headings are exploded."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover nutrition and food education, counseling, diet/eating outcomes, adolescents, children, students, and grade wording. Broad nutritional[tiab], child*[tiab], and grade*[tiab] were retained to recover probe records; final result count is 5,861."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current lint has no issues. Each term carries an explicit field tag; no short wildcard, typographic characters, or translation warnings appear in the complete evaluation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or study-design filter is applied. The harness Entrez-date bound is 2017-12-14 and the final query expresses it as an entry-date restriction, not a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "The education probe cannot be refreshed because the standard-depth two-probe budget is spent. Probe 2 screened 30 records and found none relevant; probe 1 found one relevant record, whose wording was added. The later population-block broadening changes the education probe's base, so current education coverage remains uncertain and needs human PRESS review.",
          "evidence": "Education probe 1: 1/30 relevant (PMID 28712260), followed by adding nutritional[tiab]. Education probe 2: 0/30 relevant. Both are returned in the current query after vocabulary expansion; seven development records are retrieved, but no independent seed or benchmark set exists."
        },
        {
          "issue_id": "I-d1cede3eac8fca350d4c",
          "status": "accepted-risk",
          "response": "The second and final standard-depth population probe found two likely in-scope records, and the search was broadened with child*[tiab] and grade*[tiab] to recover them. A third probe exceeds the configured standard budget. Residual population-member risk, including the provisional fifth-grade record with no abstract, should be checked by an information specialist.",
          "evidence": "Population probe 2 screened 30 records from 393 outside the original block and found PMIDs 15415210 and 27382638; both are retrieved by the broadened current query. Probe 1 found 0/30. The current relevant set has seven records and all seven are retrieved; its 100% relative recall is development-only."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 8,
      "review_sha256": "d88820980ec9c65407325c4230ec26ceb0be3b314529f9eefaea9b2f22ae42ba",
      "note": "Same-context second PRESS-structured review round. No fresh-context reviewer was available. The diagnostic report revalidated the final strategy live with zero technical blockers; no strategy changes are planned.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The four blocks correspond to the intervention, population, school setting, and food-consumption outcome. Optional tests support including school and consumption; the residual category-probe concerns remain explicitly accepted risks."
        },
        "operators": {
          "verdict": "pass",
          "note": "Boolean structure is OR within concepts and AND across concepts. The proximity expression is confined to food/nutrition word order; no untested operator changes were made."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All headings are valid and exploded, with both MeSH and title/abstract layers in each block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The final vocabulary includes the two discovered wording gaps, nutritional and child/grade terms, and all seven relevant development records are retrieved. The result set is 5,861."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Live diagnostic revalidation found no blockers or translation issues. Lint remains clear."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No ad hoc limits or study-design filters are present. The sole date bound is the required PubMed Entrez-date cutoff of 2017-12-14."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "Retain the education probe concern for information-specialist review. The available two-probe budget is exhausted; the second probe found no eligible records, and its base became stale only after the population block was widened to include child and grade wording. No independent evidence establishes full category coverage.",
          "evidence": "Education probe history reports 1/30 relevant at probe 1 and 0/30 at probe 2; the term nutritional[tiab] was added after the first finding. The final query retrieves all seven development records."
        },
        {
          "issue_id": "I-d1cede3eac8fca350d4c",
          "status": "accepted-risk",
          "response": "Retain the population residual risk for information-specialist review. The standard probe budget is spent; the two likely records found in probe 2 are recovered by child*[tiab] and grade*[tiab], but further member-only population wording has not been measured. One PMID has no abstract and remains provisional.",
          "evidence": "Population probe 2 screened 30 records from 393 outside the prior block, finding PMIDs 15415210 and 27382638. Both are in the current relevant set and retrieved by the query. Probe 1 was 0/30; seven development records are retrieved in total."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 8,
      "review_sha256": "d88820980ec9c65407325c4230ec26ceb0be3b314529f9eefaea9b2f22ae42ba",
      "note": "Same-context closing review. No fresh-context information specialist was available. The final live diagnostic found no technical blockers; the two revision rounds carried the documented category risks forward as accepted risks.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No substantive translation changes were requested in either revision round. The scope, four search blocks, eligibility, and optional decisions match the question."
        },
        "operators": {
          "verdict": "pass",
          "note": "No unresolved Boolean or proximity defects were found."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "No unresolved MeSH heading defects were found; headings are valid, exploded, and accompanied by text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The final strategy retains the terms added from screened category-probe records. Broader terms and unresolved probe limits are documented for specialist review."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Diagnostic live validation and lint show no technical blocker or translation issue."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unjustified filters or limits are present; the cutoff is Entrez date 2017-12-14."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "Accepted as a documented risk for human PRESS review. The standard probe budget has been spent, and the education probe's base changed after a population expansion.",
          "evidence": "Education probes screened 30 records each: probe 1 found one relevant record recovered by added vocabulary; probe 2 found none. All seven records in the development set are retrieved. The final live diagnostic has no technical blockers."
        },
        {
          "issue_id": "I-d1cede3eac8fca350d4c",
          "status": "accepted-risk",
          "response": "Accepted as a documented population coverage risk for human PRESS review. The final allowed probe found two likely records, both recovered with broad child and grade terms; the remaining outside-block estimate is not independently confirmed.",
          "evidence": "Population probe 2 found PMIDs 15415210 and 27382638 among 30 screened records; both are retrieved by the final query. One record's abstract is unavailable and is provisional. Seven development records are retrieved; no independent seed or validation set exists."
        }
      ]
    }
  ]
}
```


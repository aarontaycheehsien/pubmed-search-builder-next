# PubMed search strategy: audit

Generated 2026-09-29T02:46:56+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: yes (User supplied no known articles and asked to proceed without clarification. Assumptions: PICO intervention-effectiveness framework; food/nutrition education and adolescents/school students are required search blocks; school setting and food-consumption outcomes are tested as optional blocks. No language, age filter, publication-date filter, or other limit. PubMed retrieval is bounded by PSB_AS_OF=2017-12-14 (Entrez date), not publication date.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food and nutrition education intervention | search | The intervention defines the review; relevant programs may be described through member activities such as nutrition education, nutrition instruction, food education, cooking or food skills. |
| Adolescents or school students | search | The question is specific to adolescents or school students. Search broad age and student terminology; screen exact age and school eligibility. |
| School delivery setting | optional | School delivery is central to eligibility but may be absent from abstracts; test its retrieval tradeoff before deciding whether to AND it. |
| Eligible food-consumption outcomes | optional | Food consumption defines the topic but outcomes may be inconsistently named; test a broad outcome block before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:45:56+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 70,390
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Child Nutrition Sciences"[Mesh]` | 1,076 | none |
| 3 | `"Cooking"[Mesh]` | 10,657 | none |
| 4 | `"Gardening"[Mesh]` | 811 | none |
| 5 | `nutrition education[tiab]` | 3,866 | none |
| 6 | `food education[tiab]` | 84 | none |
| 7 | `nutrition instruction[tiab]` | 46 | none |
| 8 | `nutrition program*[tiab]` | 2,437 | none |
| 9 | `nutrition intervention*[tiab]` | 1,929 | none |
| 10 | `dietary education[tiab]` | 252 | none |
| 11 | `diet education[tiab]` | 115 | none |
| 12 | `nutrition curriculum[tiab]` | 87 | none |
| 13 | `food curriculum[tiab]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 14 | `nutrition lesson*[tiab]` | 28 | none |
| 15 | `food lesson*[tiab]` | 1 | none |
| 16 | `healthy eating education[tiab]` | 7 | none |
| 17 | `food literacy[tiab]` | 34 | none |
| 18 | `nutrition literacy[tiab]` | 48 | none |
| 19 | `cooking class*[tiab]` | 73 | none |
| 20 | `cooking lesson*[tiab]` | 9 | none |
| 21 | `food preparation[tiab]` | 1,508 | none |
| 22 | `culinary education[tiab]` | 3 | none |
| 23 | `gardening program*[tiab]` | 34 | none |
| 24 | `nutrition promot*[tiab]` | 145 | none |
| 25 | `food skills[tiab]` | 31 | none |
| 26 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 239,914 | none |
| 27 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 28 | `"Child"[Mesh]` | 1,797,170 | none |
| 29 | `"Students"[Mesh]` | 112,971 | none |
| 30 | `adolescen*[tiab]` | 248,945 | none |
| 31 | `teen*[tiab]` | 26,895 | none |
| 32 | `youth[tiab]` | 57,369 | none |
| 33 | `young people[tiab]` | 23,082 | none |
| 34 | `young person*[tiab]` | 3,098 | none |
| 35 | `schoolchild*[tiab]` | 13,052 | none |
| 36 | `school child*[tiab]` | 21,096 | none |
| 37 | `pupil*[tiab]` | 26,074 | none |
| 38 | `student*[tiab]` | 234,078 | none |
| 39 | `child*[tiab]` | 1,257,861 | none |
| 40 | `school-age*[tiab]` | 18,888 | none |
| 41 | `school age[tiab]` | 11,579 | none |
| 42 | `#27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41` | 3,398,882 | none |
| 43 | `#26 AND #42` | 70,390 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Child Nutrition Sciences"[Mesh] OR "Cooking"[Mesh] OR "Gardening"[Mesh] OR nutrition education[tiab] OR food education[tiab] OR nutrition instruction[tiab] OR nutrition program*[tiab] OR nutrition intervention*[tiab] OR dietary education[tiab] OR diet education[tiab] OR nutrition curriculum[tiab] OR food curriculum[tiab] OR nutrition lesson*[tiab] OR food lesson*[tiab] OR healthy eating education[tiab] OR food literacy[tiab] OR nutrition literacy[tiab] OR cooking class*[tiab] OR cooking lesson*[tiab] OR food preparation[tiab] OR culinary education[tiab] OR gardening program*[tiab] OR nutrition promot*[tiab] OR food skills[tiab]) AND ("Adolescent"[Mesh] OR "Child"[Mesh] OR "Students"[Mesh] OR adolescen*[tiab] OR teen*[tiab] OR youth[tiab] OR young people[tiab] OR young person*[tiab] OR schoolchild*[tiab] OR school child*[tiab] OR pupil*[tiab] OR student*[tiab] OR child*[tiab] OR school-age*[tiab] OR school age[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 12 | 12 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| School delivery setting | left out | 70,390 / 18,541 | 73.7% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out: 12 known in-scope records remain below the 15-record safety threshold for AND-ing an optional concept. The refreshed 30-record loss sample contained no eligible records, but this does not compensate for the shortfall in known-record evidence. |
| Eligible food-consumption outcomes | left out | 70,390 / 9,227 | 86.9% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out: 12 known in-scope records remain below the 15-record safety threshold for AND-ing an optional concept. The refreshed 30-record loss sample contained no eligible records, but this does not compensate for the shortfall in known-record evidence. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food and nutrition education intervention | 1 | `educat*[tiab] OR intervention*[tiab] OR program*[tiab] OR lesson*[tiab] OR curriculum[tiab] OR class*[tiab] OR cooking[tiab] OR garden*[tiab]` | 590,494 | 0/30 |
| Adolescents or school students | 1 | `grade*[tiab] OR pupil*[tiab] OR schoolchild*[tiab] OR school*[tiab] OR junior[tiab] OR young[tiab] OR youth*[tiab] OR elementary[tiab] OR secondary[tiab]` | 9,239 | 0/30 |
| Adolescents or school students | 2 | `grade*[tiab] OR pupil*[tiab] OR schoolchild*[tiab] OR school*[tiab] OR junior[tiab] OR young[tiab] OR youth*[tiab] OR elementary[tiab] OR secondary[tiab]` | 9,239 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 3,398,882 | 0 |
| adolescents_students | 239,914 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial strategy built from scoped blocks, controlled vocabulary discovery, and a screened PubMed pilot sample. Tested optional setting and outcome concepts are included as candidates, not AND-ed. |
| 2 | 0 | education: +24 / -0; adolescents_students: +15 / -0 | none | Initial draft using required food/nutrition education and adolescent/school-student blocks, with school-setting and food-consumption outcome candidates for separate testing. Terms reflect MeSH lookups and screened pilot records. |
| 3 | 70,386 | limits/combination | none | Removed malformed custom combine expression; default combines the two required concept blocks with AND. Optional setting and outcome blocks remain candidates for testing. |
| 4 | 70,390 | education: +1 / -0 | none | Added the bare-name food skills term requested by the internal critic because it is explicitly named in the education concept rationale. Re-evaluating the complete strategy and known set. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 3 findings; R1-F1 should-fix open, R1-F2 must-fix rejected, R1-F3 should-fix accepted-risk
- Round 2 on version 4: 3 findings; R1-F1 should-fix resolved, R1-F2 must-fix rejected, R1-F3 should-fix accepted-risk
- Round 3 on version 4: 3 findings; R1-F1 should-fix resolved, R1-F2 must-fix rejected, R1-F3 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1381 NCBI requests logged (582 from cache); strategy sha256 2c3384e95f36._

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
        "message": "70,390 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(food curriculum[tiab]) AND (\"1800/01/01\"[edat] : \"2017/12/14\"[edat])",
        "translation": "\"food curriculum\"[Title/Abstract] AND 1800/01/01:2017/12/14[Date - Entry]",
        "location": "line:13",
        "blocking": false,
        "requires_review": true,
        "id": "I-d9975e02a472546448c2"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(food curriculum[tiab]) AND (\"1800/01/01\"[edat] : \"2017/12/14\"[edat])",
        "translation": "\"food curriculum\"[Title/Abstract] AND 1800/01/01:2017/12/14[Date - Entry]",
        "location": "line:13",
        "blocking": false,
        "requires_review": true,
        "id": "I-6edf5661ab32d13c6ace"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "70,390 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(food curriculum[tiab]) AND (\"1800/01/01\"[edat] : \"2017/12/14\"[edat])",
        "translation": "\"food curriculum\"[Title/Abstract] AND 1800/01/01:2017/12/14[Date - Entry]",
        "location": "line:13",
        "blocking": false,
        "requires_review": true,
        "id": "I-d9975e02a472546448c2"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(food curriculum[tiab]) AND (\"1800/01/01\"[edat] : \"2017/12/14\"[edat])",
        "translation": "\"food curriculum\"[Title/Abstract] AND 1800/01/01:2017/12/14[Date - Entry]",
        "location": "line:13",
        "blocking": false,
        "requires_review": true,
        "id": "I-6edf5661ab32d13c6ace"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:45:56+00:00",
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
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:45:56+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Child Nutrition Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cooking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:45:56+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003296",
          "name": "Cooking",
          "type": "descriptor",
          "scope_note": "The art or practice of preparing food. It includes the preparation of special foods for diets in various diseases.",
          "tree_numbers": [
            "J01.576.423.200.200"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003296",
      "preferred_label": "Cooking",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Cooking\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Gardening",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:45:56+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D051639",
          "name": "Gardening",
          "type": "descriptor",
          "scope_note": "Cultivation of PLANTS; (FRUIT; VEGETABLES; MEDICINAL HERBS) on small plots of ground or in containers.",
          "tree_numbers": [
            "I03.450.642.581.500",
            "J01.040.498.500"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D051639",
      "preferred_label": "Gardening",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Gardening\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:45:56+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:45:56+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:45:56+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Child Nutrition Sciences\"[MeSH Terms] OR \"Cooking\"[MeSH Terms] OR \"Gardening\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"diet education\"[Title/Abstract] OR \"nutrition curriculum\"[Title/Abstract] OR \"food curriculum\"[Title/Abstract] OR \"nutrition lesson*\"[Title/Abstract] OR \"food lesson*\"[Title/Abstract] OR \"healthy eating education\"[Title/Abstract] OR \"food literacy\"[Title/Abstract] OR \"nutrition literacy\"[Title/Abstract] OR \"cooking class*\"[Title/Abstract] OR \"cooking lesson*\"[Title/Abstract] OR \"food preparation\"[Title/Abstract] OR \"culinary education\"[Title/Abstract] OR \"gardening program*\"[Title/Abstract] OR \"nutrition promot*\"[Title/Abstract] OR \"food skills\"[Title/Abstract]) AND (\"Adolescent\"[MeSH Terms] OR \"Child\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"adolescen*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth\"[Title/Abstract] OR \"young people\"[Title/Abstract] OR \"young person*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"school child*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"child*\"[Title/Abstract] OR \"school age*\"[Title/Abstract] OR \"school age\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "83c9c8b9d1c24f3affd4ef8434f517b9db895d5695dd6f31aa0dace28040ecff",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The education rationale explicitly names food skills, but that member is not represented by its own bare-name text term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concepts are OR-combined internally and AND-combined; optional setting and outcome blocks were tested and left out with the stated safety-gate rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are verified, and the broad child and student headings are consistent with the stated screening approach."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The food curriculum zero-hit warning was reviewed; it is a plausible phrase, but has no retrieval evidence in the bounded query. Retaining it is reasonable pending further review."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has balanced grouping and valid Boolean structure; no proximity operators or syntax errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez cutoff is imposed by the harness through PSB_AS_OF=2017-12-14 and must remain on every PubMed command. No publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched education concept rationale names food skills as a relevant activity, but the strategy has no bare-name food skills text term.",
          "recommendation": "Add food skills[tiab] to the education block and re-evaluate the complete strategy.",
          "status": "open"
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez date limit ending 2017-12-14 although the protocol states no date limit.",
          "recommendation": "Remove the Entrez date limit.",
          "status": "rejected",
          "response": "Rejected because the harness explicitly requires PSB_AS_OF=2017-12-14 on every command and requires PubMed to be bounded by Entrez date, while expressly prohibiting a publication-date limit. The date bound is environment-enforced and is not a review eligibility limit."
        },
        {
          "id": "R1-F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The strategy retrieves 70,386 records against a 10,000-record workload budget. Both optional concepts were tested, but neither met the evidence gate for mandatory use.",
          "recommendation": "Record that the strategy is not operationally within budget and do not choose a narrower strategy without enough evidence.",
          "status": "accepted-risk",
          "response": "The count is valid and remains an operational concern. Both eligible screened-only concepts were tested and left out because only 12 known eligible records were available, below the required 15-record gate. The broad strategy prioritizes recall, and this issue is explicitly handed to the information-specialist reviewer."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The over-budget warning is valid. Both screened-only eligibility concepts were considered and tested, but their blocks were left out because only 12 known relevant records were available, below the stated 15-record safety gate. The strategy should not be treated as within the 10,000-record workload budget.",
          "evidence": "The base query returns 70,386 records; setting and outcome blocks reduce this to 18,541 and 9,224, respectively. Each removed-record sample had 0/30 relevant records, but neither optional block met the known-record gate."
        },
        {
          "issue_id": "I-d9975e02a472546448c2",
          "status": "accepted-risk",
          "response": "Reviewed the warning at the food curriculum term in the education clause. The phrase is understandable and plausibly relevant; retain it provisionally rather than deleting it solely because it retrieves no records.",
          "evidence": "The PubMed translation is the literal Title/Abstract phrase; count is zero and the only message is No items found. The term is an OR alternative."
        },
        {
          "issue_id": "I-6edf5661ab32d13c6ace",
          "status": "accepted-risk",
          "response": "Reviewed the zero-hit warning at the food curriculum term in the education clause. Retain provisionally as a plausible phrase; it does not constrain retrieval because it is an OR alternative.",
          "evidence": "The term returned zero records under the required Entrez-date bound; zero retrieval does not establish redundancy or invalidity."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "e157891c93704dee2f46b280b4453bf8d80d07e816ff1f1c8314915ecc976177",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The education block now includes the bare-name food skills[tiab] term requested in R1-F1. Its other named activities are represented, and both required concepts retain all 12 known in-scope records."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within each required concept and the two blocks are AND-combined. Both optional blocks were tested and left out because the 12 known records remain below the 15-record safety threshold."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included MeSH headings are verified in the packet and are consistent with broad retrieval followed by eligibility screening."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The food curriculum warning was reviewed clause by clause: PubMed translates it as the literal Title/Abstract phrase, reports no items, and it remains a plausible on-scope OR alternative. Its zero count alone is not grounds for deletion."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query has balanced grouping and valid Boolean structure, with no reported syntax errors or proximity operators."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The required Entrez cutoff is applied consistently; no publication-date or other eligibility filter is used. The 70,390-record count exceeds the 10,000 workload budget and remains an explicit accepted risk because neither optional block met the evidence gate."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched education concept rationale names food skills as a relevant activity, but the strategy has no bare-name food skills text term.",
          "recommendation": "Add food skills[tiab] to the education block and re-evaluate the complete strategy.",
          "status": "resolved",
          "response": "The current education block includes food skills[tiab]. The complete evaluation is current, and all 12 known in-scope records remain retrieved."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez date limit ending 2017-12-14 although the protocol states no date limit.",
          "recommendation": "Remove the Entrez date limit.",
          "status": "rejected",
          "response": "The packet states that the harness requires PSB_AS_OF=2017-12-14 on every command and requires PubMed retrieval to be bounded by Entrez date. This is an environment bound, not a publication-date eligibility limit."
        },
        {
          "id": "R1-F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The strategy retrieves 70,390 records against a 10,000-record workload budget. Neither optional concept met the evidence gate for mandatory use.",
          "recommendation": "Record that the strategy is not operationally within budget and do not choose a narrower strategy without enough evidence.",
          "status": "accepted-risk",
          "response": "The strategy remains over budget. School setting and food-consumption outcome blocks reduce the retrieval count, but only 12 known in-scope records are available, below the 15-record safety threshold; each refreshed loss sample found 0/30 eligible records. The broad strategy prioritizes recall."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The over-budget warning is valid and remains an operational concern. Neither optional block is justified for AND-ing under the stated known-record safety gate.",
          "evidence": "The current query retrieves 70,390 records. The school-setting block reduces this to 18,541 and the food-consumption block to 9,227; only 12 known in-scope records are available, below the 15-record threshold. Both refreshed loss samples found 0/30 relevant records."
        },
        {
          "issue_id": "I-d9975e02a472546448c2",
          "status": "accepted-risk",
          "response": "Retain food curriculum[tiab] as a plausible, on-scope OR alternative. The warning was reviewed and does not indicate an ignored phrase or malformed translation.",
          "evidence": "PubMed translates the term as the literal phrase \"food curriculum\"[Title/Abstract], reports only \"No items found,\" and returns zero records under the required Entrez bound."
        },
        {
          "issue_id": "I-6edf5661ab32d13c6ace",
          "status": "accepted-risk",
          "response": "Retain the term provisionally; zero retrieval alone does not establish that it is invalid or redundant.",
          "evidence": "The term is a literal Title/Abstract phrase in the education OR clause and returns zero records under the required Entrez bound."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "e157891c93704dee2f46b280b4453bf8d80d07e816ff1f1c8314915ecc976177",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The education block includes food skills[tiab], and the current strategy retains all 12 known in-scope records."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within each required concept, and the two required blocks are AND-combined. Optional blocks were tested and left out because the known-record count is below the stated safety threshold."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included MeSH headings are verified in the packet and support broad retrieval followed by eligibility screening."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The food curriculum warning was reviewed clause by clause. PubMed translates it as a literal Title/Abstract phrase; it remains a plausible on-scope OR alternative despite zero hits."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has balanced grouping and valid Boolean structure, with no reported syntax errors or proximity operators."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The required Entrez cutoff is applied consistently, with no publication-date or other eligibility filter. The 70,390-record count exceeds the workload budget; this remains an explicit accepted risk because neither optional block met the evidence gate."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched education concept rationale names food skills as a relevant activity, but the strategy has no bare-name food skills text term.",
          "recommendation": "Add food skills[tiab] to the education block and re-evaluate the complete strategy.",
          "status": "resolved",
          "response": "The current education block includes food skills[tiab]. The complete evaluation is current, and all 12 known in-scope records remain retrieved."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez date limit ending 2017-12-14 although the protocol states no date limit.",
          "recommendation": "Remove the Entrez date limit.",
          "status": "rejected",
          "response": "The packet states that the harness requires PSB_AS_OF=2017-12-14 on every command and requires PubMed retrieval to be bounded by Entrez date. This is an environment bound, not a publication-date eligibility limit."
        },
        {
          "id": "R1-F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The strategy retrieves 70,390 records against a 10,000-record workload budget. Neither optional concept met the evidence gate for mandatory use.",
          "recommendation": "Record that the strategy is not operationally within budget and do not choose a narrower strategy without enough evidence.",
          "status": "accepted-risk",
          "response": "The strategy remains over budget. School setting and food-consumption outcome blocks reduce the retrieval count, but only 12 known in-scope records are available, below the 15-record safety threshold; each refreshed loss sample found 0/30 eligible records. The broad strategy prioritizes recall."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The over-budget warning is valid and remains an operational concern. Neither optional block is justified for AND-ing under the stated known-record safety gate.",
          "evidence": "The current query retrieves 70,390 records. The school-setting block reduces this to 18,541 and the food-consumption block to 9,227; only 12 known in-scope records are available, below the 15-record threshold. Both refreshed loss samples found 0/30 relevant records."
        },
        {
          "issue_id": "I-d9975e02a472546448c2",
          "status": "accepted-risk",
          "response": "Retain food curriculum[tiab] as a plausible, on-scope OR alternative. The warning was reviewed and does not indicate an ignored phrase or malformed translation.",
          "evidence": "PubMed translates the term as the literal Title/Abstract phrase \"food curriculum\", reports only \"No items found,\" and returns zero records under the required Entrez bound."
        },
        {
          "issue_id": "I-6edf5661ab32d13c6ace",
          "status": "accepted-risk",
          "response": "Retain the term provisionally; zero retrieval alone does not establish that it is invalid or redundant.",
          "evidence": "The term is a literal Title/Abstract phrase in the education OR clause and returns zero records under the required Entrez bound."
        }
      ]
    }
  ]
}
```


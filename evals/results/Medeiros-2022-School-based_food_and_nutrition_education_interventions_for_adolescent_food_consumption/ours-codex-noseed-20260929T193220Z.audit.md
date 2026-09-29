# PubMed search strategy: audit

Generated 2026-09-29T20:33:01+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (No known relevant articles or seed records were supplied. User requested that the run proceed without clarification; roles were assigned from the question and eligibility criteria. Harness restricts PubMed by Entrez date through PSB_AS_OF=2017/12/14; no publication-date limit is applied. Search outcome is a candidate rather than a required block pending empirical tests.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food or nutrition education intervention | search | The intervention is central to the question and can be represented by nutrition education, health education, dietary education and classroom teaching terms. |
| Adolescents or school students | search | The target population is explicit and broadly searchable through adolescent and student terminology; screen age and participant details for eligibility. |
| School delivery setting | optional | School delivery is required for eligibility and often named/indexed, but may be absent from abstracts; test a candidate block before deciding whether to AND it. |
| Food consumption outcomes | optional | Food consumption defines the topic, but outcome reporting is inconsistently named; test a candidate block before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T20:31:57+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 21,262
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 3 | `"nutrition education"[tiab]` | 3,866 | none |
| 4 | `"food education"[tiab]` | 84 | none |
| 5 | `"dietary education"[tiab]` | 252 | none |
| 6 | `"nutrition teaching"[tiab]` | 72 | none |
| 7 | `"nutrition instruction"[tiab]` | 46 | none |
| 8 | `"nutrition curriculum"[tiab]` | 87 | none |
| 9 | `"nutrition knowledge"[tiab]` | 922 | none |
| 10 | `"food knowledge"[tiab]` | 90 | none |
| 11 | `"dietary knowledge"[tiab]` | 121 | none |
| 12 | `"nutrition intervention*"[tiab]` | 1,929 | none |
| 13 | `"dietary intervention*"[tiab]` | 5,988 | none |
| 14 | `"nutrition program*"[tiab]` | 2,437 | none |
| 15 | `"food program*"[tiab]` | 485 | none |
| 16 | `(nutrition[tiab] AND educat*[tiab])` | 15,639 | none |
| 17 | `(food[tiab] AND educat*[tiab])` | 14,084 | none |
| 18 | `(dietary[tiab] AND educat*[tiab])` | 10,281 | none |
| 19 | `(nutrition[tiab] AND intervention*[tiab])` | 16,941 | none |
| 20 | `"nutrition lesson*"[tiab]` | 28 | none |
| 21 | `"food lesson*"[tiab]` | 1 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 262,949 | none |
| 23 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 24 | `"Students"[Mesh]` | 112,971 | none |
| 25 | `"Child"[Mesh]` | 1,797,170 | none |
| 26 | `adolescent*[tiab]` | 213,221 | none |
| 27 | `teen*[tiab]` | 26,895 | none |
| 28 | `teens[tiab]` | 5,616 | none |
| 29 | `youth[tiab]` | 57,369 | none |
| 30 | `youths[tiab]` | 10,200 | none |
| 31 | `teenager*[tiab]` | 13,059 | none |
| 32 | `schoolchild*[tiab]` | 13,052 | none |
| 33 | `pupil*[tiab]` | 26,074 | none |
| 34 | `(school[tiab] AND child*[tiab])` | 80,160 | none |
| 35 | `students[tiab]` | 200,550 | none |
| 36 | `student*[tiab]` | 234,078 | none |
| 37 | `child*[tiab]` | 1,257,861 | none |
| 38 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 3,390,002 | none |
| 39 | `"Schools"[Mesh]` | 107,820 | none |
| 40 | `"School Health Services"[Mesh]` | 21,872 | none |
| 41 | `school*[tiab]` | 246,627 | none |
| 42 | `classroom*[tiab]` | 14,159 | none |
| 43 | `class-based[tiab]` | 424 | none |
| 44 | `#39 OR #40 OR #41 OR #42 OR #43` | 317,006 | none |
| 45 | `#22 AND #38 AND #44` | 21,262 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR "nutrition education"[tiab] OR "food education"[tiab] OR "dietary education"[tiab] OR "nutrition teaching"[tiab] OR "nutrition instruction"[tiab] OR "nutrition curriculum"[tiab] OR "nutrition knowledge"[tiab] OR "food knowledge"[tiab] OR "dietary knowledge"[tiab] OR "nutrition intervention*"[tiab] OR "dietary intervention*"[tiab] OR "nutrition program*"[tiab] OR "food program*"[tiab] OR (nutrition[tiab] AND educat*[tiab]) OR (food[tiab] AND educat*[tiab]) OR (dietary[tiab] AND educat*[tiab]) OR (nutrition[tiab] AND intervention*[tiab]) OR "nutrition lesson*"[tiab] OR "food lesson*"[tiab]) AND ("Adolescent"[Mesh] OR "Students"[Mesh] OR "Child"[Mesh] OR adolescent*[tiab] OR teen*[tiab] OR teens[tiab] OR youth[tiab] OR youths[tiab] OR teenager*[tiab] OR schoolchild*[tiab] OR pupil*[tiab] OR (school[tiab] AND child*[tiab]) OR students[tiab] OR student*[tiab] OR child*[tiab]) AND ("Schools"[Mesh] OR "School Health Services"[Mesh] OR school*[tiab] OR classroom*[tiab] OR class-based[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
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
| School delivery setting | AND-ed | 81,588 / 21,262 | 73.9% | none | 0/30 (up to 10% of removed records could be relevant) | After the education/population wording update, the current school-block loss sample removed 60,326 records and all 30 sampled abstracts were screened; none met eligibility. The 19-record development set is preserved, and school delivery is mandatory in the protocol. Retain the setting block while documenting that category probes are not current enough to establish coverage for all unseen studies. |
| Food consumption outcomes | left out | 21,262 / 3,406 | 84.0% | 16128481, 28146599 | 0/30 (up to 10% of removed records could be relevant) | The current outcome-block loss sample removed 17,856 records; its 30 records were screened and none met eligibility. However, the separate current broader outcome category probe found two eligible reports outside this block (PMID 16128481 and PMID 28146599). Leave the outcome block out to preserve recall; the candidate vocabulary is incomplete for consumption outcomes. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food or nutrition education intervention | 1 | `nutrition[tiab] OR food[tiab] OR diet*[tiab] OR Child Nutrition Sciences[Mesh]` | 87,139 | 0/30 |
| Food or nutrition education intervention | 2 | `nutrition[tiab] OR food[tiab] OR diet*[tiab] OR Child Nutrition Sciences[Mesh]` | 4,229 | 0/30 |
| Adolescents or school students | 1 | `student*[tiab] OR child*[tiab] OR pupil*[tiab] OR Students[Mesh] OR Child[Mesh]` | 9,776 | 0/30 |
| Adolescents or school students | 2 | `student*[tiab] OR child*[tiab] OR pupil*[tiab] OR Students[Mesh] OR Child[Mesh]` | 44 | 1/30 |
| School delivery setting | 1 | `educational institution*[tiab] OR classroom*[tiab] OR school*[tiab] OR Schools[Mesh] OR School Health Services[Mesh]` | 4 | 0/4 |
| School delivery setting | 2 | `school*[tiab] OR classroom*[tiab] OR school delivery[tiab] OR Schools[Mesh]` | 0 | not screened |
| Food consumption outcomes | 1 | `eating[tiab] OR intake[tiab] OR consumption[tiab] OR food*[tiab] OR diet*[tiab]` | 2,879 | 0/30 |
| Food consumption outcomes | 2 | `eating[tiab] OR intake[tiab] OR consumption[tiab] OR food*[tiab] OR diet*[tiab]` | 2,881 | 2/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 217,008 | 0 |
| adolescents_students | 26,411 | 0 |
| school_setting | 81,588 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial scope-first draft: MeSH and title/abstract terms for education and adolescent/student population; school setting and consumption outcome are optional candidates for empirical testing; no seeds supplied. |
| 2 | 68,795 | education: +2 / -0 | none | Added the TEENS program name after terms miss showed the known study uses the program name rather than a listed education phrase; retained the broad phrase candidates pending review. |
| 3 | 20,563 | adolescents_students: +1 / -0; school_setting: +12 / -0 | none | Added the text word students based on objective mining from screened relevant records; broadened the tested outcome candidate with Fruit/Vegetables MeSH and free-text stems based on the same records. |
| 4 | 76,285 | education: +1 / -3; adolescents_students: +1 / -4; school_setting: +0 / -12 | none | Simplified redundant phrase variants and replaced the phrase-index-missing TEENS title phrase with teens[tiab]; kept an explicit student population term. Narrowed setting synonyms to headings and broad free-text stems, then re-evaluated all blocks and current optionals. |
| 5 | 21,708 | school_setting: +5 / -0 | none | Applied the measured school setting option: 71.5% count reduction, no loss among 16 development records, and 0/30 relevant records in the screened loss sample. |
| 6 | 3,299 | adolescents_students: +1 / -0; food_consumption: +22 / -0 | none | Added child*[tiab] after category probe screening found one eligible teacher-taught school nutrition program reported only as children in grades 1-4; recorded as a development record. |
| 7 | 3,297 | food_consumption: +1 / -1 | none | Removed PubMed proximity syntax that was unavailable by the requested 2017 cutoff; added the explicit reversed phrase quality of diet as a title/abstract variant and revalidated. |
| 8 | 83,472 | school_setting: +0 / -5; food_consumption: +0 / -22 | none | Moved previously tested optional blocks to candidates to measure current school-setting and outcome candidates against the updated population block and cutoff-compatible outcome vocabulary. |
| 9 | 21,892 | school_setting: +5 / -0 | none | Re-added the school-setting block based on the fresh current loss sample; all 17 known development records remain retrieved. |
| 10 | 3,297 | food_consumption: +22 / -0 | none |  |
| 11 | 21,892 | food_consumption: +0 / -22 | none |  |
| 12 | 21,262 | education: +1 / -1; adolescents_students: +1 / -0 | none | Round 2 critic found teens[tiab] in the intervention block. Moved it to the population block and added a nutrition AND intervention phrase for the TEENS study; current candidate already lacked proximity syntax, which is absent from the final candidate vocabulary. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 6: 3 findings; F1 must-fix open, F2 should-fix open, F3 should-fix open
- Round 2 on version 11: 4 findings; F1 must-fix open, F2 should-fix resolved, F3 should-fix resolved, F4 must-fix open
- Round 3 on version 12: 4 findings; F1 must-fix resolved, F2 should-fix resolved, F3 should-fix resolved, F4 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2770 NCBI requests logged (1435 from cache); strategy sha256 50aecf927859._

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
        "message": "21,262 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
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
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:adolescents_students",
        "blocking": false,
        "requires_review": true,
        "id": "I-e89fdadcf2f74aaa33fd"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:school_setting",
        "blocking": false,
        "requires_review": true,
        "id": "I-9af84dc3bcf805e2d7c7"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:food_consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-3d2125ea6e8bd1d82969"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "21,262 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
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
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:adolescents_students",
        "blocking": false,
        "requires_review": true,
        "id": "I-e89fdadcf2f74aaa33fd"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:school_setting",
        "blocking": false,
        "requires_review": true,
        "id": "I-9af84dc3bcf805e2d7c7"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:food_consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-3d2125ea6e8bd1d82969"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:31:57+00:00",
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
      "checked_at": "2026-09-29T20:31:57+00:00",
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
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:31:57+00:00",
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
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:31:57+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:31:57+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:31:57+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:31:57+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"nutrition teaching\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"nutrition curriculum\"[Title/Abstract] OR \"nutrition knowledge\"[Title/Abstract] OR \"food knowledge\"[Title/Abstract] OR \"dietary knowledge\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"dietary intervention*\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"food program*\"[Title/Abstract] OR (\"nutrition\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR (\"food\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR (\"dietary\"[Title/Abstract] AND \"educat*\"[Title/Abstract]) OR (\"nutrition\"[Title/Abstract] AND \"intervention*\"[Title/Abstract]) OR \"nutrition lesson*\"[Title/Abstract] OR \"food lesson*\"[Title/Abstract]) AND (\"Adolescent\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"Child\"[MeSH Terms] OR \"adolescent*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"teens\"[Title/Abstract] OR \"youth\"[Title/Abstract] OR \"youths\"[Title/Abstract] OR \"teenager*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR (\"school\"[Title/Abstract] AND \"child*\"[Title/Abstract]) OR \"Students\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"child*\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"School Health Services\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"class-based\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 6,
      "review_sha256": "fc6e9a9706de9ab71aa48923b483228d74f3d4dc362a4a1476d04081a8ef8b24",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched population block includes adolescent, student, and child terms, and the education block includes nutrition, food, and dietary education terms. The school and consumption concepts are represented, though making either an AND requirement may reduce recall."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy groups synonyms with OR and combines the concepts with AND. No inappropriate NOT exclusion is present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses relevant headings for health education, adolescents, students, schools, feeding behavior, food preferences, diet surveys, fruit, and vegetables, alongside title and abstract terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The outcome block is mandatory despite outcome language being inconsistently reported. Its test removed 84.9% of the records without that block, and the loss sample was small and tied to a stale evaluation. Reassess whether outcome terms should be an AND requirement."
        },
        "syntax": {
          "verdict": "revise",
          "note": "The query uses the PubMed proximity expression \"diet quality\"[tiab:~2]. That syntax postdates the requested 2017 search date. Replace it with explicit tested expressions that were available at the cutoff, then evaluate the complete revised query."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The strategy uses an Entrez date bound through 2017/12/14 and does not impose a publication-date limit, consistent with the packet instructions."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "syntax",
          "severity": "must-fix",
          "kind": "syntax",
          "finding": "The outcome block contains \"diet quality\"[tiab:~2], a proximity-search expression introduced after the requested 2017 search date. The query therefore relies on syntax unavailable at the stated historical cutoff.",
          "recommendation": "Replace the proximity expression with explicit, tested title and abstract expressions available by 2017, such as the exact phrase and any relevant reversed or intervening-word variants. Rerun the complete evaluation and record the resulting query and count.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Food-consumption outcome terms are AND-ed into a high-sensitivity search even though outcome reporting is inconsistently named. The tested outcome block reduced the school-based result set by 84.9%; the 0/30 loss sample does not establish that eligible studies lacking these terms are absent, and the outcome evaluation is marked stale.",
          "recommendation": "Reconsider the outcome block as a mandatory AND concept. Compare the complete strategy with and without it, screen an adequately documented loss sample from the current query, and retain the block only with a current evidence-based justification.",
          "status": "open"
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The school-setting block is mandatory, but its optional-concept decision is marked stale after the search changed. The reported 0/30 loss sample and lack of known-record losses therefore do not fully validate the current strategy.",
          "recommendation": "Retest the school-setting block against the current query. Document whether eligible school-delivered studies can lack school or classroom terms in searchable fields; if so, consider screening setting rather than requiring this block.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "The education block changed after its category probes, so the warning is valid and current probe coverage is incomplete. I accept this risk for this critique while recommending a fresh probe before treating the block as validated.",
          "evidence": "The two recorded education probes each screened 30 records and found no eligible records; all 17 known development records are retrieved. The packet says the block changed after those probes and the probe budget is spent, so those observations do not establish coverage for the current block."
        },
        {
          "issue_id": "I-c8fdb73cf414d3e5cc7b",
          "status": "rejected",
          "response": "The probe warning is resolved by the current population block: it includes the terms in the broader probe query, and the relevant PMID is retrieved by the current strategy.",
          "evidence": "The broader probe query uses student*, child*, pupil*, Students[Mesh], and Child[Mesh]; all five are covered in the current adolescents/students block. PMID 22523664 appears in the retrieved known records."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 11,
      "review_sha256": "2863361824e2bed168e6b2df04a5aa745a9c2d2b82a55c5922d39d4ec707ab07",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The education, population, and school blocks map to the question. The outcome block is intentionally left out after two eligible records were found outside it."
        },
        "operators": {
          "verdict": "revise",
          "note": "The education block contains teens[tiab], which is a population term and can satisfy the intervention block alone."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses relevant health education, health promotion, adolescent, student, child, school, and school health service headings with text words."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The education block contains a population-only term and education/population category probes are stale after changes."
        },
        "syntax": {
          "verdict": "revise",
          "note": "A prior version of the outcome candidate contained proximity syntax unavailable at the stated 2017 cutoff; the current strategy file should be checked for that legacy clause."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The search uses the Entrez date bound and no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "syntax",
          "severity": "must-fix",
          "kind": "syntax",
          "finding": "The retained food_consumption candidate still contains \"diet quality\"[tiab:~2], identified in the prior finding as proximity syntax introduced after the requested 2017 search date. Although the candidate is not AND-ed into the final strategy, it remains in the packet and was used for optional-block evaluation.",
          "recommendation": "Replace the proximity expression with explicit, tested title and abstract expressions available by the cutoff, or remove it from the candidate. Rerun the complete evaluation if the candidate is retained or used.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Food-consumption outcomes are no longer AND-ed into the final strategy. The current packet documents two eligible records excluded by that candidate block.",
          "recommendation": "Keep the outcome block out of the final strategy unless a future complete evaluation supports requiring it.",
          "status": "resolved",
          "response": "The current strategy leaves the outcome block out. The packet reports eligible records PMID 16128481 and PMID 28146599 lost by the candidate block, supporting that decision."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The school-setting block's original category probe is stale, but the packet reports a new optional-concept comparison against the current two-block base.",
          "recommendation": "Document and use the current comparison when deciding whether school setting should remain AND-ed.",
          "status": "resolved",
          "response": "The packet reports a current test with 17 known development records in the base and none lost, plus a random 30-record loss sample with no eligible records. This addresses the prior request to retest the school-setting block, while leaving the ordinary uncertainty of a small sample."
        },
        {
          "id": "F4",
          "domain": "operators",
          "severity": "must-fix",
          "kind": "structural",
          "finding": "teens[tiab] appears as an OR term in the food or nutrition education intervention block. A record mentioning teens without an education or intervention concept can therefore satisfy that block.",
          "recommendation": "Remove teens[tiab] from the education block or place it in the adolescents/students block, preserving the intended education concept. Rerun the complete evaluation after the change.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final yield exceeds the workload budget, and the packet has considered the optional school and food-consumption concepts. The school block is retained; the outcome block is left out after the probe found eligible records it would exclude. The remaining workload is accepted with screening required.",
          "evidence": "The final strategy returns 21,892 records against a 10,000-record budget. The school block reduces the tested base from 83,472 to 21,892; the outcome block would reduce it further but the packet identifies eligible PMIDs 16128481 and 28146599 among records it excludes."
        },
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "The education category probes are stale and their budget is spent, so they do not establish coverage for the current block. The warning remains relevant; accept the residual coverage uncertainty pending a fresh probe.",
          "evidence": "The packet marks the education probe status stale and reports two earlier probes of 30 records each with zero relevant records, while the current education block differs from the probed wording."
        },
        {
          "issue_id": "I-e89fdadcf2f74aaa33fd",
          "status": "accepted-risk",
          "response": "The adolescent/student category probes are stale after the block changed, and the spent probe budget prevents a current probe. Accept the residual coverage uncertainty pending a fresh probe.",
          "evidence": "The packet marks the population probe status stale. Earlier samples included a relevant record outside the broader block in probe 2, and the current block wording changed after those probes."
        },
        {
          "issue_id": "I-9af84dc3bcf805e2d7c7",
          "status": "rejected",
          "response": "The stale category-probe warning is superseded for the school-setting decision by a current optional-block retest. The warning does not require dropping the school block given that evidence and the eligibility requirement.",
          "evidence": "The packet reports the school block retested against the current two-block base: 17 known development records were present with none lost, and the current random loss sample found 0/30 eligible records."
        },
        {
          "issue_id": "I-4e04b1673c25a60cc719",
          "status": "rejected",
          "response": "The finding from the outcome probe supports leaving the outcome block out; it does not require another probe to validate an outcome block that is not part of the final AND-ed strategy.",
          "evidence": "The packet reports eligible PMIDs 16128481 and 28146599 excluded by the candidate outcome block and records the decision to leave that block out. The final strategy returns 21,892 records, without that block."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 12,
      "review_sha256": "bb0ce09f945ed50cd7ab0723735f995d36bfa83c0635f8c10bd3bc2ce534d1ba",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The education, adolescent/student, and school concepts are represented in the current query. Food-consumption outcomes remain out of the final AND-ed strategy after eligible records were found outside that block."
        },
        "operators": {
          "verdict": "pass",
          "note": "The current education block no longer contains teens[tiab]; the term appears in the adolescent/student block. The current query combines blocks with AND and terms within blocks with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The current strategy retains relevant health education, health promotion, adolescent, student, child, school, and school health service headings alongside text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The outcome block is omitted because eligible reports would be excluded; the stale education and population probe warnings remain documented accepted risks."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current final query and current food-consumption candidate use no proximity syntax. The historical [tiab:~2] expression appears only in earlier evaluation artifacts."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The current query uses the Entrez date bound through 2017/12/14 and no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "syntax",
          "severity": "must-fix",
          "kind": "syntax",
          "finding": "The earlier outcome block used \"diet quality\"[tiab:~2], syntax unavailable at the requested 2017 cutoff.",
          "recommendation": "Replace the proximity expression with tested expressions available by the cutoff, or remove it, then evaluate the revised strategy.",
          "status": "resolved",
          "response": "The current food-consumption candidate and final query contain no [tiab:~2] expression. The candidate uses explicit expressions, and the final query leaves that block out."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Food-consumption outcome terms were AND-ed into a high-sensitivity strategy despite inconsistent outcome reporting and a stale evaluation.",
          "recommendation": "Reconsider the outcome block as a mandatory concept and compare the strategy with and without it.",
          "status": "resolved",
          "response": "The final strategy leaves the outcome block out. The current packet reports eligible PMIDs 16128481 and 28146599 outside the candidate block."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The school-setting block's optional-concept decision was stale after the search changed.",
          "recommendation": "Retest the school-setting block against the current query and document the loss evidence.",
          "status": "resolved",
          "response": "The current comparison reports 0/30 eligible records in the school-block loss sample and preserves all 19 development records; the school block is retained because setting is required."
        },
        {
          "id": "F4",
          "domain": "operators",
          "severity": "must-fix",
          "kind": "structural",
          "finding": "teens[tiab] appeared as an OR term in the food or nutrition education intervention block, allowing a population-only mention to satisfy that block.",
          "recommendation": "Remove teens[tiab] from the education block or place it in the adolescents/students block, then rerun the evaluation.",
          "status": "resolved",
          "response": "In current version 12, teens[tiab] appears in the adolescent/student block and not in the education block. The packet records the complete evaluation with no known-record losses."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final yield remains above the workload budget after optional school and food-consumption concepts were considered. The school block is retained because delivery through school is required; the outcome block is omitted because it would exclude eligible reports. The remaining screening workload is accepted.",
          "evidence": "The version 12 final query returns 21,262 records against a 10,000-record budget. The school block removes 60,326 records from the tested base with 0/30 sampled removed records eligible; PMIDs 16128481 and 28146599 were found outside the candidate outcome block."
        },
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "The education category-probe warning remains relevant because the block changed after its probes and the probe budget is spent. Accept the residual uncertainty in coverage of the current education block.",
          "evidence": "The packet marks the education probe status stale. Its two recorded probes each screened 30 records and found no eligible records, but the current wording changed after those probes."
        },
        {
          "issue_id": "I-e89fdadcf2f74aaa33fd",
          "status": "accepted-risk",
          "response": "The adolescent/student category-probe warning remains relevant because the block changed after its probes and the probe budget is spent. Accept the residual uncertainty in coverage of the current population block.",
          "evidence": "The packet marks the population probe status stale. The earlier probes reported 0/30 and 1/30 eligible records outside their broader queries, and the current wording changed after those probes."
        },
        {
          "issue_id": "I-9af84dc3bcf805e2d7c7",
          "status": "rejected",
          "response": "The stale school-setting probe warning is superseded for the current decision by the documented current optional-block comparison. The evidence supports retaining the school block, which corresponds to a required eligibility criterion.",
          "evidence": "The current school-block comparison removed 60,326 records; its loss sample found 0/30 eligible records, and all 19 development records were preserved."
        },
        {
          "issue_id": "I-3d2125ea6e8bd1d82969",
          "status": "rejected",
          "response": "The food-consumption block is not part of the final AND-ed strategy, and current evidence supports leaving it out. The stale probe warning does not change that decision.",
          "evidence": "The current outcome-block loss sample found 0/30 eligible records, while the separate broader outcome probe found eligible PMIDs 16128481 and 28146599 outside the candidate block. The final query omits the outcome block."
        }
      ]
    }
  ]
}
```


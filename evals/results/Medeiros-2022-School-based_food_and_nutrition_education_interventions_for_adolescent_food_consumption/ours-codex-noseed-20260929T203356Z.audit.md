# PubMed search strategy: audit

Generated 2026-09-29T21:06:43+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: yes (User asked to proceed without clarification. Assumed an intervention-effectiveness PICO question; no comparator block. Adolescent/student population and food/nutrition education are core searched concepts. School delivery and food-consumption outcome are optional and will be tested. No publication-date limit; PubMed Entrez-date cutoff pinned by PSB_AS_OF=2017-12-14. Used Child[Mesh:noexp] to include school-aged children while excluding preschool-aged children.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food and nutrition education intervention | search | Intervention is central to the question and commonly named, while member programs and education terminology need broad coverage. |
| Adolescents or school students | search | The target population defines eligibility; include adolescent and student labels because records may use either category/member terms. |
| School delivery setting | optional | School setting is named directly by school, classroom, and school-level terms; this setting does not commonly hide behind a separate member label. |
| Food-consumption outcome | optional | The outcome defines the topic, but consumption measures are inconsistently reported; test before requiring. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T21:06:04+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 69,329
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Dietetics"[Mesh]` | 7,514 | none |
| 3 | `"nutrition education"[tiab]` | 3,866 | none |
| 4 | `nutrition educat*[tiab]` | 4,029 | none |
| 5 | `"food education"[tiab]` | 84 | none |
| 6 | `"diet education"[tiab]` | 115 | none |
| 7 | `"nutrition instruction"[tiab]` | 46 | none |
| 8 | `"nutrition curriculum"[tiab]` | 87 | none |
| 9 | `"food and nutrition education"[tiab]` | 105 | none |
| 10 | `nutrition counsel*[tiab]` | 724 | none |
| 11 | `nutrition program*[tiab]` | 2,437 | none |
| 12 | `dietary educat*[tiab]` | 263 | none |
| 13 | `dietary intervention*[tiab]` | 5,988 | none |
| 14 | `nutrition intervention*[tiab]` | 1,929 | none |
| 15 | `food intervention*[tiab]` | 66 | none |
| 16 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 239,796 | none |
| 17 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 18 | `"Students"[Mesh]` | 112,971 | none |
| 19 | `adolescent*[tiab]` | 213,221 | none |
| 20 | `teen*[tiab]` | 26,895 | none |
| 21 | `youth[tiab]` | 57,369 | none |
| 22 | `youths[tiab]` | 10,200 | none |
| 23 | `student*[tiab]` | 234,078 | none |
| 24 | `pupil*[tiab]` | 26,074 | none |
| 25 | `schoolchild*[tiab]` | 13,052 | none |
| 26 | `"Child"[Mesh:noexp]` | 1,587,439 | none |
| 27 | `child*[tiab]` | 1,257,861 | none |
| 28 | `#17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27` | 3,299,065 | none |
| 29 | `#16 AND #28` | 69,329 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Dietetics"[Mesh] OR "nutrition education"[tiab] OR nutrition educat*[tiab] OR "food education"[tiab] OR "diet education"[tiab] OR "nutrition instruction"[tiab] OR "nutrition curriculum"[tiab] OR "food and nutrition education"[tiab] OR nutrition counsel*[tiab] OR nutrition program*[tiab] OR dietary educat*[tiab] OR dietary intervention*[tiab] OR nutrition intervention*[tiab] OR food intervention*[tiab]) AND ("Adolescent"[Mesh] OR "Students"[Mesh] OR adolescent*[tiab] OR teen*[tiab] OR youth[tiab] OR youths[tiab] OR student*[tiab] OR pupil*[tiab] OR schoolchild*[tiab] OR "Child"[Mesh:noexp] OR child*[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
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
| School delivery setting | left out | 69,329 / 17,425 | 74.9% | none | 0/30 (up to 10% of removed records could be relevant) | The current 30-record loss sample yielded no clearly eligible study; PMID 14836540 had no abstract and remains uncertain. Only three development records are known, fewer than the 15 required to establish safety to require school setting. Keep setting for screening. |
| Food-consumption outcome | left out | 69,329 / 9,140 | 86.8% | none | 0/30 (up to 10% of removed records could be relevant) | The current 30-record loss sample contained no eligible record. Only three development records are known, fewer than the 15 required to establish safety to require an outcome block. The candidate includes broader diet-habit terms discovered from an earlier probe, while food consumption remains a screening criterion. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food and nutrition education intervention | 1 | `intervention*[tiab] OR program*[tiab] OR curricul*[tiab] OR teach*[tiab]` | 262,384 | 0/30 |
| Food and nutrition education intervention | 2 | `intervention*[tiab] OR program*[tiab] OR curricul*[tiab] OR teach*[tiab]` | 371,995 | not screened |
| Food and nutrition education intervention | 3 | `intervention*[tiab] OR program*[tiab] OR curricul*[tiab] OR teach*[tiab]` | 371,995 | 0/30 |
| Adolescents or school students | 1 | `child*[tiab] OR school*[tiab] OR pupil*[tiab] OR teen*[tiab]` | 19,942 | 0/30 |
| Adolescents or school students | 2 | `child*[tiab] OR school*[tiab] OR pupil*[tiab] OR teen*[tiab]` | 3,229 | 0/30 |
| Food-consumption outcome | 1 | `food*[tiab] OR diet*[tiab] OR fruit*[tiab] OR vegetable*[tiab]` | 4,019 | 1/30 |
| Food-consumption outcome | 2 | `food*[tiab] OR diet*[tiab] OR fruit*[tiab] OR vegetable*[tiab]` | 3,801 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 3,299,065 | 0 |
| population | 239,796 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad core blocks plus optional school-setting and food-consumption blocks; no seeds supplied; no limits beyond PubMed entry-date cutoff. |
| 2 | 0 | education: +6 / -6; population: +2 / -2 | none | Corrected controlled-heading quoting after initial lint; kept broad core blocks and optional school-setting and consumption blocks. |
| 3 | 46,796 | limits/combination | none | Corrected strategy combination to the default AND across concept blocks; optional candidates remain separate. |
| 4 | 68,575 | population: +2 / -0 | none | Expanded the population block to include child and child/student wording because eligibility includes school students as well as adolescents; category probe candidate had a school nutrition-policy intervention that justified reviewing this wording. |
| 5 | 67,872 | population: +1 / -1 | none | Added Child MeSH without explosion plus child text word to cover school-age students; preschool-only populations are outside scope. |
| 6 | 67,872 | limits/combination | none | Category probe found an eligible adolescent classroom nutrition curriculum reported as diet habits rather than an explicit food-intake phrase; added it to the relevant set and broadened the consumption candidate block. |
| 7 | 69,329 | education: +3 / -0 | none | terms miss showed that relevant PMID 27782838 described the Boost school curriculum as a multi-component dietary intervention without nutrition education wording; added generic dietary/nutrition/food intervention text terms to recover it. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 7 (Same-context critic: no fresh-context reviewer was available. This internal review is not independent PRESS peer review.): 0 findings; 
- Round 2 on version 7 (Same-context second review round of the same current strategy; no new strategy revisions were indicated by the diagnostic. This is not independent PRESS peer review.): 0 findings; 
- Round 3 on version 7 (Same-context closing review: verified that the current strategy retains both tested optional concepts for screening, all mandatory risk dispositions carry evidence, and no substantive earlier finding remains open. Not independent PRESS peer review.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1422 NCBI requests logged (664 from cache); strategy sha256 cebe57c02772._

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
        "message": "69,329 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:school",
        "blocking": false,
        "requires_review": true,
        "id": "I-e9b19d605f157a6d00b4"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-286908195ce2e073d939"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-0da39503258dbd9b0da8"
      }
    ],
    "issues": [
      {
        "severity": "info",
        "code": "noexp",
        "message": "unexploded MeSH: confirm the narrower descriptors are meant to be excluded",
        "term": "\"Child\"[Mesh:noexp]",
        "block": "population",
        "location": "block:population",
        "blocking": false,
        "requires_review": false,
        "id": "I-b10a0faf7399abe45ea5"
      },
      {
        "code": "over_workload_budget",
        "message": "69,329 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:school",
        "blocking": false,
        "requires_review": true,
        "id": "I-e9b19d605f157a6d00b4"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-286908195ce2e073d939"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-0da39503258dbd9b0da8"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T21:06:04+00:00",
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
      "requested": "Dietetics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T21:06:04+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004046",
          "name": "Dietetics",
          "type": "descriptor",
          "scope_note": "The application of nutritional principles to regulation of the diet and feeding persons or groups of persons.",
          "tree_numbers": [
            "H02.533.290"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004046",
      "preferred_label": "Dietetics",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Dietetics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T21:06:04+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T21:06:04+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T21:06:04+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh:noexp",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Dietetics\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"nutrition educat*\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"diet education\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"nutrition curriculum\"[Title/Abstract] OR \"food and nutrition education\"[Title/Abstract] OR \"nutrition counsel*\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"dietary educat*\"[Title/Abstract] OR \"dietary intervention*\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"food intervention*\"[Title/Abstract]) AND (\"Adolescent\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"adolescent*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth\"[Title/Abstract] OR \"youths\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"Child\"[MeSH Terms:noexp] OR \"child*\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 7,
      "review_sha256": "8c865cba1ef6b1d094c3ecd388d083e12239b47825f9c0057b443360f1ff5509",
      "note": "Same-context critic: no fresh-context reviewer was available. This internal review is not independent PRESS peer review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The AND-ed blocks represent food/nutrition education interventions and adolescents or school students. School delivery and consumption are explicitly tested optional concepts and left for screening because only three relevant records are known. The Child heading is unexploded to avoid preschool indexing."
        },
        "operators": {
          "verdict": "pass",
          "note": "Each concept uses OR synonyms and the two core concepts are AND-ed. No NOT or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Education, dietetics, adolescent, students and child headings provide controlled vocabulary coverage; each core block also has title/abstract terms. Child:noexp has a stated age-scope reason."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Education and intervention wording includes food, nutrition and dietary forms. Population terms include adolescents, youth, students, pupils, schoolchildren and children. The education probe history includes two screened clean probes; one earlier duplicate draw remained unscreened, as disclosed in the audit."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All clauses use explicit PubMed fields and evaluation reported no syntax or translation blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or other search limit is applied. The Entrez-date bound is the requested 2017-12-14 cutoff, not a publication-date filter."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 69,329-record core exceeds the 10,000 standard workload target. Both eligible searchable optional concepts were evaluated and sampled; requiring either alone remains above budget (school 17,425; consumption 9,140), while requiring both in an exploratory pilot count yielded 2,513 but is not justified with only three known relevant records and no adequate safety benchmark. Keep both concepts for screening to protect recall and plan a larger screening workload or additional benchmark development.",
          "evidence": "The current evaluation reports 69,329 core records, with optional-block counts of 17,425 and 9,140, and zero relevant among 30 loss-sample records for each (school sample includes PMID 14836540 without an abstract). The combined school-and-consumption pilot count was 2,513. The workload target is 10,000."
        },
        {
          "issue_id": "I-e9b19d605f157a6d00b4",
          "status": "accepted-risk",
          "response": "The school setting block is left out because the skill requires at least 15 known records before it can be safely required; only three are known. The 30-record loss sample had no clearly eligible record, but one record lacked an abstract. The school term block remains a screening criterion, and the unresolved abstract and underpowered sample remain risks.",
          "evidence": "The evaluation reports 69,329 records without the school block and 17,425 with it, 74.9% reduction, no known loss, and a 0/30 loss sample; PMID 14836540 had no abstract. Related-review discovery, similar-article screening, a neighbor search and a precise pilot count were attempted, but they yielded only three screened relevant records."
        },
        {
          "issue_id": "I-286908195ce2e073d939",
          "status": "accepted-risk",
          "response": "The consumption outcome block is left out because the known set has only three records, below the 15-record safety threshold. No eligible record was found in the current 30-record loss sample. Food consumption remains an eligibility criterion at screening. An earlier category probe did find PMID 8529088, which was added to the relevant set.",
          "evidence": "The evaluation reports 69,329 records without the outcome block and 9,140 with it, 86.8% reduction, no known loss, and 0/30 in the current loss sample. The prior consumption category probe found one relevant record among 30 (PMID 8529088); the second probe found 0/30. Related-review discovery, neighbors and a precise pilot count were tried; no 15-record independent benchmark was available."
        },
        {
          "issue_id": "I-0da39503258dbd9b0da8",
          "status": "accepted-risk",
          "response": "The consumption probe is stale because the education block changed after the last outcome probe and the probe budget is exhausted. The change added generic dietary, nutrition and food intervention phrases to recover a known eligible school study; it did not change the consumption block or the broader query used by the probe. The most recent consumption probe was clean before that change. Accept the residual risk and disclose it for specialist review.",
          "evidence": "The evaluation history shows the education terms were expanded to retrieve PMID 27782838, with no known records lost; consumption probe 2 screened 30 records and found none, while probe 1 found PMID 8529088. The validation warning explicitly identifies the outcome block as stale and the probe budget as spent."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 7,
      "review_sha256": "8c865cba1ef6b1d094c3ecd388d083e12239b47825f9c0057b443360f1ff5509",
      "note": "Same-context second review round of the same current strategy; no new strategy revisions were indicated by the diagnostic. This is not independent PRESS peer review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The AND-ed blocks represent food/nutrition education interventions and adolescents or school students. School delivery and consumption are explicitly tested optional concepts and left for screening because only three relevant records are known. The Child heading is unexploded to avoid preschool indexing."
        },
        "operators": {
          "verdict": "pass",
          "note": "Each concept uses OR synonyms and the two core concepts are AND-ed. No NOT or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Education, dietetics, adolescent, students and child headings provide controlled vocabulary coverage; each core block also has title/abstract terms. Child:noexp has a stated age-scope reason."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Education and intervention wording includes food, nutrition and dietary forms. Population terms include adolescents, youth, students, pupils, schoolchildren and children. The education probe history includes two screened clean probes; one earlier duplicate draw remained unscreened, as disclosed in the audit."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All clauses use explicit PubMed fields and evaluation reported no syntax or translation blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or other search limit is applied. The Entrez-date bound is the requested 2017-12-14 cutoff, not a publication-date filter."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 69,329-record core exceeds the 10,000 standard workload target. Both eligible searchable optional concepts were evaluated and sampled; requiring either alone remains above budget (school 17,425; consumption 9,140), while requiring both in an exploratory pilot count yielded 2,513 but is not justified with only three known relevant records and no adequate safety benchmark. Keep both concepts for screening to protect recall and plan a larger screening workload or additional benchmark development.",
          "evidence": "The current evaluation reports 69,329 core records, with optional-block counts of 17,425 and 9,140, and zero relevant among 30 loss-sample records for each (school sample includes PMID 14836540 without an abstract). The combined school-and-consumption pilot count was 2,513. The workload target is 10,000."
        },
        {
          "issue_id": "I-e9b19d605f157a6d00b4",
          "status": "accepted-risk",
          "response": "The school setting block is left out because the skill requires at least 15 known records before it can be safely required; only three are known. The 30-record loss sample had no clearly eligible record, but one record lacked an abstract. The school term block remains a screening criterion, and the unresolved abstract and underpowered sample remain risks.",
          "evidence": "The evaluation reports 69,329 records without the school block and 17,425 with it, 74.9% reduction, no known loss, and a 0/30 loss sample; PMID 14836540 had no abstract. Related-review discovery, similar-article screening, a neighbor search and a precise pilot count were attempted, but they yielded only three screened relevant records."
        },
        {
          "issue_id": "I-286908195ce2e073d939",
          "status": "accepted-risk",
          "response": "The consumption outcome block is left out because the known set has only three records, below the 15-record safety threshold. No eligible record was found in the current 30-record loss sample. Food consumption remains an eligibility criterion at screening. An earlier category probe did find PMID 8529088, which was added to the relevant set.",
          "evidence": "The evaluation reports 69,329 records without the outcome block and 9,140 with it, 86.8% reduction, no known loss, and 0/30 in the current loss sample. The prior consumption category probe found one relevant record among 30 (PMID 8529088); the second probe found 0/30. Related-review discovery, neighbors and a precise pilot count were tried; no 15-record independent benchmark was available."
        },
        {
          "issue_id": "I-0da39503258dbd9b0da8",
          "status": "accepted-risk",
          "response": "The consumption probe is stale because the education block changed after the last outcome probe and the probe budget is exhausted. The change added generic dietary, nutrition and food intervention phrases to recover a known eligible school study; it did not change the consumption block or the broader query used by the probe. The most recent consumption probe was clean before that change. Accept the residual risk and disclose it for specialist review.",
          "evidence": "The evaluation history shows the education terms were expanded to retrieve PMID 27782838, with no known records lost; consumption probe 2 screened 30 records and found none, while probe 1 found PMID 8529088. The validation warning explicitly identifies the outcome block as stale and the probe budget as spent."
        }
      ]
    },
    {
      "round": 3,
      "strategy_version": 7,
      "review_sha256": "8c865cba1ef6b1d094c3ecd388d083e12239b47825f9c0057b443360f1ff5509",
      "note": "Same-context closing review: verified that the current strategy retains both tested optional concepts for screening, all mandatory risk dispositions carry evidence, and no substantive earlier finding remains open. Not independent PRESS peer review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The AND-ed blocks represent food/nutrition education interventions and adolescents or school students. School delivery and consumption are explicitly tested optional concepts and left for screening because only three relevant records are known. The Child heading is unexploded to avoid preschool indexing."
        },
        "operators": {
          "verdict": "pass",
          "note": "Each concept uses OR synonyms and the two core concepts are AND-ed. No NOT or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Education, dietetics, adolescent, students and child headings provide controlled vocabulary coverage; each core block also has title/abstract terms. Child:noexp has a stated age-scope reason."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Education and intervention wording includes food, nutrition and dietary forms. Population terms include adolescents, youth, students, pupils, schoolchildren and children. The education probe history includes two screened clean probes; one earlier duplicate draw remained unscreened, as disclosed in the audit."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All clauses use explicit PubMed fields and evaluation reported no syntax or translation blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or other search limit is applied. The Entrez-date bound is the requested 2017-12-14 cutoff, not a publication-date filter."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 69,329-record core exceeds the 10,000 standard workload target. Both eligible searchable optional concepts were evaluated and sampled; requiring either alone remains above budget (school 17,425; consumption 9,140), while requiring both in an exploratory pilot count yielded 2,513 but is not justified with only three known relevant records and no adequate safety benchmark. Keep both concepts for screening to protect recall and plan a larger screening workload or additional benchmark development.",
          "evidence": "The current evaluation reports 69,329 core records, with optional-block counts of 17,425 and 9,140, and zero relevant among 30 loss-sample records for each (school sample includes PMID 14836540 without an abstract). The combined school-and-consumption pilot count was 2,513. The workload target is 10,000."
        },
        {
          "issue_id": "I-e9b19d605f157a6d00b4",
          "status": "accepted-risk",
          "response": "The school setting block is left out because the skill requires at least 15 known records before it can be safely required; only three are known. The 30-record loss sample had no clearly eligible record, but one record lacked an abstract. The school term block remains a screening criterion, and the unresolved abstract and underpowered sample remain risks.",
          "evidence": "The evaluation reports 69,329 records without the school block and 17,425 with it, 74.9% reduction, no known loss, and a 0/30 loss sample; PMID 14836540 had no abstract. Related-review discovery, similar-article screening, a neighbor search and a precise pilot count were attempted, but they yielded only three screened relevant records."
        },
        {
          "issue_id": "I-286908195ce2e073d939",
          "status": "accepted-risk",
          "response": "The consumption outcome block is left out because the known set has only three records, below the 15-record safety threshold. No eligible record was found in the current 30-record loss sample. Food consumption remains an eligibility criterion at screening. An earlier category probe did find PMID 8529088, which was added to the relevant set.",
          "evidence": "The evaluation reports 69,329 records without the outcome block and 9,140 with it, 86.8% reduction, no known loss, and 0/30 in the current loss sample. The prior consumption category probe found one relevant record among 30 (PMID 8529088); the second probe found 0/30. Related-review discovery, neighbors and a precise pilot count were tried; no 15-record independent benchmark was available."
        },
        {
          "issue_id": "I-0da39503258dbd9b0da8",
          "status": "accepted-risk",
          "response": "The consumption probe is stale because the education block changed after the last outcome probe and the probe budget is exhausted. The change added generic dietary, nutrition and food intervention phrases to recover a known eligible school study; it did not change the consumption block or the broader query used by the probe. The most recent consumption probe was clean before that change. Accept the residual risk and disclose it for specialist review.",
          "evidence": "The evaluation history shows the education terms were expanded to retrieve PMID 27782838, with no known records lost; consumption probe 2 screened 30 records and found none, while probe 1 found PMID 8529088. The validation warning explicitly identifies the outcome block as stale and the probe budget as spent."
        }
      ],
      "closing": true
    }
  ]
}
```


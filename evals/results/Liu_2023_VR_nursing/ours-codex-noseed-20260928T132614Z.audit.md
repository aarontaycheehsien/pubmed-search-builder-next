# PubMed search strategy: audit

Generated 2026-09-28T13:43:07+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In nursing students, is virtual reality-based teaching more effective than traditional or alternative teaching methods for improving theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking?
- Framework: PICO
- Scope confirmed by user: yes (The user asked to proceed without questions; scope roles are based on the supplied eligibility criteria and the standard-depth default. No known relevant articles were supplied. PubMed is bounded by Entrez date 2023-03-31 (PSB_AS_OF); no publication-date limit is used. Screening budget is the standard default of 10,000. Outcomes are an optional concept to be empirically tested.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Nursing students | search | The specified population is essential to eligibility and is commonly named and indexed in nursing education reports. |
| Virtual reality-based education or training | search | The intervention defines the topic and is commonly named in titles, abstracts, or indexing; include immersive simulation and virtual patients/environments. |
| Learning outcomes | optional | The outcomes define the educational purpose but outcome reporting is inconsistent; test the block before deciding whether to AND it. |
| Traditional or alternative teaching method | screen | Comparator details are inconsistently named in abstracts. |
| Randomized or controlled comparative educational intervention | screen | Design labels and control status are inconsistently reported; no ad hoc design filter. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T13:42:26+00:00
- Records added to PubMed up to: 2023-03-31
- Total records: 3,197
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Students, Nursing"[Mesh]` | 30,313 | none |
| 2 | `"Education, Nursing"[Mesh]` | 89,264 | none |
| 3 | `nursing student*[tiab]` | 20,313 | none |
| 4 | `student nurse*[tiab]` | 4,452 | none |
| 5 | `nurs* student*[tiab]` | 20,650 | none |
| 6 | `nursing undergraduate*[tiab]` | 445 | none |
| 7 | `undergraduate nursing[tiab]` | 4,289 | none |
| 8 | `nursing graduate*[tiab]` | 576 | none |
| 9 | `nursing education[tiab]` | 17,158 | none |
| 10 | `prelicensure nurs*[tiab]` | 382 | none |
| 11 | `pre-registration nurs*[tiab]` | 683 | none |
| 12 | `pre registration nurs*[tiab]` | 683 | none |
| 13 | `postgraduate nurs*[tiab]` | 238 | none |
| 14 | `post-graduate nurs*[tiab]` | 35 | none |
| 15 | `post graduate nurs*[tiab]` | 35 | none |
| 16 | `postgraduate student*[tiab]` | 1,078 | none |
| 17 | `graduate nursing student*[tiab]` | 415 | none |
| 18 | `doctoral nursing student*[tiab]` | 37 | none |
| 19 | `postgraduat*[tiab]` | 24,557 | none |
| 20 | `post-graduat*[tiab]` | 4,460 | none |
| 21 | `post graduat*[tiab]` | 4,460 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 134,032 | none |
| 23 | `"Virtual Reality"[Mesh]` | 5,646 | none |
| 24 | `"Simulation Training"[Mesh]` | 11,657 | none |
| 25 | `"Computer Simulation"[Mesh]` | 292,562 | none |
| 26 | `virtual realit*[tiab]` | 16,450 | none |
| 27 | `virtual simulation*[tiab]` | 896 | none |
| 28 | `immersive simulation*[tiab]` | 136 | none |
| 29 | `immersive technolog*[tiab]` | 160 | none |
| 30 | `virtual patient*[tiab]` | 1,492 | none |
| 31 | `virtual environment*[tiab]` | 4,386 | none |
| 32 | `virtual world*[tiab]` | 1,003 | none |
| 33 | `computer simulation*[tiab]` | 26,958 | none |
| 34 | `computer-based simulation*[tiab]` | 331 | none |
| 35 | `computer based simulation*[tiab]` | 331 | none |
| 36 | `web-based simulation*[tiab]` | 64 | none |
| 37 | `web based simulation*[tiab]` | 64 | none |
| 38 | `3D simulation*[tiab]` | 720 | none |
| 39 | `three-dimensional simulation*[tiab]` | 633 | none |
| 40 | `augmented realit*[tiab]` | 4,124 | none |
| 41 | `mixed realit*[tiab]` | 833 | none |
| 42 | `game-based virtual realit*[tiab]` | 21 | none |
| 43 | `virtual gaming simulation*[tiab]` | 5 | none |
| 44 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43` | 334,301 | none |
| 45 | `#22 AND #44` | 3,197 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Students, Nursing"[Mesh] OR "Education, Nursing"[Mesh] OR nursing student*[tiab] OR student nurse*[tiab] OR nurs* student*[tiab] OR nursing undergraduate*[tiab] OR undergraduate nursing[tiab] OR nursing graduate*[tiab] OR nursing education[tiab] OR prelicensure nurs*[tiab] OR pre-registration nurs*[tiab] OR pre registration nurs*[tiab] OR postgraduate nurs*[tiab] OR post-graduate nurs*[tiab] OR post graduate nurs*[tiab] OR postgraduate student*[tiab] OR graduate nursing student*[tiab] OR doctoral nursing student*[tiab] OR postgraduat*[tiab] OR post-graduat*[tiab] OR post graduat*[tiab]) AND ("Virtual Reality"[Mesh] OR "Simulation Training"[Mesh] OR "Computer Simulation"[Mesh] OR virtual realit*[tiab] OR virtual simulation*[tiab] OR immersive simulation*[tiab] OR immersive technolog*[tiab] OR virtual patient*[tiab] OR virtual environment*[tiab] OR virtual world*[tiab] OR computer simulation*[tiab] OR computer-based simulation*[tiab] OR computer based simulation*[tiab] OR web-based simulation*[tiab] OR web based simulation*[tiab] OR 3D simulation*[tiab] OR three-dimensional simulation*[tiab] OR augmented realit*[tiab] OR mixed realit*[tiab] OR game-based virtual realit*[tiab] OR virtual gaming simulation*[tiab])) AND ("1800/01/01"[edat] : "2023/03/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Learning outcomes | left out | 3,197 / 2,527 | 21.0% | none | 0/30 (up to 10% of removed records could be relevant) | After adding standalone postgraduate terms, the outcomes block removes 670 of 3,197 records (21.0%), below the material-reduction threshold. None of 30 sampled losses met the review population, virtual intervention, controlled comparison, and outcome criteria together; the closest comparative virtual-reality record involved non-nursing students. Outcomes remain for screening to preserve recall when they are not named in records. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nursing_students | 334,301 | 0 |
| virtual_reality | 134,032 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,622 | initial | none | Initial recall-first draft: AND nursing-student/nursing-education and virtual-reality/simulation concepts; test the listed learning outcomes as an optional block. Concepts and eligibility were set from the question before review discovery; two clearly eligible primary studies screened from a relevant review's references were added as development records. |
| 2 | 2,638 | nursing_students: +6 / -0 | none | Added explicit postgraduate and doctoral nursing-student text terms to address critic finding R1-01; eligibility already includes postgraduate nursing students. Terms are OR additions within the existing population block. |
| 3 | 3,197 | nursing_students: +3 / -0 | none | Added standalone postgraduate/post-graduate text stems to the nursing-student block to complete the subgroup coverage required by critic finding R1-01; the earlier nursing-qualified variants remain. OR additions retain the prior records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; R1-01 must-fix open
- Round 2 on version 2: 1 findings; R1-01 must-fix open
- Round 3 on version 3: 1 findings; R1-01 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 618 NCBI requests logged (319 from cache); strategy sha256 970f30056f7b._

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
      "requested": "Students, Nursing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:42:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013338",
          "name": "Students, Nursing",
          "type": "descriptor",
          "scope_note": "Individuals enrolled in a school of nursing or a formal educational program leading to a degree in nursing.",
          "tree_numbers": [
            "M01.848.769.685"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013338",
      "preferred_label": "Students, Nursing",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Students, Nursing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Education, Nursing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:42:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004506",
          "name": "Education, Nursing",
          "type": "descriptor",
          "scope_note": "Use for general articles concerning nursing education.",
          "tree_numbers": [
            "I02.358.462"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004506",
      "preferred_label": "Education, Nursing",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Education, Nursing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Virtual Reality",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:42:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000076142",
          "name": "Virtual Reality",
          "type": "descriptor",
          "scope_note": "Using computer technology to create and maintain an environment and project a user's physical presence in that environment allowing the user to interact with it.",
          "tree_numbers": [
            "L01.224.160.875",
            "L01.296.555"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000076142",
      "preferred_label": "Virtual Reality",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "\"Virtual Reality\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Simulation Training",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:42:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000066908",
          "name": "Simulation Training",
          "type": "descriptor",
          "scope_note": "A highly customized interactive medium or program that allows individuals to learn and practice real world activities in an accurate, realistic, safe and secure environment.",
          "tree_numbers": [
            "I02.903.847"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000066908",
      "preferred_label": "Simulation Training",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "\"Simulation Training\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer Simulation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:42:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003198",
          "name": "Computer Simulation",
          "type": "descriptor",
          "scope_note": "Computer-based representation of physical systems and phenomena such as chemical processes.",
          "tree_numbers": [
            "L01.224.160"
          ],
          "entry_terms": 21,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003198",
      "preferred_label": "Computer Simulation",
      "type": "descriptor",
      "location": "vocabulary:24",
      "term": {
        "text": "\"Computer Simulation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"students, nursing\"[MeSH Terms] OR \"education, nursing\"[MeSH Terms] OR \"nursing student*\"[Title/Abstract] OR \"student nurse*\"[Title/Abstract] OR \"nurs* student*\"[Title/Abstract] OR \"nursing undergraduate*\"[Title/Abstract] OR \"undergraduate nursing\"[Title/Abstract] OR \"nursing graduate*\"[Title/Abstract] OR \"nursing education\"[Title/Abstract] OR \"prelicensure nurs*\"[Title/Abstract] OR \"pre registration nurs*\"[Title/Abstract] OR \"pre registration nurs*\"[Title/Abstract] OR \"postgraduate nurs*\"[Title/Abstract] OR \"post graduate nurs*\"[Title/Abstract] OR \"post graduate nurs*\"[Title/Abstract] OR \"postgraduate student*\"[Title/Abstract] OR \"graduate nursing student*\"[Title/Abstract] OR \"doctoral nursing student*\"[Title/Abstract] OR \"postgraduat*\"[Title/Abstract] OR \"post graduat*\"[Title/Abstract] OR \"post graduat*\"[Title/Abstract]) AND (\"Virtual Reality\"[MeSH Terms] OR \"Simulation Training\"[MeSH Terms] OR \"Computer Simulation\"[MeSH Terms] OR \"virtual realit*\"[Title/Abstract] OR \"virtual simulation*\"[Title/Abstract] OR \"immersive simulation*\"[Title/Abstract] OR \"immersive technolog*\"[Title/Abstract] OR \"virtual patient*\"[Title/Abstract] OR \"virtual environment*\"[Title/Abstract] OR \"virtual world*\"[Title/Abstract] OR \"computer simulation*\"[Title/Abstract] OR \"computer based simulation*\"[Title/Abstract] OR \"computer based simulation*\"[Title/Abstract] OR \"web based simulation*\"[Title/Abstract] OR \"web based simulation*\"[Title/Abstract] OR \"3d simulation*\"[Title/Abstract] OR \"three dimensional simulation*\"[Title/Abstract] OR \"augmented realit*\"[Title/Abstract] OR \"mixed realit*\"[Title/Abstract] OR \"game based virtual realit*\"[Title/Abstract] OR \"virtual gaming simulation*\"[Title/Abstract]) AND 1800/01/01:2023/03/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "3dc43fb2c87fe8eadf502677bb8bd2e64a4624c48fdd99df80ed246864c76f03",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility criteria include postgraduate nursing education, but the nursing-student block has no clear standalone text-word coverage for postgraduate/post-graduate. 'nursing graduate*' may refer to nursing graduates and does not reliably represent postgraduate education."
        },
        "operators": {
          "verdict": "pass",
          "note": "The population and intervention blocks are OR-combined internally and AND-combined; the optional outcome block is left out as documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The draft includes nursing student and nursing education headings, plus virtual reality and simulation headings. The broad headings may add screening noise, but no heading error is evident from the packet."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add explicit coverage for the postgraduate eligibility subgroup. The existing undergraduate and pre-registration wording is represented, but postgraduate nursing students are not clearly captured."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query is balanced and combines the blocks and entry-date range coherently. The packet reports no query errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or outcome filter is applied. The entry-date cutoff is documented as the intended as-of boundary, and no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes postgraduate nursing education, but the nursing-student block lacks clear coverage for postgraduate/post-graduate nursing students. 'nursing graduate*' is not an unambiguous equivalent and may retrieve nursing graduates rather than students in postgraduate education.",
          "recommendation": "Add tested text-word expressions that cover the postgraduate subgroup, including standalone postgraduate/post-graduate wording as well as relevant nursing-student variants, and rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "f58ce1048246af8722a6b26d68a5f140034368168e6497154eade014256d987e",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The added postgraduate nursing and postgraduate student terms improve coverage, but the packet’s translation check calls for the named subgroup to be covered by its own bare name. The terms remain qualified by 'nurs*' or 'student*'; the earlier recommendation for standalone postgraduate wording is not fully met."
        },
        "operators": {
          "verdict": "pass",
          "note": "The population and intervention terms are OR-combined within blocks and the blocks are AND-combined. The optional outcome block is left out with a documented test and rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the nursing student, nursing education, virtual reality, simulation training, and computer simulation headings. The simulation headings are broad, but no heading error is established by the packet."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Postgraduate variants were added, but the earlier finding requested standalone postgraduate/post-graduate wording as well as nursing-student variants. The current terms still qualify those words with 'nurs*' or 'student*'."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query is balanced, block combinations and the entry-date range are coherent, and the packet reports no query errors, translation issues, or PubMed warning diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or outcome filter is applied. The entry-date cutoff is documented as the intended as-of boundary, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes postgraduate nursing education. Although the revised block adds postgraduate nursing and postgraduate student variants, it still lacks standalone postgraduate/post-graduate wording as requested in the prior finding and required by the packet’s translation check.",
          "recommendation": "Add tested standalone postgraduate/post-graduate text-word expressions alongside the nursing-student variants, then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "771319fbaa1c146a7e5c236b3ef13889d556e4e224d02bb5510a2bffd0d54cf4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The population block now includes standalone postgraduate, post-graduate, and post graduate text-word expressions, addressing the earlier coverage gap. The packet reports a complete current evaluation and retrieval of both known relevant records."
        },
        "operators": {
          "verdict": "pass",
          "note": "Population and intervention terms are OR-combined within blocks and the blocks are AND-combined. The optional outcomes block was tested and left out with a documented rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes nursing student and nursing education headings, plus virtual reality and simulation headings. The packet establishes no heading error."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes undergraduate and pre-registration wording and standalone postgraduate variants, alongside nursing and student subgroup terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is balanced and combines the blocks with the documented entry-date range. The packet reports no query errors, translation issues, or PubMed warning diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or outcome filter is applied. The entry-date cutoff is documented as the intended as-of boundary, and no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes postgraduate nursing education. Earlier versions lacked standalone postgraduate/post-graduate wording.",
          "recommendation": "Add tested standalone postgraduate/post-graduate text-word expressions alongside nursing-student variants, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current nursing-students block includes standalone postgraduat*[tiab], post-graduat*[tiab], and post graduat*[tiab], in addition to nursing and student subgroup variants. The packet reports the current complete evaluation, no translation issues, and retrieval of both known relevant records."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


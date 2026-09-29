# PubMed search strategy: audit

Generated 2026-09-28T22:11:44+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In nursing students, is virtual reality-based teaching more effective than traditional or alternative teaching methods for improving theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking?
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions. Scope roles were set from the question and eligibility criteria. Workload budget is the standard default of 10,000. No known relevant articles were supplied. PubMed retrieval is bounded by Entrez date 2023-03-31 via PSB_AS_OF; no publication-date limit is used. No language or study-design limits.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Nursing students in nursing education programmes | search | The review is restricted to nursing students; the population is identifiable in titles, abstracts and indexing. Undergraduate, pre-registration and postgraduate programmes are included. |
| Virtual reality, immersive simulation, virtual patients or environments used for education | search | This is the defining intervention. Terms may be named as members (for example, virtual patient or immersive simulation) without the broad label virtual reality, so it is treated as a category and probed. |
| Knowledge, practical/clinical skills, retention, satisfaction, self-efficacy or critical thinking | screen | Outcomes are inconsistently reported and are eligibility criteria, not necessary retrieval terms. |
| Traditional/conventional or alternative instructional method | screen | Comparators are inconsistently described; screen for a controlled comparison. |
| Randomized or controlled comparative educational intervention | screen | Educational designs are inconsistently indexed; no unvalidated design block is imposed. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:10:52+00:00
- Records added to PubMed up to: 2023-03-31
- Total records: 2,645
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Students, Nursing"[Mesh]` | 30,313 | none |
| 2 | `"Education, Nursing"[Mesh]` | 89,264 | none |
| 3 | `"Education, Nursing, Baccalaureate"[Mesh]` | 21,150 | none |
| 4 | `"Education, Nursing, Associate"[Mesh]` | 1,778 | none |
| 5 | `"Education, Nursing, Diploma Programs"[Mesh]` | 3,550 | none |
| 6 | `"Education, Nursing, Graduate"[Mesh]` | 8,386 | none |
| 7 | `nursing student*[tiab]` | 20,313 | none |
| 8 | `student nurse*[tiab]` | 4,452 | none |
| 9 | `students of nursing[tiab]` | 234 | none |
| 10 | `nursing undergraduate*[tiab]` | 445 | none |
| 11 | `undergraduate nursing[tiab]` | 4,289 | none |
| 12 | `pre-registration nursing[tiab]` | 526 | none |
| 13 | `preregistration nursing[tiab]` | 117 | none |
| 14 | `nursing education[tiab]` | 17,158 | none |
| 15 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14` | 109,365 | none |
| 16 | `"Virtual Reality"[Mesh]` | 5,646 | none |
| 17 | `"Simulation Training"[Mesh]` | 11,657 | none |
| 18 | `"High Fidelity Simulation Training"[Mesh]` | 386 | none |
| 19 | `"Computer Simulation"[Mesh]` | 292,562 | none |
| 20 | `virtual realit*[tiab]` | 16,450 | none |
| 21 | `VR[tiab]` | 12,192 | none |
| 22 | `immersive simulat*[tiab]` | 136 | none |
| 23 | `virtual simulat*[tiab]` | 1,077 | none |
| 24 | `virtual patient*[tiab]` | 1,492 | none |
| 25 | `virtual environment*[tiab]` | 4,386 | none |
| 26 | `virtual world*[tiab]` | 1,003 | none |
| 27 | `computer simulat*[tiab]` | 28,280 | none |
| 28 | `3D simulat*[tiab]` | 791 | none |
| 29 | `three-dimensional simulat*[tiab]` | 666 | none |
| 30 | `head-mounted display*[tiab]` | 1,487 | none |
| 31 | `head mounted display*[tiab]` | 1,487 | none |
| 32 | `immersive learning[tiab]` | 80 | none |
| 33 | `serious game*[tiab]` | 1,346 | none |
| 34 | `virtual gam* simulat*[tiab]` | 5 | none |
| 35 | `#16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 339,900 | none |
| 36 | `#15 AND #35` | 2,645 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Students, Nursing"[Mesh] OR "Education, Nursing"[Mesh] OR "Education, Nursing, Baccalaureate"[Mesh] OR "Education, Nursing, Associate"[Mesh] OR "Education, Nursing, Diploma Programs"[Mesh] OR "Education, Nursing, Graduate"[Mesh] OR nursing student*[tiab] OR student nurse*[tiab] OR students of nursing[tiab] OR nursing undergraduate*[tiab] OR undergraduate nursing[tiab] OR pre-registration nursing[tiab] OR preregistration nursing[tiab] OR nursing education[tiab]) AND ("Virtual Reality"[Mesh] OR "Simulation Training"[Mesh] OR "High Fidelity Simulation Training"[Mesh] OR "Computer Simulation"[Mesh] OR virtual realit*[tiab] OR VR[tiab] OR immersive simulat*[tiab] OR virtual simulat*[tiab] OR virtual patient*[tiab] OR virtual environment*[tiab] OR virtual world*[tiab] OR computer simulat*[tiab] OR 3D simulat*[tiab] OR three-dimensional simulat*[tiab] OR head-mounted display*[tiab] OR head mounted display*[tiab] OR immersive learning[tiab] OR serious game*[tiab] OR virtual gam* simulat*[tiab])) AND ("1800/01/01"[edat] : "2023/03/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 23 | 23 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Virtual reality, immersive simulation, virtual patients or environments used for education | 1 | `serious game*[tiab] OR avatar*[tiab] OR computer game*[tiab] OR digital patient*[tiab]` | 55 | 1/30 |
| Virtual reality, immersive simulation, virtual patients or environments used for education | 2 | `serious game*[tiab] OR avatar*[tiab] OR computer game*[tiab] OR digital patient*[tiab]` | 16 | 0/16 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nursing_students | 339,900 | 0 |
| virtual_teaching | 109,365 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial PICO draft: AND nursing students and VR/virtual teaching; screen comparator, learning outcomes, and controlled design because these are inconsistently named. Added MeSH and text-word layers for each searched concept. No seeds supplied. |
| 2 | 2,624 | nursing_students: +15 / -0; virtual_teaching: +17 / -0 | none | Corrected the strategy file to the skill schema. Initial search uses only nursing-student and virtual-teaching blocks; comparator, outcomes and design remain screening criteria. |
| 3 | 2,606 | nursing_students: +0 / -1 | none | Removed 'student of nursing[tiab]' after live translation showed All Fields fallback; the construction is redundant with 'students of nursing[tiab]' and student nurse/nursing student terms. |
| 4 | 2,645 | virtual_teaching: +2 / -0 | none | Category probe identified a controlled nursing-student study using serious-game simulated patient cases and online lectures (PMID 34812778); added serious game and virtual gaming simulation variants to improve category-member recall. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 0 findings; 
- Round 2 on version 4: 0 findings; 
- Round 3 on version 4: 1 findings; R3-DOC-1 document open

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 796 NCBI requests logged (566 from cache); strategy sha256 463de4e03448._

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
      "checked_at": "2026-09-28T22:10:52+00:00",
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
      "checked_at": "2026-09-28T22:10:52+00:00",
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
      "requested": "Education, Nursing, Baccalaureate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004508",
          "name": "Education, Nursing, Baccalaureate",
          "type": "descriptor",
          "scope_note": "A four-year program in nursing education in a college or university leading to a B.S.N. (Bachelor of Science in Nursing). Graduates are eligible for state examination for licensure as RN (Registered Nurse).",
          "tree_numbers": [
            "I02.358.462.316"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004508",
      "preferred_label": "Education, Nursing, Baccalaureate",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Education, Nursing, Baccalaureate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Education, Nursing, Associate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004507",
          "name": "Education, Nursing, Associate",
          "type": "descriptor",
          "scope_note": "A two-year program in nursing education in a community or junior college leading to an A.D. (Associate Degree). Graduates of this program are eligible for state examination for licensure as RN (Registered Nurse).",
          "tree_numbers": [
            "I02.358.462.233"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004507",
      "preferred_label": "Education, Nursing, Associate",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Education, Nursing, Associate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Education, Nursing, Diploma Programs",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004510",
          "name": "Education, Nursing, Diploma Programs",
          "type": "descriptor",
          "scope_note": "Programs usually offered in hospital schools of nursing leading to a registered nurse diploma (RN). Graduates are eligible for state examination for licensure as RN (Registered Nurse).",
          "tree_numbers": [
            "I02.358.462.482"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004510",
      "preferred_label": "Education, Nursing, Diploma Programs",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "\"Education, Nursing, Diploma Programs\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Education, Nursing, Graduate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004511",
          "name": "Education, Nursing, Graduate",
          "type": "descriptor",
          "scope_note": "Those educational activities engaged in by holders of a bachelor's degree in nursing, which are primarily designed to prepare them for entrance into a specific field of nursing, and may lead to board certification or a more advanced degree.",
          "tree_numbers": [
            "I02.358.337.450",
            "I02.358.462.565"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004511",
      "preferred_label": "Education, Nursing, Graduate",
      "type": "descriptor",
      "location": "vocabulary:6",
      "term": {
        "text": "\"Education, Nursing, Graduate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Virtual Reality",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Virtual Reality\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Simulation Training",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Simulation Training\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High Fidelity Simulation Training",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000070856",
          "name": "High Fidelity Simulation Training",
          "type": "descriptor",
          "scope_note": "A controlled learning environment that closely represents reality.",
          "tree_numbers": [
            "I02.903.847.250"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000070856",
      "preferred_label": "High Fidelity Simulation Training",
      "type": "descriptor",
      "location": "vocabulary:17",
      "term": {
        "text": "\"High Fidelity Simulation Training\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer Simulation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:10:52+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Computer Simulation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"students, nursing\"[MeSH Terms] OR \"education, nursing\"[MeSH Terms] OR \"education, nursing, baccalaureate\"[MeSH Terms] OR \"education, nursing, associate\"[MeSH Terms] OR \"education, nursing, diploma programs\"[MeSH Terms] OR \"education, nursing, graduate\"[MeSH Terms] OR \"nursing student*\"[Title/Abstract] OR \"student nurse*\"[Title/Abstract] OR \"students of nursing\"[Title/Abstract] OR \"nursing undergraduate*\"[Title/Abstract] OR \"undergraduate nursing\"[Title/Abstract] OR \"pre registration nursing\"[Title/Abstract] OR \"preregistration nursing\"[Title/Abstract] OR \"nursing education\"[Title/Abstract]) AND (\"Virtual Reality\"[MeSH Terms] OR \"Simulation Training\"[MeSH Terms] OR \"High Fidelity Simulation Training\"[MeSH Terms] OR \"Computer Simulation\"[MeSH Terms] OR \"virtual realit*\"[Title/Abstract] OR \"VR\"[Title/Abstract] OR \"immersive simulat*\"[Title/Abstract] OR \"virtual simulat*\"[Title/Abstract] OR \"virtual patient*\"[Title/Abstract] OR \"virtual environment*\"[Title/Abstract] OR \"virtual world*\"[Title/Abstract] OR \"computer simulat*\"[Title/Abstract] OR \"3d simulat*\"[Title/Abstract] OR \"three dimensional simulat*\"[Title/Abstract] OR \"head mounted display*\"[Title/Abstract] OR \"head mounted display*\"[Title/Abstract] OR \"immersive learning\"[Title/Abstract] OR \"serious game*\"[Title/Abstract] OR \"virtual gam* simulat*\"[Title/Abstract]) AND 1800/01/01:2023/03/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "d7e1c0540c4382c70a621cf2680bcf23b6e8cf937fb8de33ce88c77df7098277",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translations preserve the intended fields and Boolean structure; the population and intervention members named in scope are represented, including graduate nursing education, immersive simulation, virtual patients, and virtual environments."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each searched concept and AND combines the population and intervention blocks. Outcomes, comparators, and study design remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the nursing education, nursing student, virtual reality, simulation training, high-fidelity simulation, and computer simulation headings as verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word set covers the named population and intervention terminology. The serious-game wording is retained with a documented relevant probe record; broader game, avatar, and digital-patient terms were probed and not added."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query has no reported syntax errors, translation issues, or lint findings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or design limits are imposed. The entry-date boundary is documented as the intended as-of date, with no publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "081a1a66157a0dd9daec9d6812fe21fbdf73431c91a9c7a4aa440fc7a6a07d38",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks cover the population and intervention members named in the scope, including graduate nursing education, immersive simulation, virtual patients, and virtual environments. No process-direction terms require expansion."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines terms within each concept and AND combines the searched population and intervention blocks. Outcomes, comparators, and design remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the nursing student, nursing education, virtual reality, simulation training, high-fidelity simulation, and computer simulation headings as verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover the named population and intervention terminology. The serious-game term has a documented relevant probe record; the broader game, avatar, and digital-patient terms were probed and not added."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported complete query has no syntax errors, translation issues, or lint findings. No proximity expressions or non-null phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or study-design limits are imposed. The entry-date boundary is documented as the intended as-of date, and no publication-date limit is used."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "081a1a66157a0dd9daec9d6812fe21fbdf73431c91a9c7a4aa440fc7a6a07d38",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The population and intervention terms represent the named concepts, including graduate nursing education, immersive simulation, virtual patients, and virtual environments. No process-direction terms require expansion."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each searched block and AND combines the population and intervention blocks. Outcomes, comparators, and design remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the nursing student, nursing education, virtual reality, simulation training, high-fidelity simulation, and computer simulation headings as verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover the named population and intervention terminology. The serious-game term has a documented relevant probe record, and the broader game, avatar, and digital-patient terms were probed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query has no reported syntax errors, translation issues, or lint findings. No proximity expressions or unresolved phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or study-design limits are imposed. The entry-date boundary is documented as the intended as-of date, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R3-DOC-1",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "finding": "The review question names knowledge, practical skills, skill retention, satisfaction, and critical thinking, while the eligibility criteria also include self-efficacy. This makes the stated question and inclusion scope differ.",
          "recommendation": "Clarify whether self-efficacy is an eligible outcome and align the question and eligibility wording in the protocol.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-28T22:58:15+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In nursing students, is virtual reality-based teaching more effective than traditional or alternative teaching methods for improving theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking?
- Framework: PICO
- Scope confirmed by user: no (User asked not to pause for questions; scope and assumptions were set from the review question and criteria. No known relevant articles were supplied. PubMed is bounded by Entrez date through 2023-03-31 via PSB_AS_OF; no publication-date limit is used. Comparator and controlled design are screened. Learning outcomes are optional and will be empirically tested. Scope confirmation was not obtained because the user asked to proceed without questions.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Nursing students | search | Every eligible record concerns students in a nursing education programme; nursing students and closely related student-nurse terms are searchable in title, abstract, and MeSH. |
| Virtual reality-based education, immersive simulation, or virtual patient/environment | search | The intervention block directly searches the named modalities (virtual reality, virtual simulation, virtual patient/environment, and immersive simulation). Two screened probes of generic simulation records found no eligible member-only record, so this is treated as an enumerated intervention concept rather than an umbrella-only category. |
| Learning outcomes | optional | Outcomes define the topic and may be named, but are inconsistently reported in abstracts; test a comprehensive outcome block before deciding whether to AND it. |
| Traditional/conventional or alternative instructional comparator | screen | Comparator wording is inconsistent and may be reported only in full text; determine at screening. |
| Randomized or controlled comparative educational intervention | screen | Avoid an unvalidated ad hoc study-design filter; judge controlled comparative design at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:57:17+00:00
- Records added to PubMed up to: 2023-03-31
- Total records: 5,426
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
| 7 | `"nursing student*"[tiab]` | 20,313 | none |
| 8 | `"student nurse*"[tiab]` | 4,452 | none |
| 9 | `"nurse student*"[tiab]` | 361 | none |
| 10 | `prelicensure[tiab]` | 1,201 | none |
| 11 | `pre-licensure[tiab]` | 450 | none |
| 12 | `preregistration[tiab]` | 2,685 | none |
| 13 | `pre-registration[tiab]` | 1,977 | none |
| 14 | `undergraduate nursing[tiab]` | 4,289 | none |
| 15 | `graduate nursing student*[tiab]` | 415 | none |
| 16 | `postgraduate[tiab]` | 23,443 | none |
| 17 | `post-graduate[tiab]` | 3,897 | none |
| 18 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 131,667 | none |
| 19 | `"Virtual Reality"[Mesh]` | 5,646 | none |
| 20 | `"Simulation Training"[Mesh]` | 11,657 | none |
| 21 | `"Computer-Assisted Instruction"[Mesh]` | 12,551 | none |
| 22 | `"Computer Simulation"[Mesh]` | 292,562 | none |
| 23 | `virtual realit*[tiab]` | 16,450 | none |
| 24 | `VR[tiab]` | 12,192 | none |
| 25 | `IVR[tiab]` | 1,911 | none |
| 26 | `immersive[tiab]` | 4,177 | none |
| 27 | `virtual simulat*[tiab]` | 1,077 | none |
| 28 | `virtual patient*[tiab]` | 1,492 | none |
| 29 | `virtual environment*[tiab]` | 4,386 | none |
| 30 | `virtual world*[tiab]` | 1,003 | none |
| 31 | `computer simulat*[tiab]` | 28,280 | none |
| 32 | `computer-based simulat*[tiab]` | 413 | none |
| 33 | `computer based simulat*[tiab]` | 413 | none |
| 34 | `web-based simulat*[tiab]` | 74 | none |
| 35 | `web based simulat*[tiab]` | 74 | none |
| 36 | `screen-based simulat*[tiab]` | 48 | none |
| 37 | `screen based simulat*[tiab]` | 48 | none |
| 38 | `game-based virtual[tiab]` | 27 | none |
| 39 | `simulated patient*[tiab]` | 2,924 | none |
| 40 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 352,384 | none |
| 41 | `#18 AND #40` | 5,426 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Students, Nursing"[Mesh] OR "Education, Nursing"[Mesh] OR "Education, Nursing, Baccalaureate"[Mesh] OR "Education, Nursing, Associate"[Mesh] OR "Education, Nursing, Diploma Programs"[Mesh] OR "Education, Nursing, Graduate"[Mesh] OR "nursing student*"[tiab] OR "student nurse*"[tiab] OR "nurse student*"[tiab] OR prelicensure[tiab] OR pre-licensure[tiab] OR preregistration[tiab] OR pre-registration[tiab] OR undergraduate nursing[tiab] OR graduate nursing student*[tiab] OR postgraduate[tiab] OR post-graduate[tiab]) AND ("Virtual Reality"[Mesh] OR "Simulation Training"[Mesh] OR "Computer-Assisted Instruction"[Mesh] OR "Computer Simulation"[Mesh] OR virtual realit*[tiab] OR VR[tiab] OR IVR[tiab] OR immersive[tiab] OR virtual simulat*[tiab] OR virtual patient*[tiab] OR virtual environment*[tiab] OR virtual world*[tiab] OR computer simulat*[tiab] OR computer-based simulat*[tiab] OR computer based simulat*[tiab] OR web-based simulat*[tiab] OR web based simulat*[tiab] OR screen-based simulat*[tiab] OR screen based simulat*[tiab] OR game-based virtual[tiab] OR simulated patient*[tiab])) AND ("1800/01/01"[edat] : "2023/03/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| discovered | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Learning outcomes | left out | 5,426 / 3,962 | 27.0% | none | 0/30 (up to 10% of removed records could be relevant) | After refreshing against the current population and intervention blocks, the outcome block reduced the query by 27.0%, below the approximately 30% materiality guideline. It lost none of the 14 known relevant records and the refreshed 30-record loss sample found no eligible study, but the two-block search remains below the 10,000-record workload budget. Given the review's recall-first priority and the limited power of a 30-record loss sample, leave outcomes out of the required query. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nursing_students | 352,384 | 0 |
| virtual_reality_education | 131,667 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 4,620 | initial | none | First complete two-block draft built from MeSH authority records, full review criteria vocabulary, and screened relevant studies discovered through citations of on-topic systematic reviews. Outcomes are tested as an optional block; comparison and design stay at screening. |
| 2 | 3,214 | learning_outcomes: +23 / -0 | none | Added the learning-outcome block after it reduced the query by 30.4%, lost none of four development records, and had no relevant records in the 30-record loss sample; query scope otherwise unchanged. |
| 3 | 3,265 | learning_outcomes: +2 / -0 | none | Added outcome terms performance and learning effectiveness after terms miss showed these were the wording of two eligible development records; both records now counted in the outcome block. The two screened category probes supported treating the explicitly enumerated intervention modalities as non-category; scope confirmation remains unobtained as user asked not to pause. |
| 4 | 3,962 | nursing_students: +2 / -0 | none | Resolved the internal critic's must-fix by adding explicit unhyphenated and hyphenated postgraduate text-word terms because eligibility includes postgraduate nursing students. |
| 5 | 5,426 | learning_outcomes: +0 / -25 | none | Refreshed the optional outcome assessment after the postgraduate population terms changed. The current block reduced the query by 27.0%, below the approximate 30% guideline; its 30-record loss sample found no eligible records, and the core two-block search remains under the workload budget, so outcomes were left out to protect recall. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-01 must-fix open
- Round 2 on version 4: 2 findings; R1-01 must-fix resolved, R2-01 should-fix open
- Round 3 on version 5: 2 findings; R1-01 must-fix resolved, R2-01 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1305 NCBI requests logged (709 from cache); strategy sha256 20d603fea1d3._

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
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Virtual Reality\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Simulation Training",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Simulation Training\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer-Assisted Instruction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:57:17+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003194",
          "name": "Computer-Assisted Instruction",
          "type": "descriptor",
          "scope_note": "A self-learning technique, usually online, involving interaction of the student with programmed instructional materials.",
          "tree_numbers": [
            "I02.903.771.500.208"
          ],
          "entry_terms": 14,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003194",
      "preferred_label": "Computer-Assisted Instruction",
      "type": "descriptor",
      "location": "vocabulary:20",
      "term": {
        "text": "\"Computer-Assisted Instruction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer Simulation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:57:17+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Computer Simulation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"students, nursing\"[MeSH Terms] OR \"education, nursing\"[MeSH Terms] OR \"education, nursing, baccalaureate\"[MeSH Terms] OR \"education, nursing, associate\"[MeSH Terms] OR \"education, nursing, diploma programs\"[MeSH Terms] OR \"education, nursing, graduate\"[MeSH Terms] OR \"nursing student*\"[Title/Abstract] OR \"student nurse*\"[Title/Abstract] OR \"nurse student*\"[Title/Abstract] OR \"prelicensure\"[Title/Abstract] OR \"pre-licensure\"[Title/Abstract] OR \"preregistration\"[Title/Abstract] OR \"pre-registration\"[Title/Abstract] OR \"undergraduate nursing\"[Title/Abstract] OR \"graduate nursing student*\"[Title/Abstract] OR \"postgraduate\"[Title/Abstract] OR \"post-graduate\"[Title/Abstract]) AND (\"Virtual Reality\"[MeSH Terms] OR \"Simulation Training\"[MeSH Terms] OR \"Computer-Assisted Instruction\"[MeSH Terms] OR \"Computer Simulation\"[MeSH Terms] OR \"virtual realit*\"[Title/Abstract] OR \"VR\"[Title/Abstract] OR \"IVR\"[Title/Abstract] OR \"immersive\"[Title/Abstract] OR \"virtual simulat*\"[Title/Abstract] OR \"virtual patient*\"[Title/Abstract] OR \"virtual environment*\"[Title/Abstract] OR \"virtual world*\"[Title/Abstract] OR \"computer simulat*\"[Title/Abstract] OR \"computer based simulat*\"[Title/Abstract] OR \"computer based simulat*\"[Title/Abstract] OR \"web based simulat*\"[Title/Abstract] OR \"web based simulat*\"[Title/Abstract] OR \"screen based simulat*\"[Title/Abstract] OR \"screen based simulat*\"[Title/Abstract] OR \"game based virtual\"[Title/Abstract] OR \"simulated patient*\"[Title/Abstract]) AND 1800/01/01:2023/03/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "ae2b4e18d7fd4357635a54665527474b8ee96606944e14dbae87cecde2e921c3",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility criteria include postgraduate nursing students, but the text-word terms do not explicitly search postgraduate or post-graduate. The graduate nursing MeSH heading may not retrieve unindexed records."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks use OR internally and are combined with AND. The outcome block was empirically tested, with its recall and remaining risk documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The nursing education and student headings, virtual reality heading, and simulation-related headings are relevant to the stated concepts."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add explicit text-word coverage for postgraduate nursing students, including the hyphenated form."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translation has no errors or warnings, and the field tags and Boolean structure are coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or comparator filter is applied. The entry-date boundary is documented and matches the stated as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include postgraduate nursing education programmes, but the nursing-student block has no explicit postgraduate or post-graduate text-word term. The graduate nursing education MeSH heading may not cover unindexed records or records that use postgraduate wording.",
          "recommendation": "Add explicit text-word coverage for postgraduate and post-graduate, such as postgraduate[tiab] OR post-graduate[tiab], and evaluate the revised complete strategy.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "3b847f64878f3e6243ec4c1786d515d9497cd3deb2a724e3e71aa679b70ee5de",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The blocks cover the searched concepts named in scope. The student block now includes postgraduate[tiab] and post-graduate[tiab], and the packet reports 100% retrieval of all 14 known relevant records."
        },
        "operators": {
          "verdict": "revise",
          "note": "The OR-within-block and AND-between-block structure is clear, but the optional outcomes decision is marked stale. Its table reports a 27.0% reduction, while the rationale claims 29.3%; the packet does not establish a current optional-block evaluation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed nursing education, virtual reality, simulation, computer-assisted instruction, and learning outcome headings are relevant to the stated concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words address the named participant, intervention, and outcome concepts, including both postgraduate forms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translation has no errors or warnings, and the field tags, Boolean grouping, and date boundary are coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date boundary is stated and matches the as-of date. Comparator and controlled-design wording are appropriately left for screening."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include postgraduate nursing education programmes, but the nursing-student block has no explicit postgraduate or post-graduate text-word term.",
          "recommendation": "Add postgraduate[tiab] and post-graduate[tiab], then evaluate the revised complete strategy.",
          "status": "resolved",
          "response": "Both requested terms are present in the current nursing-student block. The packet reports 14 of 14 known relevant records retrieved, 100% recall for each known set, no misses, and no regression from the previous version."
        },
        {
          "id": "R2-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The learning-outcomes optional-block assessment is marked stale, and its reported reduction conflicts with the rationale: the table reports 27.0%, while the rationale claims 29.3%.",
          "recommendation": "Refresh the optional-block evaluation and align the reported counts, reduction, fingerprint, and decision rationale before relying on the AND decision.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "3e5f461d1c5dccd21272a75f38bfe2e508715be92a2e44515c487182c1b9d2b4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility criteria include postgraduate nursing students, and the current nursing-student block includes both postgraduate[tiab] and post-graduate[tiab]. The packet reports retrieval of all 14 known relevant records."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required query combines the nursing-student and intervention OR blocks with AND. The learning-outcomes block is left out after a refreshed evaluation: 5,426 records without it versus 3,962 with it, a 27.0% reduction; no known records lost and 0 of 30 sampled removed records relevant. The decision rationale, counts, fingerprint, and current status are aligned."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet lists relevant nursing education and student headings and virtual reality, simulation, computer-assisted instruction, and computer simulation headings. It reports the checked intervention headings as verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The participant terms include both postgraduate forms; intervention text words cover the stated virtual reality, immersive simulation, and virtual patient/environment modalities. Outcome terms were tested as an optional block and are omitted from the recall-first required query."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translation has no errors or warnings, and the field tags, Boolean grouping, and entry-date boundary are coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No comparator or study-design filter is applied; both are screened as specified. The entry-date boundary is documented through 2023-03-31, matching the stated as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include postgraduate nursing education programmes, but the nursing-student block previously lacked explicit postgraduate or post-graduate text-word terms.",
          "recommendation": "Add postgraduate[tiab] and post-graduate[tiab], then evaluate the revised complete strategy.",
          "status": "resolved",
          "response": "Both requested terms are present in the current nursing-student block. The packet reports that all 14 known relevant records are retrieved, with no misses."
        },
        {
          "id": "R2-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The learning-outcomes optional-block assessment was previously marked stale, and the reported reduction conflicted with its rationale.",
          "recommendation": "Refresh the optional-block evaluation and align its counts, reduction, fingerprint, and decision rationale.",
          "status": "resolved",
          "response": "The current evaluation is marked current and uses fingerprint 9012ecffda29c4da. It reports 5,426 records without the block and 3,962 with it, a 27.0% reduction, no known relevant records lost, and 0 of 30 sampled removed records relevant. The decision rationale matches these results and leaves outcomes out of the required query."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


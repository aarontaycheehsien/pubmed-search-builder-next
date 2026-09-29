# PubMed search strategy: audit

Generated 2026-09-28T22:26:35+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In nursing students, is virtual reality-based teaching more effective than traditional or alternative teaching methods for improving theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking?
- Framework: PICO
- Scope confirmed by user: yes (User requested no follow-up questions; scope and roles are proceeding on reasonable assumptions. Standard depth; no known relevant articles and no screening budget or language/date limits supplied. No publication-date limit. PubMed records are bounded by Entrez date through 2023-03-31 using PSB_AS_OF. Comparator, outcome and controlled-design eligibility are screened rather than required search blocks.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Nursing students in a nursing education programme | search | The target population is essential and commonly named/indexed; probe for eligible records naming only a member such as undergraduate nursing students. |
| Virtual reality-based education, immersive simulation, or virtual patient/environment | search | The defining intervention is essential and searchable, but includes named modalities such as virtual patients and simulation; probe records that may name only these members. |
| Traditional or alternative teaching method | screen | Comparators are inconsistently described in title/abstract; assess at screening. |
| Knowledge, skills, retention, satisfaction, self-efficacy, or critical thinking | screen | Outcomes are inconsistently reported in abstracts; do not require an outcome block. |
| Randomized or other controlled comparative educational intervention | screen | Study design labels are inconsistently reported and ad hoc design terms risk recall; assess at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:25:58+00:00
- Records added to PubMed up to: 2023-03-31
- Total records: 4,555
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Students, Nursing"[Mesh]` | 30,313 | none |
| 2 | `"Education, Nursing"[Mesh]` | 89,264 | none |
| 3 | `"Education, Nursing, Baccalaureate"[Mesh]` | 21,150 | none |
| 4 | `"Education, Nursing, Graduate"[Mesh]` | 8,386 | none |
| 5 | `nursing student*[tiab]` | 20,313 | none |
| 6 | `student nurse*[tiab]` | 4,452 | none |
| 7 | `nurs*[tiab] AND student*[tiab]` | 43,479 | none |
| 8 | `prelicensure[tiab]` | 1,201 | none |
| 9 | `pre-licensure[tiab]` | 450 | none |
| 10 | `undergraduate nursing[tiab]` | 4,289 | none |
| 11 | `postgraduate nursing[tiab]` | 197 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 117,449 | none |
| 13 | `"Virtual Reality"[Mesh]` | 5,646 | none |
| 14 | `"Simulation Training"[Mesh]` | 11,657 | none |
| 15 | `"Computer-Assisted Instruction"[Mesh]` | 12,551 | none |
| 16 | `virtual reality[tiab]` | 16,425 | none |
| 17 | `virtual-reality[tiab]` | 16,425 | none |
| 18 | `VR[tiab]` | 12,192 | none |
| 19 | `virtual simulation*[tiab]` | 896 | none |
| 20 | `virtual patient*[tiab]` | 1,492 | none |
| 21 | `virtual environment*[tiab]` | 4,386 | none |
| 22 | `virtual world*[tiab]` | 1,003 | none |
| 23 | `immersive simulation*[tiab]` | 136 | none |
| 24 | `immersive virtual reality[tiab]` | 1,138 | none |
| 25 | `immersive technolog*[tiab]` | 160 | none |
| 26 | `computer-based simulation*[tiab]` | 331 | none |
| 27 | `computer based simulation*[tiab]` | 331 | none |
| 28 | `screen-based simulation*[tiab]` | 37 | none |
| 29 | `web-based virtual simulation*[tiab]` | 2 | none |
| 30 | `3D virtual[tiab]` | 1,078 | none |
| 31 | `three-dimensional virtual[tiab]` | 511 | none |
| 32 | `head-mounted display*[tiab]` | 1,487 | none |
| 33 | `mixed reality[tiab]` | 830 | none |
| 34 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 52,664 | none |
| 35 | `#12 AND #34` | 4,555 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Students, Nursing"[Mesh] OR "Education, Nursing"[Mesh] OR "Education, Nursing, Baccalaureate"[Mesh] OR "Education, Nursing, Graduate"[Mesh] OR nursing student*[tiab] OR student nurse*[tiab] OR (nurs*[tiab] AND student*[tiab]) OR prelicensure[tiab] OR pre-licensure[tiab] OR undergraduate nursing[tiab] OR postgraduate nursing[tiab]) AND ("Virtual Reality"[Mesh] OR "Simulation Training"[Mesh] OR "Computer-Assisted Instruction"[Mesh] OR virtual reality[tiab] OR virtual-reality[tiab] OR VR[tiab] OR virtual simulation*[tiab] OR virtual patient*[tiab] OR virtual environment*[tiab] OR virtual world*[tiab] OR immersive simulation*[tiab] OR immersive virtual reality[tiab] OR immersive technolog*[tiab] OR computer-based simulation*[tiab] OR computer based simulation*[tiab] OR screen-based simulation*[tiab] OR web-based virtual simulation*[tiab] OR 3D virtual[tiab] OR three-dimensional virtual[tiab] OR head-mounted display*[tiab] OR mixed reality[tiab])) AND ("1800/01/01"[edat] : "2023/03/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Nursing students in a nursing education programme | 1 | `nurs*[tiab] OR Nursing[Mesh] OR Education, Nursing[Mesh]` | 1,612 | 0/30 |
| Nursing students in a nursing education programme | 2 | `nurs*[tiab] OR Nursing[Mesh] OR Education, Nursing[Mesh]` | 1,595 | 0/30 |
| Virtual reality-based education, immersive simulation, or virtual patient/environment | 1 | `virtual*[tiab] OR simulation*[tiab] OR Simulation Training[Mesh] OR Computer Simulation[Mesh]` | 2,565 | 0/30 |
| Virtual reality-based education, immersive simulation, or virtual patient/environment | 2 | `virtual*[tiab] OR simulation*[tiab] OR Simulation Training[Mesh] OR Computer Simulation[Mesh]` | 2,577 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nursing_students | 52,664 | 0 |
| virtual_teaching | 117,449 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 4,573 | initial | none | Initial two-block search and screened relevant studies. |
| 2 | 4,555 | virtual_teaching: +0 / -1 | none | Removed standalone augmented reality because it extends beyond the stated virtual reality, immersive simulation, or virtual patient/environment intervention; retained mixed reality as a possible immersive environment. Re-evaluated against the three screened development records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 454 NCBI requests logged (181 from cache); strategy sha256 dbb53df566f3._

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
      "checked_at": "2026-09-28T22:25:58+00:00",
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
      "checked_at": "2026-09-28T22:25:58+00:00",
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
      "checked_at": "2026-09-28T22:25:58+00:00",
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
      "requested": "Education, Nursing, Graduate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:25:58+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Education, Nursing, Graduate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Virtual Reality",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:25:58+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Virtual Reality\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Simulation Training",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:25:58+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "\"Simulation Training\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer-Assisted Instruction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:25:58+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Computer-Assisted Instruction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"students, nursing\"[MeSH Terms] OR \"education, nursing\"[MeSH Terms] OR \"education, nursing, baccalaureate\"[MeSH Terms] OR \"education, nursing, graduate\"[MeSH Terms] OR \"nursing student*\"[Title/Abstract] OR \"student nurse*\"[Title/Abstract] OR (\"nurs*\"[Title/Abstract] AND \"student*\"[Title/Abstract]) OR \"prelicensure\"[Title/Abstract] OR \"pre-licensure\"[Title/Abstract] OR \"undergraduate nursing\"[Title/Abstract] OR \"postgraduate nursing\"[Title/Abstract]) AND (\"virtual reality\"[MeSH Terms] OR \"Simulation Training\"[MeSH Terms] OR \"Computer-Assisted Instruction\"[MeSH Terms] OR \"virtual reality\"[Title/Abstract] OR \"virtual reality\"[Title/Abstract] OR \"VR\"[Title/Abstract] OR \"virtual simulation*\"[Title/Abstract] OR \"virtual patient*\"[Title/Abstract] OR \"virtual environment*\"[Title/Abstract] OR \"virtual world*\"[Title/Abstract] OR \"immersive simulation*\"[Title/Abstract] OR \"immersive virtual reality\"[Title/Abstract] OR \"immersive technolog*\"[Title/Abstract] OR \"computer based simulation*\"[Title/Abstract] OR \"computer based simulation*\"[Title/Abstract] OR \"screen based simulation*\"[Title/Abstract] OR \"web based virtual simulation*\"[Title/Abstract] OR \"3d virtual\"[Title/Abstract] OR \"three dimensional virtual\"[Title/Abstract] OR \"head mounted display*\"[Title/Abstract] OR \"mixed reality\"[Title/Abstract]) AND 1800/01/01:2023/03/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "58555ef8b9d0d197abf0e1de403aec9b4092449e79e93a401089aae573acd391",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The displayed PubMed translation matches the intended MeSH and title/abstract concepts; diagnostics report no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "The nursing and virtual-teaching concept blocks are OR-combined and then AND-combined. Parentheses preserve the intended logic; no proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed nursing education/student and virtual reality, simulation training, and computer-assisted instruction headings are verified in the packet and fit the searched concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover nursing students and the named virtual teaching modalities, including virtual patients and environments. Comparator, outcome, and design concepts are appropriately screened rather than required search blocks."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The numbered searches and combined strategy show valid field tags and Boolean syntax; the packet reports no query errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, or other eligibility filter is applied. The Entrez date bound through 2023-03-31 is disclosed and should be reported as the retrieval cutoff."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


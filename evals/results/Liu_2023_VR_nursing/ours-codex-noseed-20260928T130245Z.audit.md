# PubMed search strategy: audit

Generated 2026-09-28T13:25:02+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In nursing students, is virtual reality-based teaching more effective than traditional or alternative teaching methods for improving theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking?
- Framework: PICO
- Scope confirmed by user: no (The user requested that the run proceed without questions, so scope was not confirmed interactively. Assumed the question is intervention effectiveness (PICO): AND nursing students with virtual reality/immersive virtual teaching; outcomes, comparator, and controlled design are screening criteria. The question sentence lists five outcomes, while the user-supplied eligibility criteria additionally lists self-efficacy; eligibility follows the explicit criteria and includes self-efficacy. No date, language, age, or study-design search limit. No known relevant records supplied. PubMed records are bounded by Entrez date through 2023-03-31 using PSB_AS_OF; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Nursing students in nursing education programmes | search | The review is explicitly limited to learners enrolled in nursing education; nursing students and student nurses are searchable population labels. |
| Virtual reality-based teaching, immersive simulation, and virtual patients or environments | search | The educational technology defines the intervention. Because eligible immersive or virtual-patient/environment teaching may be indexed or described broadly, Simulation Training, Computer Simulation, and Computer-Assisted Instruction are retained as recall adjuncts; the final count remains under the 10,000-record standard workload budget, and their non-virtual instructional noise is handled at screening. |
| Knowledge, practical or clinical skills, skill retention, satisfaction, self-efficacy, and critical thinking | screen | These outcomes are broad and inconsistently reported; requiring an outcome block risks missing comparative education studies. |
| Traditional/conventional or alternative instructional method | screen | Comparator wording is inconsistently stated in titles and abstracts. |
| Randomized or otherwise controlled comparative educational intervention | screen | The eligibility criterion includes non-randomized controlled studies; no design block is required for the topic search, and an RCT-only validated filter would be too narrow. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T13:24:21+00:00
- Records added to PubMed up to: 2023-03-31
- Total records: 4,937
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Students, Nursing"[Mesh]` | 30,313 | none |
| 2 | `"Education, Nursing"[Mesh]` | 89,264 | none |
| 3 | `"Education, Nursing, Graduate"[Mesh]` | 8,386 | none |
| 4 | `nursing student*[tiab]` | 20,313 | none |
| 5 | `student nurse*[tiab]` | 4,452 | none |
| 6 | `nurse student*[tiab]` | 361 | none |
| 7 | `undergraduate nursing student*[tiab]` | 2,822 | none |
| 8 | `pre-registration nursing student*[tiab]` | 220 | none |
| 9 | `prelicensure nursing student*[tiab]` | 216 | none |
| 10 | `nurs*[tiab] AND student*[tiab]` | 43,479 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 116,971 | none |
| 12 | `"Virtual Reality"[Mesh]` | 5,646 | none |
| 13 | `"Simulation Training"[Mesh]` | 11,657 | none |
| 14 | `"Computer Simulation"[Mesh]` | 292,562 | none |
| 15 | `"Computer-Assisted Instruction"[Mesh]` | 12,551 | none |
| 16 | `"virtual reality"[tiab]` | 16,425 | none |
| 17 | `"virtual reality simulation"[tiab]` | 559 | none |
| 18 | `"VR simulation"[tiab]` | 355 | none |
| 19 | `"virtual simulation"[tiab]` | 795 | none |
| 20 | `"virtual patient*"[tiab]` | 1,492 | none |
| 21 | `"virtual environment*"[tiab]` | 4,386 | none |
| 22 | `"virtual world*"[tiab]` | 1,003 | none |
| 23 | `"immersive simulation"[tiab]` | 118 | none |
| 24 | `"immersive virtual reality"[tiab]` | 1,138 | none |
| 25 | `"immersive virtual environment*"[tiab]` | 336 | none |
| 26 | `"computer-based simulation"[tiab]` | 236 | none |
| 27 | `"computer based simulation"[tiab]` | 236 | none |
| 28 | `"computerized simulation"[tiab]` | 125 | none |
| 29 | `"computerised simulation"[tiab]` | 10 | none |
| 30 | `"virtual gaming simulation"[tiab]` | 4 | none |
| 31 | `"second life"[tiab]` | 338 | none |
| 32 | `"high-fidelity simulation"[tiab]` | 1,301 | none |
| 33 | `"high fidelity simulation"[tiab]` | 1,301 | none |
| 34 | `virtual[tiab] AND simulation[tiab]` | 10,649 | none |
| 35 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 330,754 | none |
| 36 | `#11 AND #35` | 4,937 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Students, Nursing"[Mesh] OR "Education, Nursing"[Mesh] OR "Education, Nursing, Graduate"[Mesh] OR nursing student*[tiab] OR student nurse*[tiab] OR nurse student*[tiab] OR undergraduate nursing student*[tiab] OR pre-registration nursing student*[tiab] OR prelicensure nursing student*[tiab] OR (nurs*[tiab] AND student*[tiab])) AND ("Virtual Reality"[Mesh] OR "Simulation Training"[Mesh] OR "Computer Simulation"[Mesh] OR "Computer-Assisted Instruction"[Mesh] OR "virtual reality"[tiab] OR "virtual reality simulation"[tiab] OR "VR simulation"[tiab] OR "virtual simulation"[tiab] OR "virtual patient*"[tiab] OR "virtual environment*"[tiab] OR "virtual world*"[tiab] OR "immersive simulation"[tiab] OR "immersive virtual reality"[tiab] OR "immersive virtual environment*"[tiab] OR "computer-based simulation"[tiab] OR "computer based simulation"[tiab] OR "computerized simulation"[tiab] OR "computerised simulation"[tiab] OR "virtual gaming simulation"[tiab] OR "second life"[tiab] OR "high-fidelity simulation"[tiab] OR "high fidelity simulation"[tiab] OR (virtual[tiab] AND simulation[tiab]))) AND ("1800/01/01"[edat] : "2023/03/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 5 | 5 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nursing_students | 330,754 | 0 |
| virtual_reality_education | 116,971 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 4,937 | initial | none | Initial two-block population and virtual/immersive teaching strategy; no user seeds. Benchmark records screened from systematic review references. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 2 findings; R1-F1 should-fix open, R1-F2 should-fix open
- Round 2 on version 1: 2 findings; R1-F1 should-fix resolved, R1-F2 should-fix accepted-risk
- Round 3 on version 1: 2 findings; R1-F1 should-fix resolved, R1-F2 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 531 NCBI requests logged (227 from cache); strategy sha256 4c3fbe9b8be8._

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
      "checked_at": "2026-09-28T13:24:21+00:00",
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
      "checked_at": "2026-09-28T13:24:21+00:00",
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
      "requested": "Education, Nursing, Graduate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:24:21+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Education, Nursing, Graduate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Virtual Reality",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:24:21+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Virtual Reality\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Simulation Training",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:24:21+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Simulation Training\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer Simulation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:24:21+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "\"Computer Simulation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer-Assisted Instruction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:24:21+00:00",
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
  "translation": "(\"students, nursing\"[MeSH Terms] OR \"education, nursing\"[MeSH Terms] OR \"education, nursing, graduate\"[MeSH Terms] OR \"nursing student*\"[Title/Abstract] OR \"student nurse*\"[Title/Abstract] OR \"nurse student*\"[Title/Abstract] OR \"undergraduate nursing student*\"[Title/Abstract] OR \"pre registration nursing student*\"[Title/Abstract] OR \"prelicensure nursing student*\"[Title/Abstract] OR (\"nurs*\"[Title/Abstract] AND \"student*\"[Title/Abstract])) AND (\"Virtual Reality\"[MeSH Terms] OR \"Simulation Training\"[MeSH Terms] OR \"Computer Simulation\"[MeSH Terms] OR \"Computer-Assisted Instruction\"[MeSH Terms] OR \"Virtual Reality\"[Title/Abstract] OR \"virtual reality simulation\"[Title/Abstract] OR \"VR simulation\"[Title/Abstract] OR \"virtual simulation\"[Title/Abstract] OR \"virtual patient*\"[Title/Abstract] OR \"virtual environment*\"[Title/Abstract] OR \"virtual world*\"[Title/Abstract] OR \"immersive simulation\"[Title/Abstract] OR \"immersive virtual reality\"[Title/Abstract] OR \"immersive virtual environment*\"[Title/Abstract] OR \"computer-based simulation\"[Title/Abstract] OR \"computer-based simulation\"[Title/Abstract] OR \"computerized simulation\"[Title/Abstract] OR \"computerised simulation\"[Title/Abstract] OR \"virtual gaming simulation\"[Title/Abstract] OR \"second life\"[Title/Abstract] OR \"high-fidelity simulation\"[Title/Abstract] OR \"high-fidelity simulation\"[Title/Abstract] OR (\"virtual\"[Title/Abstract] AND \"simulation\"[Title/Abstract])) AND 1800/01/01:2023/03/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "a7521a07d59f9023d83214aa17fa4f818dab6d19dc9fb49365aeeaaf34e473ac",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility criteria explicitly include self-efficacy although the question sentence does not; protocol notes will state that the user-supplied eligibility list governs and that this is an intended outcome."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searched concept blocks are ANDed and each block's alternatives are ORed; outcomes, comparator, and design are handled at screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH headings are verified and the Boolean structure is valid."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Broad simulation and computer-assisted terms may retrieve non-virtual interventions; the protocol and narrative will document their recall rationale and noise risk."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or translation errors were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or design limits were applied; the Entrez-date bound is documented."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The question names theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking. The eligibility criteria also accept self-efficacy, which expands the review outcome scope without a stated rationale.",
          "recommendation": "Align eligibility with the question’s named outcomes, or explicitly document self-efficacy as an intended scope extension.",
          "status": "open",
          "response": ""
        },
        {
          "id": "R1-F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The intervention block includes generic headings for Simulation Training, Computer Simulation, and Computer-Assisted Instruction, plus high-fidelity simulation phrases. These can retrieve non-virtual simulation or instruction, and the packet does not explain why that broader scope is intended.",
          "recommendation": "Document why these broad terms are needed for the stated virtual/immersive intervention scope, or revise the term set and complete another full evaluation of counts and benchmark retrieval.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 1,
      "review_sha256": "24a0da25bb8eb5db0cd51582649d950defa054a2d255d403ea8dcac82a7a506c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The protocol now explicitly explains that the user-supplied eligibility list governs and includes self-efficacy."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searched concept blocks are combined with AND, and outcomes, comparator, and design remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed headings are verified in the packet and the Boolean structure is valid."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The protocol documents the broad simulation headings as recall adjuncts, acknowledges their non-virtual noise, and reports a 4,937-record set within the 10,000-record workload budget."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The combined query is parenthesized correctly and has no reported translation errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or design limits are applied; the Entrez-date bound is documented as the intended as-of cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The question names theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking. The eligibility criteria also accept self-efficacy, which expands the review outcome scope without a stated rationale.",
          "recommendation": "Align eligibility with the question’s named outcomes, or explicitly document self-efficacy as an intended scope extension.",
          "status": "resolved",
          "response": "The protocol notes that the user-supplied eligibility criteria include self-efficacy and that eligibility follows those explicit criteria."
        },
        {
          "id": "R1-F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The intervention block includes generic headings for Simulation Training, Computer Simulation, and Computer-Assisted Instruction, plus high-fidelity simulation phrases. These can retrieve non-virtual simulation or instruction, and the packet does not explain why that broader scope is intended.",
          "recommendation": "Document why these broad terms are needed for the stated virtual/immersive intervention scope, or revise the term set and complete another full evaluation of counts and benchmark retrieval.",
          "status": "accepted-risk",
          "response": "The protocol now identifies the broad headings as recall adjuncts for eligible immersive or virtual-patient/environment teaching that may be indexed broadly, acknowledges non-virtual noise at screening, and reports a 4,937-record set below the 10,000-record workload budget. The packet does not show term-level contribution to benchmark retrieval, so the breadth remains a documented sensitivity/precision tradeoff."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 1,
      "review_sha256": "24a0da25bb8eb5db0cd51582649d950defa054a2d255d403ea8dcac82a7a506c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The protocol explains that eligibility follows the user-supplied criteria, including self-efficacy."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searched concept blocks are combined with AND, with alternatives combined using OR; outcomes, comparator, and design remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the listed MeSH headings, and the Boolean structure is valid."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The protocol documents broad simulation headings as recall adjuncts, acknowledges screening noise, and reports a 4,937-record set within the workload budget. This accepts the documented sensitivity/precision tradeoff."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is parenthesized correctly and has no reported translation errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or design filters are applied; the Entrez-date bound is documented as the as-of cutoff. Validation reports five external benchmark records and two development records."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The question names theoretical knowledge, practical skills, skill retention, satisfaction, and critical thinking. The eligibility criteria also accept self-efficacy, which expands the review outcome scope without a stated rationale.",
          "recommendation": "Align eligibility with the question’s named outcomes, or explicitly document self-efficacy as an intended scope extension.",
          "status": "resolved",
          "response": "The protocol notes that the user-supplied eligibility criteria include self-efficacy and that eligibility follows those explicit criteria."
        },
        {
          "id": "R1-F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The intervention block includes generic headings for Simulation Training, Computer Simulation, and Computer-Assisted Instruction, plus high-fidelity simulation phrases. These can retrieve non-virtual simulation or instruction, and the packet does not explain why that broader scope is intended.",
          "recommendation": "Document why these broad terms are needed for the stated virtual/immersive intervention scope, or revise the term set and complete another full evaluation of counts and benchmark retrieval.",
          "status": "accepted-risk",
          "response": "The protocol identifies broad simulation headings as recall adjuncts for eligible immersive or virtual-patient/environment teaching that may be indexed broadly, acknowledges non-virtual noise at screening, and reports a 4,937-record set below the workload budget. The breadth remains a documented sensitivity/precision tradeoff."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


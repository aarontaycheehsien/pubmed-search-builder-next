# PubMed search strategy: audit

Generated 2026-10-01T11:46:45+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / longitudinal course
- Scope confirmed by user: no (No known relevant articles supplied. User asked to proceed without clarification; roles and inclusion of both diagnosed PTSD and symptom-level post-traumatic stress are working assumptions. PubMed records are bounded by Entrez date 2016-01-24 via PSB_AS_OF; no publication-date limit. Standard-depth candidate-screening budget approximately 150 records.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and post-traumatic stress symptoms | search | The review is defined by post-traumatic stress; diagnosed PTSD and symptom-level post-traumatic stress are both in scope and are named/indexed as a condition. |
| Symptom trajectories, longitudinal course, and change patterns | optional | This defines the topic, but eligible studies may report course or repeated symptom measurements without using trajectory terminology; test as an optional block before deciding. |
| Traumatic event and participant context | screen | Trauma is intrinsic to the target condition and event details or population may be inconsistently named; screen eligibility rather than require another block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:46:28+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,255
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Stress Disorders, Post-Traumatic[Mesh]` | 25,369 | none |
| 2 | `post-traumatic stress disorder[tiab]` | 7,081 | none |
| 3 | `post traumatic stress disorder[tiab]` | 7,081 | none |
| 4 | `posttraumatic stress disorder[tiab]` | 12,500 | none |
| 5 | `PTSD[tiab]` | 15,732 | none |
| 6 | `post-traumatic stress symptom*[tiab]` | 474 | none |
| 7 | `post traumatic stress symptom*[tiab]` | 474 | none |
| 8 | `posttraumatic stress symptom*[tiab]` | 1,177 | none |
| 9 | `post-traumatic stress[tiab]` | 8,160 | none |
| 10 | `post traumatic stress[tiab]` | 8,160 | none |
| 11 | `posttraumatic stress[tiab]` | 14,174 | none |
| 12 | `PTSS[tiab]` | 510 | none |
| 13 | `traumatic stress symptom*[tiab]` | 626 | none |
| 14 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 32,255 | none |

### Strategy (single line, for copying into PubMed)

```text
((Stress Disorders, Post-Traumatic[Mesh] OR post-traumatic stress disorder[tiab] OR post traumatic stress disorder[tiab] OR posttraumatic stress disorder[tiab] OR PTSD[tiab] OR post-traumatic stress symptom*[tiab] OR post traumatic stress symptom*[tiab] OR posttraumatic stress symptom*[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab] OR posttraumatic stress[tiab] OR PTSS[tiab] OR traumatic stress symptom*[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 23 | 23 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories, longitudinal course, and change patterns | left out | 32,255 / 8,099 | 74.9% | 18629750 | 0/30 (up to 10% of removed records could be relevant) | Leave out after testing. The block would reduce the PTSD search from 32,255 to 8,099 records (74.9%) but would lose the clearly eligible PTSD symptom-course study PMID 18629750; the screened loss sample found no eligible record among 30. The one known loss outweighs the reduction in screening burden for a recall-first review. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,255 | initial | none | Initial PTSD concept with the trajectory/course block held as an optional candidate; terms built from MeSH and screened relevant records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 0 findings; 
- Round 2 on version 1: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 395 NCBI requests logged (127 from cache); strategy sha256 c45bce8fa7c7._

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
        "message": "32,255 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "32,255 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:46:28+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013313",
          "name": "Stress Disorders, Post-Traumatic",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders with symptoms that last more than one month.",
          "tree_numbers": [
            "F03.950.750.500"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013313",
      "preferred_label": "Stress Disorders, Post-Traumatic",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Stress Disorders, Post-Traumatic",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"posttraumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"traumatic stress symptom*\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "00df2556e50c6ee5a506ad0110fdad27c4e8beffb5c5f71645752fe44c9576d8",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues. The PTSD MeSH heading is verified, and the text terms are translated with the intended title/abstract fields."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD terms are combined with OR, preserving retrieval by any listed condition or symptom expression. The tested trajectory block was left out after it lost known eligible PMID 18629750; AND-ing it would violate the packet's rule."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Stress Disorders, Post-Traumatic[Mesh] is verified in the packet, and free-text terms also cover diagnosed PTSD and symptom-level post-traumatic stress."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Terms cover PTSD, PTSS, post-traumatic stress disorder, and symptom wording with hyphenated, spaced, and closed forms. The packet's translation checks are satisfied by the listed bare terms and variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or PubMed translation issues. The block query is a valid OR combination, with the entry-date cutoff applied separately."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "There are no publication-date or study-design limits. The entry-date cutoff is documented as an as-of boundary. The trauma context is explicitly assigned to screening, consistent with the scope rationale."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the over-budget screening workload for this recall-first review. The optional trajectory block was tested and would reduce results by 74.9%, but it loses a known eligible study; the packet's rules permit leaving it out.",
          "evidence": "The PTSD search returns 32,255 records against a 10,000-record budget. The trajectory block reduces this to 8,099 but loses PMID 18629750. The loss sample found 0 relevant records among 30, while the known lost study is eligible. The trauma context is deliberately assigned to screening because event and population details may be inconsistently named."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 1,
      "review_sha256": "00df2556e50c6ee5a506ad0110fdad27c4e8beffb5c5f71645752fe44c9576d8",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No translation issues are reported; the PTSD heading and title/abstract terms translate as intended."
        },
        "operators": {
          "verdict": "pass",
          "note": "PTSD and symptom terms are OR-combined. The optional trajectory block remains left out after testing because it loses known eligible PMID 18629750; the packet's rule does not permit AND-ing it."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD MeSH heading is verified in the packet, alongside free-text coverage for diagnosed PTSD and post-traumatic stress symptoms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Terms cover PTSD, PTSS, symptom wording, and hyphenated, spaced, and closed forms. The listed bare terms satisfy the packet's translation checks."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or PubMed translation issues; the PTSD block is a valid OR combination with the entry-date boundary applied separately."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or study-design limits are applied. The entry-date boundary is documented as an as-of boundary, and trauma context is assigned to screening."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the over-budget screening workload for this recall-first review. The tested trajectory block loses a known eligible study, so leaving it out is supported by the packet's rules.",
          "evidence": "The PTSD search returns 32,255 records against a 10,000-record budget. The optional trajectory block reduces results to 8,099 but loses PMID 18629750; the loss sample found 0 relevant records among 30. Trauma context is explicitly assigned to screening."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-30T15:43:31+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis / longitudinal symptom course
- Scope confirmed by user: yes (User asked to proceed without questions. Assumed all ages, all trauma types, all languages, and all study designs reporting repeated post-event PTSD symptom course are eligible; no geographic or publication-date limit. Scope treats PTSD/post-traumatic stress symptoms as the condition/outcome domain, with longitudinal trajectory terminology tested as optional. No known relevant articles were supplied. PubMed records are bounded by Entrez date 2016-01-24 via PSB_AS_OF; no [dp] limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and post-traumatic stress symptoms | search | The disorder/symptom domain defines the review topic and is expected to be named in titles, abstracts, or indexing. |
| Symptom trajectories and longitudinal course | optional | Trajectory is topic-defining and often searchable, but relevant papers may describe repeated symptom courses without using this label; test as an optional AND block. |
| Traumatic event exposure | screen | PTSD inherently involves traumatic exposure, and the review accepts all event types; requiring an additional event block would duplicate the defining diagnosis and risk losing PTSD course studies whose abstracts do not restate the event. Screen event and post-event timing at full text. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T15:43:14+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,074
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Stress Disorders, Post-Traumatic[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `posttraumatic stress disorder*[tiab]` | 12,654 | none |
| 4 | `post-traumatic stress disorder*[tiab]` | 7,263 | none |
| 5 | `post traumatic stress disorder*[tiab]` | 7,263 | none |
| 6 | `posttraumatic stress symptom*[tiab]` | 1,177 | none |
| 7 | `post-traumatic stress symptom*[tiab]` | 474 | none |
| 8 | `post traumatic stress symptom*[tiab]` | 474 | none |
| 9 | `posttraumatic stress[tiab]` | 14,174 | none |
| 10 | `post-traumatic stress[tiab]` | 8,160 | none |
| 11 | `post traumatic stress[tiab]` | 8,160 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 32,074 | none |

### Strategy (single line, for copying into PubMed)

```text
((Stress Disorders, Post-Traumatic[Mesh] OR PTSD[tiab] OR posttraumatic stress disorder*[tiab] OR post-traumatic stress disorder*[tiab] OR post traumatic stress disorder*[tiab] OR posttraumatic stress symptom*[tiab] OR post-traumatic stress symptom*[tiab] OR post traumatic stress symptom*[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 11 | 11 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 24 | 24 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 10 | 10 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories and longitudinal course | left out | 32,074 / 6,840 | 78.7% | 18629750 | 0/30 (up to 10% of removed records could be relevant) | After expanding the screened development set, the PTSD core has 45 known records (24 development, 10 held-out, 11 external benchmark). The 30-record loss sample had no relevant record, but the optional block loses benchmark PMID 18629750 and its 78.7% reduction does not justify losing a known relevant study. Leave it out and screen repeated post-event assessments. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial PTSD MeSH/free-text core; longitudinal course terms tested as an optional block; benchmark screened from a prior PTSD trajectory review. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 253 NCBI requests logged (94 from cache); strategy sha256 6dfc3ad0a132._

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
        "message": "32,074 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "32,074 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T15:43:14+00:00",
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
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"posttraumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "876703c17a1aabdc1233dea52cdd720fe7dd9c87ce8ad597bf6cd0220c79d6a2",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported PubMed translation preserves the PTSD concept terms and the Entry Date range. No unexplained translation issue or warning is reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD alternatives are OR-combined. No trajectory or trauma-event AND block is imposed; the optional trajectory block was tested and left out after it lost known relevant PMID 18629750."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD MeSH descriptor is reported as verified and is combined with free-text alternatives. The packet gives no evidence of an incorrect heading or mapping."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word alternatives cover PTSD and several spaced and unspaced forms of post-traumatic stress disorder and symptoms. The broader post-traumatic stress terms support sensitivity; no term is removed solely because known records are covered."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The numbered set is OR-combined as intended, and the final query applies the stated Entry Date range. No syntax errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, human, or study-design filters are applied. The stated as-of boundary is implemented through Entry Date, consistent with the packet's note."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 32,074-record yield exceeds the workload budget, but the packet explicitly considers the searchable trauma-event concept and explains why it remains a screening criterion. The tested trajectory block reduces yield by 78.7% but loses a known benchmark record, so retaining the broader PTSD search and screening repeated post-event assessments is justified.",
          "evidence": "The packet records the trauma-event concept as screen with a rationale against a required event block; the trajectory block was tested at 6,840 results and loses PMID 18629750; the final PTSD core retrieves all 45 known records, including all 11 benchmark records."
        }
      ]
    }
  ]
}
```


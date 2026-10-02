# PubMed search strategy: audit

Generated 2026-10-02T13:39:06+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / symptom course
- Scope confirmed by user: no (User requested standard depth, supplied no known relevant articles, and cannot answer questions during this run. Scope was therefore set from the question without confirmation. PubMed records are bounded by Entrez date through 2016-01-24 via PSB_AS_OF; no publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder | search | The condition is the topic and is reliably named and indexed; trajectory, symptom course, and the post-trauma context are handled at screening because these features may be inconsistently reported in titles and abstracts. |
| PTSD symptom trajectories and course | screen | Outcome and longitudinal pattern with variable terminology; requiring a separate trajectory block risks missing studies describing repeated symptom course without trajectory terminology. |
| Traumatic event exposure | screen | The question implies a traumatic event but trauma context is often detailed only in abstracts or full text and is not needed as a separate AND block because PTSD itself entails traumatic exposure. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:38:51+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,074
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 4 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 5 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 6 | `"post-traumatic stress disorder"[tiab]` | 7,081 | none |
| 7 | `"post traumatic stress disorder"[tiab]` | 7,081 | none |
| 8 | `"posttraumatic stress disorder"[tiab]` | 12,500 | none |
| 9 | `"post-traumatic stress disorders"[tiab]` | 246 | none |
| 10 | `"post traumatic stress disorders"[tiab]` | 246 | none |
| 11 | `"posttraumatic stress disorders"[tiab]` | 243 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 32,074 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress disorder"[tiab] OR "post traumatic stress disorder"[tiab] OR "posttraumatic stress disorder"[tiab] OR "post-traumatic stress disorders"[tiab] OR "post traumatic stress disorders"[tiab] OR "posttraumatic stress disorders"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 40,588 | initial | none | Initial one-block PTSD concept strategy; trajectories, course, and traumatic-event context remain screening criteria because they are variable outcomes/context. Added standard controlled heading and PTSD/posttraumatic stress variants; no filters or publication-date limits. |
| 2 | 32,074 | ptsd: +0 / -1 | none | Removed standalone PTS[tiab] after the critic flagged acronym ambiguity. It was a redundant expansion-risk term: the reviewed relevant records are also retrieved by PTSD, posttraumatic stress wording, or the MeSH heading. The harness requires the 2016-01-24 PubMed entry-date bound, so that bound is retained; no publication-date filter is used. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 2 findings; F1 should-fix open, F2 must-fix open
- Round 2 on version 2: 2 findings; F1 should-fix resolved, F2 must-fix rejected
- Round 3 on version 2: 2 findings; F1 should-fix resolved, F2 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 198 NCBI requests logged (48 from cache); strategy sha256 c1047da00aa4._

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
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:38:51+00:00",
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
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorders\"[Title/Abstract] OR \"post-traumatic stress disorders\"[Title/Abstract] OR \"posttraumatic stress disorders\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "0785ca40b8412554f6c5f2357e452d31328b437023dd8122c0fe1b2e3cbb1e5b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD is the sole required topic concept; symptom trajectories and event context remain screening criteria as planned."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR joins synonyms in one condition block, with no narrowing AND blocks."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Stress Disorders, Post-Traumatic descriptor is present and exploded by default."
        },
        "text_words": {
          "verdict": "revise",
          "note": "PTS is a standalone ambiguous acronym; inspect its unique contribution before deciding."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly field-tagged and PubMed diagnostics show no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The reviewer interpreted the date bound as an unjustified scope limit; the task harness explicitly requires this historical PubMed entry-date bound."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "PTS[tiab] is an ambiguous standalone abbreviation and may retrieve records unrelated to PTSD; its unique retrieval contribution should be examined.",
          "recommendation": "Test PTS[tiab] for incremental retrieval over the other terms and assess the results; remove if no retrieval benefit supports its noise risk.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The entry-date cutoff needs justification because it excludes records added to PubMed after 2016-01-24.",
          "recommendation": "Remove the cutoff unless the review scope deliberately requires the historical date.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "35ab5372b5dab0f897308eab554d2ac4e5117faf1f2405579253a1c3b037f555",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD is the searched concept; trajectory, course, and trauma exposure remain screening criteria. The condition is represented by its MeSH heading, acronym, and spelling variants."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines the condition terms in one block, without narrowing AND blocks."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Stress Disorders, Post-Traumatic heading remains in the query."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The ambiguous standalone PTS acronym was removed. All eight development records remain retrieved and no PubMed translation issues are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are tagged and current PubMed diagnostics show no syntax or translation errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date bound through 2016-01-24 is mandated by the run instructions and is recorded in the protocol; it is not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "PTS[tiab] is an ambiguous standalone abbreviation and may retrieve records unrelated to PTSD; its unique retrieval contribution should be examined.",
          "recommendation": "Test PTS[tiab] for incremental retrieval over the other terms and assess the results; remove if no retrieval benefit supports its noise risk.",
          "status": "resolved",
          "response": "Removed PTS[tiab] as recommended due to ambiguity. Re-evaluation reduced the total condition-block count from 40,588 to 32,074 and lost none of the eight screened-in development records (relative recall remains 8/8). The remaining PTSD and spelled-out forms retain the relevant terms."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The entry-date cutoff needs justification because it excludes records added to PubMed after 2016-01-24.",
          "recommendation": "Remove the cutoff unless the review scope deliberately requires the historical date.",
          "status": "rejected",
          "response": "This evaluation is explicitly required to simulate 2016-01-24 and retain PSB_AS_OF on every command. The protocol records the same Entrez-date bound. No publication-date limit was added."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "35ab5372b5dab0f897308eab554d2ac4e5117faf1f2405579253a1c3b037f555",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD is searched as planned; trajectory, symptom course, and trauma context remain screening criteria. The condition block includes the verified MeSH heading, PTSD, and spelled-out variants."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines condition synonyms in one block, without narrowing AND blocks."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Stress Disorders, Post-Traumatic heading is included and exploded by default."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The ambiguous standalone PTS term was removed. All eight development records remain retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Terms are explicitly field-tagged, and PubMed diagnostics report no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date bound through 2016-01-24 is required by the run instructions and recorded in the protocol; it is not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "PTS[tiab] is an ambiguous standalone abbreviation and may retrieve records unrelated to PTSD; its unique retrieval contribution should be examined.",
          "recommendation": "Test PTS[tiab] for incremental retrieval over the other terms and assess the results; remove if no retrieval benefit supports its noise risk.",
          "status": "resolved",
          "response": "PTS[tiab] was removed. The condition-block count is 32,074, and none of the eight development records were lost."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The entry-date cutoff needs justification because it excludes records added to PubMed after 2016-01-24.",
          "recommendation": "Remove the cutoff unless the review scope deliberately requires the historical date.",
          "status": "rejected",
          "response": "The run instructions require the historical 2016-01-24 Entrez entry-date bound, which is also recorded in the protocol. No publication-date limit is used."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


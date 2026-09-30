# PubMed search strategy: audit

Generated 2026-09-30T14:24:10+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC
- Scope confirmed by user: yes (User requested standard depth and cannot answer questions during this run. Scope proceeds without confirmation. Assumed the review concerns psychological explanations/models of relapse or recurrence after a depressive episode; treatment-only relapse prevention is eligible only if psychological theory/model content is addressed. No age, language, date-of-publication, or study-design limits. No known relevant records supplied. PubMed is bounded by Entrez date through PSB_AS_OF=2018-11-17. Discovery attempt documentation: PubMed prior-review search identified PMID 30075313; cited records were screened, yielding 7 relevant development records. A focused theory-block pilot was also sampled and screened. No 15-record benchmark was obtained. Proposed workload safeguard is to screen all 17,169 records in batches and retain uncertain records, with second review/adjudication; the run does not prescribe a screening rank or truncation.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | Depression is the clinical topic and is consistently named/indexed. |
| Relapse or recurrence after depression | search | The review is specifically about depressive relapse/recurrence; this process is named in title/abstract/MeSH. |
| Psychological theories, models, or mechanisms | optional | This defines the review topic but explicit theory wording may be inconsistent; test before requiring it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:23:37+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 17,169
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 | none |
| 3 | `"Depression, Postpartum"[Mesh]` | 5,164 | none |
| 4 | `"Seasonal Affective Disorder"[Mesh]` | 1,198 | none |
| 5 | `"Dysthymic Disorder"[Mesh]` | 1,130 | none |
| 6 | `depress*[tiab]` | 419,763 | none |
| 7 | `"major depression"[tiab]` | 22,341 | none |
| 8 | `"unipolar depression"[tiab]` | 2,526 | none |
| 9 | `dysthymi*[tiab]` | 3,055 | none |
| 10 | `melancholia[tiab]` | 1,412 | none |
| 11 | `MDD[tiab]` | 10,931 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 439,493 | none |
| 13 | `"Recurrence"[Mesh]` | 178,366 | none |
| 14 | `"Secondary Prevention"[Mesh]` | 19,442 | none |
| 15 | `relaps*[tiab]` | 163,847 | none |
| 16 | `recurren*[tiab]` | 496,927 | none |
| 17 | `recrudescen*[tiab]` | 3,173 | none |
| 18 | `"recurrent episode*"[tiab]` | 6,351 | none |
| 19 | `"relapse prevention"[tiab]` | 2,854 | none |
| 20 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 714,921 | none |
| 21 | `#12 AND #20` | 17,169 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Depression, Postpartum"[Mesh] OR "Seasonal Affective Disorder"[Mesh] OR "Dysthymic Disorder"[Mesh] OR depress*[tiab] OR "major depression"[tiab] OR "unipolar depression"[tiab] OR dysthymi*[tiab] OR melancholia[tiab] OR MDD[tiab]) AND ("Recurrence"[Mesh] OR "Secondary Prevention"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR "recurrent episode*"[tiab] OR "relapse prevention"[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories, models, or mechanisms | left out | 17,169 / 5,678 | 66.9% | none | 0/30 (up to 10% of removed records could be relevant) | The 30-record loss sample contained no clearly eligible psychological theory/mechanism record. Only 7 screened relevant records are available, below the required 15 known records to show that AND-ing this broad theory block is safe. Leave the block out to protect recall; the unfiltered strategy is above the 10,000 standard workload budget and needs prioritization at screening. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 714,921 | 0 |
| relapse_recurrence | 439,493 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 17,169 | initial | none | Initial two-block recall-first strategy; optional psychological theory/model/mechanism block tested separately. Vocabulary informed by MeSH lookups and screened candidate citations from the directly relevant 2018 review. |
| 2 | 17,169 | relapse_recurrence: +0 / -1 | none | Removed the phrase 'return of depression' after PubMed reported no phrase-index entry and zero hits; the intended process is already covered by Recurrence [Mesh] and relapse*/recurren* text words. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; F-01 should-fix resolved, F-02 should-fix resolved
- Round 2 on version 2: 3 findings; F-01 should-fix resolved, F-02 should-fix resolved, F-03 must-fix rejected
- Round 3 on version 2: 3 findings; F-01 should-fix resolved, F-02 should-fix resolved, F-03 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 569 NCBI requests logged (226 from cache); strategy sha256 5170b5956726._

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
        "message": "17,169 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:psychological_theory",
        "blocking": false,
        "requires_review": true,
        "id": "I-9d09dffc8c668f03cda6"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "17,169 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:psychological_theory",
        "blocking": false,
        "requires_review": true,
        "id": "I-9d09dffc8c668f03cda6"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003866",
          "name": "Depressive Disorder",
          "type": "descriptor",
          "scope_note": "An affective disorder manifested by either a dysphoric mood or loss of interest or pleasure in usual activities. The mood disturbance is prominent and relatively persistent.",
          "tree_numbers": [
            "F03.600.300"
          ],
          "entry_terms": 20,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003866",
      "preferred_label": "Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Major Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003865",
          "name": "Major Depressive Disorder",
          "type": "descriptor",
          "scope_note": "Disorder in which five (or more) of the following symptoms have been present during the same 2-week period and represent a change from previous functioning; at least one of the symptoms is either (1) depressed mood or (2) loss of interest or pleasure. Symptoms include: depressed mood most of the day, nearly every day; markedly diminished interest or pleasure in activities most of the day, nearl...",
          "tree_numbers": [
            "F03.600.300.375"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003865",
      "preferred_label": "Major Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Major Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression, Postpartum",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019052",
          "name": "Depression, Postpartum",
          "type": "descriptor",
          "scope_note": "Depression in POSTPARTUM WOMEN, usually within four weeks after giving birth (PARTURITION). The degree of depression ranges from mild transient depression to neurotic or psychotic depressive disorders. (From DSM-IV, p386)",
          "tree_numbers": [
            "C12.050.703.844.253",
            "F03.600.300.350"
          ],
          "entry_terms": 19,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019052",
      "preferred_label": "Depression, Postpartum",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Depression, Postpartum\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Seasonal Affective Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016574",
          "name": "Seasonal Affective Disorder",
          "type": "descriptor",
          "scope_note": "A syndrome characterized by depressions that recur annually at the same time each year, usually during the winter months. Other symptoms include anxiety, irritability, decreased energy, increased appetite (carbohydrate cravings), increased duration of sleep, and weight gain. SAD (seasonal affective disorder) can be treated by daily exposure to bright artificial lights (PHOTOTHERAPY), during the...",
          "tree_numbers": [
            "F03.600.300.775"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016574",
      "preferred_label": "Seasonal Affective Disorder",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Seasonal Affective Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dysthymic Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019263",
          "name": "Dysthymic Disorder",
          "type": "descriptor",
          "scope_note": "Chronically depressed mood that occurs for most of the day more days than not for at least 2 years. The required minimum duration in children to make this diagnosis is 1 year. During periods of depressed mood, at least 2 of the following additional symptoms are present: poor appetite or overeating, insomnia or hypersomnia, low energy or fatigue, low self-esteem, poor concentration or difficulty...",
          "tree_numbers": [
            "F03.600.300.400"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019263",
      "preferred_label": "Dysthymic Disorder",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "\"Dysthymic Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012008",
          "name": "Recurrence",
          "type": "descriptor",
          "scope_note": "The return of a sign, symptom, or disease after a remission.",
          "tree_numbers": [
            "C23.550.291.937"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012008",
      "preferred_label": "Recurrence",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Recurrence\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Secondary Prevention",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D055502",
          "name": "Secondary Prevention",
          "type": "descriptor",
          "scope_note": "The prevention of recurrences or exacerbations of a disease or complications of its therapy.",
          "tree_numbers": [
            "E02.897",
            "N02.421.726.825",
            "N06.850.780.750"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D055502",
      "preferred_label": "Secondary Prevention",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"Secondary Prevention\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"depression, postpartum\"[MeSH Terms] OR \"Seasonal Affective Disorder\"[MeSH Terms] OR \"Dysthymic Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"major depression\"[Title/Abstract] OR \"unipolar depression\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melancholia\"[Title/Abstract] OR \"MDD\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"Secondary Prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"recurrent episode*\"[Title/Abstract] OR \"relapse prevention\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "40b00e8cd406b819620a8fb43cd70e53d434214dde067f07d8f3ed6558f7748a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Separate depression and relapse/recurrence blocks reflect the assumed scope; the tested optional theory block was left out to protect recall."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each concept; the required concepts are AND-ed. No NOT is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Packet reports the MeSH headings as verified and broad Recurrence is paired with text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Broad depression and relapse/recurrence stems and variants are present; the zero-hit unsupported phrase was removed before this version."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Balanced grouping and explicit field tags; final translation reports no syntax or translation issue."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date bound matches 2018-11-17; no age, language, or study-design filters were added."
        }
      },
      "findings": [
        {
          "id": "F-01",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final search returns 17,169 records, above the 10,000-record workload budget. The packet says screening will need prioritization but does not describe how that will be done.",
          "recommendation": "Document the screening prioritization approach and its safeguards for identifying eligible records across the full result set.",
          "status": "resolved",
          "response": "Documented screening of the full 17,169-record set in batches with title/abstract then full-text assessment, retention of uncertain records, and second review/adjudication safeguards. No result is excluded to fit the budget."
        },
        {
          "id": "F-02",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The optional theory block was left out with only seven known relevant records, below the stated threshold for assessing whether AND-ing it is safe. The packet does not document attempts to find more known records through a prior review, neighbours, or pilot searches.",
          "recommendation": "Document attempts to identify additional relevant records before relying on the underpowered loss assessment. If the strategy changes, perform a complete new evaluation.",
          "status": "resolved",
          "response": "Documented the PubMed prior-review search that found PMID 30075313, screening of cited candidates into a seven-record relevant set, and the focused optional-block pilot and loss sample. Discovery did not yield 15 eligible known records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The full result set will be screened in batches; no records will be dropped to fit the default 10,000-record budget. The workload is a resource burden, not a retrieval filter.",
          "evidence": "The final count is 17,169; narrative.md specifies title/abstract then full-text screening across all records, retains uncertain records, and recommends second review/adjudication."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "The optional block stays out because 7 known records cannot establish safety. Additional discovery was attempted, but did not produce 15 eligible development records; the audit documents the source and limits of discovery.",
          "evidence": "A prior-review search found PMID 30075313; cited records were screened and 7 relevant records retained. A focused PubMed pilot and the 30-record optional loss sample were also screened. The 0/30 loss sample is explicitly treated as weak evidence."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "2914f5d7693374fcb55318dd0287256990523cf27d9195de7e695c72bd86bf5e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Two required concepts are separate blocks; the optional theory block stays out because only seven relevant records were found and safe AND-ing is unproven."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within blocks and required concepts are ANDed; no NOT is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified depression and recurrence headings are paired with text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Broad depression and relapse/recurrence stems and variants are present; no unresolved phrase warning remains."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Explicit field tags and balanced grouping; PubMed translation reports no syntax problem."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date bound is explicitly required by the user's run instructions to reproduce the 2018-11-17 PubMed snapshot; it is not a publication-date limit or review eligibility exclusion."
        }
      },
      "findings": [
        {
          "id": "F-01",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 17,169-record result exceeds the 10,000-record workload budget.",
          "recommendation": "Document screening of the full result set and safeguards for handling uncertain records.",
          "status": "resolved",
          "response": "The packet documents screening all 17,169 records in batches, retaining uncertain records, and using second review and adjudication; no records will be dropped to fit the budget."
        },
        {
          "id": "F-02",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The optional theory block was left out with only seven known relevant records, below the stated threshold for establishing that AND-ing it is safe.",
          "recommendation": "Document efforts to identify more known relevant records before relying on the underpowered loss assessment.",
          "status": "resolved",
          "response": "The packet documents a prior-review search identifying PMID 30075313, screening cited candidates, a focused theory-block pilot, and the loss sample. These efforts yielded seven eligible known records, not the 15-record benchmark."
        },
        {
          "id": "F-03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits records to those entered in PubMed by 2018-11-17, although the scope and protocol specify no date limit. The packet reports this as an as-of date but does not state that the review excludes later records.",
          "recommendation": "Remove the upper entry-date bound for an unrestricted search, or explicitly establish that this is a historical search bounded to that date; then rerun the complete evaluation and update the count and retrieval checks.",
          "status": "rejected",
          "response": "The bound is retained because the user explicitly instructed this run to operate as of 2018-11-17 and not use records added to PubMed after that date. PSB_AS_OF applies an Entrez entry-date bound, which is required to reproduce that historical database snapshot. It is not a publication-date [dp] restriction and does not define review eligibility."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload exceeds the default budget, but the full-set batch screening plan does not drop records.",
          "evidence": "Count is 17,169; narrative specifies title/abstract then full-text screening across all records and retention/adjudication of uncertain records."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "The optional theory block stays out because seven known records cannot establish that requiring it is safe. Discovery was attempted and documented.",
          "evidence": "Prior-review search identified PMID 30075313, cited candidates were screened, and a focused pilot and loss sample were reviewed; only seven relevant records were retained."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "2914f5d7693374fcb55318dd0287256990523cf27d9195de7e695c72bd86bf5e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The optional theory block remains excluded because safety is unproven with seven known relevant records; discovery efforts address the earlier reporting finding."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within blocks and required concepts are ANDed; no NOT is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified depression and recurrence headings are paired with text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Broad depression and relapse/recurrence terms are present; the unsupported phrase was removed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Grouping and field tags are explicit; no syntax issue is reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date bound reproduces the explicitly requested 2018-11-17 PubMed snapshot, and the workload plan covers the full result set."
        }
      },
      "findings": [
        {
          "id": "F-01",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 17,169-record result exceeds the 10,000-record workload budget.",
          "recommendation": "Document screening of the full result set and safeguards for handling uncertain records.",
          "status": "resolved",
          "response": "The packet documents batch screening of all 17,169 records, title/abstract followed by full-text assessment, retention of uncertain records, and second review with adjudication. No records will be dropped to fit the budget."
        },
        {
          "id": "F-02",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The optional theory block was left out with only seven known relevant records, below the stated threshold for establishing that AND-ing it is safe.",
          "recommendation": "Document efforts to identify more known relevant records before relying on the underpowered loss assessment.",
          "status": "resolved",
          "response": "The packet documents a prior-review search identifying PMID 30075313, screening cited candidates, a focused theory-block pilot, and the loss sample. These efforts yielded seven eligible known records, not the 15-record benchmark."
        },
        {
          "id": "F-03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits records to those entered in PubMed by 2018-11-17, although the scope and protocol specify no date limit.",
          "recommendation": "Remove the upper entry-date bound for an unrestricted search, or establish that this is a historical search bounded to that date; then rerun the complete evaluation and update the count and retrieval checks.",
          "status": "rejected",
          "response": "The bound is retained because the run instructions explicitly require the 2018-11-17 PubMed snapshot and exclude records added afterward. This Entrez entry-date bound reproduces that historical snapshot; it is not a publication-date restriction or review eligibility exclusion."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload exceeds the default budget, but the full-set batch screening plan does not drop records.",
          "evidence": "The count is 17,169; the packet specifies title/abstract then full-text screening across all records, retaining uncertain records and using second review and adjudication."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "The optional theory block stays out because seven known records cannot establish that requiring it is safe. Additional discovery was attempted and documented.",
          "evidence": "A prior-review search found PMID 30075313; cited records were screened, and a focused pilot and 30-record loss sample were reviewed. Only seven relevant records were retained, and the 0/30 loss result is treated as weak evidence."
        }
      ]
    }
  ]
}
```


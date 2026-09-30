# PubMed search strategy: audit

Generated 2026-09-30T13:14:22+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: Condition + course (relapse/recurrence); explanatory theory is an optional topic label
- Scope confirmed by user: no (User requested no follow-up questions. Scope assumptions: treat relapse and recurrence as the course concept; explanatory psychological theory is evaluated as an optional block and screened in eligibility. No seeds or known relevant articles supplied. Standard-depth target candidate screening budget about 150. PubMed is evaluated with Entrez date bound 2018-11-17 via PSB_AS_OF; no publication-date limit. The optional theory block was assessed with a 30-record loss sample and targeted review/pilot screening. Tested recover*[tiab] as a course term: alone with the depression block it counted 18,710 records, and in the expanded course-block evaluation it increased the final count from 26,728 to 42,670; omitted it as nonspecific. remitt*[tiab] and return*[tiab] are retained.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | Depression defines the condition and is named/indexed reliably. |
| Depressive relapse, recurrence, or return of illness | search | The course event defines the question. Search broad labels for relapse and recurrence. |
| Psychological theories, models, and explanatory mechanisms | optional | The title phrase suggests this topic, but otherwise-relevant accounts may not be labelled as theory; test before requiring it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:13:55+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 26,728
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Depressive Disorder[Mesh]` | 105,341 | none |
| 2 | `Major Depressive Disorder[Mesh]` | 28,520 | none |
| 3 | `depress*[tiab]` | 419,763 | none |
| 4 | `melanchol*[tiab]` | 2,939 | none |
| 5 | `unipolar[tiab]` | 10,360 | none |
| 6 | `#1 OR #2 OR #3 OR #4 OR #5` | 443,690 | none |
| 7 | `Recurrence[Mesh]` | 178,366 | none |
| 8 | `Secondary Prevention[Mesh]` | 19,442 | none |
| 9 | `relaps*[tiab]` | 163,847 | none |
| 10 | `recurren*[tiab]` | 496,927 | none |
| 11 | `recrudescen*[tiab]` | 3,173 | none |
| 12 | `return*[tiab]` | 223,418 | none |
| 13 | `remitt*[tiab]` | 16,130 | none |
| 14 | `#7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 932,544 | none |
| 15 | `#6 AND #14` | 26,728 | none |

### Strategy (single line, for copying into PubMed)

```text
((Depressive Disorder[Mesh] OR Major Depressive Disorder[Mesh] OR depress*[tiab] OR melanchol*[tiab] OR unipolar[tiab]) AND (Recurrence[Mesh] OR Secondary Prevention[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR return*[tiab] OR remitt*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 10 | 10 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories, models, and explanatory mechanisms | left out | 26,728 / 10,379 | 61.2% | 792937, 19758704, 24489940, 27921216, 30135832 | 2/30 | Leave the optional theory block out. The current loss sample contains two in-scope records without its theory/model wording, and the known relevant set has 10 records, below the 15-record minimum for safely AND-ing it. Though it cuts retrieval by about 61%, the known records and loss sample favor screening the broader query; prior-review, targeted-pilot, and loss-sample routes were tried, but the targeted prior review did not expose a usable included-study reference set. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 932,544 | 0 |
| relapse_recurrence | 443,690 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 23,239 | initial | none | Initial recall-first blocks drafted from question before any records reviewed; theory/model terminology is optional and will be tested. |
| 2 | 17,335 | relapse_recurrence: +0 / -1 | none | Removed remission[tiab] from the course block because remission alone does not identify relapse or recurrence and inflates retrieval with studies of remission without return; all known records are checked. |
| 3 | 42,670 | relapse_recurrence: +3 / -0 | none | Addressed critic F1 by testing return*[tiab]; also tested remitt*[tiab] and recover*[tiab] as supplementary process terms to assess whether recovery/remission wording retrieves in-scope records. Retain only if translated and recall/count evidence supports high sensitivity. |
| 4 | 26,728 | relapse_recurrence: +0 / -1 | none | Addressed critic F1 with return*[tiab]. Tested remitt*[tiab] and recover*[tiab] as requested for process-direction wording; retained remitt*[tiab] because remission is the state from which recurrence follows, but omitted recover*[tiab] after its depression-only count (18,710) showed broad, nonspecific retrieval. Re-evaluate full query and known records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; F1 must-fix open, F2 should-fix open
- Round 2 on version 4: 2 findings; F1 must-fix resolved, F2 should-fix open
- Round 3 on version 4: 2 findings; F1 must-fix resolved, F2 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 677 NCBI requests logged (283 from cache); strategy sha256 0d92f79808a9._

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
        "message": "26,728 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "26,728 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T13:13:55+00:00",
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
        "text": "Depressive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Major Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:13:55+00:00",
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
        "text": "Major Depressive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:13:55+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "Recurrence",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Secondary Prevention",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:13:55+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "Secondary Prevention",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"depressive disorder\"[MeSH Terms] OR \"major depressive disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"unipolar\"[Title/Abstract]) AND (\"recurrence\"[MeSH Terms] OR \"secondary prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"return*\"[Title/Abstract] OR \"remitt*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "9a08c88b74db0a8dfd15e565ec023c068ad832ff9379510381e5eb08e399eb93",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The MeSH and field translations shown have no warnings or errors. However, the searched course concept includes return of depressive illness, and the strategy has no independent return term. Add and test an expression for that named concept."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required blocks are joined with AND, and their synonyms are joined with OR. The tested optional block is left out of the final query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the depressive disorder, major depressive disorder, recurrence, and secondary prevention descriptors. No heading translation issues are reported."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The free-text terms cover depression, relapse, recurrence, and recrudescence, but omit the separately named return concept. The packet also requires review of process-direction coverage when a block searches for an event such as relapse or recurrence."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is syntactically coherent, and the packet reports no lint, syntax, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No limits are listed. The documented Entrez entry-date bound is applied consistently through 2018-11-17; the packet states that this is not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "block": "relapse_recurrence",
          "finding": "The searched course concept explicitly includes return of depressive illness, but the strategy has no independent free-text term for return. The current relapse and recurrence terms do not satisfy the packet's requirement that each named member of a searched concept be covered by its own bare name.",
          "recommendation": "Add an independently tested return expression, such as return*[tiab], to the relapse/recurrence block, then rerun the complete evaluation and inspect its retrievals.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "relapse_recurrence",
          "finding": "The course block searches for relapse and recurrence events but does not show testing for the other direction of the process, such as remission or recovery. The packet specifically calls for process-direction review when a block names an event such as relapse.",
          "recommendation": "Test explicit remission and recovery expressions as supplementary course terms, assess their retrievals and workload, and screen for the eligible return direction. Rerun the complete evaluation after any query change.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the workload warning for this reviewed version: the final query has 17,335 records against a 10,000-record budget, while the tested optional psychology/theory block reduces the count by 60.9% but loses three of the eight known relevant records, and its loss sample includes one relevant record. Broaden or refine the course terms before making another workload decision.",
          "evidence": "The packet reports 17,335 results, a 10,000-record budget, 6,776 results with the optional block, three known records lost, and one relevant record in a 30-record loss sample."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Accept the underpowered optional-block warning as a documented recall risk. The evidence supports leaving the broad block out, but the packet does not establish that attempts were made to find additional known records through prior reviews, neighbouring records, or pilot searches.",
          "evidence": "Only eight relevant records are listed, below the stated minimum of 15; the optional block loses three known relevant records, and the loss sample finds one relevant record among 30. No prior-review, neighbour, or pilot-search effort is documented."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "c1376086fc335ec0282909dbf158ece7fa1ef5b8e159a15335222ce3e7f772b4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation warnings or errors for the tested MeSH headings and text-word expressions. The independently tested return*[tiab] term addresses the earlier missing return expression."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required depression and course blocks are joined with AND, their terms with OR, and the optional theory block is excluded after testing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the depressive disorder, major depressive disorder, recurrence, and secondary prevention headings, with no heading translation issues."
        },
        "text_words": {
          "verdict": "revise",
          "note": "return*[tiab] resolves the missing return expression, and remitt*[tiab] supplies a tested remission expression. Recovery remains untested and absent, so the earlier process-direction finding remains open."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is coherent, with no reported lint, syntax, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No search limits are listed. The packet documents the Entrez entry-date bound through 2018-11-17 and distinguishes it from a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "block": "relapse_recurrence",
          "finding": "The searched course concept includes return of depressive illness, and the prior version lacked an independent free-text return expression.",
          "recommendation": "Add and test an independent return expression in the relapse/recurrence block, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current block includes return*[tiab], tested independently as line 12, and the complete evaluation reports no missed known relevant records."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "relapse_recurrence",
          "finding": "The course block now includes the tested remission expression remitt*[tiab], but no recovery expression is shown. Process-direction coverage therefore remains incomplete under the packet's translation check.",
          "recommendation": "Test an explicit recovery expression as a supplementary course term, assess its retrievals and workload, and rerun the complete evaluation after any query change.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the workload warning for this version. The sole optional searchable concept, psychological theories/models/mechanisms, was tested and left out based on relevant records lost and the loss sample. The broader query remains above budget; screening this volume is a documented workload risk.",
          "evidence": "The final query retrieves 26,728 records against a 10,000-record budget. The tested optional block reduces retrieval to 10,379 (61.2%) but loses five of ten known relevant records, and two of 30 sampled records removed by that block were judged relevant. The packet says prior-review, targeted-pilot, and loss-sample routes were tried."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Accept the underpowered optional-block warning as a documented recall risk. The packet records attempts to find additional known records and provides loss evidence supporting the decision to screen the broader query; the known set remains below the stated threshold.",
          "evidence": "There are ten known relevant records, below the 15-record minimum. The optional block would remove five known relevant records, and the 30-record loss sample includes two relevant records. The packet documents prior-review, targeted-pilot, and loss-sample routes, while noting that the targeted prior review did not provide a usable included-study reference set."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "302f9d11b8805ae03a9685c00a83467d97ff6820a627829b8b4b40e213406881",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet verifies the searched MeSH headings and reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required depression and course blocks are joined with AND; terms within each block are joined with OR. The tested optional theory block is left out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The depression, recurrence, and secondary prevention headings are verified, with no reported heading translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "return*[tiab] resolves F1. For F2, recover*[tiab] was tested and omitted because it raised the expanded query to 42,670 records; remitt*[tiab] and return*[tiab] remain. This supports closing F2 as accepted risk, while the packet does not establish the relevance of records uniquely retrieved by recover*."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is coherent and the packet reports no syntax or lint issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No search limits are listed. The Entrez entry-date bound through 2018-11-17 is documented and distinguished from a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "block": "relapse_recurrence",
          "finding": "The searched course concept includes return of depressive illness, and the earlier strategy lacked an independent free-text return expression.",
          "recommendation": "Add and test an independent return expression in the relapse/recurrence block, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current block includes return*[tiab], independently tested as line 12. The complete evaluation reports no missed known relevant records."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "relapse_recurrence",
          "finding": "The course block searches for relapse and recurrence events, raising a process-direction coverage concern.",
          "recommendation": "Test a recovery expression, assess its retrieval and workload, and screen for the eligible return direction.",
          "status": "accepted-risk",
          "response": "The packet documents testing recover*[tiab]: it retrieved 18,710 records with the depression block and raised the expanded query to 42,670, so it was omitted as broad. remitt*[tiab] and return*[tiab] remain in the strategy. This is sufficient to close F2 as an accepted workload and recall risk; the packet does not report screening the records uniquely added by recover*, so their relevance is not established."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the workload warning. The broad query remains above the stated budget, and the optional theory block was left out after testing because it removed known relevant records and relevant sampled records.",
          "evidence": "The final query retrieves 26,728 records against a 10,000-record budget. The optional block reduces this to 10,379 but loses five of ten known relevant records; two of 30 sampled removed records were judged relevant."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Accept the underpowered optional-block warning as a documented recall risk. The packet records attempts to find more known records and evidence supporting the decision to screen the broader query.",
          "evidence": "The known relevant set has ten records, below the stated minimum of 15. The optional block loses five known records, and the 30-record loss sample includes two relevant records. Prior-review, targeted-pilot, and loss-sample routes were tried; the targeted prior review yielded no usable included-study reference set."
        }
      ]
    }
  ]
}
```


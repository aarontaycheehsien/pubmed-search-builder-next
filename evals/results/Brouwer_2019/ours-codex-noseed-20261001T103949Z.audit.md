# PubMed search strategy: audit

Generated 2026-10-01T11:24:32+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: etiology / explanatory framework
- Scope confirmed by user: no (User has no known relevant articles and cannot answer questions during this run; proceed with reasonable assumptions without confirmation. Scope interpretation: broad depression + relapse/recurrence are required; psychological theory/model language is tested as an optional concept because relevant explanatory papers may not name theory explicitly. No language, date, age, or study-design limits. Entrez-date cutoff is supplied through PSB_AS_OF=2018-11-17 for every command; no publication-date limit is added. No ambiguity clarification was possible by user instruction.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depression and depressive disorders | search | The target phenomenon is depressive illness; relevant records may name a diagnostic subtype or manifestation rather than the broad category. |
| Relapse or recurrence of depression | search | The review is specifically about the return of depressive illness; search broadly for relapse, recurrence, and return of illness terminology. |
| Psychological theories or explanatory models of relapse/recurrence | optional | This defines the review topic, but authors may describe cognitive, interpersonal, behavioral, or other explanatory mechanisms without using theory/model labels; test its retrieval value before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:23:48+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 25,059
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 | none |
| 3 | `"Dysthymic Disorder"[Mesh]` | 1,130 | none |
| 4 | `depress*[tiab]` | 419,763 | none |
| 5 | `dysthymi*[tiab]` | 3,055 | none |
| 6 | `melanchol*[tiab]` | 2,939 | none |
| 7 | `unipolar[tiab]` | 10,360 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 443,941 | none |
| 9 | `"Recurrence"[Mesh]` | 178,366 | none |
| 10 | `"Secondary Prevention"[Mesh]` | 19,442 | none |
| 11 | `relaps*[tiab]` | 163,847 | none |
| 12 | `recurren*[tiab]` | 496,927 | none |
| 13 | `recrudescen*[tiab]` | 3,173 | none |
| 14 | `recurrent episode*[tiab]` | 6,351 | none |
| 15 | `return*[tiab]` | 223,418 | none |
| 16 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 927,028 | none |
| 17 | `#8 AND #16` | 25,059 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Dysthymic Disorder"[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR unipolar[tiab]) AND ("Recurrence"[Mesh] OR "Secondary Prevention"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR recurrent episode*[tiab] OR return*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |
| relevant_optional | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories or explanatory models of relapse/recurrence | left out | 25,059 / 8,290 | 66.9% | 318807, 2515784, 7710966, 11519159 | 0/30 (up to 10% of removed records could be relevant) | Leave this optional block out. The refreshed 30-record loss sample found no additional eligible record, but the earlier screened loss sample identified four eligible records that the candidate block misses. The base has eight known records, below the minimum 15 required to justify AND-ing; this block's apparent workload reduction cannot outweigh known recall loss. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depression and depressive disorders | 1 | `(major depressive disorder[tiab] OR MDD[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR unipolar[tiab])` | 16 | 0/16 |
| Depression and depressive disorders | 2 | `major depressive disorder[tiab] OR MDD[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR unipolar[tiab]` | 21 | 0/21 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 927,028 | 0 |
| relapse_recurrence | 443,941 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 18,203 | initial | none | Initial broad two-block strategy with an optional psychological theory/mechanism concept; includes MeSH and title/abstract vocabulary. Four screened relevant records added as development checks; no seeds supplied. |
| 2 | 17,346 | relapse_recurrence: +0 / -2 | none | Removed two unquoted return-of phrases after PubMed translated return to All Fields despite the field tag; the controlled recurrence heading and relapse/recurrence stems express the core process without fallback. No known records lost. |
| 3 | 25,059 | relapse_recurrence: +1 / -0 | none | Addressed critic F1 by adding return*[tiab] as explicit recall vocabulary; this broadens the process block and replaces the earlier rejected phrase clauses that triggered All Fields fallback. Re-evaluate known records and recalculate the optional and category sample bindings. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F1 should-fix open
- Round 2 on version 3: 1 findings; F1 should-fix resolved
- Round 3 on version 3: 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 670 NCBI requests logged (317 from cache); strategy sha256 d334ecc83bb8._

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
        "message": "25,059 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "25,059 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-10-01T11:23:48+00:00",
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
      "checked_at": "2026-10-01T11:23:48+00:00",
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
      "requested": "Dysthymic Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:23:48+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Dysthymic Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:23:48+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"Recurrence\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Secondary Prevention",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:23:48+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Secondary Prevention\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"Dysthymic Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"unipolar\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"Secondary Prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"recurrent episode*\"[Title/Abstract] OR \"return*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "3d5321509bab9f04a5b400c139e584b1a2f0a8d2ca82138b3bc9056ad022dbe7",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searched relapse/recurrence concept names return of illness, but its terms do not include a bare return term. Add a return text word and reevaluate."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required depression and relapse/recurrence blocks are combined with AND, and terms within each block are combined with OR. The optional psychological-theory block is correctly left out because it demonstrably loses eligible records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The depression and recurrence headings are verified in the packet; the MeSH terms are combined with relevant text words."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add a text-word term for return of illness, which is explicitly named in the scope and eligibility."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The evaluated query has no reported syntax or translation errors, and the final combination is explicitly grouped."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, date, age, or study-design limits are applied. The entry-date cutoff is documented as 2018-11-17."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched relapse/recurrence concept explicitly includes return of depressive illness, but the text-word set contains relaps*, recurren*, recrudescen*, and recurrent episode* without a bare return term.",
          "recommendation": "Add return*[tiab] (or another explicit, tested return text-word expression) to the relapse/recurrence block, then run a complete evaluation of the revised strategy.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 17,346-record result exceeds the 10,000-record workload budget. The optional psychological-theory block reduces results to 5,984 but loses four known eligible records. Keep the optional block out and plan screening or further refinement of the required search.",
          "evidence": "The packet reports 17,346 records without the optional block and 5,984 with it, a 65.5% reduction; the sampled losses include four relevant records. The optional concept was tested, so the workload warning is acknowledged."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Only eight relevant records are known, below the threshold for safely AND-ing the optional block, and the block loses known eligible work. Retain the leave-out decision; additional known records could support a future retest.",
          "evidence": "The packet says the known set came from screened PubMed pilot samples and a prior-review discovery query. The optional-block loss sample identified four additional relevant records, but the resulting base still has only eight known relevant records and the block loses all four optional-set records."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "c7c5fa2e14bd93847b00153d465e543914b0e3c6d93a5b96e08fb11a2cf7c8c9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The revised relapse/recurrence block now includes return*[tiab], covering the named return-of-illness terminology."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required depression and relapse/recurrence blocks are ORed internally and combined with AND. The optional theory block is correctly left out because it loses four known eligible records and the base has fewer than 15 known records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the depression and recurrence MeSH headings; relevant headings are combined with text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised text-word set includes return*[tiab] alongside relapse, recurrence, recrudescence, and recurrent-episode terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The evaluated query is explicitly grouped and reports no syntax, translation, or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, or study-design filters are applied. The 2018-11-17 entry-date cutoff is documented in the packet."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched relapse/recurrence concept explicitly includes return of depressive illness, but the text-word set lacked a bare return term.",
          "recommendation": "Add return*[tiab] or another explicit, tested return text-word expression, then run a complete evaluation.",
          "status": "resolved",
          "response": "Added return*[tiab] to the relapse/recurrence block and completed a fresh evaluation. The revised query retrieves all eight known records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count remains above the workload budget. Keep the optional theory block out because it loses known eligible records; screen the required search or pursue further refinement.",
          "evidence": "The revised base retrieves 25,059 records, above the 10,000 budget. The tested optional block reduces this to 8,290 but loses four known eligible records, and the base has only eight known records."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Retain the leave-out decision. The packet documents prior-review discovery and screened PubMed pilot samples as routes used to identify known records; the tested optional block still loses four eligible records.",
          "evidence": "There are eight known records, below the 15-record threshold for AND-ing an optional block. Four known eligible records are among those lost by the block. The packet identifies the known-record source as screened PubMed pilot samples and a prior-review discovery query."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "c7c5fa2e14bd93847b00153d465e543914b0e3c6d93a5b96e08fb11a2cf7c8c9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The recurrence block now includes return*[tiab], addressing the named return-of-illness concept."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concept blocks are ORed internally and combined with AND. The optional theory block is left out after testing because it loses four known eligible records; the eight known records are below the 15-record threshold for AND-ing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the depression and recurrence headings, which are combined with relevant text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current text-word set includes return*[tiab] alongside relapse, recurrence, recrudescence, and recurrent-episode terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The evaluated query is explicitly grouped and reports no syntax, translation, or phrase-warning issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, or study-design filters are applied. The 2018-11-17 entry-date cutoff is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched relapse/recurrence concept explicitly includes return of depressive illness, but the text-word set lacked a bare return term.",
          "recommendation": "Add return*[tiab] or another explicit, tested return text-word expression, then run a complete evaluation.",
          "status": "resolved",
          "response": "Added return*[tiab] to the relapse/recurrence block and completed a fresh evaluation. The revised query retrieves all eight known records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count exceeds the workload budget. The optional theory block was tested and left out because it loses four known eligible records; screening the required search remains the appropriate outcome.",
          "evidence": "The current base retrieves 25,059 records against a 10,000-record budget. The optional block reduces retrieval to 8,290 records but loses four known eligible records. Its refreshed loss sample found no additional eligible records."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Retain the optional block's leave-out decision. The packet records prior-review discovery and screened PubMed pilot samples as routes used to find known records, and the tested block still loses four eligible records.",
          "evidence": "The eight known records are below the 15-record threshold for AND-ing an optional block. Four known eligible records are among those lost by the block; the packet documents the discovery routes used."
        }
      ]
    }
  ]
}
```


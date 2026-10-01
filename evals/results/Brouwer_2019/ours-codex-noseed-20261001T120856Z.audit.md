# PubMed search strategy: audit

Generated 2026-10-01T13:00:22+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: Condition + process + explanatory framework
- Scope confirmed by user: no (User supplied no known relevant articles and asked to proceed without questions. Scope assumptions: a record must concern depressive relapse/recurrence and a psychological explanation; depressive disorders and relapse/recurrence are searched, while theory/model wording is tested as optional because relevant explanatory work may not label itself as theory. No date, language, age, or study-design limits. Today is treated as 2018-11-17 through PSB_AS_OF on every command (Entrez-date bound; no publication-date limit).)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders and depression | search | The target topic concerns relapse or recurrence in depressive illness; diagnostic members may be named instead of the general category. |
| Depressive relapse and recurrence | search | The process is essential to the question and is generally searchable through relapse, recurrence, remission, and return of depression wording. |
| Psychological theories, models, and explanatory mechanisms | optional | This defines the review topic but authors may describe cognitive, interpersonal, behavioral, psychodynamic, or other mechanisms without labeling them as theories; test the block before deciding whether it can be required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:59:45+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 47,011
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 | none |
| 3 | `"Depression"[Mesh]` | 112,392 | none |
| 4 | `"Depression, Postpartum"[Mesh]` | 5,164 | none |
| 5 | `"Seasonal Affective Disorder"[Mesh]` | 1,198 | none |
| 6 | `depress*[tiab]` | 419,763 | none |
| 7 | `dysthymi*[tiab]` | 3,055 | none |
| 8 | `melanchol*[tiab]` | 2,939 | none |
| 9 | `unipolar[tiab]` | 10,360 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 465,339 | none |
| 11 | `"Recurrence"[Mesh]` | 178,366 | none |
| 12 | `relaps*[tiab]` | 163,847 | none |
| 13 | `recurren*[tiab]` | 496,927 | none |
| 14 | `recrudescen*[tiab]` | 3,173 | none |
| 15 | `remission*[tiab]` | 113,679 | none |
| 16 | `"re-emergence"[tiab]` | 2,275 | none |
| 17 | `(return*[tiab] AND depress*[tiab])` | 7,933 | none |
| 18 | `reappear*[tiab]` | 11,263 | none |
| 19 | `recover*[tiab]` | 602,986 | none |
| 20 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 1,374,314 | none |
| 21 | `#10 AND #20` | 47,011 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Depression"[Mesh] OR "Depression, Postpartum"[Mesh] OR "Seasonal Affective Disorder"[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR unipolar[tiab]) AND ("Recurrence"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR remission*[tiab] OR "re-emergence"[tiab] OR (return*[tiab] AND depress*[tiab]) OR reappear*[tiab] OR recover*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories, models, and explanatory mechanisms | left out | 47,011 / 15,891 | 66.2% | 24364598 | 0/30 (up to 10% of removed records could be relevant) | Leave the optional theory/model/mechanism block out: only 8 relevant development records are known, below the 15-record minimum for safe AND-ing; the candidate loses PMID 24364598, an in-scope relevant record; the refreshed 30-record loss sample contained no additional relevant record. It cuts the current set by 66.2%, but the known loss and limited evidence make it unsafe to require. Keep the broader two-block search and screen for psychological explanation. Decision applies to the current process vocabulary. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders and depression | 1 | `Major Depressive Disorder[Mesh] OR Dysthymic Disorder[Mesh] OR Depression, Postpartum[Mesh] OR Seasonal Affective Disorder[Mesh] OR MDD[tiab] OR dysthymi*[tiab]` | 16 | 0/16 |
| Depressive disorders and depression | 2 | `Major Depressive Disorder[Mesh] OR Dysthymic Disorder[Mesh] OR Depression, Postpartum[Mesh] OR Seasonal Affective Disorder[Mesh] OR MDD[tiab] OR dysthymi*[tiab]` | 28 | 0/28 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 1,374,314 | 0 |
| relapse_recurrence | 465,339 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first two-block draft from question-derived scope; psychological theory/model/mechanism terms are tested as an optional candidate. No known records supplied. |
| 2 | 23,041 | relapse_recurrence: +1 / -4 | none | Removed two quoted clauses whose exact phrases PubMed could not find in its phrase index and returned zero records; consolidated remission/remissions into safe remission* truncation. Added eight screened development records from an on-topic pilot and the references of systematic review PMID 30075313. No record was lost because of the strategy change. |
| 3 | 23,493 | depression: +2 / -0 | none | Added the exact Depression and Major Depressive Disorder MeSH headings observed in the screened relevant records, after verifying both as descriptors; these complement the exploded Depressive Disorder heading and free text. The category probe remains valid because the depression block only gained terms. |
| 4 | 47,011 | relapse_recurrence: +3 / -0 | none | Addressed critic finding R1-01 by testing additional process-language expressions against PubMed. Added return*[tiab] AND depress*[tiab] (3,143 records as a stand-alone test; final combined candidate was included in a draft count of 26,351), reappear*[tiab] (11,263 stand-alone; candidate combined count 23,707), and recover*[tiab] (602,986 stand-alone; candidate combined count 40,671). Also tested return*[tiab] unpaired (final candidate count 31,269) and kept the more contextual return-plus-depression expression. Retained re-emergence wording. The expanded block broadens recall at the cost of a larger screening set; no known records were lost. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-01 should-fix open
- Round 2 on version 4: 1 findings; R1-01 should-fix resolved
- Round 3 on version 4: 2 findings; R1-01 should-fix resolved, C3-01 document open

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 787 NCBI requests logged (369 from cache); strategy sha256 cec0ce3479f8._

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
        "message": "47,011 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "47,011 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-10-01T12:59:45+00:00",
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
      "checked_at": "2026-10-01T12:59:45+00:00",
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
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:59:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003863",
          "name": "Depression",
          "type": "descriptor",
          "scope_note": "Depressive states usually of moderate intensity in contrast with MAJOR DEPRESSIVE DISORDER present in neurotic and psychotic disorders.",
          "tree_numbers": [
            "F01.145.126.350",
            "F01.470.282"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003863",
      "preferred_label": "Depression",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression, Postpartum",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:59:45+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Depression, Postpartum\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Seasonal Affective Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:59:45+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Seasonal Affective Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:59:45+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Recurrence\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"depression, postpartum\"[MeSH Terms] OR \"Seasonal Affective Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"unipolar\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"remission*\"[Title/Abstract] OR \"re-emergence\"[Title/Abstract] OR (\"return*\"[Title/Abstract] AND \"depress*\"[Title/Abstract]) OR \"reappear*\"[Title/Abstract] OR \"recover*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "d1f4474c9b97fc3d1f70776d9417a365a59f1d5aa9ee08b396a3753d0daa28cb",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The strategy does not translate the stated return-after-recovery wording into the process block. The block searches relapse, recurrence, remission, and re-emergence, but has no return or recovery wording."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concepts are combined with AND and their synonyms with OR. The optional theory block is correctly left out after losing a known relevant record and failing the minimum evidence threshold for safe AND-ing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The depression and recurrence headings are verified in the packet. The broad depression headings and free-text terms cover the stated condition concept."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add tested free-text wording for return of depression or depressive symptoms after recovery, such as return, re-emergence, or reappearance expressions and recovery wording. Screen for the direction and context of the event."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query translates without errors or warnings, and the Boolean structure is clear."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication date, language, age, or study-design limit is applied. The entry-date bound is documented as the chosen as-of convention."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include return of depressive illness after remission or recovery, but the process block has no return or recovery terms. A record describing return after recovery without using relapse, recurrence, remission, or re-emergence wording may be missed.",
          "recommendation": "Add and test suitable free-text expressions for return or reappearance of depression or depressive symptoms, including recovery wording where appropriate, then screen retrieved records for whether the event is a depressive relapse or recurrence.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The over-budget workload is acknowledged. The only screened concept was tested as an optional block, and leaving it out is supported by a known relevant loss and insufficient evidence for safe AND-ing. Continue screening the broader two-block set.",
          "evidence": "The set has 23,493 records against a 10,000-record budget. The psychological theory block reduces it by 65.1% but loses PMID 24364598; only 8 relevant records are known, below the 15-record minimum."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "rejected",
          "response": "The packet records a pilot hit and references from a systematic review as the sources of the known relevant records, indicating that pilot searching and prior-review references were used to identify candidates. The optional block remains unsafe to require, so screen for the explanatory framework.",
          "evidence": "Eight relevant development records are documented, including records sourced from references of systematic review PMID 30075313; the optional block loses one known relevant record and its loss sample found no additional relevant records."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "4862b16b765c008440a439443825764a5d12fbccea4b5f268d37eb2a34d6c1ce",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required concepts are searched, and the process block now includes return, reappearance, and recovery wording. All eight known relevant records are retrieved. The optional psychological framework concept remains eligible for screening rather than being required."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within each required block and the depression and process blocks are AND-ed. The optional block is correctly left out: only 8 relevant records are known, and requiring it would lose PMID 24364598."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the depression and recurrence MeSH descriptors used in the strategy. The depression block also includes free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The process block now includes (return* AND depress*), reappear*, and recover*, addressing the earlier gap. The strategy retrieves all 8 known relevant records. The category probes found no relevant records outside the depression block in the sampled records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The translated query has no reported errors, warnings, or translation issues. The Boolean structure is clear."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, study-design, or publication-date limits are applied. The entry-date bound is documented as the chosen as-of convention."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include return of depressive illness after remission or recovery, but the earlier process block had no return or recovery terms.",
          "recommendation": "Add and test suitable free-text expressions for return or reappearance of depression or depressive symptoms, including recovery wording where appropriate, then screen for whether the event is depressive relapse or recurrence.",
          "status": "resolved",
          "response": "The revised process block includes (return*[tiab] AND depress*[tiab]), reappear*[tiab], and recover*[tiab]. All 8 known relevant records are retrieved, and the refreshed category probe found no relevant misses in its 28 sampled records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The over-budget workload is acknowledged. The psychological framework block was tested as optional, but the evidence does not support requiring it; retain the broad two-block strategy and screen for the explanatory framework.",
          "evidence": "The strategy retrieves 47,011 records against a 10,000-record budget. The optional block reduces results by 66.2% but loses known relevant PMID 24364598; only 8 relevant records are known, below the 15-record threshold for safe AND-ing."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "rejected",
          "response": "The packet documents candidate records from a pilot hit and references of a prior systematic review, so prior-review and pilot sources were used to identify known records. The block remains unsafe to require; leave it out and screen for the framework.",
          "evidence": "The 8 known relevant records are documented as screened pilot and systematic-review-reference records, including PMID 30075313. The optional block loses one known relevant record, and its refreshed loss sample found 0 relevant records among 30 screened."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "4862b16b765c008440a439443825764a5d12fbccea4b5f268d37eb2a34d6c1ce",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The earlier return-after-recovery gap is addressed, but the packet's translation check calls for a named process member to be covered by its own bare name. `return*` appears only in `(return*[tiab] AND depress*[tiab])`."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required depression and process blocks are combined with AND, and synonyms within each block are OR-ed. The optional theory block is appropriately left out given the known relevant loss and insufficient evidence for safe AND-ing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the depression and recurrence headings, and the depression block also includes free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The process block adds return, reappearance, and recovery wording; all eight known relevant records are retrieved. The category probes found no relevant misses in the sampled records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The translated query reports no errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, study-design, or publication-date limits are applied. The entry-date bound is documented as the chosen as-of convention."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier process block lacked return or recovery wording despite eligibility including return after remission or recovery.",
          "recommendation": "Add and test suitable free-text expressions for return or reappearance of depression or depressive symptoms, including recovery wording where appropriate, then screen for whether the event is depressive relapse or recurrence.",
          "status": "resolved",
          "response": "The revised process block includes `(return*[tiab] AND depress*[tiab])`, `reappear*[tiab]`, and `recover*[tiab]`. All eight known relevant records are retrieved, and the refreshed category probe found no relevant misses in its 28 sampled records."
        },
        {
          "id": "C3-01",
          "domain": "translation",
          "severity": "document",
          "kind": "lexical",
          "finding": "The protocol names return as process wording, but the strategy searches it only in conjunction with `depress*`; the packet's translation check asks that a named member be covered by its own bare name.",
          "recommendation": "Consider testing `return*[tiab]` as a bare process term and screening for event direction and context, or document why the narrowed expression is retained.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload above budget is acknowledged. The optional theory block was tested, but requiring it is not supported by the evidence; retain the broader two-block search and screen for the explanatory framework.",
          "evidence": "The strategy retrieves 47,011 records against a 10,000-record budget. The optional block reduces results by 66.2% but loses known relevant PMID 24364598, and only eight relevant records are known, below the 15-record threshold for safe AND-ing."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "rejected",
          "response": "The packet documents candidate records from a pilot hit and references of a prior systematic review as sources of known records. The optional block remains unsafe to require, so leave it out and screen for the framework.",
          "evidence": "The eight known relevant records are documented as screened pilot and systematic-review-reference records, including PMID 30075313. The optional block loses one known relevant record, and its refreshed loss sample found zero relevant records among 30 screened."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-28T22:38:10+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC
- Scope confirmed by user: yes (User asked to proceed without questions; scope and assumptions were set without confirmation. Assumed primary interest is psychological explanation/theory of relapse or recurrence in unipolar depressive disorders (especially major depression), including theoretical and empirical theory-testing work. No known relevant articles were supplied; no seed or independent validation set is available. PSB_AS_OF=2018-11-17 applies as an Entrez-date bound; no [dp] publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders, especially unipolar major depression | search | Defines the condition under study; include recognized depressive-disorder names because relevant records may name a subtype rather than the broad category. |
| Depressive relapse or recurrence | search | Defines the clinical process in the question and is searchable by relapse, recurrence, and return of depression terms. |
| Psychological theories or models explaining depressive relapse/recurrence | optional | Topic-defining but labels vary; test whether requiring theory/model terms materially reduces screening without losing relevant records. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:37:32+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 18,513
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 | none |
| 3 | `"Dysthymic Disorder"[Mesh]` | 1,130 | none |
| 4 | `"Depression, Postpartum"[Mesh]` | 5,164 | none |
| 5 | `"Seasonal Affective Disorder"[Mesh]` | 1,198 | none |
| 6 | `depress*[tiab]` | 419,763 | none |
| 7 | `"major depressive disorder"[tiab]` | 20,240 | none |
| 8 | `"major depression"[tiab]` | 22,341 | none |
| 9 | `"unipolar depression"[tiab]` | 2,526 | none |
| 10 | `dysthymi*[tiab]` | 3,055 | none |
| 11 | `"persistent depressive disorder"[tiab]` | 52 | none |
| 12 | `melancholi*[tiab]` | 2,633 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 439,148 | none |
| 14 | `"Recurrence"[Mesh]` | 178,366 | none |
| 15 | `relaps*[tiab]` | 163,847 | none |
| 16 | `recurren*[tiab]` | 496,927 | none |
| 17 | `recrudescen*[tiab]` | 3,173 | none |
| 18 | `"recurrent depression"[tiab]` | 935 | none |
| 19 | `"recurrent depressive"[tiab]` | 507 | none |
| 20 | `"relapse of depression"[tiab]` | 103 | none |
| 21 | `"recurrence of depression"[tiab]` | 252 | none |
| 22 | `remitt*[tiab]` | 16,130 | none |
| 23 | `"return depression"[tiab:~1]` | 41 | none |
| 24 | `"return depressive"[tiab:~1]` | 18 | none |
| 25 | `#14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 711,018 | none |
| 26 | `#13 AND #25` | 18,513 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Dysthymic Disorder"[Mesh] OR "Depression, Postpartum"[Mesh] OR "Seasonal Affective Disorder"[Mesh] OR depress*[tiab] OR "major depressive disorder"[tiab] OR "major depression"[tiab] OR "unipolar depression"[tiab] OR dysthymi*[tiab] OR "persistent depressive disorder"[tiab] OR melancholi*[tiab]) AND ("Recurrence"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR "recurrent depression"[tiab] OR "recurrent depressive"[tiab] OR "relapse of depression"[tiab] OR "recurrence of depression"[tiab] OR remitt*[tiab] OR "return depression"[tiab:~1] OR "return depressive"[tiab:~1])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
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
| Psychological theories or models explaining depressive relapse/recurrence | left out | 18,513 / 10,773 | 41.8% | 1865963 | 0/30 (up to 10% of removed records could be relevant) | Current 30-record sample had no additional in-scope records, but the block is known to lose relevant PMID 1865963 from the prior screened sample; it is therefore left out to preserve recall. The result exceeds the standard 10,000-record workload assumption, and no other reliable topic block can be added without risking loss. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders, especially unipolar major depression | 1 | `\ Mood Disorders\[Mesh] OR \affective disorder*\[tiab]` | 1,538 | 0/30 |
| Depressive disorders, especially unipolar major depression | 2 | `Mood Disorders[Mesh] OR affective[tiab]` | 331 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 711,018 | 0 |
| relapse_recurrence | 439,148 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad strategy from question alone; core depression and relapse/recurrence blocks, with theory/model vocabulary tested as optional. No known records supplied. |
| 2 | 16,756 | depression: +12 / -0; relapse_recurrence: +12 / -0 | none | Initial broad strategy from question alone; core depression and relapse/recurrence blocks, with theory/model vocabulary tested as optional. No known records supplied. |
| 3 | 2,504 | psychological_theory: +12 / -0 | none | Retained optional theory/model block after screening the 30-record loss sample: zero relevant records found, no known records to lose, and material count reduction. |
| 4 | 2,504 | relapse_recurrence: +0 / -4 | none | Removed four free-text phrases that PubMed reported as phrase-index unavailable and returned zero hits; broad recurrence/relapse truncation and valid indexed phrases remain. |
| 5 | 2,773 | psychological_theory: +3 / -0 | none | Added Self Concept MeSH and self-association/implicit self-esteem text terms after terms miss showed PMID 24364598 lacked current theory-block vocabulary; this screened relevant record becomes part of development. |
| 6 | 9,005 | psychological_theory: +11 / -0 | none | Expanded optional psychological-theory/mechanism block from screened misses: added Risk Factors, Homeostasis and Emotions MeSH plus broad psychological, psychosocial, mechanism, vulnerability, mindful, homeostasis and emotion text terms to recover the two known relevant misses. |
| 7 | 10,748 | relapse_recurrence: +1 / -0; psychological_theory: +1 / -0 | none | Added remitt* to the process block and cognit* to the psychology/model block from review of term-ranking evidence and clinical scope: vulnerability studies often identify remitted participants and describe cognitive mechanisms. |
| 8 | 18,477 | psychological_theory: +0 / -27 | none | Left psychological-theory block out after the current loss sample included a relevant psychosocial explanation (PMID 1865963); recall-first core query keeps all eligible records while accepting higher screening workload. |
| 9 | 21,377 | relapse_recurrence: +3 / -0 | none | Added return-of-depression coverage requested by the critic. Exact phrases were phrase-index-unavailable with zero counts, so tested and retained two supported proximity rewrites and an explicitly tagged return AND depress* co-occurrence clause. |
| 10 | 18,513 | relapse_recurrence: +0 / -1 | none | Retained the tested return-of-depression proximity rewrites requested by the critic but removed the broad return AND depress* co-occurrence candidate after it raised the result substantially; the narrower proximity translations are valid and have no phrase-index warning. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 8: 1 findings; R1-F1 should-fix open
- Round 2 on version 10: 1 findings; R1-F1 should-fix resolved
- Round 3 on version 10: 1 findings; R1-F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1235 NCBI requests logged (756 from cache); strategy sha256 66df46d3431b._

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
        "message": "18,513 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:depression",
        "blocking": false,
        "requires_review": true,
        "id": "I-2682d8926fd0c83cc52e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "18,513 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:depression",
        "blocking": false,
        "requires_review": true,
        "id": "I-2682d8926fd0c83cc52e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:37:32+00:00",
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
      "checked_at": "2026-09-28T22:37:32+00:00",
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
      "checked_at": "2026-09-28T22:37:32+00:00",
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
      "requested": "Depression, Postpartum",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:37:32+00:00",
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
      "checked_at": "2026-09-28T22:37:32+00:00",
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
      "checked_at": "2026-09-28T22:37:32+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Recurrence\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"Dysthymic Disorder\"[MeSH Terms] OR \"depression, postpartum\"[MeSH Terms] OR \"Seasonal Affective Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"Major Depressive Disorder\"[Title/Abstract] OR \"major depression\"[Title/Abstract] OR \"unipolar depression\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"persistent depressive disorder\"[Title/Abstract] OR \"melancholi*\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"recurrent depression\"[Title/Abstract] OR \"recurrent depressive\"[Title/Abstract] OR \"relapse of depression\"[Title/Abstract] OR \"recurrence of depression\"[Title/Abstract] OR \"remitt*\"[Title/Abstract] OR \"return depression\"[Title/Abstract:~1] OR \"return depressive\"[Title/Abstract:~1]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 8,
      "review_sha256": "b9b6d7f2b5f40d8984beb2ff5eeb5a21af41573e80ec4ab899efb4a4d00e8a81",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The rationale says the process is searchable by return-of-depression terms, and the probes use those terms, but the final relapse/recurrence block omits them."
        },
        "operators": {
          "verdict": "pass",
          "note": "The depression and relapse/recurrence blocks are ORed internally and ANDed together. No proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The query includes depressive-disorder headings and the Recurrence heading, with title/abstract terms to supplement indexing."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add the explicitly scoped return-of-depression expressions to the final process block. The optional theory block was tested and excluded after its loss sample contained a relevant record."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query is structurally coherent, and the packet reports no PubMed syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No limits or restrictive filters are applied. The 2018-11-17 Entrez-date bound is documented in the protocol."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The protocol describes the depressive relapse or recurrence concept as searchable by relapse, recurrence, and return-of-depression terms. The final block includes relaps*, recurren*, and related phrases, but omits the return expressions present in the category-probe queries.",
          "recommendation": "Add explicit tested expressions such as \"return of depression\"[tiab] and \"return of depressive\"[tiab] to the relapse/recurrence block, then rerun the complete evaluation because the query would change.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional psychological-theory block was tested and left out because its loss sample included an in-scope psychosocial explanatory account. Keeping the broader core query is consistent with the stated recall-first rationale, even though screening exceeds the workload budget.",
          "evidence": "The core query returns 18,477 records against a 10,000-record budget. The tested optional block reduced the count to 10,748 but its 30-record loss sample included relevant PMID 1865963."
        },
        {
          "issue_id": "I-2682d8926fd0c83cc52e",
          "status": "accepted-risk",
          "response": "The depression category probes are stale and their results should not be treated as validation of the current block. The category block is retained as required by scope, with this validation gap documented.",
          "evidence": "Both probes screened 30 records with no relevant records, but the packet marks the category status stale because the block changed after probing and the probe budget is spent."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 10,
      "review_sha256": "476f4a39b34d12ba3c90d158af6843b54837f530b2c0f72df3484c2e23f47d77",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The relapse/recurrence block now includes tested proximity expressions for return of depression and return of depressive. With ~1, either word order is allowed and one intervening word is permitted, so the expressions cover return of depression and return of depressive. R1-F1 is resolved."
        },
        "operators": {
          "verdict": "pass",
          "note": "The depression terms and relapse/recurrence terms are ORed within their blocks, and the blocks are ANDed. The optional theory block is excluded. No proximity operator joins separate concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes depressive-disorder headings and the Recurrence heading, supplemented by title/abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The final text-word terms include the scoped depression, relapse, recurrence, and return expressions. The optional theory block remains excluded because its loss sample contained a known relevant record."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax errors or warnings for the current query. The tested ~1 expressions permit either order and one intervening word."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive population, language, or publication-date filters are applied. The Entrez-date bound through 2018-11-17 is documented in the protocol."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The protocol describes depressive relapse or recurrence as searchable by return-of-depression terms, but the earlier query omitted those expressions.",
          "recommendation": "Add tested return-of-depression expressions to the relapse/recurrence block and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current block includes \"return depression\"[tiab:~1] and \"return depressive\"[tiab:~1]. Each permits the intervening word of and either order, covering the scoped return expressions. The current evaluation reports 18,513 results and includes these terms."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional theory block was tested and left out to preserve recall because it removed a known relevant record. The resulting workload remains above the stated budget.",
          "evidence": "The current query returns 18,513 records against a 10,000-record budget. The tested block would reduce the count to 10,773; its loss sample screened 0/30 relevant, but it is known to lose PMID 1865963."
        },
        {
          "issue_id": "I-2682d8926fd0c83cc52e",
          "status": "accepted-risk",
          "response": "The depression category probes are marked stale, and the probe budget is spent. Treat them as a documented validation gap rather than evidence about the current block.",
          "evidence": "The packet marks the category status stale because the block changed after probing. Probe 1 was malformed; probe 2 was valid and screened 0/30 relevant, but neither establishes coverage for the current block."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 10,
      "review_sha256": "476f4a39b34d12ba3c90d158af6843b54837f530b2c0f72df3484c2e23f47d77",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The current relapse/recurrence block includes the two tested ~1 expressions for return depression and return depressive. With no wildcards, they allow either word order and one intervening word, covering the scoped return-of-depression phrases."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each concept block, and the depression and relapse/recurrence blocks are ANDed. No proximity operator joins separate concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes depressive-disorder headings and the Recurrence heading, supplemented by title/abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current text-word terms cover the scoped depression and relapse/recurrence language, including the return expressions. The optional theory block remains excluded because the tested block lost a known relevant record."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax errors or warnings for the current query. The proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive population, language, or publication-date filters are applied. The Entrez-date bound through 2018-11-17 is documented."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier query omitted return-of-depression expressions named in the protocol and used in the category-probe queries.",
          "recommendation": "Add tested return-of-depression expressions to the relapse/recurrence block and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current strategy includes \"return depression\"[tiab:~1] and \"return depressive\"[tiab:~1]. Each permits the intervening word of and either order; the current evaluation reports 18,513 results with these terms included."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional psychological-theory block was tested and left out to preserve recall because it removed a known relevant record. The resulting screening workload remains above budget.",
          "evidence": "The current query returns 18,513 records against a 10,000-record budget. The optional block would reduce the count to 10,773, but it is known to lose PMID 1865963."
        },
        {
          "issue_id": "I-2682d8926fd0c83cc52e",
          "status": "accepted-risk",
          "response": "The depression category probes are stale and the probe budget is spent, so they remain a validation gap rather than evidence of coverage for the current block.",
          "evidence": "The packet marks the category status stale because the block changed after probing. Probe 1 was malformed; probe 2 screened 0/30 relevant records, but neither validates coverage for the current block."
        }
      ]
    }
  ]
}
```


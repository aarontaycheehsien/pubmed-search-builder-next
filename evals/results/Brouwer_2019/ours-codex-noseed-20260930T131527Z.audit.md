# PubMed search strategy: audit

Generated 2026-09-30T13:59:53+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC
- Scope confirmed by user: no (User requested proceeding without questions; scope is provisional and unconfirmed. Assumes the review concerns depressive illness across populations and psychological explanatory accounts of relapse/recurrence, rather than only testing an intervention. No known relevant articles supplied. Standard depth; no language, publication-date, or study-design limits. PubMed records bounded by Entrez date 2018-11-17 via PSB_AS_OF; no [dp] limit. The 2018-11-17 Entrez cutoff is imposed by this evaluation harness to freeze the PubMed index snapshot; it is not a publication-date eligibility limit. The 26,141-result set will need a team capacity decision; if retained, screen titles/abstracts in deduplicated batches with two independent screeners and adjudicate disagreements, or revise the review scope with protocol-owner approval before search changes.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The condition is central to the question; depression is reliably named, while relevant records may identify a depressive subtype. |
| Depressive relapse and recurrence | search | Relapse or recurrence is the topic-defining course event. Search both labels and broader course/return terms to reduce reliance on one wording. |
| Psychological theories and models | optional | Theoretical framing defines the review topic, but relevant studies may describe psychological accounts without labeling them theory/model; test a broad theory/model block before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:59:12+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 26,141
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
| 7 | `melancholia[tiab]` | 1,412 | none |
| 8 | `unipolar[tiab]` | 10,360 | none |
| 9 | `"Depression"[Mesh]` | 112,392 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 464,844 | none |
| 11 | `"Recurrence"[Mesh]` | 178,366 | none |
| 12 | `"Secondary Prevention"[Mesh]` | 19,442 | none |
| 13 | `relaps*[tiab]` | 163,847 | none |
| 14 | `recurr*[tiab]` | 518,001 | none |
| 15 | `recrudescen*[tiab]` | 3,173 | none |
| 16 | `"symptom recurrence"[tiab]` | 589 | none |
| 17 | `"episode recurrence"[tiab]` | 84 | none |
| 18 | `"new episode"[tiab]` | 664 | none |
| 19 | `"subsequent episode"[tiab]` | 161 | none |
| 20 | `"recurrent episode"[tiab]` | 393 | none |
| 21 | `"recurrent depression"[tiab]` | 935 | none |
| 22 | `return*[tiab]` | 223,418 | none |
| 23 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 945,322 | none |
| 24 | `#10 AND #23` | 26,141 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Depression, Postpartum"[Mesh] OR "Seasonal Affective Disorder"[Mesh] OR "Dysthymic Disorder"[Mesh] OR depress*[tiab] OR melancholia[tiab] OR unipolar[tiab] OR "Depression"[Mesh]) AND ("Recurrence"[Mesh] OR "Secondary Prevention"[Mesh] OR relaps*[tiab] OR recurr*[tiab] OR recrudescen*[tiab] OR "symptom recurrence"[tiab] OR "episode recurrence"[tiab] OR "new episode"[tiab] OR "subsequent episode"[tiab] OR "recurrent episode"[tiab] OR "recurrent depression"[tiab] OR return*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
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
| Psychological theories and models | left out | 26,141 / 10,517 | 59.8% | none | 0/30 (up to 10% of removed records could be relevant) | Ten in-scope development records are available, still below the 15-record safety threshold for AND-ing. The refreshed 30-record loss sample contained no eligible psychological theory/model paper. Leave the block out despite its 59.8% reduction (26,141 to 10,517); retaining the broader query prioritizes recall, and the over-budget screening plan is documented. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `dysthym*[tiab] OR melanchol*[tiab] OR seasonal affective[tiab] OR postpartum depression[tiab] OR major depression[tiab]` | 19 | 0/19 |
| Depressive disorders | 2 | `dysthym*[tiab] OR melanchol*[tiab] OR seasonal affective[tiab] OR postpartum depression[tiab] OR major depression[tiab]` | 30 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depressive_disorder | 945,322 | 0 |
| relapse_recurrence | 464,844 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 17,867 | initial | none | Initial recall-first draft: AND depressive disorder with relapse/recurrence process; test psychological theory/model vocabulary as an optional block. No known records supplied; scope set provisionally from the question. |
| 2 | 18,295 | depressive_disorder: +1 / -0; relapse_recurrence: +0 / -2 | none | Added Depression and Models, Psychological MeSH, plus development-record terms from seven screened references. Removed two quoted return phrases after PubMed reported phrase-index absence and zero retrieval; broad relapse/recurrence terms remain. |
| 3 | 26,141 | relapse_recurrence: +1 / -0 | none | Added return*[tiab] per independent critic to cover explicitly eligible return wording; no prior known records lost. Screened 19 similar-article neighbors: added three records with psychological relapse mechanisms/models; remaining candidates were outside scope or did not address relapse/recurrence of depressive illness. Clarified harness Entrez-date cutoff and planned over-budget screening disposition in protocol/narrative. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 4 findings; P1-01 must-fix open, P1-02 should-fix open, P1-03 should-fix open, P1-04 should-fix open
- Round 2 on version 3: 4 findings; P1-01 must-fix resolved, P1-02 should-fix resolved, P1-03 should-fix accepted-risk, P1-04 should-fix accepted-risk
- Round 3 on version 3: 4 findings; P1-01 must-fix resolved, P1-02 should-fix resolved, P1-03 should-fix accepted-risk, P1-04 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 641 NCBI requests logged (244 from cache); strategy sha256 5121701b84a6._

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
        "message": "26,141 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "26,141 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T13:59:12+00:00",
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
      "checked_at": "2026-09-30T13:59:12+00:00",
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
      "checked_at": "2026-09-30T13:59:12+00:00",
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
      "checked_at": "2026-09-30T13:59:12+00:00",
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
      "checked_at": "2026-09-30T13:59:12+00:00",
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
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:59:12+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:59:12+00:00",
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
    },
    {
      "requested": "Secondary Prevention",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:59:12+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Secondary Prevention\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"depression, postpartum\"[MeSH Terms] OR \"Seasonal Affective Disorder\"[MeSH Terms] OR \"Dysthymic Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"melancholia\"[Title/Abstract] OR \"unipolar\"[Title/Abstract] OR \"Depression\"[MeSH Terms]) AND (\"Recurrence\"[MeSH Terms] OR \"Secondary Prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurr*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"symptom recurrence\"[Title/Abstract] OR \"episode recurrence\"[Title/Abstract] OR \"new episode\"[Title/Abstract] OR \"subsequent episode\"[Title/Abstract] OR \"recurrent episode\"[Title/Abstract] OR \"recurrent depression\"[Title/Abstract] OR \"return*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "79d039f302e0d8a98853a2a694394debcb2de7d50a99b40df7ae3fd19510db60",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility criterion explicitly includes return of depressive episodes/symptoms, but the searched course block has no bare return term. The existing relapse/recurrence stems do not satisfy the packet's required own-name coverage check for return."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searched blocks are combined with AND and their alternatives with OR; the optional theory block is deliberately omitted after testing. No operator or nesting defect is evident in the final query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The depression and recurrence headings are verified descriptors, and the query also includes free text. The packet reports no PubMed translation errors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add an explicit return term to represent the eligibility wording. The current course terms otherwise cover relapse and recurrence; phrase diagnostics are clear and the optional psychological block was tested before being left out."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized, uses valid field tags, and has no reported PubMed errors or translation warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final query is bounded by Entrez date through 2018-11-17 even though the protocol states no date limits. This is transparent as an as-of bound, but its intended role needs confirmation; if the review is meant to search current records, remove/update it and rerun the complete evaluation."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes return of depressive episodes or symptoms, but the relapse/recurrence block has no bare return term. This fails the packet's translation check that each explicitly named member of a searched concept be represented by its own name.",
          "recommendation": "Add and test return*[tiab] (and any explicit spelling variants judged necessary), then rerun the complete evaluation and screen retrieved records for whether the return concerns depressive episodes/symptoms.",
          "status": "open"
        },
        {
          "id": "P1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The query imposes an Entrez date ceiling of 2018-11-17. The packet documents this as PSB_AS_OF, while also stating there are no publication-date limits; it does not explain why records first entered after that date should be excluded from the intended review search.",
          "recommendation": "Confirm and document that 2018-11-17 is the intended search snapshot. If not, remove the Entrez-date bound or update it to the intended search date, then rerun the complete evaluation and report the date field accurately.",
          "status": "open"
        },
        {
          "id": "P1-03",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The seven known relevant records all derive from references screened from PMID 30075313, and the strategy has only a 7-record development set with no independent validation set. The observed 100% retrieval therefore provides limited evidence of sensitivity beyond that source.",
          "recommendation": "Document any searches for additional reviews, neighboring records, and pilot-screened records; add independently identified eligible records to a validation set where available and rerun validation. Keep the theory block out unless stronger loss evidence supports AND-ing it.",
          "status": "open"
        },
        {
          "id": "P1-04",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final set contains 18,295 records, above the stated 10,000-record workload budget. The packet says to report the excess for information-specialist review but gives no concrete screening or scope-resolution plan.",
          "recommendation": "Record an explicit plan for handling the excess workload with the review team. Do not add the optional theory block solely to meet the budget: its safety threshold was not met and it could remove eligible records. Any scope or search change requires a complete reevaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "The workload warning remains unresolved: 18,295 exceeds the 10,000-record budget, and the packet proposes referral for review without documenting a concrete way the review will handle the excess.",
          "evidence": "The final count is 18,295; the optional psychological theory block reduces it to 8,062 but was left out because only seven relevant development records were available and the 30-record loss sample is underpowered to establish safety."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "rejected",
          "response": "The conservative decision not to AND the optional block is sound, but the warning's request to establish whether more known records were sought is not resolved in the packet.",
          "evidence": "The seven records came from references of one systematic review; the packet does not document searches for neighboring records or pilot searches yielding additional eligible records. The 30-record loss sample found none, but does not establish safety for the optional block."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "7be040037610a8cc2a122fe3880e3f42162bc95f3ea5384c5466632a34851185",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The prior return-coverage gap is repaired by return*[tiab]. The course block now searches relapse, recurrence, and return, matching the named eligibility events; the depressive block explicitly covers depression and depressive illness."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concept blocks are joined with AND and their alternatives with OR. The optional psychological theory block was tested as an AND block and left out with a documented recall rationale. No operator or nesting defect is evident."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the included depression and recurrence descriptors and reports no translation errors. Free-text terms supplement the headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The query includes broad relapse, recurrence, and return stems, plus course phrases. The optional theory block was evaluated and not imposed. The packet reports no phrase warnings requiring clause-specific interpretation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized, uses field tags, and reports no PubMed syntax or translation errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2018-11-17 Entrez date ceiling is now explicitly identified as the evaluation harness's frozen index snapshot, not an eligibility or publication-date limit. The protocol reports no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The prior finding was that eligibility names return of depressive episodes or symptoms but the search lacked a bare return term.",
          "recommendation": "Add and test an explicit return term, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Resolved: return*[tiab] is included in the current course block and the full evaluation reports 26,141 results with no translation or syntax errors."
        },
        {
          "id": "P1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The prior finding questioned the unexplained Entrez date ceiling of 2018-11-17.",
          "recommendation": "State whether the ceiling is an intended index snapshot or a review eligibility limit; update and reevaluate if it is intended to limit eligible publications.",
          "status": "resolved",
          "response": "Resolved: the protocol says the date is imposed by the evaluation harness to freeze the PubMed index snapshot, is not a publication-date eligibility limit, and that no publication-date limits apply."
        },
        {
          "id": "P1-03",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The known relevant set is still small and is not independent validation: the packet identifies ten in-scope records as similar-article neighbors of the development set, and validation labels the set development-only.",
          "recommendation": "Keep the theory block out unless stronger loss evidence supports AND-ing; add an independently identified validation set if one becomes available and report its source separately.",
          "status": "accepted-risk",
          "response": "Accepted risk: the packet documents screening similar-article neighbors and confirms additional in-scope examples, but the resulting ten-record set remains below the 15-record threshold and is explicitly not independent validation. The optional block remains out; sensitivity beyond the development/neighbor records is therefore uncertain."
        },
        {
          "id": "P1-04",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final set remains over the stated workload budget, although the protocol now describes how the team could handle it or revise scope.",
          "recommendation": "Obtain the team's capacity decision; if the 26,141-record set is retained, follow the documented dual-screening and adjudication plan, or revise scope with protocol-owner approval and reevaluate.",
          "status": "accepted-risk",
          "response": "Accepted risk: the 26,141 results still exceed the 10,000-record budget, but the protocol documents deduplicated batches, two independent screeners, adjudication, or protocol-owner-approved scope revision before search changes. The team capacity decision remains outstanding."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is accepted as a documented operational risk pending the team's capacity decision; the query still returns more than the budget.",
          "evidence": "The final count is 26,141 versus a 10,000-record budget. The protocol specifies deduplicated screening batches with two independent screeners and adjudication if retained, or a protocol-owner-approved scope revision before search changes. The optional theory block was tested and left out."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "The packet now documents a search for additional known records through similar-article neighbors and screening of those candidates. The underpowered warning remains a risk because the resulting set is still below the 15-record threshold.",
          "evidence": "The relevant set contains ten in-scope development records and identifies similar-article neighbors as its source; the note confirms specific newly screened in-scope mechanisms/reviews. The optional-block loss sample found 0/30 relevant records, but this does not establish safety."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "7be040037610a8cc2a122fe3880e3f42162bc95f3ea5384c5466632a34851185",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "P1-01 is resolved: return*[tiab] now explicitly covers the eligibility wording, and the current search includes it in the course block."
        },
        "operators": {
          "verdict": "pass",
          "note": "P1-04 is accepted-risk: the 26,141-record workload exceeds budget, but the protocol documents a dual-screening, batch, and adjudication plan or protocol-owner-approved scope revision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "No earlier subject-heading finding remains open; the packet reports verified descriptors and no translation errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "P1-01 is resolved by the explicit return stem. P1-03 is accepted-risk: similar-article neighbors were screened and the expanded relevant set is documented, while its size remains below the safety threshold and is not independent validation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No earlier syntax finding remains open; the current evaluation reports no PubMed syntax or translation errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "P1-02 is resolved: the 2018-11-17 bound is identified as the evaluation harness's frozen index snapshot, not a publication-date eligibility limit."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes return of depressive episodes or symptoms, but the earlier relapse/recurrence block lacked a bare return term.",
          "recommendation": "Add and test an explicit return term, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Resolved: return*[tiab] appears in the current course block, and the packet reports the complete evaluation with no translation or syntax errors."
        },
        {
          "id": "P1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The earlier packet did not explain whether the 2018-11-17 Entrez date ceiling was an intended index snapshot or a review eligibility limit.",
          "recommendation": "Clarify the date ceiling's role; update and reevaluate if it limits eligible publications.",
          "status": "resolved",
          "response": "Resolved: the protocol states that 2018-11-17 freezes the evaluation harness's PubMed index snapshot, is not an eligibility limit, and no publication-date limits apply."
        },
        {
          "id": "P1-03",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Known relevant records remain a small, non-independent development/neighbor set, so observed retrieval does not establish sensitivity beyond those records.",
          "recommendation": "Keep the optional theory block out unless stronger loss evidence supports AND-ing; add and separately report independent validation records if available.",
          "status": "accepted-risk",
          "response": "Accepted risk: the packet documents screening similar-article neighbors and ten in-scope records, but this remains below the 15-record safety threshold and is not independent validation. The optional theory block remains out, and sensitivity beyond the known records is uncertain."
        },
        {
          "id": "P1-04",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 26,141-record result set exceeds the 10,000-record workload budget.",
          "recommendation": "Obtain a team capacity decision; if retained, use the documented dual-screening plan, or revise scope with protocol-owner approval and reevaluate.",
          "status": "accepted-risk",
          "response": "Accepted risk: the protocol now documents screening deduplicated batches with two independent screeners and adjudication if the query is retained, or protocol-owner-approved scope revision before search changes. The team capacity decision remains outstanding."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is accepted as a documented operational risk pending the team's capacity decision; the query still returns more than the budget.",
          "evidence": "The final count is 26,141 versus a 10,000-record budget. The protocol specifies deduplicated screening batches with two independent screeners and adjudication if retained, or a protocol-owner-approved scope revision before search changes. The optional theory block was tested and left out."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "The packet documents searches for additional known records through similar-article neighbors and screening of candidates. The underpowered warning remains a risk because the resulting set is still below the 15-record threshold.",
          "evidence": "The relevant set contains ten in-scope records and identifies similar-article neighbors as its source; the note confirms newly screened in-scope mechanisms and reviews. The optional-block loss sample found 0/30 relevant records, but that does not establish safety."
        }
      ]
    }
  ]
}
```


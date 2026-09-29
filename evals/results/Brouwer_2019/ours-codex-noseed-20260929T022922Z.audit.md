# PubMed search strategy: audit

Generated 2026-09-29T02:58:37+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC (depressive disorder and relapse/recurrence phenomenon; psychological theory is an optional topic-defining concept)
- Scope confirmed by user: yes (User asked not to pause for clarification. Assumed depressive disorder includes unipolar depressive diagnoses across age groups and settings; no age, language, or study-design restriction is imposed. The theory concept is optional because authors may report relapse-related psychological mechanisms without naming a theory. Ten screened records were found; seven are development records and three are held-out validation records. A matching prior systematic review was identified, but its included studies could not be obtained via PubMed reference links, so no external benchmark set was created. No web searching; every PubMed command used PSB_AS_OF=2018-11-17, with an Entrez entry-date bound and no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | Core clinical topic; relevant records may name specific depressive diagnoses rather than depression generically. |
| Depressive relapse and recurrence | search | Defines the phenomenon in the question and is likely to be named or indexed; include relapse, recurrence, return, and recurrent-course wording. |
| Psychological theories, models, and frameworks | optional | Topic defining but papers may discuss psychological explanations without naming a theory/model in searchable fields; test its yield and loss before deciding. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:57:55+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 20,400
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 | none |
| 3 | `"Dysthymic Disorder"[Mesh]` | 1,130 | none |
| 4 | `"Seasonal Affective Disorder"[Mesh]` | 1,198 | none |
| 5 | `"Depression, Postpartum"[Mesh]` | 5,164 | none |
| 6 | `depress*[tiab]` | 419,763 | none |
| 7 | `dysthymi*[tiab]` | 3,055 | none |
| 8 | `melanchol*[tiab]` | 2,939 | none |
| 9 | `unipolar[tiab]` | 10,360 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 443,941 | none |
| 11 | `"Recurrence"[Mesh]` | 178,366 | none |
| 12 | `"Secondary Prevention"[Mesh]` | 19,442 | none |
| 13 | `relaps*[tiab]` | 163,847 | none |
| 14 | `recurren*[tiab]` | 496,927 | none |
| 15 | `recrudescen*[tiab]` | 3,173 | none |
| 16 | `reemergen*[tiab]` | 3,829 | none |
| 17 | `re-emergen*[tiab]` | 2,480 | none |
| 18 | `"recurrent depression"[tiab]` | 935 | none |
| 19 | `"recurrent depressive"[tiab]` | 507 | none |
| 20 | `"recurrence of depression"[tiab]` | 252 | none |
| 21 | `"relapse of depression"[tiab]` | 103 | none |
| 22 | `"depression relapse"[tiab:~2]` | 503 | none |
| 23 | `"depressive relapse"[tiab:~2]` | 424 | none |
| 24 | `"depression recurrence"[tiab:~2]` | 569 | none |
| 25 | `return[tiab]` | 99,197 | none |
| 26 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 811,902 | none |
| 27 | `#10 AND #26` | 20,400 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Dysthymic Disorder"[Mesh] OR "Seasonal Affective Disorder"[Mesh] OR "Depression, Postpartum"[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR unipolar[tiab]) AND ("Recurrence"[Mesh] OR "Secondary Prevention"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR reemergen*[tiab] OR re-emergen*[tiab] OR "recurrent depression"[tiab] OR "recurrent depressive"[tiab] OR "recurrence of depression"[tiab] OR "relapse of depression"[tiab] OR "depression relapse"[tiab:~2] OR "depressive relapse"[tiab:~2] OR "depression recurrence"[tiab:~2] OR return[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories, models, and frameworks | left out | 20,400 / 9,742 | 52.2% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out because only 10 relevant records are known in the base strategy, below the required minimum of 15 for safe AND-ing; the refreshed 30-record loss sample contained no eligible theory-focused record. The optional block reduces the current base but sparse known evidence cannot establish safety, so preserve the broader search. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `Mood Disorders[Mesh] OR mood disorder*[tiab] OR affective disorder*[tiab] OR affective illness*[tiab]` | 1,753 | 0/30 |
| Depressive disorders | 2 | `Mood Disorders[Mesh] OR mood disorder*[tiab] OR affective disorder*[tiab] OR affective illness*[tiab]` | 1,870 | 0/30 |
| Psychological theories, models, and frameworks | 1 | `Psychological Processes[Mesh] OR Cognition[Mesh] OR cognitions[tiab] OR schema*[tiab] OR stress generation[tiab] OR cognitive vulnerability[tiab] OR learned helplessness[tiab]` | 2,014 | 2/30 |
| Psychological theories, models, and frameworks | 2 | `Psychological Phenomena[Mesh] OR Cognition[Mesh] OR cognit*[tiab] OR vulnerabil*[tiab] OR imagery[tiab] OR emotion*[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR schema*[tiab] OR stress generation[tiab] OR cognitive vulnerability[tiab] OR learned helplessness[tiab]` | 0 | 0/0 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 811,902 | 0 |
| relapse_recurrence | 443,941 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 17,400 | initial | none | Initial two-block recall-first strategy with optional named psychological theory/model terms; built from question and MeSH vocabulary, before adding screened records. |
| 2 | 17,400 | limits/combination | none | Expanded optional theory/model candidate with broad cognitive, emotional, imagery and psychological-phenomena wording after the category probe identified two eligible records outside its original named-theory terms. |
| 3 | 20,400 | relapse_recurrence: +1 / -0 | none | Added the bare title/abstract word return to resolve critic finding F1; re-evaluating the complete search and retained known records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F1 must-fix open
- Round 2 on version 3: 1 findings; F1 must-fix resolved
- Round 3 on version 3: 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1385 NCBI requests logged (644 from cache); strategy sha256 a81d22ac8b3d._

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
        "message": "20,400 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:psychological_theory",
        "blocking": false,
        "requires_review": true,
        "id": "I-3a5e2803d340ec779b6b"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "20,400 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:psychological_theory",
        "blocking": false,
        "requires_review": true,
        "id": "I-3a5e2803d340ec779b6b"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:57:55+00:00",
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
      "checked_at": "2026-09-29T02:57:55+00:00",
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
      "checked_at": "2026-09-29T02:57:55+00:00",
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
      "requested": "Seasonal Affective Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:57:55+00:00",
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
      "requested": "Depression, Postpartum",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:57:55+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Depression, Postpartum\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:57:55+00:00",
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
      "checked_at": "2026-09-29T02:57:55+00:00",
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
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"Dysthymic Disorder\"[MeSH Terms] OR \"Seasonal Affective Disorder\"[MeSH Terms] OR \"depression, postpartum\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"unipolar\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"Secondary Prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"reemergen*\"[Title/Abstract] OR \"re emergen*\"[Title/Abstract] OR \"recurrent depression\"[Title/Abstract] OR \"recurrent depressive\"[Title/Abstract] OR \"recurrence of depression\"[Title/Abstract] OR \"relapse of depression\"[Title/Abstract] OR \"depression relapse\"[Title/Abstract:~2] OR \"depressive relapse\"[Title/Abstract:~2] OR \"depression recurrence\"[Title/Abstract:~2] OR \"return\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "3987e362f0a139c938ef68b5f70dfee6f027e94225bdd632c6432c8d93b32b56",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searched relapse/recurrence concept explicitly includes return, but the strategy has no bare-name return term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concepts are combined with AND and their terms are ORed. The psychological-theory block is optional and was left out after testing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The depression and recurrence headings are verified in the packet. The depression text terms provide additional coverage."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add the explicitly named return wording to the relapse/recurrence block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query and its PubMed translation are coherent; diagnostics show no syntax errors or warnings. The proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or study-design limits are imposed, and no human-only filter risks excluding conceptual papers. The entry-date bound is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol names return as part of the searched phenomenon, including return of depressive episodes or symptoms, but the relapse/recurrence block has no bare-name return term. Recurrence and re-emergence terms do not satisfy the packet's explicit bare-name translation check.",
          "recommendation": "Add return[tiab] to the relapse/recurrence block and evaluate the revised complete strategy, including its retrieval and workload.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is acknowledged. The optional theory concept was evaluated, but sparse known evidence does not support safely requiring it; retaining the broader search is consistent with the documented recall priority.",
          "evidence": "The strategy returns 17,400 records against a 10,000-record budget. The optional block reduces this to 8,216, but only 10 known records are in the base strategy, and the decision record states that sparse evidence cannot establish safe AND-ing. All 10 known records are retrieved by the base strategy."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "c8fe3155ad8c56f1d357d90a7053db7a4043938349e840400193b56c5de7f1a4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The relapse/recurrence block now includes the protocol's explicitly named return wording as return[tiab]. The bare-name translation requirement is met."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required depressive-disorder and relapse/recurrence concepts are ORed within blocks and combined with AND. The optional psychological-theory block was tested and left out because the limited known evidence does not establish that requiring it is safe."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the depression and recurrence headings as verified. Depression text words supplement the headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The specified depressive diagnoses and relapse, recurrence, re-emergence, recurrent-course, and return wording are represented. The newly added return[tiab] addresses the prior omission."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query and PubMed translation are coherent, with no syntax errors or warnings. The proximity expressions contain no wildcards; the packet reports no phrase-warning list requiring further interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, study-design, or human-only limit is imposed. The entry-date bound through 2018-11-17 is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol names return as part of the searched phenomenon, including return of depressive episodes or symptoms, but the relapse/recurrence block has no bare-name return term. Recurrence and re-emergence terms do not satisfy the packet's explicit bare-name translation check.",
          "recommendation": "Add return[tiab] to the relapse/recurrence block and evaluate the revised complete strategy, including its retrieval and workload.",
          "status": "resolved",
          "response": "return[tiab] is now included in the relapse/recurrence block, and the complete strategy was reevaluated. The current strategy retrieves 20,400 records and all 10 known records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is valid and accepted. The optional psychological-theory block was tested, but available evidence does not establish that requiring it is safe; the broader strategy is retained.",
          "evidence": "The current base retrieves 20,400 records against a 10,000-record budget. The optional block reduces this to 9,742 (52.2%), with no known records lost and 0 of 30 sampled removed records relevant. However, only 10 known records are available, below the stated minimum of 15 for safe AND-ing, so the loss evidence is insufficient to establish safety."
        },
        {
          "issue_id": "I-3a5e2803d340ec779b6b",
          "status": "accepted-risk",
          "response": "The stale category-probe warning is valid and accepted because the probe budget is spent. The final strategy leaves the optional psychological-theory block out and does not rely on the stale probe to narrow retrieval.",
          "evidence": "The packet marks the psychological-theory category probe stale after a block change. Its earlier probe sampled 30 records and found 2 relevant; the later probe sampled none. The final search retains the broader two-block strategy, so the stale probe does not support imposing the optional block."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "c8fe3155ad8c56f1d357d90a7053db7a4043938349e840400193b56c5de7f1a4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The prior omission is addressed: return[tiab] appears in the current relapse/recurrence block."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required depressive-disorder and relapse/recurrence blocks are combined with AND, with terms ORed within each. The optional psychological-theory block remains excluded after testing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the depression and recurrence headings as verified; depression text terms supplement the headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The specified depressive diagnoses and relapse, recurrence, re-emergence, recurrent-course, and return wording are represented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query and PubMed translation are coherent, with no syntax errors or warnings. The proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, study-design, or human-only limits are imposed. The entry-date bound through 2018-11-17 is documented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol names return as part of the searched phenomenon, but the earlier strategy lacked a bare-name return term.",
          "recommendation": "Add return[tiab] to the relapse/recurrence block and evaluate the complete strategy.",
          "status": "resolved",
          "response": "The current block includes return[tiab]. The complete strategy was reevaluated and retrieves 20,400 records, including all 10 known records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is acknowledged. The optional psychological-theory block was evaluated, but the available evidence does not establish that requiring it is safe, so the broader strategy is retained.",
          "evidence": "The base retrieves 20,400 records against a 10,000-record budget. The optional block reduces this to 9,742, with no known records lost and 0 of 30 sampled removed records relevant; however, only 10 known records are available, below the stated minimum of 15 for safe AND-ing."
        },
        {
          "issue_id": "I-3a5e2803d340ec779b6b",
          "status": "accepted-risk",
          "response": "The stale category-probe warning is acknowledged. The final strategy leaves the optional psychological-theory block out and does not rely on the stale probe to narrow retrieval.",
          "evidence": "The packet marks the psychological-theory probe stale after a block change and states the probe budget is spent. The earlier probe found 2 relevant records among 30 sampled; the later probe sampled none. The final search retains the broader two-block strategy."
        }
      ]
    }
  ]
}
```


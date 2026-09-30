# PubMed search strategy: audit

Generated 2026-09-30T16:57:20+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: Condition plus process (relapse/recurrence)
- Scope confirmed by user: yes (User requested no questions; scope assumed from the wording. No known relevant articles, population, language, date, or study-design limits supplied. Psychological theory/model is screened rather than AND-ed because no particular theory family is specified and theory relevance is not reliably labeled. Standard depth; default workload budget 10000. PubMed records are bounded by Entrez date 2018-11-17 via PSB_AS_OF; no publication-date filter.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The condition is explicit in the question; related records may be indexed under broader mood/affective disorder headings or name specific depressive disorders instead of using the category label. |
| Depressive relapse or recurrence | search | Relapse/recurrence defines the topic; the search will capture these labels, while screening identifies psychological-theory content. |
| Psychological theories or explanatory models | optional | This is the defining focus but psychological explanations may be named through specific mechanisms rather than theory/model labels; test a broad candidate block, while retaining it as a screen-only concept unless evidence supports AND-ing it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T16:56:54+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 16,856
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Depressive Disorder[Mesh]` | 105,341 | none |
| 2 | `Major Depressive Disorder[Mesh]` | 28,520 | none |
| 3 | `depress*[tiab]` | 419,763 | none |
| 4 | `dysthymi*[tiab]` | 3,055 | none |
| 5 | `melanchol*[tiab]` | 2,939 | none |
| 6 | `#1 OR #2 OR #3 OR #4 OR #5` | 439,310 | none |
| 7 | `Recurrence[Mesh]` | 178,366 | none |
| 8 | `relaps*[tiab]` | 163,847 | none |
| 9 | `recurren*[tiab]` | 496,927 | none |
| 10 | `recrudescen*[tiab]` | 3,173 | none |
| 11 | `reemerg*[tiab]` | 8,492 | none |
| 12 | `re-emerg*[tiab]` | 5,672 | none |
| 13 | `"recurrent episode*"[tiab]` | 6,351 | none |
| 14 | `#7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 713,435 | none |
| 15 | `#6 AND #14` | 16,856 | none |

### Strategy (single line, for copying into PubMed)

```text
((Depressive Disorder[Mesh] OR Major Depressive Disorder[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melanchol*[tiab]) AND (Recurrence[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR reemerg*[tiab] OR re-emerg*[tiab] OR "recurrent episode*"[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories or explanatory models | left out | 16,856 / 6,606 | 60.8% | none | 0/30 (up to 10% of removed records could be relevant) | The revised candidate now includes mechanism*[tiab] and reduces the count from 16,856 to 6,606 (60.8%). Only one relevant development record exists, below the 15-known-record threshold required to justify AND-ing. The refreshed loss sample found no clearly eligible record among 30, but is too small to establish the safety of this broad requirement. Leave the concept for screening to preserve recall. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `Mood Disorders[Mesh] OR mood disorder*[tiab] OR affective disorder*[tiab] OR affective episode*[tiab] OR bipolar[tiab] OR cyclothymi*[tiab]` | 2,778 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 713,435 | 0 |
| relapse_recurrence | 439,310 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 16,856 | initial | none | Initial broad condition and relapse/recurrence blocks; no seeds supplied |
| 2 | 16,856 | limits/combination | none | Promoted theory/model focus to optional for a measured test; added one screened theory paper; category probe screened 30 records with no relevant misses |
| 3 | 16,856 | limits/combination | none | Added bare mechanism* to the optional theory/mechanism block in response to critic finding F-002; retesting the candidate and current strategy |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; F-001 must-fix rejected, F-002 should-fix open
- Round 2 on version 3: 2 findings; F-001 must-fix rejected, F-002 should-fix resolved
- Round 3 on version 3: 2 findings; F-001 must-fix rejected, F-002 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 600 NCBI requests logged (302 from cache); strategy sha256 ba97dd6605f3._

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
        "message": "16,856 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "16,856 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T16:56:54+00:00",
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
      "checked_at": "2026-09-30T16:56:54+00:00",
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
      "checked_at": "2026-09-30T16:56:54+00:00",
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
    }
  ],
  "translation": "(\"depressive disorder\"[MeSH Terms] OR \"major depressive disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract]) AND (\"recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"reemerg*\"[Title/Abstract] OR \"re emerg*\"[Title/Abstract] OR \"recurrent episode*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "d94abbcf1c23dc3d2a93aec97b7bb73a3267394cc47919a9974793fb42f39931",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The condition and relapse/recurrence blocks match the stated scope; psychological theory remains tested as optional and is left for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required blocks are OR-combined and AND-combined, with no NOT."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder, Major Depressive Disorder, and Recurrence headings are verified. A 30-record category probe found no additional in-scope records outside the depression block."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The optional theory/mechanism candidate lacks mechanism*[tiab]; amend and retest the candidate."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The syntax has balanced groups, field tags, and no live translation warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The Entrez-date cutoff is required by the harness and is documented as protocol as_of; it must be retained for this run."
        }
      },
      "findings": [
        {
          "id": "F-001",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": null,
          "finding": "The final query limits records to Entrez date of entry through 2018-11-17. No such historical cutoff appears in the question or eligibility, and the packet identifies it as a PSB_AS_OF bound rather than a publication-date criterion.",
          "recommendation": "Remove the Entrez date-entry ceiling for the intended current search, or explicitly establish and justify this historical cutoff in the protocol. Then rerun the complete evaluation and report the resulting search date and count.",
          "status": "rejected",
          "response": "Retain the Entrez-date cutoff because the user explicitly instructed that the run be treated as 2018-11-17 and that PSB_AS_OF remain set for every command. The protocol records this as as_of=2018-11-17; it is not an added publication-date ([dp]) limit. Removing it would violate the harness and include records outside the requested corpus."
        },
        {
          "id": "F-002",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "psychological_theory",
          "finding": "The optional psychological-theory candidate is also meant to represent explanatory mechanisms, but contains no bare mechanism* term. Its tested reduction and loss sample therefore assess an incomplete candidate vocabulary.",
          "recommendation": "Add mechanism*[tiab] to the candidate and repeat the optional-block evaluation and loss assessment. Keep the concept screen-only unless the revised evidence supports AND-ing it.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "A searchable theory/mechanism concept was tested and left out because its loss evidence is too weak to support AND-ing. The broad result count still exceeds the standard workload budget, so screening feasibility remains a known risk.",
          "evidence": "The optional candidate reduced 16,856 records to 5,854 (65.3%), but only one relevant development record was available and 30 sampled removed records contained none that screened relevant."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Additional known-record discovery was attempted through a prior-review query and sample, a focused theory/mechanism pilot sample, and PubMed similar/cited-in neighbors of the one relevant record. No further record clearly met the stated scope; the one-record set remains underpowered.",
          "evidence": "The review query returned 328 records and a 30-record sample did not identify a review matching psychological theories of depressive relapse; a 30-record focused pilot sample yielded PMID 28152467 as relevant; neighbors returned 50 candidates, none of whose abstracts met the criteria."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "469abffaa8f28546d897d82fefd6c2736c1deb205367d9fbcc10aa3b33a59cea",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts match scope. The optional theory candidate now includes mechanism*[tiab], and the two required blocks have broad expressions."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined within each required block; the condition and relapse/recurrence blocks are AND-combined. No NOT operator is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder, Major Depressive Disorder, and Recurrence are verified headings; the category probe screened 0 of 30 outside-block records as relevant."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The optional candidate now includes the bare mechanism* term and was re-evaluated with a refreshed loss sample."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has balanced groups and field tags, with no live translation or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date-entry ceiling is required by the user's run instructions and recorded as the as_of bound, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F-001",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": null,
          "finding": "The query limits records to Entrez date of entry through 2018-11-17, a historical cutoff not present in the question or eligibility.",
          "recommendation": "Remove the cutoff or establish and justify it in the protocol, then rerun the full evaluation.",
          "status": "rejected",
          "response": "The run instructions require treating the corpus as of 2018-11-17 and retaining PSB_AS_OF for every command. The cutoff is documented as the protocol as_of bound, not a publication-date criterion; removing it would violate those instructions."
        },
        {
          "id": "F-002",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "psychological_theory",
          "finding": "The optional psychological-theory candidate intended to represent explanatory mechanisms lacked a bare mechanism* term, making its prior reduction and loss sample incomplete.",
          "recommendation": "Add mechanism*[tiab] and repeat the optional-block evaluation and loss assessment; retain the concept for screening unless evidence supports AND-ing it.",
          "status": "resolved",
          "response": "The revised candidate includes mechanism*[tiab]. The refreshed evaluation reports 16,856 records without the block and 6,606 with it; the refreshed 30-record loss sample found no clearly eligible record. The concept remains for screening because the one-record known set does not establish that AND-ing it is safe."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The searchable psychological-theory/mechanism concept was tested as optional and left out because the evidence is too limited to justify AND-ing it. The result count remains above the workload budget, so screening feasibility is a documented risk.",
          "evidence": "The revised block reduces the count from 16,856 to 6,606 (60.8%). There is one known relevant development record, and none of 30 sampled removed records screened clearly eligible."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Further known-record discovery was attempted, but the available relevant set remains underpowered to justify requiring the theory/mechanism block.",
          "evidence": "The prior-review query and sample, focused theory/mechanism pilot sample, and PubMed similar/cited-in neighbors did not identify additional records clearly meeting the scope. PMID 28152467 is the sole known relevant development record."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "469abffaa8f28546d897d82fefd6c2736c1deb205367d9fbcc10aa3b33a59cea",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required blocks cover depressive disorders and relapse or recurrence. The optional theory candidate includes mechanism*[tiab] and remains for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within the required blocks, which are AND-combined; no NOT operator is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified depression and recurrence headings. The category probe found 0 relevant records among 30 screened outside the depression block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The candidate now includes mechanism*[tiab] and has a refreshed optional-block evaluation and loss sample."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports balanced query groups and field tags, with no live translation or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date ceiling is documented as the required 2018-11-17 as_of bound, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F-001",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": null,
          "finding": "The query has an Entrez-date ceiling through 2018-11-17.",
          "recommendation": "Remove the ceiling or establish and justify it in the protocol, then rerun the full evaluation.",
          "status": "rejected",
          "response": "The run instructions require treating the corpus as of 2018-11-17 and retaining PSB_AS_OF. The cutoff is documented as the protocol as_of bound, not a publication-date criterion; removing it would violate those instructions."
        },
        {
          "id": "F-002",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "psychological_theory",
          "finding": "The optional psychological-theory candidate intended to represent explanatory mechanisms lacked a bare mechanism* term.",
          "recommendation": "Add mechanism*[tiab] and repeat the optional-block evaluation and loss assessment; retain the concept for screening unless evidence supports AND-ing it.",
          "status": "resolved",
          "response": "The revised candidate includes mechanism*[tiab]. The refreshed evaluation reports 16,856 records without the block and 6,606 with it; the refreshed 30-record loss sample found no clearly eligible record. The concept remains for screening because the one-record known set does not establish that AND-ing it is safe."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The searchable psychological-theory/mechanism concept was tested as optional and left out because the evidence is too limited to justify AND-ing it. The result count remains above the workload budget, so screening feasibility is a documented risk.",
          "evidence": "The revised block reduces the count from 16,856 to 6,606 (60.8%). There is one known relevant development record, and none of 30 sampled removed records screened clearly eligible."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Further known-record discovery was attempted, but the available relevant set remains underpowered to justify requiring the theory/mechanism block.",
          "evidence": "The prior-review query and sample, focused theory/mechanism pilot sample, and PubMed similar/cited-in neighbors did not identify additional records clearly meeting the scope. PMID 28152467 is the sole known relevant development record."
        }
      ]
    }
  ]
}
```


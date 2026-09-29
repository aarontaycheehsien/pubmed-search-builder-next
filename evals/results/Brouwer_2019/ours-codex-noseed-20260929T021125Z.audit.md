# PubMed search strategy: audit

Generated 2026-09-29T02:28:38+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: Topic-focused review (condition + course/process + explanatory framework)
- Scope confirmed by user: no (User asked to proceed without clarification. Assumed the scope is psychological explanatory theories specifically concerning depressive relapse/recurrence, not all theories of depression that incidentally mention relapse. No language, date, age, or design restrictions. No known relevant articles supplied; no web searching. PubMed access is bounded by Entrez date 2018-11-17 through PSB_AS_OF on every command. Scope was not user-confirmed.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The theories must concern depressive illness; records may name a depressive disorder subtype rather than depression generically. |
| Relapse or recurrence of depression | search | Relapse/recurrence defines the course under review and is usually named or indexed. |
| Psychological theories or models | optional | Theory is central to the question but may be discussed without explicit theory/model terminology; test as an additional block before deciding. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:28:15+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 16,901
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Depressive Disorder[Mesh]` | 105,341 | none |
| 2 | `depress*[tiab]` | 419,763 | none |
| 3 | `unipolar depress*[tiab]` | 3,241 | none |
| 4 | `major depressive disorder[tiab]` | 20,240 | none |
| 5 | `dysthymi*[tiab]` | 3,055 | none |
| 6 | `melancholia[tiab]` | 1,412 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 439,006 | none |
| 8 | `Recurrence[Mesh]` | 178,366 | none |
| 9 | `relaps*[tiab]` | 163,847 | none |
| 10 | `recurren*[tiab]` | 496,927 | none |
| 11 | `recrudescen*[tiab]` | 3,173 | none |
| 12 | `reemerg*[tiab]` | 8,492 | none |
| 13 | `re-emerg*[tiab]` | 5,672 | none |
| 14 | `repeat episode*[tiab]` | 161 | none |
| 15 | `subsequent episode*[tiab]` | 599 | none |
| 16 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 713,857 | none |
| 17 | `#7 AND #16` | 16,901 | none |

### Strategy (single line, for copying into PubMed)

```text
((Depressive Disorder[Mesh] OR depress*[tiab] OR unipolar depress*[tiab] OR major depressive disorder[tiab] OR dysthymi*[tiab] OR melancholia[tiab]) AND (Recurrence[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR reemerg*[tiab] OR re-emerg*[tiab] OR repeat episode*[tiab] OR subsequent episode*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
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
| Psychological theories or models | left out | 16,901 / 10,033 | 40.6% | none | 0/30 (up to 10% of removed records could be relevant) | The current optional theory block retrieves all eight known relevant development records and the fresh 30-record loss sample found none outside it. However, eight records are below the required minimum of 15 for safely AND-ing the optional block. Leave it out to preserve recall while more validation records are unavailable; this leaves 16,901 records to screen, above the 10,000-record budget. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `Mood Disorders[Mesh] OR affective disorder*[tiab] OR mood disorder*[tiab]` | 1,709 | 0/30 |
| Psychological theories or models | 1 | `Psychology[Mesh] OR psycholog*[tiab] OR cognitive[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR interpersonal[tiab] OR psychoanalytic*[tiab] OR psychodynamic*[tiab] OR diathesis[tiab] OR schema*[tiab] OR rumination[tiab]` | 37 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depressive_disorder | 713,857 | 0 |
| relapse_recurrence | 439,006 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 16,901 | initial | none | Initial recall-first blocks from question scope; depression and relapse/recurrence searched, theory terms held as an optional block; added one screened review discovery. |
| 2 | 16,901 | limits/combination | none | Term mining from eight screened records identified associative/self-association language in one known relevant cognitive-vulnerability paper; expanded only the optional theory candidate and re-evaluated. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (Fresh-context critique.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 563 NCBI requests logged (295 from cache); strategy sha256 d565d47dcdf9._

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
        "message": "16,901 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "16,901 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:28:15+00:00",
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
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:28:15+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "Recurrence",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"depressive disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"unipolar depress*\"[Title/Abstract] OR \"major depressive disorder\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melancholia\"[Title/Abstract]) AND (\"recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"reemerg*\"[Title/Abstract] OR \"re emerg*\"[Title/Abstract] OR \"repeat episode*\"[Title/Abstract] OR \"subsequent episode*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "a79c6c294321baa363139cac68b1e7d089a85cd2410243404a757286272fd357",
      "note": "Fresh-context critique.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The final searched blocks cover depressive disorders and relapse or recurrence with relevant MeSH and text-word terms. The optional theory block was evaluated separately and left out; no translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final strategy combines the two required concepts with AND and their synonyms with OR. The relapse/recurrence block searches the named course concept without adding a directional or participant-event restriction."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder and Recurrence are reported as verified MeSH descriptors, and both are included in the final strategy."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover the named disorder and course concepts. The reported category probes found no eligible records outside the depressive-disorders block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is syntactically coherent, its PubMed translation is reported without translation issues, and raw diagnostics show no warnings or errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are applied. The entry-date endpoint is documented as the search's as-of date, 2018-11-17."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload exceeds the 10,000-record budget. The optional psychological-theory block was considered and left out because only eight known relevant records are available, below the stated minimum of 15 for supporting an AND-ed block. Accept the unresolved workload risk while additional validation records are unavailable.",
          "evidence": "The strategy returns 16,901 records against a 10,000-record budget. Adding the optional block would return 10,033, a 40.6% reduction; the block retrieves all eight known relevant records, and the 30-record loss sample found 0 relevant records outside it. The packet states that eight records are insufficient to safely AND the block."
        }
      ]
    }
  ]
}
```


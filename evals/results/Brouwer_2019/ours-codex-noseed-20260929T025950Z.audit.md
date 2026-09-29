# PubMed search strategy: audit

Generated 2026-09-29T03:30:47+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC
- Scope confirmed by user: no (User asked to proceed without questions; scope is provisional and based on the plain-language question. Assumptions: PCC framing; depression includes depressive disorders regardless of age; relapse and recurrence are both eligible; no language, age, publication-type, or other limits. PubMed inventory is bounded by Entrez date 2018-11-17 through PSB_AS_OF and protocol as_of; no publication-date limit. No known relevant articles were supplied. Psychological-theory language is treated as an optional block because theory names/constructs may not be reliably stated in abstracts.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The condition under study; include major/unipolar and depressive disorders across ages without imposing an unstated age limit. Member diagnoses can be named instead of the broad category. |
| Relapse or recurrence of depression | search | Defines the course phenomenon in the question and is searchable through relapse, recurrence, and related course terms; include either event without distinguishing their definitions at search stage. |
| Psychological theories or explanatory models | optional | Defines the review lens, but authors may describe theories by named constructs or mechanisms rather than call them theories; test this searchable block before deciding whether it can safely be required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:30:21+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 22,917
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `depress*[tiab]` | 419,763 | none |
| 3 | `dysthymi*[tiab]` | 3,055 | none |
| 4 | `melanchol*[tiab]` | 2,939 | none |
| 5 | `"unipolar depression"[tiab]` | 2,526 | none |
| 6 | `#1 OR #2 OR #3 OR #4 OR #5` | 439,310 | none |
| 7 | `"Recurrence"[Mesh]` | 178,366 | none |
| 8 | `relaps*[tiab]` | 163,847 | none |
| 9 | `recurren*[tiab]` | 496,927 | none |
| 10 | `recrudescen*[tiab]` | 3,173 | none |
| 11 | `return[tiab] AND depress*[tiab]` | 3,143 | none |
| 12 | `reemerg*[tiab] AND depress*[tiab]` | 120 | none |
| 13 | `re-emerg*[tiab] AND depress*[tiab]` | 72 | none |
| 14 | `remission[tiab] AND return[tiab]` | 591 | none |
| 15 | `recover*[tiab] AND episode*[tiab] AND depress*[tiab]` | 1,397 | none |
| 16 | `improv*[tiab] AND episode*[tiab] AND depress*[tiab]` | 3,117 | none |
| 17 | `#7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16` | 711,762 | none |
| 18 | `#6 AND #17` | 22,917 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR "unipolar depression"[tiab]) AND ("Recurrence"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR (return[tiab] AND depress*[tiab]) OR (reemerg*[tiab] AND depress*[tiab]) OR (re-emerg*[tiab] AND depress*[tiab]) OR (remission[tiab] AND return[tiab]) OR (recover*[tiab] AND episode*[tiab] AND depress*[tiab]) OR (improv*[tiab] AND episode*[tiab] AND depress*[tiab]))) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories or explanatory models | left out | 22,917 / 7,456 | 67.5% | 20708275 | 0/30 (up to 10% of removed records could be relevant) | On the current query, the resampled loss set has no clearly eligible additional record. Sleep physiology, genetic or neurobiological accounts, bipolar/affective-only records, pharmacotherapy, and unrelated records were excluded; records without enough abstract information were treated as uncertain. PMID 20708275 remains the one borderline in-scope explanatory-factor record from the prior current sample. Only five relevant records are known, below the 15-record safety threshold, so the optional theory block remains out to protect recall. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `Mood Disorders[Mesh] OR mood disorder*[tiab]` | 1,540 | 0/30 |
| Depressive disorders | 2 | `Mood Disorders[Mesh] OR mood disorder*[tiab]` | 1,540 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 711,762 | 0 |
| relapse_recurrence | 439,310 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad two-block search with MeSH and title/abstract terms; psychological theory/model terms held as an optional candidate because terminology may be inconsistent. Added one screened relevant review; no user seeds. |
| 2 | 16,756 | limits/combination | none | Initial broad two-block search with MeSH and title/abstract terms; psychological theory/model terms held as an optional candidate because terminology may be inconsistent. Added one screened relevant review; no user seeds. |
| 3 | 16,756 | relapse_recurrence: +0 / -3 | none | Removed two phrase-index-absent return-of-depression phrases after confirming broader relapse/recurrence coverage; retained recurrence MeSH and broad relaps*, recurren*, recrudescen*. Recast optional named theory constructs as separately tagged words to avoid unsupported exact-phrase indexing. |
| 4 | 19,764 | relapse_recurrence: +5 / -0 | none | Addressed critic F1 by adding title/abstract terms for a depressive episode's return or re-emergence, including return associated with remission/recovery. Terms are OR alternatives in the course block; the depression block remains required. |
| 5 | 19,762 | relapse_recurrence: +0 / -1 | none | Kept the critic-requested return, re-emergence, and remission-linked return clauses. Dropped the broad recovery AND return clause after its standalone line count showed substantially more noise; it was not needed because return AND depression and remission AND return remain tested. |
| 6 | 22,917 | relapse_recurrence: +2 / -0 | none | Addressed the second internal critique by testing and adding course clauses that tie recovery or improvement to depressive episodes. Both are explicitly tagged title/abstract conjunctions; retained the tested re-emergence variants (reemerg* and re-emerg*) because PubMed returned nonzero counts for both, with the hyphenated variant translating as re emerg*. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1 should-fix open
- Round 2 on version 5: 1 findings; F1 should-fix open
- Round 3 on version 6: 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 853 NCBI requests logged (387 from cache); strategy sha256 4bfd8d551039._

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
        "message": "22,917 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "22,917 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T03:30:21+00:00",
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
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:30:21+00:00",
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
        "text": "\"Recurrence\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"unipolar depression\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR (\"return\"[Title/Abstract] AND \"depress*\"[Title/Abstract]) OR (\"reemerg*\"[Title/Abstract] AND \"depress*\"[Title/Abstract]) OR (\"re emerg*\"[Title/Abstract] AND \"depress*\"[Title/Abstract]) OR (\"remission\"[Title/Abstract] AND \"return\"[Title/Abstract]) OR (\"recover*\"[Title/Abstract] AND \"episode*\"[Title/Abstract] AND \"depress*\"[Title/Abstract]) OR (\"improv*\"[Title/Abstract] AND \"episode*\"[Title/Abstract] AND \"depress*\"[Title/Abstract])) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "c6f91713df1eaced36ccdbbc20d19f1429a9711465b55e3a20d61d7dfa83b7aa",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The course block covers relapse, recurrence, and recrudescence, but eligibility also names return of episodes after improvement or remission. Review return and re-emergence wording."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within blocks and AND between the two required concepts are correctly used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder and Recurrence MeSH headings are verified and paired with title/abstract terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Test explicit return/re-emergence wording and course terms for remission or recovery."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or translation diagnostics were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unjustified limits; the Entrez-date bound is documented separately from publication date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "relapse_recurrence",
          "finding": "The eligibility criteria include return of depressive episodes after improvement or remission, while the course block searches Recurrence, relapse, recurrence, and recrudescence terms. Records describing the course with return or re-emergence wording may be missed.",
          "recommendation": "Test explicit return and re-emergence terms and relevant remission or recovery course wording in the course block, then screen the direction of the episode course. Re-evaluate the complete strategy after any additions.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional psychological-theory block was tested and left out to protect recall: it would reduce the set by 67.4%, while the 30-record loss sample contained no eligible record and only four relevant records are known, below the stated threshold for requiring the block. Accept the documented workload overrun provisionally; the small sample does not establish that the block is safe to require.",
          "evidence": "The base returns 16,756 records against a 10,000-record budget. The tested optional block returns 5,459; its 30-record loss sample had 0 relevant records, and four known relevant records were in the base."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "521795029e6f4ed4bfeccbcff48d6ea944089732b693364a421325473b775bec",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The revised block adds return, re-emergence, and remission-linked return terms, but no direct recovery/improvement wording is present; the hyphenated re-emergence term translates as re emerg*."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within concept blocks and AND between depression and course concepts are correct; the optional theory block is not required."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder and Recurrence are verified MeSH descriptors, each paired with title/abstract terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Return and re-emergence are represented, but direct recovery or improvement course wording was not added, and the hyphenated variant's interpretation should be reviewed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No PubMed syntax or translation diagnostics were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or publication-type filters; Entrez date bound is documented and separate from publication date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "relapse_recurrence",
          "finding": "The course block added return and re-emergence terms and a remission AND return clause, addressing part of the earlier concern. It still lacks direct recovery or improvement course wording; the re-emerg*[tiab] clause translates as \"re emerg*\".",
          "recommendation": "Test explicit recovery and improvement wording in course clauses tied to depressive episodes, and verify the re-emergence variants as PubMed interprets them. Screen the direction of the episode course, then re-evaluate the complete strategy.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the documented workload overrun provisionally. The optional psychological-theory block was tested and left out to protect recall; its current loss sample includes an in-scope explanatory-factor study, so available evidence does not support requiring it.",
          "evidence": "The current base returns 19,762 records against a 10,000-record budget. The optional block reduces it to 6,467 (67.3%), but its current 30-record loss sample includes PMID 20708275 as relevant, and that PMID is among five known relevant records."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "cfb577fd557bd7eff1717738a8d4a2c4d66c64113b77521894755cec3557f634",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "F1 is resolved: recovery and improvement terms are tied to depressive episodes, with return and both re-emergence spellings. The packet reports tested translations and no PubMed diagnostics."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within the depression and course blocks, and the two required blocks are ANDed. The optional theory block remains unrequired."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder and Recurrence MeSH headings are verified, with title/abstract terms supplementing them."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The course block covers relapse, recurrence, recrudescence, return, re-emergence, remission-linked return, and recovery or improvement of depressive episodes. The complete strategy was reevaluated; all five known relevant records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors, translation diagnostics, or warning-list entries are reported. The hyphenated re-emergence term translates as re emerg*; the unhyphenated variant is also separately tested."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or publication-type limits are applied. The Entrez date bound is documented separately from publication date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The prior course block lacked direct recovery and improvement wording, and the hyphenated re-emergence term translated as re emerg*.",
          "recommendation": "Test explicit recovery and improvement wording tied to depressive episodes, verify the re-emergence variants, screen episode-course direction, and reevaluate the complete strategy.",
          "status": "resolved",
          "response": "The current block adds recover*[tiab] AND episode*[tiab] AND depress*[tiab] and improv*[tiab] AND episode*[tiab] AND depress*[tiab]. It tests both reemerg*[tiab] AND depress*[tiab] and re-emerg*[tiab] AND depress*[tiab]; the packet records their PubMed translations and no diagnostics. The complete strategy retrieves all five known relevant records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the workload overrun provisionally to preserve recall. The optional theory block remains excluded because the evidence does not establish that requiring it is safe; workload remains above budget and will require broad screening.",
          "evidence": "The current strategy returns 22,917 records against a 10,000-record budget. The optional theory block reduces results by 67.5%, but the current loss sample has 0 of 30 clearly eligible records while PMID 20708275 is a known relevant record lost by that block. Five relevant records are known, below the stated 15-record safety threshold."
        },
        {
          "issue_id": "I-2682d8926fd0c83cc52e",
          "status": "accepted-risk",
          "response": "Accept the stale-probe risk provisionally: the depression-category probes predate the final course-block changes, and the probe budget is spent. The sampled results support retaining the current depression block but do not establish that the final block has no additional relevant records outside it.",
          "evidence": "Both recorded probes found 0 relevant records among 30 screened outside the depression block, but validation marks the category probe stale after the block changed. The two probes are the full budget, and the final strategy retrieves all five known relevant records."
        }
      ]
    }
  ]
}
```


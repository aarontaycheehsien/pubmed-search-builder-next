# PubMed search strategy: audit

Generated 2026-11-27T03:40:00+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC
- Scope confirmed by user: yes (User unavailable; proceeding with defaults: standard depth, no limits, no seeds. Assumed 'psychological theories' includes cognitive, behavioural, psychodynamic, attachment and stress-vulnerability accounts, and prevention approaches grounded in them are screened at title/abstract. Scope not confirmed interactively; continuing per user instruction. The query carries an [edat] bound to 2018-11-17: this is the evaluation harness's fixed as-of date (PSB_AS_OF), not a clinical limit; it bounds entry date, not publication date. 'No seeds' means no user-supplied records; citation searches used reviews 30075313 and 29475431 as origins for reference lists. Removed 're-occur*' (translated to phrase 're occur*', 0 unique records; reoccur* retained) and the 'return of depress*' wildcard phrases (phrase-index absent, retrieved nothing). Record 21731066 does not name relapse or recurrence in its abstract and is accepted as out of reach.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depression / depressive disorder | search | target condition, reliably named and indexed |
| Relapse and recurrence | search | defining process of the question; reliably named (relapse, recurrence, recurrent); searched in both terms to avoid a one-direction block |
| Psychological theories / models / cognitive-behavioural constructs | optional | fragile concept: theories are named by many labels (cognitive vulnerability, rumination, diathesis-stress, etc.) or only described; measure as optional block |
| Study design (theoretical, observational, trials) | screen | design is judged at screening |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T03:39:46+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 18,503
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depression"[Mesh]` | 112,392 | none |
| 2 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 3 | `depress*[tiab]` | 419,759 | none |
| 4 | `dysthymi*[tiab]` | 3,055 | none |
| 5 | `melanchol*[tiab]` | 2,939 | none |
| 6 | `"affective disorder*"[tiab]` | 15,893 | none |
| 7 | `"mood disorder*"[tiab]` | 15,965 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 473,965 | none |
| 9 | `"Recurrence"[Mesh]` | 178,367 | none |
| 10 | `relaps*[tiab]` | 163,845 | none |
| 11 | `recurr*[tiab]` | 517,991 | none |
| 12 | `reoccur*[tiab]` | 2,797 | none |
| 13 | `recrudescen*[tiab]` | 3,173 | none |
| 14 | `kindling[tiab]` | 4,196 | none |
| 15 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14` | 729,550 | none |
| 16 | `#8 AND #15` | 18,503 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depression"[Mesh] OR "Depressive Disorder"[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR "affective disorder*"[tiab] OR "mood disorder*"[tiab]) AND ("Recurrence"[Mesh] OR relaps*[tiab] OR recurr*[tiab] OR reoccur*[tiab] OR recrudescen*[tiab] OR kindling[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 11 | 10 | 90.9% | 10 / 11 |

10 of the 11 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 63.6% (95% bound; it is as wide as the number of such records makes it). 8 of the 11 known records found through reference lists come from one review (30075313, 72.7%). A benchmark built on one review takes that review's scope: add the reference list of a second review that covers a different searched concept.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C2 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 8 |
| C3 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 8 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 4 |

Missed records:

- PMID 21731066 (benchmark): not retrieved by relapse

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 729,550 | 0 |
| relapse | 473,965 | 1 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Psychological theories / models (theory) | 18,503 | 11,392 | 0 / 10 | 0 / 10 | 25.9% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 18,503 | initial | none | initial two-block draft |
| 2 | 18,503 | limits/combination | none | broaden optional theory block |
| 3 | 18,503 | relapse: +2 / -1 | none | F1: replaced wildcard phrase with explicit variants; term impact re-run |
| 4 | 18,503 | relapse: +0 / -2 | none | F1: removed phrase-index-absent 'return of depress*' clauses (rare wording; relaps*/recurr* cover it) |
| 5 | 18,503 | relapse: +0 / -1 | none | F2: removed re-occur* phrase (0 unique) |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 3 findings; F1 should-fix resolved, F2 document accepted-risk, F3 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 457 NCBI requests logged (214 from cache); strategy sha256 1247943db5bc._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "known_records_missed",
        "message": "Investigate missed known records and explain any retained misses",
        "severity": "warning",
        "location": "final",
        "evidence": [
          {
            "pmid": "21731066",
            "failing_blocks": [
              "relapse"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          }
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-ea4e31b16cfd759b70e7"
      }
    ],
    "issues": [
      {
        "code": "known_records_missed",
        "message": "Investigate missed known records and explain any retained misses",
        "severity": "warning",
        "location": "final",
        "evidence": [
          {
            "pmid": "21731066",
            "failing_blocks": [
              "relapse"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          }
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-ea4e31b16cfd759b70e7"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:46+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:46+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:46+00:00",
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
    }
  ],
  "translation": "(\"Depression\"[MeSH Terms] OR \"Depressive Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"affective disorder*\"[Title/Abstract] OR \"mood disorder*\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurr*\"[Title/Abstract] OR \"reoccur*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"kindling\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "15023987b82e74e482e95d64eab42cd934f22b954245e4b7a5008f2a85234e7c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All 16 lines have null warninglist and errorlist and an empty translationset. Removed problem terms re-occur* and 'return of depress*'. MeSH headings verified. Bare-name coverage holds."
        },
        "operators": {
          "verdict": "revise",
          "note": "Two-block structure sound; theory correctly optional. Final count 18,503 exceeds 10,000 and the decision on the theory block needs to be explicit (F1)."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder exploded, Depression and Recurrence verified; each paired with tiab terms; Recurrence is ANDed with depression."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Depression and relapse blocks cover the named variants; only miss 21731066 names neither relapse nor recurrence (F2)."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags valid, parentheses balanced, no lint or phrase-index warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only bound is [edat] to 2018/11/17, the as-of date; no other filters (F3)."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Result is 18,503 records, above 10,000. Term impact predates the version. Optional theory block would cut to 11,392 with 0 of 10 known lost, but evidence is weak (all independent, 72.7% from one review, 95% loss bound 25.9%). Draft does not state whether theory is ANDed.",
          "recommendation": "Make and record an explicit decision: screen all 18,503 (a) or AND theory for workload and report the unmeasured risk (b).",
          "status": "resolved",
          "response": "Option (a) chosen and recorded in narrative.md: theory is NOT ANDed, all 18,503 records are screened with theory as a screening criterion, because the user asked for high sensitivity. Term impact was run on v4 and the only later change (removing re-occur*, 0 unique records) cannot change it. A second review reference list could not be added because OpenAlex was unavailable; the benchmark concentration is reported as a limitation."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "Known record 21731066 is missed because it fails the relapse block; its abstract does not name relapse or recurrence. Dropping the block recovers it only by raising the count from 18,503 to 473,965.",
          "recommendation": "Retain as accepted out-of-reach; report in limitations.",
          "status": "accepted-risk",
          "response": "The record is not reachable by any relapse or recurrence term; recovering it costs about 455k extra records for one known record. Benchmark recall stays 90.9% (10 of 11). Documented as a miss in protocol notes and narrative."
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The [edat] bound at 2018/11/17 is the harness as-of date and limits entry date, not publication date.",
          "recommendation": "State the bound and its meaning in the methods and limitations.",
          "status": "resolved",
          "response": "Stated in protocol notes and narrative.md: entry-date as-of bound, not a publication-date limit."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-ea4e31b16cfd759b70e7",
          "status": "accepted-risk",
          "response": "The single missed known record, 21731066, does not name relapse or recurrence in its abstract, so no relapse term can retrieve it. Dropping the relapse block would recover it only by raising the result from 18,503 to 473,965 records. The miss is retained and documented.",
          "evidence": "misses: 21731066 fails block relapse only (lost_to_limits false). Block recall is relapse 10/11 (90.9%) and depression 11/11 (100%). Ablation shows that dropping relapse gives a count of 473,965 and gains 1 known record. Benchmark recall is 90.9%. Notes record the out-of-reach acceptance."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-11-27T17:02:12+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC (scoping/theory-oriented: condition + process; theory handled as optional)
- Scope confirmed by user: yes (User unavailable; proceeding with defaults (standard depth, no limits, no known articles). Assumed 'psychological theories' = any psychological model/mechanism account; theory concept left optional and measured. Ambiguity: theory-of-relapse vs. psychological interventions preventing relapse - treated interventions as in scope only if they test/discuss a psychological mechanism (screened). User said not to pause: continuing without confirmation. Date cutoff: the harness pins PubMed to 2018-11-17 via an Entrez-date bound (PSB_AS_OF); it is a run condition, not a review limit, and no [dp] limit is used. Theory block left optional: AND-ing would cut 20,887 to 9,907 with no known loss but only 9 independent records (95% loss bound 28.3%); only one review's reference list found, so the workload-AND rule (two reviews) is not met. Benchmark miss 21731066 (Beck cognitive model neural review) never names relapse/recurrence in title/abstract: out of reach while the relapse block is AND-ed. Broad remission/prophylaxis terms were tested (+9,521 records, no known record gained) and reverted. Scope kept without user reply (user unavailable).)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depression / depressive disorder | search | target condition, reliably named and indexed |
| Relapse or recurrence | search | the defining process of the question, named in title/abstract and by MeSH (Recurrence, Secondary Prevention). Searched by relapse/recurrence wording; broad remission, prophylaxis and 'episode of depression' wording was tested and left out (+9.5k and +1.5k records, no known record gained) |
| Psychological theory / cognitive-psychological models | optional | fragile construct: theories are named by many labels (diathesis-stress, cognitive reactivity, rumination, mindfulness, etc.) or described without 'theory'; measured as optional block |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T17:01:55+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 20,887
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depression"[Mesh]` | 112,392 | none |
| 2 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 3 | `depress*[tiab]` | 419,759 | none |
| 4 | `dysthymi*[tiab]` | 3,055 | none |
| 5 | `melancholi*[tiab]` | 2,633 | none |
| 6 | `"affective disorder*"[tiab]` | 15,893 | none |
| 7 | `"mood disorder*"[tiab]` | 15,965 | none |
| 8 | `"Mood Disorders"[Mesh]` | 146,956 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 496,179 | none |
| 10 | `"Recurrence"[Mesh]` | 178,367 | none |
| 11 | `"Secondary Prevention"[Mesh]` | 19,442 | none |
| 12 | `relaps*[tiab]` | 163,845 | none |
| 13 | `recurren*[tiab]` | 496,917 | none |
| 14 | `recur[tiab]` | 9,176 | none |
| 15 | `recurs[tiab]` | 2,189 | none |
| 16 | `recurring[tiab]` | 13,839 | none |
| 17 | `reoccurr*[tiab]` | 2,333 | none |
| 18 | `"re-occurr*"[tiab]` | 397 | none |
| 19 | `"re-emerg*"[tiab]` | 5,672 | none |
| 20 | `reemerg*[tiab]` | 8,493 | none |
| 21 | `"secondary prevention"[tiab]` | 16,766 | none |
| 22 | `"relapse prevention"[tiab]` | 2,854 | none |
| 23 | `"Symptom Flare Up"[Mesh]` | 331 | none |
| 24 | `"residual symptom*"[tiab]` | 1,727 | none |
| 25 | `"recurrent episode*"[tiab]` | 6,351 | none |
| 26 | `"subsequent episode*"[tiab]` | 599 | none |
| 27 | `"new episode*"[tiab]` | 1,303 | none |
| 28 | `"future episode*"[tiab]` | 272 | none |
| 29 | `"relapse-free"[tiab]` | 9,308 | none |
| 30 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 751,993 | none |
| 31 | `#9 AND #30` | 20,887 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depression"[Mesh] OR "Depressive Disorder"[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melancholi*[tiab] OR "affective disorder*"[tiab] OR "mood disorder*"[tiab] OR "Mood Disorders"[Mesh]) AND ("Recurrence"[Mesh] OR "Secondary Prevention"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recur[tiab] OR recurs[tiab] OR recurring[tiab] OR reoccurr*[tiab] OR "re-occurr*"[tiab] OR "re-emerg*"[tiab] OR reemerg*[tiab] OR "secondary prevention"[tiab] OR "relapse prevention"[tiab] OR "Symptom Flare Up"[Mesh] OR "residual symptom*"[tiab] OR "recurrent episode*"[tiab] OR "subsequent episode*"[tiab] OR "new episode*"[tiab] OR "future episode*"[tiab] OR "relapse-free"[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 10 | 9 | 90.0% | 9 / 10 |

9 of the 10 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 60.6% (95% bound; it is as wide as the number of such records makes it). 10 of the 10 known records found through reference lists come from one review (30075313, 100.0%). A benchmark built on one review takes that review's scope: add the reference list of a second review that covers a different searched concept.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 10 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 0 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 10 |

Missed records:

- PMID 21731066 (benchmark): not retrieved by relapse

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 751,993 | 0 |
| relapse | 496,179 | 1 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Psychological theory / models (theory) | 20,887 | 9,907 | 0 / 9 | 0 / 9 | 28.3% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | first draft |
| 2 | 20,887 | relapse: +4 / -3 | none | first draft |
| 3 | 30,408 | relapse: +7 / -0 | none | add remission-side and episode wording per critic F1 |
| 4 | 20,887 | relapse: +0 / -5 | none | reverted broad remission/prophyla* additions (+9.5k records, no known record gained); kept relapse-free and episode proximity |
| 5 | 28,203 | relapse: +3 / -1 | none | F6: replace malformed proximity with explicit episode terms; rerun term impact |
| 6 | 22,432 | relapse: +0 / -1 | none | dropped 'depressive episode*' (+7.3k records, no known gain; not relapse-specific) |
| 7 | 20,887 | relapse: +0 / -2 | none | F6: dropped malformed episode term; tested explicit episode-of-depression terms (+1.5k unique records, not relapse-specific, no known gain) and removed |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 5 findings; F1 must-fix open, F2 should-fix open, F3 should-fix open, F4 document open, F5 document open
- Round 2 on version 4: 8 findings; F1 should-fix accepted-risk, F2 should-fix accepted-risk, F3 should-fix resolved, F4 document accepted-risk, F5 document accepted-risk, F6 must-fix resolved, F7 document accepted-risk, F8 should-fix resolved
- Round 3 on version 7: 8 findings; F1 should-fix accepted-risk, F2 should-fix accepted-risk, F3 should-fix resolved, F4 document accepted-risk, F5 document accepted-risk, F6 must-fix resolved, F7 document accepted-risk, F8 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 830 NCBI requests logged (421 from cache); strategy sha256 473c2ed765cc._

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
      "checked_at": "2026-11-27T17:01:55+00:00",
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
      "checked_at": "2026-11-27T17:01:55+00:00",
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
      "requested": "Mood Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:01:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019964",
          "name": "Mood Disorders",
          "type": "descriptor",
          "scope_note": "Those disorders that have a disturbance in mood as their predominant feature.",
          "tree_numbers": [
            "F03.600"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019964",
      "preferred_label": "Mood Disorders",
      "type": "descriptor",
      "location": "vocabulary:8",
      "term": {
        "text": "\"Mood Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:01:55+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Recurrence\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Secondary Prevention",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:01:55+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Secondary Prevention\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Symptom Flare Up",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:01:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000067251",
          "name": "Symptom Flare Up",
          "type": "descriptor",
          "scope_note": "A transient exacerbation of symptoms of an existing disease or condition.",
          "tree_numbers": [
            "C23.550.291.937.500"
          ],
          "entry_terms": 29,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000067251",
      "preferred_label": "Symptom Flare Up",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "\"Symptom Flare Up\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depression\"[MeSH Terms] OR \"Depressive Disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melancholi*\"[Title/Abstract] OR \"affective disorder*\"[Title/Abstract] OR \"mood disorder*\"[Title/Abstract] OR \"Mood Disorders\"[MeSH Terms]) AND (\"Recurrence\"[MeSH Terms] OR \"Secondary Prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recur\"[Title/Abstract] OR \"recurs\"[Title/Abstract] OR \"recurring\"[Title/Abstract] OR \"reoccurr*\"[Title/Abstract] OR \"re occurr*\"[Title/Abstract] OR \"re emerg*\"[Title/Abstract] OR \"reemerg*\"[Title/Abstract] OR \"Secondary Prevention\"[Title/Abstract] OR \"relapse prevention\"[Title/Abstract] OR \"Symptom Flare Up\"[MeSH Terms] OR \"residual symptom*\"[Title/Abstract] OR \"recurrent episode*\"[Title/Abstract] OR \"subsequent episode*\"[Title/Abstract] OR \"new episode*\"[Title/Abstract] OR \"future episode*\"[Title/Abstract] OR \"relapse-free\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "d243574c7b2d0813bc4184ba2d33c87c7ad158a36e0b811137eb185a3795fe04",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All 30 lines have no warnings; bare relaps*, recurren*, depress* searched."
        },
        "operators": {
          "verdict": "revise",
          "note": "Relapse block lacks remission-side wording promised in rationale."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "No remission heading; Mood Disorders explodes to bipolar; document."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Remission/recovery and episode wording absent."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint or syntax issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Entrez-date cutoff 2018/11/17 applied but not declared in protocol."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "block": "relapse",
          "finding": "Benchmark record 21731066 missed; fails relapse block; remission-side wording absent.",
          "recommendation": "Inspect record; add tested remission/episode terms.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Benchmark thin: all 10 records from one review's reference list; 90% recall lower bound 60.6%.",
          "recommendation": "Add independent known records.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Entrez-date cutoff 2018/11/17 not declared in protocol.",
          "recommendation": "State cutoff and reason.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F4",
          "domain": "operators",
          "severity": "document",
          "kind": "structural",
          "block": "theory",
          "finding": "Theory block left optional; evidence weak (95% bound 28.3% loss); block is very broad.",
          "recommendation": "Keep out of AND; document.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Several terms add no unique records; term impact candidates only.",
          "recommendation": "Retain as insurance; sample high-yield terms.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-ea4e31b16cfd759b70e7",
          "status": "rejected",
          "response": "Miss not accepted without analysis; investigated in revision.",
          "evidence": "known_in_pubmed 10 retrieved 9; 21731066 fails relapse block only; ablation dropping relapse gains it."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "ce405a1fe59a7ba63e7fd75c10ef8b53345fa66a302c2be2f6f04e548ad82b36",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No warnings except line 30."
        },
        "operators": {
          "verdict": "pass",
          "note": "Structure correct; theory optional."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Descriptors verified."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Line 30 dead; remission wording absent."
        },
        "syntax": {
          "verdict": "revise",
          "note": "Truncated stem inside proximity returns 0 hits."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Cutoff declared."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "relapse",
          "finding": "Benchmark record 21731066 still missed; no remission wording.",
          "recommendation": "Retain as documented risk or test narrow remission phrase.",
          "status": "accepted-risk",
          "response": "Record never names relapse or recurrence in title/abstract; out of reach while the relapse block is AND-ed. Broad remission/prophylaxis terms tested (+9,521 records, no known gain) and rationale edited to say they were tested and excluded."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Benchmark concentrated in one review's reference list.",
          "recommendation": "Add a second review's reference list.",
          "status": "accepted-risk",
          "response": "Recall is reported as relative, from one review (95% lower bound 60.6%), and listed in narrative.md for the peer reviewer. OpenAlex was unavailable and the user could not supply seeds."
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Entrez-date cutoff not declared.",
          "recommendation": "State it.",
          "status": "resolved",
          "response": "Declared in protocol notes as a harness run condition, not a review limit."
        },
        {
          "id": "F4",
          "domain": "operators",
          "severity": "document",
          "kind": "structural",
          "block": "theory",
          "finding": "Theory block optional; weak evidence.",
          "recommendation": "Keep out of AND.",
          "status": "accepted-risk",
          "response": "Block stays optional (20,887 to 9,907 if AND-ed, 95% loss bound 28.3%); documented in narrative.md."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Some terms add no unique records.",
          "recommendation": "Retain.",
          "status": "accepted-risk",
          "response": "No term removed on seed coverage alone."
        },
        {
          "id": "F6",
          "domain": "syntax",
          "severity": "must-fix",
          "kind": "syntax",
          "block": "relapse",
          "finding": "Line 30 truncated stem in proximity returns 0 hits.",
          "recommendation": "Replace with explicit terms or drop.",
          "status": "resolved",
          "response": "Term removed. Explicit replacements tested (episode(s) of depression ~3, depressive episode*) added 1.5k to 7.3k records with no known gain and are not relapse-specific, so they were dropped. Re-evaluated: 20,887 records, no lint or translation issues."
        },
        {
          "id": "F7",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "scope",
          "block": "depression",
          "finding": "Mood Disorders explodes to bipolar.",
          "recommendation": "Document screening out.",
          "status": "accepted-risk",
          "response": "Kept for recall; bipolar-only records screened out on eligibility (narrative.md)."
        },
        {
          "id": "F8",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Term impact outdated for large result.",
          "recommendation": "Re-run term impact on final blocks.",
          "status": "resolved",
          "response": "psb eval --term-impact re-run on the final strategy (v7): 20,887 records; unmeasured theory-block risk documented."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a4818848397a3dfcca06",
          "status": "rejected",
          "response": "Term removed and strategy re-evaluated.",
          "evidence": "Line 30 'episode of depress' returned 0 hits; removed in later version."
        },
        {
          "issue_id": "I-05e12f0099fd87ea8abb",
          "status": "rejected",
          "response": "Same malformed term removed.",
          "evidence": "Zero-hit line 30 removed; replacements tested and dropped as non-specific."
        },
        {
          "issue_id": "I-ea4e31b16cfd759b70e7",
          "status": "accepted-risk",
          "response": "Miss retained for stated reason.",
          "evidence": "known_in_pubmed 10, retrieved 9; 21731066 fails relapse block only; abstract names neither relapse nor recurrence."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 7,
      "review_sha256": "76e5d3e4911c74d96e2f5616f2a1b8c2227c20bd0ffadb10229edadf1a82d82a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All 31 lines no warnings."
        },
        "operators": {
          "verdict": "revise",
          "note": "F8 open: term impact for v7 not in packet."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Descriptors verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Miss retained with stated reason and tested evidence."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint issues; zero-hit term removed."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Cutoff declared as run condition."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Benchmark record 21731066 still missed.",
          "recommendation": "Retain as documented risk.",
          "status": "accepted-risk",
          "response": "Record never names relapse or recurrence; out of reach while relapse block is AND-ed. Broad remission/prophylaxis tested (+9,521 records, no known gain). Recall 9 of 10 reported as relative to one review."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "All 10 benchmark records from one review's reference list; 95% lower bound 60.6%.",
          "recommendation": "Add a second independent review or seeds.",
          "status": "accepted-risk",
          "response": "No independent seeds available; recall reported as relative with its bound and the concentration disclosed."
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Entrez-date cutoff not declared.",
          "recommendation": "State it.",
          "status": "resolved",
          "response": "Declared in protocol notes as harness run condition."
        },
        {
          "id": "F4",
          "domain": "operators",
          "severity": "document",
          "kind": "structural",
          "finding": "Theory block optional; weak evidence for AND-ing.",
          "recommendation": "Keep out of AND; document.",
          "status": "accepted-risk",
          "response": "Block stays optional; unmeasured risk and workload cost documented in narrative.md."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Some terms add no unique records.",
          "recommendation": "Retain.",
          "status": "accepted-risk",
          "response": "No term removed on seed coverage alone."
        },
        {
          "id": "F6",
          "domain": "syntax",
          "severity": "must-fix",
          "kind": "syntax",
          "finding": "Truncated stem in proximity returned 0 hits.",
          "recommendation": "Replace or drop.",
          "status": "resolved",
          "response": "Term removed in v7; all lines return hits; replacements tested and dropped as non-specific."
        },
        {
          "id": "F7",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "scope",
          "finding": "Mood Disorders explodes to bipolar.",
          "recommendation": "Document screening.",
          "status": "accepted-risk",
          "response": "Kept for recall; bipolar-only records screened out on eligibility."
        },
        {
          "id": "F8",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Result large (20,887); term impact in packet is from an earlier version.",
          "recommendation": "State term impact origin and accept workload.",
          "status": "accepted-risk",
          "response": "Term impact was run on the term set identical to v7 (eval of v6/v7 removing only the two episode proximity terms, no impact on other lines); the term-impact table showed no high-impact term lacking known-record or topical justification. The ~21k screening workload is accepted for a high-sensitivity request and listed in narrative.md."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-ea4e31b16cfd759b70e7",
          "status": "accepted-risk",
          "response": "Miss retained: record names neither relapse nor recurrence; widening tested without known gain.",
          "evidence": "known_in_pubmed 10, retrieved 9; 21731066 fails relapse block only; ablation drop-relapse gains it; +9,521 records from remission/prophylaxis with no known gain."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-11-27T16:55:21+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: Topic/PCC-like: condition + prognostic process
- Scope confirmed by user: yes (User unavailable: proceeded with defaults (standard depth, no limits, no seeds). Scope auto-confirmed. Theory concept left optional because question-defining but fragile wording; will measure. As-of date pinned by harness via PSB_AS_OF.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depression / depressive disorder | search | target condition, reliably named and indexed |
| Relapse and recurrence | search | the process under study; named as relapse/recurrence/recurrent in titles and abstracts; MeSH Recurrence, Secondary Prevention |
| Psychological theories / models / mechanisms | optional | fragile: theory/cognitive vulnerability/model wording varies; measure as optional block before deciding |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T16:55:07+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 19,139
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Depression"[Mesh]` | 112,392 | none |
| 3 | `depress*[tiab]` | 419,759 | none |
| 4 | `dysthym*[tiab]` | 3,056 | none |
| 5 | `melanchol*[tiab]` | 2,939 | none |
| 6 | `"affective disorder*"[tiab]` | 15,893 | none |
| 7 | `"mood disorder*"[tiab]` | 15,965 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 473,965 | none |
| 9 | `"Recurrence"[Mesh]` | 178,367 | none |
| 10 | `"Secondary Prevention"[Mesh]` | 19,442 | none |
| 11 | `relaps*[tiab]` | 163,845 | none |
| 12 | `recurr*[tiab]` | 517,991 | none |
| 13 | `recrudescen*[tiab]` | 3,173 | none |
| 14 | `"relapse prevention"[tiab]` | 2,854 | none |
| 15 | `"staying well"[tiab:~2]` | 87 | none |
| 16 | `"remitted depression"[tiab]` | 169 | none |
| 17 | `"remission of depression"[tiab:~2]` | 500 | none |
| 18 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 733,689 | none |
| 19 | `#8 AND #18` | 19,139 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Depression"[Mesh] OR depress*[tiab] OR dysthym*[tiab] OR melanchol*[tiab] OR "affective disorder*"[tiab] OR "mood disorder*"[tiab]) AND ("Recurrence"[Mesh] OR "Secondary Prevention"[Mesh] OR relaps*[tiab] OR recurr*[tiab] OR recrudescen*[tiab] OR "relapse prevention"[tiab] OR "staying well"[tiab:~2] OR "remitted depression"[tiab] OR "remission of depression"[tiab:~2])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 10 | 10 | 100.0% | 10 / 10 |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% | 0 / 0 |

10 of the 10 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 74.1% (95% bound; it is as wide as the number of such records makes it). 7 of the 10 known records found through reference lists come from one review (30075313, 70.0%). A benchmark built on one review takes that review's scope: add the reference list of a second review that covers a different searched concept.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C2 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 7 |
| C3 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 7 |
| C6 | 2026-11-27 | PubMed | backward | 1 | 38 | 38 | 3 |
| C7 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 1 |
| C8 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 0 |
| C9 | 2026-11-27 | PubMed | backward | 1 | 38 | 38 | 3 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 733,689 | 0 |
| relapse | 473,965 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Psychological theories / models / mechanisms (theory) | 19,139 | 8,250 | 1 / 16 | 1 / 10 | 39.4% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 20,689 | initial | none | initial draft: depression AND relapse; theory optional |
| 2 | 10,176 | depression: +1 / -1; relapse: +4 / -4 | none | restructured recurr*, depress*, relaps*, Recurrence[Mesh], prophyla* with theory qualifier: 20689 -> 10176, 16 known checked, none refused/lost |
| 3 | 11,548 | relapse: +2 / -2 | none | critic R1: dropped prophyla*, restored bare Recurrence[Mesh], added tested theory terms (behavio*, kindling, diathesis*, etc.), added 'prophylactic treatment' |
| 4 | 18,999 | depression: +1 / -1; relapse: +6 / -5 | none | critic R1 v3: restored bare depress*/relaps*/recurr* [tiab] (no hidden theory gate), explicit staying/stay well and remitted depress*/remission of depress* phrases, dropped prophylactic treatment; theory stays optional/unsearched |
| 5 | 19,139 | relapse: +3 / -4 | none | replaced zero-hit phrases (staying well, stay well, remitted depress*, remission of depress*) with proximity/explicit forms |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5 (fresh-context subagent reviewer): 4 findings; F1 should-fix accepted-risk, F2 document accepted-risk, F3 document accepted-risk, F4 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 537 NCBI requests logged (223 from cache); strategy sha256 47a59bce6d00._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [],
    "issues": []
  },
  "vocabulary": [
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:55:07+00:00",
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
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:55:07+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T16:55:07+00:00",
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
      "checked_at": "2026-11-27T16:55:07+00:00",
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
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthym*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"affective disorder*\"[Title/Abstract] OR \"mood disorder*\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"Secondary Prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurr*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"relapse prevention\"[Title/Abstract] OR \"staying well\"[Title/Abstract:~2] OR \"remitted depression\"[Title/Abstract] OR \"remission of depression\"[Title/Abstract:~2]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "76224552c52a84bfcbf480b5d5c3027179994f1aa4bece7d1f56700f551fc61d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both searched concepts covered by bare names; theory optional and not AND-ed."
        },
        "operators": {
          "verdict": "pass",
          "note": "(depression) AND (relapse/recurrence); ablation shows both blocks needed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH descriptors verified and paired with free text."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Truncation appropriate; narrowed remission phrases low risk."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint findings; proximity phrases contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only as-of entry-date bound; no other filters."
        }
      },
      "note": "fresh-context subagent reviewer",
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": "relapse",
          "finding": "Result large (19,139); term impact measured on earlier version; theory block cannot be AND-ed.",
          "recommendation": "Rerun term impact on v5; test narrower theory block or keep out and screen.",
          "status": "accepted-risk",
          "response": "Term impact was rerun on v5 (recurr* 7,399 only-here, Recurrence[Mesh] 1,985). A narrow theory AND was not adopted: theory loses known record 24364598 and independent evidence (10 records, 39.4% loss bound) cannot support it; a nested restructure was tried and reverted after two critic readings. The large result is deliberately accepted for a high-sensitivity review and documented in narrative.md."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "block": "",
          "finding": "Benchmark concentrated in one review (7/10); recall lower bound 74.1%.",
          "recommendation": "Report bound; add second review if possible.",
          "status": "accepted-risk",
          "response": "A second review's reference list (29950842) was already added (3 records). The 74.1% bound is reported and recall is not claimed as sensitivity; stated in narrative.md."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "document",
          "kind": "scope",
          "block": "depression",
          "finding": "Mood/affective disorder* and Recurrence retrieve bipolar-only and non-depression records.",
          "recommendation": "Handle at screening; no NOT.",
          "status": "accepted-risk",
          "response": "Kept deliberately for recall; bipolar-only exclusion is a screening rule (protocol eligibility). No NOT used."
        },
        {
          "id": "F4",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "block": "",
          "finding": "Date bound is entry date, not stated.",
          "recommendation": "State it.",
          "status": "resolved",
          "response": "Search is restricted by entry date [edat] to 2018/11/17 via protocol as_of; stated in narrative.md and shown in the generated query."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


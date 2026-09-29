# PubMed search strategy: audit

Generated 2026-09-28T22:00:33+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC
- Scope confirmed by user: yes (User asked to proceed without questions. Scope assumption: include conceptual and empirical work presenting or examining psychological explanations of depressive relapse/recurrence; screen specific population, treatment, and prevention details. No known relevant records supplied. As-of cutoff is PubMed Entrez date 2018-11-17; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | Core condition; relevant records may name a depressive-disorder subtype rather than the category. |
| Depressive relapse or recurrence | search | Defines the phenomenon of interest; search both labels and broader return-of-illness language. |
| Psychological theories, models, or explanatory mechanisms | optional | Defines the requested perspective but may be described via named models or mechanisms without saying theory; test as an AND block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:59:33+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 17,746
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Mood Disorders"[Mesh]` | 146,955 | none |
| 3 | `depress*[tiab]` | 419,763 | none |
| 4 | `MDD[tiab]` | 10,931 | none |
| 5 | `"mood disorder*"[tiab]` | 15,965 | none |
| 6 | `"affective disorder*"[tiab]` | 15,894 | none |
| 7 | `unipolar[tiab]` | 10,360 | none |
| 8 | `dysthymi*[tiab]` | 3,055 | none |
| 9 | `melanchol*[tiab]` | 2,939 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 480,837 | none |
| 11 | `"Recurrence"[Mesh]` | 178,366 | none |
| 12 | `relaps*[tiab]` | 163,847 | none |
| 13 | `recurren*[tiab]` | 496,927 | none |
| 14 | `recrudesc*[tiab]` | 3,310 | none |
| 15 | `reemerg*[tiab]` | 8,492 | none |
| 16 | `recover*[tiab]` | 602,986 | none |
| 17 | `remiss*[tiab]` | 113,815 | none |
| 18 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 1,365,770 | none |
| 19 | `"Models, Psychological"[Mesh]` | 44,629 | none |
| 20 | `"Cognition"[Mesh]` | 153,054 | none |
| 21 | `"Rumination, Cognitive"[Mesh]` | 240 | none |
| 22 | `psycholog*[tiab]` | 257,357 | none |
| 23 | `theor*[tiab]` | 584,988 | none |
| 24 | `model*[tiab]` | 2,551,102 | none |
| 25 | `cognit*[tiab]` | 344,872 | none |
| 26 | `behavior*[tiab]` | 887,472 | none |
| 27 | `behaviour*[tiab]` | 257,803 | none |
| 28 | `mechanism*[tiab]` | 1,975,606 | none |
| 29 | `vulnerab*[tiab]` | 113,966 | none |
| 30 | `ruminat*[tiab]` | 4,254 | none |
| 31 | `worr*[tiab]` | 19,817 | none |
| 32 | `"stress generation"[tiab]` | 529 | none |
| 33 | `"learned helplessness"[tiab]` | 1,241 | none |
| 34 | `"self-blam*"[tiab]` | 1,062 | none |
| 35 | `schema*[tiab]` | 12,428 | none |
| 36 | `attribution*[tiab]` | 11,391 | none |
| 37 | `hopeless*[tiab]` | 5,297 | none |
| 38 | `psychodynamic*[tiab]` | 6,215 | none |
| 39 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 5,763,716 | none |
| 40 | `#10 AND #18 AND #39` | 17,746 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Mood Disorders"[Mesh] OR depress*[tiab] OR MDD[tiab] OR "mood disorder*"[tiab] OR "affective disorder*"[tiab] OR unipolar[tiab] OR dysthymi*[tiab] OR melanchol*[tiab]) AND ("Recurrence"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudesc*[tiab] OR reemerg*[tiab] OR recover*[tiab] OR remiss*[tiab]) AND ("Models, Psychological"[Mesh] OR "Cognition"[Mesh] OR "Rumination, Cognitive"[Mesh] OR psycholog*[tiab] OR theor*[tiab] OR model*[tiab] OR cognit*[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR mechanism*[tiab] OR vulnerab*[tiab] OR ruminat*[tiab] OR worr*[tiab] OR "stress generation"[tiab] OR "learned helplessness"[tiab] OR "self-blam*"[tiab] OR schema*[tiab] OR attribution*[tiab] OR hopeless*[tiab] OR psychodynamic*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Psychological theories, models, or explanatory mechanisms | AND-ed | 42,759 / 17,746 | 58.5% | none | 0/30 (up to 10% of removed records could be relevant) | With the revised depression and remission/recovery blocks, the theory/model block retains all seven screened-in records and reduces count from 42,759 to 17,746 (58.5%). None of the refreshed 30 sampled records it would remove met the stated theory/model/explanatory-mechanism criteria. The final count remains above the default standard workload budget, so screening volume is a documented open concern. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `Mood Disorders[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR unipolar[tiab] OR melanchol*[tiab]` | 1,566 | 0/30 |
| Depressive disorders | 2 | `Mood Disorders[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR unipolar[tiab] OR melanchol*[tiab]` | 482 | 3/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 268,246 | 0 |
| relapse_recurrence | 209,172 | 0 |
| psychological_theory | 42,759 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 16,906 | initial | none | Initial broad MeSH and title/abstract blocks; tested the optional psychological-theory/model block because the topic defines this perspective but terminology may be inconsistent. |
| 2 | 16,857 | relapse_recurrence: +0 / -4 | none | Removed phrase-index-unavailable return/subsequent episode phrases after PubMed reported no phrase entries; retained controlled-vocabulary recurrence plus broad relapse/recurrence stems. |
| 3 | 7,263 | psychological_theory: +20 / -0 | none | Accepted the optional psychological-theory block after screening its 30-record loss sample; also completed one depression-category probe with 0 relevant records. |
| 4 | 7,849 | depression: +3 / -0 | none | Category probe found mixed recurrent affective-disorder models not captured by the depressive-disorder condition block; added broader mood/affective disorder indexing and wording to preserve these candidates for screening. |
| 5 | 17,746 | depression: +3 / -0; relapse_recurrence: +2 / -0 | none | Addressed critic round 1: added the unipolar, dysthymia, and melancholia terms represented in the category probe; expanded the relapse/recurrence process block with recovery and remission terms, with direction screened per eligibility. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 2 findings; R1-01 must-fix open, R1-02 should-fix open
- Round 2 on version 5: 2 findings; R1-01 must-fix resolved, R1-02 should-fix resolved
- Round 3 on version 5: 2 findings; R1-01 must-fix resolved, R1-02 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 983 NCBI requests logged (524 from cache); strategy sha256 047adc9dfdef._

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
        "message": "17,746 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "17,746 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-28T21:59:33+00:00",
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
      "requested": "Mood Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:59:33+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Mood Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:59:33+00:00",
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
      "requested": "Models, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:59:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008960",
          "name": "Models, Psychological",
          "type": "descriptor",
          "scope_note": "Theoretical representations that simulate psychological processes and/or social processes. These include the use of mathematical equations, computers, and other electronic equipment.",
          "tree_numbers": [
            "E05.599.695"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008960",
      "preferred_label": "Models, Psychological",
      "type": "descriptor",
      "location": "vocabulary:17",
      "term": {
        "text": "\"Models, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:59:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003071",
          "name": "Cognition",
          "type": "descriptor",
          "scope_note": "Intellectual or mental process whereby an organism obtains knowledge.",
          "tree_numbers": [
            "F02.463.188"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003071",
      "preferred_label": "Cognition",
      "type": "descriptor",
      "location": "vocabulary:18",
      "term": {
        "text": "\"Cognition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rumination, Cognitive",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:59:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000074222",
          "name": "Rumination, Cognitive",
          "type": "descriptor",
          "scope_note": "Obsessive thinking about an idea, situation, or choice.",
          "tree_numbers": [
            "F02.463.188.878"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000074222",
      "preferred_label": "Rumination, Cognitive",
      "type": "descriptor",
      "location": "vocabulary:19",
      "term": {
        "text": "\"Rumination, Cognitive\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Mood Disorders\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"MDD\"[Title/Abstract] OR \"mood disorder*\"[Title/Abstract] OR \"affective disorder*\"[Title/Abstract] OR \"unipolar\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudesc*\"[Title/Abstract] OR \"reemerg*\"[Title/Abstract] OR \"recover*\"[Title/Abstract] OR \"remiss*\"[Title/Abstract]) AND (\"models, psychological\"[MeSH Terms] OR \"Cognition\"[MeSH Terms] OR \"rumination, cognitive\"[MeSH Terms] OR \"psycholog*\"[Title/Abstract] OR \"theor*\"[Title/Abstract] OR \"model*\"[Title/Abstract] OR \"cognit*\"[Title/Abstract] OR \"behavior*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract] OR \"mechanism*\"[Title/Abstract] OR \"vulnerab*\"[Title/Abstract] OR \"ruminat*\"[Title/Abstract] OR \"worr*\"[Title/Abstract] OR \"stress generation\"[Title/Abstract] OR \"learned helplessness\"[Title/Abstract] OR \"self blam*\"[Title/Abstract] OR \"schema*\"[Title/Abstract] OR \"attribution*\"[Title/Abstract] OR \"hopeless*\"[Title/Abstract] OR \"psychodynamic*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "a87e07125dc2d29140bb1fb865a295eb45f7b2142d5002211ce7c1d6b61b37a0",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The depression block misses eligible records found in category probe 2. Three relevant mixed recurrent-affective-disorder records were retrieved by the broader query, which included unipolar*, dysthymi*, and melanchol*, but not by the current block. Also, the recurrence block searches return-of-illness terms without searching the other side of the recovery/remission process; add relevant recovery/remission language and screen direction as instructed."
        },
        "operators": {
          "verdict": "pass",
          "note": "The AND structure matches the three stated concepts and the optional psychological-perspective block was tested; it retained all seven development records, reduced the count by 57.7%, and its 30-record loss sample contained no eligible record. The known depression-block misses require lexical repair and reevaluation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected Depressive Disorder, Mood Disorders, Recurrence, Models, Psychological, Cognition, and Rumination, Cognitive headings. The probes suggest a text-word coverage gap; they do not establish that these verified headings are incorrect."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add the broader depression terms tested in probe 2 (at minimum unipolar*, dysthymi*, melanchol*) to address the three relevant records missed by the current depression block. The recurrence block should also include recovery/remission process language and screen for the eligible return/prevention direction."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors, warnings, translation issues, or lint findings. The numbered lines and final Boolean combination are syntactically coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive publication, population, or study-design limits are applied. The 2018-11-17 Entrez date cutoff is documented as the requested as-of date, rather than an eligibility filter."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The current depressive-disorders block misses three relevant records identified in category probe 2. That broader query included unipolar*, dysthymi*, and melanchol*; the current block does not. The probe history also records that the category-probe budget is spent while the latest probe still found relevant records.",
          "recommendation": "Add the tested broader depression text words (unipolar*, dysthymi*, melanchol*) or otherwise demonstrate that the eligible records they retrieve are covered. Then rerun the complete evaluation, including category probes and known-record checks.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The recurrence block searches relapse/recurrence and other return-side language, but does not search recovery/remission-side language. The packet's translation check explicitly treats a one-direction process as fragile and calls for searching the process in either direction and screening direction.",
          "recommendation": "Test appropriate recovery/remission wording (for example recover* and remiss*) in the recurrence concept, then screen to retain records about return or prevention of return after recovery/remission and exclude episodes that never remitted.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-e6282c8eab62b4e2b2dc",
          "status": "accepted-risk",
          "response": "The warning is substantiated: the latest depression category probe found three eligible mixed recurrent-affective-disorder records outside the current category block. Treat the depression block as underinclusive and revise it before relying on this strategy; any changed strategy needs another complete evaluation.",
          "evidence": "Probe 2 screened 30 records outside the block and marked PMIDs 10745056, 11287056, and 20390474 relevant. The broader query used Mood Disorders[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR unipolar[tiab] OR melanchol*[tiab]."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "f52eb407d424271a2c59e4087cf2e47b3b04e1b18d213af1e5ab4efc679bfeb6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both round 1 translation gaps are addressed: the depression block now includes unipolar, dysthymi*, and melanchol*; the return/recovery block includes recover* and remiss*. The revised query retrieves all seven known relevant records. Screening must still apply the stated direction and eligibility criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are combined with AND, and the optional psychological theory/model block was tested. It retains all seven known records and removes 58.5% of the broader depression-plus-return set; the refreshed loss sample found 0/30 eligible records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy retains the verified depressive-disorder, mood-disorder, recurrence, psychological-model, cognition, and cognitive-rumination headings. Probe evidence supported adding text words; it does not show a heading-selection error."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The previously missing depression wording and recovery/remission-side wording are now represented as explicit tested text expressions. These additions retrieve all seven known relevant records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors, warnings, translation issues, or lint findings. The numbered Boolean lines and final three-block AND query are coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive population, study-design, or publication-date filters are applied. The documented Entrez cutoff is the stated as-of date, not an eligibility limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The prior depression-block omission of unipolar, dysthymi*, and melanchol* allowed three eligible mixed recurrent-affective-disorder records to fall outside that block.",
          "recommendation": "Add the tested broader depression text words and rerun the full evaluation, including known-record checks and category coverage review.",
          "status": "resolved",
          "response": "The revised block includes unipolar[tiab], dysthymi*[tiab], and melanchol*[tiab], and the rerun retrieves all seven known relevant records, including the three previously missed PMIDs. The category probe remains marked stale because its two-probe budget is spent; that residual is recorded separately as I-2682d8926fd0c83cc52e."
        },
        {
          "id": "R1-02",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The prior recurrence block searched return-side language without recovery/remission-side language, leaving the process one-sided.",
          "recommendation": "Search recovery/remission wording and screen for return or prevention of return after recovery/remission, excluding episodes that never remitted.",
          "status": "resolved",
          "response": "The current recurrence block includes recover*[tiab] and remiss*[tiab]; the full evaluation retrieves all seven known relevant records. The eligibility criteria explicitly screen out episodes without remission or recovery."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The remaining 17,746-record workload exceeds the 10,000 budget. The only optional perspective block has been tested and retained because it preserves all seven known records and its refreshed 30-record loss sample found no eligible records; the workload concern remains for screening planning.",
          "evidence": "The tested block reduces results from 42,759 to 17,746 (58.5%), with no known records lost and 0/30 relevant records in the loss sample. Depression and relapse/recurrence are required searched concepts, while the psychological theory/model block is the optional concept tested as an AND block."
        },
        {
          "issue_id": "I-2682d8926fd0c83cc52e",
          "status": "accepted-risk",
          "response": "The stale-probe warning is factual: the depression block changed after the last category probe, and the two-probe budget is spent. The known lexical gap has been repaired and verified against the full known-record set, but the category-probe evidence cannot independently establish the coverage of the changed block.",
          "evidence": "Current depression terms include unipolar[tiab], dysthymi*[tiab], and melanchol*[tiab]; all seven known relevant PMIDs are retrieved. Probe 2 had previously found three relevant records outside the older block, and the packet records the category probe status as stale with 2/2 probes used."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "f52eb407d424271a2c59e4087cf2e47b3b04e1b18d213af1e5ab4efc679bfeb6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both round 1 translation findings were handled in version 5: the depression block includes unipolar[tiab], dysthymi*[tiab], and melanchol*[tiab], and the return/recovery block includes recover*[tiab] and remiss*[tiab]. The current query retrieves all seven known relevant records. Screening must still enforce the stated direction and eligibility criteria; the inability to repeat the exhausted category probe remains an accepted risk."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are combined with AND. The optional psychological theory/model block was tested, retains all seven known records, reduces results from 42,759 to 17,746, and the refreshed loss sample found 0/30 eligible records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected depressive-disorder, mood-disorder, recurrence, psychological-model, cognition, and cognitive-rumination headings. The probe findings support text-word repair and do not identify an error in heading selection."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The previously missing depression and recovery/remission wording is present as explicit tested text expressions, and the revised strategy retrieves all seven known relevant records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors, warnings, translation issues, or lint findings. The numbered Boolean lines and final three-block AND query are coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive population, study-design, or publication-date filters are applied. The documented Entrez cutoff is the stated as-of date, not an eligibility limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The prior depressive-disorders block omitted tested depression wording that identified three eligible records outside the block.",
          "recommendation": "Add the tested broader depression text words and rerun the complete evaluation, including known-record checks and category coverage review.",
          "status": "resolved",
          "response": "Version 5 adds unipolar[tiab], dysthymi*[tiab], and melanchol*[tiab], and retrieves all seven known relevant records, including the three previously missed PMIDs. The category probe remains stale because its two-probe budget is spent; that residual uncertainty is recorded as accepted-risk issue I-2682d8926fd0c83cc52e."
        },
        {
          "id": "R1-02",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The prior recurrence block searched return-side language without recovery/remission-side language, leaving the process one-sided.",
          "recommendation": "Search recovery/remission wording and screen for return or prevention of return after recovery/remission, excluding episodes that never remitted.",
          "status": "resolved",
          "response": "Version 5 includes recover*[tiab] and remiss*[tiab] in the recurrence block, retrieves all seven known relevant records, and retains eligibility criteria that exclude episodes without remission or recovery."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final workload of 17,746 exceeds the 10,000-record budget. The optional perspective block was tested and retained because it preserves all seven known records and its refreshed 30-record loss sample found no eligible records; the remaining volume is a screening-planning risk.",
          "evidence": "The tested block reduces results from 42,759 to 17,746 (58.5%); no known records were lost and 0/30 sampled removed records were eligible."
        },
        {
          "issue_id": "I-2682d8926fd0c83cc52e",
          "status": "accepted-risk",
          "response": "The category-probe warning remains valid because the depression block changed after the last probe and the two-probe budget is spent. The known lexical gap was repaired and all seven known relevant records are retrieved, but coverage of the changed block has not been independently re-established by a fresh category probe.",
          "evidence": "Version 5 includes unipolar[tiab], dysthymi*[tiab], and melanchol*[tiab]. The earlier probe 2 identified three relevant records outside the older block; the packet marks the probe stale with 2/2 probes used."
        }
      ]
    }
  ]
}
```


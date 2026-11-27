# PubMed search strategy: audit

Generated 2026-11-27T03:37:53+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: population/condition + prognosis (course)
- Scope confirmed by user: yes (User unavailable; proceeded with defaults (standard depth, no limits, no seeds). Scope kept without confirmation. Ambiguity: trajectory treated as course/longitudinal change broadly, not only latent-class trajectories; screened later. 16400531 (benchmark miss) never names PTSD in title/abstract: out of reach while PTSD block is required. Benchmarks come from reference lists of two reviews (23593134 adult/mixed, 23824234 child disasters), titles screened only. Result of 33,577 judged acceptable for a high-sensitivity review; count without a trajectory block is unmeasured loss risk if AND-ed.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Posttraumatic stress disorder / symptoms | search | core condition, reliably named and MeSH-indexed |
| Symptom trajectories / course over time | optional | fragile: course is described in many wordings (course, longitudinal, recovery, growth mixture); measure before AND-ing; tested: AND-ing gives 16,833 vs 33,577 (-49.9%), loses 0 of 22 independent benchmark records but 95% loss bound is 13.3%; left optional because the user asked for high sensitivity and the bound is too wide |
| Traumatic event exposure | optional | exposure is implicit in PTSD; measure as optional qualifier; tested: AND-ing loses 18725431 (1 of 21 retrieved), so not searched |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T03:37:33+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 33,577
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `"Stress Disorders, Traumatic, Acute"[Mesh]` | 387 | none |
| 3 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 4 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 5 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 6 | `PTSD[tiab]` | 15,732 | none |
| 7 | `PTSS[tiab]` | 510 | none |
| 8 | `"acute stress disorder"[tiab]` | 469 | none |
| 9 | `"acute stress reaction*"[tiab]` | 201 | none |
| 10 | `"traumatic stress"[tiab]` | 9,453 | none |
| 11 | `"stress disorder*"[tiab]` | 20,149 | none |
| 12 | `"posttraumatic symptom*"[tiab]` | 403 | none |
| 13 | `"post-traumatic symptom*"[tiab]` | 236 | none |
| 14 | `"posttraumatic stress"[tiab:~3]` | 14,699 | none |
| 15 | `"post-traumatic stress"[tiab:~3]` | 8,203 | none |
| 16 | `"posttraumatic neuros*"[tiab]` | 8 | none |
| 17 | `"combat disorder*"[tiab]` | 19 | none |
| 18 | `"combat neuros*"[tiab]` | 20 | none |
| 19 | `"war neuros*"[tiab]` | 129 | none |
| 20 | `"traumatic neuros*"[tiab]` | 198 | none |
| 21 | `"rape trauma syndrome"[tiab]` | 26 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 33,577 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR "Stress Disorders, Traumatic, Acute"[Mesh] OR "posttraumatic stress"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR PTSD[tiab] OR PTSS[tiab] OR "acute stress disorder"[tiab] OR "acute stress reaction*"[tiab] OR "traumatic stress"[tiab] OR "stress disorder*"[tiab] OR "posttraumatic symptom*"[tiab] OR "post-traumatic symptom*"[tiab] OR "posttraumatic stress"[tiab:~3] OR "post-traumatic stress"[tiab:~3] OR "posttraumatic neuros*"[tiab] OR "combat disorder*"[tiab] OR "combat neuros*"[tiab] OR "war neuros*"[tiab] OR "traumatic neuros*"[tiab] OR "rape trauma syndrome"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 22 | 21 | 95.5% | 21 / 22 |

21 of the 22 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 80.2% (95% bound; it is as wide as the number of such records makes it).

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C2 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 13 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 13 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 13 |
| C7 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 9 |

Missed records:

- PMID 16400531 (benchmark): not retrieved by ptsd

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Symptom trajectories / course over time (trajectory) | 33,577 | 16,833 | 0 / 21 | 0 / 21 | 13.3% |
| Traumatic event exposure (trauma) | 33,577 | 28,882 | 1 / 21 | 1 / 21 | 20.7% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 33,577 | initial | none | initial draft: PTSD block only; trajectory/trauma optional |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 4 findings; F1 should-fix accepted-risk, F2 document accepted-risk, F3 document rejected, F4 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 310 NCBI requests logged (115 from cache); strategy sha256 0eff679421a3._

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
            "pmid": "16400531",
            "failing_blocks": [
              "ptsd"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          }
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-21e94d12c8df29c4f367"
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
            "pmid": "16400531",
            "failing_blocks": [
              "ptsd"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          }
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-21e94d12c8df29c4f367"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:37:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013313",
          "name": "Stress Disorders, Post-Traumatic",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders with symptoms that last more than one month.",
          "tree_numbers": [
            "F03.950.750.500"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013313",
      "preferred_label": "Stress Disorders, Post-Traumatic",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Traumatic, Acute",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:37:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D040701",
          "name": "Stress Disorders, Traumatic, Acute",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders that is characterized by the significant dissociative states seen immediately after overwhelming trauma. By definition it cannot last longer than 1 month, if it persists, a diagnosis of post-traumatic stress disorder (STRESS DISORDERS, POST-TRAUMATIC) is more appropriate.",
          "tree_numbers": [
            "F03.950.750.550"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D040701",
      "preferred_label": "Stress Disorders, Traumatic, Acute",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Stress Disorders, Traumatic, Acute\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"stress disorders, traumatic, acute\"[MeSH Terms] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"acute stress disorder\"[Title/Abstract] OR \"acute stress reaction*\"[Title/Abstract] OR \"traumatic stress\"[Title/Abstract] OR \"stress disorder*\"[Title/Abstract] OR \"posttraumatic symptom*\"[Title/Abstract] OR \"post traumatic symptom*\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract:~3] OR \"post-traumatic stress\"[Title/Abstract:~3] OR \"posttraumatic neuros*\"[Title/Abstract] OR \"combat disorder*\"[Title/Abstract] OR \"combat neuros*\"[Title/Abstract] OR \"war neuros*\"[Title/Abstract] OR \"traumatic neuros*\"[Title/Abstract] OR \"rape trauma syndrome\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "e00837121471682115cca65598414397fb2e6a96f0d6edf2fd4f7c6dbe7622cf",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No warnings or errors on any line. Both MeSH descriptors verified. Trajectory and trauma are measured optional blocks, not searched."
        },
        "operators": {
          "verdict": "pass",
          "note": "One-block OR search. Trauma not AND-ed because it loses 18725431. Trajectory left optional: 13.3% loss bound too wide for high sensitivity."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "PTSD and acute stress disorder descriptors included, exploded."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Good coverage of acronyms, phrase variants, proximity and historical terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Parentheses, field tags and proximity phrases correct; no diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The only date bound is the harness's Entrez-date cutoff; see F1 response."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Every query carries an [edat] range ending 2016/01/24 that protocol.json does not record.",
          "recommendation": "Record and explain the date bound.",
          "status": "accepted-risk",
          "response": "The bound is the evaluation harness's pinned search date (PSB_AS_OF=2016-01-24, an Entrez-date bound, not a [dp] limit); it simulates running the search on that date and is not a strategy limit. Counts are as of 2016-01-24. Recorded in narrative.md."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "document",
          "kind": "structural",
          "finding": "Only the PTSD block is searched and the result is large (33,577); trajectory measured at 16,833 with 0 of 21 lost, 95% loss bound 13.3%.",
          "recommendation": "Keep optional; state the unmeasured loss risk.",
          "status": "accepted-risk",
          "response": "Accepted: the sensitivity requirement outweighs the roughly 50% screening saving, and the 13.3% loss bound is too wide to justify AND-ing."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "\"post-traumatic stress\" and \"post traumatic stress\" translate identically.",
          "recommendation": "Drop one or note as intentional.",
          "status": "rejected",
          "response": "Intentional spelling variants; PubMed treats them identically so there is no effect on recall or count. Left in place to avoid re-evaluation of an unchanged result."
        },
        {
          "id": "F4",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "Unclear whether term impact was measured on the current strategy.",
          "recommendation": "State it.",
          "status": "resolved",
          "response": "psb eval --term-impact was run on this identical strategy (same terms, v1). Largest unique contributors: Mesh PTSD 7,383, PTSD[tiab] 684, traumatic stress 474, stress disorder* 285; no term was dropped because several carry known records or are small."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-21e94d12c8df29c4f367",
          "status": "accepted-risk",
          "response": "The miss is retained. 16400531 never names PTSD in its title or abstract, so no PTSD term can retrieve it. Catching it would mean dropping the required PTSD block, which would greatly increase the result. One miss in 22 benchmark records is acceptable; the 80.2% lower-bound recall is reported.",
          "evidence": "Benchmark recall is 21/22 (95.5%); the only miss is 16400531, which fails the ptsd block and is not lost to limits. It is in the trauma and trajectory blocks, so the fault is the PTSD terminology."
        }
      ]
    }
  ]
}
```


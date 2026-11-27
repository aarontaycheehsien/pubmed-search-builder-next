# PubMed search strategy: audit

Generated 2026-11-27T15:18:52+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis (condition + course/trajectory)
- Scope confirmed by user: yes (User unavailable; defaults used: standard depth, no seeds, no limits. Ambiguity: 'trajectories' read as course of PTSD symptoms over time (any longitudinal course), not only latent-class trajectories; trajectory concept tested as optional. Continuing without waiting for scope confirmation. Scope message relayed; user not available to reply, so scope kept as drafted. Trajectory block not AND-ed (known records lost). No held-out validation; benchmark = reference lists of 23593134 (13) and 22033784 (2). Recall is only a lower bound of limited strength. 16400531 (benchmark) never names PTSD/trauma-stress in abstract: out of reach. OpenAlex unavailable (budget). Benchmark provenance: 13 records from the reference list of 23593134, 2 (11074232, 12271105) from 22033784.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder / posttraumatic stress symptoms (incl. acute stress, traumatic stress) | search | target condition, named in nearly every relevant record |
| Symptom trajectories / course over time (growth mixture, latent class, longitudinal course) | optional | Left optional: AND-ing it cuts 35,734 to 14,100 but loses 2 of 34 known records (2 of the 14 found without keyword search; 95% bound on loss 38.5%). Restructuring the top 3 terms with it cut only 6% so was reverted. Recall prioritised; trajectory handled at screening. |
| Traumatic event exposure (type of trauma) | screen | exposure defines PTSD itself; trauma type judged at screening |
| Longitudinal cohort design | screen | study design handled at screening |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T15:18:40+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 35,734
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `"Stress Disorders, Traumatic"[Mesh]` | 28,166 | none |
| 3 | `PTSD[tiab]` | 15,732 | none |
| 4 | `PTSS[tiab]` | 510 | none |
| 5 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 6 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 7 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 8 | `"traumatic stress"[tiab]` | 9,453 | none |
| 9 | `"posttraumatic symptom*"[tiab]` | 403 | none |
| 10 | `"post-traumatic symptom*"[tiab]` | 236 | none |
| 11 | `"posttraumatic reaction*"[tiab]` | 54 | none |
| 12 | `"posttraumatic response*"[tiab]` | 37 | none |
| 13 | `"acute stress disorder"[tiab]` | 469 | none |
| 14 | `"acute stress reaction*"[tiab]` | 201 | none |
| 15 | `"combat disorder*"[tiab]` | 19 | none |
| 16 | `"combat stress"[tiab]` | 293 | none |
| 17 | `"trauma symptom*"[tiab]` | 595 | none |
| 18 | `"traumatic symptom*"[tiab]` | 318 | none |
| 19 | `"acute stress symptom*"[tiab]` | 66 | none |
| 20 | `"acute stress response*"[tiab]` | 360 | none |
| 21 | `"shell shock"[tiab]` | 110 | none |
| 22 | `"war neurosis"[tiab]` | 48 | none |
| 23 | `"traumatic neurosis"[tiab]` | 138 | none |
| 24 | `"combat fatigue"[tiab]` | 56 | none |
| 25 | `"battle fatigue"[tiab]` | 24 | none |
| 26 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 35,734 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR "Stress Disorders, Traumatic"[Mesh] OR PTSD[tiab] OR PTSS[tiab] OR "post-traumatic stress"[tiab] OR "posttraumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "traumatic stress"[tiab] OR "posttraumatic symptom*"[tiab] OR "post-traumatic symptom*"[tiab] OR "posttraumatic reaction*"[tiab] OR "posttraumatic response*"[tiab] OR "acute stress disorder"[tiab] OR "acute stress reaction*"[tiab] OR "combat disorder*"[tiab] OR "combat stress"[tiab] OR "trauma symptom*"[tiab] OR "traumatic symptom*"[tiab] OR "acute stress symptom*"[tiab] OR "acute stress response*"[tiab] OR "shell shock"[tiab] OR "war neurosis"[tiab] OR "traumatic neurosis"[tiab] OR "combat fatigue"[tiab] OR "battle fatigue"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 15 | 14 | 93.3% | 14 / 15 |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 20 | 20 | 100.0% | 0 / 0 |

14 of the 15 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 72.1% (95% bound; it is as wide as the number of such records makes it). 13 of the 15 known records found through reference lists come from one review (23593134, 86.7%). A benchmark built on one review takes that review's scope: add the reference list of a second review that covers a different searched concept.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C2 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 13 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 37 | 37 | 2 |

Missed records:

- PMID 16400531 (benchmark): not retrieved by ptsd

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Trajectories / course over time (trajectory) | 35,734 | 14,100 | 2 / 34 | 2 / 14 | 38.5% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | initial draft: PTSD block only, trajectory optional |
| 2 | 65,546 | ptsd: +2 / -1 | none | fix proximity wildcard |
| 3 | 35,266 | ptsd: +5 / -6 | none | reverted restructure; removed generic 'stress disorder' proximity and bare post-traumatic/posttraumatic terms (noise) |
| 4 | 33,220 | ptsd: +3 / -3 | none | restructure top3 terms with trajectory qualifier (known-record-checked) |
| 5 | 35,266 | ptsd: +3 / -3 | none | reverted restructure (6% gain not worth risk); trajectory left optional (loses 2 known) |
| 6 | 35,734 | ptsd: +9 / -2 | none | critic R1: replaced wildcard-in-phrase terms; added acute stress symptom/response, historical labels |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 8 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk, F5 document resolved, F6 should-fix accepted-risk, F7 should-fix accepted-risk, F8 document accepted-risk
- Round 2 on version 6 (Round 2 review by a fresh-context subagent (findings F1-F8 confirmed closed; F9 raised and addressed).): 9 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk, F5 document resolved, F6 should-fix accepted-risk, F7 should-fix accepted-risk, F8 document accepted-risk, F9 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 487 NCBI requests logged (172 from cache); strategy sha256 13ae2657541f._

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
      "checked_at": "2026-11-27T15:18:40+00:00",
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
      "requested": "Stress Disorders, Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T15:18:40+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D040921",
          "name": "Stress Disorders, Traumatic",
          "type": "descriptor",
          "scope_note": "Anxiety disorders manifested by the development of characteristic symptoms following a psychologically traumatic event that is outside the normal range of usual human experience. Symptoms include re-experiencing the traumatic event, increased arousal, and numbing of responsiveness to or reduced involvement with the external world. Traumatic stress disorders can be further classified by the time...",
          "tree_numbers": [
            "F03.950.750"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D040921",
      "preferred_label": "Stress Disorders, Traumatic",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Stress Disorders, Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"stress disorders, traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"traumatic stress\"[Title/Abstract] OR \"posttraumatic symptom*\"[Title/Abstract] OR \"post traumatic symptom*\"[Title/Abstract] OR \"posttraumatic reaction*\"[Title/Abstract] OR \"posttraumatic response*\"[Title/Abstract] OR \"acute stress disorder\"[Title/Abstract] OR \"acute stress reaction*\"[Title/Abstract] OR \"combat disorder*\"[Title/Abstract] OR \"combat stress\"[Title/Abstract] OR \"trauma symptom*\"[Title/Abstract] OR \"traumatic symptom*\"[Title/Abstract] OR \"acute stress symptom*\"[Title/Abstract] OR \"acute stress response*\"[Title/Abstract] OR \"shell shock\"[Title/Abstract] OR \"war neurosis\"[Title/Abstract] OR \"traumatic neurosis\"[Title/Abstract] OR \"combat fatigue\"[Title/Abstract] OR \"battle fatigue\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "be73cf97dbfc8088e13cc32d158b409f24e071f9a1712e113437e061b4de6ad3",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "'acute stress' only in narrower phrases; see F2"
        },
        "operators": {
          "verdict": "revise",
          "note": "large result; see F1"
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "descriptors verified, exploded"
        },
        "text_words": {
          "verdict": "revise",
          "note": "historical labels, acute stress; see F2, F5"
        },
        "syntax": {
          "verdict": "revise",
          "note": "wildcard inside phrase; see F3"
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "as_of/reporting; see F6, F7"
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Single block with large result; trajectory subset untested.",
          "recommendation": "Run term-impact, test narrow trajectory block.",
          "status": "resolved",
          "response": "term-impact run in v6 (top terms carry 1-5% each, none carries a known record alone). Trajectory block AND-ed loses 2 of 34 known records, so it stays optional; no narrower subset kept because the lost records (11074232, 12271105) use generic wording. Large PTSD literature is plausible; handled by screening."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "'acute stress' only in narrower phrases.",
          "recommendation": "Add acute stress symptom/response phrases.",
          "status": "resolved",
          "response": "Added \"acute stress symptom*\" and \"acute stress response*\"; bare 'acute stress' not added (laboratory stress noise)."
        },
        {
          "id": "F3",
          "domain": "syntax",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "Wildcard inside phrase.",
          "recommendation": "Replace with explicit phrases.",
          "status": "resolved",
          "response": "Removed \"trauma* symptom*\" and \"posttrauma* stress\"; added \"trauma symptom*\", \"traumatic symptom*\" (wildcard on final word only). Re-evaluated in v6, no known record lost."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "Duplicate lines 5 and 7.",
          "recommendation": "Keep and note.",
          "status": "accepted-risk",
          "response": "Harmless duplication; kept."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "No historical labels.",
          "recommendation": "Test or document.",
          "status": "resolved",
          "response": "Added shell shock, war neurosis, traumatic neurosis, combat fatigue, battle fatigue (each adds 30-41 unique records in term-impact); [ot] not added."
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Entry-date bound undeclared.",
          "recommendation": "Declare.",
          "status": "accepted-risk",
          "response": "The bound is the harness's as-of cutoff (2016-01-24), applied to Entrez date, not a publication-date limit; the search is deliberately historical and not current."
        },
        {
          "id": "F7",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Recall evidence thin.",
          "recommendation": "Report 93.3% with 72.1% bound; not cite 100% relevant.",
          "status": "accepted-risk",
          "response": "Will report benchmark 14/15 and the 72.1% lower bound; relevant-set recall labelled development only. Benchmark draws on two reviews' reference lists (23593134, 22033784)."
        },
        {
          "id": "F8",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "scope",
          "finding": "PubMed only.",
          "recommendation": "Document.",
          "status": "accepted-risk",
          "response": "PubMed-only search is the task scope; PsycINFO/Embase recommended in limitations."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-21e94d12c8df29c4f367",
          "status": "accepted-risk",
          "response": "16400531 (benchmark) abstract reports anxiety/depression and mental health service use after a disaster and never names PTSD or traumatic stress; no PTSD term can retrieve it. Out of reach, one of 15 benchmark records.",
          "evidence": "misses[0]: pmid 16400531, failing_blocks [ptsd], benchmark only; terms miss diagnosis no_block_wording; abstract read in this run."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "c9aaac0a790535cc841700ee8b5794aa47d862007be914c1a3a5106e881d5618",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Reviewed in round 2: no problems."
        },
        "operators": {
          "verdict": "pass",
          "note": "Reviewed in round 2: no problems."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Reviewed in round 2: no problems."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Reviewed in round 2: no problems."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Reviewed in round 2: no problems."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Stale figures and benchmark provenance corrected; date bound, recall reporting and PubMed-only scope carried as accepted risks."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Single block with large result; trajectory subset untested.",
          "recommendation": "Run term-impact, test narrow trajectory block.",
          "status": "resolved",
          "response": "term-impact run in v6 (top terms carry 1-5% each, none carries a known record alone). Trajectory block AND-ed loses 2 of 34 known records, so it stays optional; no narrower subset kept because the lost records (11074232, 12271105) use generic wording. Large PTSD literature is plausible; handled by screening."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "'acute stress' only in narrower phrases.",
          "recommendation": "Add acute stress symptom/response phrases.",
          "status": "resolved",
          "response": "Added \"acute stress symptom*\" and \"acute stress response*\"; bare 'acute stress' not added (laboratory stress noise)."
        },
        {
          "id": "F3",
          "domain": "syntax",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "Wildcard inside phrase.",
          "recommendation": "Replace with explicit phrases.",
          "status": "resolved",
          "response": "Removed \"trauma* symptom*\" and \"posttrauma* stress\"; added \"trauma symptom*\", \"traumatic symptom*\" (wildcard on final word only). Re-evaluated in v6, no known record lost."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "Duplicate lines 5 and 7.",
          "recommendation": "Keep and note.",
          "status": "accepted-risk",
          "response": "Harmless duplication; kept."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "No historical labels.",
          "recommendation": "Test or document.",
          "status": "resolved",
          "response": "Added shell shock, war neurosis, traumatic neurosis, combat fatigue, battle fatigue (each adds 30-41 unique records in term-impact); [ot] not added."
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Entry-date bound undeclared.",
          "recommendation": "Declare.",
          "status": "accepted-risk",
          "response": "The bound is the harness's as-of cutoff (2016-01-24), applied to Entrez date, not a publication-date limit; the search is deliberately historical and not current."
        },
        {
          "id": "F7",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Recall evidence thin.",
          "recommendation": "Report 93.3% with 72.1% bound; not cite 100% relevant.",
          "status": "accepted-risk",
          "response": "Will report benchmark 14/15 and the 72.1% lower bound; relevant-set recall labelled development only. Benchmark draws on two reviews' reference lists (23593134, 22033784)."
        },
        {
          "id": "F8",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "scope",
          "finding": "PubMed only.",
          "recommendation": "Document.",
          "status": "accepted-risk",
          "response": "PubMed-only search is the task scope; PsycINFO/Embase recommended in limitations."
        },
        {
          "id": "F9",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Trajectory rationale quoted stale counts (35,266 to 13,909) and benchmark provenance was inconsistent.",
          "recommendation": "Update to 35,734 to 14,100 and name both reviews.",
          "status": "resolved",
          "response": "protocol.json rationale now says 35,734 to 14,100, 2 of 34 known lost; notes name 23593134 (13) and 22033784 (2). Strategy unchanged; re-evaluated."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-21e94d12c8df29c4f367",
          "status": "accepted-risk",
          "response": "16400531 (benchmark) abstract reports anxiety/depression and mental health service use after a disaster and never names PTSD or traumatic stress; no PTSD term can retrieve it. Out of reach, one of 15 benchmark records.",
          "evidence": "misses[0]: pmid 16400531, failing_blocks [ptsd], benchmark only; terms miss diagnosis no_block_wording; abstract read in this run."
        }
      ],
      "note": "Round 2 review by a fresh-context subagent (findings F1-F8 confirmed closed; F9 raised and addressed)."
    }
  ]
}
```


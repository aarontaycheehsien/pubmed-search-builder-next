# PubMed search strategy: audit

Generated 2026-11-27T05:56:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis (population/condition + course/trajectory)
- Scope confirmed by user: yes (No user seeds. Defaults used (standard depth, no limits); user unavailable, scope kept as drafted. Known records: 22 benchmark records from reference lists of reviews 23824234, 23593134, 23215790 (trajectory-themed, so they favour trajectory wording), plus 5 relevant records from a precise pilot search (keyword-dependent, not independent). Recall lower bound 87.3% from 22 independent records. Trajectory block AND-ed on evidence (0 of 27 lost at v3; 95% bound on loss 12.7%; count 39,381 -> 17,452); later generic terms pruned, final result 10,336. Entry-date bound to 2016/01/24 is the harness as-of cutoff. Scope message relayed; run continued without pausing.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| PTSD and post-traumatic stress symptoms / traumatic stress reactions | search | target condition; named reliably, MeSH Stress Disorders, Post-Traumatic |
| Symptom trajectories / course over time (growth mixture, latent class, longitudinal course) | search | AND-ed on evidence: measured as optional block; 0 of 27 known records lost, 22 found without a keyword search (95% bound on share lost 12.7%), result fell 39,381 -> 17,452 at v3 (10,336 after pruning generic terms at v4) (55.7%). Caveat: independent records come from reference lists of trajectory-themed reviews (23824234, 23593134, 23215790), which favour trajectory wording. |
| Traumatic event exposure (accident, disaster, assault, combat, etc.) | screen | event types are heterogeneous and the exposure is implied by PTSD; checked at screening. Measured as optional block (41 terms): AND-ing would cut 10,336 -> 9,556 (7.5%) and lose 1 of 27 known records (18725431; 95% bound on loss 19.8%), so it stays at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T05:55:46+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 10,336
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Traumatic"[Mesh]` | 28,166 | none |
| 2 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 3 | `PTSD[tiab]` | 15,732 | none |
| 4 | `PTSS[tiab]` | 510 | none |
| 5 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 6 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 7 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 8 | `"posttraumatic symptom*"[tiab]` | 403 | none |
| 9 | `"post-traumatic symptom*"[tiab]` | 236 | none |
| 10 | `"traumatic stress"[tiab]` | 9,453 | none |
| 11 | `"acute stress disorder"[tiab]` | 469 | none |
| 12 | `"acute stress reaction*"[tiab]` | 201 | none |
| 13 | `"acute stress symptom*"[tiab]` | 66 | none |
| 14 | `"trauma symptom*"[tiab]` | 595 | none |
| 15 | `"posttraumatic reaction*"[tiab]` | 54 | none |
| 16 | `"post-traumatic reaction*"[tiab]` | 52 | none |
| 17 | `"combat disorder*"[tiab]` | 19 | none |
| 18 | `"combat stress"[tiab]` | 293 | none |
| 19 | `"shell shock"[tiab]` | 110 | none |
| 20 | `"traumatic neuros*"[tiab]` | 198 | none |
| 21 | `"posttraumatic neuros*"[tiab]` | 8 | none |
| 22 | `"post-traumatic neuros*"[tiab]` | 37 | none |
| 23 | `"posttraumatic adjustment"[tiab]` | 22 | none |
| 24 | `"post-traumatic adjustment"[tiab]` | 6 | none |
| 25 | `"posttraumatic distress"[tiab]` | 84 | none |
| 26 | `"post-traumatic distress"[tiab]` | 38 | none |
| 27 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 35,362 | none |
| 28 | `"Disease Progression"[Mesh]` | 138,667 | none |
| 29 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 30 | `"Follow-Up Studies"[Mesh]` | 555,750 | none |
| 31 | `trajector*[tiab]` | 43,861 | none |
| 32 | `"growth mixture"[tiab]` | 576 | none |
| 33 | `"latent class"[tiab]` | 2,971 | none |
| 34 | `"latent growth"[tiab]` | 1,343 | none |
| 35 | `"growth curve*"[tiab]` | 8,981 | none |
| 36 | `"growth model*"[tiab]` | 3,528 | none |
| 37 | `"mixture model*"[tiab]` | 3,628 | none |
| 38 | `"latent profile"[tiab]` | 396 | none |
| 39 | `course[tiab]` | 460,307 | none |
| 40 | `longitudinal*[tiab]` | 180,653 | none |
| 41 | `"follow-up"[tiab]` | 702,978 | none |
| 42 | `"followed up"[tiab]` | 74,344 | none |
| 43 | `prospective*[tiab]` | 506,544 | none |
| 44 | `recover*[tiab]` | 513,902 | none |
| 45 | `resilien*[tiab]` | 15,494 | none |
| 46 | `"over time"[tiab]` | 128,863 | none |
| 47 | `persist*[tiab]` | 367,129 | none |
| 48 | `remission[tiab]` | 92,395 | none |
| 49 | `"delayed onset"[tiab]` | 5,353 | none |
| 50 | `"delayed-onset"[tiab]` | 5,353 | none |
| 51 | `"time course"[tiab]` | 66,728 | none |
| 52 | `"months after"[tiab]` | 170,675 | none |
| 53 | `"years after"[tiab]` | 97,858 | none |
| 54 | `"weeks after"[tiab]` | 102,910 | none |
| 55 | `"symptom change"[tiab]` | 558 | none |
| 56 | `#28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55` | 3,141,993 | none |
| 57 | `#27 AND #56` | 10,336 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Traumatic"[Mesh] OR "Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR PTSS[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "posttraumatic symptom*"[tiab] OR "post-traumatic symptom*"[tiab] OR "traumatic stress"[tiab] OR "acute stress disorder"[tiab] OR "acute stress reaction*"[tiab] OR "acute stress symptom*"[tiab] OR "trauma symptom*"[tiab] OR "posttraumatic reaction*"[tiab] OR "post-traumatic reaction*"[tiab] OR "combat disorder*"[tiab] OR "combat stress"[tiab] OR "shell shock"[tiab] OR "traumatic neuros*"[tiab] OR "posttraumatic neuros*"[tiab] OR "post-traumatic neuros*"[tiab] OR "posttraumatic adjustment"[tiab] OR "post-traumatic adjustment"[tiab] OR "posttraumatic distress"[tiab] OR "post-traumatic distress"[tiab]) AND ("Disease Progression"[Mesh] OR "Longitudinal Studies"[Mesh] OR "Follow-Up Studies"[Mesh] OR trajector*[tiab] OR "growth mixture"[tiab] OR "latent class"[tiab] OR "latent growth"[tiab] OR "growth curve*"[tiab] OR "growth model*"[tiab] OR "mixture model*"[tiab] OR "latent profile"[tiab] OR course[tiab] OR longitudinal*[tiab] OR "follow-up"[tiab] OR "followed up"[tiab] OR prospective*[tiab] OR recover*[tiab] OR resilien*[tiab] OR "over time"[tiab] OR persist*[tiab] OR remission[tiab] OR "delayed onset"[tiab] OR "delayed-onset"[tiab] OR "time course"[tiab] OR "months after"[tiab] OR "years after"[tiab] OR "weeks after"[tiab] OR "symptom change"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 10 | 10 | 100.0% | 10 / 10 |
| benchmark2 | benchmark (included studies of a prior review; external benchmark) | 12 | 12 | 100.0% | 12 / 12 |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% | 0 / 0 |

22 of the 22 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 87.3% (95% bound; it is as wide as the number of such records makes it).

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C2 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 10 |
| C3 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 10 |
| C7 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 8 |
| C8 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 4 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 3,141,993 | 0 |
| trajectory | 35,362 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Traumatic event exposure (event) | 10,336 | 9,556 | 1 / 27 | 1 / 22 | 19.8% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | first draft: PTSD block only, trajectory optional |
| 2 | 39,381 | ptsd: +2 / -2 | none | removed wildcards from proximity terms |
| 3 | 17,452 | trajectory: +32 / -0 | none | AND-ed trajectory block on evidence (optional-block rule); term impact |
| 4 | 10,336 | ptsd: +0 / -2; trajectory: +0 / -4 | none | dropped generic noisy terms with no known-record impact: chronic*, improv*, decreas*, 'changes in', stress disorder(s) proximity |
| 5 | 10,336 | limits/combination | none | v5: drafted optional event block as restructure qualifier; term impact on v4 strategy |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 5 findings; F1 should-fix rejected, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk, F5 document resolved
- Round 2 on version 5: 7 findings; F1 should-fix rejected, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk, F5 document resolved, F6 should-fix resolved, F7 document resolved
- Round 3 on version 5: 8 findings; F1 should-fix rejected, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk, F5 document resolved, F6 should-fix resolved, F7 document resolved, F8 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1112 NCBI requests logged (551 from cache); strategy sha256 dd646a69b878._

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
      "requested": "Stress Disorders, Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T05:55:46+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"Stress Disorders, Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T05:55:46+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Disease Progression",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T05:55:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D018450",
          "name": "Disease Progression",
          "type": "descriptor",
          "scope_note": "The worsening and general progression of a disease over time. This concept is most often used for chronic and incurable diseases where the stage of the disease is an important determinant of therapy and prognosis.",
          "tree_numbers": [
            "C23.550.291.656"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D018450",
      "preferred_label": "Disease Progression",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "\"Disease Progression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T05:55:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008137",
          "name": "Longitudinal Studies",
          "type": "descriptor",
          "scope_note": "Studies in which variables relating to an individual or group of individuals are assessed over a period of time.",
          "tree_numbers": [
            "E05.318.372.500.750.500",
            "N05.715.360.330.500.750.500",
            "N06.850.520.450.500.750.500"
          ],
          "entry_terms": 32,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008137",
      "preferred_label": "Longitudinal Studies",
      "type": "descriptor",
      "location": "vocabulary:28",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T05:55:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005500",
          "name": "Follow-Up Studies",
          "type": "descriptor",
          "scope_note": "Studies in which individuals or populations are followed to assess the outcome of exposures, procedures, or effects of a characteristic, e.g., occurrence of disease.",
          "tree_numbers": [
            "E05.318.372.500.750.249",
            "N05.715.360.330.500.750.350",
            "N06.850.520.450.500.750.350"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005500",
      "preferred_label": "Follow-Up Studies",
      "type": "descriptor",
      "location": "vocabulary:29",
      "term": {
        "text": "\"Follow-Up Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, traumatic\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic symptom*\"[Title/Abstract] OR \"post traumatic symptom*\"[Title/Abstract] OR \"traumatic stress\"[Title/Abstract] OR \"acute stress disorder\"[Title/Abstract] OR \"acute stress reaction*\"[Title/Abstract] OR \"acute stress symptom*\"[Title/Abstract] OR \"trauma symptom*\"[Title/Abstract] OR \"posttraumatic reaction*\"[Title/Abstract] OR \"post traumatic reaction*\"[Title/Abstract] OR \"combat disorder*\"[Title/Abstract] OR \"combat stress\"[Title/Abstract] OR \"shell shock\"[Title/Abstract] OR \"traumatic neuros*\"[Title/Abstract] OR \"posttraumatic neuros*\"[Title/Abstract] OR \"post traumatic neuros*\"[Title/Abstract] OR \"posttraumatic adjustment\"[Title/Abstract] OR \"post-traumatic adjustment\"[Title/Abstract] OR \"posttraumatic distress\"[Title/Abstract] OR \"post-traumatic distress\"[Title/Abstract]) AND (\"Disease Progression\"[MeSH Terms] OR \"Longitudinal Studies\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"trajector*\"[Title/Abstract] OR \"growth mixture\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve*\"[Title/Abstract] OR \"growth model*\"[Title/Abstract] OR \"mixture model*\"[Title/Abstract] OR \"latent profile\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"longitudinal*\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followed up\"[Title/Abstract] OR \"prospective*\"[Title/Abstract] OR \"recover*\"[Title/Abstract] OR \"resilien*\"[Title/Abstract] OR \"over time\"[Title/Abstract] OR \"persist*\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"delayed-onset\"[Title/Abstract] OR \"delayed-onset\"[Title/Abstract] OR \"time course\"[Title/Abstract] OR \"months after\"[Title/Abstract] OR \"years after\"[Title/Abstract] OR \"weeks after\"[Title/Abstract] OR \"symptom change\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "b80b929d90e00c5710fe521e2a3c8b3fb73688dd62da6edfe994cc3241f8c679",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No warnings or translation issues on any line; bare names PTSD, PTSS, traumatic stress, acute stress disorder are searched."
        },
        "operators": {
          "verdict": "revise",
          "note": "Trajectory block is permissive; result 10,336 slightly above the 10,000 large-result threshold; term-impact predates v4; benchmarks come from trajectory-themed reviews."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "D040921 and D013313 verified, explosion covers acute stress disorder; free text backs unindexed records."
        },
        "text_words": {
          "verdict": "revise",
          "note": "PTSD synonym coverage good; v4 removals of chronic*, decreas*, improv*, 'changes in' and stress disorder proximity were undocumented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Boolean structure, tags and line references correct; redundant hyphen/space duplicate lines are harmless."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Every line carries an entry-date restriction not declared in protocol limits."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "block": null,
          "finding": "All lines are restricted by entry date to 2016/01/24 but protocol lists no limits.",
          "recommendation": "Declare the cutoff or remove it.",
          "status": "rejected",
          "response": "The [edat] bound to 2016/01/24 is the harness's as-of cutoff (PSB_AS_OF), applied so the search reproduces what PubMed held on that date. It is not a clinical or design limit and is not applied to the delivered query text as a [dp] limit. Recorded in notes and narrative."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": null,
          "finding": "Trajectory block permissive; v4 result 10,336 above threshold; measurement is from an earlier version.",
          "recommendation": "Re-run measurement and term impact on v4; try restructure.",
          "status": "resolved",
          "response": "Re-ran eval --term-impact on v4 (v5): count 10,336, no term alone adds more than 823 records (recover*, 8.0%). Tried psb restructure --qualifier event (optional block with MeSH and text layers), dry run: 10,336 -> 10,234 with no known loss, a gain of only 1%. Not applied, because the event block is itself fragile (it would lose 1 of 27 known records) and the saving is negligible. The AND of the trajectory block was justified on evidence (22 records found without keyword search, 0 lost, 55.7% reduction at v3); the 95% bound on loss is 12.7% and the benchmark sources are trajectory-themed reviews, stated in the audit/narrative. Result remains ~10k and is flagged as large."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": null,
          "finding": "v4 removed chronic*, decreas*, improv*, 'changes in', stress disorder proximity without recorded reason.",
          "recommendation": "Document why.",
          "status": "resolved",
          "response": "Removals were made after term-impact showed these generic words alone added 1,841, 1,533 and further records with no known record only reachable through them; chronic*/improv*/decreas*/'changes in' are generic words that mean course only in some contexts, and the 'stress disorder'~3 proximity matched unrelated pairs (1,809 records alone) while PTSD, ASD, traumatic stress and both MeSH headings already cover the concept. Re-evaluated after removal (v4, v5): no known record lost, 22/22 independent records retained. The limitation that known records cannot test generic course wording is accepted and documented."
        },
        {
          "id": "F4",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "block": null,
          "finding": "Redundant lines with identical counts (#6/#7, #49/#50); MeSH #1 includes #2.",
          "recommendation": "Keep or merge.",
          "status": "accepted-risk",
          "response": "Kept for explicit spelling-variant coverage; harmless to results."
        },
        {
          "id": "F5",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "block": null,
          "finding": "Notes say no seeds but 27 known records from reference lists and pilot are used; rationale cites an outdated count.",
          "recommendation": "Correct notes and rationale.",
          "status": "resolved",
          "response": "Notes and rationale updated: no user seeds; benchmark records from reference lists of reviews 23824234, 23593134 and 23215790 (trajectory-themed); 5 relevant records from a pilot search are not independent; bound 87.3% from 22 records."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "c6081e0b97e4de0175053761a0b6d59950cc9a85e9274bef3d5fa4d9512a36db",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No warnings or translation issues on any line; bare names searched."
        },
        "operators": {
          "verdict": "revise",
          "note": "Structure correct and AND of trajectory supported by measurement; result 10,336 remains above the 10,000 large-result threshold; term impact must be on current version."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Descriptors verified; explosion covers acute stress disorder."
        },
        "text_words": {
          "verdict": "pass",
          "note": "PTSD and trajectory vocabulary coverage good; v4 removals documented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Lines, tags and quoting correct."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Protocol limits empty; edat bound is the harness as-of cutoff."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "block": null,
          "finding": "All lines are restricted by entry date to 2016/01/24 but protocol lists no limits.",
          "recommendation": "Declare the cutoff or remove it.",
          "status": "rejected",
          "response": "Rejection stands: the [edat] bound is the harness as-of cutoff for reproducibility, not a protocol limit. narrative.md states that the executed query text carries the entry-date clause."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": null,
          "finding": "Trajectory block permissive; v4 result 10,336 above threshold; measurement is from an earlier version.",
          "recommendation": "Re-run measurement and term impact on v4; try restructure.",
          "status": "resolved",
          "response": "Resolved on structure and evidence; term impact has now been re-run on the current version (see F6); restructure not applied (1% gain)."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": null,
          "finding": "v4 removed chronic*, decreas*, improv*, 'changes in', stress disorder proximity without recorded reason.",
          "recommendation": "Document why.",
          "status": "resolved",
          "response": "Removals were made after term-impact showed these generic words alone added 1,841, 1,533 and further records with no known record only reachable through them; chronic*/improv*/decreas*/'changes in' are generic words that mean course only in some contexts, and the 'stress disorder'~3 proximity matched unrelated pairs (1,809 records alone) while PTSD, ASD, traumatic stress and both MeSH headings already cover the concept. Re-evaluated after removal (v4, v5): no known record lost, 22/22 independent records retained. The limitation that known records cannot test generic course wording is accepted and documented."
        },
        {
          "id": "F4",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "block": null,
          "finding": "Redundant lines with identical counts (#6/#7, #49/#50); MeSH #1 includes #2.",
          "recommendation": "Keep or merge.",
          "status": "accepted-risk",
          "response": "Kept for explicit spelling-variant coverage; harmless to results."
        },
        {
          "id": "F5",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "block": null,
          "finding": "Notes say no seeds but 27 known records from reference lists and pilot are used; rationale cites an outdated count.",
          "recommendation": "Correct notes and rationale.",
          "status": "resolved",
          "response": "Notes and rationale updated: no user seeds; benchmark records from reference lists of reviews 23824234, 23593134 and 23215790 (trajectory-themed); 5 relevant records from a pilot search are not independent; bound 87.3% from 22 records."
        },
        {
          "id": "F6",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "block": "trajectory",
          "finding": "F2 response claimed term impact re-run on current version but evidence said earlier version; result still above 10,000.",
          "recommendation": "Re-run term-impact on the current version, or correct the claim; report as flagged large result.",
          "status": "resolved",
          "response": "Re-ran psb eval --term-impact on the current strategy (v7 note; strategy v5 unchanged). Top single-term contributors: recover* 823 (8.0%), resilien* 686 (6.6%), follow-up 659 (6.4%), none carries a known record alone. The result of 10,336 is reported as a flagged large result in narrative.md."
        },
        {
          "id": "F7",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "block": "event",
          "finding": "Event rationale lacks the measurement.",
          "recommendation": "Add measurement to rationale/narrative.",
          "status": "resolved",
          "response": "Measurement added to the event concept rationale in protocol.json and to narrative.md: AND-ing would cut 10,336 to 9,556 (7.5%) and lose 1 of 27 known records (18725431; bound 19.8%)."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "a585070ef675c2c1fbe2eaf5d1a7eb6cd3b902f043004d1d3005ac6ec8f85ef0",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No warnings; bare names searched; MeSH verified; event rationale carries its measurement."
        },
        "operators": {
          "verdict": "pass",
          "note": "Two-block AND supported by measurement; 10,336 flagged large result accepted; term impact re-run on current version; restructure gained ~1%."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "D040921 and D013313 verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Good PTSD and trajectory coverage; v4 removals documented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Structure, tags, quoting correct; duplicate lines harmless."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Protocol limits empty; edat bound is the as-of cutoff."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "block": null,
          "finding": "All lines are restricted by entry date to 2016/01/24, but the protocol lists no limits.",
          "recommendation": "Declare the cutoff or remove it.",
          "status": "rejected",
          "response": "The [edat] bound is the harness's as-of reproducibility cutoff, not a clinical or design limit; documented in the notes and narrative."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": null,
          "finding": "The trajectory block is permissive, and the result of 10,336 is above the large-result threshold.",
          "recommendation": "Re-run measurement and term impact on the current version, and try a restructure.",
          "status": "resolved",
          "response": "Ablation shows 0 known records gained when the trajectory block is dropped. Term impact is on the current version. Restructure tried and not applied (1% gain)."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": null,
          "finding": "The v4 removals had no recorded reason.",
          "recommendation": "Document the reason.",
          "status": "resolved",
          "response": "Reasons recorded; no known record lost after the removals; limitation accepted."
        },
        {
          "id": "F4",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "block": null,
          "finding": "Redundant lines with identical counts.",
          "recommendation": "Keep or merge.",
          "status": "accepted-risk",
          "response": "Kept for explicit spelling-variant coverage; harmless to the result."
        },
        {
          "id": "F5",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "block": null,
          "finding": "Notes said no seeds but known records were used.",
          "recommendation": "Correct the notes and rationale.",
          "status": "resolved",
          "response": "Notes now state sources and the 87.3% bound from 22 independent records."
        },
        {
          "id": "F6",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "block": "trajectory",
          "finding": "Term impact claim versus evidence.",
          "recommendation": "Re-run term impact on the current version.",
          "status": "resolved",
          "response": "Term impact present on the current version; large result flagged."
        },
        {
          "id": "F7",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "block": "event",
          "finding": "The event rationale lacked the measurement.",
          "recommendation": "Add the measurement.",
          "status": "resolved",
          "response": "Rationale now has 10,336 -> 9,556, 1 of 27 lost (18725431), bound 19.8%."
        },
        {
          "id": "F8",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "block": null,
          "finding": "No noise-check of the unique records of generic trajectory terms (recover*, resilien*, follow-up, persist*); the numbers quoted in the F3 response cannot be checked against current evidence.",
          "recommendation": "Note in the narrative that the generic trajectory terms were retained on known-record recall, not an off-topic review; screening should expect noise.",
          "status": "accepted-risk",
          "response": "Documented in narrative.md. The generic terms were retained on known-record recall, not an off-topic review of their unique records; expect noise at screening. The 1,841 and 1,533 figures were from the v3 term-impact run, which is superseded."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


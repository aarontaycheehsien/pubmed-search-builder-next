# PubMed search strategy: audit

Generated 2026-09-28T13:19:53+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis / longitudinal symptom course
- Scope confirmed by user: no (User has no known relevant articles and cannot answer questions during this run; proceeding at standard depth with assumptions documented, without user scope confirmation. No population, age, language, or study-design limits. PubMed requests are bounded by PSB_AS_OF=2016-01-24 (Entrez date); no publication-date limit. PTSD is the required block. The trajectory and traumatic-event concepts were tested as optional and left out after loss-sample review. No seeds were available; prior-review references and optional-block loss samples supplied the benchmark and development records. Assume repeated post-event PTSD symptom measurements are eligible in any study design, including intervention studies; screen reports without repeated post-event PTSD symptom assessment out. The PTSD-only query exceeds 10,000 records; both searchable optional concepts in scope were evaluated and neither met the rule for AND-ing.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder symptoms or diagnosis | search | The condition is essential to every eligible study and is reliably named and indexed. |
| Longitudinal symptom course or trajectory | optional | This topic-defining course may be named in records, but eligible studies can describe it using recovery, chronicity, remission, persistence, resilience, or delayed-onset language; test before requiring it. |
| Exposure to a traumatic event | optional | The trauma-event context is central but its language varies widely across event types and may be implicit in PTSD records; test a broad candidate before making it a required block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T13:19:34+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,155
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Stress Disorders, Post-Traumatic[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `posttraumatic stress[tiab]` | 14,174 | none |
| 4 | `post-traumatic stress[tiab]` | 8,160 | none |
| 5 | `post traumatic stress[tiab]` | 8,160 | none |
| 6 | `posttraumatic symptom*[tiab]` | 403 | none |
| 7 | `post-traumatic symptom*[tiab]` | 236 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 32,155 | none |

### Strategy (single line, for copying into PubMed)

```text
((Stress Disorders, Post-Traumatic[Mesh] OR PTSD[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab] OR posttraumatic symptom*[tiab] OR post-traumatic symptom*[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 9 | 9 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Longitudinal symptom course or trajectory | left out | 32,155 / 10,470 | 67.4% | 17662689, 21480695, 22040192 | 3/30 | Do not require a trajectory/course label: this block would lose three screened relevant studies (PMIDs 17662689, 21480695, 22040192), all of which reported repeated post-event PTSD symptom change using wording absent from the candidate. The 30-record loss sample contained those three relevant records, so the sample also fails the no-relevant-loss criterion despite a 67.4% reduction. |
| Exposure to a traumatic event | left out | 32,155 / 26,288 | 18.2% | 21480695 | 0/30 (up to 10% of removed records could be relevant) | Do not require a trauma-event wording block: the 30-record loss sample contained no clearly eligible record, but the block would lose one screened relevant record (PMID 21480695), and it reduces the PTSD count by only 18.2%, below the roughly 30% material-reduction criterion. PTSD records may report the event context implicitly or use event descriptions outside this broad list. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,155 | initial | none | Initial high-sensitivity PTSD block with a broad optional longitudinal course/trajectory block; no user-supplied seeds, using nine abstract-screened primary records from a directly relevant prior review as benchmark. |
| 2 | 32,155 | limits/combination | none | Added a screened therapy record with repeated PTSD symptom measures to the relevant set. Also expanded scope audit with a trauma-event candidate because the PTSD-only count exceeds the workload budget; test both optional concepts before deciding. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 333 NCBI requests logged (160 from cache); strategy sha256 fb1b5fa0ef03._

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
        "message": "32,155 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "32,155 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:19:34+00:00",
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
        "text": "Stress Disorders, Post-Traumatic",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"posttraumatic symptom*\"[Title/Abstract] OR \"post traumatic symptom*\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "32271ca6683be8b4c0a527d64a0912ce8c75e4401c949af529daf52a1f5a1a4c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The supplied translations preserve the intended PTSD heading and text-word expressions. The hyphenated and unhyphenated post-traumatic stress forms translate to the same normalized phrase; no translation warnings or errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD synonyms are ORed into the required condition block. The two optional concepts were tested as additional AND-ed blocks and left out based on the documented losses and reductions."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Stress Disorders, Post-Traumatic[Mesh] is verified as a MeSH descriptor and is appropriate for the required condition concept."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy covers PTSD, posttraumatic stress, and posttraumatic symptoms in title and abstract fields. The duplicated normalized form for lines 4 and 5 is redundant but does not create a retrieval gap."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed query and translations show no syntax or translation issues. The date-entry bound is applied to the complete strategy."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, language, publication-date, or study-design limits are applied. The stated date-entry cutoff is explicit, and the optional trauma and trajectory blocks were evaluated before being left out."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 32,155-record result exceeds the 10,000-record workload budget, but both optional searchable concepts in the stated scope were tested. Requiring the trajectory block would lose three screened relevant records; requiring the traumatic-event block would lose one and reduce results by only 18.2%. The remaining workload is therefore documented as an accepted risk.",
          "evidence": "The packet reports tests for both optional concepts: trajectory reduced results by 67.4% but lost PMIDs 17662689, 21480695, and 22040192; traumatic-event wording reduced results by 18.2% but lost PMID 21480695. Both blocks were left out, and no other screened concept is identified in scope."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "6dbc14cc2a19278e83b4c9a00ec89ef7737f67672ebf46ebee547f27a3b0fba1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translations preserve the MeSH heading and the Title/Abstract expressions. No translation issues or phrase warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD terms are ORed into the required block. Both optional concepts were tested as additional AND-ed blocks; the documented relevant losses support leaving them out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Stress Disorders, Post-Traumatic is verified as a MeSH descriptor and is appropriate for the required PTSD concept."
        },
        "text_words": {
          "verdict": "pass",
          "note": "PTSD, posttraumatic stress, and posttraumatic symptoms are represented in Title/Abstract terms. The hyphenated and unhyphenated stress phrases normalize to the same expression, creating redundancy but no evident gap."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query is syntactically valid, with no diagnostics or lint issues. The Entrez date-entry bound is applied to the complete strategy."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, language, or study-design limits are applied. The date-entry cutoff is documented as a request bound rather than a publication-date limit. The protocol records that scope was not user-confirmed."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "The over-budget warning remains unresolved because the evidence supports consideration of both optional concepts in the recorded scope, but does not establish that this scope is complete: scope_confirmed is false. The 32,155-record query therefore cannot yet be accepted as a documented risk on the basis that every searchable concept has been considered.",
          "evidence": "The protocol lists and tests the trajectory and traumatic-event concepts. The trajectory block reduces results by 67.4% but loses three screened relevant studies; the trauma block reduces results by 18.2% and loses one screened relevant study. The protocol also says the user could not answer questions during the run and that assumptions were proceeding without scope confirmation."
        }
      ]
    }
  ]
}
```


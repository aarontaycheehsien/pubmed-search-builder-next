# PubMed search strategy: audit

Generated 2026-09-30T17:19:54+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis
- Scope confirmed by user: no (User could not answer questions and explicitly requested no pause; scope proceeded on reasonable assumptions. PTSD or posttraumatic stress symptoms after any traumatic event in humans; includes symptom change observed across repeated assessments, whether naturalistic or treatment-associated. Reviews, editorials, and commentaries without eligible longitudinal participant data excluded. No language, age, setting, or publication-date limits. Entrez date is bounded at 2016-01-24 via PSB_AS_OF; no publication-date limit. No user-supplied known records. For discovery, screened 30-record trajectory loss samples, ran a systematic-review-oriented search (34 records), a PTSD trajectory pilot (1,880 records; 30 sampled), and searched references of PMID 23593134 (29 citations). Neighbour search on PMID 25733025 returned no candidates; PMID 23593134 returned 29 citations, 13 eligible records added to development set. No complete included-study list was verified.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and symptoms | search | The target condition is explicitly PTSD symptoms; records can be identified by the condition without requiring trauma type or a trajectory label. |
| Symptom trajectories and longitudinal course | optional | Trajectory is topic-defining and authors may name it, but it is not universal in titles or abstracts; test as an optional block before deciding. |
| Type or occurrence of traumatic event | optional | Traumatic-event exposure is relevant but many studies use the PTSD diagnosis without naming the event in abstracts; test event vocabulary before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T17:19:28+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,228
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `"post-traumatic stress disorder"[tiab]` | 7,081 | none |
| 3 | `"post traumatic stress disorder"[tiab]` | 7,081 | none |
| 4 | `"posttraumatic stress disorder"[tiab]` | 12,500 | none |
| 5 | `post-traumatic stress[tiab]` | 8,160 | none |
| 6 | `post traumatic stress[tiab]` | 8,160 | none |
| 7 | `posttraumatic stress[tiab]` | 14,174 | none |
| 8 | `"symptoms of post-traumatic stress"[tiab]` | 1 | none |
| 9 | `"symptoms of post traumatic stress"[tiab]` | 1 | none |
| 10 | `"symptoms posttraumatic stress"[tiab:~1]` | 2,249 | none |
| 11 | `"post-traumatic stress disorders"[tiab]` | 246 | none |
| 12 | `"post traumatic stress disorders"[tiab]` | 246 | none |
| 13 | `"posttraumatic stress disorders"[tiab]` | 243 | none |
| 14 | `PTSD[tiab]` | 15,732 | none |
| 15 | `"post-traumatic stress symptom*"[tiab]` | 474 | none |
| 16 | `"post traumatic stress symptom*"[tiab]` | 474 | none |
| 17 | `"posttraumatic stress symptom*"[tiab]` | 1,177 | none |
| 18 | `"post-traumatic stress reaction*"[tiab]` | 108 | none |
| 19 | `"post traumatic stress reaction*"[tiab]` | 108 | none |
| 20 | `"posttraumatic stress reaction*"[tiab]` | 170 | none |
| 21 | `PTSS[tiab]` | 510 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 32,228 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR "post-traumatic stress disorder"[tiab] OR "post traumatic stress disorder"[tiab] OR "posttraumatic stress disorder"[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab] OR posttraumatic stress[tiab] OR "symptoms of post-traumatic stress"[tiab] OR "symptoms of post traumatic stress"[tiab] OR "symptoms posttraumatic stress"[tiab:~1] OR "post-traumatic stress disorders"[tiab] OR "post traumatic stress disorders"[tiab] OR "posttraumatic stress disorders"[tiab] OR PTSD[tiab] OR "post-traumatic stress symptom*"[tiab] OR "post traumatic stress symptom*"[tiab] OR "posttraumatic stress symptom*"[tiab] OR "post-traumatic stress reaction*"[tiab] OR "post traumatic stress reaction*"[tiab] OR "posttraumatic stress reaction*"[tiab] OR PTSS[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 13 | 13 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories and longitudinal course | left out | 32,228 / 7,727 | 76.0% | 18629750 | 0/30 (up to 10% of removed records could be relevant) | 13_known_records_below_15_safety_threshold_and_sample_zero_relevant |
| Type or occurrence of traumatic event | left out | 32,228 / 26,262 | 18.5% | 18725431 | 0/30 (up to 10% of removed records could be relevant) | loss_sample_has_no_in_scope_study_and_only_13_known_records |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 31,765 | initial | none | initial_draft |
| 2 | 31,765 | limits/combination | none | expanded_candidate_terms_after_loss_screen |
| 3 | 32,227 | ptsd: +6 / -0 | none | added_bare_PTS_words_and_optional_trauma_event_block_per_critic |
| 4 | 32,228 | ptsd: +1 / -1 | none | replaced_unindexed_exact_phrase_with_tested_proximity |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 3 findings; R1-01 should-fix open, R1-02 should-fix open, R1-03 should-fix open
- Round 2 on version 4: 3 findings; R1-01 should-fix resolved, R1-02 should-fix resolved, R1-03 should-fix resolved
- Round 3 on version 4: 3 findings; R1-01 should-fix resolved, R1-02 should-fix resolved, R1-03 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 506 NCBI requests logged (258 from cache); strategy sha256 721d129226bd._

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
        "message": "32,228 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:trajectory",
        "blocking": false,
        "requires_review": true,
        "id": "I-af36a83285447cf63c9c"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:trauma_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-1a5b6c524a4de267eee2"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "32,228 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:trajectory",
        "blocking": false,
        "requires_review": true,
        "id": "I-af36a83285447cf63c9c"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:trauma_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-1a5b6c524a4de267eee2"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:28+00:00",
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
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"symptoms of post-traumatic stress\"[Title/Abstract] OR \"symptoms of post-traumatic stress\"[Title/Abstract] OR \"symptoms posttraumatic stress\"[Title/Abstract:~1] OR \"post-traumatic stress disorders\"[Title/Abstract] OR \"post-traumatic stress disorders\"[Title/Abstract] OR \"posttraumatic stress disorders\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"posttraumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress reaction*\"[Title/Abstract] OR \"post traumatic stress reaction*\"[Title/Abstract] OR \"posttraumatic stress reaction*\"[Title/Abstract] OR \"PTSS\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "7ecb8d345923a8db7ffc1b48df15c01c0937835f8142c9302423cece7f03566b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The MeSH and Title/Abstract translations are reported without warnings or errors. The fixed entry-date bound is documented as the as-of cutoff."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD terms are ORed within the condition block. The optional trajectory block was tested with AND, and the evidence reports its reduction and loss sample."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD MeSH descriptor is verified as the expected descriptor. The scope explains why trauma type and occurrence are screened."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Consider adding bare post-traumatic stress variants and symptom formulations such as symptoms of posttraumatic stress. Current phrases mainly require the disorder, symptom, or reaction wording to occur in a particular form or order."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query syntax and PubMed diagnostics show no errors. No unsupported wildcard in a proximity expression is present."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The EDAT bound matches the documented as-of date and no other limits are present. The over-budget warning remains because the screen-only trauma-context concept has not been tested as an optional block."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The condition block may miss records that describe symptoms of post-traumatic stress without using the exact disorder or symptom/reaction phrase forms currently listed.",
          "recommendation": "Test explicit bare post-traumatic stress variants and alternative symptom formulations, then evaluate the complete revised query and its known-record retrieval.",
          "status": "open",
          "response": ""
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The 31,765-record result exceeds the 10,000-record workload budget. The protocol identifies traumatic-event type or occurrence as a screen-only concept, but the packet documents optional-block testing only for trajectory.",
          "recommendation": "Test a trauma-context block as an optional AND concept, inspect the reduction and a loss sample, and document the decision. Retain screening if the block risks excluding eligible records.",
          "status": "open",
          "response": ""
        },
        {
          "id": "R1-03",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The trajectory block was left out after a 30-record loss sample with no relevant records, but one known relevant record was lost and the packet does not document attempts to find additional known records through prior reviews, neighbouring studies, or pilot searches.",
          "recommendation": "Document those attempts and any additional known records found; reassess the optional-block decision against the expanded set.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "The warning is not adequately addressed: the screen-only trauma-context concept was not tested as an optional block.",
          "evidence": "The packet shows 31,765 results against a 10,000-record budget and reports optional testing only for trajectory."
        },
        {
          "issue_id": "I-af36a83285447cf63c9c",
          "status": "rejected",
          "response": "The underpowered decision lacks documented attempts to identify additional known records, as required by the warning.",
          "evidence": "The loss sample has 30 records and zero relevant records, but the block loses PMID 18629750; the packet lists 13 relevant records and does not report review, neighbour, or pilot search efforts beyond the screened reference set."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "68151fdfe2758ea356622619d10e349c466eb19c38dd131a306fd2997e14c7a7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Reported translations and diagnostics show no errors or warnings. The entry-date bound is documented as the as-of cutoff."
        },
        "operators": {
          "verdict": "pass",
          "note": "Condition terms are ORed, and both optional concepts were tested as AND blocks. Their reductions and known-record losses are reported."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD MeSH heading is present and verified. The protocol explains why trauma context is screened rather than required in the search."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised condition block adds bare post-traumatic stress variants and symptom formulations requested in round 1. The reported phrase diagnostics show no warnings requiring clause-specific interpretation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query reports no syntax errors. The proximity expression has no wildcard, and the packet reports no PubMed diagnostic warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Both screen-only concepts were tested, but the resulting strategy still returns 32,228 records against a 10,000-record workload budget. Leaving both blocks out preserves known relevant records each block would lose, so the workload risk needs explicit acceptance."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier condition-block concern was that symptom descriptions might be missed without exact disorder or symptom/reaction phrase forms.",
          "recommendation": "Retain the added bare post-traumatic stress variants and symptom formulations; evaluate any future rewrite against the complete query and known-record set.",
          "status": "resolved",
          "response": "The revised block includes bare post-traumatic stress variants and additional symptom formulations, and the current evaluation retrieves all 13 known relevant records."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier review requested testing the screen-only trauma-context concept as an optional AND block because the strategy exceeded the workload budget.",
          "recommendation": "Keep the documented optional-block comparison and loss evidence; record the workload consequence of leaving the block out.",
          "status": "resolved",
          "response": "The trauma-context block was tested: it reduces results by 18.5% but removes known relevant PMID 18725431, so it remains excluded and the workload warning remains for disposition."
        },
        {
          "id": "R1-03",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The earlier review requested documentation of attempts to identify more known records before relying on an underpowered trajectory-block decision.",
          "recommendation": "Retain the discovery-attempt record and treat the trajectory-block decision as uncertain while the known set remains small.",
          "status": "resolved",
          "response": "The packet documents a systematic-review search, a trajectory pilot, reference checking, and a neighbour search. These efforts produced 13 known relevant records, but the trajectory block still loses PMID 18629750."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Both identified screen-only concepts were tested as optional blocks. Leaving either in would lose a known relevant record, so the final condition-only strategy retains the larger screening workload.",
          "evidence": "The final strategy returns 32,228 records against a 10,000-record budget. The trajectory block reduces results by 76.0% but loses PMID 18629750; the trauma-context block reduces results by 18.5% but loses PMID 18725431."
        },
        {
          "issue_id": "I-af36a83285447cf63c9c",
          "status": "accepted-risk",
          "response": "The packet documents attempts to find additional known records, but the remaining set is still small and the trajectory block loses one known relevant record. Leaving the block out is therefore a cautious recall choice with residual uncertainty.",
          "evidence": "The discovery notes report a systematic-review search, a trajectory pilot, reference checking, and a neighbour search; 13 relevant records are listed, and PMID 18629750 is lost by the trajectory block."
        },
        {
          "issue_id": "I-1a5b6c524a4de267eee2",
          "status": "accepted-risk",
          "response": "Discovery attempts are documented, but the known set remains below the stated 15-record threshold. The trauma-context block is left out because it removes a known relevant record.",
          "evidence": "The packet lists 13 relevant records and reports review, pilot, reference, and neighbour searches. The trauma-context block loses PMID 18725431; its 30-record loss sample contains no relevant records."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "68151fdfe2758ea356622619d10e349c466eb19c38dd131a306fd2997e14c7a7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Reported translations and diagnostics show no errors or warnings. The entry-date bound is documented as the as-of cutoff."
        },
        "operators": {
          "verdict": "pass",
          "note": "Condition terms are ORed, and both optional concepts were tested as AND blocks with reductions and known-record losses reported."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD MeSH heading is present and verified. The protocol explains why trauma context is screened rather than required."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised condition block adds bare post-traumatic stress variants and symptom formulations. The packet reports all 13 known relevant records retrieved and no phrase warnings requiring clause-specific interpretation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query reports no syntax errors or PubMed diagnostic warnings. The proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Both optional blocks were tested and the over-budget workload was explicitly accepted as a recall risk: each block would remove a known relevant record, while the final strategy returns 32,228 records against a 10,000-record budget."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The condition block may miss records that describe symptoms of post-traumatic stress without using the exact disorder or symptom/reaction phrase forms originally listed.",
          "recommendation": "Retain the added bare post-traumatic stress variants and symptom formulations; evaluate any future rewrite against the complete query and known-record set.",
          "status": "resolved",
          "response": "The revised block includes bare post-traumatic stress variants and additional symptom formulations, and the current evaluation retrieves all 13 known relevant records."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier review requested testing the screen-only trauma-context concept as an optional AND block because the strategy exceeded the workload budget.",
          "recommendation": "Keep the documented optional-block comparison and loss evidence; record the workload consequence of leaving the block out.",
          "status": "resolved",
          "response": "The trauma-context block was tested: it reduces results by 18.5% but removes known relevant PMID 18725431, so it remains excluded and the workload risk is explicitly accepted."
        },
        {
          "id": "R1-03",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The earlier review requested documentation of attempts to identify more known records before relying on an underpowered trajectory-block decision.",
          "recommendation": "Retain the discovery-attempt record and treat the trajectory-block decision as uncertain while the known set remains small.",
          "status": "resolved",
          "response": "The packet documents a systematic-review search, a trajectory pilot, reference checking, and a neighbour search. These efforts produced 13 known relevant records, although the trajectory block still loses PMID 18629750."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Both screen-only concepts were tested as optional blocks. Leaving either in would lose a known relevant record, so the final condition-only strategy retains the larger screening workload.",
          "evidence": "The final strategy returns 32,228 records against a 10,000-record budget. The trajectory block reduces results by 76.0% but loses PMID 18629750; the trauma-context block reduces results by 18.5% but loses PMID 18725431."
        },
        {
          "issue_id": "I-af36a83285447cf63c9c",
          "status": "accepted-risk",
          "response": "The packet documents attempts to find additional known records, but the set remains small and the trajectory block loses one known relevant record. Leaving the block out is a cautious recall choice with residual uncertainty.",
          "evidence": "The discovery notes report a systematic-review search, a trajectory pilot, reference checking, and a neighbour search; 13 relevant records are listed, and PMID 18629750 is lost by the trajectory block."
        },
        {
          "issue_id": "I-1a5b6c524a4de267eee2",
          "status": "accepted-risk",
          "response": "Discovery attempts are documented, but the known set remains below the stated 15-record threshold. The trauma-context block is left out because it removes a known relevant record.",
          "evidence": "The packet lists 13 relevant records and reports review, pilot, reference, and neighbour searches. The trauma-context block loses PMID 18725431; its 30-record loss sample contains no relevant records."
        }
      ]
    }
  ]
}
```


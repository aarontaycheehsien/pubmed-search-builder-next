# PubMed search strategy: audit

Generated 2026-09-28T14:24:05+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis / symptom course
- Scope confirmed by user: no (User requested proceeding without clarification. Assumed broad human trauma populations and event types, no age, setting, language, publication date, or design restrictions, and repeated assessment/longitudinal symptom course as eligibility criteria. No known relevant articles supplied. The harness cutoff is PubMed Entrez date 2016-01-24 (also set via PSB_AS_OF for every command). PubMed-only discovery; no web search. Scope roles set from the question before examining records.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder or post-traumatic stress symptoms | search | The target condition is required and is commonly named or indexed. |
| PTSD symptom trajectories or longitudinal course | optional | This defines the topic and is searchable, but authors may describe longitudinal symptom course without using trajectory terminology; test before deciding whether to require it. |
| Traumatic event or exposure | optional | The question requires trauma exposure and event labels are searchable, but exposure may be implicit or inconsistently named; test a broad trauma block before deciding whether to require it. |
| Longitudinal/repeated assessment design | screen | Repeated measurement is essential at screening but design terms are inconsistently named and no validated design filter is required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T14:23:18+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 11,779
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `"post-traumatic stress disorder"[tiab]` | 7,081 | none |
| 4 | `"post traumatic stress disorder"[tiab]` | 7,081 | none |
| 5 | `"posttraumatic stress disorder"[tiab]` | 12,500 | none |
| 6 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 7 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 8 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 9 | `"post-traumatic stress symptom*"[tiab]` | 474 | none |
| 10 | `"post traumatic stress symptom*"[tiab]` | 474 | none |
| 11 | `"posttraumatic stress symptom*"[tiab]` | 1,177 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 32,074 | none |
| 13 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 14 | `"Follow-Up Studies"[Mesh]` | 555,748 | none |
| 15 | `"Disease Progression"[Mesh]` | 138,666 | none |
| 16 | `"Time Factors"[Mesh]` | 1,073,830 | none |
| 17 | `trajectory[tiab]` | 24,167 | none |
| 18 | `trajectories[tiab]` | 25,088 | none |
| 19 | `longitudinal[tiab]` | 168,713 | none |
| 20 | `course[tiab]` | 460,316 | none |
| 21 | `courses[tiab]` | 59,665 | none |
| 22 | `"natural course"[tiab]` | 6,566 | none |
| 23 | `"natural history"[tiab]` | 39,676 | none |
| 24 | `"follow-up"[tiab]` | 703,004 | none |
| 25 | `followup[tiab]` | 670,163 | none |
| 26 | `"follow up"[tiab]` | 703,004 | none |
| 27 | `"symptom trajectory"[tiab:~2]` | 92 | none |
| 28 | `"symptom course"[tiab:~2]` | 349 | none |
| 29 | `"change over time"[tiab:~2]` | 8,343 | none |
| 30 | `recovery[tiab]` | 341,793 | none |
| 31 | `remission[tiab]` | 92,395 | none |
| 32 | `chronicity[tiab]` | 7,037 | none |
| 33 | `persistence[tiab]` | 68,487 | none |
| 34 | `"delayed onset"[tiab:~2]` | 8,812 | none |
| 35 | `change*[tiab]` | 2,336,850 | none |
| 36 | `evolution[tiab]` | 251,890 | none |
| 37 | `improvement[tiab]` | 435,465 | none |
| 38 | `worsen*[tiab]` | 62,308 | none |
| 39 | `decrease*[tiab]` | 1,826,276 | none |
| 40 | `pattern[tiab]` | 565,490 | none |
| 41 | `patterns[tiab]` | 523,313 | none |
| 42 | `decreasing[tiab]` | 146,034 | none |
| 43 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42` | 7,057,083 | none |
| 44 | `#12 AND #43` | 11,779 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR "post-traumatic stress disorder"[tiab] OR "post traumatic stress disorder"[tiab] OR "posttraumatic stress disorder"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress symptom*"[tiab] OR "post traumatic stress symptom*"[tiab] OR "posttraumatic stress symptom*"[tiab]) AND ("Longitudinal Studies"[Mesh] OR "Follow-Up Studies"[Mesh] OR "Disease Progression"[Mesh] OR "Time Factors"[Mesh] OR trajectory[tiab] OR trajectories[tiab] OR longitudinal[tiab] OR course[tiab] OR courses[tiab] OR "natural course"[tiab] OR "natural history"[tiab] OR "follow-up"[tiab] OR followup[tiab] OR "follow up"[tiab] OR "symptom trajectory"[tiab:~2] OR "symptom course"[tiab:~2] OR "change over time"[tiab:~2] OR recovery[tiab] OR remission[tiab] OR chronicity[tiab] OR persistence[tiab] OR "delayed onset"[tiab:~2] OR change*[tiab] OR evolution[tiab] OR improvement[tiab] OR worsen*[tiab] OR decrease*[tiab] OR pattern[tiab] OR patterns[tiab] OR decreasing[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 14 | 14 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| PTSD symptom trajectories or longitudinal course | AND-ed | 32,074 / 11,779 | 63.3% | none | 0/30 (up to 10% of removed records could be relevant) | After the latest query wording, none of 28 records available under the 2016-01-24 Entrez bound in the fresh 30-record loss sample met the stated PTSD-course eligibility; PMID 16968644, found in the earlier loss sample, is now retrieved by decreasing[tiab]. The two sampled PMIDs unavailable under the bound were treated as out-of-scope for this run. Current known relevant records are still retrieved. |
| Traumatic event or exposure | left out | 11,779 / 9,764 | 17.1% | 11004740, 18725431, 23062812, 25308059 | 3/30 | The tested trauma block reduces 11,779 to 9,764 but loses held-out validation PMID 18725431 and three relevant records (PMIDs 11004740, 23062812, 25308059) because event exposure may be implicit or indexed under a specific clinical event. The fresh 30-record loss sample was screened; the three additional eligible records reinforce the decision to leave this block out for recall. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 7,057,083 | 0 |
| trajectory | 32,074 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-layer PTSD condition block; trajectory/course kept as an optional block for measured testing. Terms include MeSH, text variants, and candidate course labels. |
| 2 | 32,074 | limits/combination | none | Expanded optional course vocabulary after screening the optional loss sample: repeated symptom change/evolution terms added; a newly identified eligible daily-assessment trajectory record was added to the development set. |
| 3 | 10,799 | trajectory: +27 / -0 | none | AND-ed the optional trajectory block after its measured test: 66.3% reduction, no known record loss, and 0 clearly eligible records among 29 cutoff-valid loss-sample records. Terms were expanded first to capture symptom change/evolution wording. |
| 4 | 11,722 | trajectory: +2 / -0 | none | Round-1 critic fix: add pattern(s) to the trajectory block as named in eligibility. In response to the workload review, promote trauma exposure from screening to an optional candidate and measure it before deciding whether to AND it. |
| 5 | 11,722 | limits/combination | none | Round-1 critic fixes: pattern(s) added to trajectory block. Trauma exposure is now a candidate optional block for mandatory workload screening review; evaluating its count and known-record loss before a decision. |
| 6 | 11,779 | trajectory: +1 / -0 | none | Screening the refreshed optional loss sample identified PMID 16968644, a prospective post-crash study with repeated post-traumatic stress assessments. Added it to the development set and added decreasing[tiab] for the abstract's symptom decline wording; re-evaluate both optional decisions. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-F1 must-fix open, R1-F2 must-fix open
- Round 2 on version 6: 2 findings; R1-F1 must-fix resolved, R1-F2 must-fix resolved
- Round 3 on version 6: 2 findings; R1-F1 must-fix resolved, R1-F2 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1332 NCBI requests logged (284 from cache); strategy sha256 f0867d133229._

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
        "message": "11,779 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "11,779 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-28T14:23:18+00:00",
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
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:23:18+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:23:18+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Follow-Up Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Disease Progression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:23:18+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "\"Disease Progression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Time Factors",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:23:18+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013997",
          "name": "Time Factors",
          "type": "descriptor",
          "scope_note": "Elements of limited time intervals, contributing to particular results or situations.",
          "tree_numbers": [
            "G01.910.857"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013997",
      "preferred_label": "Time Factors",
      "type": "descriptor",
      "location": "vocabulary:15",
      "term": {
        "text": "\"Time Factors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"posttraumatic stress symptom*\"[Title/Abstract]) AND (\"Longitudinal Studies\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"Disease Progression\"[MeSH Terms] OR \"Time Factors\"[MeSH Terms] OR \"trajectory\"[Title/Abstract] OR \"trajectories\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"courses\"[Title/Abstract] OR \"natural course\"[Title/Abstract] OR \"natural history\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"symptom trajectory\"[Title/Abstract:~2] OR \"symptom course\"[Title/Abstract:~2] OR \"change over time\"[Title/Abstract:~2] OR \"recovery\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"chronicity\"[Title/Abstract] OR \"persistence\"[Title/Abstract] OR \"delayed onset\"[Title/Abstract:~2] OR \"change*\"[Title/Abstract] OR \"evolution\"[Title/Abstract] OR \"improvement\"[Title/Abstract] OR \"worsen*\"[Title/Abstract] OR \"decrease*\"[Title/Abstract] OR \"pattern\"[Title/Abstract] OR \"patterns\"[Title/Abstract] OR \"decreasing\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "d3eb002bd882c94b288ca8df90f8ac295c38d90f4847d722c1af0af2fddab9d3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block covers the named disorder and symptom forms. No translation warnings or errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD and trajectory blocks are combined with AND, and terms within each block with OR, matching the stated strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD heading and trajectory-related headings are reported as verified MeSH descriptors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Eligibility explicitly names symptom patterns, but the trajectory block has no bare pattern term."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint, translation, or PubMed query errors. Proximity phrases contain no wildcards."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final set exceeds the 10,000-record budget, and the packet does not show an optional-block evaluation for the screened trauma-exposure concept."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes symptom patterns, but the trajectory block does not search pattern(s) as bare title/abstract terms.",
          "recommendation": "Add explicit pattern[tiab] and patterns[tiab] terms, then run a complete evaluation.",
          "status": "open"
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The final query returns 10,799 records against a 10,000-record budget. The packet tests the trajectory concept as an optional block but does not report an optional-block evaluation for the screened traumatic-event/exposure concept.",
          "recommendation": "Evaluate whether a trauma-exposure block is appropriate as an optional block, documenting its effect and recall risks; then rerun the complete evaluation and account for the budget.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "The over-budget warning is valid pending consideration of the screened trauma-exposure concept as an optional block.",
          "evidence": "The final count is 10,799 versus a 10,000 budget. The tested optional-concept table lists only the PTSD symptom trajectory/course block; traumatic event or exposure is identified as a screened concept."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "5a0f4567c40eec288bf3da91c7770817aa7dc32c09b4b710c1519f6d2fbb7cd4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation warnings or errors. The current query translation covers the PTSD and trajectory terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "PTSD and trajectory blocks are joined with AND, terms within each block with OR, and the trauma block was evaluated separately as an optional concept."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the PTSD and trajectory MeSH headings as verified descriptors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The trajectory block now includes bare pattern[tiab] and patterns[tiab] terms, addressing R1-F1. It also searches the other named course and change concepts."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or PubMed query errors. The proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The optional trauma concept has now been evaluated: requiring it would lose a held-out validation record and three other relevant records, so it was left out. The final count remains above budget; see the accepted-risk disposition."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes symptom patterns, but the trajectory block does not search pattern(s) as bare title/abstract terms.",
          "recommendation": "Add explicit pattern[tiab] and patterns[tiab] terms, then run a complete evaluation.",
          "status": "resolved",
          "response": "The current trajectory block includes both pattern[tiab] and patterns[tiab], and the complete evaluation reports retrieval of all 18 known relevant and validation records."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The final query returns 10,799 records against a 10,000-record budget. The packet tests the trajectory concept as an optional block but does not report an optional-block evaluation for the screened traumatic-event/exposure concept.",
          "recommendation": "Evaluate whether a trauma-exposure block is appropriate as an optional block, documenting its effect and recall risks; then rerun the complete evaluation and account for the budget.",
          "status": "resolved",
          "response": "The current packet evaluates the trauma block, reports its reduction from 11,779 to 9,764, and documents losses of validation PMID 18725431 and relevant PMIDs 11004740, 23062812, and 25308059. It was left out to preserve recall; the remaining budget overage is dispositioned separately."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the remaining over-budget count to preserve recall. The tested trauma block would reduce results below the 10,000-record budget but lose a held-out validation record and three relevant records. The trajectory/course block has also been tested as optional, and repeated-assessment design remains a screening criterion.",
          "evidence": "The current query returns 11,779 records against a 10,000-record budget. Adding the trauma block reduces the count to 9,764 but loses PMID 18725431 and PMIDs 11004740, 23062812, and 25308059. The trajectory block retrieves all 18 known relevant and validation records."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "5a0f4567c40eec288bf3da91c7770817aa7dc32c09b4b710c1519f6d2fbb7cd4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation warnings or errors for the current strategy."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD and trajectory blocks are combined with AND, and their terms with OR. The trauma block was tested separately as an optional concept."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the PTSD and trajectory MeSH headings as verified descriptors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The trajectory block includes bare pattern[tiab] and patterns[tiab] terms, covering the named symptom-pattern concept."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or PubMed query errors; the proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The trauma concept was evaluated and left out because it loses a held-out validation record and three relevant records. The remaining count exceeds the workload budget, and that overage is dispositioned as accepted risk."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes symptom patterns, but the trajectory block does not search pattern(s) as bare title/abstract terms.",
          "recommendation": "Add explicit pattern[tiab] and patterns[tiab] terms, then run a complete evaluation.",
          "status": "resolved",
          "response": "The current trajectory block includes both pattern[tiab] and patterns[tiab], and the complete evaluation reports retrieval of all 18 known relevant and validation records."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The final query returns 10,799 records against a 10,000-record budget. The packet tests the trajectory concept as an optional block but does not report an optional-block evaluation for the screened traumatic-event/exposure concept.",
          "recommendation": "Evaluate whether a trauma-exposure block is appropriate as an optional block, documenting its effect and recall risks; then rerun the complete evaluation and account for the budget.",
          "status": "resolved",
          "response": "The packet evaluates the trauma block, reports a reduction from 11,779 to 9,764, and documents losses of validation PMID 18725431 and relevant PMIDs 11004740, 23062812, and 25308059. It was left out to preserve recall; the remaining budget overage is dispositioned separately."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the remaining over-budget count to preserve recall. The tested trauma block would reduce the count below 10,000 but lose a held-out validation record and three relevant records. The trajectory/course block was also tested as optional.",
          "evidence": "The current query returns 11,779 records against a 10,000-record budget. Adding the trauma block reduces the count to 9,764 but loses PMID 18725431 and PMIDs 11004740, 23062812, and 25308059. The trajectory block retrieves all 18 known relevant and validation records."
        }
      ]
    }
  ]
}
```


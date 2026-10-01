# PubMed search strategy: audit

Generated 2026-10-01T11:20:57+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis / longitudinal course
- Scope confirmed by user: no (User supplied no known relevant articles and asked not to be queried during this run. Assumed broad population (any age or setting), any traumatic event, and original empirical longitudinal studies of PTSD symptom course. Harness requires PubMed to be pinned to 2016-01-24 by Entrez date (PSB_AS_OF); no publication-date [dp] limit is used. Trajectory/course is tested as an optional concept because it defines the topic but can be inconsistently named.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and PTSD symptoms | search | The condition and symptom domain define the review population and are searchable by established names and indexing. |
| Symptom trajectories and longitudinal course | optional | This topic-defining course concept is searchable but may be inconsistently named; test its retrieval value before deciding whether to AND it. |
| Traumatic event exposure | screen | The event context may be reported only in the methods and is best checked during screening. |
| Longitudinal empirical study design | screen | Repeated measurement and eligible trajectory methods require study-level screening; no unvalidated design filter will be used. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:20:11+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 10,252
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `"posttraumatic stress disorder"[tiab]` | 12,500 | none |
| 4 | `"posttraumatic stress disorders"[tiab]` | 243 | none |
| 5 | `"post-traumatic stress disorder"[tiab]` | 7,081 | none |
| 6 | `"post-traumatic stress disorders"[tiab]` | 246 | none |
| 7 | `"post traumatic stress disorder"[tiab]` | 7,081 | none |
| 8 | `"post traumatic stress disorders"[tiab]` | 246 | none |
| 9 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 10 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 11 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 12 | `"posttraumatic stress symptoms"[tiab]` | 1,060 | none |
| 13 | `"post-traumatic stress symptoms"[tiab]` | 429 | none |
| 14 | `"post traumatic stress symptoms"[tiab]` | 429 | none |
| 15 | `PTSS[tiab]` | 510 | none |
| 16 | `"posttraumatic neuroses"[tiab]` | 1 | none |
| 17 | `"post-traumatic neuroses"[tiab]` | 15 | none |
| 18 | `"post traumatic neuroses"[tiab]` | 15 | none |
| 19 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18` | 32,228 | none |
| 20 | `"Disease Progression"[Mesh]` | 138,666 | none |
| 21 | `"Follow-Up Studies"[Mesh]` | 555,748 | none |
| 22 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 23 | `"Time Factors"[Mesh]` | 1,073,830 | none |
| 24 | `"Prognosis"[Mesh]` | 1,288,746 | none |
| 25 | `trajector*[tiab]` | 43,863 | none |
| 26 | `course[tiab]` | 460,316 | none |
| 27 | `longitudinal[tiab]` | 168,713 | none |
| 28 | `prospective[tiab]` | 409,960 | none |
| 29 | `follow-up[tiab]` | 703,004 | none |
| 30 | `followup[tiab]` | 670,163 | none |
| 31 | `"natural history"[tiab]` | 39,676 | none |
| 32 | `"symptom course"[tiab]` | 86 | none |
| 33 | `"symptom change"[tiab]` | 558 | none |
| 34 | `"symptom changes"[tiab]` | 301 | none |
| 35 | `remission[tiab]` | 92,395 | none |
| 36 | `recovery[tiab]` | 341,793 | none |
| 37 | `chronicity[tiab]` | 7,037 | none |
| 38 | `persistence[tiab]` | 68,487 | none |
| 39 | `fluctuat*[tiab]` | 88,066 | none |
| 40 | `stability[tiab]` | 292,954 | none |
| 41 | `pattern*[tiab]` | 1,012,701 | none |
| 42 | `#20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41` | 5,094,790 | none |
| 43 | `#19 AND #42` | 10,252 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR "posttraumatic stress disorder"[tiab] OR "posttraumatic stress disorders"[tiab] OR "post-traumatic stress disorder"[tiab] OR "post-traumatic stress disorders"[tiab] OR "post traumatic stress disorder"[tiab] OR "post traumatic stress disorders"[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "posttraumatic stress symptoms"[tiab] OR "post-traumatic stress symptoms"[tiab] OR "post traumatic stress symptoms"[tiab] OR PTSS[tiab] OR "posttraumatic neuroses"[tiab] OR "post-traumatic neuroses"[tiab] OR "post traumatic neuroses"[tiab]) AND ("Disease Progression"[Mesh] OR "Follow-Up Studies"[Mesh] OR "Longitudinal Studies"[Mesh] OR "Time Factors"[Mesh] OR "Prognosis"[Mesh] OR trajector*[tiab] OR course[tiab] OR longitudinal[tiab] OR prospective[tiab] OR follow-up[tiab] OR followup[tiab] OR "natural history"[tiab] OR "symptom course"[tiab] OR "symptom change"[tiab] OR "symptom changes"[tiab] OR remission[tiab] OR recovery[tiab] OR chronicity[tiab] OR persistence[tiab] OR fluctuat*[tiab] OR stability[tiab] OR pattern*[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 18 | 18 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories and longitudinal course | AND-ed | 32,228 / 10,252 | 68.2% | none | 0/30 (up to 10% of removed records could be relevant) | After adding pattern*[tiab] in response to the independent critic, the block retains all 18 screened development records. Its measured count reduction remains substantial, and none of the refreshed 30-record loss sample met eligibility. The 10,252-record final count is 252 above the standard workload budget; the topic concept has been tested and the remaining overage is documented for critique rather than narrowed with an unsupported filter. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 5,094,790 | 0 |
| trajectory | 32,228 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first PTSD block with a fully developed optional symptom-course block; vocabulary includes controlled headings, MeSH entry terms, variants, and screened pilot language. |
| 2 | 32,228 | ptsd: +16 / -16 | none | Corrected block-combination configuration and made phrase searching explicit; included vocabulary from the screened pilot set. |
| 3 | 9,155 | trajectory: +21 / -0 | none | AND-ed the tested trajectory/course block after retaining all 18 known relevant records, observing a 71.6% count reduction, and screening a 30-record loss sample with zero eligible records. |
| 4 | 10,252 | trajectory: +1 / -0 | none | Added pattern*[tiab] to address the critic's lexical finding; recorded the harness-required Entrez-date cutoff explicitly as as_of without adding a publication-date limit. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-01 must-fix open, R1-02 must-fix open
- Round 2 on version 4: 2 findings; R1-01 must-fix resolved, R1-02 must-fix accepted-risk
- Round 3 on version 4: 2 findings; R1-01 must-fix resolved, R1-02 must-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1088 NCBI requests logged (426 from cache); strategy sha256 a5f3af26f861._

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
        "message": "10,252 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "10,252 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-10-01T11:20:11+00:00",
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
      "requested": "Disease Progression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:11+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Disease Progression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:11+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Follow-Up Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:11+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Time Factors",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:11+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Time Factors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Prognosis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:20:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011379",
          "name": "Prognosis",
          "type": "descriptor",
          "scope_note": "A prediction of the probable outcome of a disease based on a individual's condition and the usual course of the disease as seen in similar situations.",
          "tree_numbers": [
            "E01.789"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011379",
      "preferred_label": "Prognosis",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "\"Prognosis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress disorders\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorders\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorders\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress symptoms\"[Title/Abstract] OR \"post-traumatic stress symptoms\"[Title/Abstract] OR \"post-traumatic stress symptoms\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"posttraumatic neuroses\"[Title/Abstract] OR \"post-traumatic neuroses\"[Title/Abstract] OR \"post-traumatic neuroses\"[Title/Abstract]) AND (\"Disease Progression\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"Longitudinal Studies\"[MeSH Terms] OR \"Time Factors\"[MeSH Terms] OR \"Prognosis\"[MeSH Terms] OR \"trajector*\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"prospective\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"natural history\"[Title/Abstract] OR \"symptom course\"[Title/Abstract] OR \"symptom change\"[Title/Abstract] OR \"symptom changes\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"recovery\"[Title/Abstract] OR \"chronicity\"[Title/Abstract] OR \"persistence\"[Title/Abstract] OR \"fluctuat*\"[Title/Abstract] OR \"stability\"[Title/Abstract] OR \"pattern*\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "43d6ba61b9dec59b5294421482d90ab449e168b770b0f2b179d010f975c2500d",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Eligibility includes symptom patterns over time, but the trajectory block has no pattern term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD synonyms are OR-combined, the two concepts are AND-combined, and traumatic exposure and study design are appropriately left for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD heading is verified; the course block uses relevant longitudinal and follow-up headings alongside broader headings."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add a bare text word for the eligibility term patterns; the block currently relies on trajectory, course, and other course terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed Boolean structure and field tags are coherent, with no reported translation or syntax errors."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The date-entry bound is required by the harness's PubMed as-of setting; no publication-date limit is in the protocol."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "block": "trajectory",
          "finding": "Eligibility explicitly includes studies describing symptom patterns over time, but the AND-ed trajectory block contains no pattern term. Such records may be excluded when they do not use the listed trajectory or course wording.",
          "recommendation": "Add pattern*[tiab] to the trajectory block and run a complete evaluation of the revised strategy.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluated query applies an Entrez date-entry range ending 2016-01-24. The protocol says there is no date limit, so this bound would exclude subsequently entered records and conflicts with the stated scope.",
          "recommendation": "Keep the harness-required Entrez cutoff and document it as the search as_of bound; do not substitute a publication-date limit.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "1c6a9b53103e25ac9fffa82bff74e62a1e9660c6fbe1458fe3f3ead397b68a8b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The evaluated translation has no reported warnings or errors. The searched PTSD and course concepts are represented with their own terms, including bare course, pattern, and trajectory terms; trauma exposure and study design are assigned to screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined, and the PTSD and trajectory blocks are AND-combined. The trajectory block retains all 18 known records, satisfying the packet's optional-block rule for AND-ing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the PTSD heading and the course-related headings. The course block combines longitudinal and follow-up headings with broader course headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The trajectory block now includes pattern*[tiab], alongside course[tiab] and trajector*[tiab], covering the named symptom-course, pattern, and trajectory wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure and field tags are coherent, and the packet reports no translation or syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The query uses the documented harness-required Entrez date-entry cutoff through 2016-01-24; the protocol notes this as the as-of bound and does not apply a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility explicitly includes studies describing symptom patterns over time, but the AND-ed trajectory block contains no pattern term. Such records may be excluded when they do not use the listed trajectory or course wording.",
          "recommendation": "Add pattern*[tiab] to the trajectory block and run a complete evaluation of the revised strategy.",
          "status": "resolved",
          "response": "The current trajectory block includes pattern*[tiab]. The complete version 4 evaluation reports all 18 known records retrieved and no known records lost."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluated query applies an Entrez date-entry range ending 2016-01-24. The protocol says there is no date limit, so this bound would exclude subsequently entered records and conflicts with the stated scope.",
          "recommendation": "Keep the harness-required Entrez cutoff and document it as the search as_of bound; do not substitute a publication-date limit.",
          "status": "accepted-risk",
          "response": "The packet documents the required Entrez cutoff as the search as-of bound and confirms that no publication-date limit is used. The entry-date cutoff still limits retrieval to records entered by 2016-01-24."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final count is 10,252, 252 above the 10,000-record budget. The protocol explicitly assigns traumatic-event exposure and study design to screening because event details may appear only in methods and no validated design filter is being used. Retain screening for those concepts and accept the modest workload overage.",
          "evidence": "The packet states the 10,252 final count and 10,000 budget; the scope assigns trauma exposure and longitudinal empirical design to screening with those rationales. The trajectory block retains all 18 known records and its 30-record loss sample contains 0 relevant records."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "1c6a9b53103e25ac9fffa82bff74e62a1e9660c6fbe1458fe3f3ead397b68a8b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The current translation includes the PTSD and course concepts, including pattern*[tiab]. No translation warnings or errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined and the PTSD and trajectory blocks are AND-combined. The trajectory block retains all 18 known records, meeting the stated rule for AND-ing an optional block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the PTSD heading and the course-related headings used in the trajectory block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The trajectory block now includes pattern*[tiab], addressing the earlier omission; it also includes course[tiab] and trajector*[tiab]."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure and field tags are coherent, with no reported translation or syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date cutoff is documented as the harness-required as-of bound, and no publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility explicitly includes studies describing symptom patterns over time, but the original AND-ed trajectory block contained no pattern term.",
          "recommendation": "Add pattern*[tiab] to the trajectory block and run a complete evaluation of the revised strategy.",
          "status": "resolved",
          "response": "The current trajectory block includes pattern*[tiab]. The complete version 4 evaluation reports all 18 known records retrieved and no known records lost."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluated query applies an Entrez date-entry range ending 2016-01-24, limiting retrieval to records entered by that date.",
          "recommendation": "Keep the harness-required Entrez cutoff and document it as the search as_of bound; do not substitute a publication-date limit.",
          "status": "accepted-risk",
          "response": "The packet documents the required Entrez cutoff as the search as-of bound and confirms that no publication-date limit is used. The entry-date cutoff still limits retrieval to records entered by 2016-01-24."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final count remains 10,252, which is 252 above the 10,000-record budget. The searchable trajectory concept was tested as an optional block and AND-ed with all 18 known records retained. Traumatic-event exposure and longitudinal study design remain screening concepts under the stated rationales; the remaining overage is documented.",
          "evidence": "The packet reports 10,252 final results against a 10,000 budget, all 18 known records retrieved, no known records lost, and 0 relevant records in the refreshed 30-record loss sample. Scope assigns traumatic-event exposure and longitudinal empirical design to screening."
        }
      ]
    }
  ]
}
```


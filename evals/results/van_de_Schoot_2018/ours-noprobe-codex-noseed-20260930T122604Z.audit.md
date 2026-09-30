# PubMed search strategy: audit

Generated 2026-09-30T13:12:29+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis / longitudinal symptom course
- Scope confirmed by user: no (User asked to proceed without questions. Assumed all ages and traumatic events. PTSD is required; trajectory/course was tested and AND-ed based on all 20 known relevant records retained, a 66.8% retrieval reduction, and zero clearly relevant records in the loss sample. Traumatic event exposure was moved from screen to optional and left out after its 30-record loss sample included two relevant records; it cuts 18.8%, leaving 10,649 records, 649 above the default workload budget. Longitudinal design beyond trajectory labels is screened. No known relevant articles were supplied; development examples came from a screened PubMed pilot sample and loss samples. PubMed inventory is bounded by Entrez date 2016-01-24 using PSB_AS_OF; no publication-date limit is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder | search | The condition under study; required and consistently named/indexed. |
| PTSD symptom trajectories or course | optional | Topic-defining outcome with searchable labels, but authors may describe longitudinal change without using trajectory terminology; tested and AND-ed after meeting the evidence threshold and passing its loss sample. |
| Traumatic event exposure | optional | The question specifies post-event PTSD symptoms; trauma exposure is searchable by event and exposure terms but may be absent or only implicit in PTSD records, so test rather than require without evidence. |
| Longitudinal symptom assessment/design | screen | Relevant designs can be inconsistently labelled; screen study design and repeated symptom assessment. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:11:36+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 10,649
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `"posttraumatic stress disorder"[tiab]` | 12,500 | none |
| 4 | `"post-traumatic stress disorder"[tiab]` | 7,081 | none |
| 5 | `"post traumatic stress disorder"[tiab]` | 7,081 | none |
| 6 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 7 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 8 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 9 | `"posttraumatic stress symptoms"[tiab]` | 1,060 | none |
| 10 | `"post-traumatic stress symptoms"[tiab]` | 429 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 32,074 | none |
| 12 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 13 | `"Follow-Up Studies"[Mesh]` | 555,748 | none |
| 14 | `"Disease Progression"[Mesh]` | 138,666 | none |
| 15 | `"Time Factors"[Mesh]` | 1,073,830 | none |
| 16 | `trajectory[tiab]` | 24,167 | none |
| 17 | `trajectories[tiab]` | 25,088 | none |
| 18 | `course[tiab]` | 460,316 | none |
| 19 | `longitudinal[tiab]` | 168,713 | none |
| 20 | `follow-up[tiab]` | 703,004 | none |
| 21 | `followup[tiab]` | 670,163 | none |
| 22 | `prospectiv*[tiab]` | 506,579 | none |
| 23 | `persist*[tiab]` | 367,137 | none |
| 24 | `remission[tiab]` | 92,395 | none |
| 25 | `recover*[tiab]` | 513,916 | none |
| 26 | `chronic*[tiab]` | 944,256 | none |
| 27 | `fluctuat*[tiab]` | 88,066 | none |
| 28 | `progression[tiab]` | 353,159 | none |
| 29 | `"over time"[tiab]` | 128,863 | none |
| 30 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 4,648,263 | none |
| 31 | `#11 AND #30` | 10,649 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR "posttraumatic stress disorder"[tiab] OR "post-traumatic stress disorder"[tiab] OR "post traumatic stress disorder"[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "posttraumatic stress symptoms"[tiab] OR "post-traumatic stress symptoms"[tiab]) AND ("Longitudinal Studies"[Mesh] OR "Follow-Up Studies"[Mesh] OR "Disease Progression"[Mesh] OR "Time Factors"[Mesh] OR trajectory[tiab] OR trajectories[tiab] OR course[tiab] OR longitudinal[tiab] OR follow-up[tiab] OR followup[tiab] OR prospectiv*[tiab] OR persist*[tiab] OR remission[tiab] OR recover*[tiab] OR chronic*[tiab] OR fluctuat*[tiab] OR progression[tiab] OR "over time"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 20 | 20 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| PTSD symptom trajectories or course | AND-ed | 32,074 / 10,649 | 66.8% | none | 0/30 (up to 10% of removed records could be relevant) | After the base grew to 20 known relevant records, the tested trajectory/course block retains every record, removes 66.8% of PTSD-only results, and its current 30-record loss sample contains no clearly eligible record (one record without an abstract remains uncertain). AND the block to keep screening workload near the default budget; trauma exposure was separately tested and left out. |
| Traumatic event exposure | left out | 10,649 / 8,647 | 18.8% | 11481156, 15641864 | 2/30 | The block cuts only 18.8%, below the skill's material-reduction threshold for AND-ing; its 30-record loss sample included relevant records (PMIDs 11481156 and 15641864) with longitudinal PTSD symptom course after traffic accident or abuse. Retain event context for screening. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 4,648,263 | 0 |
| trajectory | 32,074 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,074 | initial | none | Initial broad PTSD condition block; optional course/trajectory block drafted from MeSH lookup and screened pilot vocabulary. |
| 2 | 10,649 | trajectory: +18 / -0 | none | Promoted the tested PTSD symptom-course block after retaining all 18 known relevant records and a clean sampled loss set; added an optional traumatic-event block to test because the base exceeded the default screening budget. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 2: 0 findings; 
- Round 3 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 576 NCBI requests logged (287 from cache); strategy sha256 edf2572d4093._

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
        "message": "10,649 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "10,649 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T13:11:36+00:00",
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
      "checked_at": "2026-09-30T13:11:36+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:36+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Follow-Up Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Disease Progression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:36+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Disease Progression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Time Factors",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:36+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "\"Time Factors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress symptoms\"[Title/Abstract] OR \"post-traumatic stress symptoms\"[Title/Abstract]) AND (\"Longitudinal Studies\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"Disease Progression\"[MeSH Terms] OR \"Time Factors\"[MeSH Terms] OR \"trajectory\"[Title/Abstract] OR \"trajectories\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"prospectiv*\"[Title/Abstract] OR \"persist*\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"recover*\"[Title/Abstract] OR \"chronic*\"[Title/Abstract] OR \"fluctuat*\"[Title/Abstract] OR \"progression\"[Title/Abstract] OR \"over time\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "ae0ad9efcd11f09db7541d587098b01646451b5bf72ca656ce0ea614950ee239",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy covers the PTSD condition and symptom trajectory/course concepts. The traumatic-event block was tested and appropriately left out after its loss sample found relevant records. PubMed translations show no warnings."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined within concept blocks; the PTSD and trajectory/course blocks are AND-combined with clear grouping."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD, longitudinal studies, follow-up studies, disease progression, and time factors headings are relevant to the searched concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes PTSD wording variants and a broad range of course, trajectory, and longitudinal vocabulary."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags, operators, parentheses, and truncation are consistent with recorded PubMed translations."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date bound matches 2016-01-24; no additional limits are applied."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final count exceeds the 10,000-record budget by 649 records. The trajectory/course block reduces the PTSD-only set by 66.8%; the trauma-event block reduces the result by only 18.8% and removes relevant records, so it remains out of the query. The workload warning is accepted after testing the searchable optional concepts.",
          "evidence": "The optional-concept evaluation reports both reductions and known losses. The trajectory/course loss sample found no clearly eligible record among 30, with one lacking an abstract; the trauma-event sample identified relevant PMIDs 11481156 and 15641864."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "ae0ad9efcd11f09db7541d587098b01646451b5bf72ca656ce0ea614950ee239",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block covers the condition and symptom wording. The course block contains course and longitudinal vocabulary; event exposure was tested and left out after its loss sample found relevant records."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined within blocks, and the PTSD and trajectory/course blocks are AND-combined with clear grouping."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD heading represents the condition; longitudinal, follow-up, disease progression, and time factors headings support course retrieval."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover PTSD variants and a broad range of course, trajectory, persistence, recovery, and longitudinal terminology."
        },
        "syntax": {
          "verdict": "pass",
          "note": "PubMed translations show consistent field tags, grouping, operators, and truncation, with no translation warnings or errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No additional filters are used. The entry-date bound matches 2016-01-24 and is not a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the nonblocking workload warning: the final set is 649 records above the 10,000-record budget after testing the searchable optional concepts. The trajectory/course block reduces the PTSD-only set by 66.8%; the traumatic-event block reduces the result by only 18.8% and removes relevant records, so it remains out of the query.",
          "evidence": "The trajectory/course loss sample found no clearly eligible records among 30, with one record lacking an abstract and remaining uncertain. The traumatic-event loss sample found relevant PMIDs 11481156 and 15641864. The resulting count is 10,649."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "ae0ad9efcd11f09db7541d587098b01646451b5bf72ca656ce0ea614950ee239",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block covers the condition and symptom wording, and the course block includes trajectory, course, and longitudinal terms. The traumatic-event block was tested and left out after its loss sample found relevant records. The current translation has no warnings or errors."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined within blocks; the PTSD and trajectory/course blocks are AND-combined with clear grouping."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD heading represents the condition; longitudinal studies, follow-up studies, disease progression, and time factors support course retrieval."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes PTSD variants and a broad range of trajectory, course, persistence, recovery, and longitudinal vocabulary."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags, grouping, operators, truncation, and entry-date range are consistent with the recorded PubMed translation; no syntax or translation errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No additional limits are applied. The entry-date range ends at the stated 2016-01-24 cutoff."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the nonblocking workload warning. The result count is 10,649, 649 above budget. The trajectory/course block reduces the PTSD-only set by 66.8%; the traumatic-event block reduces the result by only 18.8% and removes relevant records, so it remains out of the query after testing the searchable optional concepts.",
          "evidence": "The trajectory/course block retains all 20 known relevant records; its 30-record loss sample found no clearly eligible records, though one record lacked an abstract. The traumatic-event loss sample found relevant PMIDs 11481156 and 15641864. The resulting count is 10,649."
        }
      ]
    }
  ]
}
```


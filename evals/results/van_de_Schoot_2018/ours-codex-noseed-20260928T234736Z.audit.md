# PubMed search strategy: audit

Generated 2026-09-29T00:09:46+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis
- Scope confirmed by user: no (User could not answer follow-up questions and asked me to proceed with recorded assumptions; scope was not confirmed by the user. This is a prognosis question: PTSD is required; longitudinal symptom course/trajectory was tested as optional and AND-ed after a 44.9% reduction with 0/30 eligible records in the loss sample; traumatic event/exposure was tested as an optional category and left out after only 10.2% reduction, two known records lost, and category probes found relevant studies without stable event-name wording. Trauma type is handled at screening. Age, event type, language, and study design remain unrestricted; intervention studies with longitudinal PTSD symptom outcomes are included under the broad question. No known records were supplied. A 2015 systematic review on naturalistic PTSD course was screened, but the tool returned no reference neighbors, so no benchmark set was built. The as-of date is 2016-01-24; every PubMed script command used PSB_AS_OF=2016-01-24 and no publication-date limit was applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder | search | The condition is required and is consistently named/indexed. |
| Longitudinal symptom course or trajectory | optional | This defines the topic, but authors may report symptom course without labeling it a trajectory; test the block against retrieved records before requiring it. |
| Traumatic event or exposure | optional | Traumatic event is explicit in the question and event types are searchable but heterogeneous; test an event block against record losses before requiring it. This is a category because studies may name only a specific event type. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T00:08:57+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 17,663
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `posttraumatic stress disorder[tiab]` | 12,500 | none |
| 3 | `post-traumatic stress disorder[tiab]` | 7,081 | none |
| 4 | `post traumatic stress disorder[tiab]` | 7,081 | none |
| 5 | `posttraumatic stress disorders[tiab]` | 243 | none |
| 6 | `post-traumatic stress disorders[tiab]` | 246 | none |
| 7 | `post traumatic stress disorders[tiab]` | 246 | none |
| 8 | `PTSD[tiab]` | 15,732 | none |
| 9 | `posttraumatic stress[tiab]` | 14,174 | none |
| 10 | `post-traumatic stress[tiab]` | 8,160 | none |
| 11 | `post traumatic stress[tiab]` | 8,160 | none |
| 12 | `posttraumatic neuros*[tiab]` | 8 | none |
| 13 | `post-traumatic neuros*[tiab]` | 37 | none |
| 14 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 32,082 | none |
| 15 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 16 | `"Follow-Up Studies"[Mesh]` | 555,748 | none |
| 17 | `"Disease Progression"[Mesh]` | 138,666 | none |
| 18 | `"Time Factors"[Mesh]` | 1,073,830 | none |
| 19 | `trajector*[tiab]` | 43,863 | none |
| 20 | `longitudinal[tiab]` | 168,713 | none |
| 21 | `follow-up[tiab]` | 703,004 | none |
| 22 | `followup[tiab]` | 670,163 | none |
| 23 | `follow up[tiab]` | 703,004 | none |
| 24 | `course[tiab]` | 460,316 | none |
| 25 | `courses[tiab]` | 59,665 | none |
| 26 | `natural history[tiab]` | 39,676 | none |
| 27 | `remission[tiab]` | 92,395 | none |
| 28 | `remissions[tiab]` | 8,975 | none |
| 29 | `recurrence[tiab]` | 210,412 | none |
| 30 | `recurrent[tiab]` | 220,684 | none |
| 31 | `chronicity[tiab]` | 7,037 | none |
| 32 | `chronic[tiab]` | 904,712 | none |
| 33 | `persistent[tiab]` | 171,965 | none |
| 34 | `persistence[tiab]` | 68,487 | none |
| 35 | `symptom*[tiab]` | 863,549 | none |
| 36 | `growth mixture[tiab]` | 576 | none |
| 37 | `latent class[tiab]` | 2,971 | none |
| 38 | `latent trajector*[tiab]` | 114 | none |
| 39 | `#15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 4,341,673 | none |
| 40 | `#14 AND #39` | 17,663 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR posttraumatic stress disorder[tiab] OR post-traumatic stress disorder[tiab] OR post traumatic stress disorder[tiab] OR posttraumatic stress disorders[tiab] OR post-traumatic stress disorders[tiab] OR post traumatic stress disorders[tiab] OR PTSD[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab] OR posttraumatic neuros*[tiab] OR post-traumatic neuros*[tiab]) AND ("Longitudinal Studies"[Mesh] OR "Follow-Up Studies"[Mesh] OR "Disease Progression"[Mesh] OR "Time Factors"[Mesh] OR trajector*[tiab] OR longitudinal[tiab] OR follow-up[tiab] OR followup[tiab] OR follow up[tiab] OR course[tiab] OR courses[tiab] OR natural history[tiab] OR remission[tiab] OR remissions[tiab] OR recurrence[tiab] OR recurrent[tiab] OR chronicity[tiab] OR chronic[tiab] OR persistent[tiab] OR persistence[tiab] OR symptom*[tiab] OR growth mixture[tiab] OR latent class[tiab] OR latent trajector*[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Longitudinal symptom course or trajectory | AND-ed | 32,082 / 17,663 | 44.9% | none | 0/30 (up to 10% of removed records could be relevant) | The block reduces the PTSD set by 44.9%; it loses no known records and the standard loss sample found no studies clearly meeting the longitudinal PTSD symptom-course eligibility criteria. Because the sample screen suggests a material reduction with no detected relevant record, include it while retaining its residual false-negative risk. |
| Traumatic event or exposure | left out | 17,663 / 15,854 | 10.2% | 11838628, 17568299 | 0/30 (up to 10% of removed records could be relevant) | The expanded event block cuts only 10.2% of results and the current evaluation shows it misses two known in-scope treatment-course records, so it is not safe or material enough to AND. Its loss sample contained no eligible records, but 0/30 is limited reassurance. Category probes found relevant studies using illness/hospitalization contexts or events not captured reliably by the block; trauma type remains a screening criterion and records outside the block are a known risk. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Traumatic event or exposure | 1 | `event*[tiab] OR stressor*[tiab] OR exposure*[tiab]` | 289 | 1/30 |
| Traumatic event or exposure | 2 | `event*[tiab] OR stressor*[tiab] OR exposure*[tiab]` | 239 | 2/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 4,341,673 | 0 |
| trajectory | 32,082 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial PTSD condition block and optional symptom-trajectory course block; no seeds supplied. Scope and roles were set from question before record discovery. |
| 2 | 0 | ptsd: +13 / -0 | none | Corrected strategy structure to explicit OR-ed MeSH and title/abstract terms for PTSD and optional symptom-course block. |
| 3 | 0 | ptsd: +1 / -1 | none | Quoted multiword MeSH headings explicitly after lint identified malformed unquoted heading syntax. |
| 4 | 32,082 | limits/combination | none | Removed literal combine value AND; the strategy model uses a null combine for its default AND of blocks. |
| 5 | 17,663 | trajectory: +24 / -0 | none | Promoted the tested longitudinal symptom-course block to a required block after a 44.9% reduction and 0/30 eligible records in the sampled loss set. No known sets exist, so this is not recall validation. |
| 6 | 17,663 | limits/combination | none | Added traumatic event as an optional category concept for workload review; built a broad event-member block for testing. |
| 7 | 17,663 | limits/combination | none | Screened the trauma category probe and added surgical/medical illness member terms to address the in-scope record missed by the current event block; refreshed the evaluation. |
| 8 | 17,663 | limits/combination | none | Broadened the trauma category candidate with generic event, stressor and exposure wording after multiple relevant category-probe findings; refreshed counts and set recall. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 8 (Same-context critic; no fresh-context reviewer was available in this run.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 960 NCBI requests logged (545 from cache); strategy sha256 3fbd1752c3a0._

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
        "message": "17,663 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:trauma",
        "pmids": [
          "16971821",
          "19892213"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-d949ad3304b61ef4e359"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "17,663 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:trauma",
        "pmids": [
          "16971821",
          "19892213"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-d949ad3304b61ef4e359"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:08:57+00:00",
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
      "checked_at": "2026-09-29T00:08:57+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:08:57+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Follow-Up Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Disease Progression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:08:57+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Disease Progression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Time Factors",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:08:57+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "\"Time Factors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress disorders\"[Title/Abstract] OR \"post traumatic stress disorders\"[Title/Abstract] OR \"post traumatic stress disorders\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"posttraumatic neuros*\"[Title/Abstract] OR \"post traumatic neuros*\"[Title/Abstract]) AND (\"Longitudinal Studies\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"Disease Progression\"[MeSH Terms] OR \"Time Factors\"[MeSH Terms] OR \"trajector*\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"courses\"[Title/Abstract] OR \"natural history\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"remissions\"[Title/Abstract] OR \"recurrence\"[Title/Abstract] OR \"recurrent\"[Title/Abstract] OR \"chronicity\"[Title/Abstract] OR \"chronic\"[Title/Abstract] OR \"persistent\"[Title/Abstract] OR \"persistence\"[Title/Abstract] OR \"symptom*\"[Title/Abstract] OR \"growth mixture\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"latent trajector*\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 8,
      "review_sha256": "9d542129a24449c77317a53f17fa49d85b26f90e3aee139468e5ca03e21d76e1",
      "note": "Same-context critic; no fresh-context reviewer was available in this run.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required blocks match the PTSD condition and the topic-defining longitudinal symptom course. The trauma exposure concept was tested as an optional category and left out because it loses known in-scope records and offers only a small count reduction. The user could not confirm scope; assumptions and eligibility are recorded."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR joins synonyms within each concept, AND joins PTSD and course blocks, and the final query uses no NOT or unvalidated filter."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All final MeSH headings are explicitly tagged and verified. PTSD MeSH has no narrower headings. Longitudinal Studies, Follow-Up Studies, Disease Progression, and Time Factors are exploded by default; counts and tree details were inspected. The MeSH layer is complemented by title/abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "PTSD spelling and spacing variants, acronym, historic neurosis stem, trajectory, longitudinal course, follow-up, remission/recurrence, chronicity and symptom wording are represented. Broad terms are retained for recall; no term mining from held-out records occurred."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no lint errors, translation issues, field fallback, or phrase warnings. Every final term is field-tagged."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or study-design restriction is applied. The Entrez entry-date bound is 2016-01-24 as required."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload exceeds the standard budget, but both plausible searchable concepts beyond the required PTSD condition were considered as optional AND blocks. The longitudinal symptom-course block was AND-ed after a 44.9% reduction and a 0/30 relevant loss sample. The heterogeneous event/exposure block was left out after only a 10.2% reduction and loss of known in-scope records. Requiring an event-label block would risk excluding records that describe illness or treatment contexts without conventional trauma terms. The resulting larger screening workload is accepted to preserve recall.",
          "evidence": "The current evaluated strategy returns 17,663 records against a budget of 10,000. The trauma optional candidate would return 15,854, only an 10.2% reduction, and the evaluation lists relevant PMIDs 11838628 and 17568299 as losses. Its 30-record loss sample had no eligible records. The trajectory block's measured comparison was 32,082 without versus 17,663 with the block (44.9% reduction)."
        },
        {
          "issue_id": "I-d949ad3304b61ef4e359",
          "status": "accepted-risk",
          "response": "The two-probe standard budget was used. After the first relevant trauma-category probe finding, the optional event vocabulary was broadened; the second probe still identified records with implicit illness/hospitalization or study-event wording. No further probe was available at standard depth. The event block is not part of the final query, so these findings do not signal a known loss in the delivered search. They show that trauma type and event context require screening and that the candidate category vocabulary is incomplete.",
          "evidence": "Probe 1 screened 30 records and found PMID 9497102, whose abstract measured PTSD symptoms before surgery and at six weeks and one year. The candidate was broadened with surgery, cancer and generic event/stressor/exposure terms. Probe 2 screened 30 records and found PMIDs 16971821 and 19892213, which describe temporal PTSD symptom improvement and repeated assessments after SARS hospitalization. All six screened relevant discoveries, including these records, were retrieved by the final PTSD AND trajectory query. The remaining category-probe estimate is documented in the evaluation; the probe budget is exhausted."
        }
      ]
    }
  ]
}
```


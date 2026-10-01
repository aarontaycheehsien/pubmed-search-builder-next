# PubMed search strategy: audit

Generated 2026-10-01T12:47:05+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / longitudinal course
- Scope confirmed by user: yes (User asked not to pause for questions; assumed all ages and traumatic event types are in scope. No seed records were supplied. Candidate records were identified through a title-focused PubMed pilot and review references, then screened; 19 eligible development records and 5 held-out records form a pilot-derived benchmark, not an independent gold standard. Symptom-course vocabulary was tested as an AND block and retained after a current 30-record loss sample found no eligible records and the block retrieved all benchmark records. The traumatic-event category was tested but left out of the final Boolean because it loses known eligible treatment-course records and the member-only probe found three eligible studies; two standard-depth probes were used, and the second still found relevant records. The final query returns 11,111 records, above the 10,000 workload budget; tightening the event block would reduce recall. PubMed was queried with PSB_AS_OF=2016-01-24 on every command; no publication-date limit was added.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and post-traumatic stress symptoms | search | Core condition/topic required by every eligible record; include diagnosed PTSD and symptom-level terminology. |
| Symptom trajectories and longitudinal course | optional | Defines the topic, but authors may describe repeated symptom change without trajectory labels; test as an AND block before deciding. |
| Traumatic event or exposure | optional | The question requires a traumatic event, but specific event types vary and may be named without the generic trauma label; test a broad event block to assess retrieval reduction and member-only loss. |
| Longitudinal/repeated-measure design | screen | Eligibility property assessed from abstracts/full text; design labels are inconsistently indexed. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:45:49+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 11,111
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `posttraumatic stress disorder*[tiab]` | 12,654 | none |
| 4 | `post-traumatic stress disorder*[tiab]` | 7,263 | none |
| 5 | `post traumatic stress disorder*[tiab]` | 7,263 | none |
| 6 | `posttraumatic stress symptom*[tiab]` | 1,177 | none |
| 7 | `post-traumatic stress symptom*[tiab]` | 474 | none |
| 8 | `post traumatic stress symptom*[tiab]` | 474 | none |
| 9 | `posttraumatic stress[tiab]` | 14,174 | none |
| 10 | `post-traumatic stress[tiab]` | 8,160 | none |
| 11 | `post traumatic stress[tiab]` | 8,160 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 32,074 | none |
| 13 | `"Time Factors"[Mesh]` | 1,073,830 | none |
| 14 | `"Follow-Up Studies"[Mesh]` | 555,748 | none |
| 15 | `"Disease Progression"[Mesh]` | 138,666 | none |
| 16 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 17 | `trajectory[tiab]` | 24,167 | none |
| 18 | `trajectories[tiab]` | 25,088 | none |
| 19 | `longitudinal[tiab]` | 168,713 | none |
| 20 | `prospective[tiab]` | 409,960 | none |
| 21 | `course[tiab]` | 460,316 | none |
| 22 | `chronicity[tiab]` | 7,037 | none |
| 23 | `remission[tiab]` | 92,395 | none |
| 24 | `recovery[tiab]` | 341,793 | none |
| 25 | `persistence[tiab]` | 68,487 | none |
| 26 | `persistent[tiab]` | 171,965 | none |
| 27 | `change[tiab]` | 811,160 | none |
| 28 | `changes[tiab]` | 1,644,279 | none |
| 29 | `pattern[tiab]` | 565,490 | none |
| 30 | `patterns[tiab]` | 523,313 | none |
| 31 | `time course[tiab]` | 66,728 | none |
| 32 | `follow-up[tiab]` | 703,004 | none |
| 33 | `followup[tiab]` | 670,163 | none |
| 34 | `(follow*[tiab] AND up[tiab])` | 875,440 | none |
| 35 | `repeated measure*[tiab]` | 31,858 | none |
| 36 | `growth curve*[tiab]` | 8,981 | none |
| 37 | `latent class*[tiab]` | 3,150 | none |
| 38 | `latent trajectory*[tiab]` | 88 | none |
| 39 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 5,885,458 | none |
| 40 | `#12 AND #39` | 11,111 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR posttraumatic stress disorder*[tiab] OR post-traumatic stress disorder*[tiab] OR post traumatic stress disorder*[tiab] OR posttraumatic stress symptom*[tiab] OR post-traumatic stress symptom*[tiab] OR post traumatic stress symptom*[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab]) AND ("Time Factors"[Mesh] OR "Follow-Up Studies"[Mesh] OR "Disease Progression"[Mesh] OR "Longitudinal Studies"[Mesh] OR trajectory[tiab] OR trajectories[tiab] OR longitudinal[tiab] OR prospective[tiab] OR course[tiab] OR chronicity[tiab] OR remission[tiab] OR recovery[tiab] OR persistence[tiab] OR persistent[tiab] OR change[tiab] OR changes[tiab] OR pattern[tiab] OR patterns[tiab] OR time course[tiab] OR follow-up[tiab] OR followup[tiab] OR (follow*[tiab] AND up[tiab]) OR repeated measure*[tiab] OR growth curve*[tiab] OR latent class*[tiab] OR latent trajectory*[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 19 | 19 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories and longitudinal course | AND-ed | 32,074 / 11,111 | 65.4% | none | 0/30 (up to 10% of removed records could be relevant) | Refreshed current 30-record loss sample: no records met eligibility. Current query retrieves all 19 development records and all 5 held-out records. The block cuts count substantially, while no known course study is lost; retain the block with the understood risk of terminology-dependent misses. |
| Traumatic event or exposure | left out | 11,111 / 10,038 | 9.7% | 7983220, 23073971, 26764215 | 0/30 (up to 10% of removed records could be relevant) | Refreshed 30-record loss sample screened; no additional records met the repeated PTSD-symptom course criteria. However, the category probe found three eligible member-only studies, and previously established relevant studies include records without an explicit event term (for example treatment-course reports). Event vocabulary misses eligible studies, so do not AND it. The candidate block would remove only about 9.7% of the current results, an insufficient gain to accept known losses. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Traumatic event or exposure | 1 | `Life Change Events[Mesh] OR trauma*[tiab] OR traumatic[tiab] OR disaster*[tiab] OR accident*[tiab] OR injur*[tiab] OR violence[tiab] OR assault*[tiab] OR abuse[tiab] OR war[tiab] OR combat[tiab] OR torture[tiab] OR cancer[tiab] OR surgery[tiab] OR illness[tiab] OR childbirth[tiab]` | 227 | 0/30 |
| Traumatic event or exposure | 2 | `Life Change Events[Mesh] OR trauma*[tiab] OR traumatic[tiab] OR disaster*[tiab] OR accident*[tiab] OR injur*[tiab] OR violence[tiab] OR assault*[tiab] OR abuse[tiab] OR war[tiab] OR combat[tiab] OR torture[tiab] OR cancer[tiab] OR surgery[tiab] OR illness[tiab] OR childbirth[tiab]` | 228 | 3/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 5,885,458 | 0 |
| trajectory | 32,074 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first vocabulary: PTSD descriptor plus symptom/disorder free text; broad longitudinal course terms tested as optional because trajectory is topic-defining but not reliably named. |
| 2 | 0 | ptsd: +11 / -0 | none | Initial recall-first vocabulary: PTSD MeSH descriptor plus PTSD/symptom/disorder text variants; broad course terms are tested as an optional block because trajectory is topic-defining but not reliably named. |
| 3 | 32,074 | limits/combination | none | Initial recall-first vocabulary: PTSD MeSH descriptor plus PTSD/symptom/disorder text variants; broad course terms are tested as an optional block because trajectory is topic-defining but not reliably named. |
| 4 | 10,833 | trajectory: +24 / -0 | none | Promoted the optional trajectory/course block to a required AND block after it retained all 17 known records and the 30-record loss sample contained no eligible study; reduction was material. |
| 5 | 10,994 | trajectory: +1 / -0 | none | Responding to critic finding F1: make traumatic-event context optional and test it against the known sets; add Longitudinal Studies MeSH identified by development-set term mining. Eligibility is unchanged; event type remains screened. |
| 6 | 10,994 | limits/combination | none | Testing traumatic-event wording as an optional category concept in response to critic F1; event type remains a screening criterion. Added Longitudinal Studies MeSH identified in development-set term mining. |
| 7 | 11,019 | trajectory: +1 / -0 | none | Added the field-tagged phrase components follow*[tiab] AND up[tiab] to recover PMID 11102330; proximity translation unexpectedly fell back to All Fields, so the explicit fielded conjunction is tested instead. |
| 8 | 11,111 | trajectory: +1 / -1 | none | Added the field-tagged conjunction follow*[tiab] AND up[tiab] to recover relevant record 11102330 after terms miss showed the phrase was absent; proximity translation was rejected after it fell back to All Fields. |
| 9 | 11,111 | limits/combination | none | Category probe 2 found three relevant member-only event records (cancer diagnosis, deployment, critical illness). Added those event members and related MeSH/text vocabulary to the traumatic-event candidate. Candidate remains unANDed because known losses show it is unsafe as a required block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4 (Fresh-context reviewer followed the supplied packet.): 1 findings; F1 should-fix open
- Round 2 on version 9: 1 findings; F1 should-fix resolved
- Round 3 on version 9: 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1305 NCBI requests logged (748 from cache); strategy sha256 73abb3cc6587._

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
        "message": "11,111 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:traumatic_event",
        "pmids": [
          "17403910",
          "25760659",
          "26557708"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-7682e24dcc706a04245a"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "11,111 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:traumatic_event",
        "pmids": [
          "17403910",
          "25760659",
          "26557708"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-7682e24dcc706a04245a"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:45:49+00:00",
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
      "requested": "Time Factors",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:45:49+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Time Factors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:45:49+00:00",
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
      "checked_at": "2026-10-01T12:45:49+00:00",
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
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:45:49+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"posttraumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract]) AND (\"Time Factors\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"Disease Progression\"[MeSH Terms] OR \"Longitudinal Studies\"[MeSH Terms] OR \"trajectory\"[Title/Abstract] OR \"trajectories\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"prospective\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"chronicity\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"recovery\"[Title/Abstract] OR \"persistence\"[Title/Abstract] OR \"persistent\"[Title/Abstract] OR \"change\"[Title/Abstract] OR \"changes\"[Title/Abstract] OR \"pattern\"[Title/Abstract] OR \"patterns\"[Title/Abstract] OR \"time course\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR (\"follow*\"[Title/Abstract] AND \"up\"[Title/Abstract]) OR \"repeated measure*\"[Title/Abstract] OR \"growth curve*\"[Title/Abstract] OR \"latent class*\"[Title/Abstract] OR \"latent trajectory*\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "623fca62e6fbfa81996e62b47c5f0338c8c85beb531dfd876bd4182a0d7487b9",
      "note": "Fresh-context reviewer followed the supplied packet.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD is the required condition block; trajectory/course was tested and AND-ed after known-set and loss-sample review."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-ed within the two concept blocks and the blocks are AND-ed; no NOT is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "PTSD and course headings are explicit and reported verified in the packet."
        },
        "text_words": {
          "verdict": "pass",
          "note": "PTSD, symptom and course variants are present; no phrase warnings or translation issues were reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The strategy has no syntax diagnostics."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The result count exceeds the standard workload budget and the traumatic-event context has not been tested as optional."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The final strategy exceeds the workload budget by 833 records. The trajectory block was tested, but the packet does not show an optional-block evaluation of the screened traumatic-event concept.",
          "recommendation": "Consider testing a traumatic-event block as an optional concept. AND it only if the enforced known-record rule is met and the evaluation supports it; otherwise leave it out and accept screening above budget.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "This is a provisional disposition pending the recommended test of the traumatic-event context; the final count remains above 10,000.",
          "evidence": "The measured count is 10,833, 833 above the 10,000 standard budget. A trauma-context optional block has not yet been measured."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 9,
      "review_sha256": "6cf4c9fecb74001311b05aa0119d6990ef81eda822cce6b0c3888c95da62d1ad",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block covers both diagnosed PTSD and post-traumatic stress symptoms. The trajectory block was tested against known records and a loss sample before being retained. The traumatic-event block was tested and left out after it lost three known eligible records."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-ed within the PTSD and trajectory blocks, and the blocks are AND-ed. The event block is not applied, avoiding its documented known-record losses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the PTSD and longitudinal-course MeSH headings as verified, and the query includes them."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The PTSD terms include disorder and symptom variants with joined, hyphenated, and spaced forms. The trajectory block includes longitudinal, course, change, follow-up, repeated-measure, growth-curve, and latent-class terminology. No phrase warnings or translation issues are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query has no reported syntax diagnostics or translation issues. Its entry-date bound matches the documented PubMed snapshot date; no publication-date limit was added."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The final count remains 1,111 above the workload budget, but the tested event block would lose three known eligible studies for a 9.7% reduction and was appropriately left out. The trajectory block reduces the count by 65.4%, retains all 24 benchmark records, and had a current 0/30 relevant loss sample. The remaining workload and positive second event-category probe are documented risks."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The final strategy exceeds the workload budget, and the screened traumatic-event concept had not yet been tested as an optional block.",
          "recommendation": "Test the event block as an optional concept; AND it only if the known-record rule is met and the evaluation supports it. Otherwise leave it out and document the remaining workload.",
          "status": "resolved",
          "response": "The event block was tested and left out because it removes three known eligible records for a 9.7% reduction. The remaining 11,111 records are documented as an accepted workload risk."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains applicable, but the optional event-block evaluation found that reducing the count below budget would come at the cost of known eligible records. The count above budget is therefore accepted for screening.",
          "evidence": "The final query returns 11,111 records against a 10,000-record budget. The event block reduces the count by 9.7% but loses PMIDs 7983220, 23073971, and 26764215. The retained trajectory block reduces the count by 65.4%, loses none of the 24 benchmark records, and its refreshed 30-record loss sample found 0 eligible records."
        },
        {
          "issue_id": "I-7682e24dcc706a04245a",
          "status": "accepted-risk",
          "response": "The remaining uncertainty is documented because the latest category probe still found eligible member-only records, and the event block cannot be applied without losing known eligible studies.",
          "evidence": "The second event-category probe found three relevant records among 30 screened, and the event block also loses three known records. The packet documents the two-probe limit and the reason the event block was left out."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 9,
      "review_sha256": "6cf4c9fecb74001311b05aa0119d6990ef81eda822cce6b0c3888c95da62d1ad",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block covers disorder and symptom terminology. The trajectory block was tested and retains all 24 benchmark records. The event block was tested and left out because it loses three known eligible records."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-ed within the PTSD and trajectory blocks, which are AND-ed. The event block is not applied, preserving records it would exclude."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the PTSD and longitudinal-course MeSH headings as verified and includes them in the query."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes PTSD and symptom variants, plus longitudinal, course, change, follow-up, repeated-measure, growth-curve, and latent-class terms. No phrase warnings or translation issues are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax diagnostics. The documented PubMed snapshot date is recorded, with no publication-date limit added."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 11,111-record count exceeds the 10,000 budget, but the tested event block loses three known eligible records for only a 9.7% reduction. The remaining workload and uncertainty from the positive second category probe are documented risks; screening is a legitimate outcome."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The final strategy exceeded the workload budget, and the screened traumatic-event concept had not yet been tested as an optional block.",
          "recommendation": "Test the event block as an optional concept; apply it only if the known-record rule is met and the evaluation supports it. Otherwise leave it out and document the remaining workload.",
          "status": "resolved",
          "response": "The event block was tested and left out because it removes three known eligible records for a 9.7% reduction. The remaining 11,111 records are documented as an accepted workload risk."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains applicable, but testing the optional event block showed that reducing the count would lose known eligible studies. The over-budget count is accepted for screening.",
          "evidence": "The strategy returns 11,111 records against a 10,000-record budget. The event block reduces the count by 9.7% but loses PMIDs 7983220, 23073971, and 26764215. The retained trajectory block reduces the count by 65.4%, loses none of the 24 benchmark records, and its refreshed 30-record loss sample found no eligible records."
        },
        {
          "issue_id": "I-7682e24dcc706a04245a",
          "status": "accepted-risk",
          "response": "The uncertainty is documented because the latest category probe found eligible member-only records. The event block is left out because it loses known eligible studies, so the remaining records can be screened.",
          "evidence": "The second event-category probe found three eligible records among 30 screened, and the event block loses three known records. The packet documents the two-probe limit and why the block was left out."
        }
      ]
    }
  ]
}
```


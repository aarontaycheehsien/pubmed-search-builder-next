# PubMed search strategy: audit

Generated 2026-09-30T15:12:24+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / longitudinal course
- Scope confirmed by user: no (User asked us not to pause for questions; scope was not user-confirmed. Assumptions: the target is PTSD/post-traumatic stress symptoms after a traumatic event; any population and event type are eligible, including serious medical events that may be experienced as traumatic; exclude acute-stress-only and nonlongitudinal reports. Trauma type is not required as a block because a broad exposure candidate removes known relevant records whose trauma is described as critical illness, deployment, or burns. Standard-depth PubMed discovery screened candidates from a broad disaster psychopathology review and longitudinal-course pilots; 21 records were screened into the relevant development set. The trajectory/course block was tested as optional and AND-ed after all 21 were retrieved, it reduced the base count by 67.8%, and no clearly relevant records appeared in a fresh 30-record loss sample; one loss-sample record lacked an abstract and remains uncertain. A trauma-exposure block was also tested: it cut the current query by 5.9% but lost 3/21 known records, so it was left out. No independent validation set or user-supplied seeds exist. Counts use the harness-required PSB_AS_OF=2016-01-24 Entrez-entry bound in protocol.as_of; no publication-date limit was added. Explicit workload decision: accept the remaining 603-record overrun (10,603 versus the default 10,000 budget) for this high-sensitivity draft, because the tested event block reduced results by only 5.9% and excluded three of 21 screened relevant records. Keep the broader query and send it for information-specialist PRESS peer review before use.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and post-traumatic stress symptoms | search | The topic is symptom course in PTSD; records should name PTSD or post-traumatic stress, but trauma event exposure is inherent and can be screened rather than separately required. |
| Symptom trajectories and longitudinal course | optional | This defines the review topic and is often named, but labels vary and authors may report trajectory analyses without these terms; test as an AND block before deciding. |
| Traumatic event exposure | optional | Traumatic-event exposure is searchable but event labels are not reliably stated in every PTSD record; because the query remains over the workload budget, test a broad event block and measure known-record loss before deciding. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T15:11:35+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 10,603
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 4 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 5 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 6 | `"posttraumatic stress disorder"[tiab]` | 12,500 | none |
| 7 | `"post-traumatic stress disorder"[tiab]` | 7,081 | none |
| 8 | `"post traumatic stress disorder"[tiab]` | 7,081 | none |
| 9 | `"posttraumatic stress symptom"[tiab]` | 89 | none |
| 10 | `"post-traumatic stress symptom"[tiab]` | 27 | none |
| 11 | `"post traumatic stress symptom"[tiab]` | 27 | none |
| 12 | `"Combat Disorders"[Mesh]` | 2,832 | none |
| 13 | `"posttraumatic stress symptoms"[tiab]` | 1,060 | none |
| 14 | `"post-traumatic stress symptoms"[tiab]` | 429 | none |
| 15 | `"post traumatic stress symptoms"[tiab]` | 429 | none |
| 16 | `"post-traumatic neurosis"[tiab]` | 22 | none |
| 17 | `"posttraumatic neurosis"[tiab]` | 7 | none |
| 18 | `"traumatic neurosis"[tiab]` | 138 | none |
| 19 | `"shell shock"[tiab]` | 110 | none |
| 20 | `"combat stress disorder"[tiab]` | 3 | none |
| 21 | `"war neurosis"[tiab]` | 48 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 32,935 | none |
| 23 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 24 | `"Follow-Up Studies"[Mesh]` | 555,748 | none |
| 25 | `"Time Factors"[Mesh]` | 1,073,830 | none |
| 26 | `"Disease Progression"[Mesh]` | 138,666 | none |
| 27 | `trajectory*[tiab]` | 24,169 | none |
| 28 | `longitudin*[tiab]` | 180,668 | none |
| 29 | `course[tiab]` | 460,316 | none |
| 30 | `"follow-up"[tiab]` | 703,004 | none |
| 31 | `followup[tiab]` | 670,163 | none |
| 32 | `prospective[tiab]` | 409,960 | none |
| 33 | `chang*[tiab]` | 2,432,060 | none |
| 34 | `persist*[tiab]` | 367,137 | none |
| 35 | `remission[tiab]` | 92,395 | none |
| 36 | `recovery[tiab]` | 341,793 | none |
| 37 | `growth[tiab]` | 1,123,993 | none |
| 38 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 6,151,911 | none |
| 39 | `#22 AND #38` | 10,603 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "posttraumatic stress disorder"[tiab] OR "post-traumatic stress disorder"[tiab] OR "post traumatic stress disorder"[tiab] OR "posttraumatic stress symptom"[tiab] OR "post-traumatic stress symptom"[tiab] OR "post traumatic stress symptom"[tiab] OR "Combat Disorders"[Mesh] OR "posttraumatic stress symptoms"[tiab] OR "post-traumatic stress symptoms"[tiab] OR "post traumatic stress symptoms"[tiab] OR "post-traumatic neurosis"[tiab] OR "posttraumatic neurosis"[tiab] OR "traumatic neurosis"[tiab] OR "shell shock"[tiab] OR "combat stress disorder"[tiab] OR "war neurosis"[tiab]) AND ("Longitudinal Studies"[Mesh] OR "Follow-Up Studies"[Mesh] OR "Time Factors"[Mesh] OR "Disease Progression"[Mesh] OR trajectory*[tiab] OR longitudin*[tiab] OR course[tiab] OR "follow-up"[tiab] OR followup[tiab] OR prospective[tiab] OR chang*[tiab] OR persist*[tiab] OR remission[tiab] OR recovery[tiab] OR growth[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 21 | 21 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories and longitudinal course | AND-ed | 32,935 / 10,603 | 67.8% | none | 0/30 (up to 10% of removed records could be relevant) | After further standard-depth discovery, 21 screened in-scope records are in the base and the current block loses none. It reduces the PTSD set from 32,935 to 10,603 records (67.8%), exceeding the approximate 30% materiality threshold. The refreshed 30-record loss sample contained no clearly eligible record: the closest symptom papers were single-assessment studies; one 1988 PTSD paper lacked an abstract and remains uncertain. AND the block under the scope.md rule, while recording residual risk that eligible studies lacking both trajectory/course labels and longitudinal/follow-up indexing could be missed. |
| Traumatic event exposure | left out | 10,603 / 9,980 | 5.9% | 12055495, 20146258, 25300755 | 3/30 | Leave this exposure block out. It would reduce 10,603 to 9,980 records (5.9%, below the approximate 30% materiality threshold) and removes three of 21 screened relevant records: PTSD symptom follow-up after pediatric critical illness/PICU (12055495), postdeployment soldiers (20146258), and burn-injury treatment (25300755). These event types are not reliably described using a single generic trauma vocabulary, so the block would cost recall for a small reduction. The 30-record loss sample was screened; none of the other records clearly met the repeated PTSD symptom-course eligibility criteria. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 6,151,911 | 0 |
| trajectory | 32,935 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,074 | initial | none | Initial PTSD concept block with MeSH and title/abstract variants; trajectory/course constructed as optional concept for loss testing. |
| 2 | 32,935 | ptsd: +10 / -0 | none | Expanded PTSD vocabulary with symptom plurals and historically indexed combat/post-traumatic neurosis variants; screened 10 additional pilot records into relevant set. Kept trajectory block optional pending refreshed loss-sample decision. |
| 3 | 10,603 | trajectory: +15 / -0 | none | Moved the tested longitudinal-course block into the query: 18 known relevant development records are retained, no current known misses, and 30-record loss sample had no clearly eligible record; decision meets all optional-concept admission criteria. |
| 4 | 10,603 | limits/combination | none | Updated as_of to the required 2016-01-24 Entrez-entry cutoff, and tested screened traumatic-event exposure as optional after critic finding; no publication-date limit added. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; F1 must-fix open, F2 should-fix open
- Round 2 on version 4: 2 findings; F1 must-fix resolved, F2 should-fix open
- Round 3 on version 4: 2 findings; F1 must-fix resolved, F2 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1108 NCBI requests logged (570 from cache); strategy sha256 d658dd50918a._

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
        "message": "10,603 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "10,603 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T15:11:35+00:00",
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
      "requested": "Combat Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:11:35+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003130",
          "name": "Combat Disorders",
          "type": "descriptor",
          "scope_note": "Neurotic reactions to unusual, severe, or overwhelming military stress.",
          "tree_numbers": [
            "F03.950.750.249"
          ],
          "entry_terms": 21,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003130",
      "preferred_label": "Combat Disorders",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Combat Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:11:35+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:11:35+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Follow-Up Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Time Factors",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:11:35+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Time Factors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Disease Progression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:11:35+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Disease Progression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress symptom\"[Title/Abstract] OR \"post-traumatic stress symptom\"[Title/Abstract] OR \"post-traumatic stress symptom\"[Title/Abstract] OR \"Combat Disorders\"[MeSH Terms] OR \"posttraumatic stress symptoms\"[Title/Abstract] OR \"post-traumatic stress symptoms\"[Title/Abstract] OR \"post-traumatic stress symptoms\"[Title/Abstract] OR \"post-traumatic neurosis\"[Title/Abstract] OR \"posttraumatic neurosis\"[Title/Abstract] OR \"traumatic neurosis\"[Title/Abstract] OR \"shell shock\"[Title/Abstract] OR \"combat stress disorder\"[Title/Abstract] OR \"war neurosis\"[Title/Abstract]) AND (\"Longitudinal Studies\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"Time Factors\"[MeSH Terms] OR \"Disease Progression\"[MeSH Terms] OR \"trajectory*\"[Title/Abstract] OR \"longitudin*\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"prospective\"[Title/Abstract] OR \"chang*\"[Title/Abstract] OR \"persist*\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"recovery\"[Title/Abstract] OR \"growth\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "f05b119aef7bad2989e662a4cc0ea1b32d05723d3f8949294d62412e0e92501b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block includes bare PTSD and post-traumatic stress wording, and trauma exposure is explicitly assigned to screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD and longitudinal-course blocks are OR-combined internally and AND-combined consistently with the tested optional-block decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD and longitudinal-course blocks use relevant verified MeSH descriptors; the historical Combat Disorders heading is supplemental."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The free-text terms cover PTSD, spelling and hyphenation variants, and multiple longitudinal-course labels. The retained truncations are not proximity expressions."
        },
        "syntax": {
          "verdict": "revise",
          "note": "The current query includes the harness-required Entrez-entry cutoff at 2016-01-24; record it as protocol.as_of, do not remove it."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The count slightly exceeds the workload budget; evaluate traumatic event exposure as an optional block and justify any leave-out."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez-entry date range ending 2016-01-24. The scope has no date restriction, and the run is dated 2026-09-30, so the final strategy would omit subsequently entered records.",
          "recommendation": "Remove the entry-date bound from the deliverable query, or state and justify a date cutoff in the review scope. Re-evaluate the complete query and report the resulting count.",
          "status": "open",
          "response": ""
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The final result count is 10,603, above the 10,000-record workload budget. The validation warning asks reviewers to confirm that searchable concepts assigned to screening were considered as optional blocks, but only the trajectory concept was tested. Traumatic event exposure is assigned to screening.",
          "recommendation": "Document whether traumatic-event exposure is a searchable optional concept and, if so, test it as an additional block with an appropriate loss assessment. Then record whether the remaining 603-record excess is accepted or revise the strategy and re-evaluate it.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The current candidate exceeds the stated budget by 603 records; the packet does not establish that this excess is acceptable or show a completed assessment of the screened trauma-exposure concept as an optional block.",
          "evidence": "The final count is 10,603 against a 10,000-record budget. The tested optional concept is trajectory/course; trauma exposure is designated screen in the scope."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "91770fedeea0fca29c6268a0997aed750cf096fe233cb736d879d62526841097",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block includes bare PTSD, post-traumatic stress wording, symptom variants, and historical labels. Trauma exposure is separately tested and left out with a documented known-record loss assessment."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within the PTSD and course blocks; the blocks are AND-combined in line with the tested trajectory decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses relevant verified PTSD and longitudinal-course MeSH headings. Combat Disorders is supplemental."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover PTSD wording variants and multiple course labels. Truncations are ordinary fielded PubMed terms, not proximity expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query parses without diagnostics. The required Entrez-entry cutoff is recorded as protocol.as_of, with no publication-date limit added."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The optional trauma block is now tested and appropriately left out because it removes three known relevant records for a 5.9% reduction. The final count remains 10,603, above the 10,000-record workload budget; acceptance of the remaining excess should be made explicit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entrez-entry cutoff at 2016-01-24 although the scope has no review date restriction.",
          "recommendation": "Record the required cutoff as protocol.as_of and clarify that it is an entry-date snapshot, not a publication-date limit.",
          "status": "resolved",
          "response": "The current protocol records as_of as 2016-01-24 and states that counts use the harness-required Entrez-entry bound; it also states that no publication-date limit was added."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The final count remains 10,603, exceeding the stated 10,000-record workload budget by 603. The trauma-exposure block has now been tested, but the packet does not explicitly say whether the remaining excess is accepted.",
          "recommendation": "Record whether the 603-record excess is accepted given that the tested trauma block would remove three known relevant records for only a 5.9% reduction, or revise and fully re-evaluate the strategy.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The trauma-exposure block was tested and left out because it removes three known relevant records while reducing the set by only 5.9%. The remaining 603-record excess is a documented tradeoff, though the protocol should state explicit acceptance.",
          "evidence": "The current count is 10,603 against a 10,000-record budget. The optional trauma block reduces it to 9,980 but loses three of 21 screened relevant records; the strategy notes record those losses and the reason for leaving the block out."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "c318977fca08c15ab6b3036e4996740f1dab41ccb2e850f8a4d68ce9094df851",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PTSD block covers PTSD and post-traumatic stress wording; trauma exposure was separately tested and left out with known-record losses documented."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within the PTSD and course blocks, and those blocks are AND-combined consistently with the tested trajectory decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant verified PTSD and longitudinal-course MeSH headings; Combat Disorders is supplemental."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover PTSD wording variants and multiple course labels. The truncations are ordinary fielded terms, not proximity expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query parses without diagnostics. The required Entrez-entry cutoff is recorded as protocol.as_of, with no publication-date limit added."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The event block was measured and left out because it loses three known relevant records for only a 5.9% reduction. The protocol explicitly accepts the remaining 603-record overrun to protect recall."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entrez-entry cutoff at 2016-01-24 although the scope has no review date restriction.",
          "recommendation": "Record the required cutoff as protocol.as_of and clarify that it is an entry-date snapshot, not a publication-date limit.",
          "status": "resolved",
          "response": "protocol.json records as_of=2016-01-24 and states that this is the harness-required Entrez-entry bound; no publication-date limit was added."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The final count remains 10,603, exceeding the stated 10,000-record workload budget by 603. The trauma-exposure block has now been tested, but the packet does not explicitly say whether the remaining excess is accepted.",
          "recommendation": "Explicitly record whether the 603-record excess is accepted given that the tested trauma block would remove three known relevant records for only a 5.9% reduction, or revise and fully re-evaluate the strategy.",
          "status": "accepted-risk",
          "response": "The current protocol notes explicitly accept the 603-record overrun for this high-sensitivity draft because the tested event block cut the set by only 5.9% while losing three of 21 known relevant records. I retain the broader query to preserve those records and document the workload tradeoff for the human reviewer."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 10,603-record query exceeds the standard 10,000 budget by 603. The trauma-exposure candidate was tested, reduced the set to 9,980 (5.9%), and lost three known relevant records, so the broader query is retained to protect recall. This modest overrun is explicitly accepted in protocol.notes and remains a screening workload consideration.",
          "evidence": "Current evaluation: 10,603 results, 21 relevant development records retrieved (100% relative recall), zero known misses; optional trauma candidate: 9,980 results and known losses 12055495, 20146258, and 25300755; optional decision leave_out. The candidate's 30-record loss sample contained those three relevant records."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-30T16:48:52+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / longitudinal symptom course
- Scope confirmed by user: no (Standard depth. No known relevant articles supplied; user cannot answer questions during this run and asked us to proceed without waiting. Scope roles and eligibility are working assumptions, not user-confirmed. No age, language, geography, or publication-date limit. PubMed retrieval is bounded by Entrez date through 2016-01-24 via PSB_AS_OF; do not apply a publication-date limit. A matching natural-history systematic review and screened similar-article/pilot records were used for discovery. An initial exploratory term ranking ran on the first 17 development records before the 30% split; it suggested no final query terms beyond the MeSH lookup and general vocabulary. The six-record validation set should therefore be treated as semi-independent and not as a clean external validation set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder or symptoms | search | The condition and symptom domain define the review and are reliably named or indexed. |
| Symptom trajectories, course, or longitudinal change | optional | This is topic-defining and often named, but requiring explicit trajectory or longitudinal terminology may miss eligible cohorts. Test as an optional AND block. |
| Traumatic event exposure | screen | Traumatic events are implicit in PTSD, but event context varies and an extra block risks recall loss. Confirm at screening. |
| Population and age group | screen | No age or population restriction was specified; include all populations and screen against eligibility. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T16:48:26+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,459
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Stress Disorders, Post-Traumatic[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `posttraumatic stress[tiab]` | 14,174 | none |
| 4 | `post-traumatic stress[tiab]` | 8,160 | none |
| 5 | `post traumatic stress[tiab]` | 8,160 | none |
| 6 | `posttraumatic stress disorder[tiab]` | 12,500 | none |
| 7 | `post-traumatic stress disorder[tiab]` | 7,081 | none |
| 8 | `post traumatic stress disorder[tiab]` | 7,081 | none |
| 9 | `posttraumatic stress symptoms[tiab]` | 1,060 | none |
| 10 | `post-traumatic stress symptoms[tiab]` | 429 | none |
| 11 | `post traumatic stress symptoms[tiab]` | 429 | none |
| 12 | `stress disorder*[tiab]` | 20,149 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 32,459 | none |

### Strategy (single line, for copying into PubMed)

```text
((Stress Disorders, Post-Traumatic[Mesh] OR PTSD[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab] OR posttraumatic stress disorder[tiab] OR post-traumatic stress disorder[tiab] OR post traumatic stress disorder[tiab] OR posttraumatic stress symptoms[tiab] OR post-traumatic stress symptoms[tiab] OR post traumatic stress symptoms[tiab] OR stress disorder*[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 15 | 15 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories, course, or longitudinal change | left out | 32,459 / 10,844 | 66.6% | 20889815 | 1/30 | Leave out despite the 66.6% reduction: the current candidate loses eligible development record PMID 20889815, and the latest 30-record sample itself contained this repeated-measures PTSD deployment study. Earlier candidate versions also exposed eligible records labeled without explicit trajectory/course terms. The measured loss risk outweighs the workload reduction in a high-sensitivity search. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,459 | initial | none | Initial PTSD block and optional course/trajectory block; terms include MeSH plus title/abstract labels informed by MeSH entry terms and screened longitudinal records. |
| 2 | 32,459 | limits/combination | none | Added chronic[tiab] to the optional trajectory block after loss-sample screening identified PMID 8543717 (repeated symptom measures but no existing course-label term); added that eligible sampled record to development. |
| 3 | 32,459 | limits/combination | none | Added repeated[tiab] and time point(s)[tiab] after optional loss-sample screening found two eligible records with repeated PTSD symptom assessments but no other selected course labels; added both to development. |
| 4 | 32,459 | limits/combination | none | Changed repeated[tiab] to repeat*[tiab] after PMID 11151488's eligible abstract used 'repeatedly recorded'; retains both repeated and repeatedly in the optional course block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 0 findings; 
- Round 2 on version 4: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 376 NCBI requests logged (119 from cache); strategy sha256 17c65eaef535._

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
        "message": "32,459 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "32,459 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-30T16:48:26+00:00",
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
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress symptoms\"[Title/Abstract] OR \"post traumatic stress symptoms\"[Title/Abstract] OR \"post traumatic stress symptoms\"[Title/Abstract] OR \"stress disorder*\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "87253d145cd299b8507833c74b3206fc6831f4909c679b6f10ad9a5981c2a876",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched PTSD concept is represented by its MeSH heading, acronym, and posttraumatic stress and symptom wording variants. Trajectory and longitudinal terms were tested as an optional block and left out based on observed eligible-record losses."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD terms are OR-combined in one searched concept block. No required concept or unjustified AND restriction is omitted from the final query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Stress Disorders, Post-Traumatic[Mesh] is verified as a descriptor and is appropriate for the searched condition."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes PTSD and common joined, hyphenated, and spaced forms of posttraumatic stress, including symptom wording. The broad stress disorder truncation is retained within the PTSD concept block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors or translation issues. The multiword terms translate as phrases, and no proximity syntax is used."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or population limit is applied. The Entrez date boundary through 2016-01-24 is explicitly documented as the run's as-of snapshot."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning was reviewed. The trajectory block reduced results by 66.6%, but it removed an eligible development record and the 30-record loss sample also contained that eligible study. Leaving the block out is justified for this high-sensitivity search.",
          "evidence": "The packet reports 32,459 results against a 10,000-record budget; the optional block produced 10,844 results but lost PMID 20889815, and 1 of 30 sampled removed records was relevant."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "87253d145cd299b8507833c74b3206fc6831f4909c679b6f10ad9a5981c2a876",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Round 1 found no translation issues. It recorded coverage of the PTSD descriptor, acronym, and wording variants, and documented why the optional trajectory block was left out."
        },
        "operators": {
          "verdict": "pass",
          "note": "Round 1 found no operator issues. The final strategy OR-combines the PTSD terms in one searched concept block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Round 1 found no subject-heading issues and verified the PTSD descriptor as appropriate."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Round 1 found no text-word issues, noting the acronym, joined, hyphenated, and spaced forms, plus the retained stress-disorder truncation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Round 1 found no syntax issues. The packet reports no PubMed errors, translation issues, or proximity syntax."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Round 1 found no limits or filter issues. No publication-date or population limit is applied; the Entrez date boundary is documented as the run's snapshot."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Round 1 reviewed and accepted the workload warning because the optional trajectory block removed an eligible development record and a relevant record appeared in the loss sample. Leaving the block out is justified for this high-sensitivity search.",
          "evidence": "The packet reports 32,459 results against a 10,000-record budget. The optional block reduced results to 10,844 but lost PMID 20889815; 1 of 30 sampled removed records was relevant."
        }
      ]
    }
  ]
}
```


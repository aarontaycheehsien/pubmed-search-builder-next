# PubMed search strategy: audit

Generated 2026-09-30T14:47:08+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: topic-focused review
- Scope confirmed by user: no (User requested proceeding without questions; scope is an explicit operational interpretation. No known relevant articles were supplied. Assume all ages, settings, languages, and publication types are eligible; no limits are applied. PubMed data are bounded by PSB_AS_OF=2018-11-17 (Entrez date), not publication date. Depression is the required condition block; relapse/recurrence and psychological theory are topic-defining but potentially inconsistently named and will be tested as optional concepts.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The review concerns depressive relapse and recurrence, so depression is essential and reliably searchable; the category probe will check whether records name a specific depressive disorder instead of depression generally. |
| Relapse or recurrence of depression | optional | This defines the topic and often has searchable language, but may be reported as course, maintenance, continuation, or longitudinal theory; test as an optional block before deciding. |
| Psychological theories or models | optional | Theoretical framing defines eligibility, but articles may discuss mechanisms without labeling themselves as theory; test this searchable but imperfectly named concept rather than requiring it without evidence. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:46:46+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 439,310
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Depressive Disorder[Mesh]` | 105,341 | none |
| 2 | `depress*[tiab]` | 419,763 | none |
| 3 | `major depress*[tiab]` | 42,948 | none |
| 4 | `unipolar depress*[tiab]` | 3,241 | none |
| 5 | `melanchol*[tiab]` | 2,939 | none |
| 6 | `dysthymi*[tiab]` | 3,055 | none |
| 7 | `persistent depressive disorder[tiab]` | 52 | none |
| 8 | `Depression, Postpartum[Mesh]` | 5,164 | none |
| 9 | `Seasonal Affective Disorder[Mesh]` | 1,198 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 439,310 | none |

### Strategy (single line, for copying into PubMed)

```text
((Depressive Disorder[Mesh] OR depress*[tiab] OR major depress*[tiab] OR unipolar depress*[tiab] OR melanchol*[tiab] OR dysthymi*[tiab] OR persistent depressive disorder[tiab] OR Depression, Postpartum[Mesh] OR Seasonal Affective Disorder[Mesh])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Relapse or recurrence of depression | left out | 439,310 / 24,549 | 94.4% | none | 0/30 (up to 10% of removed records could be relevant) | Only one known relevant record is available, below the minimum of 15 needed to justify AND-ing; the loss sample was screened and contained no eligible record, but that sample cannot establish safety given the tiny known set. Keep this topic-defining concept out of the required query for recall-first retrieval. |
| Psychological theories or models | left out | 439,310 / 176,196 | 59.9% | none | 0/30 (up to 10% of removed records could be relevant) | Only one known relevant record is available, below the minimum of 15 needed to justify AND-ing; the loss sample was screened and contained no eligible record, but that sample cannot establish safety given the tiny known set. Theoretical framing may be implicit, so do not require theory/model wording. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `(Mood Disorders[Mesh] OR Affective Disorders[Mesh] OR mood disorder*[tiab] OR affective disorder*[tiab])` | 36,713 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 439,310 | initial | none | Initial broad depressive-disorder block; relapse/recurrence and theory are measured as optional because both define scope but may be inconsistently named. Added one screened relevant review from a PubMed systematic-review pilot; other discovered review was excluded because it addressed operational definitions, not psychological theories. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1 (Same-context critic; no fresh-context reviewer process is available. Reviewed the packet against all six PRESS domains and the required evidence-bound diagnostics.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 549 NCBI requests logged (221 from cache); strategy sha256 ee403e95bd61._

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
        "message": "439,310 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:relapse_recurrence",
        "blocking": false,
        "requires_review": true,
        "id": "I-4f0db97e7ec07d4d2739"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:psychological_theory",
        "blocking": false,
        "requires_review": true,
        "id": "I-9d09dffc8c668f03cda6"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "439,310 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:relapse_recurrence",
        "blocking": false,
        "requires_review": true,
        "id": "I-4f0db97e7ec07d4d2739"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:psychological_theory",
        "blocking": false,
        "requires_review": true,
        "id": "I-9d09dffc8c668f03cda6"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:46:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003866",
          "name": "Depressive Disorder",
          "type": "descriptor",
          "scope_note": "An affective disorder manifested by either a dysphoric mood or loss of interest or pleasure in usual activities. The mood disturbance is prominent and relatively persistent.",
          "tree_numbers": [
            "F03.600.300"
          ],
          "entry_terms": 20,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003866",
      "preferred_label": "Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Depressive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression, Postpartum",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:46:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019052",
          "name": "Depression, Postpartum",
          "type": "descriptor",
          "scope_note": "Depression in POSTPARTUM WOMEN, usually within four weeks after giving birth (PARTURITION). The degree of depression ranges from mild transient depression to neurotic or psychotic depressive disorders. (From DSM-IV, p386)",
          "tree_numbers": [
            "C12.050.703.844.253",
            "F03.600.300.350"
          ],
          "entry_terms": 19,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019052",
      "preferred_label": "Depression, Postpartum",
      "type": "descriptor",
      "location": "vocabulary:8",
      "term": {
        "text": "Depression, Postpartum",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Seasonal Affective Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:46:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016574",
          "name": "Seasonal Affective Disorder",
          "type": "descriptor",
          "scope_note": "A syndrome characterized by depressions that recur annually at the same time each year, usually during the winter months. Other symptoms include anxiety, irritability, decreased energy, increased appetite (carbohydrate cravings), increased duration of sleep, and weight gain. SAD (seasonal affective disorder) can be treated by daily exposure to bright artificial lights (PHOTOTHERAPY), during the...",
          "tree_numbers": [
            "F03.600.300.775"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016574",
      "preferred_label": "Seasonal Affective Disorder",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "Seasonal Affective Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"depressive disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"major depress*\"[Title/Abstract] OR \"unipolar depress*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"persistent depressive disorder\"[Title/Abstract] OR \"depression, postpartum\"[MeSH Terms] OR \"seasonal affective disorder\"[MeSH Terms]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "67688ffb0342273b32a0925cffe5c992357f6ca1c9383938525945dd522a7360",
      "note": "Same-context critic; no fresh-context reviewer process is available. Reviewed the packet against all six PRESS domains and the required evidence-bound diagnostics.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required block is the depressive-disorder condition. Both topic-defining dimensions (relapse/recurrence and psychological theory) were tested as optional and left out because the evidence base had only one known relevant record; requiring either would be underpowered. Eligibility remains for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The active strategy uses a single OR block without unnecessary ANDs or NOT logic; optional tests use AND only for assessment."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder is verified and exploded, covering narrower headings such as major depressive disorder, dysthymic disorder, postpartum depression, and seasonal affective disorder. Free-text depression terms supplement unindexed records."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Depress* plus major/unipolar depression, melancholia, dysthymia, and persistent depressive disorder cover core naming variants. No known-record miss was observed. The optional blocks include broader process and theory vocabulary for possible later narrowing after human review."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All active terms are explicitly field-tagged, truncation stems meet minimum length, and the current evaluation reports no lint or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, date-of-publication, age, or study-design limits are used. PubMed is bounded by Entrez date at 2018-11-17 as requested."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The required depression-only block is intentionally broad because the two topic-specific optional blocks cannot be safely required with only one known relevant record. A high screening burden is the cost of preserving recall under this uncertainty; use the optional variants only after protocol team review or additional benchmark records.",
          "evidence": "Current PubMed count is 439,310 at Entrez date 2018-11-17, versus 24,549 with the relapse/recurrence block and 176,196 with the theory/model block. Both optional loss samples were screened (30 each, 0 relevant), but known_in_base is only 1, below the 15-record threshold."
        },
        {
          "issue_id": "I-4f0db97e7ec07d4d2739",
          "status": "accepted-risk",
          "response": "Additional known-record discovery was attempted through PubMed systematic-review queries, screening a discovered review, and inspecting references from two related reviews. Only one record met the stated scope; the user supplied no seeds and asked us to proceed without questions. The block remains out of the final query until a larger known set can support a safe decision.",
          "evidence": "PubMed pilot counts were 63 for depression plus relapse/recurrence plus theory plus systematic[sb] and 317 for depression plus relapse/recurrence plus systematic[sb]. PMID 30075313 was screened into the relevant set; PMID 29769159 was excluded as a definitions review. Reference-neighbour lists were inspected. The optional block would reduce 439,310 to 24,549; no known record would be lost, but only one known record is available."
        },
        {
          "issue_id": "I-9d09dffc8c668f03cda6",
          "status": "accepted-risk",
          "response": "Additional known-record discovery was attempted as above. Only one relevant record was identified, so the theory/model block is not AND-ed; theoretical mechanisms may be discussed without these labels. Human screening should establish the actual yield and any useful focused variant.",
          "evidence": "The theory/model block reduces 439,310 to 176,196 and would retain the only known relevant record, but the known_in_base is 1 and the 30-record loss sample found no eligible record. Pilot systematic-review searches and references did not supply 15 known relevant records."
        }
      ]
    }
  ]
}
```


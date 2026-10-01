# PubMed search strategy: audit

Generated 2026-10-01T12:07:10+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: Condition plus topic-defining process and explanatory focus
- Scope confirmed by user: yes (User asked to proceed without questions. Assumed the review concerns psychological explanations/models/mechanisms of depressive relapse or recurrence, not relapse-prevention treatment effectiveness alone. Depression is the required concept; relapse/recurrence and theory/model focus are optional because labeling may be unreliable and their contribution must be tested. No user seeds; found a matching 2018 systematic review in PubMed and screened its citation candidates plus two precise PubMed pilots. Nineteen records were added to the development relevant set after abstract screening; there is no independent validation set. Screened optional-loss and category probes. Default 10,000-record workload budget is exceeded; both searchable topic-defining optional blocks were evaluated and left out to preserve recall, with evidence and loss samples recorded. Internal critic will be same-context because no fresh context is available. No external web search used. PubMed records are bounded by Entrez date through PSB_AS_OF=2018-11-17; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The condition is central to the question; relevant records may use depression or named depressive-disorder terms. |
| Relapse or recurrence of depression | optional | Defines the topic, but abstracts may describe longitudinal course without using relapse/recurrence labels; test the block before deciding. |
| Psychological theories, models, or mechanisms | optional | Defines the explanatory focus, but relevant papers may discuss cognitive or psychological mechanisms without naming a theory; test it before deciding. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:06:51+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 460,729
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 | none |
| 3 | `"Depression"[Mesh]` | 112,392 | none |
| 4 | `depress*[tiab]` | 419,763 | none |
| 5 | `dysthym*[tiab]` | 3,056 | none |
| 6 | `melanchol*[tiab]` | 2,939 | none |
| 7 | `"unipolar depression"[tiab]` | 2,526 | none |
| 8 | `"unipolar depressive"[tiab]` | 419 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 460,729 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Depression"[Mesh] OR depress*[tiab] OR dysthym*[tiab] OR melanchol*[tiab] OR "unipolar depression"[tiab] OR "unipolar depressive"[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 19 | 19 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Relapse or recurrence of depression | left out | 460,729 / 16,633 | 96.4% | 21976044 | 0/30 (up to 10% of removed records could be relevant) | The refreshed 30-record loss sample found no in-scope record. This block would reduce the count by 96.4%, but one of 19 known relevant records (PMID 21976044) has no relapse/recurrence term in its indexed record; an AND would sacrifice recall. Leave out. |
| Psychological theories, models, or mechanisms | left out | 460,729 / 10,198 | 97.8% | 20132925, 21171724, 21211635, 21895384, 21976044, 22420036, 24364598, 26017336, 26047613, 26052359, 30075313 | 0/30 (up to 10% of removed records could be relevant) | The refreshed 30-record loss sample found no eligible in-scope record. The theory/model block would reduce the base by 97.8% but exclude 11 of 19 known relevant records, including psychological mechanism and recurrence theory records that do not use these labels. Keep the block out to protect recall; screen explanatory focus. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `Mood Disorders[Mesh]` | 28,606 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 439,310 | initial | none | Initial broad depression block with tested optional blocks for relapse/recurrence and psychological theory. Added nine screened relevant records from a matching 2018 systematic review citation set; no user seeds. |
| 2 | 460,729 | depression: +1 / -0 | none | Added Depression[Mesh] to capture records indexed with the legacy/symptom depression descriptor; its live translation includes both depressive disorder and depression MeSH terms. Optional decisions must be rechecked against the widened condition block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (same-context critic; reviewed the supplied packet myself because no fresh context was available.): 0 findings; 
- Round 2 on version 2 (same-context critic; second review of the unchanged strategy after correcting protocol notes and checking report --diagnostic.): 0 findings; 
- Round 3 on version 2 (same-context closing review; all findings and the workload disposition from the two revision rounds were checked against the unchanged strategy and current evidence.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1128 NCBI requests logged (442 from cache); strategy sha256 5b93110af401._

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
        "message": "460,729 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "460,729 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:06:51+00:00",
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
        "text": "\"Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Major Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:06:51+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003865",
          "name": "Major Depressive Disorder",
          "type": "descriptor",
          "scope_note": "Disorder in which five (or more) of the following symptoms have been present during the same 2-week period and represent a change from previous functioning; at least one of the symptoms is either (1) depressed mood or (2) loss of interest or pleasure. Symptoms include: depressed mood most of the day, nearly every day; markedly diminished interest or pleasure in activities most of the day, nearl...",
          "tree_numbers": [
            "F03.600.300.375"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003865",
      "preferred_label": "Major Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Major Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:06:51+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003863",
          "name": "Depression",
          "type": "descriptor",
          "scope_note": "Depressive states usually of moderate intensity in contrast with MAJOR DEPRESSIVE DISORDER present in neurotic and psychotic disorders.",
          "tree_numbers": [
            "F01.145.126.350",
            "F01.470.282"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003863",
      "preferred_label": "Depression",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"dysthym*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"unipolar depression\"[Title/Abstract] OR \"unipolar depressive\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "10bc9805d7f320173f89331923c4b786b408130f1622469fcca04efee1d97df0",
      "note": "same-context critic; reviewed the supplied packet myself because no fresh context was available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The depression concept is the only required AND block. Relapse/recurrence and psychological-theory blocks were tested, each loses known relevant records, and both were left out with loss samples documented."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms within the condition block are OR-ed. No NOT or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder, Major Depressive Disorder, and Depression headings are explicitly tagged [Mesh]. Depression descriptor covers moderate depressive states and supplements disorder headings; MeSH vocabulary validated."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block includes depress* plus dysthymia, melancholia, and unipolar variants, with safe truncation. A broad depress* stem increases noise but is appropriate for a recall-first condition block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms have explicit field tags, no phrase-index warnings or parser diagnostics, and PubMed translations match the intended clauses."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No user-required language, age, study-design, or publication-date limits were imposed. Query is bounded by Entrez entry date through 2018-11-17, as required."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "evidence": "The depression-only query returns 460,729 records. Adding the relapse/recurrence block reduces this to 16,633 but loses PMID 21976044; the theory block reduces it to 10,198 but loses 11 of 19 screened relevant development records. Each refreshed 30-record loss sample had 0 relevant records, which does not outweigh observed known losses.",
          "status": "accepted-risk",
          "response": "Accept the over-budget retrieval as the recall-first consequence of leaving out optional topic-defining blocks that demonstrably lose known relevant records. Screening workload is high and should be managed through staged screening tools or by protocol-approved prioritization, not by silently narrowing the search."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "10bc9805d7f320173f89331923c4b786b408130f1622469fcca04efee1d97df0",
      "note": "same-context critic; second review of the unchanged strategy after correcting protocol notes and checking report --diagnostic.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Required condition remains depression; both optional topic-defining blocks were tested and left out because they lose known relevant records. Category probe is clean."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR composition is correct; no NOT/proximity operators are in the final block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All three depression headings are verified and explicitly tagged. MeSH explosion is default; text terms cover unindexed records."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text vocabulary includes depress*, dysthym*, melanchol*, and unipolar wording. Stems meet safe truncation rules. Broadness is intentional for sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint or PubMed translation issues; every term is tagged."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Entrez-date bound only, with no publication-date filter or ad hoc design/language/age limits."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "evidence": "The base query returns 460,729. Recurrence block reduces to 16,633 and misses PMID 21976044; psychological theory block reduces to 10,198 and misses 11/19 known relevant records. Refreshed loss samples found 0/30 relevant for each. Diagnostic report reports no technical blockers.",
          "status": "accepted-risk",
          "response": "Accept the large screen burden to preserve known-record recall: the two optional topic blocks were tested and each excludes relevant records. This should be reviewed with the protocol team because screening 460,729 records may be infeasible; any tighter search requires more known included studies and explicit scope/protocol decisions."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "10bc9805d7f320173f89331923c4b786b408130f1622469fcca04efee1d97df0",
      "note": "same-context closing review; all findings and the workload disposition from the two revision rounds were checked against the unchanged strategy and current evidence.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Prior reviews consistently found the depression-only search structure defensible for recall. Both optional blocks remain left out because of known-record losses; scope assumption and workload are documented."
        },
        "operators": {
          "verdict": "pass",
          "note": "No Boolean/operator changes since earlier rounds."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified depression headings remain intact."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text terms and broad-stem rationale remain as reviewed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or translation changes; no technical issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only explicit bound is the Entrez-date cutoff; no publication-date filter."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "evidence": "Current query count is 460,729. The relapse/recurrence block loses PMID 21976044; the theory/model block loses 11 of 19 known relevant records. Both 30-record loss samples were screened and contained no relevant records; diagnostic report had no blockers.",
          "status": "accepted-risk",
          "response": "The accepted workload risk is unchanged: optional blocks excluded known records, so the broader search remains necessary for the high-sensitivity draft. A protocol-approved screening plan is needed before use."
        }
      ]
    }
  ]
}
```


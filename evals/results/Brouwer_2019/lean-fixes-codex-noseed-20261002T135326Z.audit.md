# PubMed search strategy: audit

Generated 2026-10-02T14:08:45+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: PCC
- Scope confirmed by user: no (User has no known relevant articles and asked us not to pause for questions. Assumptions: the review covers any age group and publication type, and treats relapse/recurrence as the defining topic while screening for a substantive psychological theory or model. Theory/model terminology is not required as a search block because it may be absent from abstracts. No language, age, publication-type, or publication-date limit. PubMed is bounded by Entrez date 2018-11-17 via PSB_AS_OF; no publication-date cutoff is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | Depression is the condition of interest and is reliably named and indexed. |
| Depressive relapse and recurrence | search | Relapse or recurrence defines the process of interest, though terminology varies and the block must include broad variants. |
| Psychological theories or models explaining depressive relapse/recurrence | screen | Theory and model language is inconsistently reported and may occur only in full text; assess the psychological explanatory focus at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:08:25+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 17,535
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Depressive Disorder[Mesh]` | 105,341 | none |
| 2 | `Depression[Mesh]` | 206,675 | none |
| 3 | `depress*[tiab]` | 419,764 | none |
| 4 | `#1 OR #2 OR #3` | 460,091 | none |
| 5 | `Recurrence[Mesh]` | 178,366 | none |
| 6 | `relaps*[tiab]` | 163,847 | none |
| 7 | `recurr*[tiab]` | 518,001 | none |
| 8 | `#5 OR #6 OR #7` | 721,215 | none |
| 9 | `#4 AND #8` | 17,535 | none |

### Strategy (single line, for copying into PubMed)

```text
((Depressive Disorder[Mesh] OR Depression[Mesh] OR depress*[tiab]) AND (Recurrence[Mesh] OR relaps*[tiab] OR recurr*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 721,215 | 0 |
| relapse_recurrence | 460,091 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 17,535 | initial | none | Initial recall-first two-block strategy; benchmark candidates screened from the 2018 systematic review reference links. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; R1-1 should-fix resolved
- Round 2 on version 1: 1 findings; R1-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 254 NCBI requests logged (74 from cache); strategy sha256 476551549ff5._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [],
    "issues": []
  },
  "vocabulary": [
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:08:25+00:00",
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
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:08:25+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:08:25+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012008",
          "name": "Recurrence",
          "type": "descriptor",
          "scope_note": "The return of a sign, symptom, or disease after a remission.",
          "tree_numbers": [
            "C23.550.291.937"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012008",
      "preferred_label": "Recurrence",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "Recurrence",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"depressive disorder\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"depress*\"[Title/Abstract]) AND (\"recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurr*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "424eb2e819f9c908c7663840f6eab64a0e9654e2e1b7cd8fda34503e4d18440e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues or PubMed warnings. The MeSH headings shown map to the stated descriptors, and the text terms are field-tagged."
        },
        "operators": {
          "verdict": "pass",
          "note": "The depression and relapse/recurrence blocks are combined with AND; terms within each block are combined with OR. This matches the stated search and screening roles."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included MeSH headings are verified in the packet. The packet alone does not establish a further heading gap."
        },
        "text_words": {
          "verdict": "pass",
          "note": "depress*, relaps*, and recurr* cover the named condition and process wording broadly. The process is searched in both relapse and recurrence directions; theory/model wording is appropriately reserved for screening."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed query uses consistent field tags, grouping, and search-history references. No syntax errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-type, or publication-date limit is applied. The stated Entrez date bound is reflected in the query and matches the protocol."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 100% recall result is based on three relevant records from the build, explicitly labeled development checks rather than independent validation. The packet also says there are no known relevant articles, so this result should not be read as evidence of validated sensitivity.",
          "recommendation": "Report the result as development-set coverage only and state that independent validation was not performed.",
          "status": "resolved",
          "response": "Added a clear reporting statement: 3/3 (100%) is development-set coverage from records found during this build; independent validation was not performed and the percentage is not an estimate of sensitivity. No user-supplied seed records existed, but three relevant records were found and screened in during the build."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 1,
      "review_sha256": "424eb2e819f9c908c7663840f6eab64a0e9654e2e1b7cd8fda34503e4d18440e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues or PubMed warnings. The MeSH translations are shown, and the text terms are field-tagged."
        },
        "operators": {
          "verdict": "pass",
          "note": "The condition and relapse/recurrence blocks are combined with AND, and terms within each block are combined with OR. Theory and model language is appropriately assessed at screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the included MeSH headings. It does not provide evidence of a further heading gap."
        },
        "text_words": {
          "verdict": "pass",
          "note": "depress*, relaps*, and recurr* cover the named condition and both directions of the process. Theory/model terminology is appropriately left for screening."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query has consistent grouping and field tags, and the packet reports no syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-type, or publication-date limit is applied. The Entrez date bound matches the stated protocol."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 100% recall result is based on three relevant records from the build, labeled as development checks rather than independent validation. It should not be interpreted as evidence of validated sensitivity.",
          "recommendation": "Report the result as development-set coverage and state that independent validation was not performed.",
          "status": "resolved",
          "response": "The reporting statement identifies 3/3 (100%) as development-set coverage from records found during this build, says independent validation was not performed, and clarifies that the percentage is not an estimate of sensitivity. It also states that there were no user-supplied seed records."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


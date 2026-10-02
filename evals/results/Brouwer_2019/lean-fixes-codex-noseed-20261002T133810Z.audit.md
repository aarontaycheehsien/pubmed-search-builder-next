# PubMed search strategy: audit

Generated 2026-10-02T13:52:43+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: topic review (depressive disorder + course process)
- Scope confirmed by user: no (User asked to proceed without questions. Assumed broad depressive disorder scope and treated psychological theory/model/mechanism as a screening criterion because theoretical framing may be implicit and requiring theory terminology risks missing relevant papers. No language, age, setting, or study-design limits. The PubMed record cutoff is 2018-11-17 by Entrez date (PSB_AS_OF), recorded in as_of; no publication-date [dp] limit is used. No seed articles supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depression and depressive disorders | search | The condition is required by the question and is indexed and named consistently. |
| Relapse or recurrence | search | The course process defines the topic and is searchable, though wording varies; use broad MeSH and text terms. |
| Psychological explanations, theories, models, and mechanisms | screen | Theoretical framing may be implicit or described without the word theory; screening is safer than requiring a separate block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:52:20+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 26,641
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Depressive Disorder[Mesh]` | 105,341 | none |
| 2 | `Major Depressive Disorder[Mesh]` | 28,520 | none |
| 3 | `depress*[tiab]` | 419,764 | none |
| 4 | `melancholia[tiab]` | 1,412 | none |
| 5 | `#1 OR #2 OR #3 OR #4` | 438,756 | none |
| 6 | `Recurrence[Mesh]` | 178,366 | none |
| 7 | `relaps*[tiab]` | 163,847 | none |
| 8 | `recur*[tiab]` | 531,492 | none |
| 9 | `recrudescen*[tiab]` | 3,173 | none |
| 10 | `vulnerab*[tiab]` | 113,966 | none |
| 11 | `#6 OR #7 OR #8 OR #9 OR #10` | 847,096 | none |
| 12 | `#5 AND #11` | 26,641 | none |

### Strategy (single line, for copying into PubMed)

```text
((Depressive Disorder[Mesh] OR Major Depressive Disorder[Mesh] OR depress*[tiab] OR melancholia[tiab]) AND (Recurrence[Mesh] OR relaps*[tiab] OR recur*[tiab] OR recrudescen*[tiab] OR vulnerab*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 847,096 | 0 |
| relapse_recurrence | 438,756 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 17,359 | initial | none | Initial two-block recall-first draft: broad depression and relapse/recurrence terms with explicit MeSH plus title/abstract text. Screen psychological theory/model/mechanism at eligibility because terminology is unreliable. |
| 2 | 26,641 | relapse_recurrence: +1 / -0 | none | Addressed first critic must-fix F1 by adding vulnerab*[tiab] to retrieve papers describing vulnerability to a subsequent episode without using relapse/recurrence terminology. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; F1 must-fix open
- Round 2 on version 2: 2 findings; F1 must-fix resolved, F2 must-fix resolved
- Round 3 on version 2: 2 findings; F1 must-fix resolved, F2 must-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 297 NCBI requests logged (95 from cache); strategy sha256 46e4452b1f69._

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
      "checked_at": "2026-10-02T13:52:20+00:00",
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
      "requested": "Major Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:52:20+00:00",
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
        "text": "Major Depressive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:52:20+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "Recurrence",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"depressive disorder\"[MeSH Terms] OR \"major depressive disorder\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"melancholia\"[Title/Abstract]) AND (\"recurrence\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recur*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"vulnerab*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "e2aef9b0c7f28e253e9e0daf63f29c2449cc3b45ffd34c3abce283834faba6e7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The supplied PubMed translations match the intended MeSH and title/abstract fields; no translation warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each concept and AND combines the required depression and relapse/recurrence concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Depressive Disorder, Major Depressive Disorder, and Recurrence are verified descriptors that fit the searched concepts."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Eligibility explicitly includes vulnerability to a subsequent depressive episode, but the relapse/recurrence block has no bare text term for vulnerability."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The field tags, Boolean grouping, and query syntax are valid in the supplied evidence."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No protocol limits are applied. The Entrez date cutoff is documented as a record cutoff rather than a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes vulnerability to a subsequent depressive episode, but the relapse/recurrence search block contains no standalone text term for vulnerability. The depression terms do not ensure retrieval of records that describe vulnerability without naming relapse or recurrence.",
          "recommendation": "Add a bare-name title/abstract term such as vulnerab*[tiab] to the relapse/recurrence block, then rerun the complete evaluation and report the updated retrieval and known-record results.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "658118f1adde351bc63490ca9db8b5261d6c4cf2fd825fbb5bd5ea36c54dfc68",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The supplied PubMed translations match the intended MeSH and title/abstract fields; no translation warnings or errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within each concept, and depression is ANDed with relapse or recurrence."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied evidence verifies Depressive Disorder, Major Depressive Disorder, and Recurrence as descriptors that fit the searched concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The bare text terms cover depression, relapse, recurrence, recrudescence, and vulnerability as named in the searched concepts and eligibility. Psychological theory and mechanism remain screening criteria, consistent with the protocol rationale."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The field tags, Boolean grouping, and supplied query syntax are valid. No phrase or proximity expressions require interpretation."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The strategy applies an Entrez date cutoff of 2018-11-17 despite the protocol stating that there are no date limits. Although this is not a publication-date limit, it excludes records added to PubMed after that date and is inconsistent with the stated scope."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes vulnerability to a subsequent depressive episode, but the relapse/recurrence search block in version 1 had no standalone text term for vulnerability.",
          "recommendation": "Add a bare-name title/abstract term such as vulnerab*[tiab] to the relapse/recurrence block, then rerun the complete evaluation and report updated retrieval and known-record results.",
          "status": "resolved",
          "response": "Version 2 adds vulnerab*[tiab] and reruns the full evaluation. The query retrieves all 4 of 4 development records, with no known records lost; these are development records, not independent validation. The result count is 26,641."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query limits Entrez dates to 2018-11-17, while the protocol lists no date limits. This record-entry cutoff excludes records added after that date, even though it is not a publication-date filter.",
          "recommendation": "Remove the Entrez date cutoff and rerun the complete evaluation without a date limit.",
          "status": "resolved",
          "response": "The cutoff is required by the user's harness instruction and is the intended temporal scope. I set protocol.as_of to 2018-11-17 to record the actual PubMed Entrez-date bound. The search does not use a publication-date [dp] filter. The environment bound and protocol date are identical; the query will retain this required cutoff."
        }
      ],
      "issue_dispositions": [
        {
          "id": "F1",
          "status": "resolved",
          "response": "Version 2 added vulnerab*[tiab] and reran the complete evaluation."
        },
        {
          "id": "F2",
          "status": "resolved",
          "response": "The user's harness requires an Entrez-date cutoff of 2018-11-17. The protocol now records the same effective as_of date, and no publication-date [dp] limit is used."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "c913e10c611815eea0b7d4efa6a8c8051cb1a2a29612255a3afce7e656287506",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The supplied translations match the MeSH and title/abstract terms; no translation warnings or errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within each block, and the depression and relapse/recurrence blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied evidence verifies Depressive Disorder, Major Depressive Disorder, and Recurrence as descriptors fitting the searched concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current strategy includes vulnerab*[tiab] as a standalone term, addressing F1. Other named depression and relapse/recurrence terms are represented; psychological explanations remain a screening criterion as specified in the protocol."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied query uses valid field tags and Boolean grouping. No phrase or proximity expressions require interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez cutoff remains, but the current protocol records the matching 2018-11-17 as_of date and states that no publication-date [dp] limit is used. The prior disposition identifies the cutoff as required by the user's harness."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Earlier versions lacked a standalone text term for vulnerability, despite eligibility including vulnerability to a subsequent depressive episode.",
          "recommendation": "Add a bare-name title/abstract term such as vulnerab*[tiab] and rerun the full evaluation.",
          "status": "resolved",
          "response": "The current relapse/recurrence block includes vulnerab*[tiab]. The full evaluation reports all 4 of 4 development records retrieved, with no known records lost."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entrez-date cutoff of 2018-11-17, which excludes records entered in PubMed after that date.",
          "recommendation": "Remove the cutoff or document it as the required temporal scope.",
          "status": "accepted-risk",
          "response": "The prior-round response states that the user's harness requires this cutoff. The current protocol records the matching 2018-11-17 as_of date, and the query has no publication-date [dp] filter."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


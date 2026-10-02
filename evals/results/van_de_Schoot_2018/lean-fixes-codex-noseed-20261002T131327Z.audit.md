# PubMed search strategy: audit

Generated 2026-10-02T13:24:38+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis
- Scope confirmed by user: yes (User requested proceeding without clarification. Assumption: include all ages, traumatic event types, settings, and study designs when repeated PTSD symptom assessment and trajectory/course results are reported. No language, publication-date, age, or design limits. Entrez-date cutoff is 2016-01-24 via as_of; no [dp] limit. PTSD is the sole required search block; trajectory/course and trauma details are screened because they are inconsistently named in abstracts. No user-supplied known records. Web search is prohibited for this run.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder | search | The condition that defines the topic; reliably named and indexed. |
| Longitudinal symptom trajectories or course after trauma | screen | The outcome and longitudinal feature define eligibility but are described inconsistently in titles, abstracts, and indexing; screen records for symptom course over time rather than requiring a fragile trajectory block. |
| Traumatic event or exposure | screen | PTSD itself implies trauma exposure, and trauma type/timing may be incompletely reported in abstracts; assess during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:24:26+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,074
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Stress Disorders, Post-Traumatic[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `posttraumatic stress disorder[tiab]` | 12,500 | none |
| 4 | `post-traumatic stress disorder[tiab]` | 7,081 | none |
| 5 | `post traumatic stress disorder[tiab]` | 7,081 | none |
| 6 | `posttraumatic stress[tiab]` | 14,174 | none |
| 7 | `post-traumatic stress[tiab]` | 8,160 | none |
| 8 | `post traumatic stress[tiab]` | 8,160 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 32,074 | none |

### Strategy (single line, for copying into PubMed)

```text
((Stress Disorders, Post-Traumatic[Mesh] OR PTSD[tiab] OR posttraumatic stress disorder[tiab] OR post-traumatic stress disorder[tiab] OR post traumatic stress disorder[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,074 | initial | none | Initial one-block recall-first PTSD strategy; MeSH descriptor plus title/abstract diagnosis spellings. Course/trajectory and trauma details remain screening criteria because they are variably named. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1 (Same-context critic: no independent fresh-context reviewer was available. Reviewed the packet against the six PRESS domains.): 0 findings; 
- Round 2 on version 1 (Same-context critic: no independent fresh-context reviewer was available. Second packet review; no strategy or scope changes were indicated.): 0 findings; 
- Round 3 on version 1 (Same-context closing review: no independent fresh-context reviewer was available. Both earlier rounds recorded no findings; the strategy and scope are unchanged.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 159 NCBI requests logged (28 from cache); strategy sha256 6932da785a9b._

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
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:24:26+00:00",
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
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"post traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "1be5dde257d06db6138292dc1d6cbf0ea78fb4982bf4c9b811e74f9a01f8f8f9",
      "note": "Same-context critic: no independent fresh-context reviewer was available. Reviewed the packet against the six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The sole required concept is PTSD. Trajectory/course and trauma context are screened with explicit eligibility criteria, avoiding fragile required blocks."
        },
        "operators": {
          "verdict": "pass",
          "note": "One OR-ed PTSD block uses no unnecessary AND, NOT, or proximity operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Stress Disorders, Post-Traumatic descriptor is appropriate and exploded; its lookup reports no narrower headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "PTSD and spaced, hyphenated, and closed forms of post-traumatic stress are represented in title/abstract fields. The broad stress phrase also finds symptom wording without requiring disorder."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly fielded, the lint is clean, PubMed translations have no warnings, and no technical validation blockers were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, publication-date, or study-design filters are used. The tested Entrez-date cutoff is applied through as_of."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 1,
      "review_sha256": "1be5dde257d06db6138292dc1d6cbf0ea78fb4982bf4c9b811e74f9a01f8f8f9",
      "note": "Same-context critic: no independent fresh-context reviewer was available. Second packet review; no strategy or scope changes were indicated.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD is the only required block. Trauma and symptom trajectory/course remain explicit screening criteria with no new scope issue evident in the packet."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines the disease descriptor and relevant title/abstract terms. No risky Boolean or proximity construction is present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified PTSD MeSH descriptor is appropriate; the lookup reports no narrower headings, and the explosion choice is documented."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text layer covers acronym and punctuation/spelling variants. No translation warning or known-record miss indicates a gap; remaining recall limits are documented as empirical uncertainty."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Lint is clean and live PubMed checks report no syntax, field, phrase, or controlled-vocabulary blocker."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unvalidated filter or publication-date limit is applied. The Entrez-date cutoff is represented by as_of."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 1,
      "review_sha256": "1be5dde257d06db6138292dc1d6cbf0ea78fb4982bf4c9b811e74f9a01f8f8f9",
      "note": "Same-context closing review: no independent fresh-context reviewer was available. Both earlier rounds recorded no findings; the strategy and scope are unchanged.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "There were no earlier translation findings to close. The current scope still searches PTSD only and screens for trauma-related symptom course/trajectory."
        },
        "operators": {
          "verdict": "pass",
          "note": "There were no earlier operator findings to close; the current OR-ed single block remains simple and valid."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "There were no earlier heading findings to close; the current descriptor remains verified and appropriate."
        },
        "text_words": {
          "verdict": "pass",
          "note": "There were no earlier text-word findings to close; the current variants are unchanged and the development set remains retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "There were no earlier syntax findings to close; validation reports no technical blockers or translation warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "There were no earlier filter findings to close; the Entrez date cutoff is the only limit and is encoded through as_of."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


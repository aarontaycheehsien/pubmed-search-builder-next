# PubMed search strategy: audit

Generated 2026-09-28T14:45:06+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Methodological rigour of systematic reviews in environmental health
- Framework: methodological quality assessment / domain-specific evidence synthesis
- Scope confirmed by user: no (User asked to proceed without questions. Scope roles are provisional and unconfirmed. Assumes environmental health is the review domain and methodological rigour refers to assessment of systematic review conduct/quality/reporting/risk of bias. No supplied known relevant records. PubMed records bounded by Entrez date 2020-07-20; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Systematic reviews and meta-analyses | search | The unit being assessed is systematic reviews; records must concern this recognizable review type. |
| Environmental health | search | Environmental health defines the application domain and should be identifiable by indexing or title/abstract terms. |
| Methodological rigour, quality, and risk of bias of reviews | optional | This is the topic-defining appraisal focus, but relevant overview papers may describe review methods without naming these concepts consistently; test before deciding whether to AND. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T14:44:34+00:00
- Records added to PubMed up to: 2020-07-20
- Total records: 12,405
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Systematic Reviews as Topic"[Mesh]` | 6,347 | none |
| 2 | `"Meta-Analysis as Topic"[Mesh]` | 20,321 | none |
| 3 | `"systematic review"[tiab]` | 160,742 | none |
| 4 | `"systematic reviews"[tiab]` | 30,250 | none |
| 5 | `"systematic literature review"[tiab]` | 11,090 | none |
| 6 | `"umbrella review"[tiab]` | 410 | none |
| 7 | `"umbrella reviews"[tiab]` | 40 | none |
| 8 | `meta-analy*[tiab]` | 176,011 | none |
| 9 | `"meta analysis"[tiab]` | 152,699 | none |
| 10 | `"evidence synthesis"[tiab]` | 4,462 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 289,919 | none |
| 12 | `"Environmental Health"[Mesh]` | 25,528 | none |
| 13 | `"Environmental Exposure"[Mesh]` | 309,210 | none |
| 14 | `environmental health[tiab]` | 9,584 | none |
| 15 | `environment*[tiab]` | 1,016,489 | none |
| 16 | `"environmental exposure"[tiab]` | 7,564 | none |
| 17 | `"environmental exposures"[tiab]` | 6,391 | none |
| 18 | `"exposure science"[tiab]` | 146 | none |
| 19 | `"environmental epidemiology"[tiab]` | 721 | none |
| 20 | `"environmental and occupational health"[tiab]` | 280 | none |
| 21 | `"occupational and environmental health"[tiab]` | 540 | none |
| 22 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 1,258,854 | none |
| 23 | `#11 AND #22` | 12,405 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Systematic Reviews as Topic"[Mesh] OR "Meta-Analysis as Topic"[Mesh] OR "systematic review"[tiab] OR "systematic reviews"[tiab] OR "systematic literature review"[tiab] OR "umbrella review"[tiab] OR "umbrella reviews"[tiab] OR meta-analy*[tiab] OR "meta analysis"[tiab] OR "evidence synthesis"[tiab]) AND ("Environmental Health"[Mesh] OR "Environmental Exposure"[Mesh] OR environmental health[tiab] OR environment*[tiab] OR "environmental exposure"[tiab] OR "environmental exposures"[tiab] OR "exposure science"[tiab] OR "environmental epidemiology"[tiab] OR "environmental and occupational health"[tiab] OR "occupational and environmental health"[tiab])) AND ("1800/01/01"[edat] : "2020/07/20"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Methodological rigour, quality, and risk of bias of reviews | left out | 12,405 / 9,408 | 24.2% | none | 0/30 (up to 10% of removed records could be relevant) | The block would remove 2,997 of 12,405 records (24.2%), below the roughly 30% material-reduction criterion, and would risk excluding relevant reviews that do not name appraisal terms. The stored 30-record loss sample was screened against protocol eligibility; none assessed systematic-review rigor in environmental health. Leave the concept out to preserve recall; screen the methodological focus at title/abstract/full text. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| systematic_reviews | 1,258,854 | 0 |
| environmental_health | 289,919 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 12,706 | initial | none | Initial strategy: scope-defined environmental health and systematic review blocks; optional methods/quality appraisal block tested. Vocabulary from MeSH lookups and two screened relevant records. |
| 2 | 12,405 | environmental_health: +0 / -1 | none | Removed ambiguous Environmental Pollutants MeSH mapping after authority validation; Environmental Health and Environmental Exposure headings retain the environmental domain. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (Same-context critic: no fresh-context reviewer session was available in this host.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 456 NCBI requests logged (223 from cache); strategy sha256 e56c2fc60274._

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
        "message": "12,405 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "12,405 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "requested": "Systematic Reviews as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:44:34+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000078202",
          "name": "Systematic Reviews as Topic",
          "type": "descriptor",
          "scope_note": "Works about a review of primary literature in health and health policy that attempt to identify, appraise, and synthesize all the empirical evidence that meets specified eligibility criteria to answer a given research question. It's conducted using explicit methods aimed at minimizing bias in order to produce more reliable findings regarding the effects of interventions for prevention, treatmen...",
          "tree_numbers": [
            "L01.462.500.682.759.575"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000078202",
      "preferred_label": "Systematic Reviews as Topic",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Systematic Reviews as Topic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Meta-Analysis as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:44:34+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015201",
          "name": "Meta-Analysis as Topic",
          "type": "descriptor",
          "scope_note": "A quantitative method of combining the results of independent studies (usually drawn from the published literature) and synthesizing summaries and conclusions which may be used to evaluate therapeutic effectiveness, plan new studies, etc., with application chiefly in the areas of research and medicine.",
          "tree_numbers": [
            "E05.318.370.500",
            "E05.581.500.501",
            "N05.715.360.325.515",
            "N06.850.520.445.500"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015201",
      "preferred_label": "Meta-Analysis as Topic",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Meta-Analysis as Topic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:44:34+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004782",
          "name": "Environmental Health",
          "type": "descriptor",
          "scope_note": "The science of controlling or modifying those conditions, influences, or forces surrounding man which relate to promoting, establishing, and maintaining health.",
          "tree_numbers": [
            "H02.229"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004782",
      "preferred_label": "Environmental Health",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"Environmental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Exposure",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:44:34+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004781",
          "name": "Environmental Exposure",
          "type": "descriptor",
          "scope_note": "The exposure to potentially harmful chemical, physical, or biological agents in the environment or to environmental factors that may include ionizing radiation, pathogenic organisms, or toxic chemicals.",
          "tree_numbers": [
            "N06.850.460.350"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004781",
      "preferred_label": "Environmental Exposure",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Environmental Exposure\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Systematic Reviews as Topic\"[MeSH Terms] OR \"Meta-Analysis as Topic\"[MeSH Terms] OR \"systematic review\"[Title/Abstract] OR \"systematic reviews\"[Title/Abstract] OR \"systematic literature review\"[Title/Abstract] OR \"umbrella review\"[Title/Abstract] OR \"umbrella reviews\"[Title/Abstract] OR \"meta analy*\"[Title/Abstract] OR \"meta analysis\"[Title/Abstract] OR \"evidence synthesis\"[Title/Abstract]) AND (\"Environmental Health\"[MeSH Terms] OR \"Environmental Exposure\"[MeSH Terms] OR \"Environmental Health\"[Title/Abstract] OR \"environment*\"[Title/Abstract] OR \"Environmental Exposure\"[Title/Abstract] OR \"environmental exposures\"[Title/Abstract] OR \"exposure science\"[Title/Abstract] OR \"environmental epidemiology\"[Title/Abstract] OR \"environmental and occupational health\"[Title/Abstract] OR \"occupational and environmental health\"[Title/Abstract]) AND 1800/01/01:2020/07/20[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "0dd17299d4a80e1bb165736b50f56216e19043fb304ecae792719ac426797803",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required concepts map to the question. Methodological rigor was tested as optional and left out after the measured sample and reduction; it will be screened. Environmental health is represented broadly to retain reviews naming specific exposures rather than the field label."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks are OR-combined and AND-ed without NOT; no proximity clauses are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Systematic Reviews as Topic, Meta-Analysis as Topic, Environmental Health, and Environmental Exposure are verified descriptors and exploded by default. An ambiguous Environmental Pollutants heading was removed and the strategy reevaluated."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract words cover systematic review, systematic literature review, umbrella review, meta-analysis, evidence synthesis, environmental health, environmental exposure, exposure science, and environmental epidemiology. environment* is broad but preserves recall for named hazards and domains."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms have explicit MeSH or title/abstract fields, truncation stems have at least four characters, the full query translates without warnings, and lint reports no issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or other limits were added. The required 2020-07-20 Entrez-date bound is applied by the workspace as_of setting."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional methodological-rigour block was evaluated against the required 30-record loss sample and removed 24.2% of the core result set, below the skill's approximate threshold for a material reduction. All 30 records were screened and none met the stated eligibility criteria; the sample cannot exclude relevant records in the full loss set. No other searchable focus concept remains only screened. Retaining the two broad core blocks preserves recall at the cost of a screening set above the default 10,000-record budget; confirm capacity or run a supplementary precision-focused search after protocol approval.",
          "evidence": "Evaluation v2 reports 12,405 core records, 9,408 with the optional block (24.2% reduction), no known records lost, and a 0/30 relevant loss sample. The optional decision is current. The core strategy retrieves both screened development records; no held-out or benchmark set exists."
        }
      ],
      "note": "Same-context critic: no fresh-context reviewer session was available in this host."
    }
  ]
}
```


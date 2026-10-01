# PubMed search strategy: audit

Generated 2026-10-01T11:16:21+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method-performance
- Scope confirmed by user: no (User asked to proceed without questions; scope and roles are working assumptions and were not user-confirmed. The harness explicitly requires a PubMed Entrez date-of-entry cutoff of 2017-11-29 on every command; this is a run constraint, not a review eligibility date limit. No publication-date ([dp]) limit is applied. No known relevant articles supplied. Standard-depth candidate screening budget about 150. Six records were screened in as development records; recall against them is not independent validation.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and SEM/latent-variable family models (CFA, latent growth/class, multilevel, mediation) | search | The estimation task applies to these models; the question and eligibility criteria specify these model families, which can be named in titles/abstracts or indexed. |
| Bayesian estimation | search | Bayesian estimation is the focal method and should be searchable by its labels and indexing. |
| Small sample or few-cluster context | optional | This defines the context but may be inconsistently labelled; test as an optional block and screen if not safely AND-ed. |
| Frequentist / maximum-likelihood comparator | screen | Comparator wording is inconsistently reported and is not required to retrieve method papers. |
| Performance, accuracy, bias outcomes | screen | Outcome terms vary and are better assessed during screening. |
| Monte Carlo / simulation design | screen | Simulation design is an eligibility feature; avoid an unvalidated design filter. |
| Peer-reviewed social/behavioural-science methodology | screen | Disciplinary fit and peer-review status may require journal/full-text assessment and should not be a restrictive PubMed block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:15:39+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,985
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"structural equation model"[tiab]` | 1,934 | none |
| 5 | `"structural equation models"[tiab]` | 1,695 | none |
| 6 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 7 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 8 | `SEM[tiab]` | 81,594 | none |
| 9 | `CFA[tiab]` | 7,128 | none |
| 10 | `"confirmatory factor analys*"[tiab]` | 10,281 | none |
| 11 | `"factor analysis"[tiab]` | 33,735 | none |
| 12 | `"latent variable model*"[tiab]` | 671 | none |
| 13 | `"latent growth"[tiab]` | 1,734 | none |
| 14 | `"growth curve model*"[tiab]` | 1,502 | none |
| 15 | `"latent class"[tiab]` | 4,129 | none |
| 16 | `"growth mixture model*"[tiab]` | 768 | none |
| 17 | `multilevel[tiab]` | 25,930 | none |
| 18 | `"mixed effects"[tiab]` | 11,300 | none |
| 19 | `"mixed-effects"[tiab]` | 11,300 | none |
| 20 | `"mixed effects model*"[tiab]` | 6,832 | none |
| 21 | `"mixed-effects model*"[tiab]` | 6,832 | none |
| 22 | `"hierarchical model*"[tiab]` | 3,344 | none |
| 23 | `mediation[tiab]` | 22,917 | none |
| 24 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23` | 211,829 | none |
| 25 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 26 | `Bayes*[tiab]` | 39,780 | none |
| 27 | `Bayesian[tiab]` | 35,533 | none |
| 28 | `"Bayesian estimation"[tiab]` | 966 | none |
| 29 | `MCMC[tiab]` | 1,577 | none |
| 30 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 31 | `"prior distribution*"[tiab]` | 1,143 | none |
| 32 | `#25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31` | 48,036 | none |
| 33 | `#24 AND #32` | 2,985 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "structural equation model"[tiab] OR "structural equation models"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR SEM[tiab] OR CFA[tiab] OR "confirmatory factor analys*"[tiab] OR "factor analysis"[tiab] OR "latent variable model*"[tiab] OR "latent growth"[tiab] OR "growth curve model*"[tiab] OR "latent class"[tiab] OR "growth mixture model*"[tiab] OR multilevel[tiab] OR "mixed effects"[tiab] OR "mixed-effects"[tiab] OR "mixed effects model*"[tiab] OR "mixed-effects model*"[tiab] OR "hierarchical model*"[tiab] OR mediation[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayes*[tiab] OR Bayesian[tiab] OR "Bayesian estimation"[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "prior distribution*"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small sample or few-cluster context | left out | 2,985 / 172 | 94.2% | none | 0/30 (up to 10% of removed records could be relevant) | The block reduces the current topic query from 2,985 to 172 records (94.2%), and none of 30 sampled records outside the block met eligibility. Only six relevant records have been found, below the skill's 15-record threshold for showing an AND block is safe, so retain small sample as a screening criterion to protect recall. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_models | 48,036 | 0 |
| bayesian | 211,829 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 12,296 | initial | none | First broad draft from question-defined SEM and Bayesian blocks; small-sample block retained as optional for testing. No known records supplied. |
| 2 | 2,580 | sem_models: +1 / -1; bayesian: +1 / -0 | none | Removed generic Models, Statistical MeSH after confirming it retrieved a broad, non-specific model set; added plural structural-equation wording and Bayesian-estimation phrasing; expanded optional small-sample block with sample sizes from screened records. |
| 3 | 2,985 | sem_models: +4 / -0 | none | Added mixed-effects wording to the multilevel model block after terms miss identified PMID 16345043 as a known miss; screened its abstract and confirmed it meets the stated multilevel/small-cluster simulation comparison criteria. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-F1 must-fix open
- Round 2 on version 3: 1 findings; R1-F1 must-fix resolved
- Round 3 on version 3: 1 findings; R1-F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 510 NCBI requests logged (195 from cache); strategy sha256 ed93984efa06._

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
      "requested": "Factor Analysis, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:15:39+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005163",
          "name": "Factor Analysis, Statistical",
          "type": "descriptor",
          "scope_note": "A set of statistical methods for analyzing the correlations among several variables in order to estimate the number of fundamental dimensions that underlie the observed data and to describe and measure those dimensions. It is used frequently in the development of scoring systems for rating scales and questionnaires.",
          "tree_numbers": [
            "E05.318.740.400",
            "N05.715.360.750.350",
            "N06.850.520.830.400"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005163",
      "preferred_label": "Factor Analysis, Statistical",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Factor Analysis, Statistical\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Latent Class Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:15:39+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000077272",
          "name": "Latent Class Analysis",
          "type": "descriptor",
          "scope_note": "A statistical algorithm used to analyze clusters of observed variables by constructing categorical unobserved or latent segment based on weighted analysis and the average probabilities. Such latent classes are used to infer variables whose relationships are not directly observed. In biomedical research, it is often used to categorize data that allows the determination of symptom clusters.",
          "tree_numbers": [
            "E05.318.740.250.338",
            "G17.035.625",
            "L01.224.050.687",
            "N05.715.360.750.200.375",
            "N06.850.520.830.250.338"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000077272",
      "preferred_label": "Latent Class Analysis",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Latent Class Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:15:39+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D055361",
          "name": "Multilevel Analysis",
          "type": "descriptor",
          "scope_note": "The statistical manipulation of hierarchically and non-hierarchically nested data. It includes clustered data, such as a sample of subjects within a group of schools. Prevalent in the social, behavioral sciences, and biomedical sciences, both linear and nonlinear regression models are applied.",
          "tree_numbers": [
            "N06.850.520.830.562"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D055361",
      "preferred_label": "Multilevel Analysis",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Multilevel Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:15:39+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001499",
          "name": "Bayes Theorem",
          "type": "descriptor",
          "scope_note": "A theorem in probability theory named for Thomas Bayes (1702-1761). In epidemiology, it is used to obtain the probability of disease in a group of people with some characteristic on the basis of the overall rate of that disease and of the likelihood of that characteristic in healthy and diseased individuals. The most familiar application is in clinical decision analysis where it is used for est...",
          "tree_numbers": [
            "E05.318.740.600.200",
            "N05.715.360.750.625.150",
            "N06.850.520.830.600.200"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001499",
      "preferred_label": "Bayes Theorem",
      "type": "descriptor",
      "location": "vocabulary:24",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"structural equation model\"[Title/Abstract] OR \"structural equation models\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"confirmatory factor analys*\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable model*\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model*\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"growth mixture model*\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"mixed-effects\"[Title/Abstract] OR \"mixed-effects\"[Title/Abstract] OR \"mixed effects model*\"[Title/Abstract] OR \"mixed effects model*\"[Title/Abstract] OR \"hierarchical model*\"[Title/Abstract] OR \"mediation\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"bayes*\"[Title/Abstract] OR \"Bayesian\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"prior distribution*\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "e6dfab5e59784815f4d450a879a058e7d2005799a7d104c53646a88850cb04f5",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search blocks represent both named searchable concepts. The SEM family block includes the eligibility examples, including CFA, latent growth, latent class, multilevel, and bare mediation; the Bayesian block includes text words and a heading."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each block and AND combines the SEM-family and Bayesian blocks. Comparator, outcomes, simulation design, and discipline remain screening criteria as scoped. The optional small-sample block is correctly left out because six known records do not meet the 15-record threshold."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected headings for factor analysis, latent class analysis, multilevel analysis, and Bayes theorem. These are combined with free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text terms cover the specified model families and Bayesian estimation terminology. Broad terms such as SEM and multilevel may add screening workload, but their use is consistent with the recall-oriented scope."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax or translation diagnostics for the evaluated lines."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The user-specified harness requires the Entrez date-of-entry cutoff ending 2017-11-29. Document it as a test constraint, not an eligibility limit; leave publication date unrestricted."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query is restricted by the harness-mandated Entrez date of entry through 2017-11-29; no question-level date restriction was specified.",
          "recommendation": "Record the harness requirement as the reason for the bound and ensure no publication-date limit is used.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "e6dfab5e59784815f4d450a879a058e7d2005799a7d104c53646a88850cb04f5",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks cover the named SEM and latent-variable model families, including bare mediation, and Bayesian estimation terminology."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within each searched block, and the SEM-family and Bayesian blocks are AND-ed. Comparator, outcomes, simulation design, and discipline remain screening criteria. The small-sample block is correctly left out because six known records do not meet the 15-record threshold."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected headings for factor analysis, latent class analysis, multilevel analysis, and Bayes theorem, alongside free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text terms cover the specified model families and Bayesian estimation terminology; broad terms are consistent with the recall-oriented scope."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax or translation diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The notes identify the Entrez date-of-entry cutoff through 2017-11-29 as a harness run constraint, not an eligibility limit. The final query uses [edat] and no publication-date [dp] limit."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query is restricted by the harness-mandated Entrez date of entry through 2017-11-29; no question-level date restriction was specified.",
          "recommendation": "Record the harness requirement as the reason for the bound and ensure no publication-date limit is used.",
          "status": "resolved",
          "response": "The strategy notes document the 2017-11-29 Entrez date-of-entry cutoff as a run constraint, and the final query contains an [edat] range without a [dp] limit."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "e6dfab5e59784815f4d450a879a058e7d2005799a7d104c53646a88850cb04f5",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks cover the named SEM and latent-variable model families, including bare mediation, and Bayesian estimation terminology."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within each searched block, and the model-family and Bayesian blocks are AND-ed. Comparator, outcomes, simulation design, and discipline remain screening criteria. The small-sample block is left out because six known records do not meet the 15-record threshold."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected headings for factor analysis, latent class analysis, multilevel analysis, and Bayes theorem, alongside free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text terms cover the specified model families and Bayesian estimation terminology; broad terms are consistent with the recall-oriented scope."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax or translation diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The notes identify the Entrez date-of-entry cutoff through 2017-11-29 as a harness run constraint, not an eligibility limit. The final query uses [edat] and no publication-date [dp] limit."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query is restricted by the harness-mandated Entrez date of entry through 2017-11-29; no question-level date restriction was specified.",
          "recommendation": "Record the harness requirement as the reason for the bound and ensure no publication-date limit is used.",
          "status": "resolved",
          "response": "The strategy notes document the 2017-11-29 Entrez date-of-entry cutoff as a run constraint, and the final query contains an [edat] range without a [dp] limit."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


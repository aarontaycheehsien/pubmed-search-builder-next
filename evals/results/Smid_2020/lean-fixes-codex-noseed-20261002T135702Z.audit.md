# PubMed search strategy: audit

Generated 2026-10-02T14:12:14+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: Method performance
- Scope confirmed by user: no (User requested no questions and asked to proceed; concept roles were not confirmed. No topical eligibility limits apply. The task harness explicitly requires a PubMed as-of date of 2017-11-29 and forbids later-added records; PSB_AS_OF and protocol.as_of implement that Entrez entry-date bound, with no [dp] publication-date limit. No known articles supplied. Standard-depth discovery used PubMed-only precise pilots and title/abstract screening before adding a relevant development set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable models | search | Core model family; eligibility explicitly names SEM and several common members, and model terminology is searchable. |
| Bayesian estimation | search | Core method being evaluated; Bayesian estimation is central to every eligible study and is named in titles/abstracts/indexing. |
| Small sample or few-cluster context | screen | Eligibility context can be reported inconsistently and may not appear in title/abstract. |
| Frequentist or maximum-likelihood comparison | screen | Comparator terms are inconsistently reported and screened from abstracts/full text. |
| Monte Carlo or simulation evaluation | screen | Study design is an eligibility criterion and may not be consistently indexed. |
| Social/behavioural sciences | screen | Disciplinary scope is screened from the record and full text. |
| Performance, accuracy, bias | screen | Outcome terms are variably reported and are not required retrieval concepts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:11:29+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,021
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Models, Psychological"[Mesh]` | 43,468 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 5 | `"structural equation model"[tiab]` | 1,934 | none |
| 6 | `"structural equation models"[tiab]` | 1,695 | none |
| 7 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 8 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 9 | `SEM[tiab]` | 81,594 | none |
| 10 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 11 | `CFA[tiab]` | 7,128 | none |
| 12 | `"factor analysis"[tiab]` | 33,735 | none |
| 13 | `"latent variable"[tiab]` | 2,007 | none |
| 14 | `"latent variables"[tiab]` | 1,525 | none |
| 15 | `"latent variable model"[tiab]` | 253 | none |
| 16 | `"latent variable models"[tiab]` | 277 | none |
| 17 | `"latent growth"[tiab]` | 1,734 | none |
| 18 | `"growth curve model"[tiab]` | 270 | none |
| 19 | `"growth mixture model"[tiab]` | 95 | none |
| 20 | `"latent class"[tiab]` | 4,129 | none |
| 21 | `"latent class model"[tiab]` | 304 | none |
| 22 | `multilevel[tiab]` | 25,930 | none |
| 23 | `"multi-level"[tiab]` | 4,831 | none |
| 24 | `mediation[tiab]` | 22,917 | none |
| 25 | `"indirect effect"[tiab]` | 5,281 | none |
| 26 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 240,606 | none |
| 27 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 28 | `Bayesian[tiab]` | 35,533 | none |
| 29 | `Bayes[tiab]` | 5,705 | none |
| 30 | `"Bayesian estimation"[tiab]` | 966 | none |
| 31 | `"Bayesian approach"[tiab]` | 3,278 | none |
| 32 | `"Bayesian method"[tiab]` | 1,320 | none |
| 33 | `"Bayesian analysis"[tiab]` | 2,540 | none |
| 34 | `MCMC[tiab]` | 1,577 | none |
| 35 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 36 | `#27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35` | 47,661 | none |
| 37 | `#26 AND #36` | 2,021 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Models, Psychological"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Latent Class Analysis"[Mesh] OR "structural equation model"[tiab] OR "structural equation models"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR SEM[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "factor analysis"[tiab] OR "latent variable"[tiab] OR "latent variables"[tiab] OR "latent variable model"[tiab] OR "latent variable models"[tiab] OR "latent growth"[tiab] OR "growth curve model"[tiab] OR "growth mixture model"[tiab] OR "latent class"[tiab] OR "latent class model"[tiab] OR multilevel[tiab] OR "multi-level"[tiab] OR mediation[tiab] OR "indirect effect"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian approach"[tiab] OR "Bayesian method"[tiab] OR "Bayesian analysis"[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 47,661 | 0 |
| bayesian | 240,606 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,021 | initial | none | Initial strategy, two concepts |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 0 findings; 
- Round 2 on version 1: 1 findings; R2-LF1 must-fix open
- Round 3 on version 1: 1 findings; R2-LF1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 484 NCBI requests logged (173 from cache); strategy sha256 4b4da8f41077._

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
      "checked_at": "2026-10-02T14:11:29+00:00",
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
      "requested": "Models, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:11:29+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008960",
          "name": "Models, Psychological",
          "type": "descriptor",
          "scope_note": "Theoretical representations that simulate psychological processes and/or social processes. These include the use of mathematical equations, computers, and other electronic equipment.",
          "tree_numbers": [
            "E05.599.695"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008960",
      "preferred_label": "Models, Psychological",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Models, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:11:29+00:00",
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
      "requested": "Latent Class Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:11:29+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Latent Class Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:11:29+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"models, psychological\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"structural equation model\"[Title/Abstract] OR \"structural equation models\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable\"[Title/Abstract] OR \"latent variables\"[Title/Abstract] OR \"latent variable model\"[Title/Abstract] OR \"latent variable models\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model\"[Title/Abstract] OR \"growth mixture model\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"latent class model\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"multi-level\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"indirect effect\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"Bayesian approach\"[Title/Abstract] OR \"Bayesian method\"[Title/Abstract] OR \"Bayesian analysis\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "dfbf029e734ba96fe95a53ca2b12d08b781c5ea695e6e1c47d3a0db1b5435145",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues or PubMed warnings. The SEM-family block includes the eligibility-named members in their own terms, including CFA, latent growth, latent class, multilevel, and mediation."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searchable concepts are combined with AND, and synonyms within each block with OR. Screening-only concepts remain outside the query, consistent with the stated rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected headings are verified in the packet. They are supplemented by title/abstract terms for SEM-family models and Bayesian estimation."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word set includes SEM/CFA, model-family terminology, and Bayesian/MCMC terminology, with spelling and singular/plural variants where shown. The broad SEM abbreviation may add noise, but the reported result set is finite and the packet provides no evidence of a recall problem."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The numbered lines and final Boolean query are syntactically consistent in the packet, and the final query has no reported errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No methodological or disciplinary filters are applied; those criteria are explicitly assigned to screening. The Entrez-date bound is documented as an as-of bound, not a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 1,
      "review_sha256": "dfbf029e734ba96fe95a53ca2b12d08b781c5ea695e6e1c47d3a0db1b5435145",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility-named model members are represented by their own terms, including CFA, latent growth, latent class, multilevel, and mediation. No phrase warnings or proximity operators are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are combined with OR within the model and Bayesian blocks, and the blocks are combined with AND. Screening-only concepts remain outside the query as documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified and are supplemented with title/abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover SEM and named model-family members alongside Bayesian and MCMC terminology. The broad abbreviations may add noise, but the packet shows no evidence of a recall problem."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The numbered searches and final Boolean query are consistent, with no reported translation issues, errors, or warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The Entrez-date bound ends on 2017-11-29, while the question and eligibility state no historical cutoff. Describing it as an as-of bound does not establish that this cutoff matches the requested scope."
        }
      },
      "findings": [
        {
          "id": "R2-LF1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez-date cutoff of 2017-11-29 despite no temporal restriction in the question or eligibility. This excludes later records from retrieval.",
          "recommendation": "Remove the Entrez-date bound, or establish and document a scope cutoff before retaining it; then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 1,
      "review_sha256": "f0a8b59eec94a37255f666fe4ecba43d57782745f419795a94a0767915cf02ee",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No translation issues or PubMed warnings are reported. The model-family block includes the eligibility-named members as bare terms, including mediation."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are combined with OR within each block, and the model-family and Bayesian blocks are combined with AND. Screening-only concepts remain outside the query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the selected MeSH headings as verified and supplements them with title and abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover SEM and named model-family members alongside Bayesian and MCMC terminology. The packet shows no evidence of a recall problem."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The numbered searches and final Boolean query are consistent, with no reported translation issues, errors, or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date bound is documented as a task-harness-required as-of limit through 2017-11-29, rather than a publication-date filter. No other methodological or disciplinary filters are applied."
        }
      },
      "findings": [
        {
          "id": "R2-LF1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez-date cutoff of 2017-11-29 despite no temporal restriction in the question or eligibility. This excludes later records from retrieval.",
          "recommendation": "Remove the Entrez-date bound, or establish and document a scope cutoff before retaining it; then rerun the complete evaluation.",
          "status": "rejected",
          "response": "The packet documents that the task harness explicitly requires an Entrez entry-date bound through 2017-11-29 and forbids records added afterward. It also clarifies that this is not a publication-date limit. The bound therefore follows the stated task constraint."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


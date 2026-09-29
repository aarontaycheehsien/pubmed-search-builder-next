# PubMed search strategy: audit

Generated 2026-09-29T04:09:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task
- Scope confirmed by user: yes (User asked to proceed without clarification; assumptions recorded. PubMed Entrez-date cutoff 2017-11-29 is applied through PSB_AS_OF and protocol as_of; no publication-date limit. No known relevant records were supplied. Comparator, performance outcome, and social/behavioural field are screening criteria. Small-sample context and simulation design will be tested as optional blocks.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family (including CFA, latent growth/class, multilevel, mediation) | search | The model family defines the method-performance topic; family members can be named without saying structural equation model, so the block must include member terms and be probed. |
| Bayesian estimation/inference | search | Bayesian estimation is the focal estimator and should be explicitly named in searchable records. |
| Small-sample or few-cluster estimation context | optional | It defines the context, but sample size may be reported inconsistently and must be tested before AND-ing. |
| Monte Carlo or simulation evaluation | optional | Simulation is an eligibility design and may be named, but design terminology can be inconsistent; test retrieval impact before AND-ing. |
| Frequentist/maximum-likelihood comparator | screen | Comparators may not be named in titles or abstracts; screen for comparative evaluation. |
| Estimator performance, accuracy, bias | screen | Outcomes are variable and not required terms in abstracts. |
| Social/behavioural sciences methodological publication | screen | Field and peer-review status are screening criteria, not reliable PubMed search concepts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T04:08:37+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,337
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Latent Class Analysis[Mesh]` | 81 | none |
| 2 | `Factor Analysis, Statistical[Mesh]` | 25,757 | none |
| 3 | `Multilevel Analysis[Mesh]` | 1,470 | none |
| 4 | `structural equation model*[tiab]` | 12,605 | none |
| 5 | `structural equation modeling[tiab]` | 7,913 | none |
| 6 | `structural equation modelling[tiab]` | 1,788 | none |
| 7 | `"latent variable"[tiab:~1]` | 2,135 | none |
| 8 | `"latent variables"[tiab:~1]` | 1,663 | none |
| 9 | `"factor analysis"[tiab]` | 33,735 | none |
| 10 | `"factor analyses"[tiab]` | 5,979 | none |
| 11 | `confirmatory factor analys*[tiab]` | 10,281 | none |
| 12 | `CFA[tiab]` | 7,128 | none |
| 13 | `"latent growth"[tiab:~1]` | 2,685 | none |
| 14 | `growth curve model*[tiab]` | 1,502 | none |
| 15 | `"latent class"[tiab:~1]` | 4,163 | none |
| 16 | `class growth model*[tiab]` | 115 | none |
| 17 | `multilevel[tiab]` | 25,930 | none |
| 18 | `mediation[tiab]` | 22,917 | none |
| 19 | `indirect effect*[tiab]` | 12,817 | none |
| 20 | `SEM[tiab]` | 81,594 | none |
| 21 | `BSEM[tiab]` | 42 | none |
| 22 | `MSEM[tiab]` | 34 | none |
| 23 | `mediat*[tiab]` | 1,161,571 | none |
| 24 | `item response theory[tiab]` | 2,378 | none |
| 25 | `IRT[tiab]` | 2,417 | none |
| 26 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 1,341,965 | none |
| 27 | `Bayes Theorem[Mesh]` | 28,985 | none |
| 28 | `Bayesian[tiab]` | 35,533 | none |
| 29 | `Bayes[tiab]` | 5,705 | none |
| 30 | `MCMC[tiab]` | 1,577 | none |
| 31 | `Markov chain Monte Carlo[tiab]` | 3,122 | none |
| 32 | `#27 OR #28 OR #29 OR #30 OR #31` | 47,661 | none |
| 33 | `#26 AND #32` | 2,337 | none |

### Strategy (single line, for copying into PubMed)

```text
((Latent Class Analysis[Mesh] OR Factor Analysis, Statistical[Mesh] OR Multilevel Analysis[Mesh] OR structural equation model*[tiab] OR structural equation modeling[tiab] OR structural equation modelling[tiab] OR "latent variable"[tiab:~1] OR "latent variables"[tiab:~1] OR "factor analysis"[tiab] OR "factor analyses"[tiab] OR confirmatory factor analys*[tiab] OR CFA[tiab] OR "latent growth"[tiab:~1] OR growth curve model*[tiab] OR "latent class"[tiab:~1] OR class growth model*[tiab] OR multilevel[tiab] OR mediation[tiab] OR indirect effect*[tiab] OR SEM[tiab] OR BSEM[tiab] OR MSEM[tiab] OR mediat*[tiab] OR item response theory[tiab] OR IRT[tiab]) AND (Bayes Theorem[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR MCMC[tiab] OR Markov chain Monte Carlo[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small-sample or few-cluster estimation context | left out | 2,337 / 83 | 96.4% | 26610033 | 0/29 (up to 10% of removed records could be relevant) | Leave out: a PubMed Entrez-date-bounded loss sample of 30 records found no eligible paper, and the strategy's known-record evaluation shows that eligible PMID 26610033 is lost by this block. Only two known relevant papers are available, below the 15-record threshold for AND-ing. |
| Monte Carlo or simulation evaluation | left out | 2,337 / 675 | 71.1% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out: a PubMed Entrez-date-bounded loss sample of 30 records found no eligible paper, and only two known relevant papers are available, below the 15-record threshold for AND-ing. Simulation remains a screening criterion because the sample-size trade-off paper demonstrates it may not be named using the tested terms. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Structural equation and latent-variable model family (including CFA, latent growth/class, multilevel, mediation) | 1 | `model*[tiab]` | 17,348 | 0/30 |
| Structural equation and latent-variable model family (including CFA, latent growth/class, multilevel, mediation) | 2 | `model*[tiab]` | 23,848 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 47,661 | 0 |
| bayesian | 1,341,965 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad model-family and Bayesian blocks with small-sample and simulation concepts held as optional candidates; based on protocol scope before screening records. |
| 2 | 11,537 | sem_family: +20 / -0; bayesian: +5 / -0 | none | Reformatted blocks as explicit OR terms with MeSH and title/abstract layers; corrected schema after initial structural lint failure. |
| 3 | 1,550 | sem_family: +0 / -1 | none | Removed the generic Models, Statistical MeSH heading after the category probe sample found no eligible member-only record and its explosive breadth drove the query above the 10,000-record standard budget; retained family-specific MeSH and text terms. |
| 4 | 2,337 | sem_family: +6 / -0 | none | Added SEM/BSEM/MSEM acronyms and safe mediat* morphology based on the screened included latent-mediated-effect paper; added item response theory/IRT for latent-variable-family coverage. All are OR terms within the existing family block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; R1-LF1 must-fix open
- Round 2 on version 4: 1 findings; R1-LF1 must-fix resolved
- Round 3 on version 4: 1 findings; R1-LF1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 968 NCBI requests logged (455 from cache); strategy sha256 e31075ff92c5._

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
      "requested": "Latent Class Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T04:08:37+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "Latent Class Analysis",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Factor Analysis, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T04:08:37+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Factor Analysis, Statistical",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T04:08:37+00:00",
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
        "text": "Multilevel Analysis",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T04:08:37+00:00",
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
        "text": "Bayes Theorem",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"latent class analysis\"[MeSH Terms] OR \"factor analysis, statistical\"[MeSH Terms] OR \"multilevel analysis\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"latent variable\"[Title/Abstract:~1] OR \"latent variables\"[Title/Abstract:~1] OR \"factor analysis\"[Title/Abstract] OR \"factor analyses\"[Title/Abstract] OR \"confirmatory factor analys*\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"latent growth\"[Title/Abstract:~1] OR \"growth curve model*\"[Title/Abstract] OR \"latent class\"[Title/Abstract:~1] OR \"class growth model*\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"indirect effect*\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"BSEM\"[Title/Abstract] OR \"MSEM\"[Title/Abstract] OR \"mediat*\"[Title/Abstract] OR \"item response theory\"[Title/Abstract] OR \"IRT\"[Title/Abstract]) AND (\"bayes theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"markov chain monte carlo\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "ba9df99a0f10d84791b3d6edfe400731789fe2074d7b3de50ce37a2c0737956e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The query covers the named model-family members, including bare mediation, and includes Bayesian terms. The packet reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks use OR and are combined with AND. Proximity expressions contain no wildcards, and the packet reports no operator diagnostics."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH headings used are reported as verified. The optional blocks were tested and left out based on known-record evidence and loss sampling."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word block includes explicit expressions for the model families and Bayesian estimation. The category probes found no relevant records outside the model-family block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax errors or warnings and no translation issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The Entrez cutoff is required by the harness and recorded in protocol.as_of; it is not an ad hoc publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "R1-LF1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query includes an Entrez date filter ending 2017/11/29. No such date limit appears in the question, scope, or eligibility criteria, so the strategy as written excludes later records without a stated rationale.",
          "recommendation": "Remove the date restriction unless the protocol explicitly establishes this cutoff, and rerun the complete evaluation because the query changes.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "ba9df99a0f10d84791b3d6edfe400731789fe2074d7b3de50ce37a2c0737956e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched family members named in scope have corresponding terms, including bare mediation. Bayesian terms are present, and the packet reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks use OR internally and AND between required concepts. Proximity expressions have no wildcards, and the packet reports no operator diagnostics."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the MeSH headings as verified. Optional sample-size and simulation blocks were tested and left out; the sample-size decision is also supported by a known relevant record lost."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover the named model families and Bayesian estimation. Both category probes found no relevant records outside the model-family block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax warnings or errors and no translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date cutoff matches the packet's explicit as_of date of 2017-11-29, defining the evaluated record snapshot."
        }
      },
      "findings": [
        {
          "id": "R1-LF1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query has an Entrez date cutoff of 2017-11-29.",
          "recommendation": "Document that the cutoff defines the evaluated snapshot, as indicated by the packet's as_of date.",
          "status": "resolved",
          "response": "The packet records as_of as 2017-11-29, matching the query's Entrez cutoff. The cutoff therefore has a stated snapshot rationale."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "ba9df99a0f10d84791b3d6edfe400731789fe2074d7b3de50ce37a2c0737956e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched model-family members named in scope have corresponding terms, including bare mediation, and Bayesian terms are present. The packet reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks use OR internally and AND between required concepts. Proximity expressions have no wildcards, and the packet reports no operator diagnostics."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH headings are reported as verified. Optional sample-size and simulation blocks were tested and left out; the sample-size decision is supported by a known relevant record lost."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover the named model families and Bayesian estimation. Both category probes found no relevant records outside the model-family block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax warnings or errors and no translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The prior cutoff finding remains resolved: the Entrez date cutoff matches the explicitly recorded as_of date of 2017-11-29, which defines the evaluated record snapshot."
        }
      },
      "findings": [
        {
          "id": "R1-LF1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query includes an Entrez date filter ending 2017/11/29.",
          "recommendation": "Document the cutoff's rationale in the protocol.",
          "status": "resolved",
          "response": "The packet records as_of as 2017-11-29, matching the query's Entrez cutoff. This provides the stated snapshot rationale, and the cutoff remains documented in the protocol notes."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


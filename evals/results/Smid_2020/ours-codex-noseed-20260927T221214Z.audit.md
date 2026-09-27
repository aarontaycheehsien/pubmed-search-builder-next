# PubMed search strategy: audit

Generated 2026-09-27T22:23:32+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in performance, accuracy, and bias?
- Framework: method + application context
- Scope confirmed by user: yes (User explicitly asked to proceed without follow-up. Assumed a recall-first method + application-context search: AND Bayesian estimation with the SEM/latent-variable model family. Screen small-sample/few-cluster context, estimator comparator, performance outcomes, simulation design, discipline, and peer-review status rather than requiring fragile abstract terms. No date/language restrictions beyond the harness Entrez-date bound in as_of; do not add a publication-date limit. No user-supplied seeds; attempt standard-depth PubMed-only discovery without web searching.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable family models | search | The model family defines the application context and is named in titles, abstracts, or MeSH; listed family members such as CFA, latent growth/class, multilevel, and mediation must be searchable by their own names. |
| Bayesian estimation | search | Bayesian estimation is the focal method and is expected to be reliably named or indexed. |
| Small sample or few-cluster estimation context | screen | Small-sample conditions may appear only in methods or simulation details and are inconsistently labeled. |
| Frequentist / maximum-likelihood or alternative estimator comparison | screen | Comparators may not be named in abstracts; screen for direct estimator comparisons. |
| Performance, accuracy, and bias outcomes | screen | Outcome terms are inconsistently reported and should not be required. |
| Monte Carlo or simulation evaluation | screen | Simulation design is an eligibility property, and methods may be described only in full text. |
| Peer-reviewed methodological paper in social/behavioural sciences | screen | Discipline and peer-review status are screened; PubMed's coverage is limited for social/behavioural science methodology. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-27T22:22:51+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,184
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"structural equation model*"[tiab]` | 12,605 | none |
| 5 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 6 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 7 | `"structural equation analysis"[tiab]` | 131 | none |
| 8 | `"path analysis"[tiab]` | 4,075 | none |
| 9 | `SEM[tiab]` | 81,594 | none |
| 10 | `BSEM[tiab]` | 42 | none |
| 11 | `CFA[tiab]` | 7,128 | none |
| 12 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 13 | `"exploratory factor analysis"[tiab]` | 5,306 | none |
| 14 | `"factor analysis"[tiab]` | 33,735 | none |
| 15 | `"latent variable"[tiab]` | 2,007 | none |
| 16 | `"latent class"[tiab]` | 4,129 | none |
| 17 | `"latent growth"[tiab]` | 1,734 | none |
| 18 | `"growth curve"[tiab]` | 6,069 | none |
| 19 | `mediation[tiab]` | 22,917 | none |
| 20 | `multilevel[tiab]` | 25,930 | none |
| 21 | `multi-level[tiab]` | 4,831 | none |
| 22 | `"hierarchical linear model"[tiab]` | 219 | none |
| 23 | `"hierarchical model"[tiab]` | 1,993 | none |
| 24 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23` | 207,349 | none |
| 25 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 26 | `Bayesian[tiab]` | 35,533 | none |
| 27 | `Bayes[tiab]` | 5,705 | none |
| 28 | `"Bayesian estimation"[tiab]` | 966 | none |
| 29 | `"Bayesian approach"[tiab]` | 3,278 | none |
| 30 | `"Bayesian method"[tiab]` | 1,320 | none |
| 31 | `"Bayesian analysis"[tiab]` | 2,540 | none |
| 32 | `"Bayesian inference"[tiab]` | 3,376 | none |
| 33 | `"Bayesian model"[tiab]` | 2,344 | none |
| 34 | `"Bayesian structural equation"[tiab]` | 46 | none |
| 35 | `"Bayesian SEM"[tiab]` | 4 | none |
| 36 | `MCMC[tiab]` | 1,577 | none |
| 37 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 38 | `#25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 47,661 | none |
| 39 | `#24 AND #38` | 2,184 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "structural equation model*"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "structural equation analysis"[tiab] OR "path analysis"[tiab] OR SEM[tiab] OR BSEM[tiab] OR CFA[tiab] OR "confirmatory factor analysis"[tiab] OR "exploratory factor analysis"[tiab] OR "factor analysis"[tiab] OR "latent variable"[tiab] OR "latent class"[tiab] OR "latent growth"[tiab] OR "growth curve"[tiab] OR mediation[tiab] OR multilevel[tiab] OR multi-level[tiab] OR "hierarchical linear model"[tiab] OR "hierarchical model"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian approach"[tiab] OR "Bayesian method"[tiab] OR "Bayesian analysis"[tiab] OR "Bayesian inference"[tiab] OR "Bayesian model"[tiab] OR "Bayesian structural equation"[tiab] OR "Bayesian SEM"[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_models | 47,661 | 0 |
| bayesian | 207,349 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 11,944 | initial | none | First recall-first draft: two required topic blocks, using current verified MeSH layers plus broad SEM-family/Bayesian text terms; small-sample, comparator, simulation, and outcomes remain screening criteria. |
| 2 | 2,164 | sem_models: +0 / -1 | none | Removed the generic Models, Statistical MeSH heading after the first draft's 11,944-record count; it does not name the target model family and may create noise. Test for loss of known records. |
| 3 | 2,184 | sem_models: +1 / -0 | none | Added the critic-requested path analysis[tiab] synonym, which names a common SEM approach; re-evaluate count, known records, and translation. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; R1-1 should-fix open
- Round 2 on version 3: 1 findings; R1-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 388 NCBI requests logged (179 from cache); strategy sha256 9bc7f308b7a7._

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
      "checked_at": "2026-09-27T22:22:51+00:00",
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
      "checked_at": "2026-09-27T22:22:51+00:00",
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
      "checked_at": "2026-09-27T22:22:51+00:00",
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
      "checked_at": "2026-09-27T22:22:51+00:00",
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
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"structural equation analysis\"[Title/Abstract] OR \"path analysis\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"BSEM\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"exploratory factor analysis\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"multi-level\"[Title/Abstract] OR \"hierarchical linear model\"[Title/Abstract] OR \"hierarchical model\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"Bayesian approach\"[Title/Abstract] OR \"Bayesian method\"[Title/Abstract] OR \"Bayesian analysis\"[Title/Abstract] OR \"Bayesian inference\"[Title/Abstract] OR \"Bayesian model\"[Title/Abstract] OR \"Bayesian structural equation\"[Title/Abstract] OR \"Bayesian SEM\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "9bceba3a600cc7ea939c0f7e5f1a9f0bf184c11c96a9fbbbdd0b6fb92251ca",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The listed family members are covered by their own terms, including bare mediation, multilevel, latent growth, and latent class. Add a common SEM synonym such as path analysis for review."
        },
        "operators": {
          "verdict": "pass",
          "note": "The recall-first structure correctly combines the Bayesian and model-family blocks with AND, while leaving screening concepts out of the search."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected headings are verified in the packet and are complemented by text words. No heading-related translation defect is evident from the supplied evidence."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Consider adding path analysis as a common name for structural equation work. Existing family-member terms satisfy the packet's explicit bare-name checks."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors or warnings. The strategy uses no proximity operators or wildcards in proximity."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or other restrictive filter is applied; the entry-date bound is documented as the harness cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The model-family block does not include path analysis, a common name for structural equation model work that may be used without the phrase structural equation or SEM.",
          "recommendation": "Add a tested path analysis[tiab] term, and consider path model* if supported by testing. Re-evaluate the complete strategy after the change.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "e4ca799a387f3494cf7c64b77040b175d1e6f0a358061fe29d3e78ca3b823697",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named model-family members are searchable by their own terms, including bare mediation and multilevel; path analysis is now covered by a tested title/abstract term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Bayesian and model-family blocks are combined with AND, while concepts assigned to screening are not required in the search."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied evidence verifies the selected headings, which are supplemented by title/abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The updated model-family block includes path analysis[tiab]. No additional actionable lexical gap is evident from the packet."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors, warnings, or translation issues. No proximity operators are used."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive publication-date or other eligibility filters are applied. The entry-date bound is documented as the harness cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The model-family block lacked path analysis, a common name for structural equation work.",
          "recommendation": "Add a tested path analysis[tiab] term and re-evaluate the complete strategy.",
          "status": "resolved",
          "response": "The updated strategy adds path analysis[tiab] as line 8 in the model-family block. The complete strategy was re-evaluated; the packet reports no query or translation issues and no known relevant records were lost."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


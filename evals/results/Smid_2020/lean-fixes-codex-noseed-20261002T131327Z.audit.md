# PubMed search strategy: audit

Generated 2026-10-02T13:34:20+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method-performance
- Scope confirmed by user: yes (Proceeding without clarification as requested. No known relevant articles were supplied. Entrez-date cutoff is 2017-11-29 (PSB_AS_OF); no publication-date limit is applied. Standard-depth discovery and screening will be attempted; if no relevant benchmark records can be identified, empirical recall remains unestimated.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Bayesian estimation | search | The estimation approach being evaluated is central and is reliably named in methodological records. |
| Structural equation and latent-variable models | search | The model family defines the task; named members in the eligibility criteria (CFA, latent growth/class, multilevel, mediation) are included by their own terms. |
| Small sample or few-cluster context | screen | Sample-size context can be reported only in methods/full text and is inconsistently indexed. |
| Frequentist or maximum-likelihood comparison | screen | Comparator terms are not consistently stated in titles/abstracts. |
| Monte Carlo or simulation evaluation | screen | Study design is an eligibility feature; an ad hoc design block could lose relevant records. |
| Performance, accuracy, and bias outcomes | screen | Outcome measures are variably named and belong at screening. |
| Peer-reviewed social/behavioural methodological paper | screen | Field, peer-review status, and methodological contribution require screening rather than a narrow database block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:33:27+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 13,861
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 2 | `Bayesian[tiab]` | 35,533 | none |
| 3 | `Bayes[tiab]` | 5,705 | none |
| 4 | `prior[tiab]` | 494,787 | none |
| 5 | `"prior distribution"[tiab]` | 661 | none |
| 6 | `"prior distributions"[tiab]` | 568 | none |
| 7 | `MCMC[tiab]` | 1,577 | none |
| 8 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 537,417 | none |
| 10 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 11 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 12 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 13 | `"Mediation Analysis"[Mesh]` | 1 | none |
| 14 | `"Models, Psychological"[Mesh]` | 43,468 | none |
| 15 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 16 | `"structural equation model"[tiab]` | 1,934 | none |
| 17 | `"structural equation models"[tiab]` | 1,695 | none |
| 18 | `SEM[tiab]` | 81,594 | none |
| 19 | `"latent variable"[tiab]` | 2,007 | none |
| 20 | `"latent variables"[tiab]` | 1,525 | none |
| 21 | `"latent variable model"[tiab]` | 253 | none |
| 22 | `"latent variable models"[tiab]` | 277 | none |
| 23 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 24 | `CFA[tiab]` | 7,128 | none |
| 25 | `"factor analysis"[tiab]` | 33,735 | none |
| 26 | `"factor model"[tiab]` | 5,552 | none |
| 27 | `"factor models"[tiab]` | 1,000 | none |
| 28 | `"latent growth"[tiab]` | 1,734 | none |
| 29 | `"growth curve model"[tiab]` | 270 | none |
| 30 | `"growth curve models"[tiab]` | 584 | none |
| 31 | `"latent class"[tiab]` | 4,129 | none |
| 32 | `multilevel[tiab]` | 25,930 | none |
| 33 | `multi-level[tiab]` | 4,831 | none |
| 34 | `hierarchical[tiab]` | 51,718 | none |
| 35 | `mediation[tiab]` | 22,917 | none |
| 36 | `"mediation analysis"[tiab]` | 1,822 | none |
| 37 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36` | 285,800 | none |
| 38 | `#9 AND #37` | 13,861 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR prior[tiab] OR "prior distribution"[tiab] OR "prior distributions"[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab]) AND ("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Mediation Analysis"[Mesh] OR "Models, Psychological"[Mesh] OR "structural equation modeling"[tiab] OR "structural equation model"[tiab] OR "structural equation models"[tiab] OR SEM[tiab] OR "latent variable"[tiab] OR "latent variables"[tiab] OR "latent variable model"[tiab] OR "latent variable models"[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "factor analysis"[tiab] OR "factor model"[tiab] OR "factor models"[tiab] OR "latent growth"[tiab] OR "growth curve model"[tiab] OR "growth curve models"[tiab] OR "latent class"[tiab] OR multilevel[tiab] OR multi-level[tiab] OR hierarchical[tiab] OR mediation[tiab] OR "mediation analysis"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bayesian_estimation | 285,800 | 0 |
| sem_models | 537,417 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 11,520 | initial | none | Initial two-block recall-first draft: Bayesian estimation AND SEM/latent-variable family. Screening-only criteria were deliberately not AND-ed. Added MeSH and free-text vocabulary from authority lookup and four screened relevant pilot records. |
| 2 | 5,231 | sem_models: +2 / -1 | none | Replaced the generic Models, Statistical heading after its Bayesian intersection alone returned 10,475 records, with the directly relevant Models, Psychological heading observed among a screened relevant record; added hierarchical wording for multilevel variants. Checked whether the four relevant examples remain retrieved. |
| 3 | 13,861 | bayesian_estimation: +1 / -0 | none | Added prior[tiab] to the Bayesian block because the eligibility criteria explicitly include estimation using prior distributions, and some records may report prior use without using the word Bayesian. All four development records should remain covered. |
| 4 | 5,250 | bayesian_estimation: +2 / -1 | none | Replaced prior[tiab], which raised the result count from 5,231 to 13,861, with the eligibility-specific phrases 'prior distribution(s)'[tiab] to retain the concept while reducing unrelated uses of the word prior. |
| 5 | 13,861 | bayesian_estimation: +1 / -0 | none | Restored prior[tiab] after critic round 1 requested testing. It adds broad retrieval; the diagnostic sample showed substantial noise, but the generic cue is retained for recall-first coverage of records describing priors without the exact phrase prior distribution(s). The resulting screening burden is documented. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; R1-F1 should-fix open
- Round 2 on version 5: 1 findings; R1-F1 should-fix resolved
- Round 3 on version 5: 1 findings; R1-F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 557 NCBI requests logged (319 from cache); strategy sha256 8cbe5bc83e4f._

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
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:33:27+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Factor Analysis, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:33:27+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Factor Analysis, Statistical\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Latent Class Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:33:27+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Latent Class Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:33:27+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Multilevel Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mediation Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:33:27+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000081983",
          "name": "Mediation Analysis",
          "type": "descriptor",
          "scope_note": "A type of statistical analysis used to understand, clarify, and explain the relationship and pathway between a presumed cause (an independent variable) and effect (dependent variable) with respect to causal links (mediating variables) and/or to analyze the effect of an intervention (mediating factor/variable) on an outcome.",
          "tree_numbers": [
            "E05.318.740.400.500",
            "N05.715.360.750.350.500",
            "N06.850.520.830.400.500"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000081983",
      "preferred_label": "Mediation Analysis",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Mediation Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Models, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:33:27+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Models, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"prior\"[Title/Abstract] OR \"prior distribution\"[Title/Abstract] OR \"prior distributions\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract]) AND (\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"Mediation Analysis\"[MeSH Terms] OR \"models, psychological\"[MeSH Terms] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation model\"[Title/Abstract] OR \"structural equation models\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"latent variable\"[Title/Abstract] OR \"latent variables\"[Title/Abstract] OR \"latent variable model\"[Title/Abstract] OR \"latent variable models\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"factor model\"[Title/Abstract] OR \"factor models\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model\"[Title/Abstract] OR \"growth curve models\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"multi-level\"[Title/Abstract] OR \"hierarchical\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"Mediation Analysis\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "8ec759794cb7316577e243300f61b700c729a65bf485af4258c74caf3bc02cf8",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched model-family block covers the named members CFA, latent growth/class, multilevel, and mediation with their own terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Bayesian and model-family blocks are combined with OR internally and AND between concepts; the query is balanced and parenthesized."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified, and the record shows no mapping or translation issues."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Version 4 removed prior[tiab] and added only the exact phrases prior distribution and prior distributions. The packet provides no evidence that the broader wording is dispensable; full seed retrieval does not establish that."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed translation has no errors or warnings, and the combined query is syntactically coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff is explicit and consistently applied; no unexplained limits or narrow design filters are present."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The revision removed prior[tiab], replacing it with two exact phrases. Relevant records may describe prior choices or prior information without using the exact phrase prior distribution(s); the packet does not show a tested comparison supporting this removal.",
          "recommendation": "Restore prior[tiab] or test and document an alternative set of prior-related terms against a complete evaluation, including retrieval and precision consequences.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "43eefd39bbb609dd92e8f0167de2da6ade35258ea6e341c4e8c2326bb2ed822a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Each named model-family member is represented by its own bare term: CFA, latent growth/class, multilevel, and mediation."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each concept block and the Bayesian and model-family blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified, with no mapping or translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Version 5 restores prior[tiab], resolving R1-F1. Its broad count (494,787) is documented; the term's contribution should be monitored during screening."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed translation reports no errors or warnings, and the combined query is coherently parenthesized."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff is explicit and consistently applied, with no publication-date limit or unexplained search filter."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Version 4 removed prior[tiab], replacing it with exact phrases without evidence that broader wording was dispensable.",
          "recommendation": "Restore prior[tiab] or test and document an alternative against a complete evaluation.",
          "status": "resolved",
          "response": "Version 5 restores prior[tiab]. The term has a reported count of 494,787; a random-offset sample of its SEM-family intersection showed substantial noise, but this evidence does not establish the broad term is dispensable in a recall-first search. The wider screening burden is documented."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "43eefd39bbb609dd92e8f0167de2da6ade35258ea6e341c4e8c2326bb2ed822a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The model-family block includes the named members CFA, latent growth/class, multilevel, and mediation by their own terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each concept block, and the Bayesian and model-family blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified, with no mapping or translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Version 5 restores prior[tiab], addressing R1-F1. Its broad count and screening burden are documented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed translation reports no errors or warnings, and the combined query is coherently parenthesized."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff is explicit and consistently applied; no publication-date limit or unexplained filter is present."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier version removed prior[tiab], replacing it with exact phrases without evidence that broader wording was dispensable.",
          "recommendation": "Restore prior[tiab] or test and document an alternative against a complete evaluation.",
          "status": "resolved",
          "response": "Version 5 restores prior[tiab]. Its reported count is 494,787. A random-offset sample of its SEM-family intersection showed substantial noise, but this does not establish the broad term is dispensable in a recall-first search; the wider screening burden is documented."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


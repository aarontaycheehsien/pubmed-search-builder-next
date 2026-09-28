# PubMed search strategy: audit

Generated 2026-09-27T21:58:39+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method performance
- Scope confirmed by user: no (User asked to proceed without clarification. Scope roles and screening interpretation are provisional operational assumptions. Harness cutoff is PubMed as of 2017-11-29; no query publication-date limit is to be added. No known relevant articles supplied. No web search used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family (including CFA, latent growth/class, multilevel, and mediation) | search | The target model family defines the topic and must be present in every eligible study. Named family members are included by their own terms to avoid requiring authors to label them SEM. |
| Bayesian estimation | search | Bayesian estimation is the method being evaluated and must be present in every eligible study. |
| Small samples or few clusters | screen | Sample-size context can be implicit, reported only in methods/full text, and expressed inconsistently. |
| Comparison with frequentist or maximum-likelihood estimation | screen | Comparators are inconsistently described in abstracts; do not require comparator terms as a block. |
| Monte Carlo or simulation evaluation | screen | Study design terminology is not reliably indexed and may be absent from titles/abstracts. |
| Peer-reviewed social/behavioural-science methodological paper | screen | Field, peer-review status, and methodological contribution are eligibility properties best judged during screening. |
| Estimator performance, accuracy, and bias | screen | Performance outcomes are not reliable retrieval concepts and are assessed at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-27T21:58:07+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 1,430
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 3 | `"structural equation"[tiab]` | 12,948 | none |
| 4 | `"structural equation model"[tiab:~1]` | 2,080 | none |
| 5 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 6 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 7 | `SEM[tiab]` | 81,594 | none |
| 8 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 9 | `CFA[tiab]` | 7,128 | none |
| 10 | `"latent variable"[tiab]` | 2,007 | none |
| 11 | `"latent growth"[tiab]` | 1,734 | none |
| 12 | `"growth curve"[tiab]` | 6,069 | none |
| 13 | `"growth mixture"[tiab]` | 791 | none |
| 14 | `"latent class"[tiab]` | 4,129 | none |
| 15 | `multilevel[tiab]` | 25,930 | none |
| 16 | `"hierarchical linear model"[tiab:~1]` | 391 | none |
| 17 | `mediation[tiab]` | 22,917 | none |
| 18 | `"indirect effect"[tiab]` | 5,281 | none |
| 19 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18` | 190,121 | none |
| 20 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 21 | `Bayesian[tiab]` | 35,533 | none |
| 22 | `Bayes[tiab]` | 5,705 | none |
| 23 | `"Bayesian estimation"[tiab]` | 966 | none |
| 24 | `"Bayesian method"[tiab]` | 1,320 | none |
| 25 | `"Bayesian approach"[tiab]` | 3,278 | none |
| 26 | `MCMC[tiab]` | 1,577 | none |
| 27 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 28 | `"Gibbs sampling"[tiab]` | 712 | none |
| 29 | `"prior distribution"[tiab]` | 661 | none |
| 30 | `#20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 48,058 | none |
| 31 | `#19 AND #30` | 1,430 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Multilevel Analysis"[Mesh] OR "structural equation"[tiab] OR "structural equation model"[tiab:~1] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR SEM[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "latent variable"[tiab] OR "latent growth"[tiab] OR "growth curve"[tiab] OR "growth mixture"[tiab] OR "latent class"[tiab] OR multilevel[tiab] OR "hierarchical linear model"[tiab:~1] OR mediation[tiab] OR "indirect effect"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian method"[tiab] OR "Bayesian approach"[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "Gibbs sampling"[tiab] OR "prior distribution"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 48,058 | 0 |
| bayesian_estimation | 190,121 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 11,518 | initial | none | Initial recall-first two-block strategy; searched Bayesian estimation AND the broad named SEM/latent-variable family, with sample size, comparator, simulation design, outcomes and field screened. |
| 2 | 1,430 | sem_family: +0 / -1 | none | Removed the generic Models, Statistical MeSH heading after a random sample of the broad query showed substantial unrelated statistical-model noise. Kept the specific factor-analysis and multilevel headings and text terms; the development records contain specific title/abstract wording. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 502 NCBI requests logged (208 from cache); strategy sha256 a92f58c217d6._

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
      "checked_at": "2026-09-27T21:58:07+00:00",
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
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T21:58:07+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Multilevel Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T21:58:07+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"structural equation\"[Title/Abstract] OR \"structural equation model\"[Title/Abstract:~1] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"latent variable\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve\"[Title/Abstract] OR \"growth mixture\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"hierarchical linear model\"[Title/Abstract:~1] OR \"mediation\"[Title/Abstract] OR \"indirect effect\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"Bayesian method\"[Title/Abstract] OR \"Bayesian approach\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"Gibbs sampling\"[Title/Abstract] OR \"prior distribution\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "4a1aeb13078365e7f9c1ce049a963915dd5d64f6390e68997a290b91003ca524",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both required concepts are searched, with the SEM family and Bayesian estimation joined by AND. The named family members are represented by their own terms, including bare mediation, CFA, latent growth/class, multilevel, and factor-analysis terms; no listed member is covered only by a phrase narrowed to its parent."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each concept and AND combines the two required concepts. Small-sample context, comparison approach, simulation, field, and performance outcomes remain screening criteria as scoped."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Factor Analysis, Statistical; Multilevel Analysis; and Bayes Theorem headings are used as supplementary retrieval terms. Text-word alternatives also cover the searched concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The title/abstract terms include spelling variants and named model-family members. The three known relevant records are retrieved, though they were development records rather than an independent validation set."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query is grouped correctly and its PubMed translations report no errors or warnings. The two ~1 expressions are explicit proximity searches; PubMed proximity permits either order, and no wildcards are used within them."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit or other restrictive filter is added. The 1800/01/01–2017/11/29 entry-date range implements the stated PubMed as-of cutoff."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "16308ad55d4e19116bbe52622e6419b6322447c7a8384da66163a79625db94e1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both required search concepts are represented and joined with AND. The named model-family members have their own terms, including bare mediation, CFA, latent growth/class, and multilevel. The screening criteria remain outside the search blocks as scoped."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines alternatives within each concept and AND combines the two required concepts. Small-sample context, comparator, simulation, field, peer-review status, and outcomes remain screening criteria, consistent with the protocol."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Factor Analysis, Statistical; Multilevel Analysis; and Bayes Theorem headings. They supplement text-word alternatives for the searched concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The title/abstract terms cover the named model-family members and Bayesian estimation vocabulary. All three known relevant records were retrieved, but they are development records, so this does not establish independent validation or sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is grouped correctly, and the packet reports no translation errors or warnings. Clause-specific review of both proximity expressions is acceptable: structural equation model and hierarchical linear model permit either word order, which broadens each phrase while retaining its intended model-family meaning. Neither uses wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date range implements the stated PubMed as-of cutoff of 2017-11-29. No publication-date or other restrictive filter is added."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


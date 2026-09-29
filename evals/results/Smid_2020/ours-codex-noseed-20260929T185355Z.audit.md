# PubMed search strategy: audit

Generated 2026-09-29T19:12:24+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method-performance
- Scope confirmed by user: no (User has no known relevant articles and explicitly asked not to wait for questions; the scope is an operational assumption, not user-confirmed. Scope chosen from the question before discovery. PubMed Entrez-date cutoff is 2017-11-29, enforced via PSB_AS_OF on every command; no publication-date limit is used. No language or publication-date limits. Standard depth. Three screened development records came from precise pilot searches. Recall is not independently validated; no prior review or external benchmark was found.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family | search | The model type defines the method-performance topic and is named in titles/abstracts/indexing; includes SEM, CFA, latent growth/class, multilevel, and mediation members, searched by bare names. |
| Bayesian estimation | search | The estimation approach defines the comparison and is commonly named/indexed. |
| Small samples or few clusters | optional | Topic-defining context that may be named in searchable title/abstract language but is not reliable enough to require; test it as an optional block before deciding. |
| Frequentist or maximum-likelihood comparison | screen | Comparator terms are variably reported and unnecessary as an AND block; verify at screening. |
| Monte Carlo or simulation evaluation | screen | Study design is handled at screening; no ad hoc design filter. |
| Social/behavioural sciences and peer-reviewed methods paper | screen | Field and publication status are not reliably searchable as required concepts; screen records. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T19:11:40+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 4,869
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 2 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"Mediation Analysis"[Mesh]` | 1 | none |
| 5 | `"structural equation model*"[tiab]` | 12,605 | none |
| 6 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 7 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 8 | `SEM[tiab]` | 81,594 | none |
| 9 | `"latent variable*"[tiab]` | 3,233 | none |
| 10 | `"confirmatory factor analys*"[tiab]` | 10,281 | none |
| 11 | `CFA[tiab]` | 7,128 | none |
| 12 | `"factor analys*"[tiab]` | 38,459 | none |
| 13 | `"latent class analys*"[tiab]` | 2,675 | none |
| 14 | `"latent class model*"[tiab]` | 603 | none |
| 15 | `"latent growth"[tiab]` | 1,734 | none |
| 16 | `"growth curve model*"[tiab]` | 1,502 | none |
| 17 | `"growth mixture model*"[tiab]` | 768 | none |
| 18 | `multilevel[tiab]` | 25,930 | none |
| 19 | `"multi-level"[tiab]` | 4,831 | none |
| 20 | `hierarchical[tiab]` | 51,718 | none |
| 21 | `mediation[tiab]` | 22,917 | none |
| 22 | `"indirect effect*"[tiab]` | 12,817 | none |
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 259,858 | none |
| 24 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 25 | `Bayesian[tiab]` | 35,533 | none |
| 26 | `Bayes[tiab]` | 5,705 | none |
| 27 | `"Bayesian estimation"[tiab]` | 966 | none |
| 28 | `"Bayesian estimat*"[tiab]` | 1,379 | none |
| 29 | `"Bayesian approach*"[tiab]` | 3,793 | none |
| 30 | `"Bayesian method*"[tiab]` | 3,265 | none |
| 31 | `"Bayesian analys*"[tiab]` | 3,354 | none |
| 32 | `"Bayesian structural equation"[tiab]` | 46 | none |
| 33 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 34 | `MCMC[tiab]` | 1,577 | none |
| 35 | `"prior distribution*"[tiab]` | 1,143 | none |
| 36 | `"posterior distribution*"[tiab]` | 1,486 | none |
| 37 | `"Gibbs sampling"[tiab]` | 712 | none |
| 38 | `WinBUGS[tiab]` | 295 | none |
| 39 | `BUGS[tiab]` | 3,177 | none |
| 40 | `#24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 51,482 | none |
| 41 | `#23 AND #40` | 4,869 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Latent Class Analysis"[Mesh] OR "Factor Analysis, Statistical"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Mediation Analysis"[Mesh] OR "structural equation model*"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR SEM[tiab] OR "latent variable*"[tiab] OR "confirmatory factor analys*"[tiab] OR CFA[tiab] OR "factor analys*"[tiab] OR "latent class analys*"[tiab] OR "latent class model*"[tiab] OR "latent growth"[tiab] OR "growth curve model*"[tiab] OR "growth mixture model*"[tiab] OR multilevel[tiab] OR "multi-level"[tiab] OR hierarchical[tiab] OR mediation[tiab] OR "indirect effect*"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian estimat*"[tiab] OR "Bayesian approach*"[tiab] OR "Bayesian method*"[tiab] OR "Bayesian analys*"[tiab] OR "Bayesian structural equation"[tiab] OR "Markov chain Monte Carlo"[tiab] OR MCMC[tiab] OR "prior distribution*"[tiab] OR "posterior distribution*"[tiab] OR "Gibbs sampling"[tiab] OR WinBUGS[tiab] OR BUGS[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Small samples or few clusters | left out | 4,869 / 157 | 96.8% | none | 0/30 (up to 10% of removed records could be relevant) | The loss sample had 0/30 eligible records and all three known relevant records are retrieved, but only 3 known records sit in the base strategy, below the 15-record evidence threshold required to AND this optional block. The large reduction is not sufficient evidence that it is safe; retain small-sample context for screening. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_models | 51,482 | 0 |
| bayesian | 259,858 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block strategy from question-defined scope; MeSH and broad title/abstract terms for SEM/latent-variable family and Bayesian estimation. No seeds; use 2017-11-29 PubMed entry-date cutoff. |
| 2 | 4,869 | limits/combination | none | Added a measured optional small-sample/few-cluster block because this is the topic-defining context; strategy otherwise unchanged. Three screened relevant pilot records form a development set; no independent validation set. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; R1-F1 must-fix rejected
- Round 2 on version 2: 1 findings; R1-F1 must-fix rejected
- Round 3 on version 2: 1 findings; R1-F1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 636 NCBI requests logged (357 from cache); strategy sha256 00eabab9e07c._

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
      "checked_at": "2026-09-29T19:11:40+00:00",
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
        "text": "\"Latent Class Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Factor Analysis, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:11:40+00:00",
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
        "text": "\"Factor Analysis, Statistical\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:11:40+00:00",
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
      "requested": "Mediation Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:11:40+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Mediation Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:11:40+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Latent Class Analysis\"[MeSH Terms] OR \"factor analysis, statistical\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"Mediation Analysis\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"latent variable*\"[Title/Abstract] OR \"confirmatory factor analys*\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"factor analys*\"[Title/Abstract] OR \"latent class analys*\"[Title/Abstract] OR \"latent class model*\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model*\"[Title/Abstract] OR \"growth mixture model*\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"multi-level\"[Title/Abstract] OR \"hierarchical\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"indirect effect*\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"bayesian estimat*\"[Title/Abstract] OR \"bayesian approach*\"[Title/Abstract] OR \"bayesian method*\"[Title/Abstract] OR \"bayesian analys*\"[Title/Abstract] OR \"Bayesian structural equation\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"prior distribution*\"[Title/Abstract] OR \"posterior distribution*\"[Title/Abstract] OR \"Gibbs sampling\"[Title/Abstract] OR \"WinBUGS\"[Title/Abstract] OR \"BUGS\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "fb4f3b6b1b2a64891b3bc551976d08960d108bd2f9946580760aed71a2eb1677",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched model-family terms cover the named members, including bare mediation and multilevel terms. The Bayesian block has broad free-text coverage, and the query translation reports no issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each concept block, and AND combines the model-family and Bayesian blocks. Comparator and simulation requirements remain for screening as scoped."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet records the selected MeSH headings as verified, and their translations show them applied as MeSH terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover structural equation models and named latent-variable family members, alongside Bayesian and estimation-related vocabulary. No phrase warning is reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has no reported lint, translation, or PubMed diagnostics issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The packet's Entrez-date cutoff is required by the user's harness scenario, which explicitly asks us to work as of 2017-11-29 and says PSB_AS_OF pins PubMed to that date. It is an entry-date boundary, not a publication-date eligibility limit."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query limits records to an Entrez date through 2017-11-29. This excludes later records despite no temporal restriction in the question or eligibility criteria, and the packet does not explain the cutoff.",
          "recommendation": "Remove the Entrez date limit, or document a justified temporal boundary if one was intended. Rerun the complete evaluation after changing the query.",
          "status": "rejected",
          "response": "Rejected because the user-provided harness explicitly requires simulating PubMed as of 2017-11-29, pins every PubMed command through PSB_AS_OF, and specifically forbids a publication-date cutoff because it would incorrectly drop records already in PubMed. protocol.json records that rationale; the generated query uses the Entrez entry-date bound [edat], as required. Removing it would violate the task instructions and admit records beyond the requested historical cutoff."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "fb4f3b6b1b2a64891b3bc551976d08960d108bd2f9946580760aed71a2eb1677",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The model-family block covers the named members with bare terms, including mediation and multilevel. The Bayesian block has broad text-word coverage. No phrase warnings or translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each block, and AND combines the model-family and Bayesian blocks. Comparator, small-sample context, simulation design, field, and publication status remain screening criteria as scoped."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected MeSH headings are translated as MeSH terms, with no reported heading or translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover structural equation models and the named model-family members, plus Bayesian estimation and related methods. The optional small-sample block was assessed and left out with a documented rationale."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has no reported lint, translation, or PubMed diagnostic issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date boundary through 2017-11-29 implements the documented as-of date. No publication-date or language limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query limits records to an Entrez date through 2017-11-29. This excludes later records despite no temporal restriction in the question or eligibility criteria, and the packet does not explain the cutoff.",
          "recommendation": "Remove the Entrez date limit, or document a justified temporal boundary if one was intended. Rerun the complete evaluation after changing the query.",
          "status": "rejected",
          "response": "The packet documents that the search is simulated as of 2017-11-29 and that the Entrez entry-date bound enforces that boundary; it also distinguishes this from a publication-date limit. The rationale supports retaining the bound."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "fb4f3b6b1b2a64891b3bc551976d08960d108bd2f9946580760aed71a2eb1677",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The model-family block includes the named members with bare terms, including mediation and multilevel. The Bayesian block has broad free-text coverage; no phrase warnings or translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within concept blocks, and AND combines the model-family and Bayesian blocks. Comparator, small-sample context, simulation design, field, and publication status remain screening criteria as scoped."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected MeSH headings are translated as MeSH terms, with no reported heading or translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover structural equation models and the named model-family members, plus Bayesian estimation and related methods. The optional small-sample block was tested and left out with a documented rationale."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has no reported lint, translation, or PubMed diagnostic issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date boundary through 2017-11-29 implements the documented as-of date. No publication-date or language limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query limits records to an Entrez date through 2017-11-29. This excludes later records despite no temporal restriction in the question or eligibility criteria, and the packet does not explain the cutoff.",
          "recommendation": "Remove the Entrez date limit, or document a justified temporal boundary if one was intended.",
          "status": "rejected",
          "response": "The packet documents that the search is simulated as of 2017-11-29 and that the Entrez entry-date bound enforces that boundary; it also distinguishes this from a publication-date limit. The rationale supports retaining the bound."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


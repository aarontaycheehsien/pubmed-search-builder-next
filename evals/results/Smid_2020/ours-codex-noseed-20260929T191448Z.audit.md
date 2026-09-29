# PubMed search strategy: audit

Generated 2026-09-29T19:37:17+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task + application context
- Scope confirmed by user: no (User supplied the question and eligibility criteria, no seeds, standard depth, and instructed not to pause for clarification. Scope roles are assumed and not user-confirmed. PubMed entry-date retrieval is bounded by PSB_AS_OF=2017-11-29 for every command; no publication-date filter is applied. Comparators, outcomes, publication peer-review status, and social/behavioural-science field will be screened rather than searched. Discovered relevant papers were screened into the development set; no held-out validation set exists. Recall is development relative recall only. The harness-mandated PSB_AS_OF cutoff is an Entrez Entry Date bound, not a review publication-date criterion; no [dp] publication-date restriction is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family (SEM, CFA, latent growth/class, multilevel, mediation) | search | The model family defines the application; each named member must be retrievable on its own terms, and related records may use only a member label. |
| Bayesian estimation (including priors and MCMC) of models | search | Bayesian estimation is the method under study and should be named in titles, abstracts, or indexing; MCMC and prior terms broaden its wording. |
| Small samples or few clusters | optional | This context is required by eligibility and may be named in searchable language, but numeric/sample-size conditions and wording vary; test before deciding whether to AND it. |
| Monte Carlo or simulation evaluation | optional | The design is required by eligibility and often named in methodological abstracts, so test a design block before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T19:36:25+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,414
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 3 | `"Models, Psychological"[Mesh]` | 43,468 | none |
| 4 | `"structural equation model"[tiab:~0]` | 1,961 | none |
| 5 | `"structural equation models"[tiab:~0]` | 1,699 | none |
| 6 | `"structural equation modeling"[tiab:~0]` | 7,913 | none |
| 7 | `"structural equation modelling"[tiab:~0]` | 1,788 | none |
| 8 | `"latent variable model"[tiab:~0]` | 255 | none |
| 9 | `"latent variable models"[tiab:~0]` | 278 | none |
| 10 | `"factor analysis"[tiab]` | 33,735 | none |
| 11 | `"confirmatory factor analysis"[tiab:~0]` | 8,095 | none |
| 12 | `CFA[tiab]` | 7,128 | none |
| 13 | `"latent growth"[tiab:~1]` | 2,685 | none |
| 14 | `"latent class"[tiab:~1]` | 4,163 | none |
| 15 | `multilevel[tiab]` | 25,930 | none |
| 16 | `mediation[tiab]` | 22,917 | none |
| 17 | `"path analysis"[tiab:~0]` | 4,098 | none |
| 18 | `SEM[tiab]` | 81,594 | none |
| 19 | `"item factor analysis"[tiab:~0]` | 130 | none |
| 20 | `"item response theory"[tiab:~0]` | 2,378 | none |
| 21 | `"latent trait model"[tiab:~0]` | 47 | none |
| 22 | `"growth curve model"[tiab:~0]` | 276 | none |
| 23 | `"growth curve models"[tiab:~0]` | 587 | none |
| 24 | `"mixture model"[tiab:~0]` | 2,743 | none |
| 25 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 242,915 | none |
| 26 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 27 | `Bayes[tiab]` | 5,705 | none |
| 28 | `Bayesian[tiab]` | 35,533 | none |
| 29 | `"Bayesian estimation"[tiab]` | 966 | none |
| 30 | `"Bayesian method"[tiab]` | 1,320 | none |
| 31 | `"Bayesian methods"[tiab]` | 1,812 | none |
| 32 | `"Bayesian approach"[tiab]` | 3,278 | none |
| 33 | `"Bayesian analysis"[tiab]` | 2,540 | none |
| 34 | `"Bayesian model"[tiab]` | 2,344 | none |
| 35 | `"Bayesian models"[tiab]` | 702 | none |
| 36 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 37 | `MCMC[tiab]` | 1,577 | none |
| 38 | `"Gibbs sampling"[tiab]` | 712 | none |
| 39 | `"prior distribution"[tiab]` | 661 | none |
| 40 | `"prior distributions"[tiab]` | 568 | none |
| 41 | `#26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40` | 48,128 | none |
| 42 | `#25 AND #41` | 2,414 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Models, Psychological"[Mesh] OR "structural equation model"[tiab:~0] OR "structural equation models"[tiab:~0] OR "structural equation modeling"[tiab:~0] OR "structural equation modelling"[tiab:~0] OR "latent variable model"[tiab:~0] OR "latent variable models"[tiab:~0] OR "factor analysis"[tiab] OR "confirmatory factor analysis"[tiab:~0] OR CFA[tiab] OR "latent growth"[tiab:~1] OR "latent class"[tiab:~1] OR multilevel[tiab] OR mediation[tiab] OR "path analysis"[tiab:~0] OR SEM[tiab] OR "item factor analysis"[tiab:~0] OR "item response theory"[tiab:~0] OR "latent trait model"[tiab:~0] OR "growth curve model"[tiab:~0] OR "growth curve models"[tiab:~0] OR "mixture model"[tiab:~0]) AND ("Bayes Theorem"[Mesh] OR Bayes[tiab] OR Bayesian[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian method"[tiab] OR "Bayesian methods"[tiab] OR "Bayesian approach"[tiab] OR "Bayesian analysis"[tiab] OR "Bayesian model"[tiab] OR "Bayesian models"[tiab] OR "Markov chain Monte Carlo"[tiab] OR MCMC[tiab] OR "Gibbs sampling"[tiab] OR "prior distribution"[tiab] OR "prior distributions"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small samples or few clusters | left out | 2,414 / 114 | 95.3% | none | 0/30 (up to 10% of removed records could be relevant) | The broad base has only six known relevant records, below the 15-record threshold needed to justify AND-ing an optional block. The standard loss sample found no eligible records; this sample is weak evidence because eligible papers are rare, so preserve recall and screen the small-sample condition. |
| Monte Carlo or simulation evaluation | left out | 2,414 / 819 | 66.1% | none | 0/30 (up to 10% of removed records could be relevant) | The broad base has only six known relevant records, below the 15-record threshold needed to justify AND-ing an optional block. The standard loss sample found no eligible records; this sample is weak evidence because eligible papers are rare, so preserve recall and screen the simulation requirement. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Structural equation and latent-variable model family (SEM, CFA, latent growth/class, multilevel, mediation) | 1 | `latent[tiab] OR factor*[tiab] OR CFA[tiab] OR psychometric*[tiab] OR mediation[tiab] OR multilevel[tiab] OR path analysis[tiab] OR growth curve[tiab]` | 6,862 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 48,128 | 0 |
| bayesian_estimation | 242,915 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,833 | initial | none | Initial two-block strategy; discovered and screened three relevant small-sample Bayesian SEM/CFA simulation comparison papers through PubMed pilots. |
| 2 | 2,414 | sem_family: +6 / -0 | none | Expanded SEM-family vocabulary to include member-only item factor/response and growth-curve model names; expanded small-sample wording after screened pilot discoveries. Added screened methodological candidates. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; R1-F01 must-fix open
- Round 2 on version 2: 1 findings; R1-F01 must-fix resolved
- Round 3 on version 2: 1 findings; R1-F01 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 552 NCBI requests logged (274 from cache); strategy sha256 d8422fde8315._

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
      "checked_at": "2026-09-29T19:36:25+00:00",
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
      "checked_at": "2026-09-29T19:36:25+00:00",
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
      "requested": "Models, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:36:25+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Models, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:36:25+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"models, psychological\"[MeSH Terms] OR \"structural equation model\"[Title/Abstract:~0] OR \"structural equation models\"[Title/Abstract:~0] OR \"structural equation modeling\"[Title/Abstract:~0] OR \"structural equation modelling\"[Title/Abstract:~0] OR \"latent variable model\"[Title/Abstract:~0] OR \"latent variable models\"[Title/Abstract:~0] OR \"factor analysis\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract:~0] OR \"CFA\"[Title/Abstract] OR \"latent growth\"[Title/Abstract:~1] OR \"latent class\"[Title/Abstract:~1] OR \"multilevel\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"path analysis\"[Title/Abstract:~0] OR \"SEM\"[Title/Abstract] OR \"item factor analysis\"[Title/Abstract:~0] OR \"item response theory\"[Title/Abstract:~0] OR \"latent trait model\"[Title/Abstract:~0] OR \"growth curve model\"[Title/Abstract:~0] OR \"growth curve models\"[Title/Abstract:~0] OR \"mixture model\"[Title/Abstract:~0]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayes\"[Title/Abstract] OR \"Bayesian\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"Bayesian method\"[Title/Abstract] OR \"Bayesian methods\"[Title/Abstract] OR \"Bayesian approach\"[Title/Abstract] OR \"Bayesian analysis\"[Title/Abstract] OR \"Bayesian model\"[Title/Abstract] OR \"Bayesian models\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Gibbs sampling\"[Title/Abstract] OR \"prior distribution\"[Title/Abstract] OR \"prior distributions\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "01c5ebc39b1f8964f0a0544e51926a67f7bb0999260225f5547ea0f2b7a21d07",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy covers the model-family members named in the scope with their own terms, including mediation, multilevel, CFA, latent growth, and latent class. The notes disclose that comparator and outcome terms are screened rather than searched."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searched concepts are ORed internally and ANDed together. The optional blocks were tested separately and left out with a recall-preserving rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are verified in the packet and supplement the text-word terms. No heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes broad Bayesian terminology and model-family wording, with relevant named members represented. Omitting sample-size and simulation terms from the final AND search is supported by the stated optional-block assessment."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query groups its OR clauses correctly, uses supported fields and proximity syntax, and reports no PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final query applies an upper Entry Date of 2017-11-29, although the question and eligibility criteria specify no date cutoff. This excludes later-indexed records and needs correction or an explicit scope justification."
        }
      },
      "findings": [
        {
          "id": "R1-F01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits PubMed Entry Date to 1800-01-01 through 2017-11-29. The packet gives no question-based rationale for excluding records entered after that date.",
          "recommendation": "Remove the upper Entry Date bound unless the review scope explicitly requires it, then rerun the complete evaluation and update counts and known-record checks.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "8446acbb555e85ff82cb04ef8336c45fa9a5715e15c6d38e3a548505ca1aacab",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched model-family terms cover the members named in the scope, including CFA, latent growth and class, multilevel, and mediation. The packet says comparators and outcomes will be screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "The model-family and Bayesian blocks are ORed internally and ANDed together. Optional small-sample and simulation blocks were tested separately and left out with recall-preserving rationales."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified, with no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy combines broad Bayesian wording with model-family terms. Leaving out the optional sample-size and simulation blocks is supported by the stated tests and screening plan."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query groups its OR clauses, uses reported fields and proximity expressions, and has no reported PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The upper Entry Date bound remains and excludes records entered after 2017-11-29. The packet now explicitly identifies it as the harness-mandated PSB_AS_OF retrieval bound, distinguishes it from a publication-date eligibility criterion, and reports no publication-date filter. This addresses the earlier finding's missing justification; the cutoff remains a documented retrieval limitation."
        }
      },
      "findings": [
        {
          "id": "R1-F01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits PubMed Entry Date to 1800-01-01 through 2017-11-29, excluding records entered after that date.",
          "recommendation": "Document the harness cutoff as a retrieval limitation and distinguish it from the review's publication-date eligibility criteria.",
          "status": "resolved",
          "response": "The packet now documents PSB_AS_OF=2017-11-29 as a harness-mandated Entrez Entry Date bound, states that it is not a review publication-date criterion, and confirms that no [dp] restriction is applied. The operational cutoff remains, but the earlier concern that it lacked an explicit justification is addressed."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "8446acbb555e85ff82cb04ef8336c45fa9a5715e15c6d38e3a548505ca1aacab",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy includes the named model-family members, including CFA, latent growth and class, multilevel, and mediation. The packet says comparators and outcomes will be screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "The searched concept blocks are ORed internally and ANDed together. The optional small-sample and simulation blocks were tested separately and left out with recall-preserving rationales."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the MeSH headings as verified and reports no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy combines broad Bayesian terms with model-family terms. The packet documents why optional sample-size and simulation blocks were left out and says those criteria will be screened."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query groups its OR clauses and uses reported fields and proximity expressions. The packet reports no PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The packet documents the 2017-11-29 upper Entry Date bound as the harness-mandated retrieval cutoff, distinguishes it from publication-date eligibility, and reports no publication-date filter."
        }
      },
      "findings": [
        {
          "id": "R1-F01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits PubMed Entry Date to 1800-01-01 through 2017-11-29, excluding records entered after that date.",
          "recommendation": "Document the harness cutoff as a retrieval limitation and distinguish it from the review's publication-date eligibility criteria.",
          "status": "resolved",
          "response": "The packet documents PSB_AS_OF=2017-11-29 as a harness-mandated Entrez Entry Date bound, states that it is not a review publication-date criterion, and confirms that no [dp] restriction is applied. The operational cutoff remains, but the earlier concern that it lacked an explicit justification is addressed."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


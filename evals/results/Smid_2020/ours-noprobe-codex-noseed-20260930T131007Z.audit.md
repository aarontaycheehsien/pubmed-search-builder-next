# PubMed search strategy: audit

Generated 2026-09-30T13:44:55+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task (+ application context tested as optional)
- Scope confirmed by user: no (User requested no questions during this run; scope proceeded provisionally without confirmation. No known relevant articles were supplied. Two records were screened in as relevant from a precise PubMed pilot. PSB_AS_OF was pinned to 2017-11-29 for every command. Standard workload budget 10,000.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family | search | The method comparison is specifically in SEM-family models. Include SEM, CFA, latent growth/class, multilevel, and mediation by their own labels because the eligibility criteria name these members. |
| Bayesian estimation | search | The target estimator is necessarily Bayesian and is a searchable methodological topic. |
| Small-sample or few-cluster context | optional | This defines the application context and may be named in titles/abstracts, but not reliably enough to require without testing. |
| Monte Carlo or simulation evaluation | optional | This is a recognizable design authors may name, but its terminology is not necessarily present in all records; test its retrieval effect. |
| Frequentist / maximum-likelihood comparison | screen | Comparators can be omitted from titles and abstracts; screen for direct comparator. |
| Performance, accuracy, and bias outcomes | screen | Outcome terms vary and may not be indexed consistently; screen for estimator performance. |
| Social/behavioural-science methodological paper and peer review | screen | Field and peer-review status are not reliable searchable constraints. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:43:58+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,699
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
| 8 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 9 | `"exploratory factor analysis"[tiab]` | 5,306 | none |
| 10 | `"factor analysis"[tiab]` | 33,735 | none |
| 11 | `"latent variable"[tiab]` | 2,007 | none |
| 12 | `"latent variables"[tiab]` | 1,525 | none |
| 13 | `"latent growth"[tiab]` | 1,734 | none |
| 14 | `"growth curve model"[tiab]` | 270 | none |
| 15 | `"growth mixture"[tiab]` | 791 | none |
| 16 | `"latent class"[tiab]` | 4,129 | none |
| 17 | `"multilevel"[tiab]` | 25,930 | none |
| 18 | `"multi-level"[tiab]` | 4,831 | none |
| 19 | `"hierarchical model"[tiab]` | 1,993 | none |
| 20 | `"hierarchical models"[tiab]` | 1,000 | none |
| 21 | `mediation[tiab]` | 22,917 | none |
| 22 | `"indirect effect"[tiab]` | 5,281 | none |
| 23 | `"path analysis"[tiab]` | 4,075 | none |
| 24 | `"covariance structure"[tiab]` | 990 | none |
| 25 | `SEM[tiab]` | 81,594 | none |
| 26 | `SEMs[tiab]` | 1,528 | none |
| 27 | `CFA[tiab]` | 7,128 | none |
| 28 | `CFAs[tiab]` | 447 | none |
| 29 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 210,412 | none |
| 30 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 31 | `Bayesian[tiab]` | 35,533 | none |
| 32 | `Bayes[tiab]` | 5,705 | none |
| 33 | `"Bayesian estimation"[tiab]` | 966 | none |
| 34 | `"Bayesian methods"[tiab]` | 1,812 | none |
| 35 | `"Bayesian approach"[tiab]` | 3,278 | none |
| 36 | `MCMC[tiab]` | 1,577 | none |
| 37 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 38 | `"Markov chains"[tiab]` | 625 | none |
| 39 | `"posterior distribution"[tiab]` | 1,034 | none |
| 40 | `#30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 48,400 | none |
| 41 | `#29 AND #40` | 2,699 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "structural equation model"[tiab] OR "structural equation models"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "confirmatory factor analysis"[tiab] OR "exploratory factor analysis"[tiab] OR "factor analysis"[tiab] OR "latent variable"[tiab] OR "latent variables"[tiab] OR "latent growth"[tiab] OR "growth curve model"[tiab] OR "growth mixture"[tiab] OR "latent class"[tiab] OR "multilevel"[tiab] OR "multi-level"[tiab] OR "hierarchical model"[tiab] OR "hierarchical models"[tiab] OR mediation[tiab] OR "indirect effect"[tiab] OR "path analysis"[tiab] OR "covariance structure"[tiab] OR SEM[tiab] OR SEMs[tiab] OR CFA[tiab] OR CFAs[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian methods"[tiab] OR "Bayesian approach"[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "Markov chains"[tiab] OR "posterior distribution"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small-sample or few-cluster context | left out | 2,699 / 163 | 94.0% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out: it materially reduces the core count, but only two eligible known records are available, below the 15-record evidence threshold for AND-ing. A fresh 30-record loss sample contained no clearly eligible record. |
| Monte Carlo or simulation evaluation | left out | 2,699 / 1,013 | 62.5% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out: it materially reduces the core count, but only two eligible known records are available, below the 15-record evidence threshold for AND-ing. A fresh 30-record loss sample contained no clearly eligible record. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 48,400 | 0 |
| bayesian | 210,412 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,658 | initial | none | Initial recall-first core blocks: SEM/latent-variable family AND Bayesian estimation. Small-sample context and simulation are optional candidates to measure, not assumed mandatory. |
| 2 | 2,699 | sem_family: +4 / -0 | none | Resolved the critic's must-fix lexical finding by adding explicit title/abstract acronyms SEM, SEMs, CFA, and CFAs. PubMed probe counts for SEM AND Bayesian (54) and CFA AND Bayesian (17) supported inclusion; acronym noise remains screening-level and the two known relevant records stay retrieved. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; PRESS-R1-001 must-fix open
- Round 2 on version 2: 1 findings; PRESS-R1-001 must-fix resolved
- Round 3 on version 2: 1 findings; PRESS-R1-001 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 658 NCBI requests logged (309 from cache); strategy sha256 668f7779632d._

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
      "checked_at": "2026-09-30T13:43:58+00:00",
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
      "checked_at": "2026-09-30T13:43:58+00:00",
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
      "checked_at": "2026-09-30T13:43:58+00:00",
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
      "checked_at": "2026-09-30T13:43:58+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"structural equation model\"[Title/Abstract] OR \"structural equation models\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"exploratory factor analysis\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable\"[Title/Abstract] OR \"latent variables\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model\"[Title/Abstract] OR \"growth mixture\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"multi-level\"[Title/Abstract] OR \"hierarchical model\"[Title/Abstract] OR \"hierarchical models\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"indirect effect\"[Title/Abstract] OR \"path analysis\"[Title/Abstract] OR \"covariance structure\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"SEMs\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"CFAs\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"Bayesian methods\"[Title/Abstract] OR \"Bayesian approach\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"Markov chains\"[Title/Abstract] OR \"posterior distribution\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "699e3f208cce806b8becc764178b226083a92ca0539966b4c9f1b0f75835af87",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searched SEM family is named as including SEM, but the text-word block contains only expanded structural-equation phrases and does not include the bare SEM label. This leaves a stated family member without its own label-based expression."
        },
        "operators": {
          "verdict": "pass",
          "note": "The model-family synonyms are ORed, the Bayesian synonyms are ORed, and the two required concepts are ANDed. Optional context and design blocks remain out of the required combination."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the selected headings as verified and shows no translation diagnostics. They supplement the title/abstract terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add and evaluate an explicit SEM acronym expression (and an explicit plural form if intended); the current text-word list does not search the stated SEM label. Existing full phrases otherwise cover the named model-family terms, including bare mediation, latent growth/class, and multilevel expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query is correctly grouped as two OR blocks joined by AND, and the packet reports no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unrequested language, publication-type, or other restrictive limits are present. The fixed entry-date ceiling is explicit in the query and matches the packet's stated as-of date."
        }
      },
      "findings": [
        {
          "id": "PRESS-R1-001",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol explicitly names SEM as a searched family member, but the strategy has no SEM acronym expression; its structural-equation expressions use only the expanded phrase. The translation check requires each named member to be represented by its own bare label.",
          "recommendation": "Add explicit title/abstract expressions for SEM and, if intended, SEMs (for example, SEM[tiab] and SEMs[tiab]); evaluate their translations and retrieval contribution before adopting them.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "20526550b7a25a7cac309de763ce3bced5a50a8cbf4cc077efcd2a51c2cf8f89",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy names each eligibility-listed SEM-family member with its own expression, including bare mediation, SEM/SEMs, and CFA/CFAs. The optional context and simulation blocks remain out of the required query based on the packet's retrieval-loss evaluations."
        },
        "operators": {
          "verdict": "pass",
          "note": "Model-family and Bayesian expressions are ORed within their blocks, and those two required blocks are joined by AND. Optional concepts are not ANDed into the core search."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the selected headings as verified, with no translation issues; they supplement the title/abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "SEM[tiab] and SEMs[tiab] are now explicitly tested and included in the model-family block. The packet reports their separate counts and literal Title/Abstract translations, with no diagnostics or issues. SEM's large count (81,594) signals possible breadth but does not by itself establish irrelevance; the protocol requires the bare family label."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query is correctly grouped as two OR blocks joined by AND, and the packet reports no query errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-type, or other unrequested restrictive filters are present. The entry-date ceiling is explicit and matches the packet's stated as-of date."
        }
      },
      "findings": [
        {
          "id": "PRESS-R1-001",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol explicitly names SEM as a searched family member, but the round 1 strategy lacked SEM acronym expressions.",
          "recommendation": "Add and evaluate explicit title/abstract expressions for SEM and SEMs.",
          "status": "resolved",
          "response": "The revised strategy adds SEM[tiab] and SEMs[tiab] as separate tested terms in the SEM-family block. Their packet-reported counts are 81,594 and 1,528; translations preserve the Title/Abstract field and diagnostics report no issues. Both appear in the complete query. This resolves the missing-label finding."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "20526550b7a25a7cac309de763ce3bced5a50a8cbf4cc077efcd2a51c2cf8f89",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The model-family block represents the named members with their own labels, including bare mediation, SEM/SEMs, and CFA/CFAs; the optional context and simulation concepts remain optional based on the reported loss evaluations."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the SEM-family and Bayesian blocks, and the two required blocks are ANDed. Small-sample and simulation blocks are not required in the combination."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified headings for statistical factor analysis, latent class analysis, multilevel analysis, and Bayes theorem, with no translation diagnostics; these supplement the text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover the named SEM-family and Bayesian concepts. SEM[tiab] and SEMs[tiab] are included and separately tested, resolving the prior missing-label finding; no phrase warnings are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query groups each concept block and joins the two required blocks with AND. The packet reports no query errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-type, or other restrictive limit is applied. The entry-date ceiling is explicit and matches the stated 2017-11-29 as-of date."
        }
      },
      "findings": [
        {
          "id": "PRESS-R1-001",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol named SEM as a searched family member, but the round 1 strategy lacked SEM acronym expressions.",
          "recommendation": "Add and evaluate explicit title/abstract expressions for SEM and SEMs.",
          "status": "resolved",
          "response": "The current strategy includes separately tested SEM[tiab] and SEMs[tiab] expressions in the SEM-family block. The packet reports counts of 81,594 and 1,528, literal Title/Abstract translations, and no diagnostics; both terms appear in the complete query. This resolves the finding."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


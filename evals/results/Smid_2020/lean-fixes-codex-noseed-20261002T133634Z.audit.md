# PubMed search strategy: audit

Generated 2026-10-02T13:55:28+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task + application context
- Scope confirmed by user: no (The user asked to proceed without clarification; scope is not user-confirmed. No seed articles were supplied. Every PubMed command used PSB_AS_OF=2017-11-29 (ISO format), bounding records by Entrez date; no publication-date limit was used. At standard depth, PubMed pilots, a focused review search, and screening of reference/neighbour candidates identified five relevant development records; no in-scope systematic-review benchmark or independent validation set was identified. Two additional candidates were left uncertain because the abstracts did not establish the required simulation and small-sample criteria. A later publication year on PMID 29172613 was retained because the PubMed record was present by the Entrez cutoff.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Bayesian estimation | search | The estimation method under study is central and normally named in the abstract or indexed. |
| Structural equation and latent-variable model family | search | The model family defines the task; named members in eligibility are searched by their own names to retain studies that omit the SEM umbrella label. |
| Small samples or few clusters | screen | This is an eligibility context that may be described only in the methods or simulation conditions. |
| Frequentist / maximum-likelihood or alternative estimator comparison | screen | Comparators can be inconsistently named in abstracts and should not be required as a Boolean block. |
| Estimator performance, accuracy, and bias | screen | Outcomes are variably reported and should be assessed during screening. |
| Monte Carlo or simulation evaluation | screen | Study design can be omitted from searchable fields; no ad hoc design filter will be imposed. |
| Social / behavioural sciences and peer-reviewed methodological publication | screen | Discipline and peer-review status are not reliably captured by a single PubMed concept or validated filter. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:54:45+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,600
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 2 | `Bayesian[tiab]` | 35,533 | none |
| 3 | `Bayes[tiab]` | 5,705 | none |
| 4 | `"Bayesian estimation"[tiab]` | 966 | none |
| 5 | `"Bayesian method*"[tiab]` | 3,265 | none |
| 6 | `"Bayesian approach*"[tiab]` | 3,793 | none |
| 7 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 8 | `MCMC[tiab]` | 1,577 | none |
| 9 | `"prior distribution*"[tiab]` | 1,143 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 47,885 | none |
| 11 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 12 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 13 | `"structural equation model*"[tiab]` | 12,605 | none |
| 14 | `SEM[tiab]` | 81,594 | none |
| 15 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 16 | `CFA[tiab]` | 7,128 | none |
| 17 | `"factor analysis"[tiab]` | 33,735 | none |
| 18 | `"latent variable model*"[tiab]` | 671 | none |
| 19 | `"latent growth"[tiab]` | 1,734 | none |
| 20 | `"growth curve model*"[tiab]` | 1,502 | none |
| 21 | `"latent class"[tiab]` | 4,129 | none |
| 22 | `"growth mixture model*"[tiab]` | 768 | none |
| 23 | `mediation[tiab]` | 22,917 | none |
| 24 | `multilevel[tiab]` | 25,930 | none |
| 25 | `"multi-level"[tiab]` | 4,831 | none |
| 26 | `"hierarchical model*"[tiab]` | 3,344 | none |
| 27 | `"path analysis"[tiab]` | 4,075 | none |
| 28 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27` | 203,914 | none |
| 29 | `#10 AND #28` | 2,600 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian method*"[tiab] OR "Bayesian approach*"[tiab] OR "Markov chain Monte Carlo"[tiab] OR MCMC[tiab] OR "prior distribution*"[tiab]) AND ("Factor Analysis, Statistical"[Mesh] OR "Multilevel Analysis"[Mesh] OR "structural equation model*"[tiab] OR SEM[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "factor analysis"[tiab] OR "latent variable model*"[tiab] OR "latent growth"[tiab] OR "growth curve model*"[tiab] OR "latent class"[tiab] OR "growth mixture model*"[tiab] OR mediation[tiab] OR multilevel[tiab] OR "multi-level"[tiab] OR "hierarchical model*"[tiab] OR "path analysis"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bayesian | 203,914 | 0 |
| sem_family | 47,885 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block strategy uses Bayesian estimation AND SEM/latent-variable family. Small-sample context, comparator, performance, simulation, discipline, and peer-reviewed status are screened to preserve recall. Terms include MeSH Bayes Theorem, Factor Analysis, Statistical, and Multilevel Analysis plus named family members. No limits; PubMed entry-date bound 2017-11-29 is harness-defined. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; F1 should-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 328 NCBI requests logged (120 from cache); strategy sha256 6d6943dcce25._

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
      "checked_at": "2026-10-02T13:54:45+00:00",
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
      "checked_at": "2026-10-02T13:54:45+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Factor Analysis, Statistical\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:54:45+00:00",
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
    }
  ],
  "translation": "(\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"bayesian method*\"[Title/Abstract] OR \"bayesian approach*\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"prior distribution*\"[Title/Abstract]) AND (\"factor analysis, statistical\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable model*\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model*\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"growth mixture model*\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"multi-level\"[Title/Abstract] OR \"hierarchical model*\"[Title/Abstract] OR \"path analysis\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "2e67386b83d9d17168663643f352fc907653609c58b111ff627f6b1be23a9866",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched model family includes the eligibility terms in their own form, including mediation, multilevel, CFA, latent growth, and latent class."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required search concepts are combined with AND, with synonyms within each block combined by OR. No proximity operators are used."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The packet verifies Bayes Theorem as a heading, but its supplied scope note describes the theorem rather than Bayesian estimation. The packet gives no evidence that this heading indexes relevant estimation-method papers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word set covers the named model-family terms and Bayesian approaches. Broad acronyms and terms may add noise, but the packet provides no basis for removing them from this recall-oriented strategy."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported translations show the intended Boolean structure, and the query diagnostics report no errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or eligibility filters are imposed. The Entrez-date cutoff is documented in the packet as applying to every PubMed command."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "\"Bayes Theorem\"[Mesh] is verified, but the packet's scope note describes the probability theorem rather than Bayesian estimation. There is no packet evidence that this heading indexes relevant estimator-method papers.",
          "recommendation": "Check whether relevant methodological records are indexed with this heading and identify a more directly applicable verified heading if available. If retaining or removing it, document the rationale and rerun the complete evaluation.",
          "status": "rejected",
          "response": "Retained because the live MeSH record for D001499 lists Bayesian Estimation as an entry term, so the descriptor is directly mapped to the searched estimation concept despite its broad scope-note wording. The heading is assigned to multiple screened-in records, including PMID 23148476; the development set's full 100% relative recall is maintained. The text-word layer independently searches Bayesian and related terms."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


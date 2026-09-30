# PubMed search strategy: audit

Generated 2026-09-30T13:08:32+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task + application context
- Scope confirmed by user: yes (User requested no clarification pauses; scope proceeds on the stated criteria. No known relevant articles supplied. PSB_AS_OF is set to 2017-11-29 for every command; no publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable family models (including CFA, latent growth/class, multilevel, and mediation) | search | The model family defines the methodological topic; all listed members are searched by their own names to avoid requiring authors to name SEM explicitly. |
| Bayesian estimation | search | The estimation approach under study is required and is generally identifiable by Bayesian terminology. |
| Small samples or few clusters | optional | This application context defines the question and has searchable labels, but may be reported only in methods/full text; test its retrieval cost and losses. |
| Monte Carlo or simulation study | optional | The eligibility design is often named in abstracts but not universally; test as an optional block before deciding. |
| Frequentist / maximum-likelihood or alternative estimator comparison | screen | Comparators may be described inconsistently or only in full text; screen for an eligible estimator comparison. |
| Performance, accuracy, and bias outcomes | screen | Estimator outcomes are inconsistently named and do not define a reliable PubMed block. |
| Peer-reviewed social/behavioural-science methodological context | screen | Disciplinary and peer-review status are not reliably captured by PubMed search terms. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:07:39+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 1,407
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"structural equation model*"[tiab]` | 12,605 | none |
| 5 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 6 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 7 | `"structural equation"[tiab:~1]` | 12,970 | none |
| 8 | `SEM[tiab]` | 81,594 | none |
| 9 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 10 | `CFA[tiab]` | 7,128 | none |
| 11 | `"factor analysis"[tiab]` | 33,735 | none |
| 12 | `"latent variable model*"[tiab]` | 671 | none |
| 13 | `"latent growth"[tiab]` | 1,734 | none |
| 14 | `"growth curve model*"[tiab]` | 1,502 | none |
| 15 | `"latent class"[tiab]` | 4,129 | none |
| 16 | `multilevel[tiab]` | 25,930 | none |
| 17 | `mediation[tiab]` | 22,917 | none |
| 18 | `mediator[tiab]` | 63,582 | none |
| 19 | `"indirect effect*"[tiab]` | 12,817 | none |
| 20 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 268,202 | none |
| 21 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 22 | `Bayesian[tiab]` | 35,533 | none |
| 23 | `Bayes[tiab]` | 5,705 | none |
| 24 | `MCMC[tiab]` | 1,577 | none |
| 25 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 26 | `"prior distribution*"[tiab]` | 1,143 | none |
| 27 | `"posterior distribution*"[tiab]` | 1,486 | none |
| 28 | `"Bayesian estimation"[tiab]` | 966 | none |
| 29 | `"Bayesian approach"[tiab]` | 3,278 | none |
| 30 | `#21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 48,119 | none |
| 31 | `#20 AND #30` | 1,407 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "structural equation model*"[tiab] OR "structural equation modelling"[tiab] OR "structural equation modeling"[tiab] OR "structural equation"[tiab:~1] OR SEM[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "factor analysis"[tiab] OR "latent variable model*"[tiab] OR "latent growth"[tiab] OR "growth curve model*"[tiab] OR "latent class"[tiab] OR multilevel[tiab] OR mediation[tiab] OR mediator[tiab] OR "indirect effect*"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "prior distribution*"[tiab] OR "posterior distribution*"[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian approach"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small samples or few clusters | left out | 1,407 / 82 | 94.2% | none | 0/30 (up to 10% of removed records could be relevant) | Only 2 screened relevant records are in the base, below the 15-record evidence threshold for safely AND-ing. Re-screened all 30 records in the current loss sample; none met all criteria. Despite a 94.2% reduction, retain this context for screening to protect recall. |
| Monte Carlo or simulation study | left out | 1,407 / 438 | 68.9% | none | 0/30 (up to 10% of removed records could be relevant) | Only 2 screened relevant records are in the base, below the 15-record evidence threshold for safely AND-ing. Re-screened all 30 records in the current loss sample; none met all criteria. Despite a 68.9% reduction, retain design for screening because it may not be labelled in every abstract. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem | 48,119 | 0 |
| bayesian | 268,202 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,407 | initial | none | Initial recall-first draft: AND SEM/latent-variable family with Bayesian estimation; measure small-sample and simulation blocks as optional candidates. Terms include MeSH and title/abstract variants. |
| 2 | 1,407 | sem: +0 / -1 | none | Address critic finding meSH-date-mediation: remove the Mediation Analysis MeSH descriptor introduced after the 2017 cutoff; retain text-word mediation terms. No other changes. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1 (Same-context critic: no fresh-context reviewer was available in this run. Reviewed the packet against all six PRESS domains.): 1 findings; meSH-date-mediation should-fix open
- Round 2 on version 2 (Same-context critic: no fresh-context reviewer was available in this run. Rechecked the revised packet and carried the prior finding forward.): 1 findings; meSH-date-mediation should-fix resolved
- Round 3 on version 2 (Same-context closing critic: no fresh-context reviewer was available in this run. Verified the prior finding against the current strategy and evaluation.): 1 findings; meSH-date-mediation should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 426 NCBI requests logged (176 from cache); strategy sha256 ad2cc71336c7._

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
      "checked_at": "2026-09-30T13:07:39+00:00",
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
      "checked_at": "2026-09-30T13:07:39+00:00",
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
      "checked_at": "2026-09-30T13:07:39+00:00",
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
      "checked_at": "2026-09-30T13:07:39+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation\"[Title/Abstract:~1] OR \"SEM\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable model*\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model*\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"mediator\"[Title/Abstract] OR \"indirect effect*\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"prior distribution*\"[Title/Abstract] OR \"posterior distribution*\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"Bayesian approach\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "d62d9ebec5a3d834222333445eada0a90ad584002c7712084228ae14c8aca8a4",
      "note": "Same-context critic: no fresh-context reviewer was available in this run. Reviewed the packet against all six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The AND-ed concepts are the required model family and Bayesian estimation. Small-sample and simulation concepts were measured as optional and left out under the documented evidence rule; comparators and outcomes remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within blocks and AND joins the two required concepts. No NOT, filters, or limits are used. Proximity is restrained to structural equation wording."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The current MeSH descriptor Mediation Analysis was introduced in 2021, after the requested 2017-11-29 historical frame. Remove it to avoid relying on post-cutoff indexing vocabulary; retain the free-text mediation terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include model-family members by their own names, spelling variants, relevant acronyms, Bayesian estimation terms, and safe truncations."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are field-tagged, punctuation is ASCII, wildcard stems are at least four letters, and live translations have no technical or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No additional filters or publication-date limits are applied. The entry-date bound is supplied by PSB_AS_OF as required."
        }
      },
      "findings": [
        {
          "id": "meSH-date-mediation",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "sem",
          "finding": "The Mediation Analysis MeSH descriptor was introduced in 2021, later than the requested 2017-11-29 historical frame.",
          "recommendation": "Remove the descriptor, keep the free-text mediation vocabulary, and rerun evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "d14bd42f0db9c768e5bb842e859df48089bba4b9ff7d01a7325dccdec8e74c86",
      "note": "Same-context critic: no fresh-context reviewer was available in this run. Rechecked the revised packet and carried the prior finding forward.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required model-family and Bayesian concepts remain the only AND-ed blocks. Optional small-sample and simulation concepts remain tested and left out with current decisions; comparison and outcome eligibility are screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "Boolean structure is appropriate, with synonym ORs and the two core concepts AND-ed. No NOT or unvalidated filter is present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The post-cutoff Mediation Analysis heading was removed. Remaining MeSH terms are appropriate and were introduced by the historical frame."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text terms retain the mediation member and cover SEM, CFA, latent growth/class, multilevel, indirect effects, and Bayesian/MCMC terminology."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Live translation is clean, with explicit fields, valid truncation, and no unresolved phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, or study-design filters were added. The Entrez-date cutoff is applied through PSB_AS_OF."
        }
      },
      "findings": [
        {
          "id": "meSH-date-mediation",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "sem",
          "finding": "The Mediation Analysis MeSH descriptor was introduced in 2021, later than the requested 2017-11-29 historical frame.",
          "recommendation": "Remove the descriptor, keep the free-text mediation vocabulary, and rerun evaluation.",
          "status": "resolved",
          "response": "Removed \"Mediation Analysis\"[Mesh] from the SEM block. The current strategy version 2 retains mediation[tiab], mediator[tiab], and \"indirect effect*\"[tiab]; live reevaluation shows no known records lost and the combined count remains 1,407 under the 2017-11-29 Entrez bound."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "d14bd42f0db9c768e5bb842e859df48089bba4b9ff7d01a7325dccdec8e74c86",
      "note": "Same-context closing critic: no fresh-context reviewer was available in this run. Verified the prior finding against the current strategy and evaluation.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The revised strategy still matches the two required concepts, leaves the optional blocks out under measured rules, and screens comparator, outcome, and discipline properties."
        },
        "operators": {
          "verdict": "pass",
          "note": "Boolean and proximity operators remain appropriate and validated."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The only post-cutoff MeSH descriptor identified in round 1 is absent from the current strategy; the relevant free-text terms remain."
        },
        "text_words": {
          "verdict": "pass",
          "note": "All named model-family members remain represented in title/abstract vocabulary, along with Bayesian estimation terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current live syntax and translations are clean."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date bound is retained without a publication-date limit or ad hoc study-design filter."
        }
      },
      "findings": [
        {
          "id": "meSH-date-mediation",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "sem",
          "finding": "The Mediation Analysis MeSH descriptor was introduced in 2021, later than the requested 2017-11-29 historical frame.",
          "recommendation": "Remove the descriptor, keep the free-text mediation vocabulary, and rerun evaluation.",
          "status": "resolved",
          "response": "Confirmed resolved: \"Mediation Analysis\"[Mesh] is absent from strategy version 2. The prior response records its removal and reevaluation; the current packet shows mediation[tiab], mediator[tiab], and \"indirect effect*\"[tiab] retained."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


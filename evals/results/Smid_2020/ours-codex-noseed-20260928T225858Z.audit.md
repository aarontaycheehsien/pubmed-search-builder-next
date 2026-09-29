# PubMed search strategy: audit

Generated 2026-09-28T23:23:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: Method performance
- Scope confirmed by user: yes (User asked to proceed without questions; scope and assumptions are provisional. PubMed availability cutoff is 2017-11-29 via PSB_AS_OF/Entrez date; no publication-date limit. No known relevant records supplied. Standard depth; screen candidates only after checking against all eligibility criteria. SEM-family and Bayesian estimation are the core required concepts; small-sample and simulation blocks will be tested as optional concepts. Comparator, performance outcomes, and field/peer-review eligibility are screening criteria. The strategy is for retrieval and screening, not an answer to the evidence question.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family | search | The estimation method is meaningful only for a specified SEM/latent-variable model family; members are explicitly named in eligibility and need broad coverage. |
| Bayesian estimation | search | Central estimation approach, typically named in titles/abstracts or indexed. |
| Small-sample or few-cluster context | optional | Topic-defining context that authors often name but may report only sample size; test loss and yield before requiring it. |
| Monte Carlo or simulation evaluation | optional | A recognizable methodological design likely to be named, but abstracts may omit it; test before AND-ing. |
| Frequentist/maximum-likelihood comparator | screen | Comparators are inconsistently named and can include alternative estimators; screen for the required comparison. |
| Accuracy, bias, and estimator performance | screen | Outcome terms are inconsistently reported; screen the full text/results. |
| Peer-reviewed social/behavioural sciences methodology | screen | Field and peer-review status are not reliably searchable as a single PubMed concept. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:22:20+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 9,394
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Statistics as Topic[Mesh]` | 2,501,457 | none |
| 2 | `Factor Analysis, Statistical[Mesh]` | 25,757 | none |
| 3 | `Multilevel Analysis[Mesh]` | 1,470 | none |
| 4 | `structural equation[tiab]` | 12,948 | none |
| 5 | `structural equation model[tiab]` | 1,934 | none |
| 6 | `structural equation modeling[tiab]` | 7,913 | none |
| 7 | `structural equation modelling[tiab]` | 1,788 | none |
| 8 | `SEM[tiab]` | 81,594 | none |
| 9 | `confirmatory factor analysis[tiab]` | 8,085 | none |
| 10 | `CFA[tiab]` | 7,128 | none |
| 11 | `latent growth[tiab]` | 1,734 | none |
| 12 | `growth curve model[tiab]` | 270 | none |
| 13 | `latent class[tiab]` | 4,129 | none |
| 14 | `latent variable[tiab]` | 2,007 | none |
| 15 | `multilevel[tiab]` | 25,930 | none |
| 16 | `mediation[tiab]` | 22,917 | none |
| 17 | `factor analysis[tiab]` | 33,735 | none |
| 18 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 2,643,765 | none |
| 19 | `Bayes Theorem[Mesh]` | 28,985 | none |
| 20 | `bayesian[tiab]` | 35,533 | none |
| 21 | `bayes[tiab]` | 5,705 | none |
| 22 | `Bayesian estimation[tiab]` | 966 | none |
| 23 | `Bayesian approach[tiab]` | 3,278 | none |
| 24 | `MCMC[tiab]` | 1,577 | none |
| 25 | `Markov chain Monte Carlo[tiab]` | 3,122 | none |
| 26 | `Gibbs sampling[tiab]` | 712 | none |
| 27 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 47,909 | none |
| 28 | `Monte Carlo Method[Mesh]` | 25,842 | none |
| 29 | `Computer Simulation[Mesh]` | 211,062 | none |
| 30 | `simulation[tiab]` | 155,075 | none |
| 31 | `simulations[tiab]` | 148,754 | none |
| 32 | `simulat*[tiab]` | 427,276 | none |
| 33 | `Monte Carlo[tiab]` | 41,522 | none |
| 34 | `#28 OR #29 OR #30 OR #31 OR #32 OR #33` | 550,598 | none |
| 35 | `#18 AND #27 AND #34` | 9,394 | none |

### Strategy (single line, for copying into PubMed)

```text
((Statistics as Topic[Mesh] OR Factor Analysis, Statistical[Mesh] OR Multilevel Analysis[Mesh] OR structural equation[tiab] OR structural equation model[tiab] OR structural equation modeling[tiab] OR structural equation modelling[tiab] OR SEM[tiab] OR confirmatory factor analysis[tiab] OR CFA[tiab] OR latent growth[tiab] OR growth curve model[tiab] OR latent class[tiab] OR latent variable[tiab] OR multilevel[tiab] OR mediation[tiab] OR factor analysis[tiab]) AND (Bayes Theorem[Mesh] OR bayesian[tiab] OR bayes[tiab] OR Bayesian estimation[tiab] OR Bayesian approach[tiab] OR MCMC[tiab] OR Markov chain Monte Carlo[tiab] OR Gibbs sampling[tiab]) AND (Monte Carlo Method[Mesh] OR Computer Simulation[Mesh] OR simulation[tiab] OR simulations[tiab] OR simulat*[tiab] OR Monte Carlo[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small-sample or few-cluster context | left out | 9,394 / 622 | 93.4% | none | 0/30 (up to 10% of removed records could be relevant) | The broader query without this block is 9,394 records, within the standard 10,000-record workload budget. Although it cut counts substantially and its latest 0/30 loss sample found no eligible records, the sample does not establish that authors consistently label small-sample context in searchable fields. Leave the optional block out to preserve recall; screen sample size/few-cluster eligibility. |
| Monte Carlo or simulation evaluation | AND-ed | 34,884 / 9,394 | 73.1% | none | 0/30 (up to 10% of removed records could be relevant) | The refreshed sample is against the broader SEM/Bayesian base without a small-sample requirement. The simulation block reduces that 34,884-record base to 9,394, within the standard 10,000-record screening budget, retains all three development records, and none of 30 randomly sampled removed records met eligibility on abstract screening. Since Monte Carlo/simulation evaluation is an explicit inclusion criterion and this block materially controls screening volume, retain it while noting the remaining risk that abstracts omit design terms. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem | 11,814 | 0 |
| bayesian | 115,317 | 0 |
| simulation | 34,884 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 34,884 | initial | none | Initial broad SEM-family and Bayesian blocks with both optional small-sample and simulation concepts; vocab includes member terms and MeSH headings, and avoids the post-2017 introduced Latent Class Analysis heading. |
| 2 | 1,450 | small_sample: +9 / -0 | none | Optional small-sample block AND-ed after 30/30 randomly drawn removed records screened as irrelevant; all three development records retained and count fell 95.8%. |
| 3 | 622 | simulation: +6 / -0 | none | Optional simulation block AND-ed after 30/30 randomly sampled removed records screened as irrelevant; all three development records retained. Small-sample block is already justified by its screened loss sample. |
| 4 | 9,394 | small_sample: +0 / -9 | none | Left the optional small-sample block out to preserve recall because the broadened 9,394-record search is still within the 10,000-record standard budget; re-tested simulation on that broader base and retained it after a fresh 0/30 loss sample. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-01 should-fix open, R1-02 document open
- Round 2 on version 4: 2 findings; R1-01 should-fix resolved, R1-02 document resolved
- Round 3 on version 4: 2 findings; R1-01 should-fix resolved, R1-02 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 636 NCBI requests logged (305 from cache); strategy sha256 757a74e012c1._

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
      "requested": "Statistics as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:22:20+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013223",
          "name": "Statistics as Topic",
          "type": "descriptor",
          "scope_note": "Works about the science and art of collecting, summarizing, and analyzing data that are subject to random variation.",
          "tree_numbers": [
            "E05.318.740",
            "H01.548.832",
            "N05.715.360.750",
            "N06.850.520.830"
          ],
          "entry_terms": 33,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013223",
      "preferred_label": "Statistics as Topic",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Statistics as Topic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Factor Analysis, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:22:20+00:00",
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
      "checked_at": "2026-09-28T23:22:20+00:00",
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
      "checked_at": "2026-09-28T23:22:20+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "Bayes Theorem",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Monte Carlo Method",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:22:20+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009010",
          "name": "Monte Carlo Method",
          "type": "descriptor",
          "scope_note": "In statistics, a technique for numerically approximating the solution of a mathematical problem by studying the distribution of some random variable, often generated by a computer. The name alludes to the randomness characteristic of the games of chance played at the gambling casinos in Monte Carlo. (From Random House Unabridged Dictionary, 2d ed, 1993)",
          "tree_numbers": [
            "E05.318.740.525",
            "L01.906.394.422",
            "N05.715.360.750.540",
            "N06.850.520.830.525"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009010",
      "preferred_label": "Monte Carlo Method",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "Monte Carlo Method",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer Simulation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:22:20+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003198",
          "name": "Computer Simulation",
          "type": "descriptor",
          "scope_note": "Computer-based representation of physical systems and phenomena such as chemical processes.",
          "tree_numbers": [
            "L01.224.160"
          ],
          "entry_terms": 21,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003198",
      "preferred_label": "Computer Simulation",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "Computer Simulation",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"statistics as topic\"[MeSH Terms] OR \"factor analysis, statistical\"[MeSH Terms] OR \"multilevel analysis\"[MeSH Terms] OR \"structural equation\"[Title/Abstract] OR \"structural equation model\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"latent variable\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract]) AND (\"bayes theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"bayes\"[Title/Abstract] OR \"bayesian estimation\"[Title/Abstract] OR \"bayesian approach\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"markov chain monte carlo\"[Title/Abstract] OR \"gibbs sampling\"[Title/Abstract]) AND (\"monte carlo method\"[MeSH Terms] OR \"computer simulation\"[MeSH Terms] OR \"simulation\"[Title/Abstract] OR \"simulations\"[Title/Abstract] OR \"simulat*\"[Title/Abstract] OR \"monte carlo\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "e3d5c18e069ef60abced29b0723691aa490300bc086bd28bf2a45d940211a013",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All named SEM/latent-variable model-family members are represented by standalone text terms."
        },
        "operators": {
          "verdict": "revise",
          "note": "Reassess the optional AND blocks given the 0/30 loss samples and available screening budget."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings shown were verified and no translation issues were reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The model-family and Bayesian blocks include broad free-text wording and MCMC variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure and field tags are coherent; no query errors or translation issues were reported."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Clarify the Entrez entry-date cutoff in the scope and audit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The small-sample and simulation blocks are both AND-ed into the search even though each is designated optional and each has a 0/30 loss sample. The broader queries remain within the stated 10,000-record workload budget: 9,394 without the small-sample block and 1,450 without the simulation block. Those samples do not establish that the omitted records are irrelevant.",
          "recommendation": "Reassess whether either optional block needs to be a mandatory search condition. If retaining them, explain the deliberate precision-versus-recall trade-off and gather stronger evidence about records excluded by each block.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The final query includes an Entry Date range through 2017-11-29, while the strategy reports limits as empty and the scope does not state a date cutoff.",
          "recommendation": "Report the Entry Date cutoff explicitly among the search limits and clarify that it is intentional for this search.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "56426ae6857e27d27308959f5ec5d4d5d03c450590287e521bc780a94e18ed1d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Every named SEM and latent-variable family member is represented by a standalone term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The small-sample block was removed. The simulation block is retained with a rationale tied to an explicit inclusion criterion, workload budget, and refreshed loss sample."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified headings and no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes broad model-family and Bayesian terms, plus simulation and Monte Carlo variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure is coherent, with no reported query errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The protocol notes identify the 2017-11-29 PubMed availability cutoff and state there is no publication-date limit; the query applies the Entrez Entry Date range."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier round asked for reassessment of the optional small-sample and simulation blocks, which were both AND-ed into the search.",
          "recommendation": "Reassess whether either optional block must remain a search condition and document the evidence and trade-off.",
          "status": "resolved",
          "response": "The small-sample block is now left out. The simulation block remains AND-ed because simulation is an explicit eligibility criterion and it reduces the broader base to within the 10,000-record budget; the packet documents the refreshed 0/30 loss sample and remaining risk."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The query applies an Entry Date cutoff through 2017-11-29, while the protocol limits list is empty.",
          "recommendation": "Report the Entry Date cutoff explicitly and clarify that it is intentional.",
          "status": "resolved",
          "response": "The protocol notes explicitly identify 2017-11-29 as the PubMed availability cutoff, and the query applies that Entry Date range. The notes also clarify that there is no publication-date limit."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "56426ae6857e27d27308959f5ec5d4d5d03c450590287e521bc780a94e18ed1d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Named SEM and latent-variable family members have standalone search terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The small-sample block was removed. The simulation block is retained with a documented rationale, workload budget, and refreshed loss sample."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified headings and no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes broad model-family and Bayesian terms, plus simulation and Monte Carlo variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure and field tags are coherent, with no reported query errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The protocol notes state the 2017-11-29 PubMed availability cutoff, and the query applies that Entry Date range; no publication-date limit is reported."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier round asked for reassessment of the optional small-sample and simulation blocks, which were both AND-ed into the search.",
          "recommendation": "Reassess whether either optional block must remain a search condition and document the evidence and trade-off.",
          "status": "resolved",
          "response": "The small-sample block was removed. The simulation block remains AND-ed because simulation is an explicit inclusion criterion and reduces the broader base to within the 10,000-record budget; the packet documents a refreshed 0/30 loss sample and the remaining risk."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The query applies an Entry Date cutoff through 2017-11-29, while the protocol limits list was empty.",
          "recommendation": "Report the Entry Date cutoff explicitly and clarify that it is intentional.",
          "status": "resolved",
          "response": "The protocol notes identify 2017-11-29 as the PubMed availability cutoff, and the query applies that Entry Date range. The notes also clarify that there is no publication-date limit."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


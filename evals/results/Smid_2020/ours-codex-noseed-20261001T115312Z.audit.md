# PubMed search strategy: audit

Generated 2026-10-01T12:35:40+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method performance
- Scope confirmed by user: no (The user asked not to pause for questions, so the protocol-defined scope was used without user confirmation. No user-supplied known articles were provided. Six relevant records were screened in from PubMed pilot and similar-article candidates. Standard depth. PubMed is bounded by harness via PSB_AS_OF=2017-11-29 on every command; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family | search | The model family defines the method application; the criteria explicitly include named members such as CFA, latent growth/class, multilevel and mediation models, which may be named without saying SEM. |
| Bayesian estimation | search | The estimation approach being evaluated is central and likely named in abstracts or indexing. |
| Small-sample or few-cluster context | optional | This context defines the review topic and may often be named, but may not be explicit in every abstract; test the block before deciding whether to AND it. |
| Monte Carlo or simulation study design | optional | Simulation is a recognizable, topic-defining study design frequently named in methodological abstracts, but it is not guaranteed to be indexed or named consistently; evaluate its reduction and loss sample before deciding. |
| Frequentist comparator, performance outcomes, and social/behavioural-science field | screen | Comparator type, accuracy/bias outcomes, and field are variable or screening-level eligibility criteria; do not require separate AND blocks. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:34:27+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 11,582
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"Models, Statistical"[Mesh]` | 370,212 | none |
| 5 | `"structural equation model*"[tiab]` | 12,605 | none |
| 6 | `"covariance structure model*"[tiab]` | 126 | none |
| 7 | `"confirmatory factor analys*"[tiab]` | 10,281 | none |
| 8 | `CFA[tiab]` | 7,128 | none |
| 9 | `"latent variable model*"[tiab]` | 671 | none |
| 10 | `"latent growth model*"[tiab]` | 551 | none |
| 11 | `"growth mixture model*"[tiab]` | 768 | none |
| 12 | `"latent class model*"[tiab]` | 603 | none |
| 13 | `"latent class analys*"[tiab]` | 2,675 | none |
| 14 | `factor analys*[tiab]` | 38,459 | none |
| 15 | `mediation[tiab]` | 22,917 | none |
| 16 | `multilevel[tiab]` | 25,930 | none |
| 17 | `"path analys*"[tiab]` | 5,178 | none |
| 18 | `SEM[tiab]` | 81,594 | none |
| 19 | `"latent growth"[tiab]` | 1,734 | none |
| 20 | `"latent class"[tiab]` | 4,129 | none |
| 21 | `"growth mixture"[tiab]` | 791 | none |
| 22 | `"indirect effect*"[tiab]` | 12,817 | none |
| 23 | `"mediated effect*"[tiab]` | 8,056 | none |
| 24 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23` | 581,122 | none |
| 25 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 26 | `Bayesian[tiab]` | 35,533 | none |
| 27 | `Bayes[tiab]` | 5,705 | none |
| 28 | `MCMC[tiab]` | 1,577 | none |
| 29 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 30 | `"prior distribution*"[tiab]` | 1,143 | none |
| 31 | `"posterior distribution*"[tiab]` | 1,486 | none |
| 32 | `"Bayesian estimation"[tiab]` | 966 | none |
| 33 | `"Bayesian method*"[tiab]` | 3,265 | none |
| 34 | `#25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 48,119 | none |
| 35 | `#24 AND #34` | 11,582 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Models, Statistical"[Mesh] OR "structural equation model*"[tiab] OR "covariance structure model*"[tiab] OR "confirmatory factor analys*"[tiab] OR CFA[tiab] OR "latent variable model*"[tiab] OR "latent growth model*"[tiab] OR "growth mixture model*"[tiab] OR "latent class model*"[tiab] OR "latent class analys*"[tiab] OR factor analys*[tiab] OR mediation[tiab] OR multilevel[tiab] OR "path analys*"[tiab] OR SEM[tiab] OR "latent growth"[tiab] OR "latent class"[tiab] OR "growth mixture"[tiab] OR "indirect effect*"[tiab] OR "mediated effect*"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "prior distribution*"[tiab] OR "posterior distribution*"[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian method*"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| seeds | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Small-sample or few-cluster context | left out | 11,582 / 630 | 94.6% | none | 0/30 (up to 10% of removed records could be relevant) | Left out because only six eligible known records are in the base search, below the 15-record threshold for safely AND-ing an optional concept, though 0/30 sampled loss records were relevant. Tested reduction was 94.6% (11,582 to 630); the sample does not establish safety. |
| Monte Carlo or simulation study design | left out | 11,582 / 4,398 | 62.0% | none | 0/30 (up to 10% of removed records could be relevant) | Left out because only six eligible known records are in the base search, below the 15-record threshold for safely AND-ing an optional concept, though 0/30 sampled loss records were relevant. Tested reduction was 62.0% (11,582 to 4,398); the sample does not establish safety. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Structural equation and latent-variable model family | 1 | `model*[tiab] OR latent[tiab] OR factor[tiab] OR CFA[tiab] OR SEM[tiab] OR mediation[tiab] OR multilevel[tiab] OR path[tiab]` | 18,651 | 0/30 |
| Structural equation and latent-variable model family | 2 | `model*[tiab] OR latent[tiab] OR factor[tiab] OR CFA[tiab] OR SEM[tiab] OR mediation[tiab] OR multilevel[tiab] OR path[tiab]` | 18,602 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 48,119 | 0 |
| bayesian | 581,122 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 11,499 | initial | none | Initial recall-first strategy from protocol-defined concepts; added MeSH headings and title/abstract terms for SEM-family members and Bayesian estimation. Small-sample context tested as an optional block; comparison/design/outcomes remain screening criteria. |
| 2 | 11,499 | limits/combination | none | Promoted simulation design from screen to optional after recognizing it is frequently named in methodological abstracts and could address the workload count; added MeSH and free-text design terms. No inclusion criteria changed. |
| 3 | 11,651 | bayesian: +1 / -0 | none | Added the screened relevant records' observed Bayesian term 'priors' to the Bayesian block; retained the optional blocks as leave-out decisions because the known set is underpowered. No known records lost. |
| 4 | 11,499 | bayesian: +0 / -1 | none | Reverted the candidate term priors[tiab] after it added 152 records without gaining either known relevant record; existing Bayesian vocabulary covers the concept with lower noise. Restored the strategy state used by the optional decisions and category probe. |
| 5 | 11,548 | sem_family: +3 / -0 | none | Broadened latent growth/class family terms to search the bare named members, as required by the criteria and scope instructions. This increases recall; the old optional decisions and category probe need refreshed measurements. |
| 6 | 11,662 | sem_family: +2 / -0; bayesian: +2 / -0 | none | Added bare mediation outcome vocabulary (indirect effect and mediated effect) and Gibbs sampling terms as supported synonyms for family/estimation concepts; rerun optional and category measurements against updated query. |
| 7 | 11,582 | bayesian: +0 / -2 | none | Removed Gibbs sampling/sampler alternatives before delivery because adding a Bayesian-block term invalidated the category probe; MCMC and Bayesian wording cover the indexed method and no known record depends on Gibbs wording. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 7 (Same-context critic: no separate fresh-context reviewer was available in this run. This is internal PRESS-structured QA, not independent PRESS peer review.): 1 findings; MESH-2019 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1406 NCBI requests logged (703 from cache); strategy sha256 2772f5e874c4._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "over_workload_budget",
        "message": "11,582 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:small_sample",
        "blocking": false,
        "requires_review": true,
        "id": "I-20f029382d8d13d0bc00"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:simulation_design",
        "blocking": false,
        "requires_review": true,
        "id": "I-6b781c01a3e2b154b9de"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "11,582 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:small_sample",
        "blocking": false,
        "requires_review": true,
        "id": "I-20f029382d8d13d0bc00"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:simulation_design",
        "blocking": false,
        "requires_review": true,
        "id": "I-6b781c01a3e2b154b9de"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Factor Analysis, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:34:27+00:00",
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
      "checked_at": "2026-10-01T12:34:27+00:00",
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
      "checked_at": "2026-10-01T12:34:27+00:00",
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
      "requested": "Models, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:34:27+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015233",
          "name": "Models, Statistical",
          "type": "descriptor",
          "scope_note": "Statistical formulations or analyses which, when applied to data and found to fit the data, are then used to verify the assumptions and parameters used in the analysis. Examples of statistical models are the linear model, binomial model, polynomial model, two-parameter model, etc.",
          "tree_numbers": [
            "E05.318.740.500",
            "E05.599.835",
            "N05.715.360.750.530",
            "N06.850.520.830.500"
          ],
          "entry_terms": 20,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015233",
      "preferred_label": "Models, Statistical",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Models, Statistical\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:34:27+00:00",
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
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"models, statistical\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"covariance structure model*\"[Title/Abstract] OR \"confirmatory factor analys*\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"latent variable model*\"[Title/Abstract] OR \"latent growth model*\"[Title/Abstract] OR \"growth mixture model*\"[Title/Abstract] OR \"latent class model*\"[Title/Abstract] OR \"latent class analys*\"[Title/Abstract] OR \"factor analys*\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"path analys*\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"growth mixture\"[Title/Abstract] OR \"indirect effect*\"[Title/Abstract] OR \"mediated effect*\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"prior distribution*\"[Title/Abstract] OR \"posterior distribution*\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"bayesian method*\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 7,
      "review_sha256": "53bb3ea9804e44c2f29ee4e4a1b87be2b1c8bf4e5e99cd7d671494cbece0f79b",
      "note": "Same-context critic: no separate fresh-context reviewer was available in this run. This is internal PRESS-structured QA, not independent PRESS peer review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required method and model-family concepts are AND-ed; comparators, small-sample eligibility, simulation, outcomes and field are screened or tested as optional. Bare family members include CFA, latent growth/class, growth mixture, mediation/indirect effects, multilevel and path analysis. Both optional concepts were tested and left out under the underpowered-known-set rule."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each concept; AND combines only the two required concepts. No NOT or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH headings are current verified descriptors and both blocks have explicit MeSH and title/abstract layers. Models, Statistical is broad and intentionally exploded for recall. Latent Class Analysis was introduced in 2019, which is documented as a historical-vocabulary risk."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover named model-family members and Bayesian/MCMC/prior/posterior language. SEM and CFA are ambiguous acronyms, retained for recall within the required Bayesian intersection; screening handles noise."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly field-tagged, PubMed translation checks returned no warnings, and there are no phrase-index review issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, publication-type, or study-design filter is used. The harness applies the PubMed entry-date bound through PSB_AS_OF=2017-11-29."
        }
      },
      "findings": [
        {
          "id": "MESH-2019",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "reporting",
          "finding": "The Latent Class Analysis MeSH descriptor was introduced in 2019, after the assumed 2017 search date. The run is entry-date bounded, but the current descriptor may reflect later indexing of older records.",
          "recommendation": "Keep this historical-vocabulary limitation visible and ask an information specialist to confirm it for reproducibility.",
          "status": "accepted-risk",
          "response": "The descriptor is valid in the current MeSH authority and supplements bare latent-class title/abstract terms. PSB_AS_OF restricts records to PubMed entries by 2017-11-29; the audit and narrative disclose that MeSH itself is current rather than reconstructed historically."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 11,582-record query exceeds the 10,000 standard workload budget. The small-sample block reduced the count to 630 and the simulation block to 4,398, but both remain optional because six known records are below the 15-record threshold; requiring either could lose unknown eligible studies. The user requested high sensitivity, so retain the broad query and disclose the screening burden.",
          "evidence": "The final query count was 11,582. Both optional concepts were tested, with 0 relevant among 30 screened losses for each. The known set has six records, all retrieved."
        },
        {
          "issue_id": "I-20f029382d8d13d0bc00",
          "status": "accepted-risk",
          "response": "The small-sample concept was evaluated but not AND-ed because only six relevant records were available, below the required 15. A clean 30-record loss sample is insufficient to prove safety. Further discovery was attempted through a systematic-review query, focused pilot searches, and similar-article candidates.",
          "evidence": "The small-sample block reduced records from 11,582 to 630; it lost none of six known records and had 0/30 relevant in the loss sample. The systematic-review query returned nine titles with no matching methodological review identified; pilot and similar-article screening yielded six eligible development records."
        },
        {
          "issue_id": "I-6b781c01a3e2b154b9de",
          "status": "accepted-risk",
          "response": "The simulation-design concept was evaluated but not AND-ed because only six relevant records were available, below the required 15. A clean 30-record loss sample is insufficient to prove safety. Further discovery was attempted through a systematic-review query, focused pilot searches, and similar-article candidates.",
          "evidence": "The simulation block reduced records from 11,582 to 4,398; it lost none of six known records and had 0/30 relevant in the loss sample. The systematic-review query returned nine titles with no matching methodological review identified; pilot and similar-article screening yielded six eligible development records."
        }
      ]
    }
  ]
}
```


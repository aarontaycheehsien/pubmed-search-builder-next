# PubMed search strategy: audit

Generated 2026-09-29T00:13:23+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task + application context
- Scope confirmed by user: yes (User asked to proceed without clarification. Scope roles and eligibility were set from the question before examining records. No known relevant articles were supplied. Treat small-sample context and simulation as optional, tested concepts; comparison, outcomes, and disciplinary field are screened. No publication-date limit; PubMed records are bounded by Entrez date as of 2017-11-29 per harness. After the screened small-sample record exposed a loss under simulation wording, the simulation block is no longer required in the query; it remains optional and will be retested. Comparator moved from screen to optional for measured workload reduction because it is a searchable, often-named methods-comparison element.  Comparator moved from screen to optional because it is central and often named in methods-comparison papers; this was tested to reduce workload. )
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family | search | The review concerns performance of Bayesian estimation specifically in SEM-family models; searchable model-family labels form the task context. Includes all named members in the eligibility criteria. |
| Bayesian estimation | search | Essential estimator under study and typically named in methodological records. |
| Small sample or few-cluster context | optional | Defines the application context and is often named, but may be omitted from titles/abstracts; test before deciding whether to AND. |
| Monte Carlo or simulation study | optional | Eligibility requires simulation evidence and authors often name simulation designs; test its recall and screening yield before deciding whether to AND. |
| Frequentist / maximum-likelihood comparator | optional | The frequentist/maximum-likelihood alternative is central and often named in methods-comparison abstracts; test as an optional workload-reduction concept while protecting the known comparison record. |
| Performance, accuracy, bias outcomes | screen | Performance outcomes and their measures vary and are screened from the record/full text. |
| Social/behavioural-sciences field | screen | Field eligibility is not reliably searchable and will be screened. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T00:12:33+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 12,364
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 2 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"Mediation Analysis"[Mesh]` | 1 | none |
| 5 | `"Models, Statistical"[Mesh]` | 370,212 | none |
| 6 | `"structural equation model*"[tiab]` | 12,605 | none |
| 7 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 8 | `"latent variable model*"[tiab]` | 671 | none |
| 9 | `"latent growth"[tiab]` | 1,734 | none |
| 10 | `"growth curve model*"[tiab]` | 1,502 | none |
| 11 | `"confirmatory factor analys*"[tiab]` | 10,281 | none |
| 12 | `"factor analys*"[tiab]` | 38,459 | none |
| 13 | `CFA[tiab]` | 7,128 | none |
| 14 | `"latent class model*"[tiab]` | 603 | none |
| 15 | `"latent class analys*"[tiab]` | 2,675 | none |
| 16 | `"multilevel model*"[tiab]` | 4,596 | none |
| 17 | `"hierarchical linear model*"[tiab]` | 2,083 | none |
| 18 | `"hierarchical model*"[tiab]` | 3,344 | none |
| 19 | `mediation[tiab]` | 22,917 | none |
| 20 | `"path analys*"[tiab]` | 5,178 | none |
| 21 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 470,413 | none |
| 22 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 23 | `Bayes*[tiab]` | 39,780 | none |
| 24 | `Bayesian[tiab]` | 35,533 | none |
| 25 | `MCMC[tiab]` | 1,577 | none |
| 26 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 27 | `"Markov chain"[tiab]` | 4,870 | none |
| 28 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27` | 49,381 | none |
| 29 | `#21 AND #28` | 12,364 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Latent Class Analysis"[Mesh] OR "Factor Analysis, Statistical"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Mediation Analysis"[Mesh] OR "Models, Statistical"[Mesh] OR "structural equation model*"[tiab] OR "structural equation modeling"[tiab] OR "latent variable model*"[tiab] OR "latent growth"[tiab] OR "growth curve model*"[tiab] OR "confirmatory factor analys*"[tiab] OR "factor analys*"[tiab] OR CFA[tiab] OR "latent class model*"[tiab] OR "latent class analys*"[tiab] OR "multilevel model*"[tiab] OR "hierarchical linear model*"[tiab] OR "hierarchical model*"[tiab] OR mediation[tiab] OR "path analys*"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayes*[tiab] OR Bayesian[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "Markov chain"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Small sample or few-cluster context | left out | 12,364 / 628 | 94.9% | 28358542 | 0/30 (up to 10% of removed records could be relevant) | The current 30-record loss sample was reviewed; it includes PMID 28358542, a likely relevant paper with small participant counts, which the known-record evaluation confirms this block misses. Despite a 94.9% reduction, preserve it by leaving this optional block unrequired; screen small-sample status. |
| Monte Carlo or simulation study | left out | 12,364 / 4,072 | 67.1% | 28358542 | 0/30 (up to 10% of removed records could be relevant) | The current 30-record loss sample was reviewed. The known relevant development record PMID 28358542 is missed by this block; its abstract's parameter-recovery comparison over participant counts likely reflects simulation although it does not name a Monte Carlo design. Despite a 67.1% reduction, leave the block unrequired and screen design in full text. |
| Frequentist / maximum-likelihood comparator | left out | 12,364 / 4,124 | 66.6% | none | 0/30 (up to 10% of removed records could be relevant) | Although the block reduced retrieval by 66.6%, the 0/30 loss sample and single development record do not establish sensitivity to all eligible alternatives: the protocol allows comparison with alternative estimators that may not be labeled frequentist, maximum likelihood, or classical estimation. Because the review asks for a high-sensitivity search, retain the comparator as a tested candidate but leave it unrequired and screen the comparison. This leaves 12,364 records, above the default 10,000 standard workload budget; screen capacity was not supplied, and additional narrowing blocks lost a likely relevant record. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_models | 49,381 | 0 |
| bayesian | 470,413 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 12,364 | initial | none | Initial recall-first strategy; model family and Bayesian estimation searched, with sample-size context and simulation tested as optional blocks. No seed records were supplied; proceed under the requested 2017-11-29 Entrez bound. |
| 2 | 4,072 | simulation: +7 / -0 | none | AND simulation after a standard loss sample (0/30 clearly eligible); evaluate current query with simulation required and refresh the small-sample optional test because its comparison base changed. |
| 3 | 12,364 | simulation: +0 / -7 | none | Revised after PMID 28358542 was screened in: simulation block lost that likely relevant record, so simulation returns to optional. Comparator becomes optional because this central estimator contrast is likely searchable and workload is above budget. Measure all optional blocks on the revised core. |
| 4 | 4,124 | comparator: +9 / -0 | none | AND comparator after screened standard loss sample (0/30 eligible); then reevaluate all optional blocks and resample them against the revised core query. |
| 5 | 12,364 | comparator: +0 / -9 | none | After internal critique, comparator block left out to protect high sensitivity to eligible alternative estimators not named by the current comparator vocabulary. Query count returns to 12,364; no required optional block is AND-ed. Workload budget remains above default and is documented for review. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 2 findings; R1-01 should-fix open, R1-02 document accepted-risk
- Round 2 on version 5: 2 findings; R1-01 should-fix resolved, R1-02 document accepted-risk
- Round 3 on version 5: 2 findings; R1-01 should-fix resolved, R1-02 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 977 NCBI requests logged (519 from cache); strategy sha256 2b5cadd595f3._

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
        "message": "12,364 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "12,364 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Latent Class Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:12:33+00:00",
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
      "checked_at": "2026-09-29T00:12:33+00:00",
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
      "checked_at": "2026-09-29T00:12:33+00:00",
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
      "checked_at": "2026-09-29T00:12:33+00:00",
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
      "requested": "Models, Statistical",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:12:33+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Models, Statistical\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bayes Theorem",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:12:33+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Latent Class Analysis\"[MeSH Terms] OR \"factor analysis, statistical\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"Mediation Analysis\"[MeSH Terms] OR \"models, statistical\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"latent variable model*\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model*\"[Title/Abstract] OR \"confirmatory factor analys*\"[Title/Abstract] OR \"factor analys*\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"latent class model*\"[Title/Abstract] OR \"latent class analys*\"[Title/Abstract] OR \"multilevel model*\"[Title/Abstract] OR \"hierarchical linear model*\"[Title/Abstract] OR \"hierarchical model*\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"path analys*\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"bayes*\"[Title/Abstract] OR \"Bayesian\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"Markov chain\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "6943cf3d3849ca65bceb4dcd457ef6ed746be53ab6c536d57616a8bbbc447ef9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The model-family block includes the named members with their own searchable terms, including latent growth, latent class, multilevel, and bare mediation. Bayesian terms are present; outcome measures and field are explicitly assigned to screening."
        },
        "operators": {
          "verdict": "revise",
          "note": "The required comparator block has useful workload reduction and retrieves the development record, but it may exclude eligible comparisons whose abstracts do not use the listed comparator wording. The 0/30 loss sample does not resolve that vocabulary risk."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy combines model-family, Bayesian, and likelihood-related headings with title/abstract terms. No heading-specific translation errors are reported in the packet."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks cover the stated concepts with phrase variants, truncation, and acronyms. Small-sample and simulation concepts were tested and left unrequired after each missed the development record."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure is coherent, and the submitted query translations report no errors or warnings. No proximity operators require interpretation."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "There is no publication-date limit, but the saved query is bounded by Entrez date through 2017-11-29. That is a dated search snapshot and will omit records entered afterward if used as a current search."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The comparator block is ANDed into the final query, although its vocabulary may miss eligible Bayesian comparisons that describe the alternative estimator without naming maximum likelihood, frequentist methods, classical estimation, or an alternative estimator. The 30-record loss sample found no relevant records, but does not establish that the comparator vocabulary is sufficiently sensitive.",
          "recommendation": "Either leave the comparator concept unrequired and screen comparisons, or expand and test comparator wording against additional eligible records before retaining it as mandatory. Re-run the complete evaluation after changing the block.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The final query has an Entrez date ceiling of 2017-11-29. The packet documents this as the harness snapshot date, but the review question has no date restriction, so using this saved query as a current search would omit later-entered records.",
          "recommendation": "Retain the cutoff only when reporting this historical snapshot; rerun the strategy with a current search date for an up-to-date review and report the actual search date.",
          "status": "accepted-risk",
          "response": "The packet identifies 2017-11-29 as the harness Entrez snapshot boundary and states that there is no publication-date limit. This is acceptable as a documented historical evaluation, but the strategy needs a current rerun before use as an up-to-date search."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "ec6179ee0fd3815e533369b1de25e81e59e921cf3aeb3c56298d480022202c60",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The model-family block covers the named SEM members, including bare mediation, latent growth/class, multilevel, CFA, and path analysis. Bayesian estimation has heading and text-word coverage. Outcomes and disciplinary field are explicitly assigned to screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query requires only the model-family and Bayesian blocks. The comparator remains an optional tested concept and is not ANDed into the query, resolving the prior sensitivity concern. The query retrieves the known development record."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes model-family and Bayesian headings alongside text words. The packet reports no translation errors or warnings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word blocks cover the named model families and Bayesian methods. Small-sample, simulation, and comparator blocks were tested as optional concepts; the first two each miss the known development record and are left unrequired."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure is coherent, the final query translation reports no errors or warnings, and no proximity operators require interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date ceiling is documented as the historical harness snapshot boundary, with no publication-date restriction. The cutoff is acceptable for this historical evaluation; an up-to-date search requires a current rerun."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The comparator block is ANDed into the final query, although its vocabulary may miss eligible Bayesian comparisons that describe the alternative estimator without naming maximum likelihood, frequentist methods, classical estimation, or an alternative estimator. The 30-record loss sample found no relevant records, but does not establish that the comparator vocabulary is sufficiently sensitive.",
          "recommendation": "Either leave the comparator concept unrequired and screen comparisons, or expand and test comparator wording against additional eligible records before retaining it as mandatory. Re-run the complete evaluation after changing the block.",
          "status": "resolved",
          "response": "The version 5 final query does not AND the comparator block. It remains a tested optional candidate, and the comparison is screened. The current evaluation retrieves PMID 28358542."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The final query has an Entrez date ceiling of 2017-11-29. The packet documents this as the harness snapshot date, but the review question has no date restriction, so using this saved query as a current search would omit later-entered records.",
          "recommendation": "Retain the cutoff only when reporting this historical snapshot; rerun the strategy with a current search date for an up-to-date review and report the actual search date.",
          "status": "accepted-risk",
          "response": "The packet identifies 2017-11-29 as the harness Entrez snapshot boundary and states that there is no publication-date limit. This is acceptable for the documented historical evaluation; a current rerun is needed before using the strategy as an up-to-date search."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional small-sample, simulation, and comparator concepts were all tested. The small-sample and simulation blocks each miss the known relevant development record, and the comparator block remains unrequired because its vocabulary may miss eligible alternatives. The packet assigns outcomes and field to screening because their measures and disciplinary labels are not reliably searchable. The 12,364-record result exceeds the 10,000-record budget, but further narrowing with the tested blocks would risk sensitivity; screening capacity was not supplied.",
          "evidence": "The packet reports counts of 12,364 without and 628 with the small-sample block, 12,364 without and 4,072 with the simulation block, and 12,364 without and 4,124 with the comparator block. Both small-sample and simulation blocks list PMID 28358542 as lost. The final query leaves all three blocks unrequired."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "ec6179ee0fd3815e533369b1de25e81e59e921cf3aeb3c56298d480022202c60",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The model-family block covers the named SEM members, including bare mediation, latent growth/class, multilevel, CFA, and path analysis. Bayesian estimation has heading and text-word coverage; outcomes and disciplinary field are assigned to screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query requires only the model-family and Bayesian blocks. The comparator remains optional and the query retrieves the known development record."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes model-family and Bayesian headings alongside text words. The packet reports no translation errors or warnings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word blocks cover the named model families and Bayesian methods. Small-sample, simulation, and comparator concepts were tested as optional blocks; the first two miss the known development record and remain unrequired."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean structure is coherent, the final query translation reports no errors or warnings, and no proximity operators require interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date ceiling is documented as the historical harness snapshot boundary, with no publication-date restriction. An up-to-date search requires a current rerun."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The comparator block was ANDed into the final query, although its vocabulary may miss eligible Bayesian comparisons that describe the alternative estimator without naming maximum likelihood, frequentist methods, classical estimation, or an alternative estimator.",
          "recommendation": "Leave the comparator concept unrequired and screen comparisons, or expand and test its wording before making it mandatory.",
          "status": "resolved",
          "response": "The version 5 final query does not AND the comparator block. It remains a tested optional candidate, and the comparison is screened. The current evaluation retrieves PMID 28358542."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The final query has an Entrez date ceiling of 2017-11-29. Using this saved query as a current search would omit later-entered records.",
          "recommendation": "Retain the cutoff only when reporting this historical snapshot; rerun with a current search date for an up-to-date review and report the actual search date.",
          "status": "accepted-risk",
          "response": "The packet identifies 2017-11-29 as the harness Entrez snapshot boundary and states there is no publication-date limit. This is acceptable for the documented historical evaluation; a current rerun is needed before using the strategy as an up-to-date search."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional small-sample, simulation, and comparator concepts were tested. The small-sample and simulation blocks each miss the known relevant development record, and the comparator remains unrequired because its vocabulary may miss eligible alternatives. Outcomes and field are assigned to screening. The 12,364-record result exceeds the 10,000-record budget, but further narrowing with the tested blocks would risk sensitivity; screening capacity was not supplied.",
          "evidence": "The packet reports counts of 12,364 without and 628 with the small-sample block, 12,364 without and 4,072 with the simulation block, and 12,364 without and 4,124 with the comparator block. Both small-sample and simulation blocks list PMID 28358542 as lost. The final query leaves all three blocks unrequired."
        }
      ]
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-30T14:29:03+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in performance, accuracy, and bias?
- Framework: method performance
- Scope confirmed by user: yes (User requested no follow-up questions; scope roles and assumptions are recorded and proceeding without confirmation. No known relevant articles were supplied. Harness cutoff is PubMed Entrez date 2017-11-29 via PSB_AS_OF; no publication-date limit is applied. No web search is used. Critic F001 test evidence: before/after final model-family counts were 2,136 and 2,173, with no known records lost; PubMed count for the incremental query below was 37. Exact incremental query: (SEM[tiab] AND ("Bayes Theorem"[Mesh] OR "Markov Chains"[Mesh] OR Bayes*[tiab] OR Bayesian[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "Markov chain Monte-Carlo"[tiab] OR "Monte Carlo Markov chain"[tiab] OR "Gibbs sampling"[tiab] OR "prior distribution"[tiab] OR "prior distributions"[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian inference"[tiab]) NOT ("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Mediation Analysis"[Mesh] OR "structural equation model"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "structural equation models"[tiab] OR "latent variable model"[tiab] OR "latent variable models"[tiab] OR "latent variable modeling"[tiab] OR "latent variable modelling"[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "factor analysis"[tiab] OR "latent growth"[tiab] OR "growth curve model"[tiab] OR "growth mixture"[tiab] OR "latent class"[tiab] OR "multilevel model"[tiab] OR "hierarchical model"[tiab] OR multilevel[tiab] OR mediation[tiab] OR "path analysis"[tiab] OR "path model"[tiab] OR "indirect effect"[tiab])). All 37 increment PMIDs were sampled and abstracts fetched: 28860492, 28781553, 28594224, 28569630, 28369873, 27989906, 27760125, 27418702, 27168986, 27057832, 26986267, 26877685, 26825341, 26823632, 26681991, 25627247, 24768562, 24636526, 24465976, 23927904, 23063546, 22465401, 22348127, 21501217, 27021721, 19786021, 19592185, 17985305, 17562014, 14635763, 11119467, 18282892, 8934587, 8574964, 7644856, 2305421, 6166840. Screening judgment: none met the review's full eligibility criteria; the abstracts show acronym collisions or unrelated uses (including standard error of the mean, scanning electron microscopy, stochastic EM, Bayesian phylogenetic analysis, and unrelated Bayesian models), and one broad Bayesian-psychology review that does not evaluate SEM estimator performance. SEM[tiab] is retained to cover acronym-only SEM records at a 37-record increment.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family | search | This is the application family defining the methods question, with named members including structural equation modeling, CFA, latent growth/class models, multilevel models, and mediation. |
| Bayesian estimation | search | The method under evaluation is central and is usually named as Bayesian estimation, Bayesian inference, or MCMC. |
| Small-sample or few-cluster context | optional | This defines the application context and may be named in titles/abstracts, but qualifying studies may report sample-size conditions only in the full text; test as an optional block. |
| Monte Carlo or simulation study | optional | Simulation is a recognizable design label, but abstracts may not state it consistently; test its effect before deciding whether to AND it. |
| Frequentist, maximum-likelihood, or alternative estimator comparator | screen | Comparators are inconsistently named and are eligibility properties best assessed during screening. |
| Estimator performance, accuracy, and bias outcomes | screen | Outcome language varies and may occur only in the full text. |
| Peer-reviewed methodological paper in social/behavioural sciences | screen | Disciplinary relevance and peer-review status are not reliably searchable as article concepts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:28:15+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 2,173
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"Mediation Analysis"[Mesh]` | 1 | none |
| 5 | `"structural equation model"[tiab]` | 1,934 | none |
| 6 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 7 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 8 | `"structural equation models"[tiab]` | 1,695 | none |
| 9 | `SEM[tiab]` | 81,594 | none |
| 10 | `"latent variable model"[tiab]` | 253 | none |
| 11 | `"latent variable models"[tiab]` | 277 | none |
| 12 | `"latent variable modeling"[tiab]` | 171 | none |
| 13 | `"latent variable modelling"[tiab]` | 39 | none |
| 14 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 15 | `CFA[tiab]` | 7,128 | none |
| 16 | `"factor analysis"[tiab]` | 33,735 | none |
| 17 | `"latent growth"[tiab]` | 1,734 | none |
| 18 | `"growth curve model"[tiab]` | 270 | none |
| 19 | `"growth mixture"[tiab]` | 791 | none |
| 20 | `"latent class"[tiab]` | 4,129 | none |
| 21 | `"multilevel model"[tiab]` | 799 | none |
| 22 | `"hierarchical model"[tiab]` | 1,993 | none |
| 23 | `multilevel[tiab]` | 25,930 | none |
| 24 | `mediation[tiab]` | 22,917 | none |
| 25 | `"path analysis"[tiab]` | 4,075 | none |
| 26 | `"path model"[tiab]` | 931 | none |
| 27 | `"indirect effect"[tiab]` | 5,281 | none |
| 28 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27` | 206,601 | none |
| 29 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 30 | `"Markov Chains"[Mesh]` | 13,023 | none |
| 31 | `Bayes*[tiab]` | 39,780 | none |
| 32 | `Bayesian[tiab]` | 35,533 | none |
| 33 | `MCMC[tiab]` | 1,577 | none |
| 34 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 35 | `"Markov chain Monte-Carlo"[tiab]` | 3,122 | none |
| 36 | `"Monte Carlo Markov chain"[tiab]` | 133 | none |
| 37 | `"Gibbs sampling"[tiab]` | 712 | none |
| 38 | `"prior distribution"[tiab]` | 661 | none |
| 39 | `"prior distributions"[tiab]` | 568 | none |
| 40 | `"Bayesian estimation"[tiab]` | 966 | none |
| 41 | `"Bayesian inference"[tiab]` | 3,376 | none |
| 42 | `#29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41` | 58,709 | none |
| 43 | `#28 AND #42` | 2,173 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Mediation Analysis"[Mesh] OR "structural equation model"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "structural equation models"[tiab] OR SEM[tiab] OR "latent variable model"[tiab] OR "latent variable models"[tiab] OR "latent variable modeling"[tiab] OR "latent variable modelling"[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "factor analysis"[tiab] OR "latent growth"[tiab] OR "growth curve model"[tiab] OR "growth mixture"[tiab] OR "latent class"[tiab] OR "multilevel model"[tiab] OR "hierarchical model"[tiab] OR multilevel[tiab] OR mediation[tiab] OR "path analysis"[tiab] OR "path model"[tiab] OR "indirect effect"[tiab]) AND ("Bayes Theorem"[Mesh] OR "Markov Chains"[Mesh] OR Bayes*[tiab] OR Bayesian[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "Markov chain Monte-Carlo"[tiab] OR "Monte Carlo Markov chain"[tiab] OR "Gibbs sampling"[tiab] OR "prior distribution"[tiab] OR "prior distributions"[tiab] OR "Bayesian estimation"[tiab] OR "Bayesian inference"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small-sample or few-cluster context | left out | 2,173 / 105 | 95.2% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out: sample-size context would reduce the current core set from 2,173 to 105, but only one known in-scope record is available, below the 15-record safety threshold for AND-ing. Screened all 30 current removed records by title/abstract; none met all inclusion criteria. Retain context for screening because small-sample status may only be described in full text. |
| Monte Carlo or simulation study | left out | 2,173 / 786 | 63.8% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out: simulation terms would materially reduce the current core set, but only one known in-scope record is available, below the 15-record safety threshold for AND-ing. Screened all 30 current removed records by title/abstract; none met all inclusion criteria. Retain design for screening because eligible simulation studies may be described inconsistently or only in full text. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 58,709 | 0 |
| bayesian_estimation | 206,601 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 15,108 | initial | none | Initial broad method-performance search: AND core SEM-family and Bayesian-estimation blocks; sample-size context and simulation design kept as candidates for optional-block testing. No known records supplied; cutoff is Entrez date 2017-11-29. |
| 2 | 2,136 | sem_family: +0 / -1 | none | Removed generic Models, Statistical MeSH heading after its 370,212-record standalone count showed it was too broad for the SEM-family block; retained direct SEM/latent-family descriptors and bare named family members. Recheck coverage against the screened relevant article. |
| 3 | 2,173 | sem_family: +1 / -0 | none | Added SEM[tiab] per PRESS critic F001 as a test of acronym-only coverage; inspect its title/abstract count and incremental retrieval under the Bayesian block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F001 should-fix open
- Round 2 on version 3: 1 findings; F001 should-fix open
- Round 3 on version 3: 1 findings; F001 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 909 NCBI requests logged (482 from cache); strategy sha256 838eb4f6dd23._

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
      "checked_at": "2026-09-30T14:28:15+00:00",
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
      "checked_at": "2026-09-30T14:28:15+00:00",
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
      "checked_at": "2026-09-30T14:28:15+00:00",
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
      "checked_at": "2026-09-30T14:28:15+00:00",
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
      "checked_at": "2026-09-30T14:28:15+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Markov Chains",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:28:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008390",
          "name": "Markov Chains",
          "type": "descriptor",
          "scope_note": "A stochastic process such that the conditional probability distribution for a state at any future instant, given the present state, is unaffected by any additional knowledge of the past history of the system.",
          "tree_numbers": [
            "E05.318.740.600.500",
            "E05.318.740.996.500",
            "G17.830.500",
            "N05.715.360.750.625.500",
            "N05.715.360.750.770.500",
            "N06.850.520.830.600.500",
            "N06.850.520.830.996.500"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008390",
      "preferred_label": "Markov Chains",
      "type": "descriptor",
      "location": "vocabulary:29",
      "term": {
        "text": "\"Markov Chains\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"Mediation Analysis\"[MeSH Terms] OR \"structural equation model\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"structural equation models\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"latent variable model\"[Title/Abstract] OR \"latent variable models\"[Title/Abstract] OR \"latent variable modeling\"[Title/Abstract] OR \"latent variable modelling\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model\"[Title/Abstract] OR \"growth mixture\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"multilevel model\"[Title/Abstract] OR \"hierarchical model\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"path analysis\"[Title/Abstract] OR \"path model\"[Title/Abstract] OR \"indirect effect\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Markov Chains\"[MeSH Terms] OR \"bayes*\"[Title/Abstract] OR \"Bayesian\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"markov chain monte carlo\"[Title/Abstract] OR \"markov chain monte carlo\"[Title/Abstract] OR \"Monte Carlo Markov chain\"[Title/Abstract] OR \"Gibbs sampling\"[Title/Abstract] OR \"prior distribution\"[Title/Abstract] OR \"prior distributions\"[Title/Abstract] OR \"Bayesian estimation\"[Title/Abstract] OR \"Bayesian inference\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "172602fefbe5851f201222027060b313fc8c0939d33226ea4abbde07b49cf7ea",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two searched concepts correspond to the locked model-family and Bayesian-estimation concepts. The named model-family examples in the question and eligibility are represented, including bare mediation, multilevel, CFA, latent growth, and latent class terms. Sample-size, simulation, comparator, and outcome concepts are not made mandatory AND blocks; that is consistent with the stated recall rationale and their screening roles."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are OR-combined internally and AND-combined with each other. No proximity operators or Boolean precedence problems are evident in the parenthesized query. The candidate concepts are evaluated separately rather than silently added as required blocks."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH descriptors are verified in the packet and appear in their intended OR blocks. Factor Analysis, Statistical is broad, but the strategy preserves recall and its breadth is acknowledged in the optional-block rationale; no narrower replacement is evidenced here."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The model-family block covers the spelled-out structural equation terms but omits the common bare acronym SEM. This is a plausible lexical route for records that use the acronym without spelling out the term in title or abstract."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The translated query has no reported PubMed errors, warnings, or translation issues, and its field tags and parentheses are consistent. The reported clause translations and combined translation are syntactically valid."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, or study-design filter is applied. The Entrez Date cutoff through 2017-11-29 is disclosed as the harness as-of boundary, not represented as an eligibility limit."
        }
      },
      "findings": [
        {
          "id": "F001",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The structural equation model-family block does not include the bare acronym SEM[tiab]. Records may use SEM without spelling out structural equation modeling in the searchable fields. The supplied single known relevant record does not establish whether this omission causes a miss.",
          "recommendation": "Test SEM[tiab] as an additional model-family term, inspect its incremental retrieval within the Bayesian block, and screen a sample for relevance. Retain or reject it on that evidence; do not remove existing terms based only on known-record coverage.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "84d6cc8a6748785a0c94d94ca7bcc4f2b760348902c630fd74ec65c6abe80661",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks match the two designated searchable concepts. Named model-family members are represented, including bare mediation and multilevel, CFA, latent growth, and latent class terms. The small-sample and simulation concepts remain optional, consistent with their reported losses and screening rationale; comparator and outcomes remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The model-family terms and Bayesian-estimation terms are OR-combined within blocks, and the blocks are AND-combined with explicit parentheses. Candidate optional concepts are evaluated separately and are not silently made mandatory."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH descriptors are represented in their intended blocks and the packet reports no heading verification problems. Factor Analysis, Statistical and Bayes Theorem are broad, but the packet provides no narrower evidenced replacement and preserves recall."
        },
        "text_words": {
          "verdict": "revise",
          "note": "SEM[tiab] is now present, addressing F001's original lexical omission. However, the packet does not document the specified incremental SEM query yielding 37 records or its screened sample: the displayed 37 is the Gibbs sampling term's sequence number, not evidence of an incremental SEM retrieval. The current strategy and retrieval of the single known record do not establish the incremental records' relevance."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors, warnings, or translation issues for the combined query. Parentheses and field tags are consistent. The Markov chain spelling variants translate identically, which is redundant but not a syntax defect."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication, language, or study-design limits are applied. The Entrez Date cutoff through 2017-11-29 is disclosed as the harness as-of boundary rather than presented as an eligibility restriction."
        }
      },
      "findings": [
        {
          "id": "F001",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "SEM[tiab] has been added to the current model-family block, but the packet does not include the incremental SEM search result count of 37 or the screening results for its sample. The displayed numbered term 37 is Gibbs sampling, so the requested evidence cannot be verified from this packet.",
          "recommendation": "Include the exact incremental query, its 37-record result set or count basis, the screened sample and relevance judgments, and the resulting retain-or-remove rationale. Re-evaluate the term based on that evidence.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "ed95ff174037c550507255a05f67c7a45f9023c5b3dffa6c36c85540eac5457e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks correspond to the designated model-family and Bayesian-estimation concepts. Named model-family members are represented, while small-sample context and simulation remain optional for screening as supported by the reported reduction and limited known-record base."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within the two concept blocks, which are AND-combined with explicit parentheses. Optional concepts are evaluated separately and are not made mandatory."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings appear in their intended blocks. Broad headings are acknowledged; the packet provides no evidenced narrower replacements."
        },
        "text_words": {
          "verdict": "pass",
          "note": "SEM[tiab] is present. The packet now supplies the exact incremental query, a count of 37 and all 37 PMIDs with abstracts fetched. The documented screening found none met full eligibility, identified acronym collisions and unrelated Bayesian uses, and explains retaining SEM for acronym-only coverage at this 37-record increment."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors, warnings, or translation issues for the combined query; parentheses and field tags are consistent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication, language, or study-design filter is applied. The Entrez Date cutoff is disclosed as the harness as-of boundary, not an eligibility limit."
        }
      },
      "findings": [
        {
          "id": "F001",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The packet previously lacked verifiable incremental retrieval and screening evidence for SEM[tiab].",
          "recommendation": "Retain SEM[tiab] with the documented incremental-query evidence and rationale; assess the resulting screening burden during screening.",
          "status": "resolved",
          "response": "The current packet provides the exact incremental query, the 37-record count, the full list of 37 increment PMIDs, and states that abstracts were fetched and screened. None met all eligibility criteria; acronym collisions and unrelated uses were noted. SEM is retained to cover acronym-only SEM records, with the increment quantified at 37."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


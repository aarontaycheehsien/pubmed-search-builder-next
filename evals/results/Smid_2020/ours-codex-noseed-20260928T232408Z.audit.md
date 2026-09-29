# PubMed search strategy: audit

Generated 2026-09-28T23:48:30+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task
- Scope confirmed by user: yes (The user asked to proceed without clarification. Assumed the searchable core is model family AND Bayesian estimation; small-sample/few-cluster context, comparator, simulation design, performance outcomes, social/behavioural field, and peer-review status are screening criteria. No known relevant articles were supplied. PubMed is bounded by Entrez date 2017-11-29; no publication-date limit is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family (SEM, CFA, latent growth/class, multilevel, mediation) | search | The model/task family defines the review topic and can be searched by its named methods and model-family terminology. Search all named members on their own; category false because this is a model/method family, not a population or exposure category. |
| Bayesian estimation (including prior distributions and MCMC) | search | The estimation approach is central to every eligible study and usually named in title, abstract, or indexing. Frequentist/maximum-likelihood comparator will be screened because comparator terminology is inconsistently reported. |
| Small sample or few-cluster context | optional | This topic-defining context is often named in methods papers, so test an optional block; wording and thresholds vary, so require it only if the loss sample supports AND-ing. |
| Frequentist/maximum-likelihood or alternative-estimator comparison | screen | Comparator language and the specific comparison may be absent from abstracts; screen for it. |
| Monte Carlo/simulation evaluation | optional | A recognisable study design that is often named in methodological abstracts, so test it as an optional block; do not require it without measuring loss. |
| Social/behavioural sciences methodological setting | screen | Field and peer-review status are not reliably searchable as a concept; apply at screening. |
| Performance, accuracy, bias, and related properties | screen | Performance outcomes define eligibility but are heterogeneous and inconsistently named; screen. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:47:32+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 4,623
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"Mediation Analysis"[Mesh]` | 1 | none |
| 5 | `"Models, Statistical"[Mesh]` | 370,212 | none |
| 6 | `"structural equation model*"[tiab]` | 12,605 | none |
| 7 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 8 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 9 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 10 | `CFA[tiab]` | 7,128 | none |
| 11 | `"factor analysis"[tiab]` | 33,735 | none |
| 12 | `"latent variable*"[tiab]` | 3,233 | none |
| 13 | `"latent class"[tiab]` | 4,129 | none |
| 14 | `"latent growth"[tiab]` | 1,734 | none |
| 15 | `"growth curve model*"[tiab]` | 1,502 | none |
| 16 | `multilevel[tiab]` | 25,930 | none |
| 17 | `"multi-level"[tiab]` | 4,831 | none |
| 18 | `mediation[tiab]` | 22,917 | none |
| 19 | `"path analysis"[tiab]` | 4,075 | none |
| 20 | `"hierarchical model*"[tiab]` | 3,344 | none |
| 21 | `"hierarchical linear model*"[tiab]` | 2,083 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 486,209 | none |
| 23 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 24 | `Bayesian[tiab]` | 35,533 | none |
| 25 | `Bayes[tiab]` | 5,705 | none |
| 26 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 27 | `MCMC[tiab]` | 1,577 | none |
| 28 | `#23 OR #24 OR #25 OR #26 OR #27` | 47,661 | none |
| 29 | `"Monte Carlo Method"[Mesh]` | 25,842 | none |
| 30 | `simulation[tiab]` | 155,075 | none |
| 31 | `simulations[tiab]` | 148,754 | none |
| 32 | `simulated[tiab]` | 121,220 | none |
| 33 | `"Monte Carlo"[tiab]` | 41,522 | none |
| 34 | `"Computer Simulation"[Mesh]` | 211,062 | none |
| 35 | `#29 OR #30 OR #31 OR #32 OR #33 OR #34` | 493,328 | none |
| 36 | `#22 AND #28 AND #35` | 4,623 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Mediation Analysis"[Mesh] OR "Models, Statistical"[Mesh] OR "structural equation model*"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "confirmatory factor analysis"[tiab] OR CFA[tiab] OR "factor analysis"[tiab] OR "latent variable*"[tiab] OR "latent class"[tiab] OR "latent growth"[tiab] OR "growth curve model*"[tiab] OR multilevel[tiab] OR "multi-level"[tiab] OR mediation[tiab] OR "path analysis"[tiab] OR "hierarchical model*"[tiab] OR "hierarchical linear model*"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Markov chain Monte Carlo"[tiab] OR MCMC[tiab]) AND ("Monte Carlo Method"[Mesh] OR simulation[tiab] OR simulations[tiab] OR simulated[tiab] OR "Monte Carlo"[tiab] OR "Computer Simulation"[Mesh])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Small sample or few-cluster context | left out | 4,623 / 287 | 93.8% | none | 0/30 (up to 10% of removed records could be relevant) | The refreshed loss sample contained no clearly eligible record (0/30), but screening also surfaced PMID 26735714, a Monte Carlo comparison of Bayesian MCMC and other mediation methods in social science whose abstract does not make the sample-size regime clear. Because sample-size context may be specified only in full text, and the base search is under the 10,000-record workload budget, I am leaving this block out to preserve sensitivity. Screen sample-size and cluster-count eligibility at full-text screening. |
| Monte Carlo/simulation evaluation | AND-ed | 12,314 / 4,623 | 62.5% | none | 0/30 (up to 10% of removed records could be relevant) | The refreshed 30-record random loss sample, screened against all inclusion criteria, contained no eligible small-sample SEM-family estimator-comparison simulation study (0/30). All six screened-in development records are retrieved by the simulation block; adding it reduces the uncapped base count 12,314 to 4,623 (62.5%). The finite sample cannot rule out relevant studies whose simulation design is not named in indexed fields. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_models | 11,583 | 0 |
| bayesian_estimation | 40,959 | 0 |
| simulation | 12,314 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block strategy: SEM/latent model family AND Bayesian estimation; simulation remains an optional design block for testing. No known articles were supplied, so recall is not estimated. |
| 2 | 11,493 | sem_models: +19 / -0; bayesian_estimation: +5 / -0 | none | Initial model-family AND Bayesian-estimation strategy; simulation design remains optional pending count and loss-sample review. No known articles were supplied, so recall is not estimated. |
| 3 | 3,589 | simulation: +5 / -0 | none | Screened 48-record precise PubMed pilot and identified two eligible development records; added both to relevant set and mined their vocabulary. AND-ed simulation after 0/30 relevant records in random loss sample and 68.8% reduction; remaining omission risk documented. |
| 4 | 4,351 | simulation: +1 / -0 | none | Added three screened-in pilot papers and the Computer Simulation MeSH heading carried by the 2016 multilevel SEM study. Testing small-sample/few-cluster context as an optional block because it is a named topic-defining feature. |
| 5 | 4,351 | limits/combination | none | The small-sample optional block initially missed relevant PMID 26717127; its abstract says small number of groups. Added small number of groups/number of groups/few groups terms to recover it before re-sampling. |
| 6 | 273 | small_sample: +12 / -0 | none | Added group-number variants to recover relevant PMID 26717127, screened a refreshed 30-record small-sample loss sample (0 eligible), and AND-ed the small-sample block given no known losses and a 93.7% reduction. Simulation block decision refreshed after adding Computer Simulation MeSH. |
| 7 | 287 | sem_models: +2 / -0; small_sample: +0 / -1 | none | Removed zero-hit phrase-index warning for small number of groups after checking its translation; the term number of groups retrieves the relevant small-groups record. Added hierarchical model wording as a multilevel-model synonym for recall. |
| 8 | 4,623 | small_sample: +0 / -11 | none | Small-sample block left out despite large reduction: a plausible mediation-method paper has unclear sample-size context in its abstract, while baseline volume is within the screening budget. Preserve sensitivity; sample-size eligibility remains for full-text screening. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 8 (Same-context critic: no separate fresh-context reviewer was available under the active collaboration constraints. I reviewed the packet against the six PRESS domains.): 0 findings; 
- Round 2 on version 8 (Same-context second revision review: no separate fresh-context reviewer was available under the active collaboration constraints. I re-read the current bound packet; it reports no earlier findings and no unresolved validation issues.): 0 findings; 
- Round 3 on version 8 (Same-context closing review: earlier revision rounds recorded no findings, and the current packet shows no mandatory validation dispositions outstanding.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1150 NCBI requests logged (664 from cache); strategy sha256 7d9c2505843e._

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
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Monte Carlo Method",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Monte Carlo Method\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Computer Simulation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:47:32+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Computer Simulation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"Mediation Analysis\"[MeSH Terms] OR \"models, statistical\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable*\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model*\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"multi-level\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"path analysis\"[Title/Abstract] OR \"hierarchical model*\"[Title/Abstract] OR \"hierarchical linear model*\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"MCMC\"[Title/Abstract]) AND (\"Monte Carlo Method\"[MeSH Terms] OR \"simulation\"[Title/Abstract] OR \"simulations\"[Title/Abstract] OR \"simulated\"[Title/Abstract] OR \"Monte Carlo\"[Title/Abstract] OR \"Computer Simulation\"[MeSH Terms]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 8,
      "review_sha256": "6dafc7e8cfc02874fbacedb500a219181f619fd8686cd72025c388ba9f056769",
      "note": "Same-context critic: no separate fresh-context reviewer was available under the active collaboration constraints. I reviewed the packet against the six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched core is SEM/latent-variable methods AND Bayesian estimation. The listed model-family members are represented by bare terms and MeSH; simulation was tested and AND-ed after 0/30 relevant records in its loss sample and material reduction. Small-sample wording was tested and left out to preserve sensitivity; screen that criterion at full text."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR joins synonyms within each concept and AND joins the searchable concepts; no NOT or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Bayes Theorem, Factor Analysis, Statistical, Latent Class Analysis, Multilevel Analysis, Mediation Analysis, Models, Statistical, Monte Carlo Method, and Computer Simulation are explicitly tagged and authority-checked. Explosions are retained by default; broad Models, Statistical is retained for recall and will add noise."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text terms include spelling variants, SEM and CFA, named model members, hierarchical models, Bayesian/Bayes, MCMC, Monte Carlo, simulation variants, and simulation design headings. No unresolved phrase-index warnings remain."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms have explicit fields; PubMed translations have no remaining syntax or translation issues; safe truncation is used."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or study-design filter is applied. The effective Entrez-entry cutoff is 2017-11-29 as required."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 8,
      "review_sha256": "6dafc7e8cfc02874fbacedb500a219181f619fd8686cd72025c388ba9f056769",
      "note": "Same-context second revision review: no separate fresh-context reviewer was available under the active collaboration constraints. I re-read the current bound packet; it reports no earlier findings and no unresolved validation issues.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The SEM-family members are represented by broad member terms. Bayesian estimation and simulation are the only required AND concepts. Small-sample wording remains unrequired after optional testing; screen eligibility at full text."
        },
        "operators": {
          "verdict": "pass",
          "note": "Boolean structure is OR within concepts and AND across concepts; no inappropriate exclusion or proximity operation is present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Explicit MeSH headings cover factor analysis, latent class, multilevel analysis, mediation, statistical models, Bayesian analysis, and simulation. Broad headings may add noise but were retained for recall."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text vocabulary includes model-family synonyms and spelling variants, Bayesian/Bayes/MCMC, and simulation/Monte Carlo variants. The zero-hit small-number-of-groups phrase was removed after inspecting its PubMed translation; number of groups remains and retrieves the known few-groups record."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Explicit field tags, balanced Boolean syntax, and current PubMed translations are valid; no open phrase warnings remain."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No ad hoc filters or limits remain. The Entrez entry-date bound is 2017-11-29 and is not a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 8,
      "review_sha256": "6dafc7e8cfc02874fbacedb500a219181f619fd8686cd72025c388ba9f056769",
      "note": "Same-context closing review: earlier revision rounds recorded no findings, and the current packet shows no mandatory validation dispositions outstanding.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No earlier findings were raised. The optional-block decisions and full-text screening of sample-size context are documented in the bound protocol and audit."
        },
        "operators": {
          "verdict": "pass",
          "note": "No earlier findings were raised; Boolean structure remains sound."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "No earlier findings were raised; controlled vocabulary terms remain authority-checked and explicitly tagged."
        },
        "text_words": {
          "verdict": "pass",
          "note": "No earlier findings were raised; broad text vocabulary remains appropriate for recall-first retrieval."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No earlier findings were raised; no technical or translation issues remain."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No earlier findings were raised; only the required Entrez as-of date boundary is used."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


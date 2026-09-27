# PubMed search strategy: audit

Generated 2026-09-27T15:14:23+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task + application context
- Scope confirmed by user: no (User requested no questions or pauses; scope was provisionally set from supplied criteria without user confirmation. Historical cutoff 2017-11-29 imposed by run instructions; PubMed entry date (EDAT) is used. No known relevant articles were supplied; no language or publication-type limits; peer-review/social-behavioural eligibility is screened.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and related latent-variable models | search | The model family defines the methodological application and is likely named in records. |
| Bayesian estimation | search | Bayesian estimation is the focal method and is commonly named in titles, abstracts, or indexing. |
| Small samples or few clusters | screen | Sample-size terminology is inconsistent; screen rather than require it in every abstract. |
| Frequentist or maximum-likelihood comparison | screen | Comparators can be underreported and are handled at screening. |
| Estimator performance, accuracy, and bias | screen | Outcome terms are inconsistently reported and should not be required. |
| Monte Carlo or simulation study | screen | Design is an eligibility criterion that may be absent from indexing and abstracts. |
| Social or behavioural sciences; peer-reviewed methodological paper | screen | Discipline and publication status are eligibility criteria, not reliable search blocks. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2017-11-29
- Total records: 870
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 |
| 2 | `"structural equation model*"[tiab]` | 12,605 |
| 3 | `"structural equation modeling"[tiab]` | 7,913 |
| 4 | `"structural equation modelling"[tiab]` | 1,788 |
| 5 | `"latent variable model*"[tiab]` | 671 |
| 6 | `"latent variable"[tiab]` | 2,007 |
| 7 | `"confirmatory factor analys*"[tiab]` | 10,281 |
| 8 | `"factor analys*"[tiab]` | 38,459 |
| 9 | `"path analys*"[tiab]` | 5,178 |
| 10 | `"latent growth"[tiab]` | 1,734 |
| 11 | `"growth mixture model*"[tiab]` | 768 |
| 12 | `"latent class model*"[tiab]` | 603 |
| 13 | `"multilevel structural equation"[tiab]` | 166 |
| 14 | `"mediation model*"[tiab]` | 1,442 |
| 15 | `SEM[tiab]` | 81,594 |
| 16 | `"latent covariate model*"[tiab]` | 3 |
| 17 | `"latent group mean"[tiab]` | 2 |
| 18 | `"mediational model*"[tiab]` | 438 |
| 19 | `"logistic mediation"[tiab]` | 3 |
| 20 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 151,225 |
| 21 | `"Bayes Theorem"[Mesh]` | 28,985 |
| 22 | `Bayesian[tiab]` | 35,533 |
| 23 | `Bayes[tiab]` | 5,706 |
| 24 | `"Bayesian estimat*"[tiab]` | 1,379 |
| 25 | `"Bayesian approach*"[tiab]` | 3,793 |
| 26 | `"Bayesian method*"[tiab]` | 3,265 |
| 27 | `"Bayesian analys*"[tiab]` | 3,354 |
| 28 | `"Bayesian structural equation"[tiab]` | 46 |
| 29 | `"Bayesian SEM"[tiab]` | 4 |
| 30 | `"prior distribution*"[tiab]` | 1,143 |
| 31 | `"posterior distribution*"[tiab]` | 1,486 |
| 32 | `"Markov chain Monte Carlo"[tiab]` | 3,122 |
| 33 | `MCMC[tiab]` | 1,577 |
| 34 | `"Gibbs sampling"[tiab]` | 712 |
| 35 | `#21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 48,358 |
| 36 | `#20 AND #35` | 870 |

### Strategy (single line, for copying into PubMed)

```text
("Factor Analysis, Statistical"[Mesh] OR "structural equation model*"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "latent variable model*"[tiab] OR "latent variable"[tiab] OR "confirmatory factor analys*"[tiab] OR "factor analys*"[tiab] OR "path analys*"[tiab] OR "latent growth"[tiab] OR "growth mixture model*"[tiab] OR "latent class model*"[tiab] OR "multilevel structural equation"[tiab] OR "mediation model*"[tiab] OR SEM[tiab] OR "latent covariate model*"[tiab] OR "latent group mean"[tiab] OR "mediational model*"[tiab] OR "logistic mediation"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimat*"[tiab] OR "Bayesian approach*"[tiab] OR "Bayesian method*"[tiab] OR "Bayesian analys*"[tiab] OR "Bayesian structural equation"[tiab] OR "Bayesian SEM"[tiab] OR "prior distribution*"[tiab] OR "posterior distribution*"[tiab] OR "Markov chain Monte Carlo"[tiab] OR MCMC[tiab] OR "Gibbs sampling"[tiab])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem | 48,358 | 0 |
| bayesian | 151,225 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 34,975 | initial | none | Initial two-block draft: SEM/latent-variable models AND Bayesian estimation. Sample size, comparator, outcomes, simulation design, and field/publication eligibility remain screening criteria to protect recall. MeSH uses pre-cutoff descriptors; the 2019 Latent Class Analysis descriptor was excluded. |
| 2 | 869 | sem: +2 / -2 | none | Expanded the latent-variable model vocabulary from screened pilot abstracts (latent covariate model; latent group mean) and removed generic Models, Statistical and Statistics as Topic MeSH terms after random sampling showed severe off-topic retrieval. Kept the focused Factor Analysis, Statistical heading and broad within-family text vocabulary. |
| 3 | 869 | limits/combination | none | Added the additional screened relevant PMID 27594086 discovered by a second precision pilot. No changes to strategy vocabulary; prior candidate and neighbor screens found no further clearly eligible records. |
| 4 | 869 | limits/combination | none | Added screened-in neighbor PMID 28715231 (Bayesian versus ML item factor analysis under sparse/limited-sample conditions). The existing factor-analysis and Bayesian terms retrieve it; no strategy change. |
| 5 | 870 | sem: +2 / -0 | none | Added two in-block mediation variants mined from the screened relevant PMID 15316954 (mediational model; logistic mediation); this mediation-family record was added to the development set. Comparator, small-sample context, and simulation remain screening criteria. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 0 findings; 
- Round 2 on version 5: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 488 NCBI requests logged (219 from cache); strategy sha256 00f7b29a6c3f._

## Rationale

The review question is a method-performance question, so the search combines two defining, searchable concepts: SEM/related latent-variable models AND Bayesian estimation. The SEM block includes the pre-existing MeSH descriptor `Factor Analysis, Statistical` and title/abstract wording for structural equation models, CFA/factor analysis, path and mediation models, latent growth/class models, and multilevel forms. The Bayesian block combines the pre-cutoff MeSH descriptor `Bayes Theorem` with Bayesian, prior/posterior, MCMC, and Gibbs-sampling terminology. The `Latent Class Analysis` descriptor found during live vocabulary lookup was introduced in 2019 and was not used under the historical cutoff. Generic MeSH headings `Models, Statistical` and `Statistics as Topic` were removed after a random sample from the initial 34,975-record draft showed substantial off-topic retrieval; the revised search retrieved the then-known development set after their removal. Small-sample/few-cluster context, the comparator, outcomes, simulation design, and field/publication eligibility remain screening criteria. No language or publication-type filter was applied. The run-specific historical restriction is PubMed entry date through 2017-11-29, added to the copyable query below.

### Cutoff-bound query for this run

The run-specific EDAT bound is included explicitly here so the query reproduces the historical cutoff used for the count:

```text
("Factor Analysis, Statistical"[Mesh] OR "structural equation model*"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "latent variable model*"[tiab] OR "latent variable"[tiab] OR "confirmatory factor analys*"[tiab] OR "factor analys*"[tiab] OR "path analys*"[tiab] OR "latent growth"[tiab] OR "growth mixture model*"[tiab] OR "latent class model*"[tiab] OR "multilevel structural equation"[tiab] OR "mediation model*"[tiab] OR SEM[tiab] OR "latent covariate model*"[tiab] OR "latent group mean"[tiab] OR "mediational model*"[tiab] OR "logistic mediation"[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Bayesian estimat*"[tiab] OR "Bayesian approach*"[tiab] OR "Bayesian method*"[tiab] OR "Bayesian analys*"[tiab] OR "Bayesian structural equation"[tiab] OR "Bayesian SEM"[tiab] OR "prior distribution*"[tiab] OR "posterior distribution*"[tiab] OR "Markov chain Monte Carlo"[tiab] OR MCMC[tiab] OR "Gibbs sampling"[tiab]) AND 1800/01/01:2017/11/29[Date - Entry]
```

## How known records were found

The user supplied no seed articles. A PubMed pilot for a topic-matched systematic review returned 0 records. Precision pilots returned 1 record for Bayesian structural equation plus small-sample wording, 13 for Bayesian CFA plus simulation, 17 for SEM/factor analysis plus Bayesian/MCMC, simulation, and maximum likelihood, and 10 for Bayesian plus small-sample/ few-group and SEM-family wording. These result lists overlap; title and abstract candidates were screened against the supplied eligibility criteria. A PubMed similar-record search returned 29 candidates; abstracts were retrieved for 28 (one candidate was unavailable). Seven records were screened in as relevant and used as a development set: PMIDs 15316954, 24550881, 26579002, 26717127, 26745462, 27594086, and 28715231. No records were held out, so there is no independent validation set.

## Critic dispositions

Round 1 reviewed version 4 and passed all six PRESS domains with no findings. Round 2 reviewed version 5 and also passed all six domains with no findings. The second round followed addition of mediation terminology found in a screened relevant abstract. These were independent-context, automated PRESS-structured internal critiques, not information-specialist peer review.

## Open risks for the peer reviewer

Recall was not independently validated; 7/7 is relative recall on a small development set only, not sensitivity. A random sample showed that the broader SEM/factor-analysis and Bayesian vocabulary still retrieves off-topic statistical and biomedical records. The standalone acronym `SEM`, generic factor-analysis wording, and Bayes-related indexing are retained for recall and require screening. PubMed is the only database searched. The historical date bound is an imposed run constraint; confirm whether it is appropriate for the actual review protocol. Have an information specialist PRESS-review the strategy before use.
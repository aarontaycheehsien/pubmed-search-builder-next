# PubMed search strategy: audit

Generated 2026-09-29T18:53:04+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: method + task + application context
- Scope confirmed by user: yes (User asked to proceed without questions. Scope roles are agent-set from the supplied question and eligibility criteria; no user confirmation was obtained. PubMed retrieval is bounded by PSB_AS_OF=2017-11-29 as required by the harness; no publication-date limit is added. No known relevant records were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family (including CFA, latent growth/class, multilevel, and mediation models) | search | The model family defines the review topic and can be named in title, abstract, or MeSH. The block will include the named family members as well as SEM terminology. |
| Bayesian estimation | search | Bayesian estimation is the method being evaluated and is central to every eligible record. |
| Small-sample or few-cluster estimation context | optional | Small samples define eligibility and may be named in abstracts, but reporting is inconsistent; test the block before deciding whether to AND it. |
| Frequentist/maximum-likelihood comparison, simulation design, estimator performance outcomes, and social/behavioural science field | screen | Comparators, simulation methods, performance outcomes, and discipline are unreliable as required PubMed blocks and will be assessed during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T18:52:05+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 1,346
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Latent Class Analysis"[Mesh]` | 81 | none |
| 3 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 4 | `"Mediation Analysis"[Mesh]` | 1 | none |
| 5 | `"structural equation model"[tiab]` | 1,934 | none |
| 6 | `"structural equation models"[tiab]` | 1,695 | none |
| 7 | `"structural equation"[tiab]` | 12,948 | none |
| 8 | `"equation modeling"[tiab]` | 8,161 | none |
| 9 | `"equation modelling"[tiab]` | 1,842 | none |
| 10 | `"equation models"[tiab]` | 2,761 | none |
| 11 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 12 | `"structural equation modelling"[tiab]` | 1,788 | none |
| 13 | `"confirmatory factor analysis"[tiab]` | 8,085 | none |
| 14 | `"confirmatory factor analyses"[tiab]` | 2,597 | none |
| 15 | `"factor analysis"[tiab]` | 33,735 | none |
| 16 | `"latent variable model"[tiab]` | 253 | none |
| 17 | `"latent variable models"[tiab]` | 277 | none |
| 18 | `"latent variable modeling"[tiab]` | 171 | none |
| 19 | `"latent variable modelling"[tiab]` | 39 | none |
| 20 | `"latent growth model"[tiab]` | 115 | none |
| 21 | `"latent growth models"[tiab]` | 187 | none |
| 22 | `latent growth[tiab]` | 1,734 | none |
| 23 | `"latent growth curve"[tiab]` | 928 | none |
| 24 | `"latent class model"[tiab]` | 304 | none |
| 25 | `"latent class models"[tiab]` | 274 | none |
| 26 | `latent class[tiab]` | 4,129 | none |
| 27 | `"growth curve model"[tiab]` | 270 | none |
| 28 | `"growth curve models"[tiab]` | 584 | none |
| 29 | `"multilevel model"[tiab]` | 799 | none |
| 30 | `"multilevel models"[tiab]` | 1,667 | none |
| 31 | `multilevel[tiab]` | 25,930 | none |
| 32 | `"hierarchical linear model"[tiab]` | 219 | none |
| 33 | `"hierarchical linear models"[tiab]` | 504 | none |
| 34 | `mediation[tiab]` | 22,917 | none |
| 35 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 115,133 | none |
| 36 | `"Bayes Theorem"[Mesh]` | 28,985 | none |
| 37 | `Bayesian[tiab]` | 35,533 | none |
| 38 | `Bayes[tiab]` | 5,705 | none |
| 39 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 40 | `MCMC[tiab]` | 1,577 | none |
| 41 | `"prior distribution"[tiab]` | 661 | none |
| 42 | `"prior distributions"[tiab]` | 568 | none |
| 43 | `"posterior distribution"[tiab]` | 1,034 | none |
| 44 | `"posterior distributions"[tiab]` | 521 | none |
| 45 | `#36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44` | 48,117 | none |
| 46 | `#35 AND #45` | 1,346 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Latent Class Analysis"[Mesh] OR "Multilevel Analysis"[Mesh] OR "Mediation Analysis"[Mesh] OR "structural equation model"[tiab] OR "structural equation models"[tiab] OR "structural equation"[tiab] OR "equation modeling"[tiab] OR "equation modelling"[tiab] OR "equation models"[tiab] OR "structural equation modeling"[tiab] OR "structural equation modelling"[tiab] OR "confirmatory factor analysis"[tiab] OR "confirmatory factor analyses"[tiab] OR "factor analysis"[tiab] OR "latent variable model"[tiab] OR "latent variable models"[tiab] OR "latent variable modeling"[tiab] OR "latent variable modelling"[tiab] OR "latent growth model"[tiab] OR "latent growth models"[tiab] OR latent growth[tiab] OR "latent growth curve"[tiab] OR "latent class model"[tiab] OR "latent class models"[tiab] OR latent class[tiab] OR "growth curve model"[tiab] OR "growth curve models"[tiab] OR "multilevel model"[tiab] OR "multilevel models"[tiab] OR multilevel[tiab] OR "hierarchical linear model"[tiab] OR "hierarchical linear models"[tiab] OR mediation[tiab]) AND ("Bayes Theorem"[Mesh] OR Bayesian[tiab] OR Bayes[tiab] OR "Markov chain Monte Carlo"[tiab] OR MCMC[tiab] OR "prior distribution"[tiab] OR "prior distributions"[tiab] OR "posterior distribution"[tiab] OR "posterior distributions"[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Small-sample or few-cluster estimation context | left out | 1,346 / 26 | 98.1% | none | 0/30 (up to 10% of removed records could be relevant) | Leave the small-sample block out: only four screened relevant records are known, below the 15-record threshold required to justify AND-ing; the current 30-record loss sample contained no eligible record, but cannot establish safety at this niche's low prevalence. The block removes most of the core result, and small-sample reporting may be inconsistent. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sem_family | 48,117 | 0 |
| bayesian_estimation | 115,133 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 820 | initial | none | Initial recall-first draft; SEM-family and Bayesian estimation are searched, while small-sample wording is optional and design/comparator/outcome/field remain screening criteria. |
| 2 | 845 | sem_family: +1 / -0 | none | Added the mined phrase 'equation models' from both screened relevant records in the SEM-family block; it broadens model wording without requiring comparator, design, or outcome terms. |
| 3 | 852 | sem_family: +3 / -0 | none | Added 'structural equation' and spelling variants 'equation modeling/modelling' from screened records; these broaden within-block phrasing, with no comparator or design restriction. |
| 4 | 1,346 | sem_family: +3 / -0 | none | Resolved internal critic finding R1-01 by adding the required bare-name terms latent growth, latent class, and multilevel to the SEM-family block; checking retrieval and translation. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-01 must-fix open
- Round 2 on version 4: 2 findings; R1-01 must-fix resolved, R2-01 should-fix rejected
- Round 3 on version 4: 2 findings; R1-01 must-fix resolved, R2-01 should-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 735 NCBI requests logged (326 from cache); strategy sha256 c237b4c5be75._

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
      "checked_at": "2026-09-29T18:52:05+00:00",
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
      "checked_at": "2026-09-29T18:52:05+00:00",
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
      "checked_at": "2026-09-29T18:52:05+00:00",
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
      "checked_at": "2026-09-29T18:52:05+00:00",
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
      "checked_at": "2026-09-29T18:52:05+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Bayes Theorem\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Latent Class Analysis\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"Mediation Analysis\"[MeSH Terms] OR \"structural equation model\"[Title/Abstract] OR \"structural equation models\"[Title/Abstract] OR \"structural equation\"[Title/Abstract] OR \"equation modeling\"[Title/Abstract] OR \"equation modelling\"[Title/Abstract] OR \"equation models\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"structural equation modelling\"[Title/Abstract] OR \"confirmatory factor analysis\"[Title/Abstract] OR \"confirmatory factor analyses\"[Title/Abstract] OR \"factor analysis\"[Title/Abstract] OR \"latent variable model\"[Title/Abstract] OR \"latent variable models\"[Title/Abstract] OR \"latent variable modeling\"[Title/Abstract] OR \"latent variable modelling\"[Title/Abstract] OR \"latent growth model\"[Title/Abstract] OR \"latent growth models\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"latent growth curve\"[Title/Abstract] OR \"latent class model\"[Title/Abstract] OR \"latent class models\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"growth curve model\"[Title/Abstract] OR \"growth curve models\"[Title/Abstract] OR \"multilevel model\"[Title/Abstract] OR \"multilevel models\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"hierarchical linear model\"[Title/Abstract] OR \"hierarchical linear models\"[Title/Abstract] OR \"mediation\"[Title/Abstract]) AND (\"Bayes Theorem\"[MeSH Terms] OR \"Bayesian\"[Title/Abstract] OR \"Bayes\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"prior distribution\"[Title/Abstract] OR \"prior distributions\"[Title/Abstract] OR \"posterior distribution\"[Title/Abstract] OR \"posterior distributions\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "e6200dd7ca934aa6ce9739b51df343d6015af623d02a5073994ccd94a1268a13",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The required structural-equation family includes latent growth/class and multilevel models, but those members are represented only by phrases narrowed to models, curves, or analysis. The packet's translation check requires each named member to be covered by its own bare name."
        },
        "operators": {
          "verdict": "pass",
          "note": "The family and Bayesian terms are ORed within their blocks, and the two required blocks are ANDed. The optional small-sample block was tested and left out with a documented rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports no translation errors or warnings for the selected MeSH terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add bare-name text expressions for latent growth, latent class, and multilevel so records using those member names without model/curve/analysis wording can be retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The assembled query has balanced block structure and the packet reports no syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The query's EDAT boundary is documented as the harness's retrieval cutoff, and the packet states that no publication-date limit was added. No unsupported eligibility filter is ANDed into the strategy."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol names latent growth/class and multilevel as searched members of the model family, but the text terms cover them only as phrases such as \"latent growth model\", \"latent class model\", and \"multilevel model\"; the corresponding MeSH terms are also narrowed to \"Latent Class Analysis\" and \"Multilevel Analysis\". This does not meet the packet's requirement to cover each named member by its own bare name.",
          "recommendation": "Add bare-name text expressions for latent growth, latent class, and multilevel, then run another complete evaluation of the revised strategy.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "135c6723de842974369aeb425f32c66d9c30a0d7252d0824e6c8e43d07a8e06c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The revised strategy includes the bare text expressions latent growth[tiab], latent class[tiab], and multilevel[tiab], resolving the prior coverage gap for the named model-family members."
        },
        "operators": {
          "verdict": "pass",
          "note": "The terms are ORed within the model-family and Bayesian-estimation blocks, and the required blocks are ANDed. The optional small-sample block was tested and left out with a documented rationale."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The selected family headings are relevant to the named models, but Bayes Theorem is a theorem descriptor whose supplied scope note does not establish coverage of Bayesian estimation. The packet provides no reason or evidence for retaining it."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The required model-family members now have bare-name text expressions. The other listed expressions cover SEM, CFA, factor analysis, and mediation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The assembled query has balanced block structure, and the packet reports no syntax errors or translation diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The EDAT cutoff is documented as the harness retrieval boundary; no publication-date limit or unsupported eligibility filter is added."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol names latent growth/class and multilevel as searched members of the model family, but the text terms cover them only as phrases narrowed to models, curves, or analysis. The packet requires each named member to be covered by its own bare name.",
          "recommendation": "Add bare-name text expressions for latent growth, latent class, and multilevel, then run another complete evaluation of the revised strategy.",
          "status": "resolved",
          "response": "The revised strategy adds latent growth[tiab], latent class[tiab], and multilevel[tiab]; the packet reports these expressions and their translations."
        },
        {
          "id": "R2-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The Bayesian-estimation block includes \"Bayes Theorem\"[Mesh]. The supplied scope note describes a probability theorem and its applications, but does not establish that this heading represents Bayesian estimation. No retention rationale or supporting evidence is provided.",
          "recommendation": "Remove the heading or provide evidence supporting its use for Bayesian estimation, then run another complete evaluation after any rewrite or removal.",
          "status": "rejected",
          "response": "Retain this heading because the live MeSH record for D001499, Bayes Theorem, lists Bayesian Estimation and Bayesian Analysis as entry terms. The heading therefore maps directly to the target estimation concept. It is paired with explicit Bayesian and MCMC title/abstract terms."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "135c6723de842974369aeb425f32c66d9c30a0d7252d0824e6c8e43d07a8e06c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy includes bare-name text expressions for latent growth, latent class, multilevel, and mediation, resolving the earlier coverage gap."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within the required blocks, and the family and Bayesian-estimation blocks are ANDed. The optional small-sample block was tested and left out with a documented rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The family headings are relevant. The prior concern about Bayes Theorem is rejected based on the stated MeSH entry-term rationale and its pairing with explicit Bayesian and MCMC text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The required family members have bare-name text coverage, alongside terms for SEM, CFA, factor analysis, and mediation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The assembled query has balanced block structure, and the packet reports no syntax errors or translation diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The EDAT boundary is documented as the retrieval cutoff. No publication-date limit or unsupported eligibility filter is added."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The protocol names latent growth/class and multilevel as searched family members, so each needs coverage by its own bare-name expression.",
          "recommendation": "Add bare-name text expressions for latent growth, latent class, and multilevel, then run a complete evaluation.",
          "status": "resolved",
          "response": "The revised strategy includes latent growth[tiab], latent class[tiab], and multilevel[tiab], and the packet reports their translations."
        },
        {
          "id": "R2-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The Bayesian-estimation block includes \"Bayes Theorem\"[Mesh], whose scope note describes a probability theorem and does not itself establish coverage of Bayesian estimation.",
          "recommendation": "Remove the heading or provide evidence supporting its use for Bayesian estimation, then run a complete evaluation after any change.",
          "status": "rejected",
          "response": "The earlier disposition gives the MeSH entry-term rationale: the D001499 record lists Bayesian Estimation and Bayesian Analysis as entry terms. The heading is also paired with explicit Bayesian and MCMC title/abstract terms."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


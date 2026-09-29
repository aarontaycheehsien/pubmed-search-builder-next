# PubMed search strategy: audit

Generated 2026-09-29T03:38:56+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In structural equation models estimated with small samples, how does Bayesian estimation compare with frequentist (maximum likelihood) estimation in terms of performance, accuracy, and bias?
- Framework: Method performance
- Scope confirmed by user: yes (User asked to proceed without clarification; standard depth. No known relevant articles were supplied. No web search; PSB_AS_OF is set for every psb command to enforce Entrez-date cutoff 2017-11-29, with no publication-date limit. Core searchable concepts are model family and Bayesian estimation. Monte Carlo/simulation is tested as optional; small-sample/few-cluster context, comparator, discipline and peer-reviewed status are screened. PubMed-only retrieval may poorly represent social/behavioural methodological literature.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Structural equation and latent-variable model family | search | The model family defines the method application; members such as CFA, latent growth/class, multilevel and mediation can be named without the umbrella SEM label, so search the family and probe member-only wording. |
| Bayesian estimation | search | Bayesian estimation is the method under evaluation and should be named in eligible methodological reports; search Bayesian/Bayes, MCMC and related estimation terms. |
| Monte Carlo or simulation study | optional | Simulation design defines the eligible performance evaluation and is often named, but it may not be stated in every title/abstract; test its yield and loss before deciding whether to AND it. |
| Small samples or few clusters | screen | Sample-size context and few-cluster characteristics are inconsistently indexed and often only assessable in full text. |
| Frequentist, maximum-likelihood or alternative estimator | screen | Comparisons and comparator details are variably named; screen records for comparative evaluation. |
| Peer-reviewed social/behavioural methodological paper | screen | Discipline and peer-review status are screening judgements; no PubMed publication-type limit is justified. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:38:19+00:00
- Records added to PubMed up to: 2017-11-29
- Total records: 5,069
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Factor Analysis, Statistical"[Mesh]` | 25,757 | none |
| 2 | `"Multilevel Analysis"[Mesh]` | 1,470 | none |
| 3 | `structural equation model*[tiab]` | 12,605 | none |
| 4 | `"structural equation modeling"[tiab]` | 7,913 | none |
| 5 | `SEM[tiab]` | 81,594 | none |
| 6 | `"latent variable model*"[tiab]` | 671 | none |
| 7 | `"latent variable modeling"[tiab]` | 171 | none |
| 8 | `factor analys*[tiab]` | 38,459 | none |
| 9 | `confirmatory factor analys*[tiab]` | 10,281 | none |
| 10 | `CFA[tiab]` | 7,128 | none |
| 11 | `latent growth[tiab]` | 1,734 | none |
| 12 | `growth curve model*[tiab]` | 1,502 | none |
| 13 | `latent growth curve*[tiab]` | 973 | none |
| 14 | `growth mixture model*[tiab]` | 768 | none |
| 15 | `latent class model*[tiab]` | 603 | none |
| 16 | `latent class[tiab]` | 4,129 | none |
| 17 | `multilevel[tiab]` | 25,930 | none |
| 18 | `hierarchical model*[tiab]` | 3,344 | none |
| 19 | `mediation[tiab]` | 22,917 | none |
| 20 | `mediating variable*[tiab]` | 933 | none |
| 21 | `indirect effect*[tiab]` | 12,817 | none |
| 22 | `path analys*[tiab]` | 5,178 | none |
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 218,091 | none |
| 24 | `"Markov Chains"[Mesh]` | 13,023 | none |
| 25 | `bayes*[tiab]` | 39,780 | none |
| 26 | `MCMC[tiab]` | 1,577 | none |
| 27 | `"Markov chain Monte Carlo"[tiab]` | 3,122 | none |
| 28 | `"Monte Carlo Markov chain"[tiab]` | 133 | none |
| 29 | `Gibbs sampl*[tiab]` | 1,028 | none |
| 30 | `posterior[tiab]` | 243,365 | none |
| 31 | `prior distribution*[tiab]` | 1,143 | none |
| 32 | `#24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31` | 291,070 | none |
| 33 | `#23 AND #32` | 5,069 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Factor Analysis, Statistical"[Mesh] OR "Multilevel Analysis"[Mesh] OR structural equation model*[tiab] OR "structural equation modeling"[tiab] OR SEM[tiab] OR "latent variable model*"[tiab] OR "latent variable modeling"[tiab] OR factor analys*[tiab] OR confirmatory factor analys*[tiab] OR CFA[tiab] OR latent growth[tiab] OR growth curve model*[tiab] OR latent growth curve*[tiab] OR growth mixture model*[tiab] OR latent class model*[tiab] OR latent class[tiab] OR multilevel[tiab] OR hierarchical model*[tiab] OR mediation[tiab] OR mediating variable*[tiab] OR indirect effect*[tiab] OR path analys*[tiab]) AND ("Markov Chains"[Mesh] OR bayes*[tiab] OR MCMC[tiab] OR "Markov chain Monte Carlo"[tiab] OR "Monte Carlo Markov chain"[tiab] OR Gibbs sampl*[tiab] OR posterior[tiab] OR prior distribution*[tiab])) AND ("1800/01/01"[edat] : "2017/11/29"[edat])
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
| Monte Carlo or simulation study | left out | 5,069 / 943 | 81.4% | none | 0/30 (up to 10% of removed records could be relevant) | Leave simulation unANDed: the current base search has 3 known eligible development records, below the 15-record safety threshold for AND-ing an optional concept. The block would reduce results by 81.4%, and none of the refreshed 30 sampled losses met eligibility; the sample is weak evidence for rare relevant records, so retaining sensitivity takes priority. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Structural equation and latent-variable model family | 1 | `model*[tiab] OR factor*[tiab] OR latent*[tiab]` | 67,820 | not screened |
| Structural equation and latent-variable model family | 2 | `model*[tiab] OR factor*[tiab] OR latent*[tiab]` | 67,820 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| model_family | 291,070 | 0 |
| bayesian | 218,091 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,504,077 | initial | none | Initial recall-first draft: SEM/latent-variable family and Bayesian estimation are the required topic blocks; simulation is a tested optional design concept; comparator, small-sample context and discipline remain screening criteria. No records known yet; omitted post-2017 MeSH headings. |
| 2 | 4,900 | model_family: +4 / -3; bayesian: +1 / -2 | none | Removed Statistics as Topic from the Bayesian block after translation/evaluation showed it caused a two-and-a-half-million-record retrieval. Removed unsupported question-mark wildcard latent variable model?ing after its PubMed translation fell back to All Fields. Replaced broad MeSH with Markov Chains, whose heading covers MCMC-related records; retained Bayesian-specific title/abstract terms. |
| 3 | 5,069 | model_family: +1 / -0 | none | Addressed critic finding R1-1 by adding the named member in its bare form, latent class[tiab], beside the broader latent class model* phrase. This only adds retrieval terms; known-record recall remains to be rechecked. Existing category probe remains valid because the block only gained terms. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-1 should-fix open, R1-2 should-fix open
- Round 2 on version 3: 2 findings; R1-1 should-fix resolved, R1-2 should-fix resolved
- Round 3 on version 3: 2 findings; R1-1 should-fix resolved, R1-2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 734 NCBI requests logged (267 from cache); strategy sha256 076f08548fa9._

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
      "checked_at": "2026-09-29T03:38:19+00:00",
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
      "requested": "Multilevel Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:38:19+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Multilevel Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Markov Chains",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:38:19+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Markov Chains\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"factor analysis, statistical\"[MeSH Terms] OR \"Multilevel Analysis\"[MeSH Terms] OR \"structural equation model*\"[Title/Abstract] OR \"structural equation modeling\"[Title/Abstract] OR \"SEM\"[Title/Abstract] OR \"latent variable model*\"[Title/Abstract] OR \"latent variable modeling\"[Title/Abstract] OR \"factor analys*\"[Title/Abstract] OR \"confirmatory factor analys*\"[Title/Abstract] OR \"CFA\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"growth curve model*\"[Title/Abstract] OR \"latent growth curve*\"[Title/Abstract] OR \"growth mixture model*\"[Title/Abstract] OR \"latent class model*\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"multilevel\"[Title/Abstract] OR \"hierarchical model*\"[Title/Abstract] OR \"mediation\"[Title/Abstract] OR \"mediating variable*\"[Title/Abstract] OR \"indirect effect*\"[Title/Abstract] OR \"path analys*\"[Title/Abstract]) AND (\"Markov Chains\"[MeSH Terms] OR \"bayes*\"[Title/Abstract] OR \"MCMC\"[Title/Abstract] OR \"Markov chain Monte Carlo\"[Title/Abstract] OR \"Monte Carlo Markov chain\"[Title/Abstract] OR \"gibbs sampl*\"[Title/Abstract] OR \"posterior\"[Title/Abstract] OR \"prior distribution*\"[Title/Abstract]) AND 1800/01/01:2017/11/29[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "3652986cc86cf8ecd7865885d8b5277603b2a6ac2aff7a536c9ca1670593472d",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Eligibility names latent class as a model-family member, but the strategy only searches the narrower phrase `latent class model*`; add the member's bare name."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concept blocks are joined with AND, and their synonyms are joined with OR. The simulation block is optional and is not AND-ed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied packet verifies the Factor Analysis, Statistical; Multilevel Analysis; and Markov Chains headings. It provides no evidence of an incorrect heading mapping."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add a bare `latent class` expression so the named model-family member is not searchable only when followed by `model`."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translations show no errors or warnings, and the final query applies the stated Entrez-date cutoff."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The simulation-block rationale says there were zero known eligible records in the base search, while the current evidence reports three relevant records retrieved by it. Reconcile the rationale with the current evidence."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names latent class as a model-family member, but the search contains only `latent class model*[tiab]`. This misses records that name the member without that following word, contrary to the packet's translation check.",
          "recommendation": "Add an explicit bare-name expression such as `latent class[tiab]`, then rerun the complete evaluation for the revised strategy.",
          "status": "open"
        },
        {
          "id": "R1-2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The optional simulation-block rationale says zero known eligible records were in the base search, but the current evidence reports three relevant records in the base search, all retrieved. The stated count is inconsistent with the evidence supporting the leave-out decision.",
          "recommendation": "Reconcile the rationale with the current evidence and document the decision using the current count and optional-block results.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "c58f1afe5c61b4ae78d15556e99ca56f7ce246b5360c62012ceed4e3f110439b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search now includes the bare `latent class[tiab]` term required by the eligibility wording. The other named model-family members also have explicit search terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concept blocks are joined with AND, their synonyms with OR, and the tested simulation block remains optional."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Factor Analysis, Statistical; Multilevel Analysis; and Markov Chains headings, with no evidence of incorrect mappings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The model-family terms cover the named members, including bare `mediation` and `latent class`. The Bayesian block includes Bayesian wording and related estimation terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported translations show no errors or warnings, and the final query applies the stated Entrez-date cutoff."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-type or other search limits are applied. The simulation block is left out with a rationale consistent with the three known records, the 81.4% reduction, and the 0/30 loss sample. The Entrez-date cutoff matches the protocol's as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names latent class as a model-family member, but the search contains only `latent class model*[tiab]`. This misses records that name the member without that following word, contrary to the packet's translation check.",
          "recommendation": "Add an explicit bare-name expression such as `latent class[tiab]`, then rerun the complete evaluation for the revised strategy.",
          "status": "resolved",
          "response": "The current strategy includes `latent class[tiab]`, and the packet reports a complete current evaluation."
        },
        {
          "id": "R1-2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The optional simulation-block rationale says zero known eligible records were in the base search, but the current evidence reports three relevant records in the base search, all retrieved. The stated count is inconsistent with the evidence supporting the leave-out decision.",
          "recommendation": "Reconcile the rationale with the current evidence and document the decision using the current count and optional-block results.",
          "status": "resolved",
          "response": "The current rationale correctly states that the base search has three known eligible development records, below the 15-record threshold, and reports the optional block's 81.4% reduction and 0/30 sampled losses."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "c58f1afe5c61b4ae78d15556e99ca56f7ce246b5360c62012ceed4e3f110439b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy includes bare `latent class[tiab]` and the other named model-family terms; the earlier coverage gap is addressed."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concept blocks are joined with AND, synonyms within each block with OR, and the optional simulation block is not AND-ed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Factor Analysis, Statistical; Multilevel Analysis; and Markov Chains headings, with no evidence of incorrect mappings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the named model-family members, including bare `latent class` and `mediation`, and include Bayesian wording and related estimation terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translation has no errors or warnings, and the final query applies the stated Entrez-date cutoff."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-type or other search limits are applied. The simulation block remains optional, and its rationale now matches the three known records, the 81.4% reduction, and the 0/30 loss sample."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names latent class as a model-family member, but the search contains only `latent class model*[tiab]`. This misses records that name the member without that following word, contrary to the packet's translation check.",
          "recommendation": "Add an explicit bare-name expression such as `latent class[tiab]`, then rerun the complete evaluation for the revised strategy.",
          "status": "resolved",
          "response": "The current strategy includes `latent class[tiab]`, and the packet reports a complete current evaluation."
        },
        {
          "id": "R1-2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The optional simulation-block rationale says zero known eligible records were in the base search, but the current evidence reports three relevant records in the base search, all retrieved. The stated count is inconsistent with the evidence supporting the leave-out decision.",
          "recommendation": "Reconcile the rationale with the current evidence and document the decision using the current count and optional-block results.",
          "status": "resolved",
          "response": "The current rationale states that the base search has three known eligible development records, below the 15-record threshold, and reports the optional block's 81.4% reduction and 0/30 sampled losses."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


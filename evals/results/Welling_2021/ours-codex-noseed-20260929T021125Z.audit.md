# PubMed search strategy: audit

Generated 2026-09-29T02:33:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: yes (User requested proceed without questions. Assumed studies qualify if reporting either lifestyle behavior(s) or well-being; no population, design, language, or publication-date restrictions were requested. Standard workload budget defaults to 10,000. No known relevant articles supplied. Cutoff is PubMed Entrez date via as_of/PSB_AS_OF, not a publication-date limit. Standard-depth discovery screened COVID-19 systematic-review candidates and focused PubMed pilot hits; seven clearly relevant records were added to the development relevant set. No held-out validation set exists. The broad exposure-only strategy exceeds the 10,000 screening budget; a tested lifestyle/well-being candidate cuts the count but remains out of the search because only seven known relevant records support the decision.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The pandemic/lockdown is the exposure defining every in-scope record and is consistently nameable in this period. |
| Lifestyle behaviors and well-being outcomes | optional | Topic-defining outcomes may reduce screening burden, but studies can report specific behaviors without naming lifestyle; test as an OR outcome block before deciding. |
| Population | screen | No population restriction is stated; age groups and settings will be assessed at screening. |
| Impact/effect of exposure | screen | Impact language is inconsistently indexed and comparative designs are not required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:32:46+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 103,873
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"COVID-19"[Mesh]` | 57,089 | none |
| 2 | `"SARS-CoV-2"[Mesh]` | 45,931 | none |
| 3 | `COVID-19[tiab]` | 67,388 | none |
| 4 | `COVID19[tiab]` | 64,206 | none |
| 5 | `"COVID 19"[tiab]` | 67,388 | none |
| 6 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 7 | `SARS-CoV2[tiab]` | 1,049 | none |
| 8 | `2019-nCoV[tiab]` | 1,288 | none |
| 9 | `2019nCoV[tiab]` | 926 | none |
| 10 | `"2019 novel coronavirus"[tiab]` | 1,176 | none |
| 11 | `"novel coronavirus"[tiab]` | 6,179 | none |
| 12 | `"coronavirus disease 2019"[tiab]` | 14,613 | none |
| 13 | `"COVID-19 pandemic"[tiab]` | 20,381 | none |
| 14 | `"COVID-19 outbreak"[tiab]` | 3,314 | none |
| 15 | `"coronavirus pandemic"[tiab]` | 1,011 | none |
| 16 | `lockdown*[tiab]` | 3,416 | none |
| 17 | `quarantin*[tiab]` | 6,954 | none |
| 18 | `"stay at home"[tiab]` | 815 | none |
| 19 | `"stay-at-home"[tiab]` | 815 | none |
| 20 | `confinement[tiab]` | 20,190 | none |
| 21 | `"social distancing"[tiab]` | 2,657 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 103,873 | none |

### Strategy (single line, for copying into PubMed)

```text
(("COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR "COVID 19"[tiab] OR SARS-CoV-2[tiab] OR SARS-CoV2[tiab] OR 2019-nCoV[tiab] OR 2019nCoV[tiab] OR "2019 novel coronavirus"[tiab] OR "novel coronavirus"[tiab] OR "coronavirus disease 2019"[tiab] OR "COVID-19 pandemic"[tiab] OR "COVID-19 outbreak"[tiab] OR "coronavirus pandemic"[tiab] OR lockdown*[tiab] OR quarantin*[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR confinement[tiab] OR "social distancing"[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being outcomes | left out | 103,873 / 12,802 | 87.7% | none | 0/30 (up to 10% of removed records could be relevant) | The candidate outcome block reduces the current strategy from 103,873 to 12,802 records (87.7%), and loses none of the seven known relevant development records. The current 30-record loss sample contained no clearly eligible record; two separate 30-record category probes also found no clearly eligible member-only record. Still leave the outcome block out because seven known records are below the required 15-record minimum for justifying AND-ing, and the exposure-only query preserves recall at the cost of an over-budget screening load. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Lifestyle behaviors and well-being outcomes | 1 | `behavior*[tiab] OR behaviour*[tiab] OR activity[tiab] OR activities[tiab] OR eating[tiab] OR mood[tiab] OR wellness[tiab] OR well-being[tiab] OR wellbeing[tiab] OR health[tiab]` | 24,414 | 0/30 |
| Lifestyle behaviors and well-being outcomes | 2 | `behavior*[tiab] OR behaviour*[tiab] OR activity[tiab] OR activities[tiab] OR eating[tiab] OR mood[tiab] OR wellness[tiab] OR well-being[tiab] OR wellbeing[tiab] OR health[tiab]` | 22,422 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 135,768 | initial | none | Initial broad COVID-19 pandemic/lockdown exposure block with a candidate OR block for lifestyle and well-being outcomes; terms include historical coronavirus forms, indexed headings, and lockdown terminology. |
| 2 | 141,128 | covid_exposure: +2 / -0 | none | Added SARS-CoV-2 and Pandemics MeSH headings found on the screened relevant records; retained the broad outcome block as optional and out of the query to avoid risking recall with only seven known relevant records. |
| 3 | 103,873 | covid_exposure: +0 / -4 | none | Removed broad Coronavirus Infections, Pandemics, Quarantine, and Social Isolation MeSH headings from the exposure OR block: these headings also retrieve non-COVID infections/pandemics and general quarantine/social isolation literature. Retained COVID-19 and SARS-CoV-2 MeSH plus disease-specific text variants and lockdown terms. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1 must-fix rejected
- Round 2 on version 3: 1 findings; F1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 654 NCBI requests logged (239 from cache); strategy sha256 c12c48ace365._

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
        "message": "103,873 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "103,873 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:32:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000086382",
          "name": "COVID-19",
          "type": "descriptor",
          "scope_note": "A viral disorder generally characterized by high FEVER; COUGH; DYSPNEA; CHILLS; PERSISTENT TREMOR; MUSCLE PAIN; HEADACHE; SORE THROAT; a new loss of taste and/or smell (see AGEUSIA and ANOSMIA) and other symptoms of a VIRAL PNEUMONIA. A coronavirus, SARS-CoV-2 VIRUS, in the genus BETACORONAVIRUS is the causative agent.",
          "tree_numbers": [
            "C01.748.610.763.500",
            "C01.925.705.500",
            "C01.925.782.600.550.200.163",
            "C08.381.677.807.500",
            "C08.730.610.763.500"
          ],
          "entry_terms": 36,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000086382",
      "preferred_label": "COVID-19",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"COVID-19\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "SARS-CoV-2",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:32:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000086402",
          "name": "SARS-CoV-2",
          "type": "descriptor",
          "scope_note": "A species of BETACORONAVIRUS causing atypical respiratory disease (COVID-19) in humans. The organism was first identified in 2019 in Wuhan, China. The natural host is the Chinese intermediate horseshoe bat, RHINOLOPHUS affinis.",
          "tree_numbers": [
            "B04.820.578.500.540.150.113.937.500"
          ],
          "entry_terms": 24,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000086402",
      "preferred_label": "SARS-CoV-2",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"SARS-CoV-2\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"covid 19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"covid 19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"covid 19\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019nCoV\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"COVID-19 pandemic\"[Title/Abstract] OR \"COVID-19 outbreak\"[Title/Abstract] OR \"coronavirus pandemic\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"confinement\"[Title/Abstract] OR \"social distancing\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "e3edaeb5bb1ba54752252e210655e71c20f503427d2bee9df5b99d6f884b07ea",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block includes COVID-19 name variants and lockdown-related terms as separate expressions; no process-direction or parent-narrowed-term issue is evident."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are OR-combined, with no population or outcome block that would unnecessarily narrow retrieval."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The COVID-19 and SARS-CoV-2 MeSH headings are verified in the packet, and the free-text terms supplement them."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The free-text list covers common COVID-19 naming variants and lockdown, quarantine, stay-at-home, confinement, and distancing terminology."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The recorded query and term translations show no syntax errors or PubMed warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The reviewer finding is rejected because the required Entrez-date cutoff is explicitly imposed by the user?s harness instructions."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entry Date range ending 2020-11-22. No such cutoff appears in the scope or eligibility criteria, so this excludes later records relevant to the stated question.",
          "recommendation": "Remove the Entry Date limit for a current search, or explicitly define and justify a cutoff in the protocol before retaining it; then rerun the complete evaluation for the revised query.",
          "status": "rejected",
          "response": "The user?s harness instructions explicitly require treating PubMed as of 2020-11-22, pinning the snapshot through PSB_AS_OF for every command, and not adding a publication-date limit. The workspace uses the corresponding protocol as_of Entrez-date bound, as required. Removing it would violate the task. This is an evaluation snapshot restriction, not a publication-date eligibility criterion."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The outcome block was considered as an optional block, but only seven known relevant development records are available, below the stated minimum of 15 for justifying an AND restriction. The tested outcome block also leaves 12,802 records, still above the 10,000-record workload budget. The exposure-only strategy therefore retains the broader recall-oriented search while documenting the workload warning.",
          "evidence": "The packet reports 103,873 records without the outcome block and 12,802 with it; no known records were lost, but the development set contains only seven records. The loss sample and two category probes each screened 30 records with zero clearly eligible records."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "e3edaeb5bb1ba54752252e210655e71c20f503427d2bee9df5b99d6f884b07ea",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched exposure concept is represented by separate COVID-19/SARS-CoV-2 names and lockdown-related terms. No member of a searched concept is represented only by a phrase narrowed with a parent term, and no one-direction process term is present."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure expressions are OR-combined. Population and outcome remain screening concepts; the outcome block was tested as an optional AND block and left out with a documented rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The COVID-19 and SARS-CoV-2 MeSH headings are verified in the packet and are supplemented by free-text variants and lockdown terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The free-text terms cover common COVID-19 naming variants and pandemic, outbreak, lockdown, quarantine, stay-at-home, confinement, and social-distancing language."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The recorded final query and translation show no PubMed syntax errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date cutoff is retained as the explicitly required 2020-11-22 evaluation snapshot bound, not as an eligibility filter. The over-workload warning is explicitly reviewed and its accepted risk is supported by the optional-block evaluation."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entry Date range ending 2020-11-22. No such cutoff appears in the scope or eligibility criteria, so this excludes later records relevant to the stated question.",
          "recommendation": "Remove the Entry Date limit for a current search, or explicitly define and justify a cutoff in the protocol before retaining it; then rerun the complete evaluation for the revised query.",
          "status": "rejected",
          "response": "The packet earlier-round record states that the harness explicitly requires the PubMed snapshot as of 2020-11-22 and the corresponding Entrez-date bound, with no publication-date limit. The cutoff is therefore an evaluation snapshot restriction, not an eligibility criterion."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The optional lifestyle and well-being outcome block was considered and tested, but the seven known relevant development records are below the stated minimum of 15 for justifying an AND restriction. The exposure-only strategy is retained despite the workload warning.",
          "evidence": "The exposure-only strategy retrieves 103,873 records, exceeding the 10,000-record budget. The tested outcome block reduces retrieval to 12,802 records (87.7%) and loses none of the seven known records, but remains above budget. The 30-record loss sample and both 30-record category probes found zero clearly eligible records; these samples do not meet the minimum known-record count for justifying the restriction."
        }
      ]
    }
  ]
}
```


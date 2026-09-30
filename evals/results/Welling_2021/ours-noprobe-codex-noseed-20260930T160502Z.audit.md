# PubMed search strategy: audit

Generated 2026-09-30T16:48:53+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User asked not to be questioned during this run. Assumed all human populations and any empirical design; outcomes include physical activity/sedentary behavior, diet/eating, sleep, alcohol/tobacco/other substance use, and psychological/social well-being. COVID-19 or related restrictions are the exposure. Outcome block will be tested as optional. Cutoff is Entrez date 2020-11-22 via PSB_AS_OF; no publication-date filter. No known relevant records supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The pandemic or associated restrictions are the defining exposure and are searchable by disease, virus, pandemic and quarantine terminology. |
| Lifestyle behaviors and well-being | optional | These are topic-defining outcomes, but studies may describe behavior or well-being without using a common outcome label; test a broad outcome block before deciding whether to require it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T16:48:14+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 123,001
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Coronavirus Infections"[Mesh]` | 67,535 | none |
| 2 | `"Quarantine"[Mesh]` | 3,936 | none |
| 3 | `"Pandemics"[Mesh]` | 50,277 | none |
| 4 | `COVID-19[tiab]` | 67,388 | none |
| 5 | `COVID19[tiab]` | 64,206 | none |
| 6 | `COVID-19 pandemic[tiab]` | 20,381 | none |
| 7 | `COVID pandemic*[tiab]` | 183 | none |
| 8 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 9 | `coronavirus pandemic*[tiab]` | 1,029 | none |
| 10 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 11 | `SARS-CoV2[tiab]` | 1,049 | none |
| 12 | `2019-nCoV[tiab]` | 1,288 | none |
| 13 | `novel coronavirus[tiab]` | 6,179 | none |
| 14 | `severe acute respiratory syndrome coronavirus 2[tiab]` | 7,988 | none |
| 15 | `lockdown[tiab]` | 3,157 | none |
| 16 | `lockdowns[tiab]` | 441 | none |
| 17 | `stay-at-home[tiab]` | 815 | none |
| 18 | `stay at home[tiab]` | 815 | none |
| 19 | `shelter-in-place[tiab]` | 210 | none |
| 20 | `quarantine[tiab]` | 6,169 | none |
| 21 | `social distanc*[tiab]` | 3,813 | none |
| 22 | `physical distanc*[tiab]` | 1,606 | none |
| 23 | `movement restriction*[tiab]` | 568 | none |
| 24 | `"COVID-19"[Mesh]` | 57,089 | none |
| 25 | `"SARS-CoV-2"[Mesh]` | 45,931 | none |
| 26 | `pandemic*[tiab]` | 58,444 | none |
| 27 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 123,001 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Coronavirus Infections"[Mesh] OR "Quarantine"[Mesh] OR "Pandemics"[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR COVID-19 pandemic[tiab] OR COVID pandemic*[tiab] OR coronavirus disease 2019[tiab] OR coronavirus pandemic*[tiab] OR SARS-CoV-2[tiab] OR SARS-CoV2[tiab] OR 2019-nCoV[tiab] OR novel coronavirus[tiab] OR severe acute respiratory syndrome coronavirus 2[tiab] OR lockdown[tiab] OR lockdowns[tiab] OR stay-at-home[tiab] OR stay at home[tiab] OR shelter-in-place[tiab] OR quarantine[tiab] OR social distanc*[tiab] OR physical distanc*[tiab] OR movement restriction*[tiab] OR "COVID-19"[Mesh] OR "SARS-CoV-2"[Mesh] OR pandemic*[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 14 | 14 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Lifestyle behaviors and well-being | left out | 123,001 / 14,441 | 88.3% | none | 0/30 (up to 10% of removed records could be relevant) | The updated strategy's 30-record random loss sample contained no eligible studies; only 14 screened relevant records sit in the base strategy, below the 15-record evidence threshold required to justify AND-ing the optional outcome. Leave it out to protect recall; screen outcomes during selection. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad COVID-19 exposure block and optional lifestyle/well-being outcome block; no known relevant records were supplied. |
| 2 | 102,535 | covid: +2 / -0 | none | Added directly observed COVID-19 and SARS-CoV-2 MeSH headings and psychosocial/fear/change vocabulary found in screened relevant records. |
| 3 | 123,001 | covid: +1 / -0 | none | Added pandemic*[tiab] per critic finding P1-TXT-01 to cover the bare-named pandemic concept, while retaining COVID-specific terms and lockdown vocabulary. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; P1-TXT-01 should-fix open
- Round 2 on version 3: 1 findings; P1-TXT-01 should-fix resolved
- Round 3 on version 3: 1 findings; P1-TXT-01 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 509 NCBI requests logged (166 from cache); strategy sha256 cc7f776f341b._

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
        "message": "123,001 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:outcomes",
        "blocking": false,
        "requires_review": true,
        "id": "I-45faba5f9a1cdbee1581"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "123,001 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:outcomes",
        "blocking": false,
        "requires_review": true,
        "id": "I-45faba5f9a1cdbee1581"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:48:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D018352",
          "name": "Coronavirus Infections",
          "type": "descriptor",
          "scope_note": "Virus diseases caused by the CORONAVIRUS genus. Some specifics include transmissible enteritis of turkeys (ENTERITIS, TRANSMISSIBLE, OF TURKEYS); FELINE INFECTIOUS PERITONITIS; and transmissible gastroenteritis of swine (GASTROENTERITIS, TRANSMISSIBLE, OF SWINE).",
          "tree_numbers": [
            "C01.925.782.600.550.200"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D018352",
      "preferred_label": "Coronavirus Infections",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Coronavirus Infections\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:48:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011790",
          "name": "Quarantine",
          "type": "descriptor",
          "scope_note": "Limited freedom of movement of individuals to reduce the risk of spread of communicable disease by those who have been exposed to infectious or communicable disease in order to prevent its spread; a period of detention of vessels, vehicles, or travelers coming from infected or suspected places; and detention or isolation on account of suspected contagion. It includes government regulations on t...",
          "tree_numbers": [
            "N06.850.780.200.725"
          ],
          "entry_terms": 28,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011790",
      "preferred_label": "Quarantine",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Quarantine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:48:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D058873",
          "name": "Pandemics",
          "type": "descriptor",
          "scope_note": "Epidemics of infectious disease that have spread to many countries, often more than one continent, and usually affecting a large number of people.",
          "tree_numbers": [
            "N06.850.290.200.600"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D058873",
      "preferred_label": "Pandemics",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Pandemics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:48:14+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"COVID-19\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "SARS-CoV-2",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:48:14+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"SARS-CoV-2\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Coronavirus Infections\"[MeSH Terms] OR \"Quarantine\"[MeSH Terms] OR \"Pandemics\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"covid 19 pandemic\"[Title/Abstract] OR \"covid pandemic*\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"coronavirus pandemic*\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"severe acute respiratory syndrome coronavirus 2\"[Title/Abstract] OR \"lockdown\"[Title/Abstract] OR \"lockdowns\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"Quarantine\"[Title/Abstract] OR \"social distanc*\"[Title/Abstract] OR \"physical distanc*\"[Title/Abstract] OR \"movement restriction*\"[Title/Abstract] OR \"COVID-19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"pandemic*\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "4c1d55fd83ba432be1df469d14e0af4af2eaade0ef0a820fefc88b6b55c790e1",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The exposure block covers COVID-19, lockdown, quarantine, and distancing terms, but the protocol also names the pandemic itself. The only free-text pandemic terms are narrowed by COVID/coronavirus wording; add the bare pandemic name."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure synonyms are OR-combined, with no restrictive AND or proximity construction."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The block includes relevant headings for coronavirus infections, COVID-19, SARS-CoV-2, pandemics, and quarantine."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add a bare pandemic free-text term, such as pandemic*[tiab], to cover the named pandemic concept independently of COVID/coronavirus phrases."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed query is balanced and the reported translations show no syntax errors or warnings. No proximity operators or wildcard proximity constructions are used."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The stated 2020-11-22 cutoff is applied as an Entrez date filter, consistent with the packet's notes; no other limits are applied."
        }
      },
      "findings": [
        {
          "id": "P1-TXT-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched exposure concept includes the COVID-19 pandemic, but free-text pandemic terms appear only in phrases restricted by COVID or coronavirus wording. This misses the packet's required bare-name coverage for pandemic.",
          "recommendation": "Add and evaluate a bare term such as pandemic*[tiab], then rerun the complete evaluation because the strategy will change.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The outcome concept was tested as an optional block; requiring it would reduce results by 88%, while only 14 known relevant records were available, below the stated threshold for requiring the block. The large set is documented for screening.",
          "evidence": "The optional-block evaluation reports 102,535 records without the outcome block and 12,304 with it, with no known records lost; the loss sample was 0/30 relevant."
        },
        {
          "issue_id": "I-45faba5f9a1cdbee1581",
          "status": "accepted-risk",
          "response": "The evidence records candidate screening from COVID-19 child/adolescent mental-health reviews, yielding 14 relevant records. That documents an attempt to identify known records from prior reviews, though the set remains below the 15-record threshold.",
          "evidence": "The relevant-set source is listed as screened reference candidates from COVID-19 child/adolescent mental-health reviews; all 14 records were retrieved."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "0e7b8b86ce4f3f84675dd37825f38059e1219afab16ff211846474dcb1283500",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block now includes pandemic*[tiab], covering pandemic by its bare name as required, alongside COVID-19 and related restriction terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure synonyms are OR-combined, with no restrictive AND or proximity construction."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The block includes relevant headings for coronavirus infections, COVID-19, SARS-CoV-2, pandemics, and quarantine."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover COVID-19 variants, pandemic, lockdown, stay-at-home, shelter-in-place, quarantine, distancing, and movement restrictions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query is balanced, and the reported translations show no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The stated 2020-11-22 cutoff is applied as an Entrez date filter; no other limits are applied."
        }
      },
      "findings": [
        {
          "id": "P1-TXT-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched exposure concept included the COVID-19 pandemic, but free-text pandemic terms appeared only in phrases restricted by COVID or coronavirus wording.",
          "recommendation": "Add and evaluate a bare term such as pandemic*[tiab], then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The strategy now includes pandemic*[tiab]. The complete evaluation was rerun at version 3, and the term is present in the final query."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The large result set is documented for screening. The optional outcome block was tested, but requiring it would substantially restrict retrieval and still leave the result count above the workload budget.",
          "evidence": "The current strategy returns 123,001 records. The outcome block reduces this to 14,441 records, an 88.3% reduction; no known relevant records were lost, and the 30-record random loss sample contained 0 relevant records. The strategy leaves the block optional."
        },
        {
          "issue_id": "I-45faba5f9a1cdbee1581",
          "status": "accepted-risk",
          "response": "The available prior-review candidates were screened for additional known relevant records. The set remains below the threshold for justifying an outcome block, so outcomes will be screened during selection.",
          "evidence": "The relevant-set source is screened reference candidates from COVID-19 child/adolescent mental-health reviews; 14 relevant records were identified and all 14 were retrieved. The outcome-block loss sample had 0 relevant records among 30 screened."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "0e7b8b86ce4f3f84675dd37825f38059e1219afab16ff211846474dcb1283500",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block now includes pandemic*[tiab] as a bare term, covering the named pandemic concept alongside COVID-19 and related restrictions."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure synonyms are OR-combined, and the optional outcome block is left out after testing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The block includes relevant headings for coronavirus infections, COVID-19, SARS-CoV-2, pandemics, and quarantine."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover COVID-19 variants, pandemic, lockdown, stay-at-home, shelter-in-place, quarantine, distancing, and movement restrictions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query is balanced, with no lint issues, syntax errors, or warnings reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2020-11-22 cutoff is applied as an Entrez date filter; no other limits are applied."
        }
      },
      "findings": [
        {
          "id": "P1-TXT-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched exposure concept included the COVID-19 pandemic, but free-text pandemic terms previously appeared only in phrases restricted by COVID or coronavirus wording.",
          "recommendation": "Add and evaluate a bare term such as pandemic*[tiab], then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The strategy includes pandemic*[tiab]. The complete evaluation was rerun at version 3, and the term is present in the final query."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The outcome block remains optional to protect recall; outcomes will be screened during selection.",
          "evidence": "The strategy returns 123,001 records. The outcome block reduces this to 14,441 records, an 88.3% reduction; no known relevant records were lost, and the 30-record random loss sample contained 0 relevant records. The 14 known relevant records remain below the stated threshold for requiring the block."
        },
        {
          "issue_id": "I-45faba5f9a1cdbee1581",
          "status": "accepted-risk",
          "response": "Available prior-review candidates were screened for additional known relevant records. The set remains below the threshold for justifying an outcome block, so outcomes will be screened during selection.",
          "evidence": "The relevant-record source is screened reference candidates from COVID-19 child/adolescent mental-health reviews. Fourteen relevant records were identified and all 14 were retrieved; the outcome-block loss sample had 0 relevant records among 30 screened."
        }
      ]
    }
  ]
}
```


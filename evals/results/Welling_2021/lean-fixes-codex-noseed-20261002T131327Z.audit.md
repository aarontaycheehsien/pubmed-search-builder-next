# PubMed search strategy: audit

Generated 2026-10-02T13:32:49+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User instructed not to ask questions during this run. Scope and eligibility are provisional interpretations of the broad question. No known relevant records were supplied. PSB_AS_OF pins NCBI queries to Entrez date 2020-11-22; no publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related restrictions | search | The pandemic is the defining exposure and is reliably named or indexed. Lockdown and restriction language is included in this block as synonyms/context, not required as an additional AND block. |
| Lifestyle behaviors | screen | A broad, multidomain outcome that may be inconsistently named and indexed; assess at screening. |
| Well-being | screen | A broad outcome including psychological and subjective well-being; outcome language is inconsistently reported and should not be required for retrieval. |
| Human populations | screen | No age or population subgroup is specified; assess population eligibility at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:32:20+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 128,242
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `SARS-CoV-2[Mesh]` | 45,930 | none |
| 3 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 4 | `Quarantine[Mesh]` | 3,936 | none |
| 5 | `Pandemics[Mesh]` | 50,277 | none |
| 6 | `COVID*[tiab]` | 68,959 | none |
| 7 | `coronavir*[tiab]` | 43,266 | none |
| 8 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 9 | `2019-nCoV[tiab]` | 1,288 | none |
| 10 | `Wuhan coronavirus[tiab]` | 29 | none |
| 11 | `novel coronavirus[tiab]` | 6,179 | none |
| 12 | `coronavirus disease 2019[tiab]` | 14,613 | none |
| 13 | `lockdown*[tiab]` | 3,416 | none |
| 14 | `quarantin*[tiab]` | 6,954 | none |
| 15 | `social distancing[tiab]` | 2,657 | none |
| 16 | `stay at home[tiab]` | 815 | none |
| 17 | `stay-at-home[tiab]` | 815 | none |
| 18 | `home confinement[tiab]` | 121 | none |
| 19 | `self-isolat*[tiab]` | 400 | none |
| 20 | `pandemic*[tiab]` | 58,444 | none |
| 21 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 128,242 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR SARS-CoV-2[Mesh] OR Coronavirus Infections[Mesh] OR Quarantine[Mesh] OR Pandemics[Mesh] OR COVID*[tiab] OR coronavir*[tiab] OR SARS-CoV-2[tiab] OR 2019-nCoV[tiab] OR Wuhan coronavirus[tiab] OR novel coronavirus[tiab] OR coronavirus disease 2019[tiab] OR lockdown*[tiab] OR quarantin*[tiab] OR social distancing[tiab] OR stay at home[tiab] OR stay-at-home[tiab] OR home confinement[tiab] OR self-isolat*[tiab] OR pandemic*[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,478,792 | initial | none | First recall-first draft; one COVID/pandemic/restriction block only, with lifestyle and well-being handled at screening to avoid requiring variable outcome language. |
| 2 | 102,685 | covid_exposure: +1 / -3 | none | Removed Pandemics[Mesh] and unqualified isolation/confinement terms after line counts showed they broadened retrieval beyond the COVID topic; retained specific lockdown, quarantine, social-distancing, stay-at-home, home-confinement, and self-isolation language. |
| 3 | 128,242 | covid_exposure: +2 / -0 | none | Added Pandemics[Mesh] and pandemic*[tiab] after the independent critic identified incomplete coverage of the pandemic exposure concept. Retained broad terms to protect sensitivity; screen non-COVID pandemic records out. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-01 must-fix open, R1-02 should-fix open
- Round 2 on version 3: 3 findings; R1-01 must-fix resolved, R1-02 should-fix resolved, R2-01 document accepted-risk
- Round 3 on version 3: 3 findings; R1-01 must-fix resolved, R1-02 should-fix resolved, R2-01 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 326 NCBI requests logged (105 from cache); strategy sha256 407ad8a55e72._

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
      "requested": "COVID-19",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:32:20+00:00",
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
        "text": "COVID-19",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "SARS-CoV-2",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:32:20+00:00",
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
        "text": "SARS-CoV-2",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:32:20+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "Coronavirus Infections",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:32:20+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "Quarantine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:32:20+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "Pandemics",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"covid 19\"[MeSH Terms] OR \"SARS-CoV-2\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"pandemics\"[MeSH Terms] OR \"covid*\"[Title/Abstract] OR \"coronavir*\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"wuhan coronavirus\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"home confinement\"[Title/Abstract] OR \"self isolat*\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "d718d5c37e03c5a18d251b15781d8c2fffb4c0ddb4ceecf2005cf2da6d97a390",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searched exposure concept names the pandemic, but the strategy has no standalone pandemic term. COVID terms may miss records that describe the pandemic without naming COVID-19."
        },
        "operators": {
          "verdict": "pass",
          "note": "The searched concept is combined with OR, and the strategy does not require lockdown or restriction language as a separate AND block."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The verified headings are valid, but Pandemics[Mesh] is absent despite pandemic being named in the searched concept."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add a standalone pandemic text-word expression. The current COVID and restriction terms do not explicitly cover records that use pandemic wording alone."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The explicit OR expression, field tags, truncation, and tested translations show no syntax errors or unresolved warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No protocol limits are applied. The entry-date ceiling matches the stated as-of date and is not a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The searched concept includes the COVID-19 pandemic, but no standalone term covers pandemic wording when COVID-19 is not named. The strategy therefore does not fully translate the named exposure concept.",
          "recommendation": "Add pandemic*[tiab] to cover pandemic, pandemics, and pandemic-related wording. Keep restriction terms as OR synonyms within the same exposure block.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Pandemics[Mesh] is missing from the exposure block, although the concept explicitly includes the pandemic.",
          "recommendation": "Add Pandemics[Mesh] and test its translation and contribution to the block.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "0562bebc9c70dbf660464ac28f7f81e4bef4a4c2985bdfef7c43b7aa0a0569de",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block now covers COVID-19, pandemic wording, and related restriction terms. pandemic*[tiab] and Pandemics[Mesh] address the gap identified in round 1."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms are combined with OR. Lockdown and restriction terms remain contextual synonyms in the same block, not required AND concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are verified in the packet, including the added Pandemics[Mesh]."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word block includes pandemic*[tiab] and COVID, coronavirus, lockdown, quarantine, distancing, stay-at-home, confinement, and self-isolation wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The tested query has no reported syntax errors, warnings, or unresolved translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No protocol limits are applied. The entry-date ceiling matches the stated as-of date and is not a publication-date limit. All three known records are development records, so their 100% retrieval does not establish independent validation."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The searched concept included the COVID-19 pandemic, but the prior strategy had no standalone term for pandemic wording when COVID-19 was not named.",
          "recommendation": "Add pandemic*[tiab] while retaining restriction terms as OR synonyms within the exposure block.",
          "status": "resolved",
          "response": "Added pandemic*[tiab] to the exposure block; evaluation retained all three known development records."
        },
        {
          "id": "R1-02",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Pandemics[Mesh] was missing although the searched concept explicitly included the pandemic.",
          "recommendation": "Add Pandemics[Mesh] and test its translation and contribution to the block.",
          "status": "resolved",
          "response": "Added and tested Pandemics[Mesh]; PubMed translated it as a MeSH term without translation issues, and no known records were lost."
        },
        {
          "id": "R2-01",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "All three known relevant records were used for development, not independent validation. Their 100% retrieval should not be presented as an independent sensitivity estimate.",
          "recommendation": "Label the result as development-set retrieval and report that independent validation was not performed.",
          "status": "accepted-risk",
          "response": "The audit and narrative label this as development relative recall and state that no independent validation set was available; no sensitivity claim is made."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "0562bebc9c70dbf660464ac28f7f81e4bef4a4c2985bdfef7c43b7aa0a0569de",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block covers COVID-19, pandemic wording, and related restrictions. The previously identified standalone pandemic wording gap is addressed."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms are combined with OR; restriction terms are not required as a separate AND block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings, including Pandemics[Mesh], are verified in the packet."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover COVID and coronavirus wording, pandemic wording, and related restriction terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The tested query reports no syntax errors, warnings, or unresolved translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No protocol limits are applied. The entry-date ceiling matches the stated as-of date and is not a publication-date limit. The packet identifies all three known records as development records, not independent validation."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The earlier strategy lacked standalone coverage for pandemic wording when COVID-19 was not named.",
          "recommendation": "Add pandemic*[tiab] while retaining restriction terms as OR synonyms within the exposure block.",
          "status": "resolved",
          "response": "The current block includes pandemic*[tiab] and Pandemics[Mesh]; evaluation retained all three known development records."
        },
        {
          "id": "R1-02",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier strategy omitted Pandemics[Mesh] although the searched concept included the pandemic.",
          "recommendation": "Add Pandemics[Mesh] and test its translation and contribution to the block.",
          "status": "resolved",
          "response": "Pandemics[Mesh] is included and verified; the packet reports no translation issues and no known records lost."
        },
        {
          "id": "R2-01",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "All three known relevant records were used for development, so their 100% retrieval is not an independent sensitivity estimate.",
          "recommendation": "Label the result as development-set retrieval and state that independent validation was not performed.",
          "status": "accepted-risk",
          "response": "The packet identifies the records as development records, reports development relative recall, and states that the result does not establish independent validation."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


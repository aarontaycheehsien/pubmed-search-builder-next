# PubMed search strategy: audit

Generated 2026-10-02T13:50:17+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without clarification; scope and eligibility are working assumptions. PSB_AS_OF was set to 2020-11-22 for every command, enforcing an Entrez-date bound; no publication-date limit was used. No language, population, or study-design limit. Outcomes are screened because they are broad and inconsistently indexed. A candidate systematic review on schoolchildren was too narrow to serve as a benchmark; six screened pilot records were added as a non-independent development set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown or quarantine measures | search | The pandemic and its restrictions are the defining exposure; COVID-19, pandemic, and lockdown/quarantine terms are searched broadly in one block to retain studies using different labels. |
| Lifestyle behaviors | screen | Behaviors such as physical activity, diet, sleep, sedentary behavior, and substance use are inconsistently named and indexed; requiring this fragile outcome block risks missing relevant studies. |
| Well-being | screen | Psychological, social, and general well-being outcomes vary in terminology and may be secondary findings; screen rather than AND as a required block. |
| Any population | screen | No population subgroup is specified in the question. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:49:46+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 126,898
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 3 | `Pandemics[Mesh]` | 50,277 | none |
| 4 | `Quarantine[Mesh]` | 3,936 | none |
| 5 | `COVID-19[tiab]` | 67,388 | none |
| 6 | `COVID19[tiab]` | 64,206 | none |
| 7 | `2019-nCoV[tiab]` | 1,288 | none |
| 8 | `"2019 nCoV"[tiab]` | 1,288 | none |
| 9 | `"novel coronavirus"[tiab:~1]` | 6,418 | none |
| 10 | `"2019 novel coronavirus"[tiab:~1]` | 2,326 | none |
| 11 | `"coronavirus disease 2019"[tiab:~2]` | 15,475 | none |
| 12 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 13 | `coronavirus[tiab]` | 41,791 | none |
| 14 | `pandemic*[tiab]` | 58,444 | none |
| 15 | `lockdown*[tiab]` | 3,416 | none |
| 16 | `lock-down[tiab]` | 163 | none |
| 17 | `quarantin*[tiab]` | 6,954 | none |
| 18 | `"stay at home"[tiab:~1]` | 869 | none |
| 19 | `"stay-at-home"[tiab]` | 815 | none |
| 20 | `"social distancing"[tiab:~1]` | 2,679 | none |
| 21 | `"physical distancing"[tiab:~1]` | 446 | none |
| 22 | `"containment measure*"[tiab]` | 636 | none |
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 126,898 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR Coronavirus Infections[Mesh] OR Pandemics[Mesh] OR Quarantine[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR 2019-nCoV[tiab] OR "2019 nCoV"[tiab] OR "novel coronavirus"[tiab:~1] OR "2019 novel coronavirus"[tiab:~1] OR "coronavirus disease 2019"[tiab:~2] OR SARS-CoV-2[tiab] OR coronavirus[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR lock-down[tiab] OR quarantin*[tiab] OR "stay at home"[tiab:~1] OR "stay-at-home"[tiab] OR "social distancing"[tiab:~1] OR "physical distancing"[tiab:~1] OR "containment measure*"[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad exposure block; searched COVID-19/pandemic and lockdown/quarantine vocabulary, with outcomes screened. Added six screened pilot records for development recall. |
| 2 | 126,898 | exposure: +4 / -0 | none | Revision 1: added 2019-nCoV and alternate novel coronavirus/COVID disease-name text variants requested by critic F1; preserve the single broad exposure block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1 (Same-context critic: no fresh-context reviewer was available under the run constraints.): 1 findings; F1 should-fix open
- Round 2 on version 2 (Same-context critic: no fresh-context reviewer was available under the run constraints.): 2 findings; F1 should-fix resolved, F2 document accepted-risk
- Round 3 on version 2 (Same-context closing critic: no fresh-context reviewer was available under the run constraints.): 2 findings; F1 should-fix resolved, F2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 269 NCBI requests logged (47 from cache); strategy sha256 4eb3ab5cd9a9._

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
      "checked_at": "2026-10-02T13:49:46+00:00",
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
      "requested": "Coronavirus Infections",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:49:46+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Coronavirus Infections",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:49:46+00:00",
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
        "text": "Pandemics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:49:46+00:00",
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
    }
  ],
  "translation": "(\"COVID-19\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"pandemics\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"COVID-19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"2019 ncov\"[Title/Abstract] OR \"2019 ncov\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract:~1] OR \"2019 novel coronavirus\"[Title/Abstract:~1] OR \"coronavirus disease 2019\"[Title/Abstract:~2] OR \"SARS-CoV-2\"[Title/Abstract] OR \"coronavirus\"[Title/Abstract] OR \"pandemic*\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock-down\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract:~1] OR \"stay-at-home\"[Title/Abstract] OR \"social distancing\"[Title/Abstract:~1] OR \"physical distancing\"[Title/Abstract:~1] OR \"containment measure*\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "294e21180e134897a37fd56b8dda866eeebe00abc92dc59482603623b0978e88",
      "note": "Same-context critic: no fresh-context reviewer was available under the run constraints.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The COVID pandemic/restriction exposure is the only searched concept; variable outcomes and unspecified population are screened to preserve recall."
        },
        "operators": {
          "verdict": "pass",
          "note": "One OR block is appropriate for alternative exposure labels, with no NOT operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "COVID-19, Coronavirus Infections, Pandemics, and Quarantine are relevant exploded descriptors; each is explicitly tagged."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add common 2019-nCoV and COVID disease-name variants to the title/abstract layer."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Evaluation found no syntax, field, wildcard, proximity, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No optional limits or study-design filters are applied; the Entrez-date bound is supplied by the run environment."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "exposure",
          "finding": "The text-word layer does not cover common alternate disease-name forms such as 'novel coronavirus' and 'coronavirus disease 2019'.",
          "recommendation": "Add likely 2019-nCoV / novel coronavirus / coronavirus disease 2019 title-abstract forms, then re-evaluate translations and known-record recall.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "932b37512241f04133bf2718eb21760a4334aea081a3f73dd5a2e29942d68fdc",
      "note": "Same-context critic: no fresh-context reviewer was available under the run constraints.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The defining exposure is searched in one broad block; lifestyle and well-being outcomes and population are screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR connects exposure synonyms and restriction descriptions; the query uses no NOT."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified COVID-19, Coronavirus Infections, Pandemics, and Quarantine headings are relevant; COVID-19 is a newer descriptor, so the audit will flag historical indexing limitations."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revision adds 2019-nCoV, novel coronavirus, and coronavirus disease 2019 variants with proximity where word order may vary."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All clauses translated without warnings; no syntax, field, wildcard, or proximity blockers were returned."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No limits or unvalidated filters; the Entrez-date bound is handled by PSB_AS_OF."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "exposure",
          "finding": "The text-word layer does not cover common alternate disease-name forms such as 'novel coronavirus' and 'coronavirus disease 2019'.",
          "recommendation": "Add likely 2019-nCoV / novel coronavirus / coronavirus disease 2019 title-abstract forms, then re-evaluate translations and known-record recall.",
          "status": "resolved",
          "response": "Added 2019 nCoV, novel coronavirus, 2019 novel coronavirus, and coronavirus disease 2019 text variants. The complete re-evaluation returned all six screened development records (6/6) and no translation issues; the final count remained 126,898."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "document",
          "kind": "structural",
          "block": "exposure",
          "finding": "The broad OR exposure block also retrieves papers about other coronavirus outbreaks or pandemics and restriction language without an explicit COVID-19 label.",
          "recommendation": "Keep the broad block for sensitivity and state that screening must confirm COVID-19 relevance.",
          "status": "accepted-risk",
          "response": "The query is intentionally recall-first and uses one exposure block because lockdown/pandemic terminology is variable. Outcomes and pandemic relevance are eligibility-screened; the block returned 126,898 records under the Entrez-date bound, so screening burden is substantial."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "932b37512241f04133bf2718eb21760a4334aea081a3f73dd5a2e29942d68fdc",
      "note": "Same-context closing critic: no fresh-context reviewer was available under the run constraints.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "F1 was resolved by adding disease-name variants; F2 is carried as an accepted screening-burden risk."
        },
        "operators": {
          "verdict": "pass",
          "note": "No Boolean or proximity changes were made after the reviewed version."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The same relevant, explicitly tagged descriptors remain; historical indexing caveat is documented."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Alternate disease-name forms are present and current evaluation shows no translation issues."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or validation blockers are present in the evaluated version."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unvalidated filter or publication-date limit was introduced."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "exposure",
          "finding": "The text-word layer does not cover common alternate disease-name forms such as 'novel coronavirus' and 'coronavirus disease 2019'.",
          "recommendation": "Add likely 2019-nCoV / novel coronavirus / coronavirus disease 2019 title-abstract forms, then re-evaluate translations and known-record recall.",
          "status": "resolved",
          "response": "Added 2019 nCoV, novel coronavirus, 2019 novel coronavirus, and coronavirus disease 2019 text variants. Evaluation retrieved all six screened development records and reported no translation issues."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "document",
          "kind": "structural",
          "block": "exposure",
          "finding": "The broad OR exposure block also retrieves papers about other coronavirus outbreaks or pandemics and restriction language without an explicit COVID-19 label.",
          "recommendation": "Keep the broad block for sensitivity and state that screening must confirm COVID-19 relevance.",
          "status": "accepted-risk",
          "response": "The query intentionally favors recall by retaining varied pandemic and restriction labels in one exposure block. Eligibility screening must confirm COVID-19 relevance; the resulting screening burden is documented."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


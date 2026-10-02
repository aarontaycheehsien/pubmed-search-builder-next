# PubMed search strategy: audit

Generated 2026-10-02T14:07:32+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (Proceeding without clarification at the user's request. Assumed either lifestyle behavior or well-being outcomes are eligible; no population subgroup, language, or publication-date restrictions were specified. PubMed retrieval is bounded by the harness PSB_AS_OF=2020-11-22 Entrez-date setting; no publication-date limit is applied. No known relevant articles were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The pandemic and associated restrictions define the exposure and should be named in records; search COVID-19 and lockdown/restriction vocabulary broadly in one exposure block. |
| Lifestyle behaviors and well-being | screen | These are outcomes and may be inconsistently described in titles, abstracts, or indexing; screen for studies reporting either lifestyle behavior or well-being outcomes rather than requiring an outcome block. |
| People affected by the pandemic or restrictions | screen | The question specifies no population subgroup; population and setting are assessed at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:06:56+00:00
- Records added to PubMed up to: 2020-11-22
- Total records: 121,518
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `COVID-19[Mesh]` | 57,089 | none |
| 2 | `Coronavirus Infections[Mesh]` | 67,535 | none |
| 3 | `Quarantine[Mesh]` | 3,936 | none |
| 4 | `COVID-19[tiab]` | 67,388 | none |
| 5 | `COVID19[tiab]` | 64,206 | none |
| 6 | `"COVID 19"[tiab]` | 67,388 | none |
| 7 | `"coronavirus disease 2019"[tiab]` | 14,613 | none |
| 8 | `"coronavirus disease-19"[tiab]` | 777 | none |
| 9 | `"2019 novel coronavirus"[tiab]` | 1,176 | none |
| 10 | `2019-nCoV[tiab]` | 1,288 | none |
| 11 | `2019 nCoV[tiab]` | 1,288 | none |
| 12 | `SARS-CoV-2[tiab]` | 23,503 | none |
| 13 | `SARS CoV 2[tiab]` | 23,503 | none |
| 14 | `"novel coronavirus"[tiab]` | 6,179 | none |
| 15 | `lockdown*[tiab]` | 3,416 | none |
| 16 | `"lock down"[tiab]` | 163 | none |
| 17 | `"stay at home"[tiab]` | 815 | none |
| 18 | `"stay-at-home"[tiab]` | 815 | none |
| 19 | `"shelter in place"[tiab]` | 210 | none |
| 20 | `"shelter-in-place"[tiab]` | 210 | none |
| 21 | `quarantin*[tiab]` | 6,954 | none |
| 22 | `"social distancing"[tiab]` | 2,657 | none |
| 23 | `"physical distancing"[tiab]` | 436 | none |
| 24 | `"movement restriction"[tiab]` | 280 | none |
| 25 | `"movement restrictions"[tiab]` | 307 | none |
| 26 | `"community containment"[tiab]` | 20 | none |
| 27 | `"containment measure"[tiab]` | 40 | none |
| 28 | `"containment measures"[tiab]` | 601 | none |
| 29 | `Pandemics[Mesh]` | 50,277 | none |
| 30 | `pandemic*[tiab]` | 58,444 | none |
| 31 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30` | 121,518 | none |

### Strategy (single line, for copying into PubMed)

```text
((COVID-19[Mesh] OR Coronavirus Infections[Mesh] OR Quarantine[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR "COVID 19"[tiab] OR "coronavirus disease 2019"[tiab] OR "coronavirus disease-19"[tiab] OR "2019 novel coronavirus"[tiab] OR 2019-nCoV[tiab] OR 2019 nCoV[tiab] OR SARS-CoV-2[tiab] OR SARS CoV 2[tiab] OR "novel coronavirus"[tiab] OR lockdown*[tiab] OR "lock down"[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "shelter in place"[tiab] OR "shelter-in-place"[tiab] OR quarantin*[tiab] OR "social distancing"[tiab] OR "physical distancing"[tiab] OR "movement restriction"[tiab] OR "movement restrictions"[tiab] OR "community containment"[tiab] OR "containment measure"[tiab] OR "containment measures"[tiab] OR Pandemics[Mesh] OR pandemic*[tiab])) AND ("1800/01/01"[edat] : "2020/11/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 231,034 | initial | none | Initial recall-first exposure block combines COVID-19/pandemic and related restriction language; outcomes and population remain screening concepts. Added five screened primary studies as development records. No matching prior review was identified for a benchmark by the cutoff. |
| 2 | 95,634 | pandemic_lockdown: +0 / -4 | none | Removed generic pandemic, confinement, and social-isolation alternatives after evaluation showed they substantially broadened the exposure-only set without adding identifiable scope; retained COVID identifiers and specific lockdown, quarantine, distancing, and containment vocabulary. No development records lost. |
| 3 | 121,518 | pandemic_lockdown: +2 / -0 | none | Restored the pandemic dimension as Pandemics[Mesh] and pandemic*[tiab] in response to the critic's scope and subject-heading findings; retained the remaining exposure terms. This may increase noise from pandemics other than COVID-19, which screening will resolve. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-T1 must-fix open, R1-SH1 should-fix open
- Round 2 on version 3: 2 findings; R1-T1 must-fix resolved, R1-SH1 should-fix resolved
- Round 3 on version 3: 2 findings; R1-T1 must-fix resolved, R1-SH1 should-fix resolved
- Round 4 on version 3: 2 findings; R1-T1 must-fix resolved, R1-SH1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 346 NCBI requests logged (207 from cache); strategy sha256 51711a6a8aec._

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
      "checked_at": "2026-10-02T14:06:56+00:00",
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
      "checked_at": "2026-10-02T14:06:56+00:00",
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
      "requested": "Quarantine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:06:56+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "Quarantine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Pandemics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:06:56+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Pandemics",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"covid 19\"[MeSH Terms] OR \"coronavirus infections\"[MeSH Terms] OR \"quarantine\"[MeSH Terms] OR \"covid 19\"[Title/Abstract] OR \"COVID19\"[Title/Abstract] OR \"covid 19\"[Title/Abstract] OR \"coronavirus disease 2019\"[Title/Abstract] OR \"coronavirus disease-19\"[Title/Abstract] OR \"2019 novel coronavirus\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"2019-nCoV\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"SARS-CoV-2\"[Title/Abstract] OR \"novel coronavirus\"[Title/Abstract] OR \"lockdown*\"[Title/Abstract] OR \"lock down\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"stay-at-home\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"shelter-in-place\"[Title/Abstract] OR \"quarantin*\"[Title/Abstract] OR \"social distancing\"[Title/Abstract] OR \"physical distancing\"[Title/Abstract] OR \"movement restriction\"[Title/Abstract] OR \"movement restrictions\"[Title/Abstract] OR \"community containment\"[Title/Abstract] OR \"containment measure\"[Title/Abstract] OR \"containment measures\"[Title/Abstract] OR \"pandemics\"[MeSH Terms] OR \"pandemic*\"[Title/Abstract]) AND 1800/01/01:2020/11/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "e2ef48dec217ff854847b0ab347639e4935bb675b1d8213808c259872ca20fdd",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searched exposure concept explicitly includes the pandemic and eligibility names SARS-CoV-2 pandemic context, but the strategy has no bare pandemic term. COVID-19 and restriction terms may not retrieve records that describe the context only as a pandemic."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure synonyms are combined with OR in one block, consistent with the scope. No proximity operators are used."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "COVID-19, Coronavirus Infections, and Quarantine are verified and relevant headings, but Pandemics[Mesh] was removed and is absent despite pandemic being an explicitly named exposure dimension."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The list has broad COVID-19 and restriction vocabulary, but pandemic*[tiab] was removed. The development set is not independent and all five known records remain retrieved, which does not establish that this omission is safe."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported queries have no PubMed errors or warnings. The phrase forms and truncation terms are syntactically accepted; no proximity syntax requires interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limits are applied. The Entrez-date boundary through 2020-11-22 is stated in the notes and reflected in the executed query."
        }
      },
      "findings": [
        {
          "id": "R1-T1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The strategy does not search the pandemic dimension by its bare name, although the exposure concept and eligibility explicitly name the COVID-19 pandemic and SARS-CoV-2 pandemic context. Records may describe the context as a pandemic without using the listed virus names or restriction terms.",
          "recommendation": "Restore pandemic*[tiab] as an independent exposure term and retain screening to determine whether the pandemic context is relevant to the eligible outcomes. Re-evaluate the complete search after the change.",
          "status": "open"
        },
        {
          "id": "R1-SH1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Pandemics[Mesh] was removed from the prior strategy and is absent from the current exposure block, despite pandemic being an explicitly named concept.",
          "recommendation": "Add Pandemics[Mesh] alongside the existing verified headings, then re-evaluate the complete search and its retrieval diagnostics.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "7fd2e1cd9f435fba3ddf284562ff7592200156cd1d2b776ea27645886bd96932",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block covers the named COVID-19, SARS-CoV-2, pandemic, and lockdown/restriction dimensions. pandemic*[tiab] searches the pandemic dimension by its bare name, addressing the prior coverage gap."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms are joined with OR in one block, consistent with the scope. No proximity operators require interpretation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "COVID-19, Coronavirus Infections, Quarantine, and Pandemics are included as verified headings. Pandemics[Mesh] addresses the prior omission."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block includes COVID-19 and SARS-CoV-2 variants, pandemic*[tiab], and lockdown, quarantine, distancing, and containment vocabulary. All five development records are retrieved; as noted previously, this development set is not independent evidence of sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported queries have no PubMed errors, warnings, or translation issues. No proximity syntax is used."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limits are applied. The Entrez-date boundary through 2020-11-22 is documented and appears in the executed query."
        }
      },
      "findings": [
        {
          "id": "R1-T1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The strategy did not search the pandemic dimension by its bare name, although the exposure concept and eligibility explicitly name the COVID-19 pandemic and SARS-CoV-2 pandemic context.",
          "recommendation": "Restore pandemic*[tiab] as an independent exposure term and re-evaluate the complete search.",
          "status": "resolved",
          "response": "pandemic*[tiab] is present in the current exposure block, and the complete search was re-evaluated. The current strategy retrieves all five listed development records."
        },
        {
          "id": "R1-SH1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Pandemics[Mesh] was absent from the exposure block despite pandemic being an explicitly named concept.",
          "recommendation": "Add Pandemics[Mesh] and re-evaluate the complete search and its retrieval diagnostics.",
          "status": "resolved",
          "response": "Pandemics[Mesh] is included in the current exposure block, and the complete search was re-evaluated."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "7fd2e1cd9f435fba3ddf284562ff7592200156cd1d2b776ea27645886bd96932",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block searches COVID-19, SARS-CoV-2, pandemic, and lockdown or restriction dimensions. pandemic*[tiab] covers the pandemic dimension by its bare name."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms are joined with OR in one block, consistent with the stated scope. No proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "COVID-19, Coronavirus Infections, Quarantine, and Pandemics are included as verified headings; the prior Pandemics[Mesh] omission is addressed."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block includes pandemic*[tiab] and broad COVID-19, SARS-CoV-2, lockdown, quarantine, distancing, and containment vocabulary. All five development records are retrieved; that development set is not independent evidence of sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported queries have no PubMed errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limits are applied. The Entrez-date boundary through 2020-11-22 is documented and appears in the executed query."
        }
      },
      "findings": [
        {
          "id": "R1-T1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The strategy did not search the pandemic dimension by its bare name, although the exposure concept and eligibility explicitly name the COVID-19 pandemic and SARS-CoV-2 pandemic context.",
          "recommendation": "Restore pandemic*[tiab] as an independent exposure term and re-evaluate the complete search.",
          "status": "resolved",
          "response": "pandemic*[tiab] is present in the current exposure block, and the complete search was re-evaluated. The current strategy retrieves all five listed development records."
        },
        {
          "id": "R1-SH1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Pandemics[Mesh] was absent from the exposure block despite pandemic being an explicitly named concept.",
          "recommendation": "Add Pandemics[Mesh] and re-evaluate the complete search and its retrieval diagnostics.",
          "status": "resolved",
          "response": "Pandemics[Mesh] is included in the current exposure block, and the complete search was re-evaluated."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 4,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "8ba764288b778eb3e4fce0ceaf16d06f0766b9458226922311684cbd6a56b82e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block searches the named COVID-19, SARS-CoV-2, pandemic, and lockdown or restriction dimensions. pandemic*[tiab] covers pandemic by its bare name."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are joined with OR in one block, consistent with the stated scope. No proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "COVID-19, Coronavirus Infections, Quarantine, and Pandemics are included as verified headings; Pandemics[Mesh] remains present."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block retains pandemic*[tiab] and broad COVID-19, SARS-CoV-2, lockdown, quarantine, distancing, and containment vocabulary. All six listed development records are retrieved, though this set is not independent evidence of sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported queries have no PubMed errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limits are applied. The Entrez-date boundary through 2020-11-22 is documented and appears in the executed query."
        }
      },
      "findings": [
        {
          "id": "R1-T1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The strategy previously did not search the pandemic dimension by its bare name, although the exposure concept and eligibility explicitly name the COVID-19 pandemic and SARS-CoV-2 pandemic context.",
          "recommendation": "Restore pandemic*[tiab] as an independent exposure term and re-evaluate the complete search.",
          "status": "resolved",
          "response": "pandemic*[tiab] remains in the exposure block, and the complete search was re-evaluated. All six listed development records are retrieved."
        },
        {
          "id": "R1-SH1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Pandemics[Mesh] was previously absent from the exposure block despite pandemic being an explicitly named concept.",
          "recommendation": "Add Pandemics[Mesh] and re-evaluate the complete search and its retrieval diagnostics.",
          "status": "resolved",
          "response": "Pandemics[Mesh] is included in the exposure block, and the complete search was re-evaluated."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


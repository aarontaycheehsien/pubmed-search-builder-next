# PubMed search strategy: audit

Generated 2026-10-02T14:01:43+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (diagnostic-test-accuracy review): in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?
- Framework: PIRD
- Scope confirmed by user: no (Proceeding without user clarification as requested; the scope is an agent-recorded assumption, not user-confirmed. Scope assumes malaria and rapid diagnostic test are the only AND-ed concepts; species, uncomplicated status, endemic setting, reference standard, and accuracy are screened. No known relevant articles were supplied. The harness requires PubMed Entrez-date bound PSB_AS_OF=2013-06-09 for every command; protocol as_of records this bound. No publication-date ([dp]) limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Malaria, including Plasmodium vivax and non-falciparum malaria | search | The target condition is required in all eligible studies and is reliably named/indexed. Search malaria broadly to preserve sensitivity; screen species and uncomplicated status. |
| Malaria rapid diagnostic tests | search | The index test is required and commonly named as a rapid diagnostic test, RDT, or antigen test; search explicit rapid-test vocabulary and screen test eligibility. |
| Non-falciparum / P. vivax species, uncomplicated disease, endemic setting | screen | These eligibility details may be reported only in full text and should not be required as additional AND blocks. |
| Eligible reference standard and diagnostic performance | screen | Reference standards and accuracy measures are screening criteria and are inconsistently named in titles/abstracts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:00:59+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,172
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `malaria[tiab]` | 55,839 | none |
| 3 | `malarial[tiab]` | 7,260 | none |
| 4 | `malarias[tiab]` | 272 | none |
| 5 | `plasmodium[tiab]` | 34,635 | none |
| 6 | `plasmodia[tiab]` | 1,281 | none |
| 7 | `vivax[tiab]` | 5,921 | none |
| 8 | `ovale[tiab]` | 5,356 | none |
| 9 | `malariae[tiab]` | 888 | none |
| 10 | `falciparum[tiab]` | 25,874 | none |
| 11 | `"non-falciparum"[tiab]` | 55 | none |
| 12 | `"non falciparum"[tiab]` | 55 | none |
| 13 | `"nonfalciparum"[tiab]` | 59 | none |
| 14 | `"P. vivax"[tiab]` | 2,944 | none |
| 15 | `"P. ovale"[tiab]` | 503 | none |
| 16 | `"P. malariae"[tiab]` | 571 | none |
| 17 | `"Malaria, Vivax"[Mesh]` | 2,872 | none |
| 18 | `"Plasmodium vivax"[Mesh]` | 3,745 | none |
| 19 | `"Plasmodium vivax"[tiab]` | 3,467 | none |
| 20 | `"Plasmodium ovale"[tiab]` | 274 | none |
| 21 | `"Plasmodium malariae"[tiab]` | 421 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 81,583 | none |
| 23 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 | none |
| 24 | `"rapid diagnostic test"[tiab]` | 579 | none |
| 25 | `"rapid diagnostic tests"[tiab]` | 769 | none |
| 26 | `"rapid test"[tiab]` | 2,005 | none |
| 27 | `"rapid tests"[tiab]` | 891 | none |
| 28 | `RDT[tiab]` | 653 | none |
| 29 | `RDTs[tiab]` | 303 | none |
| 30 | `immunochromatograph*[tiab]` | 1,749 | none |
| 31 | `"lateral flow"[tiab:~1]` | 829 | none |
| 32 | `dipstick*[tiab]` | 2,298 | none |
| 33 | `"test strip"[tiab]` | 676 | none |
| 34 | `"test strips"[tiab]` | 775 | none |
| 35 | `"antigen test"[tiab]` | 1,412 | none |
| 36 | `"antigen tests"[tiab]` | 519 | none |
| 37 | `"antigen detection"[tiab]` | 3,135 | none |
| 38 | `"point of care"[tiab:~1]` | 6,273 | none |
| 39 | `"rapid diagnostic"[tiab]` | 2,352 | none |
| 40 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 35,559 | none |
| 41 | `#22 AND #40` | 1,172 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR malaria[tiab] OR malarial[tiab] OR malarias[tiab] OR plasmodium[tiab] OR plasmodia[tiab] OR vivax[tiab] OR ovale[tiab] OR malariae[tiab] OR falciparum[tiab] OR "non-falciparum"[tiab] OR "non falciparum"[tiab] OR "nonfalciparum"[tiab] OR "P. vivax"[tiab] OR "P. ovale"[tiab] OR "P. malariae"[tiab] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR "Plasmodium vivax"[tiab] OR "Plasmodium ovale"[tiab] OR "Plasmodium malariae"[tiab]) AND ("Reagent Kits, Diagnostic"[Mesh] OR "rapid diagnostic test"[tiab] OR "rapid diagnostic tests"[tiab] OR "rapid test"[tiab] OR "rapid tests"[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR "lateral flow"[tiab:~1] OR dipstick*[tiab] OR "test strip"[tiab] OR "test strips"[tiab] OR "antigen test"[tiab] OR "antigen tests"[tiab] OR "antigen detection"[tiab] OR "point of care"[tiab:~1] OR "rapid diagnostic"[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 35,559 | 0 |
| rapid_test | 81,583 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,152 | initial | none | Initial two-block recall-first PIRD strategy; malaria and rapid-test concepts searched, eligibility details screened. Used only controlled headings introduced by 2013; omitted 2016/2023 point-of-care / rapid-test headings. |
| 2 | 1,172 | malaria: +5 / -0; rapid_test: +1 / -0 | none | Added screened-record vocabulary from MeSH/tiab term ranking: explicit vivax malaria and Plasmodium headings, full species names, and rapid diagnostic wording; no concepts or limits changed. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; P1-01 must-fix open
- Round 2 on version 2: 1 findings; P1-01 must-fix resolved
- Round 3 on version 2: 1 findings; P1-01 must-fix resolved
- Round 4 on version 2: 1 findings; P1-01 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 731 NCBI requests logged (354 from cache); strategy sha256 23920b524cc0._

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
      "requested": "Malaria",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:00:59+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008288",
          "name": "Malaria",
          "type": "descriptor",
          "scope_note": "A protozoan disease caused in humans by four species of the PLASMODIUM genus: PLASMODIUM FALCIPARUM; PLASMODIUM VIVAX; PLASMODIUM OVALE; and PLASMODIUM MALARIAE; and transmitted by the bite of an infected female mosquito of the genus ANOPHELES. Malaria is endemic in parts of Asia, Africa, Central and South America, Oceania, and certain Caribbean islands. It is characterized by extreme exhaustio...",
          "tree_numbers": [
            "C01.610.752.530",
            "C01.920.852.750"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008288",
      "preferred_label": "Malaria",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Malaria",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Malaria, Vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:00:59+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016780",
          "name": "Malaria, Vivax",
          "type": "descriptor",
          "scope_note": "Malaria caused by PLASMODIUM VIVAX. This form of malaria is less severe than MALARIA, FALCIPARUM, but there is a higher probability for relapses to occur. Febrile paroxysms often occur every other day.",
          "tree_numbers": [
            "C01.610.752.530.700",
            "C01.920.852.750.700"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016780",
      "preferred_label": "Malaria, Vivax",
      "type": "descriptor",
      "location": "vocabulary:17",
      "term": {
        "text": "\"Malaria, Vivax\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:00:59+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010966",
          "name": "Plasmodium vivax",
          "type": "descriptor",
          "scope_note": "A protozoan parasite that causes vivax malaria (MALARIA, VIVAX). This species is found almost everywhere malaria is endemic and is the only one that has a range extending into the temperate regions.",
          "tree_numbers": [
            "B01.043.075.380.611.761"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010966",
      "preferred_label": "Plasmodium vivax",
      "type": "descriptor",
      "location": "vocabulary:18",
      "term": {
        "text": "\"Plasmodium vivax\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:00:59+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011933",
          "name": "Reagent Kits, Diagnostic",
          "type": "descriptor",
          "scope_note": "Commercially prepared reagent sets, with accessory devices, containing all of the major components and literature necessary to perform one or more designated diagnostic tests or procedures. They may be for laboratory or personal use.",
          "tree_numbers": [
            "D27.505.259.875",
            "D27.720.470.410.680",
            "E07.720"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011933",
      "preferred_label": "Reagent Kits, Diagnostic",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "\"Reagent Kits, Diagnostic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"malarial\"[Title/Abstract] OR \"malarias\"[Title/Abstract] OR \"plasmodium\"[Title/Abstract] OR \"plasmodia\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"falciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"malaria, vivax\"[MeSH Terms] OR \"Plasmodium vivax\"[MeSH Terms] OR \"Plasmodium vivax\"[Title/Abstract] OR \"Plasmodium ovale\"[Title/Abstract] OR \"Plasmodium malariae\"[Title/Abstract]) AND (\"reagent kits, diagnostic\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract:~1] OR \"dipstick*\"[Title/Abstract] OR \"test strip\"[Title/Abstract] OR \"test strips\"[Title/Abstract] OR \"antigen test\"[Title/Abstract] OR \"antigen tests\"[Title/Abstract] OR \"antigen detection\"[Title/Abstract] OR \"point of care\"[Title/Abstract:~1] OR \"rapid diagnostic\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "655e76ea88f9206cb7e438cc384a9a3e28983705079a532526b19ed3201e73b7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The blocks cover malaria and the named Plasmodium species, plus rapid-test, RDT, immunochromatography, antigen-test, and related vocabulary. Species and setting eligibility details are appropriately screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each block and AND combines the two searched concepts, consistent with the stated scope. The proximity expressions have no reported PubMed warnings."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses verified Malaria and vivax headings and a diagnostic-kit heading alongside free-text terms. No vocabulary verification errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the key malaria species and rapid-test terminology. Four known relevant records are retrieved, though this small development set does not establish broad sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query parses without errors; the only translation is the expected Malaria MeSH translation."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The 2013-06-09 Entrez date bound was required by the harness but was not explicit in the protocol's as_of field; making the mandated bound explicit and retaining it."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query applies an Entrez date range ending 2013-06-09, but the protocol did not explicitly identify it as the harness-mandated as-of bound.",
          "recommendation": "Record the required Entrez date bound explicitly in protocol.json as_of; retain no publication-date limit.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "5acbb3bb79f5c449a4b073f2d6419f34cc622e396cf2b834e66aadbb827d3b33",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria block covers the named species, and the rapid-test block includes explicit rapid-test, RDT, immunochromatography, and antigen-test terms. Species, severity, setting, reference standard, and accuracy are appropriately left for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each searched concept and AND combines the two required concepts. The proximity terms have no reported warnings; no warning requires clause-specific interpretation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Malaria, Malaria, Vivax, Plasmodium vivax, and Reagent Kits, Diagnostic headings; no vocabulary verification errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The free-text terms cover malaria and the named non-falciparum species, along with the stated rapid-test terminology. All four development records were retrieved; this small set does not establish broad sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The executed query reports no errors or warnings. The Malaria heading translation is expected, and the final query reflects the two stated blocks."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The protocol now explicitly records the harness-mandated 2013-06-09 Entrez date bound and states that no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query applies an Entrez date range ending 2013-06-09, but the protocol did not explicitly identify it as the harness-mandated as-of bound.",
          "recommendation": "Record the required Entrez date bound explicitly in protocol.json as_of; retain no publication-date limit.",
          "status": "resolved",
          "response": "The protocol now records as_of as 2013-06-09 and explains that this is the harness-mandated Entrez-date bound; it also states that no publication-date limit is used."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "5acbb3bb79f5c449a4b073f2d6419f34cc622e396cf2b834e66aadbb827d3b33",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two searched concepts match the stated scope. Species, severity, setting, reference standard, and accuracy remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines terms within each concept and AND combines the two required concepts. The packet reports no proximity warnings."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Malaria, Malaria, Vivax, Plasmodium vivax, and Reagent Kits, Diagnostic headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover malaria and named Plasmodium species, plus explicit rapid-test, RDT, immunochromatography, and antigen-test vocabulary. All four development records are retrieved; this small set does not establish broad sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The executed query reports no errors or warnings, and its translation reflects the two stated blocks and Entrez date bound."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The protocol now records the 2013-06-09 harness-mandated Entrez-date bound and states that no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query applies an Entrez date range ending 2013-06-09, but the protocol did not explicitly identify it as the harness-mandated as-of bound.",
          "recommendation": "Record the required Entrez date bound explicitly in protocol.json as_of; retain no publication-date limit.",
          "status": "resolved",
          "response": "The protocol records as_of as 2013-06-09, explains that this is the harness-mandated Entrez-date bound, and states that no publication-date limit is used."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 4,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "671ee17ce463a9041fd475612eba87758742bd1e0b5f7071581acfa555aedabf",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two searched concepts match the stated scope. The malaria terms cover the named Plasmodium species; species, severity, setting, reference standard, and diagnostic performance remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines terms within each concept and AND combines the two required concepts. The proximity terms have no reported warnings."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Malaria, Malaria, Vivax, Plasmodium vivax, and Reagent Kits, Diagnostic headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover malaria and the named species, plus rapid-test, RDT, immunochromatography, and antigen-test vocabulary. All seven development records were retrieved; this development set is not independent validation and does not establish broad sensitivity."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The executed query reports no errors or warnings. Its translation reflects the two stated blocks and the Entrez date bound."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The protocol records the 2013-06-09 harness-mandated Entrez-date bound and states that no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query applies an Entrez date range ending 2013-06-09, but the protocol did not explicitly identify it as the harness-mandated as-of bound.",
          "recommendation": "Record the required Entrez date bound explicitly in protocol.json as_of; retain no publication-date limit.",
          "status": "resolved",
          "response": "The protocol records as_of as 2013-06-09, explains that this is the harness-mandated Entrez-date bound, and states that no publication-date limit is used."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


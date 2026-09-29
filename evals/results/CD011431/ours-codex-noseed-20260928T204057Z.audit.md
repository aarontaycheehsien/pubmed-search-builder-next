# PubMed search strategy: audit

Generated 2026-09-28T21:02:25+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (a diagnostic-test-accuracy review: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?)
- Framework: PIRD
- Scope confirmed by user: yes (User asked to proceed without questions; scope roles are provisional assumptions. Standard depth; default workload budget 10,000. No known relevant records supplied. No publication-date, language, or other limits. PubMed entry-date bound PSB_AS_OF=2013-06-09 is imposed by the run harness, not a publication-date filter.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum malaria, including Plasmodium vivax | search | Target diagnosis is required in every eligible record and is indexed/named; species can be indexed as members of the malaria category. |
| Malaria rapid diagnostic tests | search | Index test is required in every eligible record; studies may name a commercial test/member rather than the category phrase. |
| Malaria-endemic setting | optional | Setting is an explicit eligibility criterion and sometimes named as endemic, but many eligible studies only name the country; test the searchable setting labels before deciding. |
| Suspected or confirmed uncomplicated malaria | screen | Clinical suspicion and severity are not named consistently enough to require as search blocks. |
| Diagnostic accuracy and eligible reference standard | screen | Accuracy terminology and reference-standard details are unreliable as title/abstract search requirements. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:01:44+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,754
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Malaria"[Mesh]` | 50,641 | none |
| 2 | `"Malaria, Vivax"[Mesh]` | 2,872 | none |
| 3 | `malaria[tiab]` | 55,839 | none |
| 4 | `vivax[tiab]` | 5,921 | none |
| 5 | `"non-falciparum"[tiab]` | 55 | none |
| 6 | `nonfalciparum[tiab]` | 59 | none |
| 7 | `"non falciparum"[tiab]` | 55 | none |
| 8 | `malariae[tiab]` | 888 | none |
| 9 | `ovale[tiab]` | 5,356 | none |
| 10 | `knowlesi[tiab]` | 866 | none |
| 11 | `"Plasmodium vivax"[tiab]` | 3,467 | none |
| 12 | `"Plasmodium malariae"[tiab]` | 421 | none |
| 13 | `"Plasmodium ovale"[tiab]` | 274 | none |
| 14 | `"Plasmodium knowlesi"[tiab]` | 687 | none |
| 15 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14` | 72,038 | none |
| 16 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 | none |
| 17 | `"Diagnostic Tests, Routine"[Mesh]` | 7,136 | none |
| 18 | `"rapid diagnostic test"[tiab]` | 579 | none |
| 19 | `"rapid diagnostic tests"[tiab]` | 769 | none |
| 20 | `"malaria rapid diagnostic test"[tiab]` | 46 | none |
| 21 | `"malaria rapid diagnostic tests"[tiab]` | 110 | none |
| 22 | `"rapid malaria test"[tiab]` | 25 | none |
| 23 | `"rapid malaria tests"[tiab]` | 12 | none |
| 24 | `"rapid test"[tiab]` | 2,005 | none |
| 25 | `"rapid tests"[tiab]` | 891 | none |
| 26 | `immunochromatographic[tiab]` | 1,333 | none |
| 27 | `immunochromatography[tiab]` | 490 | none |
| 28 | `"lateral flow"[tiab]` | 720 | none |
| 29 | `dipstick[tiab]` | 2,112 | none |
| 30 | `OptiMAL[tiab]` | 235,534 | none |
| 31 | `Paracheck[tiab]` | 53 | none |
| 32 | `CareStart[tiab]` | 21 | none |
| 33 | `VIKIA[tiab]` | 19 | none |
| 34 | `BinaxNOW[tiab]` | 47 | none |
| 35 | `"SD Bioline"[tiab]` | 59 | none |
| 36 | `RDT[tiab]` | 653 | none |
| 37 | `#16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36` | 265,504 | none |
| 38 | `#15 AND #37` | 1,754 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR malaria[tiab] OR vivax[tiab] OR "non-falciparum"[tiab] OR nonfalciparum[tiab] OR "non falciparum"[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab] OR "Plasmodium vivax"[tiab] OR "Plasmodium malariae"[tiab] OR "Plasmodium ovale"[tiab] OR "Plasmodium knowlesi"[tiab]) AND ("Reagent Kits, Diagnostic"[Mesh] OR "Diagnostic Tests, Routine"[Mesh] OR "rapid diagnostic test"[tiab] OR "rapid diagnostic tests"[tiab] OR "malaria rapid diagnostic test"[tiab] OR "malaria rapid diagnostic tests"[tiab] OR "rapid malaria test"[tiab] OR "rapid malaria tests"[tiab] OR "rapid test"[tiab] OR "rapid tests"[tiab] OR immunochromatographic[tiab] OR immunochromatography[tiab] OR "lateral flow"[tiab] OR dipstick[tiab] OR OptiMAL[tiab] OR Paracheck[tiab] OR CareStart[tiab] OR VIKIA[tiab] OR BinaxNOW[tiab] OR "SD Bioline"[tiab] OR RDT[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Malaria-endemic setting | left out | 1,754 / 395 | 77.5% | 15228812, 22929630, 23608372, 23692957 | 1/30 | Do not require the setting wording: the candidate would reduce the main result set by 77.5%, but it loses known eligible development records and a screened loss sample contained PMID 15228812, an eligible non-falciparum RDT evaluation from a mesoendemic area. This conservative block also cannot capture studies that only name the country; keep endemicity for screening. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum malaria, including Plasmodium vivax | 1 | `Plasmodium[tiab] OR plasmodia[tiab] OR malaria parasite[tiab] OR Malaria[Mesh]` | 68 | 0/30 |
| Malaria rapid diagnostic tests | 1 | `rapid[tiab] OR test[tiab] OR tests[tiab] OR kit[tiab] OR kits[tiab] OR assay[tiab] OR assays[tiab]` | 8,691 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 265,504 | 0 |
| rdt | 72,038 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | First recall-first two-block draft; older diagnostic kit headings and test/species terminology found in the screened records; post-cutoff MeSH headings excluded. |
| 2 | 1,754 | malaria: +14 / -0; rdt: +21 / -0 | none | First recall-first two-block draft; terms drawn from screened records; post-cutoff MeSH headings excluded. |
| 3 | 1,754 | limits/combination | none | Test a protocol-named optional endemic-setting block; country-only setting mentions are not reliably searchable. |
| 4 | 1,754 | limits/combination | none | Expand optional setting block to cover endemicity morphology after a known endemic-setting record was absent from the first version; retest its reduction and known loss. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 0 findings; 
- Round 2 on version 4: 0 findings; 
- Round 3 on version 4: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1067 NCBI requests logged (653 from cache); strategy sha256 e36b7f47a463._

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
      "checked_at": "2026-09-28T21:01:44+00:00",
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
        "text": "\"Malaria\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Malaria, Vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:01:44+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Malaria, Vivax\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:01:44+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Reagent Kits, Diagnostic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:01:44+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003955",
          "name": "Diagnostic Tests, Routine",
          "type": "descriptor",
          "scope_note": "Diagnostic procedures, such as laboratory tests and x-rays, routinely performed on all individuals or specified categories of individuals in a specified situation, e.g., patients being admitted to the hospital. These include routine tests administered to neonates.",
          "tree_numbers": [
            "E01.370.395"
          ],
          "entry_terms": 27,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003955",
      "preferred_label": "Diagnostic Tests, Routine",
      "type": "descriptor",
      "location": "vocabulary:16",
      "term": {
        "text": "\"Diagnostic Tests, Routine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"Malaria\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract] OR \"Plasmodium vivax\"[Title/Abstract] OR \"Plasmodium malariae\"[Title/Abstract] OR \"Plasmodium ovale\"[Title/Abstract] OR \"Plasmodium knowlesi\"[Title/Abstract]) AND (\"reagent kits, diagnostic\"[MeSH Terms] OR \"diagnostic tests, routine\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"malaria rapid diagnostic test\"[Title/Abstract] OR \"malaria rapid diagnostic tests\"[Title/Abstract] OR \"rapid malaria test\"[Title/Abstract] OR \"rapid malaria tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"immunochromatographic\"[Title/Abstract] OR \"immunochromatography\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"dipstick\"[Title/Abstract] OR \"OptiMAL\"[Title/Abstract] OR \"Paracheck\"[Title/Abstract] OR \"CareStart\"[Title/Abstract] OR \"VIKIA\"[Title/Abstract] OR \"BinaxNOW\"[Title/Abstract] OR \"SD Bioline\"[Title/Abstract] OR \"RDT\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "7b5091556688c6477aee555162db22858f9b6b9203a154d928adf2fff1746f63",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria block includes the named diagnosis and bare species epithets; the RDT block includes generic test wording and named test brands. The category probes found no relevant records outside either block in the screened samples."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concepts are OR-combined within blocks and AND-combined across blocks. The optional endemic-setting block was tested and appropriately left out after it removed known eligible records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the listed MeSH descriptors. The strategy also includes title and abstract terms, so retrieval does not depend on indexing alone."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word blocks cover malaria and named species, plus common RDT wording, test formats, acronyms, and several commercial names. The evidence reports retrieval of all eight known relevant records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed query has balanced concept groups, valid field tags, and no translation errors or warnings in the packet."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, or other user-specified limits are reported. The packet identifies the 2013-06-09 entry-date bound as imposed by the run harness."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "7b5091556688c6477aee555162db22858f9b6b9203a154d928adf2fff1746f63",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria block covers the named diagnosis and species with bare terms; the RDT block covers generic test wording and named brands. Category probes found no relevant records outside either block in the screened samples."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within the two required blocks and the blocks are AND-combined. The optional endemic-setting block was tested and left out after it removed known eligible records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH descriptors, and retrieval also uses title and abstract terms rather than relying on indexing alone."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover malaria and named species, RDT wording, test formats, acronyms, and several commercial names. All eight known relevant records were retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query has balanced concept groups and valid field tags, with no translation errors or warnings reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No user-specified publication-date, language, or other limits are reported. The packet identifies the 2013-06-09 entry-date bound as imposed by the run harness."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "7b5091556688c6477aee555162db22858f9b6b9203a154d928adf2fff1746f63",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The blocks cover the named malaria diagnoses and species, and malaria RDT wording, formats, acronyms, and brands. Both category probes screened 0 of 30 records relevant outside their blocks; all eight known relevant records were retrieved."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required concepts are OR-combined within blocks and AND-combined across blocks. The optional endemic-setting block was tested and left out after removing known eligible records and a relevant record from the loss sample."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports both MeSH descriptors as verified; title and abstract terms also support retrieval."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words represent the named species and common RDT terms, test formats, acronyms, and commercial names. All eight known relevant records were retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has balanced concept groups and valid field tags. The packet reports no translation errors, warnings, or proximity expressions requiring clause-specific interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No user-specified limits are reported. The 2013-06-09 entry-date bound is identified as imposed by the run harness."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


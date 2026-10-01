# PubMed search strategy: audit

Generated 2026-10-01T12:37:29+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?
- Framework: PIRD
- Scope confirmed by user: no (User asked to proceed without questions; scope was not interactively confirmed. Assumed all ages, no language restriction, and reference standards include microscopy and/or a validated molecular method or other eligible parasitological comparator. Run date is constrained by PSB_AS_OF=2013-06-09 (Entrez entry-date bound), with no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum malaria, including Plasmodium vivax | search | Target diagnosis; species and malaria are indexed and named, but relevant studies may name only a member species, so a category probe is required. |
| Malaria rapid diagnostic tests | search | The index test is required and commonly identified as a rapid diagnostic test or rapid test. |
| People with suspected or confirmed uncomplicated malaria in endemic settings | screen | Age, uncomplicated status, endemic setting, and suspicion/confirmation can be absent or inconsistent in abstracts; assess at screening. |
| Eligible reference standard and diagnostic accuracy | screen | Reference methods and diagnostic performance are inconsistently named in abstracts; assess eligibility at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:36:31+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,908
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Malaria"[Mesh]` | 50,641 | none |
| 2 | `"Malaria, Vivax"[Mesh]` | 2,872 | none |
| 3 | `"Plasmodium vivax"[Mesh]` | 3,745 | none |
| 4 | `"Plasmodium malariae"[Mesh]` | 810 | none |
| 5 | `"Plasmodium ovale"[Mesh]` | 131 | none |
| 6 | `"Plasmodium knowlesi"[Mesh]` | 280 | none |
| 7 | `malaria[tiab]` | 55,839 | none |
| 8 | `malarial[tiab]` | 7,260 | none |
| 9 | `plasmodium*[tiab]` | 34,658 | none |
| 10 | `plasmodia[tiab]` | 1,281 | none |
| 11 | `vivax[tiab]` | 5,921 | none |
| 12 | `malariae[tiab]` | 888 | none |
| 13 | `ovale[tiab]` | 5,356 | none |
| 14 | `knowlesi[tiab]` | 866 | none |
| 15 | `"non-falciparum"[tiab]` | 55 | none |
| 16 | `"non falciparum"[tiab]` | 55 | none |
| 17 | `nonfalciparum[tiab]` | 59 | none |
| 18 | `"p vivax"[tiab]` | 2,944 | none |
| 19 | `"p malariae"[tiab]` | 571 | none |
| 20 | `"p ovale"[tiab]` | 503 | none |
| 21 | `"p knowlesi"[tiab]` | 425 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 81,441 | none |
| 23 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 | none |
| 24 | `"Point-of-Care Systems"[Mesh]` | 6,781 | none |
| 25 | `"rapid diagnostic test"[tiab:~2]` | 757 | none |
| 26 | `"rapid diagnostic tests"[tiab]` | 769 | none |
| 27 | `"rapid test"[tiab:~2]` | 8,342 | none |
| 28 | `"rapid tests"[tiab]` | 891 | none |
| 29 | `RDT[tiab]` | 653 | none |
| 30 | `RDTs[tiab]` | 303 | none |
| 31 | `mRDT[tiab]` | 14 | none |
| 32 | `MRDTs[tiab]` | 6 | none |
| 33 | `ICT[tiab]` | 2,484 | none |
| 34 | `immunochromatograph*[tiab]` | 1,749 | none |
| 35 | `immuno-chromatograph*[tiab]` | 77 | none |
| 36 | `dipstick*[tiab]` | 2,298 | none |
| 37 | `"antigen detection test"[tiab:~2]` | 299 | none |
| 38 | `"rapid antigen test"[tiab:~2]` | 317 | none |
| 39 | `"point of care"[tiab:~2]` | 6,445 | none |
| 40 | `OptiMAL[tiab]` | 235,534 | none |
| 41 | `Paracheck[tiab]` | 53 | none |
| 42 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41` | 275,422 | none |
| 43 | `#22 AND #42` | 1,908 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR "Plasmodium malariae"[Mesh] OR "Plasmodium ovale"[Mesh] OR "Plasmodium knowlesi"[Mesh] OR malaria[tiab] OR malarial[tiab] OR plasmodium*[tiab] OR plasmodia[tiab] OR vivax[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab] OR "non-falciparum"[tiab] OR "non falciparum"[tiab] OR nonfalciparum[tiab] OR "p vivax"[tiab] OR "p malariae"[tiab] OR "p ovale"[tiab] OR "p knowlesi"[tiab]) AND ("Reagent Kits, Diagnostic"[Mesh] OR "Point-of-Care Systems"[Mesh] OR "rapid diagnostic test"[tiab:~2] OR "rapid diagnostic tests"[tiab] OR "rapid test"[tiab:~2] OR "rapid tests"[tiab] OR RDT[tiab] OR RDTs[tiab] OR mRDT[tiab] OR MRDTs[tiab] OR ICT[tiab] OR immunochromatograph*[tiab] OR immuno-chromatograph*[tiab] OR dipstick*[tiab] OR "antigen detection test"[tiab:~2] OR "rapid antigen test"[tiab:~2] OR "point of care"[tiab:~2] OR OptiMAL[tiab] OR Paracheck[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 14 | 14 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum malaria, including Plasmodium vivax | 1 | `Plasmodium cynomolgi[Mesh] OR cynomolgi[tiab] OR monkey malaria[tiab]` | 0 | 0/0 |
| Non-falciparum malaria, including Plasmodium vivax | 2 | `parasite*[tiab] OR Parasitemia[Mesh]` | 1,045 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria_species | 275,422 | 0 |
| rapid_test | 81,441 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,908 | initial | none | Initial two-block PIRD strategy: required broad malaria/species block and RDT block; added MeSH plus title/abstract species, rapid-test formats, abbreviations and brand examples. No limits. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 2 findings; R1-F1 must-fix open, R1-F2 document accepted-risk
- Round 2 on version 1: 2 findings; R1-F1 must-fix resolved, R1-F2 document accepted-risk
- Round 3 on version 1: 2 findings; R1-F1 must-fix resolved, R1-F2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 601 NCBI requests logged (272 from cache); strategy sha256 92a3913b78ca._

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
      "checked_at": "2026-10-01T12:36:31+00:00",
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
      "checked_at": "2026-10-01T12:36:31+00:00",
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
      "requested": "Plasmodium vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:36:31+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Plasmodium vivax\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium malariae",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:36:31+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010965",
          "name": "Plasmodium malariae",
          "type": "descriptor",
          "scope_note": "A protozoan parasite that occurs primarily in subtropical and temperate areas. It is the causal agent of quartan malaria. As the parasite grows it exhibits little ameboid activity.",
          "tree_numbers": [
            "B01.043.075.380.611.661"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010965",
      "preferred_label": "Plasmodium malariae",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Plasmodium malariae\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium ovale",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:36:31+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D041122",
          "name": "Plasmodium ovale",
          "type": "descriptor",
          "scope_note": "A species of protozoan parasite causing MALARIA. It is the rarest of the four species of PLASMODIUM infecting humans, but is common in West African countries and neighboring areas.",
          "tree_numbers": [
            "B01.043.075.380.611.700"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D041122",
      "preferred_label": "Plasmodium ovale",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "\"Plasmodium ovale\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium knowlesi",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:36:31+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016790",
          "name": "Plasmodium knowlesi",
          "type": "descriptor",
          "scope_note": "A protozoan parasite from Southeast Asia that causes monkey malaria. It is naturally acquired by man in Malaysia and can also be transmitted experimentally to humans.",
          "tree_numbers": [
            "B01.043.075.380.611.610"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016790",
      "preferred_label": "Plasmodium knowlesi",
      "type": "descriptor",
      "location": "vocabulary:6",
      "term": {
        "text": "\"Plasmodium knowlesi\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:36:31+00:00",
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
    },
    {
      "requested": "Point-of-Care Systems",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:36:31+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019095",
          "name": "Point-of-Care Systems",
          "type": "descriptor",
          "scope_note": "Laboratory and other services provided to patients at the bedside. These include diagnostic and laboratory testing using automated information entry.",
          "tree_numbers": [
            "N04.452.442.452.452.680",
            "N04.452.515.360.652",
            "N04.590.874"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019095",
      "preferred_label": "Point-of-Care Systems",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "\"Point-of-Care Systems\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"Plasmodium vivax\"[MeSH Terms] OR \"Plasmodium malariae\"[MeSH Terms] OR \"Plasmodium ovale\"[MeSH Terms] OR \"Plasmodium knowlesi\"[MeSH Terms] OR \"Malaria\"[Title/Abstract] OR \"malarial\"[Title/Abstract] OR \"plasmodium*\"[Title/Abstract] OR \"plasmodia\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"p knowlesi\"[Title/Abstract]) AND (\"reagent kits, diagnostic\"[MeSH Terms] OR \"Point-of-Care Systems\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract:~2] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract:~2] OR \"rapid tests\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"mRDT\"[Title/Abstract] OR \"MRDTs\"[Title/Abstract] OR \"ICT\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"immuno chromatograph*\"[Title/Abstract] OR \"dipstick*\"[Title/Abstract] OR \"antigen detection test\"[Title/Abstract:~2] OR \"rapid antigen test\"[Title/Abstract:~2] OR \"point of care\"[Title/Abstract:~2] OR \"OptiMAL\"[Title/Abstract] OR \"Paracheck\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "391fbe01b269e8accce6e6dfc4f4b056c44581b7c89066ce8179e58191bc6391",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The displayed PubMed translation preserves the intended MeSH, title/abstract, and proximity expressions. The named member species have bare text-word coverage, and the phrase searches show no translation errors."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required search concepts are combined with AND, with synonyms OR-ed within each block. The 1,908-record result is within the 10,000-record workload budget. All 14 known records are retrieved, though they are development records rather than independent validation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed malaria, species, diagnostic reagent kit, and point-of-care headings as verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy covers the named malaria species and common rapid-test wording, abbreviations, methods, and product names. The broad terms are constrained by the other required concept."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated with no reported errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The executed query adds an Entrez entry-date ceiling of 2013-06-09, although the question and listed limits specify no date restriction. This excludes later-entered records and needs explicit scope justification or removal."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed strategy silently limits records to Entrez entry dates through 2013-06-09. No such cutoff appears in the question, eligibility criteria, or strategy limits, so the reported 1,908 records do not represent the stated unrestricted question.",
          "recommendation": "Remove the entry-date ceiling unless the review is explicitly intended to end on 2013-06-09. Then rerun the complete evaluation, including translation, counts, known-record checks, category probes, and validation.",
          "status": "open"
        },
        {
          "id": "R1-F2",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "The 100% retrieval result is based on 14 records identified during the build and is not independent validation.",
          "recommendation": "Keep the result explicitly labeled as development-set retrieval; obtain a separate validation set if making a claim about independent validation.",
          "status": "accepted-risk",
          "response": "The packet already labels these records as development, not independent. The result should not be described as independent validation."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 1,
      "review_sha256": "df9b3299ef3a9dd474cd022c456ce0a1524654ead0d8d49691618b8b468f9209",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The displayed translation preserves the MeSH, title/abstract, and proximity expressions. The named malaria species have bare text-word coverage, and no translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required search blocks are ORed internally and combined with AND. The search returns 1,908 records, within the 10,000-record budget, and retrieves all 14 development records. These records are not independent validation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the malaria, species, diagnostic reagent kit, and point-of-care headings as verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include the named malaria species and a range of rapid-test terms, abbreviations, methods, and product names. The category probes found no relevant records outside the malaria-species block in the screened samples."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated with no reported errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date ceiling is explicitly listed as the harness-required as-of bound through 2013-06-09, with no publication-date limit. The executed query matches that documented bound."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The prior review flagged the Entrez entry-date ceiling as an undocumented restriction. The updated packet documents it as the explicit harness-required bound through 2013-06-09.",
          "recommendation": "Retain the bound for this as-of evaluation and keep its rationale documented.",
          "status": "resolved",
          "response": "The updated protocol limits and notes explicitly document the harness-required Entrez entry-date bound; the executed query applies that bound."
        },
        {
          "id": "R1-F2",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "Retrieval of 14 records identified during the build is development-set performance, not independent validation.",
          "recommendation": "Continue labeling the result as development-set retrieval; use a separate validation set before claiming independent validation.",
          "status": "accepted-risk",
          "response": "The packet labels the records as development records and states they are not independent validation."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 1,
      "review_sha256": "df9b3299ef3a9dd474cd022c456ce0a1524654ead0d8d49691618b8b468f9209",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The displayed translation preserves the MeSH, title/abstract, and proximity expressions. Named malaria species have bare text-word coverage, with no reported translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the two required search blocks, which are combined with AND. The 1,908-record result is within the workload budget; all 14 known records are development records, not independent validation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the malaria, species, diagnostic reagent kit, and point-of-care headings as verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks cover the named malaria species and a range of rapid-test wording, abbreviations, methods, and product names. Category probes found no relevant records outside the malaria-species block among those screened."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated with no reported errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date bound through 2013-06-09 is documented as the harness-required as-of limit, and the executed query matches it."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The earlier review flagged the Entrez entry-date ceiling as an undocumented restriction.",
          "recommendation": "Retain the bound for this as-of evaluation and keep its rationale documented.",
          "status": "resolved",
          "response": "The protocol limits and notes document the harness-required Entrez entry-date bound through 2013-06-09, and the executed query applies it."
        },
        {
          "id": "R1-F2",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "Retrieval of the 14 records identified during the build is development-set performance, not independent validation.",
          "recommendation": "Continue labeling the result as development-set retrieval; use a separate validation set before claiming independent validation.",
          "status": "accepted-risk",
          "response": "The packet labels these records as development records and states they are not independent validation."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


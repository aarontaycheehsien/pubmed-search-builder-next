# PubMed search strategy: audit

Generated 2026-09-30T13:55:51+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In people with suspected non-falciparum or Plasmodium vivax malaria in endemic countries, what is the diagnostic accuracy of rapid diagnostic tests?
- Framework: PIRD
- Scope confirmed by user: yes (User requested no clarification pause; scope and role assumptions are provisional. User reports no known relevant articles. Environment cutoff PSB_AS_OF=2013-06-09 is an Entrez-date bound; no publication-date limit is applied. No language, geography, or study-design limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum or Plasmodium vivax malaria | search | Target condition; the species and malaria terminology define the topic, but records may name only a species/member, so include member vocabulary and probe. |
| Malaria rapid diagnostic tests | search | Index test is central to the question and searchable; relevant reports may name only a test format or product, so probe. |
| People with suspected or confirmed uncomplicated malaria | screen | Suspicion, confirmation status, and uncomplicated severity are eligibility properties often absent from titles and abstracts. |
| Malaria-endemic countries/settings | screen | Endemicity may not be stated in bibliographic records and is judged from study location/context at screening. |
| Eligible reference standards and diagnostic performance | screen | Reference standard and accuracy outcomes are not reliably named; assess from full text. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:54:50+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 8,438
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Malaria"[Mesh]` | 50,641 | none |
| 2 | `"Malaria, Vivax"[Mesh]` | 2,872 | none |
| 3 | `"Plasmodium vivax"[Mesh]` | 3,745 | none |
| 4 | `malaria[tiab]` | 55,839 | none |
| 5 | `plasmodium[tiab]` | 34,635 | none |
| 6 | `vivax[tiab]` | 5,921 | none |
| 7 | `malariae[tiab]` | 888 | none |
| 8 | `ovale[tiab]` | 5,356 | none |
| 9 | `knowlesi[tiab]` | 866 | none |
| 10 | `non-falciparum[tiab]` | 55 | none |
| 11 | `nonfalciparum[tiab]` | 59 | none |
| 12 | `"non falciparum"[tiab]` | 55 | none |
| 13 | `"benign tertian"[tiab]` | 69 | none |
| 14 | `"quartan malaria"[tiab]` | 106 | none |
| 15 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14` | 79,536 | none |
| 16 | `"Reagent Strips"[Mesh]` | 2,830 | none |
| 17 | `"Diagnostic Tests, Routine"[Mesh]` | 7,136 | none |
| 18 | `"rapid diagnostic test"[tiab]` | 579 | none |
| 19 | `"rapid diagnostic tests"[tiab]` | 769 | none |
| 20 | `"rapid test"[tiab]` | 2,005 | none |
| 21 | `"rapid tests"[tiab]` | 891 | none |
| 22 | `RDT[tiab]` | 653 | none |
| 23 | `RDTs[tiab]` | 303 | none |
| 24 | `immunochromatograph*[tiab]` | 1,749 | none |
| 25 | `"lateral flow"[tiab]` | 720 | none |
| 26 | `dipstick*[tiab]` | 2,298 | none |
| 27 | `"antigen-detecting test"[tiab]` | 3 | none |
| 28 | `"antigen detection test"[tiab]` | 202 | none |
| 29 | `"malaria antigen test"[tiab]` | 3 | none |
| 30 | `"point-of-care test"[tiab]` | 271 | none |
| 31 | `"point of care test"[tiab]` | 271 | none |
| 32 | `HRP2[tiab]` | 168 | none |
| 33 | `pLDH[tiab]` | 158 | none |
| 34 | `"parasite lactate dehydrogenase"[tiab]` | 70 | none |
| 35 | `OptiMAL[tiab]` | 235,534 | none |
| 36 | `ParaSight[tiab]` | 81 | none |
| 37 | `BinaxNOW[tiab]` | 47 | none |
| 38 | `CareStart[tiab]` | 21 | none |
| 39 | `Paracheck[tiab]` | 53 | none |
| 40 | `"VIKIA malaria"[tiab]` | 2 | none |
| 41 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 | none |
| 42 | `"Immunoassay"[Mesh]` | 418,448 | none |
| 43 | `"Antigens, Protozoan"[Mesh]` | 12,579 | none |
| 44 | `"rapid diagnostic"[tiab]` | 2,352 | none |
| 45 | `"diagnostic test"[tiab]` | 10,497 | none |
| 46 | `"diagnostic tests"[tiab]` | 14,514 | none |
| 47 | `"First Response"[tiab]` | 902 | none |
| 48 | `ParaHIT[tiab]` | 9 | none |
| 49 | `"SD BIOLINE"[tiab]` | 59 | none |
| 50 | `#16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49` | 702,645 | none |
| 51 | `#15 AND #50` | 8,438 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR malaria[tiab] OR plasmodium[tiab] OR vivax[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab] OR non-falciparum[tiab] OR nonfalciparum[tiab] OR "non falciparum"[tiab] OR "benign tertian"[tiab] OR "quartan malaria"[tiab]) AND ("Reagent Strips"[Mesh] OR "Diagnostic Tests, Routine"[Mesh] OR "rapid diagnostic test"[tiab] OR "rapid diagnostic tests"[tiab] OR "rapid test"[tiab] OR "rapid tests"[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR "lateral flow"[tiab] OR dipstick*[tiab] OR "antigen-detecting test"[tiab] OR "antigen detection test"[tiab] OR "malaria antigen test"[tiab] OR "point-of-care test"[tiab] OR "point of care test"[tiab] OR HRP2[tiab] OR pLDH[tiab] OR "parasite lactate dehydrogenase"[tiab] OR OptiMAL[tiab] OR ParaSight[tiab] OR BinaxNOW[tiab] OR CareStart[tiab] OR Paracheck[tiab] OR "VIKIA malaria"[tiab] OR "Reagent Kits, Diagnostic"[Mesh] OR "Immunoassay"[Mesh] OR "Antigens, Protozoan"[Mesh] OR "rapid diagnostic"[tiab] OR "diagnostic test"[tiab] OR "diagnostic tests"[tiab] OR "First Response"[tiab] OR ParaHIT[tiab] OR "SD BIOLINE"[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum or Plasmodium vivax malaria | 1 | `(Plasmodium[Mesh] OR plasmodium[tiab] OR malaria[tiab] OR vivax[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab])` | 13 | 0/13 |
| Non-falciparum or Plasmodium vivax malaria | 2 | `(Plasmodium[Mesh] OR plasmodium[tiab] OR malaria[tiab] OR vivax[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab])` | 110 | 0/30 |
| Malaria rapid diagnostic tests | 1 | `(Malaria[Mesh] OR malaria[tiab] OR vivax[tiab] OR malariae[tiab] OR ovale[tiab]) AND (diagnostic test[tiab] OR test kit[tiab] OR assay*[tiab] OR blood test[tiab])` | 3,564 | 0/30 |
| Malaria rapid diagnostic tests | 2 | `(Malaria[Mesh] OR malaria[tiab] OR vivax[tiab] OR malariae[tiab] OR ovale[tiab]) AND (diagnostic test[tiab] OR test kit[tiab] OR assay*[tiab] OR blood test[tiab])` | 2,281 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 702,645 | 0 |
| rapid_test | 79,536 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first PIRD draft: malaria/species AND rapid-test blocks; eligibility context and accuracy screened. |
| 2 | 1,900 | malaria: +14 / -0; rapid_test: +25 / -0 | none | Initial recall-first PIRD draft: malaria/species AND rapid-test blocks; eligibility context and accuracy screened. |
| 3 | 8,438 | rapid_test: +9 / -0 | none | Added relevant Reagent Kits, Diagnostic, Immunoassay, and Antigens, Protozoan MeSH; mined rapid-diagnostic/test phrases and products First Response, ParaHIT, and SD BIOLINE from screened relevant records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (same-context critic: no independent fresh-review context was available; this is self-review, not PRESS peer review.): 1 findings; validation-independence document accepted-risk
- Round 2 on version 3 (same-context critic: final revision round self-review; no independent fresh-review context was available.): 1 findings; validation-independence document accepted-risk
- Round 3 on version 3 (same-context closing review: verifies prior dispositions only; no independent fresh-review context was available.): 1 findings; validation-independence document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 557 NCBI requests logged (231 from cache); strategy sha256 5d56f9f0cfb6._

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
      "checked_at": "2026-09-30T13:54:50+00:00",
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
      "checked_at": "2026-09-30T13:54:50+00:00",
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
      "checked_at": "2026-09-30T13:54:50+00:00",
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
      "requested": "Reagent Strips",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:54:50+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011934",
          "name": "Reagent Strips",
          "type": "descriptor",
          "scope_note": "Narrow pieces of material impregnated or covered with a substance used to produce a chemical reaction. The strips are used in detecting, measuring, producing, etc., other substances. (From Dorland, 28th ed)",
          "tree_numbers": [
            "D27.505.259.875.680",
            "D27.720.470.410.680.680",
            "E07.720.720"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011934",
      "preferred_label": "Reagent Strips",
      "type": "descriptor",
      "location": "vocabulary:15",
      "term": {
        "text": "\"Reagent Strips\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:54:50+00:00",
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
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:54:50+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "\"Reagent Kits, Diagnostic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Immunoassay",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:54:50+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007118",
          "name": "Immunoassay",
          "type": "descriptor",
          "scope_note": "A technique using antibodies for identifying or quantifying a substance. Usually the substance being studied serves as antigen both in antibody production and in measurement of antibody by the test substance.",
          "tree_numbers": [
            "E05.478.566",
            "E05.601.470"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007118",
      "preferred_label": "Immunoassay",
      "type": "descriptor",
      "location": "vocabulary:41",
      "term": {
        "text": "\"Immunoassay\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Antigens, Protozoan",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:54:50+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000953",
          "name": "Antigens, Protozoan",
          "type": "descriptor",
          "scope_note": "Any part or derivative of any protozoan that elicits immunity; malaria (Plasmodium) and trypanosome antigens are presently the most frequently encountered.",
          "tree_numbers": [
            "D12.776.820.125",
            "D23.050.293"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000953",
      "preferred_label": "Antigens, Protozoan",
      "type": "descriptor",
      "location": "vocabulary:42",
      "term": {
        "text": "\"Antigens, Protozoan\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"Plasmodium vivax\"[MeSH Terms] OR \"Malaria\"[Title/Abstract] OR \"plasmodium\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"benign tertian\"[Title/Abstract] OR \"quartan malaria\"[Title/Abstract]) AND (\"Reagent Strips\"[MeSH Terms] OR \"diagnostic tests, routine\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"dipstick*\"[Title/Abstract] OR \"antigen-detecting test\"[Title/Abstract] OR \"antigen detection test\"[Title/Abstract] OR \"malaria antigen test\"[Title/Abstract] OR \"point-of-care test\"[Title/Abstract] OR \"point-of-care test\"[Title/Abstract] OR \"HRP2\"[Title/Abstract] OR \"pLDH\"[Title/Abstract] OR \"parasite lactate dehydrogenase\"[Title/Abstract] OR \"OptiMAL\"[Title/Abstract] OR \"ParaSight\"[Title/Abstract] OR \"BinaxNOW\"[Title/Abstract] OR \"CareStart\"[Title/Abstract] OR \"Paracheck\"[Title/Abstract] OR \"VIKIA malaria\"[Title/Abstract] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"Immunoassay\"[MeSH Terms] OR \"antigens, protozoan\"[MeSH Terms] OR \"rapid diagnostic\"[Title/Abstract] OR \"diagnostic test\"[Title/Abstract] OR \"diagnostic tests\"[Title/Abstract] OR \"First Response\"[Title/Abstract] OR \"ParaHIT\"[Title/Abstract] OR \"SD BIOLINE\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "0cd888535d810e0c4e1e47cdbb2e0b571f567133763ec633d9e56813c61ec6da",
      "note": "same-context critic: no independent fresh-review context was available; this is self-review, not PRESS peer review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PIRD scope is represented by target malaria/species and index rapid-test blocks. Suspicion, uncomplicated status, endemicity, reference standard, and accuracy are screened because they are not consistently named in records. No extra optional block is required by the topic wording."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are OR-combined internally and AND-ed; no NOT, proximity, or limits are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Malaria and vivax headings are verified, exploded by default, and paired with text words. No dedicated rapid-test descriptor was found; broader diagnostic/reagent-kit, immunoassay, and protozoan-antigen headings supplement the text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text layer covers malaria species, non-falciparum spellings, RDT forms, test formats/antigens, and brands mined from screened records. Relevant terms are present as OR alternatives; broad brand/product terms are constrained by the malaria block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Evaluation reported no lint, translation, or vocabulary issues. All terms have explicit tags, quotes are plain ASCII, and truncations meet the minimum stem length."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, geography, design, or publication-date filter is applied. The Entrez-date cutoff is 2013-06-09 as requested."
        }
      },
      "findings": [
        {
          "id": "validation-independence",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "There are no user-supplied seeds or included-study benchmark. The five relevant records were discovered in pilot searching and used for development, so their full retrieval is not independent validation.",
          "recommendation": "Report that independent recall was not estimated and request PRESS review by an information specialist before use.",
          "status": "accepted-risk",
          "response": "Recorded as a limitation: only relative recall against five development records is available; the search is empirically unvalidated against an independent benchmark, and human PRESS peer review remains pending."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "0cd888535d810e0c4e1e47cdbb2e0b571f567133763ec633d9e56813c61ec6da",
      "note": "same-context critic: final revision round self-review; no independent fresh-review context was available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search blocks match the malaria/PIRD target and index test. Suspected status, uncomplicated severity, endemic setting and reference-standard/accuracy features remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Two OR synonym blocks are joined with AND; no unsupported operator or proximity construct is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified malaria/vivax and diagnostic-test-related headings are paired with title/abstract vocabulary. The broad test headings are recall supplements and are not used as required clauses."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Species variants, rapid-test formats, antigens, acronyms, and screened-record product names are represented. Current category probes found no relevant misses."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current evaluation reports no translation or syntax issues, no short truncation, and no phrase-index warning."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only the mandated Entrez-date bound is applied; no publication-date restriction or unsupported filter is used."
        }
      },
      "findings": [
        {
          "id": "validation-independence",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "There are no user-supplied seeds or included-study benchmark. The five relevant records were discovered in pilot searching and used for development, so their full retrieval is not independent validation.",
          "recommendation": "Report that independent recall was not estimated and request PRESS review by an information specialist before use.",
          "status": "accepted-risk",
          "response": "The audit and narrative retain this limitation: relative recall is measured only on development records; independent validation is unavailable, and human PRESS peer review remains pending."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "0cd888535d810e0c4e1e47cdbb2e0b571f567133763ec633d9e56813c61ec6da",
      "note": "same-context closing review: verifies prior dispositions only; no independent fresh-review context was available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required concept blocks remain aligned with the diagnostic accuracy scope; other eligibility properties are screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Boolean structure and absence of NOT/proximity remain appropriate."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified headings and text-word layers remain intact; no technical controlled-vocabulary issue was identified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Species, test format, acronym, antigen, and product-name vocabulary remains broad; both probes were screened with no eligible misses."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Evaluation remains free of blockers, translation warnings, and phrase-index issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The requested Entrez cutoff is used without a publication-date limit; the audit states the lack of independent validation and peer review."
        }
      },
      "findings": [
        {
          "id": "validation-independence",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "There are no user-supplied seeds or included-study benchmark. The five relevant records were discovered in pilot searching and used for development, so their full retrieval is not independent validation.",
          "recommendation": "Report that independent recall was not estimated and request PRESS review by an information specialist before use.",
          "status": "accepted-risk",
          "response": "Verified in the audit and narrative. Relative recall is only against the five-record development set; independent validation is unavailable, and human PRESS peer review remains pending."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


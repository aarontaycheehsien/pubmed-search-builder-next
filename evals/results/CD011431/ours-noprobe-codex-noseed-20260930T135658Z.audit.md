# PubMed search strategy: audit

Generated 2026-09-30T14:41:33+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (a diagnostic-test-accuracy review: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?)
- Framework: PIRD
- Scope confirmed by user: yes (User requested no questions during this run; scope roles were set from the question and eligibility criteria before reviewing any records. No known relevant articles were supplied. Harness date bound is PubMed Entrez date 2013-06-09 (PSB_AS_OF); no publication-date filter is used. No language, geography, age, or design limits. Endemic setting is tested as optional; uncomplicated status, suspected population, reference standard and accuracy are screened.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum or Plasmodium vivax malaria | search | Target diagnosis; malaria and its named species are searchable and required by the question. |
| Malaria rapid diagnostic tests | search | Index test; rapid tests are central to the question and usually described or indexed. |
| Malaria-endemic setting | optional | A required eligibility property, but country or endemicity may not be named consistently; test an explicit setting block before deciding. |
| People with suspected malaria | screen | Suspicion and uncomplicated severity may be reported inconsistently or only in full text. |
| Eligible reference standard | screen | Reference standard eligibility is evaluated during screening; studies may not name it in abstracts. |
| Diagnostic performance | screen | Accuracy outcomes are not required to be named in titles or abstracts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:40:42+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,742
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Malaria"[Mesh]` | 50,641 | none |
| 2 | `"Malaria, Vivax"[Mesh]` | 2,872 | none |
| 3 | `"Plasmodium vivax"[Mesh]` | 3,745 | none |
| 4 | `malaria*[tiab]` | 59,105 | none |
| 5 | `plasmodium[tiab]` | 34,635 | none |
| 6 | `vivax[tiab]` | 5,921 | none |
| 7 | `"non-falciparum"[tiab]` | 55 | none |
| 8 | `nonfalciparum[tiab]` | 59 | none |
| 9 | `"P. vivax"[tiab]` | 2,944 | none |
| 10 | `"P vivax"[tiab]` | 2,944 | none |
| 11 | `"P. malariae"[tiab]` | 571 | none |
| 12 | `"P. ovale"[tiab]` | 503 | none |
| 13 | `"P. knowlesi"[tiab]` | 425 | none |
| 14 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 76,237 | none |
| 15 | `"Point-of-Care Testing"[Mesh]` | 1 | none |
| 16 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 | none |
| 17 | `"Reagent Strips"[Mesh]` | 2,830 | none |
| 18 | `"rapid diagnostic test"[tiab]` | 579 | none |
| 19 | `"rapid diagnostic tests"[tiab]` | 769 | none |
| 20 | `"rapid test"[tiab]` | 2,005 | none |
| 21 | `"rapid tests"[tiab]` | 891 | none |
| 22 | `"rapid antigen test"[tiab]` | 134 | none |
| 23 | `"rapid antigen tests"[tiab]` | 72 | none |
| 24 | `"immunochromatographic test"[tiab]` | 369 | none |
| 25 | `"immunochromatographic tests"[tiab]` | 64 | none |
| 26 | `immunochromatograph*[tiab]` | 1,749 | none |
| 27 | `"immunochromatographic assay"[tiab]` | 336 | none |
| 28 | `"immunochromatographic assays"[tiab]` | 53 | none |
| 29 | `"lateral flow test"[tiab]` | 60 | none |
| 30 | `"lateral flow tests"[tiab]` | 22 | none |
| 31 | `"lateral flow assay"[tiab]` | 106 | none |
| 32 | `"lateral flow assays"[tiab]` | 39 | none |
| 33 | `dipstick*[tiab]` | 2,298 | none |
| 34 | `"card test"[tiab]` | 272 | none |
| 35 | `"card tests"[tiab]` | 42 | none |
| 36 | `"antigen detection test"[tiab]` | 202 | none |
| 37 | `"antigen detection tests"[tiab]` | 196 | none |
| 38 | `"bedside test"[tiab]` | 317 | none |
| 39 | `"bedside tests"[tiab]` | 196 | none |
| 40 | `ICT[tiab]` | 2,484 | none |
| 41 | `RDT[tiab]` | 653 | none |
| 42 | `RDTs[tiab]` | 303 | none |
| 43 | `(OptiMAL[tiab] AND (malaria[tiab] OR plasmodium[tiab] OR vivax[tiab]))` | 755 | none |
| 44 | `Binax[tiab]` | 154 | none |
| 45 | `"First Response"[tiab]` | 902 | none |
| 46 | `ParaScreen[tiab]` | 10 | none |
| 47 | `CareStart[tiab]` | 21 | none |
| 48 | `ParaSight[tiab]` | 81 | none |
| 49 | `#15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48` | 28,470 | none |
| 50 | `#14 AND #49` | 1,742 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR malaria*[tiab] OR plasmodium[tiab] OR vivax[tiab] OR "non-falciparum"[tiab] OR nonfalciparum[tiab] OR "P. vivax"[tiab] OR "P vivax"[tiab] OR "P. malariae"[tiab] OR "P. ovale"[tiab] OR "P. knowlesi"[tiab]) AND ("Point-of-Care Testing"[Mesh] OR "Reagent Kits, Diagnostic"[Mesh] OR "Reagent Strips"[Mesh] OR "rapid diagnostic test"[tiab] OR "rapid diagnostic tests"[tiab] OR "rapid test"[tiab] OR "rapid tests"[tiab] OR "rapid antigen test"[tiab] OR "rapid antigen tests"[tiab] OR "immunochromatographic test"[tiab] OR "immunochromatographic tests"[tiab] OR immunochromatograph*[tiab] OR "immunochromatographic assay"[tiab] OR "immunochromatographic assays"[tiab] OR "lateral flow test"[tiab] OR "lateral flow tests"[tiab] OR "lateral flow assay"[tiab] OR "lateral flow assays"[tiab] OR dipstick*[tiab] OR "card test"[tiab] OR "card tests"[tiab] OR "antigen detection test"[tiab] OR "antigen detection tests"[tiab] OR "bedside test"[tiab] OR "bedside tests"[tiab] OR ICT[tiab] OR RDT[tiab] OR RDTs[tiab] OR (OptiMAL[tiab] AND (malaria[tiab] OR plasmodium[tiab] OR vivax[tiab])) OR Binax[tiab] OR "First Response"[tiab] OR ParaScreen[tiab] OR CareStart[tiab] OR ParaSight[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 18 | 18 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Malaria-endemic setting | left out | 1,742 / 499 | 71.4% | 11904103, 12219143, 12792694, 15228812, 16259289, 17172395, 18620560, 18983278, 19860920, 20979601, 21087378, 21376357, 23785869 | 2/30 | Leave endemic setting out: the setting block reduces the current base count by 71.4%, but loses 13 of 18 screened-in development records, failing the no-loss rule. Two of 30 records in the current random loss sample (PMIDs 15228812 and 18983278) were screened eligible; these are already in the relevant set. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 28,470 | 0 |
| rdt | 76,237 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 906 | initial | none | Initial two-block PIRD strategy from question; target malaria and rapid diagnostic tests are searched, with endemic setting tested as an optional concept. No known articles were supplied. |
| 2 | 929 | rdt: +8 / -1 | none | Removed the future-introduced Rapid Diagnostic Tests MeSH heading after live verification showed year introduced 2023 and zero hits under the 2013-06-09 entry-date cutoff; retained Point-of-Care Testing MeSH and expanded text synonyms for test formats. |
| 3 | 1,770 | malaria: +1 / -0; rdt: +9 / -0 | none | Added species-specific Plasmodium vivax and diagnostic-kit MeSH headings, RDT text acronyms and common test brands mined from the screened relevant set; added PMID 11904103 from the endemic-setting loss sample as relevant. |
| 4 | 1,742 | rdt: +1 / -1 | none | Resolved critic R1-01 by replacing the broad OptiMAL[tiab] term (235,534 hits) with an explicit compound clause requiring malaria, Plasmodium or vivax in the same title/abstract; standalone and proximity alternatives were checked, with the latter translating to All Fields and rejected. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-01 should-fix open, R1-02 should-fix open
- Round 2 on version 4: 2 findings; R1-01 should-fix resolved, R1-02 should-fix rejected
- Round 3 on version 4: 2 findings; R1-01 should-fix resolved, R1-02 should-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 706 NCBI requests logged (360 from cache); strategy sha256 154f2f969218._

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
      "checked_at": "2026-09-30T14:40:42+00:00",
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
      "checked_at": "2026-09-30T14:40:42+00:00",
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
      "checked_at": "2026-09-30T14:40:42+00:00",
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
      "requested": "Point-of-Care Testing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:42+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000067716",
          "name": "Point-of-Care Testing",
          "type": "descriptor",
          "scope_note": "Allows patient diagnoses in the physician’s office, in other ambulatory setting or at bedside. The results of care are timely, and allow rapid treatment to the patient. (from NIH Fact Sheet Point-of-Care Diagnostic Testing, 2010.)",
          "tree_numbers": [
            "N04.590.874.500"
          ],
          "entry_terms": 26,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000067716",
      "preferred_label": "Point-of-Care Testing",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Point-of-Care Testing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:42+00:00",
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
      "requested": "Reagent Strips",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:40:42+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Reagent Strips\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"Plasmodium vivax\"[MeSH Terms] OR \"malaria*\"[Title/Abstract] OR \"plasmodium\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"P vivax\"[Title/Abstract] OR \"P vivax\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"p knowlesi\"[Title/Abstract]) AND (\"Point-of-Care Testing\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"Reagent Strips\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"rapid antigen test\"[Title/Abstract] OR \"rapid antigen tests\"[Title/Abstract] OR \"immunochromatographic test\"[Title/Abstract] OR \"immunochromatographic tests\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"immunochromatographic assay\"[Title/Abstract] OR \"immunochromatographic assays\"[Title/Abstract] OR \"lateral flow test\"[Title/Abstract] OR \"lateral flow tests\"[Title/Abstract] OR \"lateral flow assay\"[Title/Abstract] OR \"lateral flow assays\"[Title/Abstract] OR \"dipstick*\"[Title/Abstract] OR \"card test\"[Title/Abstract] OR \"card tests\"[Title/Abstract] OR \"antigen detection test\"[Title/Abstract] OR \"antigen detection tests\"[Title/Abstract] OR \"bedside test\"[Title/Abstract] OR \"bedside tests\"[Title/Abstract] OR \"ICT\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR (\"OptiMAL\"[Title/Abstract] AND (\"Malaria\"[Title/Abstract] OR \"plasmodium\"[Title/Abstract] OR \"vivax\"[Title/Abstract])) OR \"Binax\"[Title/Abstract] OR \"First Response\"[Title/Abstract] OR \"ParaScreen\"[Title/Abstract] OR \"CareStart\"[Title/Abstract] OR \"ParaSight\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "0f29e928c7884ca58b3d0276c3a5c8af237bdb9d2c168696b0e6c16d804083bb",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translations preserve the specified fields and terms; no translation issues or PubMed errors were reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The malaria and rapid-test blocks are OR-combined and then AND-combined, consistent with the searchable concepts. Screening-only criteria are not restrictive blocks."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet lists verified MeSH headings, supported by text-word terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "OptiMAL[tiab] has an anomalously high count; test specific expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or lint issues were reported."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Review whether the entry-date ceiling is the intended endpoint."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "rdt",
          "finding": "OptiMAL[tiab] retrieves 235,534 records, suggesting it retrieves ordinary uses of 'optimal' as well as the test brand.",
          "recommendation": "Test explicit brand-plus-test expressions, compare translations and counts, and keep broad form only if useful additional retrieval is shown.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The query has an Entrez entry-date ceiling of 2013-06-09 that is not stated in the review question.",
          "recommendation": "Confirm and document the intended search endpoint; update or remove if current review.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "645a8146bee9129e5a2f0f85daeb29134e1a3886bfde5b497e656690fda8fa7f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The revised query preserves the two searched concepts and screen-only eligibility criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks are correctly OR-combined and AND-combined; endemicity remains optional and is left out after measured losses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings are reported as verified and paired with title/abstract vocabulary."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The OptiMAL term is now restricted by related malaria words and has a reported count of 755; all 18 screened-in development records remain retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax, lint, translation or PubMed errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2013-06-09 Entrez entry-date ceiling is required by the user-provided harness conditions, is recorded in protocol.json, and is not a publication-date filter."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "rdt",
          "finding": "The earlier unqualified OptiMAL[tiab] term had an anomalously high reported count and could retrieve ordinary uses of optimal. The current query requires OptiMAL and a malaria-related title/abstract term.",
          "recommendation": "Retain the constrained expression and document its tested count; avoid reintroducing the unqualified term without evidence that it improves relevant retrieval.",
          "status": "resolved",
          "response": "Replaced OptiMAL[tiab] with (OptiMAL[tiab] AND (malaria[tiab] OR plasmodium[tiab] OR vivax[tiab])). The compound expression counted 755 and the current complete query still retrieves all 18 screened-in development records."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The Entrez entry-date ceiling remains 2013-06-09, while the review question itself does not state an endpoint.",
          "recommendation": "Document the intended search endpoint and remove or update the bound if the review requires a later endpoint.",
          "status": "rejected",
          "response": "The run instructions explicitly require working as if today were 2013-06-09 and pin PubMed to that date through PSB_AS_OF for every command. I recorded the Entrez date bound in protocol.json and used no publication-date limit, as instructed. Removing or changing the bound would violate the run constraints."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "645a8146bee9129e5a2f0f85daeb29134e1a3886bfde5b497e656690fda8fa7f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The translation preserves the two searched concepts, their fields, and the entry-date bound; no translation issues or PubMed errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The malaria and rapid-test blocks use OR internally and are AND-combined. The optional setting block was tested and left out after relevant-record losses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings are reported verified, with title/abstract terms supporting both searched concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The OptiMAL term is constrained by malaria-related title/abstract terms and counts 755; all 18 screened-in development records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax, lint, translation, or PubMed errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2013-06-09 Entrez date bound is documented as a harness requirement. No publication-date or other limit is used."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier unqualified OptiMAL[tiab] term had an anomalously high count and could retrieve ordinary uses of optimal.",
          "recommendation": "Keep the tested malaria-constrained expression; do not restore the unqualified term without evidence of useful additional retrieval.",
          "status": "resolved",
          "response": "The strategy replaces OptiMAL[tiab] with (OptiMAL[tiab] AND (malaria[tiab] OR plasmodium[tiab] OR vivax[tiab])). Its reported count is 755 and all 18 screened-in development records remain retrieved."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The Entrez entry-date ceiling is 2013-06-09, an endpoint not stated in the review question.",
          "recommendation": "Document the intended endpoint and remove or update the bound if the review requires a later endpoint.",
          "status": "rejected",
          "response": "The run conditions require the 2013-06-09 PubMed Entrez date bound through PSB_AS_OF. It is documented in the protocol, and no publication-date filter is used."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


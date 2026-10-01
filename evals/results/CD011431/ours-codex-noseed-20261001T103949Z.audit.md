# PubMed search strategy: audit

Generated 2026-10-01T11:20:00+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (a diagnostic-test-accuracy review: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?)
- Framework: PIRD
- Scope confirmed by user: yes (User requested proceeding without clarification; scope roles and screening assumptions are provisional. No known relevant articles were supplied. Run is pinned by PSB_AS_OF=2013/06/09 (Entrez date); no publication-date limit is used. Standard-depth discovery will be attempted, but no web search is permitted.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum malaria / Plasmodium vivax | search | Target diagnosis is essential; malaria and named species are searchable, and relevant records may name a species rather than non-falciparum malaria. |
| Malaria rapid diagnostic tests | search | Index test is essential and usually named; include assay-family and product-specific terminology because records may name a test type or product rather than the generic label. |
| Malaria-endemic setting | screen | Endemicity is inconsistently stated in abstracts and is better assessed from study location/context. |
| Uncomplicated disease | screen | Severity is inconsistently indexed and may be reported in full text. |
| Eligible reference standard | screen | Reference standard eligibility is judged from methods/full text, not reliably named in indexing. |
| Diagnostic performance | screen | Accuracy measures are inconsistently stated in titles and abstracts; do not require them in a recall-first strategy. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:19:18+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 6,046
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Malaria"[Mesh]` | 50,641 | none |
| 2 | `"Malaria, Vivax"[Mesh]` | 2,872 | none |
| 3 | `"Plasmodium vivax"[Mesh]` | 3,745 | none |
| 4 | `"Plasmodium"[Mesh]` | 36,161 | none |
| 5 | `malaria[tiab]` | 55,839 | none |
| 6 | `malaria*[tiab]` | 59,105 | none |
| 7 | `plasmodium[tiab]` | 34,635 | none |
| 8 | `vivax[tiab]` | 5,921 | none |
| 9 | `"P. vivax"[tiab]` | 2,944 | none |
| 10 | `"P vivax"[tiab]` | 2,944 | none |
| 11 | `non-falciparum[tiab]` | 55 | none |
| 12 | `non falciparum[tiab]` | 55 | none |
| 13 | `knowlesi[tiab]` | 866 | none |
| 14 | `malariae[tiab]` | 888 | none |
| 15 | `ovale[tiab]` | 5,356 | none |
| 16 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 82,103 | none |
| 17 | `"Diagnostic Tests, Routine"[Mesh]` | 7,136 | none |
| 18 | `"Immunologic Tests"[Mesh]` | 403,920 | none |
| 19 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 | none |
| 20 | `"Immunoassay"[Mesh]` | 418,448 | none |
| 21 | `"rapid diagnostic test"[tiab:~2]` | 757 | none |
| 22 | `"rapid test"[tiab:~2]` | 8,342 | none |
| 23 | `"rapid antigen test"[tiab:~2]` | 317 | none |
| 24 | `"immunochromatographic test"[tiab:~2]` | 562 | none |
| 25 | `"lateral flow test"[tiab:~2]` | 119 | none |
| 26 | `"lateral flow assay"[tiab:~2]` | 156 | none |
| 27 | `RDT[tiab]` | 653 | none |
| 28 | `RDTs[tiab]` | 303 | none |
| 29 | `CareStart[tiab]` | 21 | none |
| 30 | `OptiMAL[tiab]` | 235,534 | none |
| 31 | `ParaHIT[tiab]` | 9 | none |
| 32 | `OnSite[tiab]` | 7,425 | none |
| 33 | `BinaxNOW[tiab]` | 47 | none |
| 34 | `"SD Bioline"[tiab]` | 59 | none |
| 35 | `"First Response"[tiab]` | 902 | none |
| 36 | `ICT[tiab]` | 2,484 | none |
| 37 | `#17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36` | 1,042,430 | none |
| 38 | `#16 AND #37` | 6,046 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR "Plasmodium"[Mesh] OR malaria[tiab] OR malaria*[tiab] OR plasmodium[tiab] OR vivax[tiab] OR "P. vivax"[tiab] OR "P vivax"[tiab] OR non-falciparum[tiab] OR non falciparum[tiab] OR knowlesi[tiab] OR malariae[tiab] OR ovale[tiab]) AND ("Diagnostic Tests, Routine"[Mesh] OR "Immunologic Tests"[Mesh] OR "Reagent Kits, Diagnostic"[Mesh] OR "Immunoassay"[Mesh] OR "rapid diagnostic test"[tiab:~2] OR "rapid test"[tiab:~2] OR "rapid antigen test"[tiab:~2] OR "immunochromatographic test"[tiab:~2] OR "lateral flow test"[tiab:~2] OR "lateral flow assay"[tiab:~2] OR RDT[tiab] OR RDTs[tiab] OR CareStart[tiab] OR OptiMAL[tiab] OR ParaHIT[tiab] OR OnSite[tiab] OR BinaxNOW[tiab] OR "SD Bioline"[tiab] OR "First Response"[tiab] OR ICT[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 20 | 20 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum malaria / Plasmodium vivax | 1 | `Malaria[Mesh] OR Plasmodium[Mesh] OR Plasmodium[tiab] OR malaria*[tiab] OR vivax[tiab] OR knowlesi[tiab] OR malariae[tiab] OR ovale[tiab]` | 0 | 0/0 |
| Non-falciparum malaria / Plasmodium vivax | 2 | `Malaria[Mesh] OR Plasmodium[Mesh] OR Plasmodium[tiab] OR malaria*[tiab] OR vivax[tiab] OR knowlesi[tiab] OR malariae[tiab] OR ovale[tiab]` | 0 | 0/0 |
| Malaria rapid diagnostic tests | 1 | `(test*[tiab] OR assay*[tiab] OR device*[tiab] OR antigen*[tiab] OR immunoassay*[tiab])` | 15,870 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 1,042,430 | 0 |
| rdt | 82,103 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block PIRD strategy: malaria/non-falciparum target condition AND malaria rapid diagnostic tests; no limits. Added screened PubMed pilot DTA records to relevant set. |
| 2 | 6,046 | rdt: +2 / -0 | none | Added screened P. vivax/non-falciparum pilot records and their recurrent MeSH headings Reagent Kits, Diagnostic and Immunoassay in the RDT block; preserved MeSH and text-word layers. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (same-context critic: a fresh-context reviewer was unavailable in this run. I assessed the packet against the six PRESS domains and treated this as internal QA only.): 0 findings; 
- Round 2 on version 2 (same-context closing round: verified the prior round and current evidence binding. No fresh-context reviewer was available, so this is not independent PRESS review.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 554 NCBI requests logged (176 from cache); strategy sha256 ae90c1a6b995._

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
      "checked_at": "2026-10-01T11:19:18+00:00",
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
      "checked_at": "2026-10-01T11:19:18+00:00",
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
      "checked_at": "2026-10-01T11:19:18+00:00",
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
      "requested": "Plasmodium",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:19:18+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010961",
          "name": "Plasmodium",
          "type": "descriptor",
          "scope_note": "A genus of protozoa that comprise the malaria parasites of mammals. Four species infect humans (although occasional infections with primate malarias may occur). These are PLASMODIUM FALCIPARUM; PLASMODIUM MALARIAE; PLASMODIUM OVALE, and PLASMODIUM VIVAX. Species causing infection in vertebrates other than man include: PLASMODIUM BERGHEI; PLASMODIUM CHABAUDI; P. vinckei, and PLASMODIUM YOELII in...",
          "tree_numbers": [
            "B01.043.075.380.611"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010961",
      "preferred_label": "Plasmodium",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Plasmodium\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:19:18+00:00",
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
      "requested": "Immunologic Tests",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:19:18+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007159",
          "name": "Immunologic Tests",
          "type": "descriptor",
          "scope_note": "Immunologic techniques involved in diagnosis.",
          "tree_numbers": [
            "E01.370.225.812",
            "E05.200.812",
            "E05.478.594"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007159",
      "preferred_label": "Immunologic Tests",
      "type": "descriptor",
      "location": "vocabulary:17",
      "term": {
        "text": "\"Immunologic Tests\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:19:18+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Reagent Kits, Diagnostic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Immunoassay",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:19:18+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Immunoassay\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"Plasmodium vivax\"[MeSH Terms] OR \"Plasmodium\"[MeSH Terms] OR \"Malaria\"[Title/Abstract] OR \"malaria*\"[Title/Abstract] OR \"Plasmodium\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"P vivax\"[Title/Abstract] OR \"P vivax\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"ovale\"[Title/Abstract]) AND (\"diagnostic tests, routine\"[MeSH Terms] OR \"Immunologic Tests\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"Immunoassay\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract:~2] OR \"rapid test\"[Title/Abstract:~2] OR \"rapid antigen test\"[Title/Abstract:~2] OR \"immunochromatographic test\"[Title/Abstract:~2] OR \"lateral flow test\"[Title/Abstract:~2] OR \"lateral flow assay\"[Title/Abstract:~2] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"CareStart\"[Title/Abstract] OR \"OptiMAL\"[Title/Abstract] OR \"ParaHIT\"[Title/Abstract] OR \"OnSite\"[Title/Abstract] OR \"BinaxNOW\"[Title/Abstract] OR \"SD Bioline\"[Title/Abstract] OR \"First Response\"[Title/Abstract] OR \"ICT\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "9853523ba319bc539b2e31cec7622e107b9f0c0a16b36064dcdf2c35dcc7c779",
      "note": "same-context critic: a fresh-context reviewer was unavailable in this run. I assessed the packet against the six PRESS domains and treated this as internal QA only.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required PIRD concepts are condition and index test. Endemic setting, severity, reference standard, and accuracy measures are screened because the query does not reliably require those labels. The two category concepts were probed; the malaria block captures the broader malaria/species query, and the RDT loss sample found no eligible records."
        },
        "operators": {
          "verdict": "pass",
          "note": "Each block is OR-ed and the two essential concepts are AND-ed. No NOT operator, proximity joins, or study-design filters are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Malaria, Malaria, Vivax, Plasmodium vivax, and Plasmodium headings provide broad and species-specific indexing coverage. Diagnostic Tests, Routine, Immunologic Tests, Reagent Kits, Diagnostic, and Immunoassay are verified pre-cutoff headings observed or relevant to the RDT concept. The Rapid Diagnostic Tests and Point-of-Care Testing headings were excluded because their introduction years postdate the 2013 cutoff."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The condition block covers generic malaria, named Plasmodium, P. vivax and non-falciparum wording and the principal other human species. The test block includes rapid-test, antigen, immunochromatographic and lateral-flow wording, acronyms, and product names. Some product/acronym terms are broad in isolation, but the condition block constrains the final search and the final count remains within the 10,000-record screening budget."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly tagged. The live PubMed translations show the intended fields and proximity operators; lint and translation checks report no issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, geography, publication-date, age, or design filters were added. The only date bound is the harness-mandated Entrez entry-date cutoff of 2013-06-09; no publication-date limit is present."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "9853523ba319bc539b2e31cec7622e107b9f0c0a16b36064dcdf2c35dcc7c779",
      "note": "same-context closing round: verified the prior round and current evidence binding. No fresh-context reviewer was available, so this is not independent PRESS review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The closing review confirms the earlier scope assessment and the recorded screening roles; the setting and severity remain screening decisions with stated rationale."
        },
        "operators": {
          "verdict": "pass",
          "note": "The OR-within-block and AND-between-essential-block structure remains unchanged and correctly expressed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected MeSH headings remain appropriate and live-verified; post-cutoff Rapid Diagnostic Tests and Point-of-Care Testing headings are excluded."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word coverage remains broad across disease wording, species, assay families, acronyms, and products. Known-record retrieval remains complete for the development set."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint, translation, phrase, or other syntax issue is open in the current evaluation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only the mandated 2013-06-09 Entrez entry-date bound is applied; there is no publication-date filter."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


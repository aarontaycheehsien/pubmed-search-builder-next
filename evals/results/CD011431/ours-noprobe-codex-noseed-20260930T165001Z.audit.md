# PubMed search strategy: audit

Generated 2026-09-30T17:20:04+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In people with suspected non-falciparum or Plasmodium vivax malaria in endemic countries, what is the diagnostic accuracy of rapid diagnostic tests for uncomplicated malaria?
- Framework: PIRD
- Scope confirmed by user: no (User asked to proceed without questions. Scope is PIRD: malaria target condition and malaria rapid diagnostic test are searched; endemic setting is tested as optional; severity, suspected status, reference standard, and accuracy are screened. No seeds supplied. Use PSB_AS_OF=2013-06-09 as an Entrez-date bound only; do not apply a publication-date limit. No language or geography filter. Standard-depth PubMed-only candidate discovery will be attempted; any unscreened candidates remain outside known-record sets.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Uncomplicated non-falciparum or Plasmodium vivax malaria | search | Target condition; search malaria and its named vivax/non-falciparum members so records do not need to use the umbrella wording. |
| Malaria rapid diagnostic tests | search | Index test; a required named test technology in this diagnostic-accuracy question. |
| Malaria-endemic countries/settings | optional | Setting can be named in abstracts but is not reliably described as endemic; test as optional, then decide from retrieval evidence. |
| Suspected/confirmed uncomplicated malaria | screen | Suspected status and uncomplicated severity are often not named consistently in abstracts. |
| Eligible reference standard and diagnostic performance | screen | Reference standard and accuracy outcomes are inconsistently reported and should not be required search blocks. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T17:19:14+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 7,725
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Malaria, Vivax[Mesh]` | 2,872 | none |
| 3 | `Plasmodium vivax[Mesh]` | 3,745 | none |
| 4 | `Plasmodium malariae[Mesh]` | 810 | none |
| 5 | `Plasmodium ovale[Mesh]` | 131 | none |
| 6 | `Plasmodium knowlesi[Mesh]` | 280 | none |
| 7 | `malaria[tiab]` | 55,839 | none |
| 8 | `plasmodi*[tiab]` | 35,922 | none |
| 9 | `vivax[tiab]` | 5,921 | none |
| 10 | `malariae[tiab]` | 888 | none |
| 11 | `ovale[tiab]` | 5,356 | none |
| 12 | `knowlesi[tiab]` | 866 | none |
| 13 | `non-falciparum[tiab]` | 55 | none |
| 14 | `nonfalciparum[tiab]` | 59 | none |
| 15 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14` | 80,504 | none |
| 16 | `Antigens, Protozoan[Mesh]` | 12,579 | none |
| 17 | `Diagnostic Tests, Routine[Mesh]` | 7,136 | none |
| 18 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 19 | `Immunoassay[Mesh]` | 418,448 | none |
| 20 | `rapid diagnostic test*[tiab]` | 1,321 | none |
| 21 | `rapid test*[tiab]` | 3,281 | none |
| 22 | `malaria test*[tiab]` | 125 | none |
| 23 | `RDT[tiab]` | 653 | none |
| 24 | `RDTs[tiab]` | 303 | none |
| 25 | `immunochromatograph*[tiab]` | 1,749 | none |
| 26 | `lateral flow[tiab]` | 720 | none |
| 27 | `point-of-care test*[tiab]` | 1,572 | none |
| 28 | `point of care test*[tiab]` | 1,572 | none |
| 29 | `malaria antigen test*[tiab]` | 7 | none |
| 30 | `antigen detection[tiab]` | 3,135 | none |
| 31 | `ICT[tiab]` | 2,484 | none |
| 32 | `pLDH[tiab]` | 158 | none |
| 33 | `HRP2[tiab]` | 168 | none |
| 34 | `histidine-rich protein 2[tiab]` | 169 | none |
| 35 | `parasite lactate dehydrogenase[tiab]` | 70 | none |
| 36 | `#16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35` | 455,540 | none |
| 37 | `#15 AND #36` | 7,725 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Malaria, Vivax[Mesh] OR Plasmodium vivax[Mesh] OR Plasmodium malariae[Mesh] OR Plasmodium ovale[Mesh] OR Plasmodium knowlesi[Mesh] OR malaria[tiab] OR plasmodi*[tiab] OR vivax[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab] OR non-falciparum[tiab] OR nonfalciparum[tiab]) AND (Antigens, Protozoan[Mesh] OR Diagnostic Tests, Routine[Mesh] OR Reagent Kits, Diagnostic[Mesh] OR Immunoassay[Mesh] OR rapid diagnostic test*[tiab] OR rapid test*[tiab] OR malaria test*[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR lateral flow[tiab] OR point-of-care test*[tiab] OR point of care test*[tiab] OR malaria antigen test*[tiab] OR antigen detection[tiab] OR ICT[tiab] OR pLDH[tiab] OR HRP2[tiab] OR histidine-rich protein 2[tiab] OR parasite lactate dehydrogenase[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 16 | 16 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Malaria-endemic countries/settings | left out | 7,725 / 1,151 | 85.1% | 19860920, 20005196, 20046179, 20378137, 20602766, 20979601, 21696587, 22536317, 22818643 | 0/30 (up to 10% of removed records could be relevant) | The refreshed block reduces the base count 85.1% but still loses 9 of 16 screened-in relevant records, whose abstracts often name the country without describing it as endemic. In the refreshed 30-record loss sample, none met all criteria: relevant-looking records were falciparum-only, non-endemic, or did not report diagnostic accuracy. Retain setting as an eligibility screen to preserve recall. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 455,540 | 0 |
| rdt | 80,504 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 3,700 | initial | none | Initial two-block PIRD strategy. Built broad malaria target-condition wording plus vivax and named non-falciparum species terms; included malaria RDT test names, immunochromatography, antigen targets, and relevant MeSH; measured endemic setting as an optional block. Vocabulary informed by 16 screened focused-pilot records. |
| 2 | 7,725 | rdt: +1 / -0 | none | Added the indexed Antigens, Protozoan heading carried by relevant malaria RDT records; no known record was lost. This changes the base query, so the optional endemic-setting test will be refreshed. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 755 NCBI requests logged (353 from cache); strategy sha256 091ea136611d._

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
      "checked_at": "2026-09-30T17:19:14+00:00",
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
      "checked_at": "2026-09-30T17:19:14+00:00",
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
        "text": "Malaria, Vivax",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
        "text": "Plasmodium vivax",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium malariae",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
        "text": "Plasmodium malariae",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium ovale",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
        "text": "Plasmodium ovale",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium knowlesi",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
        "text": "Plasmodium knowlesi",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Antigens, Protozoan",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "Antigens, Protozoan",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
        "text": "Diagnostic Tests, Routine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "Reagent Kits, Diagnostic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Immunoassay",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:19:14+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "Immunoassay",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"plasmodium vivax\"[MeSH Terms] OR \"plasmodium malariae\"[MeSH Terms] OR \"plasmodium ovale\"[MeSH Terms] OR \"plasmodium knowlesi\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"plasmodi*\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract]) AND (\"antigens, protozoan\"[MeSH Terms] OR \"diagnostic tests, routine\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"immunoassay\"[MeSH Terms] OR \"rapid diagnostic test*\"[Title/Abstract] OR \"rapid test*\"[Title/Abstract] OR \"malaria test*\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"point of care test*\"[Title/Abstract] OR \"point of care test*\"[Title/Abstract] OR \"malaria antigen test*\"[Title/Abstract] OR \"antigen detection\"[Title/Abstract] OR \"ICT\"[Title/Abstract] OR \"pLDH\"[Title/Abstract] OR \"HRP2\"[Title/Abstract] OR \"histidine rich protein 2\"[Title/Abstract] OR \"parasite lactate dehydrogenase\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "d1b83f32a3cb713a51cc9d04ef3240a5d552918d860a6acb1c124b9554b32550",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The tested terms translate to the intended MeSH or title/abstract fields; no translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The malaria terms and RDT terms are ORed within their respective blocks, and the required blocks are ANDed. The optional endemic-setting block was tested and left out based on the reported recall losses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified. The malaria and named-species headings cover the searched condition; broader diagnostic headings are paired with the malaria block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy covers malaria and each named non-falciparum species with bare title/abstract terms, plus the stated non-falciparum variants. It includes multiple RDT expressions and test-marker terms. Suspected status, uncomplicated severity, reference standards, and accuracy outcomes are appropriately retained for screening."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The combined query is parenthesized, and the reported PubMed diagnostics contain no errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or geography filters are applied. The query uses the stated Entrez-date bound through 2013-06-09; the packet identifies this as an as-of bound, not a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-10-02T14:15:43+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (a diagnostic-test-accuracy review: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?)
- Framework: PIRD
- Scope confirmed by user: yes (User asked to proceed without questions. Scope roles are provisional and based on PIRD: malaria and rapid diagnostic test are searched; species, uncomplicated status, reference standard/accuracy, and endemic setting are screened. No known relevant articles were supplied. PubMed requests are bounded by PSB_AS_OF=2013-06-09 (Entrez date); no publication-date limit is applied. No web search used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Malaria | search | Target disease; malaria is reliably named and indexed. Search broadly, then screen species and uncomplicated status. |
| Malaria rapid diagnostic tests | search | Index test central to the question and commonly named in records. |
| Non-falciparum malaria or Plasmodium vivax | screen | Species subgroup may be reported only in full text or not indexed consistently; screen at eligibility. |
| Suspected or confirmed uncomplicated malaria | screen | Clinical presentation and severity are eligibility details with inconsistent abstract reporting. |
| Eligible reference standard and diagnostic performance | screen | Reference methods and accuracy metrics are not reliable retrieval concepts; assess at screening. |
| Malaria-endemic setting | screen | Setting may be implicit or absent from title and abstract; assess at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:15:01+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,102
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Plasmodium vivax[Mesh]` | 3,745 | none |
| 3 | `malaria[tiab]` | 55,839 | none |
| 4 | `plasmodi*[tiab]` | 35,922 | none |
| 5 | `paludism[tiab]` | 72 | none |
| 6 | `Plasmodium vivax[tiab]` | 3,467 | none |
| 7 | `Plasmodium falciparum[tiab]` | 21,715 | none |
| 8 | `Plasmodium malariae[tiab]` | 421 | none |
| 9 | `Plasmodium ovale[tiab]` | 274 | none |
| 10 | `Plasmodium knowlesi[tiab]` | 687 | none |
| 11 | `non-falciparum[tiab]` | 55 | none |
| 12 | `non falciparum[tiab]` | 55 | none |
| 13 | `P. vivax[tiab]` | 2,944 | none |
| 14 | `P. falciparum[tiab]` | 10,636 | none |
| 15 | `P. malariae[tiab]` | 571 | none |
| 16 | `P. ovale[tiab]` | 503 | none |
| 17 | `P. knowlesi[tiab]` | 425 | none |
| 18 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 75,297 | none |
| 19 | `Diagnostic Tests, Routine[Mesh]` | 7,136 | none |
| 20 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 21 | `rapid diagnostic test[tiab]` | 579 | none |
| 22 | `rapid diagnostic tests[tiab]` | 769 | none |
| 23 | `rapid test[tiab]` | 2,005 | none |
| 24 | `rapid tests[tiab]` | 891 | none |
| 25 | `RDT[tiab]` | 653 | none |
| 26 | `RDTs[tiab]` | 303 | none |
| 27 | `rapid antigen test[tiab]` | 134 | none |
| 28 | `rapid antigen tests[tiab]` | 72 | none |
| 29 | `rapid antigen detection test[tiab]` | 70 | none |
| 30 | `rapid antigen detection tests[tiab]` | 51 | none |
| 31 | `malaria rapid test[tiab]` | 9 | none |
| 32 | `malaria rapid tests[tiab]` | 4 | none |
| 33 | `dipstick[tiab]` | 2,112 | none |
| 34 | `immunochromatograph*[tiab]` | 1,749 | none |
| 35 | `immunochromatography[tiab]` | 490 | none |
| 36 | `lateral flow[tiab]` | 720 | none |
| 37 | `point-of-care[tiab]` | 6,137 | none |
| 38 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 36,336 | none |
| 39 | `#18 AND #38` | 1,102 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Plasmodium vivax[Mesh] OR malaria[tiab] OR plasmodi*[tiab] OR paludism[tiab] OR Plasmodium vivax[tiab] OR Plasmodium falciparum[tiab] OR Plasmodium malariae[tiab] OR Plasmodium ovale[tiab] OR Plasmodium knowlesi[tiab] OR non-falciparum[tiab] OR non falciparum[tiab] OR P. vivax[tiab] OR P. falciparum[tiab] OR P. malariae[tiab] OR P. ovale[tiab] OR P. knowlesi[tiab]) AND (Diagnostic Tests, Routine[Mesh] OR Reagent Kits, Diagnostic[Mesh] OR rapid diagnostic test[tiab] OR rapid diagnostic tests[tiab] OR rapid test[tiab] OR rapid tests[tiab] OR RDT[tiab] OR RDTs[tiab] OR rapid antigen test[tiab] OR rapid antigen tests[tiab] OR rapid antigen detection test[tiab] OR rapid antigen detection tests[tiab] OR malaria rapid test[tiab] OR malaria rapid tests[tiab] OR dipstick[tiab] OR immunochromatograph*[tiab] OR immunochromatography[tiab] OR lateral flow[tiab] OR point-of-care[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 36,336 | 0 |
| rapid_test | 75,297 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 6,108 | initial | none | Initial PIRD strategy: AND malaria and rapid-test concepts; screened species, uncomplicated status, reference standard/performance and setting. Terms include MeSH/text layers; newer 2023 Rapid Diagnostic Tests heading excluded because of the 2013 cutoff. |
| 2 | 1,101 | rapid_test: +0 / -1 | none | Removed Antigens, Protozoan[Mesh] from the rapid-test block after its 5,233-record malaria intersection showed broad antigen/vaccine noise; retained Diagnostic Tests, Routine and Reagent Kits, Diagnostic plus all text terms. Known in-scope record remains covered. |
| 3 | 1,102 | malaria: +7 / -0 | none | Added abbreviated species names and non-falciparum wording after the PRESS-structured internal critic identified lexical coverage gaps; checked translation and known-record retrieval. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (same-context critic; no fresh-context reviewer was available in this host.): 1 findings; species_text_variants should-fix open
- Round 2 on version 3 (same-context critic; no fresh-context reviewer was available in this host.): 1 findings; species_text_variants should-fix resolved
- Round 3 on version 3 (same-context critic; no fresh-context reviewer was available in this host.): 1 findings; species_text_variants should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 414 NCBI requests logged (154 from cache); strategy sha256 dfd16f3fac5e._

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
      "checked_at": "2026-10-02T14:15:01+00:00",
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
      "requested": "Plasmodium vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:15:01+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Plasmodium vivax",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:15:01+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "Diagnostic Tests, Routine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:15:01+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "Reagent Kits, Diagnostic",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"plasmodium vivax\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"plasmodi*\"[Title/Abstract] OR \"paludism\"[Title/Abstract] OR \"plasmodium vivax\"[Title/Abstract] OR \"plasmodium falciparum\"[Title/Abstract] OR \"plasmodium malariae\"[Title/Abstract] OR \"plasmodium ovale\"[Title/Abstract] OR \"plasmodium knowlesi\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"p falciparum\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"p knowlesi\"[Title/Abstract]) AND (\"diagnostic tests, routine\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"rapid antigen test\"[Title/Abstract] OR \"rapid antigen tests\"[Title/Abstract] OR \"rapid antigen detection test\"[Title/Abstract] OR \"rapid antigen detection tests\"[Title/Abstract] OR \"malaria rapid test\"[Title/Abstract] OR \"malaria rapid tests\"[Title/Abstract] OR \"dipstick\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"immunochromatography\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"point-of-care\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "d69284f452433ef867004d13ab5f54dea9a89ca373f4a52f68f5c82a4e164e03",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PIRD scope is represented by malaria and rapid-test AND blocks; species, uncomplicated status, accuracy/reference method and endemic setting remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Two concept blocks are OR-ed internally and AND-ed; no unvalidated study-design, accuracy, or setting block is required."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Malaria is exploded and paired with Plasmodium vivax; Diagnostic Tests, Routine and Reagent Kits, Diagnostic are older verified headings. The dedicated Rapid Diagnostic Tests heading was introduced after the requested cutoff and is excluded."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The disease block has full binomials and general stems but would benefit from common abbreviated species forms and the phrase non-falciparum, especially because the review targets species subgroups."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly field-tagged; wildcard length is safe; PubMed translations show no warnings or errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility filter or publication-date limit is used. The effective Entrez date bound is the harness cutoff 2013-06-09."
        }
      },
      "findings": [
        {
          "id": "species_text_variants",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "malaria",
          "finding": "The malaria block does not explicitly include abbreviated forms such as P. vivax/P. malariae/P. ovale/P. knowlesi or non-falciparum wording that may occur in titles and abstracts.",
          "recommendation": "Add common abbreviated and non-falciparum variants to the malaria [tiab] block, then evaluate their translation and known-record coverage.",
          "status": "open"
        }
      ],
      "issue_dispositions": [],
      "note": "same-context critic; no fresh-context reviewer was available in this host."
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "232cbefbddd7e4faae7ca33a8724d7f77d507fd5c6f8195340e19fc810e68882",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Malaria and rapid diagnostic test are the two core searchable concepts. Species and uncomplicated status, accuracy/reference standard, and endemicity remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The query uses OR within concept blocks and AND between the two required concepts; no study-design or performance block narrows retrieval."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The Malaria heading is exploded; Plasmodium vivax supplements organism indexing. Diagnostic Tests, Routine and Reagent Kits, Diagnostic are verified historical headings. Newer Rapid Diagnostic Tests and Point-of-Care Testing headings are excluded for the 2013 cutoff."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Full species names, abbreviated species names, non-falciparum variants, common RDT terms, and antigen/lateral-flow/immunochromatographic wording are included. No phrase or translation warnings remain."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Terms are tagged; PubMed translations have no errors or unresolved warnings; wildcard stems meet the length rule."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit, language, geography, or design filter is used. The query carries only the PSB_AS_OF Entrez-entry cutoff."
        }
      },
      "findings": [
        {
          "id": "species_text_variants",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "malaria",
          "finding": "The malaria block does not explicitly include abbreviated forms such as P. vivax/P. malariae/P. ovale/P. knowlesi or non-falciparum wording that may occur in titles and abstracts.",
          "recommendation": "Add common abbreviated and non-falciparum variants to the malaria [tiab] block, then evaluate their translation and known-record coverage.",
          "status": "resolved",
          "response": "Added non-falciparum, non falciparum, and abbreviated P. species terms to the malaria block. PubMed translated each term without warnings or errors; the development record remained retrieved, and the final count changed from 1,101 to 1,102."
        }
      ],
      "issue_dispositions": [],
      "note": "same-context critic; no fresh-context reviewer was available in this host."
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "232cbefbddd7e4faae7ca33a8724d7f77d507fd5c6f8195340e19fc810e68882",
      "note": "same-context critic; no fresh-context reviewer was available in this host.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required PIRD concepts are searched; eligibility details are screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR alternatives are correctly grouped within the malaria and rapid-test blocks, and the blocks are AND-combined."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected headings are verified and available for the historical query; headings introduced after 2013 are omitted."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Full and abbreviated species terms, non-falciparum wording, and rapid-test variants are present; the closing review confirms the prior lexical change."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete evaluation reports no syntax, translation, or unresolved validation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No ad hoc filters or publication-date limits are present; only the required Entrez cutoff applies."
        }
      },
      "findings": [
        {
          "id": "species_text_variants",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "malaria",
          "finding": "The malaria block does not explicitly include abbreviated forms such as P. vivax/P. malariae/P. ovale/P. knowlesi or non-falciparum wording that may occur in titles and abstracts.",
          "recommendation": "Add common abbreviated and non-falciparum variants to the malaria [tiab] block, then evaluate their translation and known-record coverage.",
          "status": "resolved",
          "response": "The block now contains non-falciparum and abbreviated species terms. Evaluation confirmed the included record remains retrieved; all terms translated without warnings and there are no technical blockers."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


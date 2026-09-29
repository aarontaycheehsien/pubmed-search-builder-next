# PubMed search strategy: audit

Generated 2026-09-28T22:09:02+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Molecular assays for the diagnosis of sepsis in neonates
- Framework: PIRD
- Scope confirmed by user: no (User asked to proceed without questions. Scope is provisionally set from the eligibility criteria: PIRD with neonatal population, sepsis/bloodstream infection, and molecular assay as search blocks; reference-standard eligibility and diagnostic performance are screened. Since the protocol did not define an acceptable reference standard, screening provisionally treats microbial culture and clinical/composite diagnosis as eligible comparators; verify this with the review team. Neonates are interpreted as infants during the first 28 days; mixed pediatric studies count only when neonatal-specific performance can be judged. No language or publication-date restriction. Entrez date is bounded at 2014-08-09 via PSB_AS_OF; no [dp] cutoff. No known records were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Neonates or newborn infants | search | Required population; neonatal age labels and named neonatal subgroups are searchable, but some relevant records may name an age-group member such as preterm or premature infants. |
| Neonatal sepsis or bloodstream infection | search | Target diagnosis/context is central; include sepsis, septicemia, bacteremia and bloodstream infection terminology as members. |
| Molecular or nucleic-acid amplification assay | search | Index test defines the review; individual methods such as PCR and other nucleic-acid amplification techniques are searchable members. |
| Eligible reference standard | screen | Eligibility property often described in full text and heterogeneous across studies. |
| Diagnostic performance | screen | Accuracy outcomes are inconsistently named in titles and abstracts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:07:55+00:00
- Records added to PubMed up to: 2014-08-09
- Total records: 1,469
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Infant, Newborn"[Mesh]` | 516,613 | none |
| 2 | `neonat*[tiab]` | 200,319 | none |
| 3 | `newborn*[tiab]` | 144,652 | none |
| 4 | `infant*[tiab]` | 356,084 | none |
| 5 | `preterm*[tiab]` | 49,276 | none |
| 6 | `premature*[tiab]` | 99,036 | none |
| 7 | `"low birth weight"[tiab]` | 19,882 | none |
| 8 | `"very low birth weight"[tiab]` | 5,507 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 892,857 | none |
| 10 | `"Sepsis"[Mesh]` | 96,896 | none |
| 11 | `"Bacteremia"[Mesh]` | 22,734 | none |
| 12 | `sepsis[tiab]` | 65,928 | none |
| 13 | `septic*[tiab]` | 57,072 | none |
| 14 | `bacterem*[tiab]` | 19,298 | none |
| 15 | `bacteraem*[tiab]` | 4,846 | none |
| 16 | `pyem*[tiab]` | 135 | none |
| 17 | `"bloodstream infection"[tiab]` | 2,506 | none |
| 18 | `"blood stream infection"[tiab]` | 344 | none |
| 19 | `"blood poisoning"[tiab]` | 30 | none |
| 20 | `septicemia[tiab]` | 12,411 | none |
| 21 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 170,610 | none |
| 22 | `"Molecular Diagnostic Techniques"[Mesh]` | 10,539 | none |
| 23 | `"Nucleic Acid Amplification Techniques"[Mesh]` | 384,192 | none |
| 24 | `"Polymerase Chain Reaction"[Mesh]` | 379,038 | none |
| 25 | `"Real-Time Polymerase Chain Reaction"[Mesh]` | 26,943 | none |
| 26 | `"Multiplex Polymerase Chain Reaction"[Mesh]` | 1,931 | none |
| 27 | `"Reverse Transcriptase Polymerase Chain Reaction"[Mesh]` | 137,364 | none |
| 28 | `"In Situ Hybridization"[Mesh]` | 83,580 | none |
| 29 | `"Oligonucleotide Array Sequence Analysis"[Mesh]` | 70,727 | none |
| 30 | `molecular[tiab]` | 918,436 | none |
| 31 | `PCR[tiab]` | 345,331 | none |
| 32 | `qPCR[tiab]` | 12,523 | none |
| 33 | `"polymerase chain reaction"[tiab]` | 173,771 | none |
| 34 | `"real-time PCR"[tiab]` | 41,289 | none |
| 35 | `"real time PCR"[tiab]` | 41,289 | none |
| 36 | `"reverse transcriptase PCR"[tiab]` | 4,770 | none |
| 37 | `"reverse transcription PCR"[tiab]` | 10,816 | none |
| 38 | `"nucleic acid amplification"[tiab]` | 2,113 | none |
| 39 | `"nucleic acid test"[tiab]` | 118 | none |
| 40 | `"nucleic acid assay"[tiab]` | 29 | none |
| 41 | `microarray[tiab]` | 59,464 | none |
| 42 | `hybridization[tiab]` | 151,455 | none |
| 43 | `hybridisation[tiab]` | 8,941 | none |
| 44 | `sequencing[tiab]` | 141,259 | none |
| 45 | `"in situ hybridization"[tiab]` | 78,523 | none |
| 46 | `"in situ hybridisation"[tiab]` | 4,891 | none |
| 47 | `FISH[tiab]` | 115,046 | none |
| 48 | `DNA[tiab]` | 791,040 | none |
| 49 | `amplif*[tiab]` | 185,114 | none |
| 50 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49` | 2,300,536 | none |
| 51 | `#9 AND #21 AND #50` | 1,469 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Infant, Newborn"[Mesh] OR neonat*[tiab] OR newborn*[tiab] OR infant*[tiab] OR preterm*[tiab] OR premature*[tiab] OR "low birth weight"[tiab] OR "very low birth weight"[tiab]) AND ("Sepsis"[Mesh] OR "Bacteremia"[Mesh] OR sepsis[tiab] OR septic*[tiab] OR bacterem*[tiab] OR bacteraem*[tiab] OR pyem*[tiab] OR "bloodstream infection"[tiab] OR "blood stream infection"[tiab] OR "blood poisoning"[tiab] OR septicemia[tiab]) AND ("Molecular Diagnostic Techniques"[Mesh] OR "Nucleic Acid Amplification Techniques"[Mesh] OR "Polymerase Chain Reaction"[Mesh] OR "Real-Time Polymerase Chain Reaction"[Mesh] OR "Multiplex Polymerase Chain Reaction"[Mesh] OR "Reverse Transcriptase Polymerase Chain Reaction"[Mesh] OR "In Situ Hybridization"[Mesh] OR "Oligonucleotide Array Sequence Analysis"[Mesh] OR molecular[tiab] OR PCR[tiab] OR qPCR[tiab] OR "polymerase chain reaction"[tiab] OR "real-time PCR"[tiab] OR "real time PCR"[tiab] OR "reverse transcriptase PCR"[tiab] OR "reverse transcription PCR"[tiab] OR "nucleic acid amplification"[tiab] OR "nucleic acid test"[tiab] OR "nucleic acid assay"[tiab] OR microarray[tiab] OR hybridization[tiab] OR hybridisation[tiab] OR sequencing[tiab] OR "in situ hybridization"[tiab] OR "in situ hybridisation"[tiab] OR FISH[tiab] OR DNA[tiab] OR amplif*[tiab])) AND ("1800/01/01"[edat] : "2014/08/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 11 | 11 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Neonates or newborn infants | 1 | `Infant[Mesh:noexp] OR baby[tiab] OR babies[tiab]` | 406 | 0/30 |
| Neonates or newborn infants | 2 | `Infant[Mesh:noexp] OR baby[tiab] OR babies[tiab]` | 445 | 0/30 |
| Neonatal sepsis or bloodstream infection | 1 | `Bacterial Infections[Mesh] OR infection*[tiab] OR bloodstream[tiab] OR bacteri*[tiab]` | 9,810 | 0/30 |
| Neonatal sepsis or bloodstream infection | 2 | `Bacterial Infections[Mesh] OR infection*[tiab] OR bloodstream[tiab] OR bacteri*[tiab]` | 11,473 | 0/30 |
| Molecular or nucleic-acid amplification assay | 1 | `Molecular Biology[Mesh] OR DNA[tiab] OR RNA[tiab] OR gene*[tiab] OR genetic*[tiab] OR nucleic acid*[tiab]` | 1,980 | 0/30 |
| Molecular or nucleic-acid amplification assay | 2 | `Molecular Biology[Mesh] OR DNA[tiab] OR RNA[tiab] OR gene*[tiab] OR genetic*[tiab] OR nucleic acid*[tiab]` | 1,811 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| neonates | 15,097 | 0 |
| sepsis | 61,462 | 0 |
| molecular_assay | 20,715 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,284 | initial | none | Initial PIRD strategy from question and eligibility criteria; added MeSH plus broad title/abstract synonyms for neonatal population, sepsis/bloodstream infection, and molecular assays. Relevant set was drawn from screened title-focused PubMed pilots and split 30% for semi-independent validation; no user-supplied seed set. |
| 2 | 1,469 | molecular_assay: +2 / -0 | none | Added development-record terms DNA[tiab] (present in 5/8 relevant development records) and amplif*[tiab] to widen the molecular-assay block for records describing nucleic-acid amplification without naming PCR. Category probes found no relevant record outside any current concept block; none of the held-out records was used for term mining. |
| 3 | 1,469 | sepsis: +1 / -0 | none | Resolved internal critic finding R2-F1 by adding septicemia[tiab] as an explicit bare term to the sepsis block. This term is logically covered by septic*[tiab]; the edit makes the named member explicit. Rechecked relative recall, category probes, line counts, and PubMed translation. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 2: 1 findings; R2-F1 must-fix open
- Round 3 on version 3: 1 findings; R2-F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 949 NCBI requests logged (514 from cache); strategy sha256 54324df6fa4d._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:neonates",
        "blocking": false,
        "requires_review": true,
        "id": "I-0e688af5f547a13d12ec"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:neonates",
        "blocking": false,
        "requires_review": true,
        "id": "I-0e688af5f547a13d12ec"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Infant, Newborn",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007231",
          "name": "Infant, Newborn",
          "type": "descriptor",
          "scope_note": "An infant during the first 28 days after birth.",
          "tree_numbers": [
            "M01.060.703.520"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007231",
      "preferred_label": "Infant, Newborn",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Infant, Newborn\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sepsis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D018805",
          "name": "Sepsis",
          "type": "descriptor",
          "scope_note": "Systemic inflammatory response syndrome with a proven or suspected infectious etiology. When sepsis is associated with organ dysfunction distant from the site of infection, it is called severe sepsis. When sepsis is accompanied by HYPOTENSION despite adequate fluid infusion, it is called SEPTIC SHOCK.",
          "tree_numbers": [
            "C01.757",
            "C23.550.470.790.500"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D018805",
      "preferred_label": "Sepsis",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "\"Sepsis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bacteremia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016470",
          "name": "Bacteremia",
          "type": "descriptor",
          "scope_note": "The presence of viable bacteria circulating in the blood. Fever, chills, tachycardia, and tachypnea are common acute manifestations of bacteremia. The majority of cases are seen in already hospitalized patients, most of whom have underlying diseases or procedures which render their bloodstreams susceptible to invasion.",
          "tree_numbers": [
            "C01.150.252.100",
            "C01.757.100",
            "C23.550.470.790.500.100"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016470",
      "preferred_label": "Bacteremia",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Bacteremia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Molecular Diagnostic Techniques",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D025202",
          "name": "Molecular Diagnostic Techniques",
          "type": "descriptor",
          "scope_note": "MOLECULAR BIOLOGY techniques used in the diagnosis of disease.",
          "tree_numbers": [
            "E01.370.225.880",
            "E05.200.880",
            "E05.393.520"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D025202",
      "preferred_label": "Molecular Diagnostic Techniques",
      "type": "descriptor",
      "location": "vocabulary:20",
      "term": {
        "text": "\"Molecular Diagnostic Techniques\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Nucleic Acid Amplification Techniques",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D021141",
          "name": "Nucleic Acid Amplification Techniques",
          "type": "descriptor",
          "scope_note": "Laboratory techniques that involve the in-vitro synthesis of many copies of DNA or RNA from one original template.",
          "tree_numbers": [
            "E05.393.620"
          ],
          "entry_terms": 33,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D021141",
      "preferred_label": "Nucleic Acid Amplification Techniques",
      "type": "descriptor",
      "location": "vocabulary:21",
      "term": {
        "text": "\"Nucleic Acid Amplification Techniques\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016133",
          "name": "Polymerase Chain Reaction",
          "type": "descriptor",
          "scope_note": "In vitro method for producing large amounts of specific DNA or RNA fragments of defined length and sequence from small amounts of short oligonucleotide flanking sequences (primers). The essential steps include thermal denaturation of the double-stranded target molecules, annealing of the primers to their complementary sequences, and extension of the annealed primers by enzymatic synthesis with ...",
          "tree_numbers": [
            "E05.393.620.500"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016133",
      "preferred_label": "Polymerase Chain Reaction",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "\"Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Real-Time Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D060888",
          "name": "Real-Time Polymerase Chain Reaction",
          "type": "descriptor",
          "scope_note": "Methods used for detecting the amplified DNA products from the polymerase chain reaction as they accumulate instead of at the end of the reaction.",
          "tree_numbers": [
            "E05.393.620.500.706"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D060888",
      "preferred_label": "Real-Time Polymerase Chain Reaction",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "\"Real-Time Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multiplex Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D060885",
          "name": "Multiplex Polymerase Chain Reaction",
          "type": "descriptor",
          "scope_note": "Methods for using more than one primer set in a polymerase chain reaction to amplify more than one segment of the target DNA sequence in a single reaction.",
          "tree_numbers": [
            "E05.393.620.500.487"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D060885",
      "preferred_label": "Multiplex Polymerase Chain Reaction",
      "type": "descriptor",
      "location": "vocabulary:24",
      "term": {
        "text": "\"Multiplex Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reverse Transcriptase Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D020133",
          "name": "Reverse Transcriptase Polymerase Chain Reaction",
          "type": "descriptor",
          "scope_note": "A variation of the PCR technique in which cDNA is made from RNA via reverse transcription. The resultant cDNA is then amplified using standard PCR protocols.",
          "tree_numbers": [
            "E05.393.620.500.725"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D020133",
      "preferred_label": "Reverse Transcriptase Polymerase Chain Reaction",
      "type": "descriptor",
      "location": "vocabulary:25",
      "term": {
        "text": "\"Reverse Transcriptase Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "In Situ Hybridization",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017403",
          "name": "In Situ Hybridization",
          "type": "descriptor",
          "scope_note": "A technique that localizes specific nucleic acid sequences within intact chromosomes, eukaryotic cells, or bacterial cells through the use of specific nucleic acid-labeled probes.",
          "tree_numbers": [
            "E01.370.225.500.620.670.325",
            "E01.370.225.750.600.670.325",
            "E05.200.500.620.670.325",
            "E05.200.750.600.670.325",
            "E05.393.332.438.001",
            "E05.393.661.475"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017403",
      "preferred_label": "In Situ Hybridization",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "\"In Situ Hybridization\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Oligonucleotide Array Sequence Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:07:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D020411",
          "name": "Oligonucleotide Array Sequence Analysis",
          "type": "descriptor",
          "scope_note": "Hybridization of a nucleic acid sample to a very large set of OLIGONUCLEOTIDE PROBES, which have been attached individually in columns and rows to a solid support, to determine a BASE SEQUENCE, or to detect variations in a gene sequence, GENE EXPRESSION, or for GENE MAPPING.",
          "tree_numbers": [
            "E05.393.661.640",
            "E05.393.760.640",
            "E05.588.570.660",
            "E05.601.640"
          ],
          "entry_terms": 39,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D020411",
      "preferred_label": "Oligonucleotide Array Sequence Analysis",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "\"Oligonucleotide Array Sequence Analysis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"infant, newborn\"[MeSH Terms] OR \"neonat*\"[Title/Abstract] OR \"newborn*\"[Title/Abstract] OR \"infant*\"[Title/Abstract] OR \"preterm*\"[Title/Abstract] OR \"premature*\"[Title/Abstract] OR \"low birth weight\"[Title/Abstract] OR \"very low birth weight\"[Title/Abstract]) AND (\"Sepsis\"[MeSH Terms] OR \"Bacteremia\"[MeSH Terms] OR \"Sepsis\"[Title/Abstract] OR \"septic*\"[Title/Abstract] OR \"bacterem*\"[Title/Abstract] OR \"bacteraem*\"[Title/Abstract] OR \"pyem*\"[Title/Abstract] OR \"bloodstream infection\"[Title/Abstract] OR \"blood stream infection\"[Title/Abstract] OR \"blood poisoning\"[Title/Abstract] OR \"septicemia\"[Title/Abstract]) AND (\"Molecular Diagnostic Techniques\"[MeSH Terms] OR \"Nucleic Acid Amplification Techniques\"[MeSH Terms] OR \"Polymerase Chain Reaction\"[MeSH Terms] OR \"Real-Time Polymerase Chain Reaction\"[MeSH Terms] OR \"Multiplex Polymerase Chain Reaction\"[MeSH Terms] OR \"Reverse Transcriptase Polymerase Chain Reaction\"[MeSH Terms] OR \"In Situ Hybridization\"[MeSH Terms] OR \"Oligonucleotide Array Sequence Analysis\"[MeSH Terms] OR \"molecular\"[Title/Abstract] OR \"PCR\"[Title/Abstract] OR \"qPCR\"[Title/Abstract] OR \"Polymerase Chain Reaction\"[Title/Abstract] OR \"real time pcr\"[Title/Abstract] OR \"real time pcr\"[Title/Abstract] OR \"reverse transcriptase PCR\"[Title/Abstract] OR \"reverse transcription PCR\"[Title/Abstract] OR \"nucleic acid amplification\"[Title/Abstract] OR \"nucleic acid test\"[Title/Abstract] OR \"nucleic acid assay\"[Title/Abstract] OR \"microarray\"[Title/Abstract] OR \"hybridization\"[Title/Abstract] OR \"hybridisation\"[Title/Abstract] OR \"sequencing\"[Title/Abstract] OR \"In Situ Hybridization\"[Title/Abstract] OR \"in situ hybridisation\"[Title/Abstract] OR \"FISH\"[Title/Abstract] OR \"DNA\"[Title/Abstract] OR \"amplif*\"[Title/Abstract]) AND 1800/01/01:2014/08/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "9676fc4fad369f692ad49d5e18641b0234587bfefd8152ee3e40a91a5cb0ef60",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three required search concepts map to separate blocks, while reference-standard eligibility and diagnostic performance remain screening criteria as specified. The listed neonatal subgroups, sepsis and bloodstream-infection terms, and molecular assay methods are represented. No phrase warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query combines the three concept blocks with AND and combines their members with OR. The component probes also show the intended block structure."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes verified headings for newborns, sepsis and bacteremia, molecular diagnostic techniques, nucleic-acid amplification, PCR variants, hybridization, and array sequence analysis."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word set includes neonatal age labels and subgroups; sepsis, bacteremia, and bloodstream-infection wording; and a range of molecular assay terms. All 11 known relevant and validation records were retrieved, though the packet’s category-probe samples are limited."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query has no reported PubMed syntax errors, warnings, or translation issues. The displayed translation preserves the intended Boolean structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date restriction is reported. The Entrez date bound matches the stated 2014-08-09 as-of snapshot."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "90ddff1f47b6c985f81ef49889ed3ac72a5c944e56d718053983c0aced6f5f1b",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The required search concepts map to separate blocks, and the reference standard and diagnostic performance remain screening criteria. However, the protocol names septicemia as a sepsis-term member, while the text-word block relies on septic*[tiab] rather than including septicemia[tiab] as its own bare term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query combines the three search blocks with AND and their members with OR. The probes preserve the intended block structure."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes verified headings for newborns, sepsis and bacteremia, and the listed molecular diagnostic and nucleic-acid assay methods."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The text words cover neonatal labels, sepsis and bloodstream infection, and molecular assay methods. The named member septicemia is present only through septic*[tiab], contrary to the packet’s bare-name translation check."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query reports no PubMed syntax errors, warnings, or translation issues, and the displayed translation preserves its Boolean structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limit is reported. The Entrez date bound matches the stated 2014-08-09 snapshot."
        }
      },
      "findings": [
        {
          "id": "R2-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The sepsis rationale names septicemia as a searchable member, but the strategy includes only septic*[tiab], not septicemia[tiab] as its own bare name. The packet’s translation check requires a named member to be covered by its own bare name rather than only by a wildcard.",
          "recommendation": "Add septicemia[tiab] as an explicit term in the sepsis block, then run another complete evaluation.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "16738e59a792d81d594edfe9c9e0a1c2173400bb81a5536bb11821e48539f014",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three searchable concepts remain separate blocks, with reference-standard eligibility and diagnostic performance screened as specified. Septicemia is now included as its own bare term, resolving the prior translation finding."
        },
        "operators": {
          "verdict": "pass",
          "note": "The complete query combines the three concept blocks with AND and their terms with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes verified headings for newborns, sepsis and bacteremia, and the listed molecular diagnostic, nucleic-acid amplification, PCR, hybridization, and array methods."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover neonatal labels and subgroups, sepsis and bloodstream-infection wording, and molecular assay methods. The formerly missing standalone septicemia term is present."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query reports no PubMed syntax errors, warnings, or translation issues; its displayed translation preserves the intended Boolean structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date restriction is reported. The Entrez date bound matches the stated 2014-08-09 snapshot."
        }
      },
      "findings": [
        {
          "id": "R2-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The sepsis rationale names septicemia as a searchable member, but the strategy previously included only septic*[tiab], not septicemia[tiab] as its own bare name.",
          "recommendation": "Add septicemia[tiab] explicitly to the sepsis block and run another complete evaluation.",
          "status": "resolved",
          "response": "The current sepsis block and evaluated query include septicemia[tiab] explicitly; the complete evaluation reports no syntax or translation issues."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-0e688af5f547a13d12ec",
          "status": "accepted-risk",
          "response": "The neonatal category probes are stale because the block changed after the last probe and the probe budget is spent. Accept this limited evidence gap for the closing review; the available probes found no relevant records outside the earlier block.",
          "evidence": "The two earlier neonatal probes sampled 30 records each from 406 and 445 records outside the block, with 0 relevant in each sample. The current complete evaluation retrieves all 19 known relevant and validation records, with no misses."
        }
      ]
    }
  ]
}
```


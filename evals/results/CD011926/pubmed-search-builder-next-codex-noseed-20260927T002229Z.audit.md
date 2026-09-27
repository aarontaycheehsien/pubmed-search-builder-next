# PubMed search strategy: audit

Generated 2026-09-27T00:35:38+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Molecular assays for the diagnosis of sepsis in neonates
- Framework: PIRD
- Scope confirmed by user: no (User asked not to pause for questions; scope roles were inferred from the supplied eligibility criteria; scope was not user-confirmed because the user asked not to pause. User supplied no known articles. Search date bound uses PubMed Entrez date (records added by 2014-08-09); no language or study-design limit. Diagnostic performance/reference standard retained as a screening criterion. A publication-date ceiling through 2014-08-09 is applied in strategy.json in addition to the PubMed entry-date bound.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Neonates or newborn infants | search | Population is explicit and reliably indexed with age terms and neonatal headings. |
| Neonatal sepsis or bloodstream infection | search | Target condition is central and searchable in headings and title/abstract language. |
| Molecular or nucleic-acid amplification assays | search | Index test technology defines the review topic and is named/indexed in searchable records. |
| Diagnostic performance against an eligible reference standard | screen | Reference standards and diagnostic performance are inconsistently described/indexed; assess at screening. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2014-08-09
- Total records: 1,479 (1,484 before limits)
- Limits and filters: `1800/01/01:2014/08/09[dp]` (Harness instruction limits eligible literature to publications on or before 2014-08-09; the workspace as_of additionally limits PubMed entry date.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Infant, Newborn"[Mesh]` | 516,613 |
| 2 | `"Infant"[Mesh]` | 973,401 |
| 3 | `neonat*[tiab]` | 200,319 |
| 4 | `newborn*[tiab]` | 144,652 |
| 5 | `neonate*[tiab]` | 66,234 |
| 6 | `infant*[tiab]` | 356,084 |
| 7 | `preterm[tiab]` | 47,635 |
| 8 | `prematur*[tiab]` | 109,694 |
| 9 | `"very low birth weight"[tiab]` | 5,507 |
| 10 | `VLBW[tiab]` | 2,585 |
| 11 | `"young infant"[tiab]` | 794 |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 1,233,253 |
| 13 | `"Sepsis"[Mesh]` | 96,896 |
| 14 | `sepsis[tiab]` | 65,928 |
| 15 | `septic*[tiab]` | 57,072 |
| 16 | `septicemia[tiab]` | 12,411 |
| 17 | `septicaemia[tiab]` | 5,668 |
| 18 | `bloodstream infection*[tiab]` | 5,061 |
| 19 | `bacteremia[tiab]` | 17,641 |
| 20 | `bacteraemia[tiab]` | 4,429 |
| 21 | `fungemia[tiab]` | 1,351 |
| 22 | `fungaemia[tiab]` | 282 |
| 23 | `candidemia[tiab]` | 1,543 |
| 24 | `candidaemia[tiab]` | 365 |
| 25 | `septicemia*[tiab]` | 12,600 |
| 26 | `septicaemia*[tiab]` | 5,754 |
| 27 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 171,468 |
| 28 | `"Molecular Diagnostic Techniques"[Mesh]` | 10,539 |
| 29 | `"Nucleic Acid Amplification Techniques"[Mesh]` | 384,192 |
| 30 | `"Polymerase Chain Reaction"[Mesh]` | 379,038 |
| 31 | `"Reverse Transcriptase Polymerase Chain Reaction"[Mesh]` | 137,364 |
| 32 | `"Real-Time Polymerase Chain Reaction"[Mesh]` | 26,943 |
| 33 | `"Multiplex Polymerase Chain Reaction"[Mesh]` | 1,931 |
| 34 | `"Nucleic Acid Hybridization"[Mesh]` | 197,120 |
| 35 | `"In Situ Hybridization"[Mesh]` | 83,580 |
| 36 | `"In Situ Hybridization, Fluorescence"[Mesh]` | 36,705 |
| 37 | `"DNA Probes"[Mesh]` | 182,652 |
| 38 | `"Oligonucleotide Array Sequence Analysis"[Mesh]` | 70,727 |
| 39 | `"RNA, Ribosomal, 16S"[Mesh]` | 31,989 |
| 40 | `PCR[tiab]` | 345,331 |
| 41 | `"polymerase chain reaction"[tiab]` | 173,771 |
| 42 | `RT-PCR[tiab]` | 105,987 |
| 43 | `"reverse transcriptase PCR"[tiab]` | 4,770 |
| 44 | `"real-time PCR"[tiab]` | 41,289 |
| 45 | `"real time PCR"[tiab]` | 41,289 |
| 46 | `qPCR[tiab]` | 12,523 |
| 47 | `"quantitative PCR"[tiab]` | 16,124 |
| 48 | `"multiplex PCR"[tiab]` | 5,973 |
| 49 | `"nucleic acid amplification"[tiab]` | 2,113 |
| 50 | `"DNA amplification"[tiab]` | 3,472 |
| 51 | `"molecular assay"[tiab]` | 533 |
| 52 | `"molecular assays"[tiab]` | 1,152 |
| 53 | `"molecular test"[tiab]` | 376 |
| 54 | `"molecular tests"[tiab]` | 1,020 |
| 55 | `"molecular diagnostic"[tiab]` | 2,434 |
| 56 | `"molecular diagnostics"[tiab]` | 2,308 |
| 57 | `"16S rRNA"[tiab]` | 26,329 |
| 58 | `"16S rDNA"[tiab]` | 7,338 |
| 59 | `"ribosomal RNA"[tiab]` | 13,242 |
| 60 | `"bacterial DNA"[tiab]` | 3,362 |
| 61 | `"DNA probe"[tiab]` | 5,135 |
| 62 | `"DNA probes"[tiab]` | 6,989 |
| 63 | `hybridization[tiab]` | 151,455 |
| 64 | `hybridisation[tiab]` | 8,941 |
| 65 | `microarray*[tiab]` | 73,929 |
| 66 | `FISH[tiab]` | 115,046 |
| 67 | `SeptiFast[tiab]` | 69 |
| 68 | `LightCycler[tiab]` | 1,459 |
| 69 | `"Self-Sustained Sequence Replication"[Mesh]` | 209 |
| 70 | `"Sequence Analysis, DNA"[Mesh]` | 166,605 |
| 71 | `LAMP[tiab]` | 13,439 |
| 72 | `"loop-mediated isothermal amplification"[tiab]` | 1,112 |
| 73 | `"isothermal amplification"[tiab]` | 1,299 |
| 74 | `"DNA sequencing"[tiab]` | 19,242 |
| 75 | `"16S sequencing"[tiab]` | 40 |
| 76 | `"sequence-based assay"[tiab]` | 9 |
| 77 | `"sequencing assay"[tiab]` | 164 |
| 78 | `sequencing[tiab]` | 141,259 |
| 79 | `#28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78` | 1,208,951 |
| 80 | `#12 AND #27 AND #79` | 1,484 |
| 81 | `#80 AND 1800/01/01:2014/08/09[dp]` | 1,479 |

### Strategy (single line, for copying into PubMed)

```text
(("Infant, Newborn"[Mesh] OR "Infant"[Mesh] OR neonat*[tiab] OR newborn*[tiab] OR neonate*[tiab] OR infant*[tiab] OR preterm[tiab] OR prematur*[tiab] OR "very low birth weight"[tiab] OR VLBW[tiab] OR "young infant"[tiab]) AND ("Sepsis"[Mesh] OR sepsis[tiab] OR septic*[tiab] OR septicemia[tiab] OR septicaemia[tiab] OR bloodstream infection*[tiab] OR bacteremia[tiab] OR bacteraemia[tiab] OR fungemia[tiab] OR fungaemia[tiab] OR candidemia[tiab] OR candidaemia[tiab] OR septicemia*[tiab] OR septicaemia*[tiab]) AND ("Molecular Diagnostic Techniques"[Mesh] OR "Nucleic Acid Amplification Techniques"[Mesh] OR "Polymerase Chain Reaction"[Mesh] OR "Reverse Transcriptase Polymerase Chain Reaction"[Mesh] OR "Real-Time Polymerase Chain Reaction"[Mesh] OR "Multiplex Polymerase Chain Reaction"[Mesh] OR "Nucleic Acid Hybridization"[Mesh] OR "In Situ Hybridization"[Mesh] OR "In Situ Hybridization, Fluorescence"[Mesh] OR "DNA Probes"[Mesh] OR "Oligonucleotide Array Sequence Analysis"[Mesh] OR "RNA, Ribosomal, 16S"[Mesh] OR PCR[tiab] OR "polymerase chain reaction"[tiab] OR RT-PCR[tiab] OR "reverse transcriptase PCR"[tiab] OR "real-time PCR"[tiab] OR "real time PCR"[tiab] OR qPCR[tiab] OR "quantitative PCR"[tiab] OR "multiplex PCR"[tiab] OR "nucleic acid amplification"[tiab] OR "DNA amplification"[tiab] OR "molecular assay"[tiab] OR "molecular assays"[tiab] OR "molecular test"[tiab] OR "molecular tests"[tiab] OR "molecular diagnostic"[tiab] OR "molecular diagnostics"[tiab] OR "16S rRNA"[tiab] OR "16S rDNA"[tiab] OR "ribosomal RNA"[tiab] OR "bacterial DNA"[tiab] OR "DNA probe"[tiab] OR "DNA probes"[tiab] OR hybridization[tiab] OR hybridisation[tiab] OR microarray*[tiab] OR FISH[tiab] OR SeptiFast[tiab] OR LightCycler[tiab] OR "Self-Sustained Sequence Replication"[Mesh] OR "Sequence Analysis, DNA"[Mesh] OR LAMP[tiab] OR "loop-mediated isothermal amplification"[tiab] OR "isothermal amplification"[tiab] OR "DNA sequencing"[tiab] OR "16S sequencing"[tiab] OR "sequence-based assay"[tiab] OR "sequencing assay"[tiab] OR sequencing[tiab])) AND (1800/01/01:2014/08/09[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 12 | 12 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| neonate | 10,743 | 0 |
| sepsis | 55,997 | 0 |
| molecular | 27,625 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,316 | initial | none | Initial three-block strategy; searched neonatal population, sepsis/bloodstream infection, and molecular/nucleic-acid assays; reference standard and accuracy remain screening criteria; publication-date cutoff added per harness. |
| 2 | 1,316 | limits/combination | none | Initial three-block strategy; searched neonatal population, sepsis/bloodstream infection, and molecular/nucleic-acid assays; reference standard and accuracy remain screening criteria; publication-date cutoff added per harness. |
| 3 | 1,479 | molecular: +10 / -0 | none | Internal critic F1: documented required publication-date cutoff in protocol; retained strategy limit. F2: added LAMP/isothermal amplification and sequencing-based terms plus corresponding MeSH headings because molecular assays include these approaches. |
| 4 | 1,479 | limits/combination | none | final counts, run live |
| 5 | 1,479 | limits/combination | none | final counts, run live |
| 6 | 1,479 | limits/combination | none | final counts, run live |
| 7 | 1,479 | limits/combination | none | final counts, run live |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; F1 must-fix open, F2 should-fix open
- Round 2 on version 3: 2 findings; F1 must-fix resolved, F2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 813 NCBI requests logged (192 from cache); strategy sha256 641a5be54948._

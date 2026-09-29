# PubMed search strategy: audit

Generated 2026-09-28T21:08:48+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Molecular assays for the diagnosis of sepsis in neonates
- Framework: PIRD
- Scope confirmed by user: no (User requested standard depth, supplied no known relevant articles, and cannot answer questions during this run; proceed with the stated PIRD interpretation without confirmation. The runtime PSB_AS_OF environment bound is 2014-08-09 (Entrez date); no publication-date limit is applied. Reference-standard and diagnostic-performance eligibility are handled at screening. The sepsis/bloodstream-infection concept is treated as an explicit named label set rather than a category; bacteremia, fungemia, candidemia, and viral bloodstream wording are covered directly.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Neonates or newborn infants | search | Population required by the question; neonatal age is commonly named or indexed, with newborn and premature-infant terminology included as members. |
| Neonatal sepsis or bloodstream infection | search | The search concept is an explicit list of diagnosis labels in the eligibility criteria (sepsis or bloodstream infection), not a broad unenumerated topic category; named bloodstream-infection members such as bacteremia and fungemia are searched directly, alongside the exploded Sepsis heading. |
| Molecular or nucleic-acid amplification assay | search | Index test defining the review; relevant studies may name an assay member such as PCR or 16S rRNA rather than the broader molecular-test category. |
| Eligible reference standard | screen | Eligibility depends on the comparator/reference standard used; details are inconsistently named in titles and abstracts. |
| Diagnostic performance | screen | Accuracy measures are not reliably reported in titles/abstracts; screen for diagnostic evaluation. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:07:38+00:00
- Records added to PubMed up to: 2014-08-09
- Total records: 1,565
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Infant, Newborn"[Mesh]` | 516,613 | none |
| 2 | `neonat*[tiab]` | 200,319 | none |
| 3 | `newborn*[tiab]` | 144,652 | none |
| 4 | `infant*[tiab]` | 356,084 | none |
| 5 | `"newborn infant"[tiab:~0]` | 7,980 | none |
| 6 | `"premature infant"[tiab:~1]` | 4,314 | none |
| 7 | `"preterm infant"[tiab:~1]` | 2,846 | none |
| 8 | `"low birth weight"[tiab:~2]` | 20,221 | none |
| 9 | `premature*[tiab]` | 99,036 | none |
| 10 | `preterm*[tiab]` | 49,276 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 892,943 | none |
| 12 | `"Sepsis"[Mesh]` | 96,896 | none |
| 13 | `"Bacteremia"[Mesh]` | 22,734 | none |
| 14 | `sepsis[tiab]` | 65,928 | none |
| 15 | `septicemia[tiab]` | 12,411 | none |
| 16 | `septicem*[tiab]` | 13,240 | none |
| 17 | `bacteremia[tiab]` | 17,641 | none |
| 18 | `bacteraemia[tiab]` | 4,429 | none |
| 19 | `bacterem*[tiab]` | 19,298 | none |
| 20 | `bacteraem*[tiab]` | 4,846 | none |
| 21 | `"bloodstream infection"[tiab:~0]` | 2,514 | none |
| 22 | `"blood stream infection"[tiab:~0]` | 346 | none |
| 23 | `"systemic infection"[tiab:~1]` | 6,098 | none |
| 24 | `fungemia*[tiab]` | 1,383 | none |
| 25 | `fungaemia*[tiab]` | 294 | none |
| 26 | `candidemia*[tiab]` | 1,563 | none |
| 27 | `candidaemia*[tiab]` | 370 | none |
| 28 | `viremia[tiab]` | 8,881 | none |
| 29 | `viraemia[tiab]` | 2,365 | none |
| 30 | `BSI[tiab]` | 2,269 | none |
| 31 | `"bloodstream infections"[tiab:~0]` | 3,375 | none |
| 32 | `"blood stream infections"[tiab:~0]` | 431 | none |
| 33 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32` | 164,670 | none |
| 34 | `"Molecular Diagnostic Techniques"[Mesh]` | 10,539 | none |
| 35 | `"Nucleic Acid Amplification Techniques"[Mesh]` | 384,192 | none |
| 36 | `"Polymerase Chain Reaction"[Mesh]` | 379,038 | none |
| 37 | `"Real-Time Polymerase Chain Reaction"[Mesh]` | 26,943 | none |
| 38 | `"Multiplex Polymerase Chain Reaction"[Mesh]` | 1,931 | none |
| 39 | `"Reverse Transcriptase Polymerase Chain Reaction"[Mesh]` | 137,364 | none |
| 40 | `"In Situ Hybridization"[Mesh]` | 83,580 | none |
| 41 | `"RNA, Ribosomal, 16S"[Mesh]` | 31,989 | none |
| 42 | `"Sequence Analysis, DNA"[Mesh]` | 166,605 | none |
| 43 | `molecul*[tiab]` | 1,369,727 | none |
| 44 | `PCR[tiab]` | 345,331 | none |
| 45 | `qPCR[tiab]` | 12,523 | none |
| 46 | `"polymerase chain reaction"[tiab:~0]` | 173,784 | none |
| 47 | `"real time PCR"[tiab:~1]` | 58,627 | none |
| 48 | `"real time polymerase chain reaction"[tiab:~1]` | 17,514 | none |
| 49 | `"reverse transcriptase PCR"[tiab:~1]` | 5,768 | none |
| 50 | `"nucleic acid amplification"[tiab:~1]` | 2,231 | none |
| 51 | `"nucleic acid test"[tiab:~1]` | 408 | none |
| 52 | `"gene amplification"[tiab:~1]` | 7,357 | none |
| 53 | `"16S rRNA"[tiab:~0]` | 26,359 | none |
| 54 | `"16S ribosomal RNA"[tiab:~0]` | 1,928 | none |
| 55 | `"16S rDNA"[tiab:~0]` | 7,343 | none |
| 56 | `"in situ hybridization"[tiab:~1]` | 79,566 | none |
| 57 | `"fluorescence in situ hybridization"[tiab:~1]` | 21,052 | none |
| 58 | `"DNA probe"[tiab:~1]` | 6,684 | none |
| 59 | `"DNA sequencing"[tiab:~0]` | 19,537 | none |
| 60 | `"RNA sequencing"[tiab:~0]` | 2,284 | none |
| 61 | `"oligonucleotide array"[tiab:~1]` | 908 | none |
| 62 | `FISH[tiab]` | 115,046 | none |
| 63 | `LAMP[tiab]` | 13,439 | none |
| 64 | `"loop mediated isothermal amplification"[tiab:~1]` | 1,125 | none |
| 65 | `"transcription mediated amplification"[tiab:~1]` | 238 | none |
| 66 | `TMA[tiab]` | 4,561 | none |
| 67 | `#34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66` | 2,141,882 | none |
| 68 | `#11 AND #33 AND #67` | 1,565 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Infant, Newborn"[Mesh] OR neonat*[tiab] OR newborn*[tiab] OR infant*[tiab] OR "newborn infant"[tiab:~0] OR "premature infant"[tiab:~1] OR "preterm infant"[tiab:~1] OR "low birth weight"[tiab:~2] OR premature*[tiab] OR preterm*[tiab]) AND ("Sepsis"[Mesh] OR "Bacteremia"[Mesh] OR sepsis[tiab] OR septicemia[tiab] OR septicem*[tiab] OR bacteremia[tiab] OR bacteraemia[tiab] OR bacterem*[tiab] OR bacteraem*[tiab] OR "bloodstream infection"[tiab:~0] OR "blood stream infection"[tiab:~0] OR "systemic infection"[tiab:~1] OR fungemia*[tiab] OR fungaemia*[tiab] OR candidemia*[tiab] OR candidaemia*[tiab] OR viremia[tiab] OR viraemia[tiab] OR BSI[tiab] OR "bloodstream infections"[tiab:~0] OR "blood stream infections"[tiab:~0]) AND ("Molecular Diagnostic Techniques"[Mesh] OR "Nucleic Acid Amplification Techniques"[Mesh] OR "Polymerase Chain Reaction"[Mesh] OR "Real-Time Polymerase Chain Reaction"[Mesh] OR "Multiplex Polymerase Chain Reaction"[Mesh] OR "Reverse Transcriptase Polymerase Chain Reaction"[Mesh] OR "In Situ Hybridization"[Mesh] OR "RNA, Ribosomal, 16S"[Mesh] OR "Sequence Analysis, DNA"[Mesh] OR molecul*[tiab] OR PCR[tiab] OR qPCR[tiab] OR "polymerase chain reaction"[tiab:~0] OR "real time PCR"[tiab:~1] OR "real time polymerase chain reaction"[tiab:~1] OR "reverse transcriptase PCR"[tiab:~1] OR "nucleic acid amplification"[tiab:~1] OR "nucleic acid test"[tiab:~1] OR "gene amplification"[tiab:~1] OR "16S rRNA"[tiab:~0] OR "16S ribosomal RNA"[tiab:~0] OR "16S rDNA"[tiab:~0] OR "in situ hybridization"[tiab:~1] OR "fluorescence in situ hybridization"[tiab:~1] OR "DNA probe"[tiab:~1] OR "DNA sequencing"[tiab:~0] OR "RNA sequencing"[tiab:~0] OR "oligonucleotide array"[tiab:~1] OR FISH[tiab] OR LAMP[tiab] OR "loop mediated isothermal amplification"[tiab:~1] OR "transcription mediated amplification"[tiab:~1] OR TMA[tiab])) AND ("1800/01/01"[edat] : "2014/08/09"[edat])
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
| Neonates or newborn infants | 1 | `(Infant[Mesh] OR Infant, Premature[Mesh] OR Infant, Low Birth Weight[Mesh] OR infant*[tiab] OR baby[tiab] OR babies[tiab])` | 428 | 0/30 |
| Neonates or newborn infants | 2 | `(Infant[Mesh] OR Infant, Premature[Mesh] OR Infant, Low Birth Weight[Mesh] OR infant*[tiab] OR baby[tiab] OR babies[tiab])` | 496 | 0/30 |
| Molecular or nucleic-acid amplification assay | 1 | `(PCR[tiab] OR assay*[tiab] OR test*[tiab] OR diagnos*[tiab] OR amplif*[tiab] OR hybridiz*[tiab] OR sequenc*[tiab] OR DNA[tiab] OR RNA[tiab] OR Nucleic Acid Amplification Techniques[Mesh] OR Molecular Diagnostic Techniques[Mesh])` | 5,471 | 0/30 |
| Molecular or nucleic-acid amplification assay | 2 | `(PCR[tiab] OR assay*[tiab] OR test*[tiab] OR diagnos*[tiab] OR amplif*[tiab] OR hybridiz*[tiab] OR sequenc*[tiab] OR DNA[tiab] OR RNA[tiab] OR Nucleic Acid Amplification Techniques[Mesh] OR Molecular Diagnostic Techniques[Mesh])` | 5,793 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| neonates | 17,253 | 0 |
| sepsis_bsi | 55,216 | 0 |
| molecular_assay | 20,255 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial three-block PIRD draft from scope and screened related records; MeSH plus broad molecular-method vocabulary added, with accuracy/reference standard left for screening. |
| 2 | 0 | neonates: +2 / -0; sepsis_bsi: +2 / -0; molecular_assay: +2 / -0 | none | Initial three-block PIRD draft from scope and screened related records; MeSH plus broad molecular-method vocabulary added, with accuracy/reference standard left for screening. |
| 3 | 0 | neonates: +8 / -2; sepsis_bsi: +12 / -2; molecular_assay: +28 / -2 | none | Initial three-block PIRD draft from scope and screened related records; MeSH plus broad molecular-method vocabulary added, with accuracy/reference standard left for screening. |
| 4 | 1,331 | limits/combination | none | First valid three-block PIRD draft; MeSH and broad assay vocabulary, accuracy/reference standard screened. |
| 5 | 1,407 | neonates: +2 / -0; molecular_assay: +5 / -0 | none | Address critic lexical findings by adding bare preterm/premature population wording and FISH/LAMP/TMA plus spelled-out amplification methods; retain required Entrez cutoff 2014-08-09. |
| 6 | 1,565 | sepsis_bsi: +9 / -0 | none | Complete critic vocabulary revisions; add bloodstream infection member labels (fungemia/candidemia/viremia and plural BSI wording), remove duplicate FISH phrase, and classify the sepsis/B​​SI label list as non-category because named members are searched explicitly. Retain required runtime Entrez cutoff. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 3 findings; R1-F01 should-fix open, R1-F02 should-fix open, R1-F03 must-fix open
- Round 2 on version 6: 3 findings; R1-F01 should-fix resolved, R1-F02 should-fix resolved, R1-F03 must-fix accepted-risk
- Round 3 on version 6: 3 findings; R1-F01 should-fix resolved, R1-F02 should-fix resolved, R1-F03 must-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1120 NCBI requests logged (559 from cache); strategy sha256 9fb8a6eca66f._

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
      "requested": "Infant, Newborn",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Sepsis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bacteremia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Bacteremia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Molecular Diagnostic Techniques",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Molecular Diagnostic Techniques\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Nucleic Acid Amplification Techniques",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Nucleic Acid Amplification Techniques\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Real-Time Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Real-Time Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Multiplex Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "\"Multiplex Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reverse Transcriptase Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "\"Reverse Transcriptase Polymerase Chain Reaction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "In Situ Hybridization",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "\"In Situ Hybridization\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "RNA, Ribosomal, 16S",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012336",
          "name": "RNA, Ribosomal, 16S",
          "type": "descriptor",
          "scope_note": "Constituent of 30S subunit prokaryotic ribosomes containing 1600 nucleotides and 21 proteins. 16S rRNA is involved in initiation of polypeptide synthesis.",
          "tree_numbers": [
            "D13.444.735.686.670"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012336",
      "preferred_label": "RNA, Ribosomal, 16S",
      "type": "descriptor",
      "location": "vocabulary:39",
      "term": {
        "text": "\"RNA, Ribosomal, 16S\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sequence Analysis, DNA",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:07:38+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017422",
          "name": "Sequence Analysis, DNA",
          "type": "descriptor",
          "scope_note": "A multistage process that includes cloning, physical mapping, subcloning, determination of the DNA SEQUENCE, and information analysis.",
          "tree_numbers": [
            "E05.393.760.700"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017422",
      "preferred_label": "Sequence Analysis, DNA",
      "type": "descriptor",
      "location": "vocabulary:40",
      "term": {
        "text": "\"Sequence Analysis, DNA\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"infant, newborn\"[MeSH Terms] OR \"neonat*\"[Title/Abstract] OR \"newborn*\"[Title/Abstract] OR \"infant*\"[Title/Abstract] OR \"newborn infant\"[Title/Abstract:~0] OR \"premature infant\"[Title/Abstract:~1] OR \"preterm infant\"[Title/Abstract:~1] OR \"low birth weight\"[Title/Abstract:~2] OR \"premature*\"[Title/Abstract] OR \"preterm*\"[Title/Abstract]) AND (\"Sepsis\"[MeSH Terms] OR \"Bacteremia\"[MeSH Terms] OR \"Sepsis\"[Title/Abstract] OR \"septicemia\"[Title/Abstract] OR \"septicem*\"[Title/Abstract] OR \"Bacteremia\"[Title/Abstract] OR \"bacteraemia\"[Title/Abstract] OR \"bacterem*\"[Title/Abstract] OR \"bacteraem*\"[Title/Abstract] OR \"bloodstream infection\"[Title/Abstract:~0] OR \"blood stream infection\"[Title/Abstract:~0] OR \"systemic infection\"[Title/Abstract:~1] OR \"fungemia*\"[Title/Abstract] OR \"fungaemia*\"[Title/Abstract] OR \"candidemia*\"[Title/Abstract] OR \"candidaemia*\"[Title/Abstract] OR \"viremia\"[Title/Abstract] OR \"viraemia\"[Title/Abstract] OR \"BSI\"[Title/Abstract] OR \"bloodstream infections\"[Title/Abstract:~0] OR \"blood stream infections\"[Title/Abstract:~0]) AND (\"Molecular Diagnostic Techniques\"[MeSH Terms] OR \"Nucleic Acid Amplification Techniques\"[MeSH Terms] OR \"Polymerase Chain Reaction\"[MeSH Terms] OR \"Real-Time Polymerase Chain Reaction\"[MeSH Terms] OR \"Multiplex Polymerase Chain Reaction\"[MeSH Terms] OR \"Reverse Transcriptase Polymerase Chain Reaction\"[MeSH Terms] OR \"In Situ Hybridization\"[MeSH Terms] OR \"rna, ribosomal, 16s\"[MeSH Terms] OR \"sequence analysis, dna\"[MeSH Terms] OR \"molecul*\"[Title/Abstract] OR \"PCR\"[Title/Abstract] OR \"qPCR\"[Title/Abstract] OR \"Polymerase Chain Reaction\"[Title/Abstract:~0] OR \"real time PCR\"[Title/Abstract:~1] OR \"Real-Time Polymerase Chain Reaction\"[Title/Abstract:~1] OR \"reverse transcriptase PCR\"[Title/Abstract:~1] OR \"nucleic acid amplification\"[Title/Abstract:~1] OR \"nucleic acid test\"[Title/Abstract:~1] OR \"gene amplification\"[Title/Abstract:~1] OR \"16S rRNA\"[Title/Abstract:~0] OR \"16S ribosomal RNA\"[Title/Abstract:~0] OR \"16S rDNA\"[Title/Abstract:~0] OR \"In Situ Hybridization\"[Title/Abstract:~1] OR \"fluorescence in situ hybridization\"[Title/Abstract:~1] OR \"DNA probe\"[Title/Abstract:~1] OR \"DNA sequencing\"[Title/Abstract:~0] OR \"RNA sequencing\"[Title/Abstract:~0] OR \"oligonucleotide array\"[Title/Abstract:~1] OR \"FISH\"[Title/Abstract] OR \"LAMP\"[Title/Abstract] OR \"loop mediated isothermal amplification\"[Title/Abstract:~1] OR \"transcription mediated amplification\"[Title/Abstract:~1] OR \"TMA\"[Title/Abstract]) AND 1800/01/01:2014/08/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "8918ff4d38002d9c17c6af72a50838a938f6256429fec6cdd3025be237e9586c",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Population rationale includes premature-infant terminology, while only phrases requiring infant are present; bare status terms should be searched."
        },
        "operators": {
          "verdict": "pass",
          "note": "Three required concepts are ANDed and their synonyms ORed; proximity distances are appropriate and no wildcard is used within proximity."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant headings are present and the sampled category probes found no relevant gap."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Explicit FISH, LAMP, loop-mediated isothermal amplification, and transcription-mediated amplification wording may improve coverage."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Boolean structure is balanced and PubMed translation preserves the intended blocks."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The reviewer recommended removing the entry-date bound; this recommendation is subject to the explicit run cutoff requirement."
        }
      },
      "findings": [
        {
          "id": "R1-F01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The neonatal block requires infant in proximity phrases and lacks standalone premature/preterm status terms.",
          "recommendation": "Add premature*[tiab] and preterm*[tiab] and reevaluate.",
          "status": "open"
        },
        {
          "id": "R1-F02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The molecular-test block does not explicitly include FISH, LAMP, loop-mediated isothermal amplification, or transcription-mediated amplification.",
          "recommendation": "Add justified variants and reevaluate.",
          "status": "open"
        },
        {
          "id": "R1-F03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "Reviewer objected to the effective entry-date bound through 2014-08-09.",
          "recommendation": "Remove the entry-date limit unless protocol documents the cutoff.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "c2e91b6d4d49055a152615af2b8492a0fb0b285a54507a34fb92921dc52389c8",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The neonatal block includes standalone premature* and preterm* terms. Named sepsis and bloodstream-infection labels and the specified molecular assay variants are searched directly."
        },
        "operators": {
          "verdict": "pass",
          "note": "Three required concepts are ANDed and their synonyms ORed. Proximity expressions use explicit distances and no wildcard within proximity."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant neonatal, sepsis, bacteremia, and molecular-method headings are included. The sampled category probes found no relevant records outside the population or assay blocks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "FISH, LAMP, loop-mediated isothermal amplification, transcription-mediated amplification, and TMA are now included."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is balanced and PubMed translation preserves the intended blocks and date field."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2014-08-09 Entrez date bound is documented as the runtime PSB_AS_OF cutoff; no publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The neonatal block required infant in proximity phrases and lacked standalone premature/preterm status terms.",
          "recommendation": "Add premature*[tiab] and preterm*[tiab] and reevaluate.",
          "status": "resolved",
          "response": "Version 6 adds premature*[tiab] and preterm*[tiab]; the current neonatal block covers these status terms independently."
        },
        {
          "id": "R1-F02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The molecular-test block did not explicitly include FISH, LAMP, loop-mediated isothermal amplification, or transcription-mediated amplification.",
          "recommendation": "Add justified variants and reevaluate.",
          "status": "resolved",
          "response": "Version 6 includes FISH[tiab], LAMP[tiab], the loop-mediated and transcription-mediated amplification phrases, and TMA[tiab]."
        },
        {
          "id": "R1-F03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "Reviewer objected to the effective entry-date bound through 2014-08-09.",
          "recommendation": "Remove the entry-date limit unless protocol documents the cutoff.",
          "status": "accepted-risk",
          "response": "The packet documents 2014-08-09 as the runtime PSB_AS_OF Entrez-date bound. The user-requested run cutoff is retained; it is not a publication-date restriction."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "c2e91b6d4d49055a152615af2b8492a0fb0b285a54507a34fb92921dc52389c8",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Version 6 adds standalone premature*[tiab] and preterm*[tiab]. The named sepsis and bloodstream-infection labels, including the stated members, are searched directly."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three required concepts are combined with AND, with synonyms combined using OR. Proximity distances are explicit and no wildcard is used within proximity."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant neonatal, sepsis, bacteremia, and molecular-method headings. The supplied category probes found no relevant records outside the population or assay blocks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Version 6 includes FISH, LAMP, loop-mediated isothermal amplification, transcription-mediated amplification, and TMA terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied PubMed translation is balanced and preserves the intended blocks and entry-date field."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2014-08-09 Entrez-date cutoff is documented as the runtime PSB_AS_OF bound, and no publication-date limit is applied. The reviewer’s objection is recorded as accepted risk."
        }
      },
      "findings": [
        {
          "id": "R1-F01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The neonatal block required infant in proximity phrases and lacked standalone premature/preterm status terms.",
          "recommendation": "Add premature*[tiab] and preterm*[tiab] and reevaluate.",
          "status": "resolved",
          "response": "Version 6 adds premature*[tiab] and preterm*[tiab]; the current neonatal block covers these status terms independently."
        },
        {
          "id": "R1-F02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The molecular-test block did not explicitly include FISH, LAMP, loop-mediated isothermal amplification, or transcription-mediated amplification.",
          "recommendation": "Add justified variants and reevaluate.",
          "status": "resolved",
          "response": "Version 6 includes FISH[tiab], LAMP[tiab], the loop-mediated and transcription-mediated amplification phrases, and TMA[tiab]."
        },
        {
          "id": "R1-F03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "Reviewer objected to the effective entry-date bound through 2014-08-09.",
          "recommendation": "Remove the entry-date limit unless protocol documents the cutoff.",
          "status": "accepted-risk",
          "response": "The packet documents 2014-08-09 as the runtime PSB_AS_OF Entrez-date bound. The user-requested run cutoff is retained; it is not a publication-date restriction."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


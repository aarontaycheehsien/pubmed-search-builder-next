# PubMed search strategy: audit

Generated 2026-09-28T21:40:46+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Molecular assays for the diagnosis of sepsis in neonates
- Framework: PIRD
- Scope confirmed by user: yes (No known relevant articles were supplied and the user asked to proceed without questions. Scope was set from the question using PIRD: sepsis and molecular assay are required search blocks; neonatal population is tested as optional because some mixed-age studies may report the eligible subgroup only in full text; reference-standard and diagnostic-performance details are screened. No date, language, age, or study-design limits. PubMed Entrez-date cutoff is supplied through PSB_AS_OF=2014-08-09 on every command; no publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Neonatal sepsis or bloodstream infection | search | The target condition is central to every eligible study; includes sepsis and bloodstream-infection wording. |
| Molecular or nucleic-acid amplification assay | search | The index test defines the review and is ordinarily named in abstracts or indexing. |
| Neonates or newborn infants | optional | Population is central, but mixed-age studies may report neonatal subgroup eligibility only in full text; test whether AND-ing age terms is safe. |
| Eligible reference standard and diagnostic performance | screen | Reference standards and performance eligibility are inconsistently named in abstracts; apply at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:39:42+00:00
- Records added to PubMed up to: 2014-08-09
- Total records: 748
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Sepsis[Mesh]` | 96,896 | none |
| 2 | `Bacteremia[Mesh]` | 22,734 | none |
| 3 | `sepsis[tiab]` | 65,928 | none |
| 4 | `septicemia[tiab]` | 12,411 | none |
| 5 | `bloodstream infection*[tiab]` | 5,061 | none |
| 6 | `bacteremia[tiab]` | 17,641 | none |
| 7 | `bacteraemia[tiab]` | 4,429 | none |
| 8 | `fungemia[tiab]` | 1,351 | none |
| 9 | `fungaemia[tiab]` | 282 | none |
| 10 | `pyemia[tiab]` | 63 | none |
| 11 | `pyaemia[tiab]` | 137 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 149,403 | none |
| 13 | `Molecular Diagnostic Techniques[Mesh]` | 10,539 | none |
| 14 | `Nucleic Acid Amplification Techniques[Mesh]` | 384,192 | none |
| 15 | `Polymerase Chain Reaction[Mesh]` | 379,038 | none |
| 16 | `In Situ Hybridization[Mesh]` | 83,580 | none |
| 17 | `molecular assay*[tiab]` | 1,644 | none |
| 18 | `molecular test*[tiab]` | 2,815 | none |
| 19 | `molecular diagnos*[tiab]` | 8,939 | none |
| 20 | `nucleic acid amplification[tiab]` | 2,113 | none |
| 21 | `nucleic acid test*[tiab]` | 641 | none |
| 22 | `polymerase chain reaction[tiab]` | 173,771 | none |
| 23 | `PCR[tiab]` | 345,331 | none |
| 24 | `RT-PCR[tiab]` | 105,987 | none |
| 25 | `real-time PCR[tiab]` | 41,289 | none |
| 26 | `real time PCR[tiab]` | 41,289 | none |
| 27 | `multiplex PCR[tiab]` | 5,973 | none |
| 28 | `broad-range PCR[tiab]` | 154 | none |
| 29 | `16S rRNA[tiab]` | 26,329 | none |
| 30 | `16S ribosomal RNA[tiab]` | 1,876 | none |
| 31 | `DNA probe*[tiab]` | 11,483 | none |
| 32 | `gene probe*[tiab]` | 2,032 | none |
| 33 | `DNA hybridization[tiab]` | 8,089 | none |
| 34 | `fluorescence in situ hybridization[tiab]` | 20,918 | none |
| 35 | `FISH[tiab]` | 115,046 | none |
| 36 | `DNA microarray*[tiab]` | 9,034 | none |
| 37 | `microbial DNA[tiab]` | 442 | none |
| 38 | `SeptiFast[tiab]` | 69 | none |
| 39 | `Real-Time Polymerase Chain Reaction[Mesh]` | 26,943 | none |
| 40 | `RNA, Ribosomal, 16S[Mesh]` | 31,989 | none |
| 41 | `qPCR[tiab]` | 12,523 | none |
| 42 | `qRT-PCR[tiab]` | 8,596 | none |
| 43 | `quantitative PCR[tiab]` | 16,124 | none |
| 44 | `quantitative real-time PCR[tiab]` | 9,871 | none |
| 45 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44` | 818,746 | none |
| 46 | `Infant, Newborn[Mesh]` | 516,613 | none |
| 47 | `Infant, Premature[Mesh]` | 43,920 | none |
| 48 | `Infant, Low Birth Weight[Mesh]` | 27,295 | none |
| 49 | `neonat*[tiab]` | 200,319 | none |
| 50 | `newborn*[tiab]` | 144,652 | none |
| 51 | `neonatal[tiab]` | 153,149 | none |
| 52 | `new-born[tiab]` | 3,362 | none |
| 53 | `infant, newborn[tiab]` | 17,161 | none |
| 54 | `#46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53` | 649,233 | none |
| 55 | `#12 AND #45 AND #54` | 748 | none |

### Strategy (single line, for copying into PubMed)

```text
((Sepsis[Mesh] OR Bacteremia[Mesh] OR sepsis[tiab] OR septicemia[tiab] OR bloodstream infection*[tiab] OR bacteremia[tiab] OR bacteraemia[tiab] OR fungemia[tiab] OR fungaemia[tiab] OR pyemia[tiab] OR pyaemia[tiab]) AND (Molecular Diagnostic Techniques[Mesh] OR Nucleic Acid Amplification Techniques[Mesh] OR Polymerase Chain Reaction[Mesh] OR In Situ Hybridization[Mesh] OR molecular assay*[tiab] OR molecular test*[tiab] OR molecular diagnos*[tiab] OR nucleic acid amplification[tiab] OR nucleic acid test*[tiab] OR polymerase chain reaction[tiab] OR PCR[tiab] OR RT-PCR[tiab] OR real-time PCR[tiab] OR real time PCR[tiab] OR multiplex PCR[tiab] OR broad-range PCR[tiab] OR 16S rRNA[tiab] OR 16S ribosomal RNA[tiab] OR DNA probe*[tiab] OR gene probe*[tiab] OR DNA hybridization[tiab] OR fluorescence in situ hybridization[tiab] OR FISH[tiab] OR DNA microarray*[tiab] OR microbial DNA[tiab] OR SeptiFast[tiab] OR Real-Time Polymerase Chain Reaction[Mesh] OR RNA, Ribosomal, 16S[Mesh] OR qPCR[tiab] OR qRT-PCR[tiab] OR quantitative PCR[tiab] OR quantitative real-time PCR[tiab]) AND (Infant, Newborn[Mesh] OR Infant, Premature[Mesh] OR Infant, Low Birth Weight[Mesh] OR neonat*[tiab] OR newborn*[tiab] OR neonatal[tiab] OR new-born[tiab] OR infant, newborn[tiab])) AND ("1800/01/01"[edat] : "2014/08/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Neonates or newborn infants | AND-ed | 8,330 / 748 | 91.0% | none | 0/30 (up to 10% of removed records could be relevant) | Refreshed against the current query after the qPCR terms were added. The 30-record loss sample contained no eligible neonatal sepsis diagnostic-accuracy study; no current known relevant record is lost. The neonatal population is a required eligibility criterion and the measured reduction remains about 91%, so retain this block. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Neonatal sepsis or bloodstream infection | 1 | `infection*[tiab] OR Infections[Mesh]` | 5,982 | 0/30 |
| Neonatal sepsis or bloodstream infection | 2 | `infection*[tiab] OR Infections[Mesh]` | 6,000 | 0/30 |
| Neonates or newborn infants | 1 | `Infant[Mesh] OR infant*[tiab] OR preterm[tiab] OR premature[tiab] OR baby[tiab] OR babies[tiab]` | 423 | 0/30 |
| Neonates or newborn infants | 2 | `Infant[Mesh] OR infant*[tiab] OR preterm[tiab] OR premature[tiab] OR baby[tiab] OR babies[tiab]` | 432 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| sepsis | 20,489 | 0 |
| molecular_assay | 16,881 | 0 |
| neonatal_population | 8,330 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial PIRD draft: sepsis/bloodstream infection AND molecular assay; neonatal age retained as an optional block for measurement because mixed-age cohort eligibility may appear only in full text. |
| 2 | 8,178 | limits/combination | none | Initial PIRD draft: sepsis/bloodstream infection AND molecular assay; neonatal age retained as an optional block for measurement because mixed-age cohort eligibility may appear only in full text. |
| 3 | 736 | neonatal_population: +8 / -0 | none | Measured and included neonatal-population block after screening its 30-record loss sample; no relevant record was identified among losses. |
| 4 | 2,119 | sepsis: +1 / -0; molecular_assay: +2 / -0 | none | Added MeSH headings observed in screened relevant records: Bacterial Infections in the sepsis block, and Real-Time Polymerase Chain Reaction plus RNA, Ribosomal, 16S in the assay block; each addresses observed indexing variants without adding design or accuracy filters. |
| 5 | 748 | sepsis: +0 / -1 | none | Removed Bacterial Infections[Mesh] after evaluation showed the query rose from 736 to 2,119 when added, while all five development records were already retrieved by existing sepsis wording and the prior category probe found no eligible miss. Retained the two molecular MeSH headings observed in screened relevant studies. |
| 6 | 748 | molecular_assay: +4 / -0 | none | Added explicit qPCR, qRT-PCR, quantitative PCR, and quantitative real-time PCR text terms in response to critic finding R1-TW-1; these name molecular amplification assay variants omitted by PCR alone. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 1 findings; R1-TW-1 should-fix open
- Round 2 on version 6: 2 findings; R1-TW-1 should-fix resolved, R2-TR-1 should-fix open
- Round 3 on version 6: 2 findings; R1-TW-1 should-fix resolved, R2-TR-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1320 NCBI requests logged (693 from cache); strategy sha256 c6dadd380eb2._

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
        "location": "concept:sepsis",
        "blocking": false,
        "requires_review": true,
        "id": "I-5fbde8b3c6cbfcdcdd61"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:neonatal_population",
        "blocking": false,
        "requires_review": true,
        "id": "I-c6edc45fa1031f306a9c"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:sepsis",
        "blocking": false,
        "requires_review": true,
        "id": "I-5fbde8b3c6cbfcdcdd61"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:neonatal_population",
        "blocking": false,
        "requires_review": true,
        "id": "I-c6edc45fa1031f306a9c"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Sepsis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "Sepsis",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bacteremia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Bacteremia",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Molecular Diagnostic Techniques",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "Molecular Diagnostic Techniques",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Nucleic Acid Amplification Techniques",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "Nucleic Acid Amplification Techniques",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Polymerase Chain Reaction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "In Situ Hybridization",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "In Situ Hybridization",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Real-Time Polymerase Chain Reaction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Real-Time Polymerase Chain Reaction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "RNA, Ribosomal, 16S",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
        "text": "RNA, Ribosomal, 16S",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Infant, Newborn",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "Infant, Newborn",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Infant, Premature",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007234",
          "name": "Infant, Premature",
          "type": "descriptor",
          "scope_note": "A human infant born before 37 weeks of GESTATION.",
          "tree_numbers": [
            "M01.060.703.520.520"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007234",
      "preferred_label": "Infant, Premature",
      "type": "descriptor",
      "location": "vocabulary:45",
      "term": {
        "text": "Infant, Premature",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Infant, Low Birth Weight",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:39:42+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007230",
          "name": "Infant, Low Birth Weight",
          "type": "descriptor",
          "scope_note": "An infant having a birth weight of 2500 gm. (5.5 lb.) or less but INFANT, VERY LOW BIRTH WEIGHT is available for infants having a birth weight of 1500 grams (3.3 lb.) or less.",
          "tree_numbers": [
            "M01.060.703.520.460"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007230",
      "preferred_label": "Infant, Low Birth Weight",
      "type": "descriptor",
      "location": "vocabulary:46",
      "term": {
        "text": "Infant, Low Birth Weight",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"sepsis\"[MeSH Terms] OR \"bacteremia\"[MeSH Terms] OR \"sepsis\"[Title/Abstract] OR \"septicemia\"[Title/Abstract] OR \"bloodstream infection*\"[Title/Abstract] OR \"bacteremia\"[Title/Abstract] OR \"bacteraemia\"[Title/Abstract] OR \"fungemia\"[Title/Abstract] OR \"fungaemia\"[Title/Abstract] OR \"pyemia\"[Title/Abstract] OR \"pyaemia\"[Title/Abstract]) AND (\"molecular diagnostic techniques\"[MeSH Terms] OR \"nucleic acid amplification techniques\"[MeSH Terms] OR \"polymerase chain reaction\"[MeSH Terms] OR \"in situ hybridization\"[MeSH Terms] OR \"molecular assay*\"[Title/Abstract] OR \"molecular test*\"[Title/Abstract] OR \"molecular diagnos*\"[Title/Abstract] OR \"nucleic acid amplification\"[Title/Abstract] OR \"nucleic acid test*\"[Title/Abstract] OR \"polymerase chain reaction\"[Title/Abstract] OR \"PCR\"[Title/Abstract] OR \"RT-PCR\"[Title/Abstract] OR \"real time pcr\"[Title/Abstract] OR \"real time pcr\"[Title/Abstract] OR \"multiplex pcr\"[Title/Abstract] OR \"broad range pcr\"[Title/Abstract] OR \"16s rrna\"[Title/Abstract] OR \"16s ribosomal rna\"[Title/Abstract] OR \"dna probe*\"[Title/Abstract] OR \"gene probe*\"[Title/Abstract] OR \"dna hybridization\"[Title/Abstract] OR \"fluorescence in situ hybridization\"[Title/Abstract] OR \"FISH\"[Title/Abstract] OR \"dna microarray*\"[Title/Abstract] OR \"microbial dna\"[Title/Abstract] OR \"SeptiFast\"[Title/Abstract] OR \"real time polymerase chain reaction\"[MeSH Terms] OR \"rna, ribosomal, 16s\"[MeSH Terms] OR \"qPCR\"[Title/Abstract] OR \"qRT-PCR\"[Title/Abstract] OR \"quantitative pcr\"[Title/Abstract] OR \"quantitative real time pcr\"[Title/Abstract]) AND (\"infant, newborn\"[MeSH Terms] OR \"infant, premature\"[MeSH Terms] OR \"infant, low birth weight\"[MeSH Terms] OR \"neonat*\"[Title/Abstract] OR \"newborn*\"[Title/Abstract] OR \"neonatal\"[Title/Abstract] OR \"new-born\"[Title/Abstract] OR \"infant newborn\"[Title/Abstract]) AND 1800/01/01:2014/08/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "d63b38f4c47efa72bfe905f1e6cc583ba961e2358c5f78e1c77e95ead4d84424",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks match the condition and assay concepts. The neonatal block is optional and its current decision is supported by the reported loss sample and reduction. Reference-standard and diagnostic-performance criteria are screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks use OR within concepts and AND across concepts. No NOT or proximity operators appear."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet documents verified headings for the condition, molecular methods, and neonatal population. No translation warnings or heading issues are reported."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The assay block includes PCR variants such as RT-PCR and real-time PCR, but omits common qPCR wording. The bare PCR term does not establish that qPCR records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint errors, PubMed errors, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are specified. The packet identifies the Entry Date cutoff as an as-of evaluation boundary, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-TW-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "molecular_assay",
          "finding": "The block names PCR, RT-PCR, and real-time PCR, but not qPCR or quantitative PCR. Records may describe a molecular diagnostic assay using qPCR wording without any of the listed assay phrases.",
          "recommendation": "Add and evaluate explicit qPCR and quantitative PCR variants, including qRT-PCR where appropriate; check the revised strategy for count changes and known-record losses.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "a0957dbb3f7fb31cdfb4a147198416152f3ba59de01ac034c68d4ee845d55069",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The condition, assay, and neonatal blocks represent the stated search concepts, and reference-standard and performance criteria remain for screening. The prior population-block assessment is stale after four assay terms were added: its stored fingerprint differs from the current one, although the reported count remains 748. The packet therefore does not establish that the current AND-ed population block has been tested for losses. Retain it on eligibility grounds, but refresh the safety assessment before relying on that test."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy uses OR within concept blocks and AND across them. No NOT or proximity operator appears in the final query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH headings for the condition, molecular methods, and neonatal population. No translation issues are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The assay block now includes qPCR, qRT-PCR, quantitative PCR, and quantitative real-time PCR, resolving the prior omission. The packet reports all five development records retrieved and no known records lost after the additions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint errors, PubMed errors, or translation issues. The final query translation is reported with the Entry Date boundary."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are specified. The 2014-08-09 Entry Date cutoff is identified as an as-of evaluation boundary, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-TW-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The block named PCR, RT-PCR, and real-time PCR, but omitted qPCR and quantitative PCR wording.",
          "recommendation": "Add and evaluate explicit qPCR and quantitative PCR variants, including qRT-PCR where appropriate; check count changes and known-record losses.",
          "status": "resolved",
          "response": "The current molecular assay block adds qPCR[tiab], qRT-PCR[tiab], quantitative PCR[tiab], and quantitative real-time PCR[tiab]. The packet reports the count unchanged at 748, no known records lost or gained, and all five development records retrieved."
        },
        {
          "id": "R2-TR-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The population AND safety assessment is stale after the molecular assay block changed. The optional-concept fingerprint is 9d3521238715a217, while the current fingerprint is ad8024ffad81abad; the packet labels the assessment stale. The stated 30-record loss sample and 91.0% reduction therefore do not establish safety for the current strategy. The packet reports the current test as 8,330 records without the population block and 748 with it.",
          "recommendation": "Refresh the population-block loss assessment against the current query before describing the AND-ed block as tested for safety. Retain the block meanwhile because neonatal eligibility is required and the packet does not show known records lost.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-5fbde8b3c6cbfcdcdd61",
          "status": "accepted-risk",
          "response": "The stale category-probe warning is accepted with residual uncertainty because the probe budget is spent and the packet provides no current probe sample. The sepsis category block itself was not among the changed terms, but the assay additions changed the rest of the probe query.",
          "evidence": "The prior sepsis probes used the broader clause `infection*[tiab] OR Infections[Mesh]`; probe 1 screened 30 of 5,982 outside-block records and probe 2 screened 30 of 6,000, with 0 relevant in each. Since version 5, qPCR[tiab], qRT-PCR[tiab], quantitative PCR[tiab], and quantitative real-time PCR[tiab] were added to the assay block. The current strategy count remains 748, with no known records lost or gained and all five development records retrieved. These observations support retaining the strategy for now but do not make the old probes current."
        },
        {
          "issue_id": "I-c6edc45fa1031f306a9c",
          "status": "accepted-risk",
          "response": "The stale population-probe warning is accepted with residual uncertainty because the probe budget is spent and the packet provides no current probe sample. Keep the neonatal block on eligibility grounds; do not treat the stale probes as evidence that AND-ing it is safe.",
          "evidence": "The prior population probes used `Infant[Mesh] OR infant*[tiab] OR preterm[tiab] OR premature[tiab] OR baby[tiab] OR babies[tiab]`; probe 1 screened 30 of 423 outside-block records and probe 2 screened 30 of 432, with 0 relevant in each. The assay block has since gained qPCR[tiab], qRT-PCR[tiab], quantitative PCR[tiab], and quantitative real-time PCR[tiab]. The current count is 748, all five development records are retrieved, and the reported reduction from 8,330 to 748 is 91.0%; however, the packet labels the population assessment stale and its current fingerprint differs from the stored one. These facts support retaining the required population block while leaving its current loss-safety assessment unverified."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "56cc08aa374ab36d57ff786834b25fe1719cfc4c5328374cd9993775cc1c771b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search blocks represent the stated condition and assay concepts; reference-standard and diagnostic-performance criteria remain for screening. The current population-block assessment matches fingerprint ad8024ffad81abad, reports a 30-record loss sample with 0 relevant records, and shows no known records lost."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy uses OR within concepts and AND across concepts. No NOT or proximity operators appear in the final query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH headings for the condition, molecular methods, and neonatal population, with no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The molecular assay block includes qPCR, qRT-PCR, quantitative PCR, and quantitative real-time PCR. All five development records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint errors, PubMed errors, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are specified. The 2014-08-09 Entry Date cutoff is identified as an evaluation boundary, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-TW-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The block named PCR, RT-PCR, and real-time PCR, but omitted qPCR and quantitative PCR wording.",
          "recommendation": "Add and evaluate explicit qPCR and quantitative PCR variants, including qRT-PCR where appropriate; check count changes and known-record losses.",
          "status": "resolved",
          "response": "The current block adds qPCR[tiab], qRT-PCR[tiab], quantitative PCR[tiab], and quantitative real-time PCR[tiab]. The packet reports all five development records retrieved, no known records lost or gained, and the count unchanged at 748."
        },
        {
          "id": "R2-TR-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The population AND safety assessment was stale after the molecular assay block changed. The optional-concept fingerprint is 9d3521238715a217, while the current fingerprint is ad8024ffad81abad; the packet labels the assessment stale. The stated 30-record loss sample and 91.0% reduction therefore do not establish safety for the current strategy. The packet reports the current test as 8,330 records without the population block and 748 with it.",
          "recommendation": "Refresh the population-block loss assessment against the current query before describing the AND-ed block as tested for safety. Retain the block meanwhile because neonatal eligibility is required and the packet does not show known records lost.",
          "status": "resolved",
          "response": "The packet now reports a current population-block assessment with fingerprint ad8024ffad81abad, matching the current fingerprint. Its 30-record loss sample contains no relevant records; the current reduction is 91.0%, from 8,330 to 748, with no known records lost."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-5fbde8b3c6cbfcdcdd61",
          "status": "accepted-risk",
          "response": "The sepsis category-probe warning remains because the probe budget is spent and no current probe sample is provided. Retain the strategy with residual uncertainty about coverage outside this block.",
          "evidence": "The prior probes each screened 30 records and found 0 relevant: 0/30 of 5,982 outside-block records and 0/30 of 6,000. The assay block later gained qPCR[tiab], qRT-PCR[tiab], quantitative PCR[tiab], and quantitative real-time PCR[tiab], so those probes are stale. The current count is 748, with no known records lost or gained and all five development records retrieved."
        },
        {
          "issue_id": "I-c6edc45fa1031f306a9c",
          "status": "accepted-risk",
          "response": "The neonatal population category-probe warning remains because the probe budget is spent and no current probe sample is provided. The separately refreshed population-block loss assessment supports retaining the AND-ed block, while the stale category probes leave residual uncertainty.",
          "evidence": "The prior probes each screened 30 records and found 0 relevant: 0/30 of 423 outside-block records and 0/30 of 432. Those probes are stale after the assay block additions. Separately, the current population-block assessment matches fingerprint ad8024ffad81abad, reports 0/30 relevant in its loss sample, a 91.0% reduction from 8,330 to 748, and no known records lost."
        }
      ]
    }
  ]
}
```


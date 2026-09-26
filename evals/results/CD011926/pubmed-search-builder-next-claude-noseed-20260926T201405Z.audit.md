# PubMed search strategy: audit

Generated 2026-09-26T20:27:16+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Molecular assays for the diagnosis of sepsis in neonates
- Framework: PIRD
- Scope confirmed by user: no (User asked not to be consulted during the run. Assumptions: (1) depth = standard; (2) no date/language/design limits; searches bounded to records added to PubMed by 2014-08-09 (as_of) per the run's date; (3) framework PIRD - population, target condition and index test are AND-ed; reference standard and accuracy measures handled at screening; no diagnostic filter; (4) scope not confirmed by the user because they asked not to pause - proceeding with the table as drafted; (5) ambiguity: 'molecular assays' interpreted as nucleic-acid-based tests (PCR and other amplification/hybridisation/sequencing methods), not protein biomarkers - consistent with the user's eligibility criterion; (6) neonatal sepsis interpreted to include bloodstream infection, bacteraemia and fungaemia, early- and late-onset. No seeds supplied; known records to be found via prior reviews, precise pilots and neighbours. Known records: no user seeds; prior review Pammi 2011 (PMID 21949139) found but its reference list was not available via ELink, so no benchmark set; 30 records screened in from a precise title pilot and neighbours (21 development, 9 held out as validation). Host gene-expression assays not searched explicitly (screen). Scope not user-confirmed (user asked not to pause).)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Neonates / newborn infants | search | Population; every eligible study involves neonates; reliably named (neonat*, newborn, preterm infant, NICU) and indexed (Infant, Newborn check tag). |
| Sepsis / bloodstream infection (target condition) | search | Target condition; always present; reliably named (sepsis, septicaemia, bacteraemia, bloodstream infection) and indexed (Sepsis exploded incl. Neonatal Sepsis, Bacteremia, Fungemia). Text layer adds blood culture, neonatal/newborn infection, serious/invasive bacterial infection and suspected infection phrases; broad 'bacterial infection' terms were tested (v2) and dropped as noise. |
| Molecular / nucleic-acid amplification assay (index test) | search | Index test; always present; named in abstracts (PCR, 16S rRNA, real-time PCR, SeptiFast, hybridisation, sequencing) and indexed (Polymerase Chain Reaction, Nucleic Acid Amplification Techniques, Molecular Diagnostic Techniques). |
| Reference standard (blood culture, clinical sepsis definition) | screen | Reference standard is not reliably reported in abstracts; judged at screening (PIRD convention). |
| Diagnostic accuracy measures / study design | screen | Accuracy terms (sensitivity, specificity) unreliable in abstracts and indexing; no diagnostic filter applied to maximise sensitivity. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-26
- Records added to PubMed up to: 2014-08-09
- Total records: 2,055
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Infant, Newborn"[Mesh]` | 516,613 |
| 2 | `"Infant, Newborn, Diseases"[Mesh]` | 152,612 |
| 3 | `"Intensive Care Units, Neonatal"[Mesh]` | 10,220 |
| 4 | `"Intensive Care, Neonatal"[Mesh]` | 4,464 |
| 5 | `neonat*[tiab]` | 200,319 |
| 6 | `newborn*[tiab]` | 144,652 |
| 7 | `"new born"[tiab]` | 3,362 |
| 8 | `"new borns"[tiab]` | 359 |
| 9 | `infant*[tiab]` | 356,084 |
| 10 | `preterm*[tiab]` | 49,276 |
| 11 | `"pre term"[tiab]` | 1,925 |
| 12 | `premature*[tiab]` | 99,036 |
| 13 | `prematurity[tiab]` | 14,699 |
| 14 | `NICU*[tiab]` | 6,041 |
| 15 | `"low birth weight"[tiab]` | 19,882 |
| 16 | `"low birthweight"[tiab]` | 5,861 |
| 17 | `VLBW[tiab]` | 2,585 |
| 18 | `ELBW[tiab]` | 894 |
| 19 | `"early onset sepsis"[tiab]` | 344 |
| 20 | `"late onset sepsis"[tiab]` | 419 |
| 21 | `"early onset infection"[tiab]` | 78 |
| 22 | `"late onset infection"[tiab]` | 83 |
| 23 | `baby[tiab]` | 29,752 |
| 24 | `babies[tiab]` | 28,884 |
| 25 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 962,259 |
| 26 | `"Sepsis"[Mesh]` | 96,896 |
| 27 | `"Systemic Inflammatory Response Syndrome"[Mesh]` | 99,968 |
| 28 | `"Candidemia"[Mesh]` | 522 |
| 29 | `sepsis[tiab]` | 65,928 |
| 30 | `septic*[tiab]` | 57,072 |
| 31 | `septicemi*[tiab]` | 13,230 |
| 32 | `septicaemi*[tiab]` | 6,094 |
| 33 | `bacteremi*[tiab]` | 19,296 |
| 34 | `bacteraemi*[tiab]` | 4,846 |
| 35 | `fungemi*[tiab]` | 1,400 |
| 36 | `fungaemi*[tiab]` | 296 |
| 37 | `candidemi*[tiab]` | 1,575 |
| 38 | `candidaemi*[tiab]` | 372 |
| 39 | `pyemi*[tiab]` | 85 |
| 40 | `pyaemi*[tiab]` | 153 |
| 41 | `"bloodstream infection"[tiab]` | 2,506 |
| 42 | `"bloodstream infections"[tiab]` | 3,368 |
| 43 | `"blood stream infection"[tiab]` | 344 |
| 44 | `"blood stream infections"[tiab]` | 428 |
| 45 | `"bloodstream pathogens"[tiab]` | 58 |
| 46 | `"blood infection"[tiab]` | 153 |
| 47 | `"blood infections"[tiab]` | 89 |
| 48 | `"systemic infection"[tiab]` | 4,243 |
| 49 | `"systemic infections"[tiab]` | 2,202 |
| 50 | `"invasive infection"[tiab]` | 912 |
| 51 | `"invasive infections"[tiab]` | 1,435 |
| 52 | `"blood culture"[tiab]` | 8,647 |
| 53 | `"blood cultures"[tiab]` | 11,854 |
| 54 | `SIRS[tiab]` | 3,376 |
| 55 | `"neonatal infection"[tiab]` | 1,244 |
| 56 | `"neonatal infections"[tiab]` | 907 |
| 57 | `"newborn infection"[tiab]` | 53 |
| 58 | `"newborn infections"[tiab]` | 34 |
| 59 | `"serious bacterial infection"[tiab]` | 280 |
| 60 | `"serious bacterial infections"[tiab]` | 500 |
| 61 | `"invasive bacterial infection"[tiab]` | 113 |
| 62 | `"invasive bacterial infections"[tiab]` | 152 |
| 63 | `"suspected infection"[tiab]` | 647 |
| 64 | `"suspected infections"[tiab]` | 149 |
| 65 | `#26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64` | 194,221 |
| 66 | `"Molecular Diagnostic Techniques"[Mesh]` | 10,539 |
| 67 | `"Nucleic Acid Amplification Techniques"[Mesh]` | 384,192 |
| 68 | `"Nucleic Acid Hybridization"[Mesh]` | 197,120 |
| 69 | `"Oligonucleotide Array Sequence Analysis"[Mesh]` | 70,727 |
| 70 | `"Sequence Analysis, DNA"[Mesh]` | 166,605 |
| 71 | `"DNA Probes"[Mesh]` | 182,652 |
| 72 | `"RNA, Ribosomal, 16S"[Mesh]` | 31,989 |
| 73 | `"RNA, Ribosomal, 18S"[Mesh]` | 4,721 |
| 74 | `"DNA, Ribosomal"[Mesh]` | 27,323 |
| 75 | `"Genes, rRNA"[Mesh]` | 6,198 |
| 76 | `"DNA, Bacterial"[Mesh]` | 94,161 |
| 77 | `"DNA, Fungal"[Mesh]` | 21,323 |
| 78 | `PCR[tiab]` | 345,331 |
| 79 | `"polymerase chain reaction"[tiab]` | 173,771 |
| 80 | `"polymerase chain reactions"[tiab]` | 1,993 |
| 81 | `RT-PCR[tiab]` | 105,987 |
| 82 | `qPCR[tiab]` | 12,523 |
| 83 | `rtPCR[tiab]` | 103,794 |
| 84 | `molecular[tiab]` | 918,436 |
| 85 | `"nucleic acid"[tiab]` | 34,143 |
| 86 | `"nucleic acids"[tiab]` | 25,307 |
| 87 | `amplif*[tiab]` | 185,114 |
| 88 | `16S[tiab]` | 40,169 |
| 89 | `18S[tiab]` | 8,950 |
| 90 | `rRNA[tiab]` | 48,804 |
| 91 | `rDNA[tiab]` | 20,261 |
| 92 | `"ribosomal DNA"[tiab]` | 7,024 |
| 93 | `"ribosomal RNA"[tiab]` | 13,242 |
| 94 | `DNA[tiab]` | 791,040 |
| 95 | `SeptiFast[tiab]` | 69 |
| 96 | `"Septi Fast"[tiab]` | 1 |
| 97 | `LightCycler[tiab]` | 1,459 |
| 98 | `SepsiTest[tiab]` | 11 |
| 99 | `VYOO[tiab]` | 5 |
| 100 | `Magicplex[tiab]` | 4 |
| 101 | `Xpert[tiab]` | 410 |
| 102 | `GeneXpert[tiab]` | 129 |
| 103 | `microarray*[tiab]` | 73,929 |
| 104 | `genechip*[tiab]` | 3,101 |
| 105 | `"gene chip"[tiab]` | 893 |
| 106 | `"gene chips"[tiab]` | 384 |
| 107 | `hybridization[tiab]` | 151,455 |
| 108 | `hybridisation[tiab]` | 8,941 |
| 109 | `sequencing[tiab]` | 141,259 |
| 110 | `pyrosequenc*[tiab]` | 5,632 |
| 111 | `"universal primer"[tiab]` | 417 |
| 112 | `"universal primers"[tiab]` | 994 |
| 113 | `"broad range"[tiab]` | 24,958 |
| 114 | `panbacterial[tiab]` | 29 |
| 115 | `"pan bacterial"[tiab]` | 15 |
| 116 | `"loop mediated"[tiab]` | 1,274 |
| 117 | `LAMP[tiab]` | 13,439 |
| 118 | `isothermal[tiab]` | 10,145 |
| 119 | `multiplex[tiab]` | 22,641 |
| 120 | `"in situ hybridization"[tiab]` | 78,523 |
| 121 | `"fluorescence in situ hybridization"[tiab]` | 20,918 |
| 122 | `"fluorescent in situ hybridization"[tiab]` | 5,204 |
| 123 | `"PNA FISH"[tiab]` | 114 |
| 124 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 6,692 |
| 125 | `"Metagenomics"[Mesh]` | 1,683 |
| 126 | `metagenom*[tiab]` | 3,931 |
| 127 | `"next generation sequencing"[tiab]` | 6,727 |
| 128 | `"next-generation sequencing"[tiab]` | 6,727 |
| 129 | `NGS[tiab]` | 1,903 |
| 130 | `FilmArray[tiab]` | 34 |
| 131 | `BioFire[tiab]` | 10 |
| 132 | `Verigene[tiab]` | 33 |
| 133 | `T2Candida[tiab]` | 2 |
| 134 | `"T2 magnetic resonance"[tiab]` | 150 |
| 135 | `ddPCR[tiab]` | 252 |
| 136 | `"digital PCR"[tiab]` | 206 |
| 137 | `Unyvero[tiab]` | 1 |
| 138 | `#66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96 OR #97 OR #98 OR #99 OR #100 OR #101 OR #102 OR #103 OR #104 OR #105 OR #106 OR #107 OR #108 OR #109 OR #110 OR #111 OR #112 OR #113 OR #114 OR #115 OR #116 OR #117 OR #118 OR #119 OR #120 OR #121 OR #122 OR #123 OR #124 OR #125 OR #126 OR #127 OR #128 OR #129 OR #130 OR #131 OR #132 OR #133 OR #134 OR #135 OR #136 OR #137` | 2,439,570 |
| 139 | `#25 AND #65 AND #138` | 2,055 |

### Strategy (single line, for copying into PubMed)

```text
("Infant, Newborn"[Mesh] OR "Infant, Newborn, Diseases"[Mesh] OR "Intensive Care Units, Neonatal"[Mesh] OR "Intensive Care, Neonatal"[Mesh] OR neonat*[tiab] OR newborn*[tiab] OR "new born"[tiab] OR "new borns"[tiab] OR infant*[tiab] OR preterm*[tiab] OR "pre term"[tiab] OR premature*[tiab] OR prematurity[tiab] OR NICU*[tiab] OR "low birth weight"[tiab] OR "low birthweight"[tiab] OR VLBW[tiab] OR ELBW[tiab] OR "early onset sepsis"[tiab] OR "late onset sepsis"[tiab] OR "early onset infection"[tiab] OR "late onset infection"[tiab] OR baby[tiab] OR babies[tiab]) AND ("Sepsis"[Mesh] OR "Systemic Inflammatory Response Syndrome"[Mesh] OR "Candidemia"[Mesh] OR sepsis[tiab] OR septic*[tiab] OR septicemi*[tiab] OR septicaemi*[tiab] OR bacteremi*[tiab] OR bacteraemi*[tiab] OR fungemi*[tiab] OR fungaemi*[tiab] OR candidemi*[tiab] OR candidaemi*[tiab] OR pyemi*[tiab] OR pyaemi*[tiab] OR "bloodstream infection"[tiab] OR "bloodstream infections"[tiab] OR "blood stream infection"[tiab] OR "blood stream infections"[tiab] OR "bloodstream pathogens"[tiab] OR "blood infection"[tiab] OR "blood infections"[tiab] OR "systemic infection"[tiab] OR "systemic infections"[tiab] OR "invasive infection"[tiab] OR "invasive infections"[tiab] OR "blood culture"[tiab] OR "blood cultures"[tiab] OR SIRS[tiab] OR "neonatal infection"[tiab] OR "neonatal infections"[tiab] OR "newborn infection"[tiab] OR "newborn infections"[tiab] OR "serious bacterial infection"[tiab] OR "serious bacterial infections"[tiab] OR "invasive bacterial infection"[tiab] OR "invasive bacterial infections"[tiab] OR "suspected infection"[tiab] OR "suspected infections"[tiab]) AND ("Molecular Diagnostic Techniques"[Mesh] OR "Nucleic Acid Amplification Techniques"[Mesh] OR "Nucleic Acid Hybridization"[Mesh] OR "Oligonucleotide Array Sequence Analysis"[Mesh] OR "Sequence Analysis, DNA"[Mesh] OR "DNA Probes"[Mesh] OR "RNA, Ribosomal, 16S"[Mesh] OR "RNA, Ribosomal, 18S"[Mesh] OR "DNA, Ribosomal"[Mesh] OR "Genes, rRNA"[Mesh] OR "DNA, Bacterial"[Mesh] OR "DNA, Fungal"[Mesh] OR PCR[tiab] OR "polymerase chain reaction"[tiab] OR "polymerase chain reactions"[tiab] OR RT-PCR[tiab] OR qPCR[tiab] OR rtPCR[tiab] OR molecular[tiab] OR "nucleic acid"[tiab] OR "nucleic acids"[tiab] OR amplif*[tiab] OR 16S[tiab] OR 18S[tiab] OR rRNA[tiab] OR rDNA[tiab] OR "ribosomal DNA"[tiab] OR "ribosomal RNA"[tiab] OR DNA[tiab] OR SeptiFast[tiab] OR "Septi Fast"[tiab] OR LightCycler[tiab] OR SepsiTest[tiab] OR VYOO[tiab] OR Magicplex[tiab] OR Xpert[tiab] OR GeneXpert[tiab] OR microarray*[tiab] OR genechip*[tiab] OR "gene chip"[tiab] OR "gene chips"[tiab] OR hybridization[tiab] OR hybridisation[tiab] OR sequencing[tiab] OR pyrosequenc*[tiab] OR "universal primer"[tiab] OR "universal primers"[tiab] OR "broad range"[tiab] OR panbacterial[tiab] OR "pan bacterial"[tiab] OR "loop mediated"[tiab] OR LAMP[tiab] OR isothermal[tiab] OR multiplex[tiab] OR "in situ hybridization"[tiab] OR "fluorescence in situ hybridization"[tiab] OR "fluorescent in situ hybridization"[tiab] OR "PNA FISH"[tiab] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR "Metagenomics"[Mesh] OR metagenom*[tiab] OR "next generation sequencing"[tiab] OR "next-generation sequencing"[tiab] OR NGS[tiab] OR FilmArray[tiab] OR BioFire[tiab] OR Verigene[tiab] OR T2Candida[tiab] OR "T2 magnetic resonance"[tiab] OR ddPCR[tiab] OR "digital PCR"[tiab] OR Unyvero[tiab])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 21 | 21 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| neonate | 19,211 | 0 |
| sepsis | 72,095 | 0 |
| molecular | 24,745 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,885 | initial | none | v1: first draft, three blocks (neonate AND sepsis AND molecular), MeSH + broad tiab |
| 2 | 2,460 | sepsis: +9 / -0; molecular: +2 / -1 | none | v2: drop FISH[tiab] (fish/animal noise, 115k) for spelled-out FISH phrases; add broader infection layer (Bacterial Infections noexp, bacterial/neonatal/perinatal infection phrases) to sepsis block for neonatal-infection wording (e.g. candidate 19279393) |
| 3 | 2,028 | sepsis: +0 / -5 | none | v3: remove Bacterial Infections[Mesh:noexp], bacterial infection(s) and perinatal infection(s): sample of the ~600 added records was almost all off-topic (CF, HIV, GBS carriage, diarrhoea); keep specific neonatal/newborn infection phrases, which retrieve candidate 19279393 |
| 4 | 2,055 | neonate: +2 / -0; sepsis: +6 / -0; molecular: +14 / -0 | none | v4: critic round 1 F1/F2/F4 (sequencing MeSH + NGS/metagenomic words, commercial platform names, baby/babies) and F3 partial (specific serious/invasive bacterial infection and suspected infection phrases; broad bacterial infection terms already tested in v2 and rejected as noise) |
| 5 | 2,055 | limits/combination | none | final counts, run live |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (fresh-context subagent (general-purpose) given only packet-1.md): 6 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix accepted-risk, F4 should-fix resolved, F5 document accepted-risk, F6 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 892 NCBI requests logged (403 from cache); strategy sha256 a4f7537bc019._

## Rationale (added by hand)

- **Structure (PIRD):** neonate AND sepsis AND molecular assay. The reference standard (blood culture or a clinical definition) and accuracy measures are handled at screening, not searched. No diagnostic-accuracy filter is used because accuracy terms and indexing are unreliable for diagnostic test accuracy (DTA) studies. No limits are applied. Counts are bounded to records added to PubMed up to 2014-08-09 (`as_of`), to match the harness date.
- **MeSH:** every heading is exploded. `Sepsis` covers Neonatal Sepsis, Bacteremia, Fungemia and Shock, Septic. `Candidemia` is redundant but kept. `Infant, Newborn` covers Infant, Premature and Infant, Low Birth Weight. `Infant, Newborn, Diseases` is included for neonatal infection indexing. `Nucleic Acid Amplification Techniques` covers PCR and its narrower headings. Headings for hybridisation, microarray, sequencing, rRNA/rDNA and bacterial/fungal DNA are added because studies of 16S/18S broad-range assays are often indexed there rather than under the technique.
- **Text words:** the population block uses `infant*` and baby/babies deliberately, because neonatal studies often say only "infants". The sepsis block includes blood culture wording, because nearly every eligible study compares against blood culture. The molecular block is deliberately broad (`molecular`, `DNA`, `amplif*`, 16S, commercial assay names). The three-way AND keeps the result manageable at 2,055 records.
- **Rejected:** broad "bacterial infection(s)" and `Bacterial Infections[Mesh:noexp]` were tested in v2. They added about 600 records, and a sample of them was almost entirely off-topic. They were removed in v3. `FISH[tiab]` (115k records, mostly about fish) was replaced by the spelled-out FISH phrases.

## How known records were found (added by hand)

- The user supplied no seeds.
- A prior systematic review matching the scope was found: Pammi et al. 2011, PMID 21949139. Its reference list was not returned by `psb neighbors --links refs`, so there is **no external benchmark set**.
- Candidates came from two sources, about 150 screened on title and abstract in total:
  1. A precise title-only pilot (neonate AND sepsis AND molecular words in titles; 68 hits).
  2. Similar and citing neighbours of the pilot includes (top 120).
- 30 records were screened in: 24 from the pilot and 6 from neighbours. Records that were uncertain or had no abstract were left out, including 19279393 (neonatal infections, multiplex PCR, sepsis not stated), 19559305, 19609126, 22556324 and 10685241.
- Held-out validation set: 9 of the 30 records (`psb set split`, fraction 0.3, seed 1). No term was added because of a validation miss.
- **Independence caveat:** 24 of the 30 records came from a title search that uses the same core words as the strategy, and the neighbours are similar to them. So 100% relative recall is optimistic and is **not** an estimate of sensitivity.

## Critic dispositions (added by hand)

The critic was one round of a fresh-context subagent review, given only `packet-1.md`. It is PRESS-structured internal QA, not PRESS peer review.

| Finding | What happened |
|---|---|
| F1: sequencing MeSH and NGS/metagenomic terms | Resolved in v4. |
| F2: commercial platform names | Resolved in v4. |
| F3: bacterial infection wording | Accepted risk. The broad terms were tested and rejected as noise. Specific phrases were added (serious/invasive bacterial infection, suspected infection). |
| F4: baby/babies | Resolved in v4. |
| F5: host gene-expression assays | Accepted risk. They are handled at screening. |
| F6: redundant lines | Kept deliberately. |

## Open risks for the peer reviewer (added by hand)

- The scope was **not confirmed by the user** (they asked not to be consulted). Please check the interpretation of "molecular assay": it currently covers nucleic-acid amplification, hybridisation and sequencing of pathogen DNA/RNA, and excludes protein biomarkers and host transcriptomics.
- Studies that describe only "infection" or "bacterial infection" in newborns, with no sepsis, bacteraemia, blood culture or Sepsis MeSH wording, may be missed. See F3 and the uncertain candidate 19279393; the strategy does retrieve it.
- Studies of mixed paediatric populations that do not mention neonates, newborns or infants in the title, abstract or MeSH would be missed. Screening may also need separable neonatal data.
- There is no external benchmark. Obtaining the included studies of Pammi 2011 and checking them against this strategy is strongly recommended.
- Recall was measured only on development and semi-independent sets drawn from the same pilot, so it overstates true sensitivity.
- This draft needs **PRESS peer review by an information specialist** before use. Other databases (Embase, CINAHL, LILACS, trial registries) and citation searching are outside this deliverable.

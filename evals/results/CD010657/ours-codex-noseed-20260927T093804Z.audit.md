# PubMed search strategy: audit

Generated 2026-09-27T09:47:12+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In children with urinary tract infection, what is the accuracy of DMSA renal scan or ultrasound for detecting vesicoureteral reflux?
- Framework: PIRD
- Scope confirmed by user: yes (User asked to proceed without questions; scope is inferred directly from stated question/eligibility. Work is historically bounded to 2013-01-30. No known relevant articles were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Vesicoureteral reflux | search | The target diagnosis defines the topic and is reliably named/indexed. |
| DMSA renal scan or renal/urinary ultrasound | search | The index tests define the question and are searchable named technologies. |
| Children with urinary tract infection | screen | Age and UTI context can be inconsistently indexed and are verified during screening. |
| Diagnostic evaluation/accuracy | screen | Design and accuracy terminology are variably reported; no study-design block is required. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2013-01-30
- Total records: 2,061
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Vesico-Ureteral Reflux"[Mesh]` | 7,234 |
| 2 | `vesicoureteral reflux[tiab]` | 3,780 |
| 3 | `vesico-ureteral reflux[tiab]` | 1,021 |
| 4 | `vesicoureteric reflux[tiab]` | 819 |
| 5 | `vesico-ureteric reflux[tiab]` | 456 |
| 6 | `VUR[tiab]` | 1,500 |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 9,000 |
| 8 | `"Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh]` | 1,153 |
| 9 | `"Radionuclide Imaging"[Mesh]` | 165,890 |
| 10 | `"Ultrasonography"[Mesh]` | 319,531 |
| 11 | `DMSA[tiab]` | 1,948 |
| 12 | `dimercaptosuccinic acid[tiab]` | 1,492 |
| 13 | `99mTc-DMSA[tiab]` | 295 |
| 14 | `Tc-99m DMSA[tiab]` | 108 |
| 15 | `dimercaptosuccinic acid scintigraph*[tiab]` | 75 |
| 16 | `renal scintigraph*[tiab]` | 1,024 |
| 17 | `renal scan[tiab]` | 579 |
| 18 | `kidney scan[tiab]` | 10 |
| 19 | `ultrasound[tiab]` | 141,762 |
| 20 | `ultrasonograph*[tiab]` | 73,208 |
| 21 | `sonograph*[tiab]` | 41,566 |
| 22 | `renal sonography[tiab]` | 200 |
| 23 | `renal ultrasound[tiab]` | 814 |
| 24 | `urinary ultrasound[tiab]` | 9 |
| 25 | `echograph*[tiab]` | 8,470 |
| 26 | `cystosonograph*[tiab]` | 25 |
| 27 | `voiding urosonograph*[tiab]` | 52 |
| 28 | `reflux sonograph*[tiab]` | 3 |
| 29 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 562,816 |
| 30 | `#7 AND #29` | 2,061 |

### Strategy (single line, for copying into PubMed)

```text
("Vesico-Ureteral Reflux"[Mesh] OR vesicoureteral reflux[tiab] OR vesico-ureteral reflux[tiab] OR vesicoureteric reflux[tiab] OR vesico-ureteric reflux[tiab] OR VUR[tiab]) AND ("Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh] OR "Radionuclide Imaging"[Mesh] OR "Ultrasonography"[Mesh] OR DMSA[tiab] OR dimercaptosuccinic acid[tiab] OR 99mTc-DMSA[tiab] OR Tc-99m DMSA[tiab] OR dimercaptosuccinic acid scintigraph*[tiab] OR renal scintigraph*[tiab] OR renal scan[tiab] OR kidney scan[tiab] OR ultrasound[tiab] OR ultrasonograph*[tiab] OR sonograph*[tiab] OR renal sonography[tiab] OR renal ultrasound[tiab] OR urinary ultrasound[tiab] OR echograph*[tiab] OR cystosonograph*[tiab] OR voiding urosonograph*[tiab] OR reflux sonograph*[tiab]) AND 1800/01/01:2013/01/30[Date - Entry]
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| reflux | 562,816 | 0 |
| test | 9,000 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,061 | initial | none | Initial recall-first two-block strategy: controlled vocabulary plus broad DMSA and urinary ultrasound text words; population and diagnostic evaluation screened, not AND-ed. |
| 2 | 2,061 | test: +1 / -1 | none | Quoted the Ultrasonography MeSH heading explicitly after PubMed reported ATM on the unquoted heading; retained all vocabulary and structure. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (same-context critic: no separate fresh-context reviewer was available in this run.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 419 NCBI requests logged (166 from cache); strategy sha256 4781a5b706a0._

## Rationale

Vesicoureteral reflux and the index tests were searched as the two required searchable topic concepts. The population context (children with UTI) and diagnostic-evaluation eligibility were left for screening because they may be missing or inconsistently reported in indexing and abstracts. The target condition uses the exploded Vesico-Ureteral Reflux heading and its common spelling variants plus VUR. The test block uses the DMSA-specific heading, the broader Radionuclide Imaging heading to cover older or less specific indexing, and Ultrasonography, alongside DMSA, scan, scintigraphy, ultrasound, sonography, echography, cystosonography, and voiding urosonography wording. No study-design, age, language, or publication-date restriction was used. The copied query in `final_strategy.txt` adds the entry-date bound required to reproduce the requested historical cutoff when run in today's PubMed; this is a simulation bound, not a review eligibility restriction.

## How known records were found

No articles were supplied. PubMed searches through the skill workflow identified candidate prior reviews; abstracts were checked, and the references of the 2005 systematic review on further investigation of confirmed UTI in children were used as a candidate source. Fifty cited records were screened by title/abstract; five met the stated criteria and were added to the development set. A precise PubMed pilot sample was also screened, contributing one additional relevant record. Six development records were retained in total. No records were held out, and no review's included-study list was available as a benchmark set. The broader review and candidate references were not treated as confirmed relevant without screening.

## Critic dispositions

Round 1 was a same-context PRESS-structured internal critique because a fresh-context reviewer was unavailable. All six domains passed and there were no findings to disposition. This is automated internal QA, not independent PRESS peer review.

## Open risks for the peer reviewer

The six retained records are a small development set drawn from a limited candidate pool; the reported 100% relative recall is not independent validation or an estimate of sensitivity. The broad Radionuclide Imaging heading and general ultrasound/sonography terms may retrieve records where imaging is not the eligible index test, so screening remains necessary. A human information specialist should check the coverage of older DMSA terminology, the boundary between renal ultrasound and reflux sonography, and the historical entry-date bound before using the strategy.

# PubMed search strategy: audit

Generated 2026-09-27T14:44:35+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In patients with rotator cuff tears, is cellular therapy (e.g. mesenchymal stem cells, bone marrow aspirate, platelet-rich plasma) beneficial compared with controls for healing and clinical outcomes?
- Framework: PICO
- Scope confirmed by user: no (User requested no clarification and asked us to proceed. No known articles supplied. Scope decisions: intervention effectiveness PICO; search only rotator cuff and cellular biologic augmentation; comparator, outcome, and comparative human design screened. PRP retained because explicitly included in question. Publication cutoff set to 2020-05-15; no language, study design, or other limits. No web search; only PubMed/MeSH via psb.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Rotator cuff tear or repair | search | Defines the patient condition and surgical context; both tear and repair terminology may identify eligible studies. |
| Cellular therapy or biologic augmentation | search | Defines the intervention; includes MSCs, bone marrow aspirate/concentrate, PRP, and adipose- or tendon-derived cells as specified in the question. |
| Control or standard repair; comparative human study | screen | Comparative design and human setting can be inconsistently indexed or described; screen eligibility. |
| Healing/retear, pain, or function | screen | Outcomes are inconsistently reported in titles, abstracts, and indexing; do not AND an outcome block. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2020-05-15
- Total records: 583 (585 before limits)
- Limits and filters: `("1800/01/01"[dp] : "2020/05/15"[dp])` (Publication date cutoff requested by the user: include literature published through 2020-05-15. The protocol also sets the historical PubMed entry-date bound.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Rotator Cuff Injuries"[Mesh]` | 6,021 |
| 2 | `"Rotator cuff disease"[tiab]` | 500 |
| 3 | `"rotator cuff diseases"[tiab]` | 21 |
| 4 | `"rotator cuff syndrome"[tiab]` | 89 |
| 5 | `"rotator cuff syndromes"[tiab]` | 4 |
| 6 | `"rotator cuff lesion"[tiab]` | 66 |
| 7 | `"rotator cuff lesions"[tiab]` | 218 |
| 8 | `"rotator cuff tendinopathy"[tiab]` | 258 |
| 9 | `"rotator cuff tendinopathies"[tiab]` | 20 |
| 10 | `"rotator cuff pathology"[tiab]` | 347 |
| 11 | `"Rotator Cuff"[Mesh]` | 6,661 |
| 12 | `"rotator cuff"[tiab]` | 11,564 |
| 13 | `"rotator cuff tear"[tiab]` | 2,632 |
| 14 | `"rotator cuff tears"[tiab]` | 3,703 |
| 15 | `"rotator cuff repair"[tiab]` | 2,813 |
| 16 | `"rotator cuff repairs"[tiab]` | 519 |
| 17 | `"cuff tear"[tiab]` | 2,988 |
| 18 | `"cuff tears"[tiab]` | 3,815 |
| 19 | `"cuff repair"[tiab]` | 2,913 |
| 20 | `"cuff repairs"[tiab]` | 545 |
| 21 | `supraspinatus[tiab]` | 3,580 |
| 22 | `infraspinatus[tiab]` | 2,148 |
| 23 | `subscapularis[tiab]` | 1,974 |
| 24 | `"full thickness tear"[tiab]` | 309 |
| 25 | `"full-thickness tear"[tiab]` | 309 |
| 26 | `"partial thickness tear"[tiab]` | 142 |
| 27 | `"partial-thickness tear"[tiab]` | 142 |
| 28 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27` | 15,716 |
| 29 | `"Platelet-Rich Plasma"[Mesh]` | 4,666 |
| 30 | `"Mesenchymal Stem Cells"[Mesh]` | 39,771 |
| 31 | `"Stem Cells"[Mesh]` | 223,593 |
| 32 | `"Bone Marrow Cells"[Mesh:noexp]` | 56,255 |
| 33 | `"Cell- and Tissue-Based Therapy"[Mesh:noexp]` | 7,078 |
| 34 | `"Cell Transplantation"[Mesh]` | 101,105 |
| 35 | `"Mesenchymal Stem Cell Transplantation"[Mesh]` | 12,417 |
| 36 | `"Tissue Engineering"[Mesh]` | 36,603 |
| 37 | `"platelet-rich plasma"[tiab]` | 9,974 |
| 38 | `"platelet rich plasma"[tiab]` | 9,974 |
| 39 | `PRP[tiab]` | 15,823 |
| 40 | `"platelet-rich fibrin"[tiab]` | 1,215 |
| 41 | `"platelet rich fibrin"[tiab]` | 1,215 |
| 42 | `"platelet-rich fibrin matrix"[tiab]` | 59 |
| 43 | `"platelet rich fibrin matrix"[tiab]` | 59 |
| 44 | `"platelet-rich plasma fibrin matrix"[tiab]` | 3 |
| 45 | `"platelet-rich fibrin gel"[tiab]` | 11 |
| 46 | `"leukocyte-rich platelet-rich fibrin"[tiab]` | 0 |
| 47 | `"platelet-leukocyte membrane"[tiab]` | 2 |
| 48 | `PRFM[tiab]` | 48 |
| 49 | `L-PRF[tiab]` | 124 |
| 50 | `"autologous conditioned plasma"[tiab]` | 59 |
| 51 | `"autologous platelet concentrate"[tiab]` | 100 |
| 52 | `"platelet lysate"[tiab]` | 690 |
| 53 | `"platelet gel"[tiab]` | 277 |
| 54 | `"mesenchymal stem cell"[tiab]` | 10,072 |
| 55 | `"mesenchymal stem cells"[tiab]` | 40,152 |
| 56 | `"mesenchymal stromal cell"[tiab]` | 1,381 |
| 57 | `"mesenchymal stromal cells"[tiab]` | 6,429 |
| 58 | `"stem cell"[tiab]` | 158,551 |
| 59 | `"stem cells"[tiab]` | 173,411 |
| 60 | `"stem cell*"[tiab]` | 264,732 |
| 61 | `MSC[tiab]` | 18,591 |
| 62 | `MSCs[tiab]` | 24,587 |
| 63 | `"bone marrow aspirate"[tiab]` | 2,375 |
| 64 | `"bone marrow concentrate"[tiab]` | 146 |
| 65 | `"bone marrow aspirate concentrate"[tiab]` | 186 |
| 66 | `"bone marrow-derived cell"[tiab]` | 347 |
| 67 | `"bone marrow derived cell"[tiab]` | 347 |
| 68 | `BMAC[tiab]` | 175 |
| 69 | `BMC[tiab]` | 6,609 |
| 70 | `"adipose-derived stem cell"[tiab]` | 741 |
| 71 | `"adipose derived stem cell"[tiab]` | 741 |
| 72 | `"adipose-derived cell"[tiab]` | 22 |
| 73 | `"adipose derived cell"[tiab]` | 22 |
| 74 | `"stromal vascular fraction"[tiab]` | 1,216 |
| 75 | `"tendon-derived stem cell"[tiab]` | 10 |
| 76 | `"tendon derived stem cell"[tiab]` | 10 |
| 77 | `"tendon stem cell"[tiab]` | 20 |
| 78 | `"tendon progenitor cell"[tiab]` | 10 |
| 79 | `"biologic augmentation"[tiab]` | 76 |
| 80 | `"biological augmentation"[tiab]` | 121 |
| 81 | `"bone marrow stimulation"[tiab]` | 236 |
| 82 | `"marrow stimulation"[tiab]` | 389 |
| 83 | `"marrow venting"[tiab]` | 2 |
| 84 | `microfracture[tiab]` | 1,318 |
| 85 | `#29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84` | 477,309 |
| 86 | `#28 AND #85` | 585 |
| 87 | `#86 AND ("1800/01/01"[dp] : "2020/05/15"[dp])` | 583 |

### Strategy (single line, for copying into PubMed)

```text
(("Rotator Cuff Injuries"[Mesh] OR "Rotator cuff disease"[tiab] OR "rotator cuff diseases"[tiab] OR "rotator cuff syndrome"[tiab] OR "rotator cuff syndromes"[tiab] OR "rotator cuff lesion"[tiab] OR "rotator cuff lesions"[tiab] OR "rotator cuff tendinopathy"[tiab] OR "rotator cuff tendinopathies"[tiab] OR "rotator cuff pathology"[tiab] OR "Rotator Cuff"[Mesh] OR "rotator cuff"[tiab] OR "rotator cuff tear"[tiab] OR "rotator cuff tears"[tiab] OR "rotator cuff repair"[tiab] OR "rotator cuff repairs"[tiab] OR "cuff tear"[tiab] OR "cuff tears"[tiab] OR "cuff repair"[tiab] OR "cuff repairs"[tiab] OR supraspinatus[tiab] OR infraspinatus[tiab] OR subscapularis[tiab] OR "full thickness tear"[tiab] OR "full-thickness tear"[tiab] OR "partial thickness tear"[tiab] OR "partial-thickness tear"[tiab]) AND ("Platelet-Rich Plasma"[Mesh] OR "Mesenchymal Stem Cells"[Mesh] OR "Stem Cells"[Mesh] OR "Bone Marrow Cells"[Mesh:noexp] OR "Cell- and Tissue-Based Therapy"[Mesh:noexp] OR "Cell Transplantation"[Mesh] OR "Mesenchymal Stem Cell Transplantation"[Mesh] OR "Tissue Engineering"[Mesh] OR "platelet-rich plasma"[tiab] OR "platelet rich plasma"[tiab] OR PRP[tiab] OR "platelet-rich fibrin"[tiab] OR "platelet rich fibrin"[tiab] OR "platelet-rich fibrin matrix"[tiab] OR "platelet rich fibrin matrix"[tiab] OR "platelet-rich plasma fibrin matrix"[tiab] OR "platelet-rich fibrin gel"[tiab] OR "leukocyte-rich platelet-rich fibrin"[tiab] OR "platelet-leukocyte membrane"[tiab] OR PRFM[tiab] OR L-PRF[tiab] OR "autologous conditioned plasma"[tiab] OR "autologous platelet concentrate"[tiab] OR "platelet lysate"[tiab] OR "platelet gel"[tiab] OR "mesenchymal stem cell"[tiab] OR "mesenchymal stem cells"[tiab] OR "mesenchymal stromal cell"[tiab] OR "mesenchymal stromal cells"[tiab] OR "stem cell"[tiab] OR "stem cells"[tiab] OR "stem cell*"[tiab] OR MSC[tiab] OR MSCs[tiab] OR "bone marrow aspirate"[tiab] OR "bone marrow concentrate"[tiab] OR "bone marrow aspirate concentrate"[tiab] OR "bone marrow-derived cell"[tiab] OR "bone marrow derived cell"[tiab] OR BMAC[tiab] OR BMC[tiab] OR "adipose-derived stem cell"[tiab] OR "adipose derived stem cell"[tiab] OR "adipose-derived cell"[tiab] OR "adipose derived cell"[tiab] OR "stromal vascular fraction"[tiab] OR "tendon-derived stem cell"[tiab] OR "tendon derived stem cell"[tiab] OR "tendon stem cell"[tiab] OR "tendon progenitor cell"[tiab] OR "biologic augmentation"[tiab] OR "biological augmentation"[tiab] OR "bone marrow stimulation"[tiab] OR "marrow stimulation"[tiab] OR "marrow venting"[tiab] OR microfracture[tiab])) AND (("1800/01/01"[dp] : "2020/05/15"[dp]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 19 | 19 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| rotator_cuff | 477,309 | 0 |
| cellular_therapy | 15,716 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 581 | initial | none | Initial recall-first draft with topic blocks, date cutoff and broad vocabulary. |
| 2 | 583 | rotator_cuff: +9 / -0; cellular_therapy: +1 / -0 | none | Addressed critic findings: added broader rotator cuff disease/lesion/tendinopathy text variants and the targeted Bone Marrow Cells MeSH heading (unexploded to avoid unrelated hematologic child headings). |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 2 findings; F1 should-fix open, F2 should-fix open
- Round 2 on version 2: 2 findings; F1 should-fix resolved, F2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 953 NCBI requests logged (368 from cache); strategy sha256 c1d2732ffe3e._

## Rationale

The question is intervention effectiveness, so the strategy searches only the rotator cuff condition/repair concept AND the biologic intervention concept. Comparative design, control, human study status, and healing/pain/function outcomes are screening criteria because indexing and abstract wording can be inconsistent. The condition block combines the MeSH headings Rotator Cuff Injuries and Rotator Cuff with tear, repair, muscle, disease, lesion, syndrome, and tendinopathy wording. Broader disease terms were added after internal critique to catch eligible tear/repair reports that use less specific wording; their scope is resolved at screening. The intervention block combines Platelet-Rich Plasma, Mesenchymal Stem Cells, Stem Cells, Bone Marrow Cells, Cell- and Tissue-Based Therapy, cell transplantation, mesenchymal stem cell transplantation, and tissue engineering headings with PRP/PRF, BMAC/BMC, MSC, adipose- and tendon-derived cell, and marrow-augmentation terms. Cell- and Tissue-Based Therapy and Bone Marrow Cells are searched without explosion: the first has a broad tissue-transplantation branch, and the second has hematologic cell subheadings outside this intervention scope. Separate cell-transplantation and mesenchymal stem cell headings remain included. No language, study-design, human-only, outcome, or comparator filter was added. The only publication limit is the requested cutoff through 2020-05-15; the protocol also constrains PubMed entry dates to records available by that date.

## How known records were found

No user-supplied seed records were available. PubMed pilots identified topic-specific systematic reviews and candidate comparative reports; abstracts of 31 selected primary clinical reports were screened, with 27 judged eligible and entered as the discovered relevant set. Four selected candidates were excluded for lacking a comparative control, lacking the eligible tear/repair population, or being uncontrolled. PubMed's references link for candidate reviews returned no records, so an included-study benchmark set could not be assembled. The 27 discovered records were split before term mining into 19 development records and 8 held-out validation records. The validation set was held out from vocabulary mining but comes from the same pilot-discovery pool, so it is semi-independent rather than an external validation. Both sets were retrieved in full by version 2. Recall against known records is not an estimate of absolute sensitivity.

## Critic dispositions

Two fresh-context PRESS-structured internal critique rounds were completed. Round 1 suggested broader rotator cuff disease/lesion wording and a targeted bone marrow cell heading. Both were added in version 2, and evaluation showed no losses from either known set. Round 2 marked both findings resolved and found no remaining must-fix issues. This automated internal critique is not an information specialist's PRESS peer review.

## Open risks for the peer reviewer

The known-record set is dominated by PRP/platelet-product comparative studies, with limited empirical checking of BMAC and no discovered eligible comparative records for adipose- or tendon-derived cells. Those intervention families are represented by vocabulary and MeSH, but their recall is not independently demonstrated. Generic stem-cell, cell-transplantation, tissue-engineering, PRP, and marrow stimulation/microfracture wording is intentionally broad and will retrieve preclinical studies, reviews, and non-eligible shoulder conditions for screening. The question explicitly includes PRP; a reviewer should confirm whether it is intended to remain grouped with cellular therapies and whether marrow stimulation counts as biologic augmentation. The proposed scope was not personally confirmed because the user explicitly asked us not to pause for questions; the documented assumptions were applied. As required for PRISMA-S item 12, report status is: internal PRESS-structured critic only; PRESS peer review pending.
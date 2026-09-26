# PubMed search strategy: audit

Generated 2026-09-26T20:40:29+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO (prognostic factor / exposure)
- Scope confirmed by user: yes (User could not answer questions during the run and asked not to wait. Assumptions: (1) depth standard; (2) no language, date or design limits requested; search restricted by as_of 2017/05/06 only to reproduce the search date of the harness (not a review limit); (3) scope confirmed by assistant without user pause; (4) ambiguity resolved: SVD is the exposure/prognostic factor and dementia/cognition the outcome (not a population of people with dementia); outcome AND-ed because it defines the topic, with broad cognition wording, verified by ablation; (5) cohort design and community setting are handled at screening, not searched; (6) no seeds supplied - known records built from prior systematic reviews and screened pilot searches.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and its MRI markers (white matter hyperintensities/leukoaraiosis, lacunar/silent infarcts, cerebral microbleeds, enlarged perivascular spaces, vascular brain injury) | search | the exposure / prognostic factor; every relevant record must involve it; reliably named and indexed (Cerebral Small Vessel Diseases, Leukoaraiosis, Stroke Lacunar, Cerebral Hemorrhage, White Matter) |
| Dementia, Alzheimer disease, cognitive decline or impairment | search | the outcome defines the topic (SVD literature is huge and covers stroke, gait, mood, mortality); dementia/cognition is reliably named in abstracts and well indexed (Dementia, Cognition Disorders, Cognition). Built broadly (any cognition wording) and checked by ablation. |
| Population-based / community-dwelling longitudinal cohort with follow-up | screen | study design and setting are eligibility properties; inconsistently described in abstracts; no validated cohort filter required for a recall-first search |
| MRI imaging modality | screen | MRI is implied by the markers; many records on WMH/infarcts do not name MRI; handled within svd block wording |
| Incident/risk/prospective wording | screen | outcome timing and risk measures are judged at screening |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-26
- Records added to PubMed up to: 2017/05/06
- Total records: 12,495 (13,128 before limits)
- Limits and filters: `NOT ("Animals"[Mesh] NOT "Humans"[Mesh])` (the question concerns human population-based cohorts; standard exclusion of records indexed as animal-only (keeps unindexed and human records))

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 |
| 3 | `"Leukoencephalopathies"[Mesh:noexp]` | 1,458 |
| 4 | `"Cerebrovascular Disorders"[Mesh:noexp] AND ("Magnetic Resonance Imaging"[Mesh] OR MRI[tiab] OR "magnetic resonance"[tiab] OR neuroimaging[tiab] OR "Neuroimaging"[Mesh])` | 6,553 |
| 5 | `"Brain Infarction"[Mesh] AND ("Magnetic Resonance Imaging"[Mesh] OR MRI[tiab] OR "magnetic resonance"[tiab] OR neuroimaging[tiab] OR "Neuroimaging"[Mesh])` | 11,738 |
| 6 | `"Cerebral Hemorrhage"[Mesh] AND ("Magnetic Resonance Imaging"[Mesh] OR MRI[tiab] OR "magnetic resonance"[tiab] OR neuroimaging[tiab] OR "Neuroimaging"[Mesh])` | 6,939 |
| 7 | `"Cerebral Amyloid Angiopathy"[Mesh]` | 1,516 |
| 8 | `"small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small-vessel disease"[tiab] OR "small-vessel diseases"[tiab] OR SVD[tiab] OR CSVD[tiab] OR "cerebral small vessel*"[tiab] OR "brain small vessel*"[tiab] OR "small vessel ischemic"[tiab] OR "small vessel ischaemic"[tiab] OR "small vessel cerebrovascular"[tiab] OR "small vessel pathology"[tiab] OR "small vessel change*"[tiab] OR "small-vessel ischemic"[tiab] OR "small-vessel ischaemic"[tiab]` | 4,000 |
| 9 | `microangiopath*[tiab] OR "microvascular disease*"[tiab] OR "microvascular brain"[tiab] OR "cerebral microvascular"[tiab] OR arteriolosclerosis[tiab]` | 11,058 |
| 10 | `"white matter hyperintens*"[tiab] OR "periventricular hyperintens*"[tiab] OR "subcortical hyperintens*"[tiab] OR "white matter signal hyperintens*"[tiab] OR hyperintensities[tiab] OR hyperintensity[tiab] OR "hyperintense lesion*"[tiab] OR WMH[tiab] OR WMHs[tiab]` | 7,946 |
| 11 | `"white matter lesion"[tiab] OR "white matter lesions"[tiab] OR "white matter change"[tiab] OR "white matter changes"[tiab] OR "white matter disease"[tiab] OR "white matter damage"[tiab] OR "white matter abnormalities"[tiab] OR "white matter abnormality"[tiab] OR "white matter grade"[tiab] OR "white matter hypodensity"[tiab] OR "white matter hypodensities"[tiab] OR WML[tiab] OR WMLs[tiab]` | 8,910 |
| 12 | `leukoaraio*[tiab] OR leucoaraio*[tiab] OR "leuko-araiosis"[tiab] OR binswanger*[tiab] OR "subcortical arteriosclerotic encephalopathy"[tiab] OR "ischemic leukoencephalopathy"[tiab] OR "vascular leukoencephalopathy"[tiab]` | 1,650 |
| 13 | `lacune*[tiab] OR lacunar*[tiab] OR lacunae[tiab]` | 8,458 |
| 14 | `"silent infarct*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent stroke*"[tiab] OR "covert infarct*"[tiab] OR "covert brain infarct*"[tiab] OR "covert stroke*"[tiab] OR "covert cerebrovascular"[tiab] OR "subclinical infarct*"[tiab] OR "subclinical brain infarct*"[tiab] OR "subclinical cerebral infarct*"[tiab] OR "subclinical stroke*"[tiab] OR "subclinical cerebrovascular"[tiab] OR "asymptomatic infarct*"[tiab] OR "asymptomatic brain infarct*"[tiab]` | 1,110 |
| 15 | `"brain infarct*"[tiab] OR "cerebral infarct*"[tiab] OR "MRI-defined infarct*"[tiab] OR "MRI-defined brain infarct*"[tiab] OR "MRI infarct*"[tiab] OR "subcortical infarct*"[tiab] OR microinfarct*[tiab] OR "micro-infarcts"[tiab] OR "micro infarcts"[tiab]` | 20,113 |
| 16 | `microbleed*[tiab] OR "micro-bleeds"[tiab] OR "micro bleeds"[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "micro-hemorrhages"[tiab] OR "micro-haemorrhages"[tiab] OR ((CMB[tiab] OR CMBs[tiab]) AND (cerebral[tiab] OR brain[tiab] OR MRI[tiab]))` | 2,135 |
| 17 | `"perivascular space"[tiab] OR "perivascular spaces"[tiab] OR "Virchow-Robin"[tiab] OR EPVS[tiab] OR (PVS[tiab] AND (perivascular[tiab] OR MRI[tiab] OR "magnetic resonance"[tiab]))` | 2,150 |
| 18 | `"vascular brain injury"[tiab] OR "vascular brain lesions"[tiab] OR "vascular brain damage"[tiab] OR "cerebrovascular lesions"[tiab] OR "subcortical vascular"[tiab] OR "subcortical ischemic"[tiab] OR "subcortical ischaemic"[tiab] OR "cerebral amyloid angiopathy"[tiab]` | 3,427 |
| 19 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18` | 84,669 |
| 20 | `"Dementia"[Mesh]` | 145,526 |
| 21 | `"Cognitive Dysfunction"[Mesh]` | 8,211 |
| 22 | `"Cognition Disorders"[Mesh]` | 80,254 |
| 23 | `"Cognition"[Mesh]` | 138,866 |
| 24 | `"Memory Disorders"[Mesh]` | 26,825 |
| 25 | `"Neuropsychological Tests"[Mesh]` | 161,667 |
| 26 | `dementia*[tiab] OR alzheimer*[tiab]` | 170,489 |
| 27 | `cognit*[tiab] OR neurocognit*[tiab] OR MCI[tiab]` | 312,963 |
| 28 | `memory[tiab] OR "executive function"[tiab] OR "executive functions"[tiab] OR "executive functioning"[tiab] OR "processing speed"[tiab] OR "information processing"[tiab] OR "psychomotor speed"[tiab] OR neuropsycholog*[tiab] OR "mini-mental"[tiab] OR MMSE[tiab] OR "intellectual decline"[tiab] OR "mental decline"[tiab]` | 264,782 |
| 29 | `#20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 782,207 |
| 30 | `#19 AND #29` | 13,128 |
| 31 | `#30 NOT ("Animals"[Mesh] NOT "Humans"[Mesh])` | 12,495 |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Leukoencephalopathies"[Mesh:noexp] OR ("Cerebrovascular Disorders"[Mesh:noexp] AND ("Magnetic Resonance Imaging"[Mesh] OR MRI[tiab] OR "magnetic resonance"[tiab] OR neuroimaging[tiab] OR "Neuroimaging"[Mesh])) OR ("Brain Infarction"[Mesh] AND ("Magnetic Resonance Imaging"[Mesh] OR MRI[tiab] OR "magnetic resonance"[tiab] OR neuroimaging[tiab] OR "Neuroimaging"[Mesh])) OR ("Cerebral Hemorrhage"[Mesh] AND ("Magnetic Resonance Imaging"[Mesh] OR MRI[tiab] OR "magnetic resonance"[tiab] OR neuroimaging[tiab] OR "Neuroimaging"[Mesh])) OR "Cerebral Amyloid Angiopathy"[Mesh] OR ("small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small-vessel disease"[tiab] OR "small-vessel diseases"[tiab] OR SVD[tiab] OR CSVD[tiab] OR "cerebral small vessel*"[tiab] OR "brain small vessel*"[tiab] OR "small vessel ischemic"[tiab] OR "small vessel ischaemic"[tiab] OR "small vessel cerebrovascular"[tiab] OR "small vessel pathology"[tiab] OR "small vessel change*"[tiab] OR "small-vessel ischemic"[tiab] OR "small-vessel ischaemic"[tiab]) OR (microangiopath*[tiab] OR "microvascular disease*"[tiab] OR "microvascular brain"[tiab] OR "cerebral microvascular"[tiab] OR arteriolosclerosis[tiab]) OR ("white matter hyperintens*"[tiab] OR "periventricular hyperintens*"[tiab] OR "subcortical hyperintens*"[tiab] OR "white matter signal hyperintens*"[tiab] OR hyperintensities[tiab] OR hyperintensity[tiab] OR "hyperintense lesion*"[tiab] OR WMH[tiab] OR WMHs[tiab]) OR ("white matter lesion"[tiab] OR "white matter lesions"[tiab] OR "white matter change"[tiab] OR "white matter changes"[tiab] OR "white matter disease"[tiab] OR "white matter damage"[tiab] OR "white matter abnormalities"[tiab] OR "white matter abnormality"[tiab] OR "white matter grade"[tiab] OR "white matter hypodensity"[tiab] OR "white matter hypodensities"[tiab] OR WML[tiab] OR WMLs[tiab]) OR (leukoaraio*[tiab] OR leucoaraio*[tiab] OR "leuko-araiosis"[tiab] OR binswanger*[tiab] OR "subcortical arteriosclerotic encephalopathy"[tiab] OR "ischemic leukoencephalopathy"[tiab] OR "vascular leukoencephalopathy"[tiab]) OR (lacune*[tiab] OR lacunar*[tiab] OR lacunae[tiab]) OR ("silent infarct*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent stroke*"[tiab] OR "covert infarct*"[tiab] OR "covert brain infarct*"[tiab] OR "covert stroke*"[tiab] OR "covert cerebrovascular"[tiab] OR "subclinical infarct*"[tiab] OR "subclinical brain infarct*"[tiab] OR "subclinical cerebral infarct*"[tiab] OR "subclinical stroke*"[tiab] OR "subclinical cerebrovascular"[tiab] OR "asymptomatic infarct*"[tiab] OR "asymptomatic brain infarct*"[tiab]) OR ("brain infarct*"[tiab] OR "cerebral infarct*"[tiab] OR "MRI-defined infarct*"[tiab] OR "MRI-defined brain infarct*"[tiab] OR "MRI infarct*"[tiab] OR "subcortical infarct*"[tiab] OR microinfarct*[tiab] OR "micro-infarcts"[tiab] OR "micro infarcts"[tiab]) OR (microbleed*[tiab] OR "micro-bleeds"[tiab] OR "micro bleeds"[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "micro-hemorrhages"[tiab] OR "micro-haemorrhages"[tiab] OR ((CMB[tiab] OR CMBs[tiab]) AND (cerebral[tiab] OR brain[tiab] OR MRI[tiab]))) OR ("perivascular space"[tiab] OR "perivascular spaces"[tiab] OR "Virchow-Robin"[tiab] OR EPVS[tiab] OR (PVS[tiab] AND (perivascular[tiab] OR MRI[tiab] OR "magnetic resonance"[tiab]))) OR ("vascular brain injury"[tiab] OR "vascular brain lesions"[tiab] OR "vascular brain damage"[tiab] OR "cerebrovascular lesions"[tiab] OR "subcortical vascular"[tiab] OR "subcortical ischemic"[tiab] OR "subcortical ischaemic"[tiab] OR "cerebral amyloid angiopathy"[tiab])) AND ("Dementia"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] OR "Memory Disorders"[Mesh] OR "Neuropsychological Tests"[Mesh] OR (dementia*[tiab] OR alzheimer*[tiab]) OR (cognit*[tiab] OR neurocognit*[tiab] OR MCI[tiab]) OR (memory[tiab] OR "executive function"[tiab] OR "executive functions"[tiab] OR "executive functioning"[tiab] OR "processing speed"[tiab] OR "information processing"[tiab] OR "psychomotor speed"[tiab] OR neuropsycholog*[tiab] OR "mini-mental"[tiab] OR MMSE[tiab] OR "intellectual decline"[tiab] OR "mental decline"[tiab]))) NOT (("Animals"[Mesh] NOT "Humans"[Mesh]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 10 | 10 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 10 | 10 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| svd | 782,207 | 0 |
| cognition | 84,669 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 19,500 | initial | none | first draft: svd AND cognition, broad MeSH + tiab |
| 2 | 12,044 | svd: +9 / -9 | none | noise cuts: MRI-context for Cerebrovascular Disorders/Brain Infarction/Cerebral Hemorrhage MeSH; narrowed hyperintens*; dropped WMC and leukoencephalopath* text; fixed short-stem truncation; animal-only exclusion |
| 3 | 12,044 | svd: +1 / -1 | none | removed zero-hit phrase ischaemic leukoencephalopathy |
| 4 | 12,478 | svd: +6 / -6 | none | critic round 1: F1 infarct variants via phrase truncation, F2 quoted microvascular disease*, F3 PVS and CMB restricted to brain/MRI context, F6 duplicate removed |
| 5 | 12,495 | svd: +3 / -3 | none | critic round 2: small vessel phrase variants, leuko-araiosis, quoted Virchow-Robin |
| 6 | 12,495 | limits/combination | none | final counts, run live |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 6 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk, F5 document accepted-risk, F6 document resolved
- Round 2 on version 4: 4 findings; R2-F1 should-fix rejected, R2-F2 should-fix resolved, R2-F3 document accepted-risk, R2-F4 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 514 NCBI requests logged (205 from cache); strategy sha256 0d9bfacbdcc4._

## Rationale (added by hand)

- **Searched concepts.** `svd` (exposure/prognostic factor) AND `cognition` (outcome). The outcome is AND-ed because it defines the topic: SVD markers are studied against many outcomes (stroke, gait, mood, mortality), and dementia/cognition wording is reliably present in titles, abstracts and MeSH. It is built very broadly (any cognition, memory, executive or neuropsychological wording) to protect recall. Ablation shows neither block costs any known record.
- **Screened, not searched.** Population-based/community-dwelling setting, prospective/longitudinal design with follow-up, incident outcomes, and MRI as modality. None is reliably named in abstracts, and no validated cohort filter is needed for a recall-first search.
- **MeSH decisions.** Cerebral Small Vessel Diseases (exploded; introduced 2012, which is why pre-2012 indexing is caught via text words and MRI-restricted Cerebrovascular Disorders[Mesh:noexp]). Leukoaraiosis and Cerebral Amyloid Angiopathy are exploded. Leukoencephalopathies is `:noexp` because its narrower headings are leukodystrophies and PML. Brain Infarction, Cerebral Hemorrhage and Cerebrovascular Disorders (noexp) are ANDed with MRI/neuroimaging wording inside the block. Unrestricted, they added about 7,000 acute-stroke and haemorrhage records (v1 to v2) and no known record depended on them. White Matter[Mesh] was tested and rejected (see R2-F1).
- **Text words.** Each marker has its own line (WMH, WML, leukoaraiosis, lacunes, silent/covert/subclinical infarcts, brain/cerebral infarcts, microbleeds, perivascular spaces, vascular brain injury). Ambiguous acronyms (PVS, CMB) need brain/MRI context. WMC was dropped because it matched "working memory capacity". Hyphenated short stems (micro-bleed*) were replaced by explicit phrases because PubMed dropped the truncation.
- **Limits.** None on date, language or design. The only restriction is the standard animal-only exclusion. The `as_of` bound of 2017/05/06 reproduces the search date for this run; it is not a review limit.

## How known records were found (added by hand)

- No seeds were supplied.
- **Benchmark (10 records, external).** These came from the reference lists of four prior systematic reviews/meta-analyses (PMIDs 20660506 Debette & Markus 2010, 24814849, 23178504, 25377475). There were 78 references, and 17 were screened on title/abstract. Ten were included: community/population cohorts with baseline MRI SVD markers and follow-up for dementia or cognitive decline. Cross-sectional studies, selected clinic/MCI/stroke samples and non-SVD exposures were excluded. The benchmark was never used for term mining.
- **Relevant (14 records).** These came from two precise pilot searches and from similar-articles of the included records. About 70 candidates were reviewed and about 45 abstracts screened. A 30% random hold-out was split into `validation` (4 records), which was never mined. No validation miss ever occurred, so the validation set stayed held out.
- Uncertain records were left out of all sets. Examples: PROSPER (trial sample), CT-based WML studies, and LADIS (sample selected for white matter changes).

## Critic dispositions (added by hand)

- Round 1: F1 added infarct variants; F2 quoted a phrase; F3 restricted PVS/CMB; F6 removed a duplicate. F4 (White Matter heading) and F5 (breadth of the cognition block) were documented as accepted risks.
- Round 2: R2-F1 White Matter[Mesh] or /pathology was rejected after testing, because it added 507–849 records of DTI/psychiatric noise and no relevant ones. R2-F2 added small-vessel phrase variants. R2-F3 is documented (limited validation). R2-F4 was fixed.
- Both rounds were run by a fresh-context subagent. This is internal PRESS-structured QA, not PRESS peer review.

## Open risks for the peer reviewer (added by hand)

- **Yield is about 12,500 records.** Most of the load comes from the breadth of the cognition block (Neuropsychological Tests[Mesh], memory[tiab], information processing[tiab]) and from the infarct lines. If screening is prohibitive, test dropping those terms against the known sets first. Do not add a cohort design block.
- **Limited validation.** Relative recall is 100% on a 10-record benchmark, 10 development records and a 4-record semi-independent validation set. That is supportive evidence, not sensitivity. The benchmark reviews are mostly WMH/microbleed focused, so lacune- and perivascular-space-only studies are under-represented.
- **Studies whose abstract reports only "MRI findings"/"brain MRI abnormalities",** or only atrophy together with an unnamed vascular component, may be missed if they are not indexed with the SVD headings.
- **CT-defined white matter lesions** are retrieved by the text words, but whether they are eligible (the protocol says MRI marker) is a screening decision for the review team.
- **Recent records** (2016–2017) may not yet be MeSH-indexed and depend on the text words.
- PubMed only. Embase and other sources are needed for a systematic review.

PRISMA-S item 12 (peer review): internal PRESS-structured critic only; PRESS peer review pending.

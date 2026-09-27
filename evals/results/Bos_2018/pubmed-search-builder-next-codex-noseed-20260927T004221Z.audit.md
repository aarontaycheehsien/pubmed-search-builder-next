# PubMed search strategy: audit

Generated 2026-09-27T00:52:41+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: no (User has no known relevant articles and cannot answer questions during this run; proceed with the stated scope without confirmation. Harness publication cutoff: 2017-05-06; no web search and no literature published after this date. No language, age, geography, or study-design limits.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | Exposure defines the review topic and is searchable through MeSH and text words. |
| Population-based or longitudinal community-dwelling cohorts | screen | Population basis and community dwelling status may not be consistently named in titles or abstracts. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | screen | Outcomes can be reported inconsistently; screening this broad outcome avoids losing exposure studies. |
| Prospective cohort or longitudinal observational follow-up | screen | Study design and follow-up labels are inconsistently indexed and will be assessed at screening. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2017-05-06
- Total records: 83,203
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Leukoaraiosis"[Mesh]` | 470 |
| 2 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 |
| 4 | `"Cerebral Infarction"[Mesh]` | 29,744 |
| 5 | `"Cerebral Hemorrhage"[Mesh]` | 31,304 |
| 6 | `"cerebral small vessel disease"[tiab]` | 813 |
| 7 | `"cerebral small-vessel disease"[tiab]` | 813 |
| 8 | `"small vessel disease"[tiab]` | 2,316 |
| 9 | `"small-vessel disease"[tiab]` | 2,316 |
| 10 | `"cerebral microangiopath*"[tiab]` | 150 |
| 11 | `"white matter hyperintens*"[tiab]` | 2,354 |
| 12 | `"white-matter hyperintens*"[tiab]` | 2,354 |
| 13 | `"white matter lesion*"[tiab]` | 4,051 |
| 14 | `"white-matter lesion*"[tiab]` | 4,051 |
| 15 | `"white matter change*"[tiab]` | 1,880 |
| 16 | `leukoaraiosis[tiab]` | 1,008 |
| 17 | `"subcortical ischemic vascular disease"[tiab]` | 60 |
| 18 | `"subcortical ischaemic vascular disease"[tiab]` | 12 |
| 19 | `"subcortical vascular disease"[tiab]` | 35 |
| 20 | `"lacunar infarct*"[tiab]` | 2,251 |
| 21 | `"lacunar lesion*"[tiab]` | 131 |
| 22 | `"silent infarct*"[tiab]` | 311 |
| 23 | `"silent brain infarct*"[tiab]` | 280 |
| 24 | `"covert infarct*"[tiab]` | 4 |
| 25 | `"subclinical infarct*"[tiab]` | 30 |
| 26 | `"brain infarct*"[tiab]` | 3,534 |
| 27 | `"cerebral infarct*"[tiab]` | 15,197 |
| 28 | `"cerebral microbleed*"[tiab]` | 710 |
| 29 | `"brain microbleed*"[tiab]` | 59 |
| 30 | `"microbleed*"[tiab]` | 1,468 |
| 31 | `"cerebral microhemorrhag*"[tiab]` | 62 |
| 32 | `"cerebral microhaemorrhag*"[tiab]` | 4 |
| 33 | `"brain microhemorrhag*"[tiab]` | 15 |
| 34 | `"vascular brain injury"[tiab]` | 73 |
| 35 | `"vascular brain lesions"[tiab]` | 72 |
| 36 | `"vascular brain disease"[tiab]` | 36 |
| 37 | `("white matter"[tiab] AND (WMH[tiab] OR WML[tiab] OR WMSH[tiab]))` | 1,427 |
| 38 | `"periventricular hyperintens*"[tiab]` | 316 |
| 39 | `"subcortical hyperintens*"[tiab]` | 97 |
| 40 | `"white matter signal hyperintens*"[tiab]` | 36 |
| 41 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40` | 83,203 |

### Strategy (single line, for copying into PubMed)

```text
("Leukoaraiosis"[Mesh] OR "Cerebral Small Vessel Diseases"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Infarction"[Mesh] OR "Cerebral Hemorrhage"[Mesh] OR "cerebral small vessel disease"[tiab] OR "cerebral small-vessel disease"[tiab] OR "small vessel disease"[tiab] OR "small-vessel disease"[tiab] OR "cerebral microangiopath*"[tiab] OR "white matter hyperintens*"[tiab] OR "white-matter hyperintens*"[tiab] OR "white matter lesion*"[tiab] OR "white-matter lesion*"[tiab] OR "white matter change*"[tiab] OR leukoaraiosis[tiab] OR "subcortical ischemic vascular disease"[tiab] OR "subcortical ischaemic vascular disease"[tiab] OR "subcortical vascular disease"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar lesion*"[tiab] OR "silent infarct*"[tiab] OR "silent brain infarct*"[tiab] OR "covert infarct*"[tiab] OR "subclinical infarct*"[tiab] OR "brain infarct*"[tiab] OR "cerebral infarct*"[tiab] OR "cerebral microbleed*"[tiab] OR "brain microbleed*"[tiab] OR "microbleed*"[tiab] OR "cerebral microhemorrhag*"[tiab] OR "cerebral microhaemorrhag*"[tiab] OR "brain microhemorrhag*"[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesions"[tiab] OR "vascular brain disease"[tiab] OR ("white matter"[tiab] AND (WMH[tiab] OR WML[tiab] OR WMSH[tiab])) OR "periventricular hyperintens*"[tiab] OR "subcortical hyperintens*"[tiab] OR "white matter signal hyperintens*"[tiab])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 339,695 | initial | none | Initial recall-first one-block PECO strategy. Searched only cerebral small vessel disease and MRI markers; kept population/cohort, dementia/cognitive outcome, and longitudinal design for screening. Used MeSH plus broad marker text variants, with no methodological or language limits; PubMed cutoff 2017-05-06. |
| 2 | 83,019 | csd: +0 / -1 | 15569873 | Removed the very broad Cerebrovascular Disorders MeSH heading after its individual line count dominated retrieval; the specific CSVD and MRI-marker vocabulary remains. Checked whether screened benchmark records are retained. |
| 3 | 83,047 | csd: +1 / -0 | none | Added the specific Leukoaraiosis MeSH descriptor identified on the missed known record by psb terms miss. This retains that record without the very broad Cerebrovascular Disorders heading; the former benchmark is now development-informed, so its recall is not independent. |
| 4 | 83,203 | csd: +3 / -0 | none | Addressed internal critic finding F1 by adding common periventricular, subcortical, and white matter signal hyperintensity wording. Evaluated for benchmark loss and translation problems. |
| 5 | 83,203 | csd: +0 / -1 | none | Removed the zero-yield brain microhaemorrhage spelling variant after its PubMed line count returned no records; no benchmark records were lost. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (Same-context PRESS-structured internal critique; no separate fresh-context reviewer was available.): 1 findings; F1 must-fix open
- Round 2 on version 5 (Same-context PRESS-structured internal critique; no separate fresh-context reviewer was available.): 2 findings; F1 must-fix resolved, F2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 370 NCBI requests logged (217 from cache); strategy sha256 bb63299a4414._

## Rationale

Only cerebral small vessel disease and its MRI markers are searched. The strategy includes exploded `Cerebral Small Vessel Diseases`, `Leukoaraiosis`, `Stroke, Lacunar`, `Cerebral Infarction`, and `Cerebral Hemorrhage` MeSH headings, plus title/abstract wording for white matter hyperintensities and lesions, lacunar or silent infarcts, microbleeds, and vascular brain injury. Cerebrovascular disorders was considered but removed because its heading was very broad; `Leukoaraiosis` was added after a miss diagnosis recovered the known Cardiovascular Health Study record. The broad Cerebral Hemorrhage heading was kept as a sensitivity measure for microbleeds that may be indexed under hemorrhage. Population/cohort setting, dementia/cognitive outcomes, and longitudinal design remain screening criteria. The only date restriction is the requested publication cutoff, 2017-05-06; no other limits or filters were applied.

## How known records were found

There were no user-supplied records. A PubMed search for pre-cutoff systematic reviews identified a matching longitudinal white matter hyperintensity review (PMID 20660506). Its 50 cited primary records were screened by title and abstract against the stated cohort, exposure, outcome, and follow-up criteria; eight clearly eligible records were retained as a benchmark. A missed record (PMID 15569873) led to adding its specific Leukoaraiosis MeSH heading, so the benchmark has since informed development and is no longer independent validation. No records were held out. Other review citations and uncertain records were excluded from the known set.

## Critic dispositions

The same-context PRESS-structured internal critique identified a text-word gap for periventricular and subcortical hyperintensities and white matter signal hyperintensity. Those terms were added and retained all eight known records. The broad Cerebral Hemorrhage heading was documented as an accepted risk because it supports sensitivity for cerebral microbleed records without a dedicated MeSH descriptor. The zero-yield `brain microhaemorrhag*` phrase was removed. No fresh-context reviewer was available; this internal critique is not PRESS peer review.

## Open risks for the peer reviewer

The final one-block exposure search is broad (83,203 PubMed records by the as-of bound) because population, outcome, and design are screened rather than required. The benchmark covers community and longitudinal cohort evidence for white matter lesions and infarcts, but gives limited direct validation of the microbleed vocabulary. The selected Cerebral Hemorrhage and Cerebral Infarction headings may retrieve substantial unrelated stroke literature. Scope was not confirmed interactively because the user asked us to proceed without questions. A human information specialist should review marker coverage and the screening burden before the strategy is used.
# PubMed search strategy: audit

Generated 2026-09-27T00:38:49+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without follow-up questions. Assumed broad MRI marker exposure scope includes white matter hyperintensities/leukoaraiosis, lacunes/silent infarcts, cerebral microbleeds, and vascular brain injury. Outcome, cohort/community setting, and longitudinal design are screening criteria, not AND blocks. Search and eligible literature are bounded through 2017-05-06 per harness; no other limits.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure is central to every eligible record and is searchable through established disease and MRI-marker vocabulary. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | screen | Outcomes can be inconsistently reported in titles and abstracts; screen after retrieving exposure records. |
| Community-dwelling or population-based cohort participants | screen | Setting and sampling frame are often only clear in full text and should not narrow recall. |
| Prospective or longitudinal observational follow-up | screen | Study design labels are inconsistently indexed; assess eligibility during screening. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2017-05-06
- Total records: 91,025 (91,189 before limits)
- Limits and filters: `1800/01/01:2017/05/06[dp]` (The task specifies an information cutoff of 2017-05-06; restrict publication dates through that day.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 |
| 4 | `"Cerebral Infarction"[Mesh]` | 29,744 |
| 5 | `"Brain Infarction"[Mesh]` | 34,827 |
| 6 | `"Cerebral Hemorrhage"[Mesh]` | 31,304 |
| 7 | `"White Matter"[Mesh]` | 4,280 |
| 8 | `"cerebral small vessel disease"[tiab]` | 813 |
| 9 | `"small vessel disease"[tiab]` | 2,316 |
| 10 | `"small-vessel disease"[tiab]` | 2,316 |
| 11 | `"cerebral microangiopath*"[tiab]` | 150 |
| 12 | `"small vessel ischemic disease"[tiab]` | 15 |
| 13 | `"subcortical ischemic vascular disease"[tiab]` | 60 |
| 14 | `"white matter hyperintens*"[tiab]` | 2,354 |
| 15 | `"white-matter hyperintens*"[tiab]` | 2,354 |
| 16 | `"white matter lesion*"[tiab]` | 4,051 |
| 17 | `"white-matter lesion*"[tiab]` | 4,051 |
| 18 | `"white matter change*"[tiab]` | 1,880 |
| 19 | `"white matter abnormalit*"[tiab]` | 1,590 |
| 20 | `leukoaraiosis[tiab]` | 1,008 |
| 21 | `leucoaraiosis[tiab]` | 38 |
| 22 | `"age-related white matter change*"[tiab]` | 130 |
| 23 | `"age related white matter change*"[tiab]` | 130 |
| 24 | `ARWMC[tiab]` | 58 |
| 25 | `WMH[tiab]` | 1,105 |
| 26 | `WML[tiab]` | 582 |
| 27 | `lacune*[tiab]` | 686 |
| 28 | `"lacunar infarction"[tiab]` | 927 |
| 29 | `"lacunar infarct*"[tiab]` | 2,251 |
| 30 | `"lacunar stroke*"[tiab]` | 918 |
| 31 | `"silent brain infarct*"[tiab]` | 280 |
| 32 | `"silent cerebral infarct*"[tiab]` | 322 |
| 33 | `"silent infarct*"[tiab]` | 311 |
| 34 | `"silent infarction"[tiab]` | 91 |
| 35 | `"subclinical infarct*"[tiab]` | 30 |
| 36 | `"covert infarct*"[tiab]` | 4 |
| 37 | `"brain infarct*"[tiab]` | 3,534 |
| 38 | `"cerebral infarct*"[tiab]` | 15,197 |
| 39 | `"cerebral microbleed*"[tiab]` | 710 |
| 40 | `"brain microbleed*"[tiab]` | 59 |
| 41 | `"cerebral microhemorrhag*"[tiab]` | 62 |
| 42 | `"cerebral microhaemorrhag*"[tiab]` | 4 |
| 43 | `"brain microhemorrhag*"[tiab]` | 15 |
| 44 | `"vascular brain injury"[tiab]` | 73 |
| 45 | `"vascular brain lesion*"[tiab]` | 74 |
| 46 | `"subcortical vascular lesion*"[tiab]` | 28 |
| 47 | `SIVD[tiab]` | 120 |
| 48 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47` | 91,189 |
| 49 | `#48 AND 1800/01/01:2017/05/06[dp]` | 91,025 |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Infarction"[Mesh] OR "Brain Infarction"[Mesh] OR "Cerebral Hemorrhage"[Mesh] OR "White Matter"[Mesh] OR "cerebral small vessel disease"[tiab] OR "small vessel disease"[tiab] OR "small-vessel disease"[tiab] OR "cerebral microangiopath*"[tiab] OR "small vessel ischemic disease"[tiab] OR "subcortical ischemic vascular disease"[tiab] OR "white matter hyperintens*"[tiab] OR "white-matter hyperintens*"[tiab] OR "white matter lesion*"[tiab] OR "white-matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter abnormalit*"[tiab] OR leukoaraiosis[tiab] OR leucoaraiosis[tiab] OR "age-related white matter change*"[tiab] OR "age related white matter change*"[tiab] OR ARWMC[tiab] OR WMH[tiab] OR WML[tiab] OR lacune*[tiab] OR "lacunar infarction"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent infarct*"[tiab] OR "silent infarction"[tiab] OR "subclinical infarct*"[tiab] OR "covert infarct*"[tiab] OR "brain infarct*"[tiab] OR "cerebral infarct*"[tiab] OR "cerebral microbleed*"[tiab] OR "brain microbleed*"[tiab] OR "cerebral microhemorrhag*"[tiab] OR "cerebral microhaemorrhag*"[tiab] OR "brain microhemorrhag*"[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesion*"[tiab] OR "subcortical vascular lesion*"[tiab] OR SIVD[tiab])) AND (1800/01/01:2017/05/06[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1 | initial | none | Initial one-block exposure strategy from scope-first PECO decisions; outcome, setting and design screened only. Added broad small-vessel disease/MRI-marker vocabulary and a 2017-05-06 publication-date limit alongside protocol as_of. |
| 2 | 343,275 | limits/combination | none | Corrected the explicit publication-date bound from a single-day term to a through-date range after the initial evaluation showed no eligible hits; protocol as_of remains for the NCBI entry-date audit bound. |
| 3 | 343,275 | limits/combination | none | Temporarily removed the very broad Cerebrovascular Disorders MeSH heading, which could retrieve stroke/vascular records without small-vessel markers; checked its impact on total count and screened relevant set before deciding whether to restore. |
| 4 | 90,789 | csvd: +0 / -1 | none | Temporarily removed the very broad Cerebrovascular Disorders MeSH heading, which could retrieve stroke/vascular records without small-vessel markers; checked its impact on total count and screened relevant set before deciding whether to restore. |
| 5 | 90,789 | csvd: +0 / -1 | none | Removed the zero-yield brain microhaemorrhage spelling after line-level count showed no PubMed records; the broader cerebral microhaemorrhage UK spelling remains. No known records lost. |
| 6 | 91,025 | csvd: +4 / -0 | none | Resolved critic F1 by documenting the required 2017-05-06 publication cutoff in protocol limits. Addressed F3 by adding lacune/lacunar infarction and silent infarction variants; evaluate recall and result growth. F2 broad-heading contribution review remains open for a separate check. |
| 7 | 91,025 | limits/combination | none | Addressed round-2 critic concern about generic brain/cerebral infarct* title-abstract terms by removing both; checked whether precise MRI-marker terms/headings retain all screened relevant discoveries and how the count changes. |
| 8 | 91,025 | limits/combination | none | final counts, run live |
| 9 | 91,025 | limits/combination | none | Clarification: the previous attempted removal of generic brain/cerebral infarct* phrases did not change strategy.json, as shown by zero terms changed and an unchanged result count. The terms remain as documented accepted risks following the second critic pass; no validation record was lost. |
| 10 | 91,025 | limits/combination | none | final counts, run live |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 3 findings; F1 must-fix resolved, F2 should-fix accepted-risk, F3 should-fix resolved
- Round 2 on version 6: 4 findings; F1 must-fix resolved, F2 should-fix accepted-risk, F3 should-fix resolved, F4 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 634 NCBI requests logged (367 from cache); strategy sha256 ac64cd91df9f._

## Rationale

- The strategy searches one exposure block for cerebral small vessel disease and MRI markers. Every eligible record must concern this exposure, and it is searchable through MeSH and title/abstract language.
- Outcomes (incident dementia, Alzheimer disease, cognitive decline/impairment), cohort/community setting, and longitudinal design are screened rather than AND-ed. These details can be absent or inconsistently named in abstracts, so requiring them could lose eligible records.
- MeSH terms are exploded by default. The block includes Cerebral Small Vessel Diseases, Leukoaraiosis, Stroke, Lacunar, and the broader Brain/Cerebral Infarction, Cerebral Hemorrhage and White Matter headings because no single specific heading covers all MRI-defined presentations. Text terms cover WMH/WML, leukoaraiosis/leucoaraiosis, small vessel disease variants, lacunes/lacunar and silent infarcts, microbleeds/microhemorrhages, and vascular brain injury. No publication type or study-design filter is applied.
- The broad Cerebrovascular Disorders heading was removed after testing: the dated count fell from 343,275 to 90,789 while all seven development records remained retrieved. Other broad marker-related headings and generic infarct wording were retained as accepted sensitivity risks.
- The only limit is the task-mandated publication date through 2017-05-06. No language, age, geography, or study-design restriction was used.

## How known records were found

No articles were supplied. A PubMed systematic-review query found the 2010 review "The clinical importance of white matter hyperintensities on brain magnetic resonance imaging" (PMID 20660506). Its references were explored with `psb neighbors`; 50 citation candidates were returned. Titles and snippets were reviewed, and full abstracts were checked for selected candidates. Seven eligible population/community or community-dwelling cohort records were added to the `relevant` development set, including Rotterdam Scan Study, Cardiovascular Health Study, Austrian Stroke Prevention Study, and Framingham Offspring records. The review citations were discovery sources, not an included-study benchmark. No independent benchmark or held-out validation set was established; the seven development records were used during strategy construction.

## Critic dispositions

- Round 1 F1 (date-limit documentation): resolved by adding the harness-defined publication cutoff and rationale to `protocol.json` and rerunning evaluation.
- Round 1 F2 (broad MeSH headings): accepted-risk. Broader headings may recover records indexed under infarction, hemorrhage, or white matter only. Their noise burden is material and precision was not established by the small development set. The broader Cerebrovascular Disorders heading was removed after count comparison.
- Round 1 F3 (lacune/lacunar and silent-infarction variants): resolved by adding `lacune*`, `lacunar infarction`, `silent infarct*`, and `silent infarction`; evaluation retained every development record.
- Round 2 F4 (generic brain/cerebral infarct wording): accepted-risk. Kept because eligible MRI infarct records may not say "silent," "lacunar," or "small vessel" in the title/abstract. These terms increase screening noise; their incremental eligible yield is uncertain.
- The second PRESS-structured internal critic check found no open must-fix findings. This is automated internal QA, not information-specialist PRESS peer review.

## Open risks for the peer reviewer

Relative recall is only against seven discovery records and is not an estimate of sensitivity. There is no independent validation set. Broad MeSH headings (especially Cerebral Infarction, Brain Infarction, Cerebral Hemorrhage, and White Matter) and generic brain/cerebral infarct title/abstract terms may produce substantial irrelevant retrieval; they were retained for possible sensitivity gains. The 2010 review and its citation links may not cover all marker families, especially cerebral microbleeds. Check the strategy against additional known studies, current MeSH mapping, and other databases with an information specialist before use.
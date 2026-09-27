# PubMed search strategy: audit

Generated 2026-09-27T14:41:09+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Methodological rigour of systematic reviews in environmental health
- Framework: review method + application context
- Scope confirmed by user: no (The user supplied no known articles and cannot answer questions during this run, so I proceeded with the stated scope assumptions. Interpreted the question as identifying environmental-health systematic review reports for appraisal of their rigor; rigor itself is screened, not AND-ed. Environmental/occupational exposure topics are included when health-related. No language limit. The user-requested publication-date cutoff through 2020-07-20 is explicit; the same date is also the PubMed Entrez entry-date ceiling, excluding records first added to PubMed after that as-of date.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Systematic reviews | search | These are the review reports whose methods will be appraised; systematic-review labels are searchable in publication type, MeSH, and title/abstract. |
| Environmental health | search | The application context is required; broad environmental-health, exposure, pollutant, and common environmental topic vocabulary supports recall. |
| Methodological rigour or quality | screen | Rigor is the characteristic assessed in the retrieved reviews, not necessarily named in their records; appraise at screening rather than requiring quality terminology. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2020-07-20
- Total records: 5,260 (5,282 before limits)
- Limits and filters: `"1800/01/01"[dp]:"2020/07/20"[dp]` (The user requested no literature published after 2020-07-20; this is the explicit publication-date cutoff. The workspace also applies the same date as an Entrez entry-date ceiling, excluding records added after that date.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Systematic Reviews as Topic"[Mesh]` | 6,347 |
| 2 | `"Systematic Review"[Publication Type]` | 151,195 |
| 3 | `"Meta-Analysis"[Publication Type]` | 123,018 |
| 4 | `"systematic review"[tiab]` | 160,742 |
| 5 | `"systematic reviews"[tiab]` | 30,252 |
| 6 | `"systematic literature review"[tiab]` | 11,090 |
| 7 | `"systematic literature reviews"[tiab]` | 505 |
| 8 | `"meta-analysis"[tiab]` | 152,699 |
| 9 | `"meta-analyses"[tiab]` | 38,218 |
| 10 | `"meta analysis"[tiab]` | 152,699 |
| 11 | `"meta analyses"[tiab]` | 38,218 |
| 12 | `"overview of systematic reviews"[tiab]` | 506 |
| 13 | `"overviews of systematic reviews"[tiab]` | 37 |
| 14 | `"research synthesis"[tiab]` | 540 |
| 15 | `"evidence synthesis"[tiab]` | 4,462 |
| 16 | `"umbrella review"[tiab]` | 410 |
| 17 | `"umbrella reviews"[tiab]` | 40 |
| 18 | `"meta-review"[tiab]` | 209 |
| 19 | `"meta-reviews"[tiab]` | 22 |
| 20 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 301,879 |
| 21 | `"Environmental Health"[Mesh]` | 25,528 |
| 22 | `"Environmental Exposure"[Mesh]` | 309,210 |
| 23 | `"Environmental Pollutants"[Mesh]` | 254,025 |
| 24 | `"Air Pollution"[Mesh]` | 59,328 |
| 25 | `"Water Pollution"[Mesh]` | 28,577 |
| 26 | `"Pesticides"[Mesh]` | 102,673 |
| 27 | `"Noise"[Mesh]` | 24,740 |
| 28 | `"Radiation Exposure"[Mesh]` | 74,160 |
| 29 | `"Occupational Exposure"[Mesh]` | 64,382 |
| 30 | `"environmental health"[tiab]` | 9,584 |
| 31 | `"environmental health science"[tiab]` | 81 |
| 32 | `"environmental epidemiology"[tiab]` | 721 |
| 33 | `"environmental exposure"[tiab]` | 7,564 |
| 34 | `"environmental exposures"[tiab]` | 6,391 |
| 35 | `"environmental pollutant"[tiab]` | 2,227 |
| 36 | `"environmental pollutants"[tiab]` | 5,443 |
| 37 | `"environmental pollution"[tiab]` | 7,249 |
| 38 | `"air pollution"[tiab]` | 27,926 |
| 39 | `"air pollutant"[tiab]` | 2,626 |
| 40 | `"air pollutants"[tiab]` | 7,660 |
| 41 | `"water pollution"[tiab]` | 3,970 |
| 42 | `"pesticide exposure"[tiab]` | 2,614 |
| 43 | `"environmental noise"[tiab]` | 1,208 |
| 44 | `"noise exposure"[tiab]` | 4,479 |
| 45 | `"chemical exposure"[tiab]` | 2,328 |
| 46 | `"chemical exposures"[tiab]` | 1,469 |
| 47 | `"occupational exposure"[tiab]` | 17,828 |
| 48 | `"occupational exposures"[tiab]` | 4,329 |
| 49 | `"environmental epidemiologic"[tiab]` | 65 |
| 50 | `"exposure science"[tiab]` | 146 |
| 51 | `"environmental and occupational health"[tiab]` | 280 |
| 52 | `"occupational and environmental health"[tiab]` | 540 |
| 53 | `#21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52` | 675,804 |
| 54 | `#20 AND #53` | 5,282 |
| 55 | `#54 AND "1800/01/01"[dp]:"2020/07/20"[dp]` | 5,260 |

### Strategy (single line, for copying into PubMed)

```text
(("Systematic Reviews as Topic"[Mesh] OR "Systematic Review"[Publication Type] OR "Meta-Analysis"[Publication Type] OR "systematic review"[tiab] OR "systematic reviews"[tiab] OR "systematic literature review"[tiab] OR "systematic literature reviews"[tiab] OR "meta-analysis"[tiab] OR "meta-analyses"[tiab] OR "meta analysis"[tiab] OR "meta analyses"[tiab] OR "overview of systematic reviews"[tiab] OR "overviews of systematic reviews"[tiab] OR "research synthesis"[tiab] OR "evidence synthesis"[tiab] OR "umbrella review"[tiab] OR "umbrella reviews"[tiab] OR "meta-review"[tiab] OR "meta-reviews"[tiab]) AND ("Environmental Health"[Mesh] OR "Environmental Exposure"[Mesh] OR "Environmental Pollutants"[Mesh] OR "Air Pollution"[Mesh] OR "Water Pollution"[Mesh] OR "Pesticides"[Mesh] OR "Noise"[Mesh] OR "Radiation Exposure"[Mesh] OR "Occupational Exposure"[Mesh] OR "environmental health"[tiab] OR "environmental health science"[tiab] OR "environmental epidemiology"[tiab] OR "environmental exposure"[tiab] OR "environmental exposures"[tiab] OR "environmental pollutant"[tiab] OR "environmental pollutants"[tiab] OR "environmental pollution"[tiab] OR "air pollution"[tiab] OR "air pollutant"[tiab] OR "air pollutants"[tiab] OR "water pollution"[tiab] OR "pesticide exposure"[tiab] OR "environmental noise"[tiab] OR "noise exposure"[tiab] OR "chemical exposure"[tiab] OR "chemical exposures"[tiab] OR "occupational exposure"[tiab] OR "occupational exposures"[tiab] OR "environmental epidemiologic"[tiab] OR "exposure science"[tiab] OR "environmental and occupational health"[tiab] OR "occupational and environmental health"[tiab])) AND ("1800/01/01"[dp]:"2020/07/20"[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| systematic_review | 675,804 | 0 |
| environmental_health | 301,879 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,238 | initial | none | Initial two-block recall-first strategy; environmental health is the required context and review quality is assessed at screening. Added screened pilot development records. |
| 2 | 2,258 | systematic_review: +2 / -0 | none | Added research synthesis and evidence synthesis phrases from objective term ranking and candidate terminology review; retained the two-block structure and cutoff. |
| 3 | 2,933 | environmental_health: +14 / -0 | none | Corrected the target-record interpretation: retrieved records are environmental-health systematic reviews to appraise. Replaced methodological guidance pilot records with nine screened target reviews. Added common subtopic vocabulary after PRESS critic noted environmental-health reviews may name specific exposures without using broad context labels. |
| 4 | 3,011 | environmental_health: +3 / -0 | none | Added Occupational Exposure MeSH and text terms to cover the protocol's occupational-environmental scope. Added a screened target review and split 30% of ten development records into held-out validation per standard-depth workflow. |
| 5 | 5,260 | systematic_review: +5 / -0 | none | Added Meta-Analysis publication type and hyphenated/unhyphenated title-abstract variants in response to round-2 critic finding F2; review-level methods are assessed at screening. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F1 should-fix resolved
- Round 2 on version 4: 2 findings; F1 should-fix resolved, F2 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 720 NCBI requests logged (356 from cache); strategy sha256 6ddd12cd17b3._

## Rationale

The question is interpreted as finding systematic review reports in environmental health so their methods can be appraised. `Systematic Reviews as Topic` is paired with systematic-review publication type and title/abstract wording because MeSH coverage alone is limited, particularly for a heading introduced in 2019. The `Meta-Analysis` publication type and text variants retain systematic-search meta-analyses whose titles do not say “systematic review”; screen results to exclude meta-analyses that do not meet the review eligibility criteria.

Environmental health and exposure are searched with exploded MeSH headings plus title/abstract terms. The MeSH lookup showed `Environmental Health` at 25,528 exploded versus 14,291 un-exploded records, and `Environmental Exposure` at 309,210 exploded versus 76,224 un-exploded records. Explosion was retained for recall; no `:noexp` restriction was used. Air pollution, water pollution, pesticides, noise, radiation exposure, and occupational exposure headings and terms were added to capture common environmental-health subtopics that may not use the phrase “environmental health.” Methodological rigor is screened rather than required as search wording, because systematic reviews may not label their methods consistently. No language limit was used. The publication-date bound is the user-required cutoff.

## How known records were found

The user supplied no seed articles. PubMed pilot searches and sampled results were screened at title and abstract level. Ten completed environmental-health systematic reviews were selected as known relevant records; seven were used for development and three were held out before term mining. No matching prior-review benchmark or user-provided seed set was available. The held-out set is semi-independent because it was consulted during evaluation, and neither set estimates absolute sensitivity.

## Critic dispositions

The round 1 should-fix finding asked for vocabulary covering specific exposure topics. It was addressed by adding exposure-topic MeSH headings and free-text terms. Round 2 identified missing meta-analysis vocabulary relative to the eligibility criteria; the `Meta-Analysis` publication type and hyphenated/unhyphenated singular and plural terms were added. Both findings are marked resolved; no must-fix finding remains open.

## Open risks for the peer reviewer

The scope treats occupational-environmental exposure reviews as eligible when health-related; confirm that this matches the protocol. The exposure-topic vocabulary is broad but cannot enumerate every environmental health domain. The 5,260-record result creates a substantial screening workload. Known-record testing used a small, selected set with no user seeds or external benchmark, so the observed relative recall must not be read as sensitivity. This PubMed-only draft still needs PRESS peer review by an information specialist before use.
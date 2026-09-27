# PubMed search strategy: audit

Generated 2026-09-27T15:13:36+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Impact of the COVID-19 pandemic and related lockdown measures on lifestyle behaviors and well-being
- Framework: PECO
- Scope confirmed by user: no (User asked not to be queried during this run. Scope is provisional. No known relevant articles were supplied. Publication cutoff set to 2020-11-22; strategy includes an explicit publication-date range, while psb as_of also bounds PubMed entry date. Search COVID-19/pandemic and lockdown/quarantine as one broad exposure block; screen lifestyle and well-being outcomes instead of AND-ing heterogeneous outcome terms. Current MeSH record shows COVID-19 descriptor introduced 2021(2020), so it is omitted to respect the as-of-2020-11-22 information boundary. Searches were made through psb only; no web search.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| COVID-19 pandemic and related lockdown measures | search | The pandemic and related restrictions define the exposure and are commonly named in titles, abstracts, or indexing. |
| Lifestyle behaviours and well-being | screen | These are heterogeneous outcomes (e.g., activity, diet, sleep, substance use, mental and subjective well-being) whose labels are variably reported; AND-ing them risks losing studies. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2020-11-22
- Total records: 151,652 (155,659 before limits)
- Limits and filters: `("1900/01/01"[dp] : "2020/11/22"[dp])` (Required publication-date cutoff; no records published after 2020-11-22.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `Coronavirus Infections[Mesh]` | 67,535 |
| 2 | `Pandemics[Mesh]` | 50,277 |
| 3 | `Quarantine[Mesh]` | 3,936 |
| 4 | `COVID-19[tiab]` | 67,388 |
| 5 | `COVID19[tiab]` | 64,206 |
| 6 | `"COVID 19"[tiab]` | 67,388 |
| 7 | `"coronavirus disease 2019"[tiab]` | 14,613 |
| 8 | `"2019 novel coronavirus"[tiab]` | 1,176 |
| 9 | `2019-nCoV[tiab]` | 1,288 |
| 10 | `SARS-CoV-2[tiab]` | 23,503 |
| 11 | `SARS-CoV2[tiab]` | 1,049 |
| 12 | `"severe acute respiratory syndrome coronavirus 2"[tiab]` | 7,988 |
| 13 | `coronavirus[tiab]` | 41,791 |
| 14 | `pandemic*[tiab]` | 58,444 |
| 15 | `lockdown*[tiab]` | 3,416 |
| 16 | `"lock down"[tiab]` | 163 |
| 17 | `quarantine*[tiab]` | 6,745 |
| 18 | `"stay at home"[tiab]` | 815 |
| 19 | `"stay-at-home"[tiab]` | 815 |
| 20 | `"stay home"[tiab]` | 227 |
| 21 | `"shelter in place"[tiab]` | 210 |
| 22 | `"shelter-in-place"[tiab]` | 210 |
| 23 | `"social distancing"[tiab]` | 2,657 |
| 24 | `"social isolation"[tiab]` | 7,931 |
| 25 | `"self isolation"[tiab]` | 289 |
| 26 | `confinement[tiab]` | 20,190 |
| 27 | `"home confinement"[tiab]` | 121 |
| 28 | `"home-confinement"[tiab]` | 121 |
| 29 | `"movement restriction"[tiab]` | 280 |
| 30 | `"movement restrictions"[tiab]` | 307 |
| 31 | `"movement control order"[tiab]` | 23 |
| 32 | `self-isolation[tiab]` | 289 |
| 33 | `self-isolate[tiab]` | 67 |
| 34 | `self-isolated[tiab]` | 32 |
| 35 | `"physical distancing"[tiab]` | 436 |
| 36 | `"physical distance"[tiab]` | 960 |
| 37 | `"restriction of movement"[tiab]` | 261 |
| 38 | `"mobility restriction"[tiab]` | 121 |
| 39 | `"mobility restrictions"[tiab]` | 156 |
| 40 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 155,659 |
| 41 | `#40 AND ("1900/01/01"[dp] : "2020/11/22"[dp])` | 151,652 |

### Strategy (single line, for copying into PubMed)

```text
((Coronavirus Infections[Mesh] OR Pandemics[Mesh] OR Quarantine[Mesh] OR COVID-19[tiab] OR COVID19[tiab] OR "COVID 19"[tiab] OR "coronavirus disease 2019"[tiab] OR "2019 novel coronavirus"[tiab] OR 2019-nCoV[tiab] OR SARS-CoV-2[tiab] OR SARS-CoV2[tiab] OR "severe acute respiratory syndrome coronavirus 2"[tiab] OR coronavirus[tiab] OR pandemic*[tiab] OR lockdown*[tiab] OR "lock down"[tiab] OR quarantine*[tiab] OR "stay at home"[tiab] OR "stay-at-home"[tiab] OR "stay home"[tiab] OR "shelter in place"[tiab] OR "shelter-in-place"[tiab] OR "social distancing"[tiab] OR "social isolation"[tiab] OR "self isolation"[tiab] OR confinement[tiab] OR "home confinement"[tiab] OR "home-confinement"[tiab] OR "movement restriction"[tiab] OR "movement restrictions"[tiab] OR "movement control order"[tiab] OR self-isolation[tiab] OR self-isolate[tiab] OR self-isolated[tiab] OR "physical distancing"[tiab] OR "physical distance"[tiab] OR "restriction of movement"[tiab] OR "mobility restriction"[tiab] OR "mobility restrictions"[tiab])) AND (("1900/01/01"[dp] : "2020/11/22"[dp]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 126,430 | initial | none | Initial recall-first exposure block based on question; outcomes screened because heterogeneous and inconsistently indexed. No seeds supplied; COVID-19 MeSH omitted because descriptor introduction is post-cutoff. |
| 2 | 154,290 | pandemic_lockdown: +10 / -0 | none | Expanded restriction vocabulary after PubMed pilot and abstract screening; retained one exposure block and screen-only outcomes. COVID-19 descriptor remains omitted for the simulated 2020-11-22 cutoff. |
| 3 | 154,281 | pandemic_lockdown: +3 / -1 | none | Replaced a PubMed-ignored short truncation stem with explicit self-isolation forms after lint flagged it; other restriction terms retained for recall. |
| 4 | 155,659 | pandemic_lockdown: +5 / -0 | none | Added physical distancing and further restriction phrasing after critic recommendation; COVID-19 MeSH heading deliberately omitted because it was introduced after the simulated search date. |
| 5 | 151,652 | limits/combination | none | Applied the required publication-date cutoff explicitly; psb as_of separately limits PubMed entry date. Assessed any resulting losses against screened development records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 4 findings; F1 should-fix accepted-risk, F2 should-fix resolved, F3 should-fix accepted-risk, F4 document accepted-risk
- Round 2 on version 5: 1 findings; R2-01 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 373 NCBI requests logged (146 from cache); strategy sha256 717b918e43f5._

## Rationale

The search uses one exposure block for the COVID-19 pandemic and related restrictions. The outcomes remain screening criteria because lifestyle behaviours and well-being encompass many variably named constructs; making them a required AND block could omit relevant studies. The exposure vocabulary combines title/abstract variants for COVID-19, SARS-CoV-2, pandemic, quarantine, lockdown, confinement, distancing, stay-at-home and movement restrictions with the exploded MeSH headings `Coronavirus Infections`, `Pandemics` and `Quarantine`. COVID-19[Mesh] was omitted because the current descriptor record reports introduction in 2021 (with 2020 indexing), outside the simulated 2020-11-22 information boundary. No supplementary concepts or `:noexp` headings were used. The sole limit is the required publication-date range through 2020-11-22; `as_of` also bounds PubMed entry date. Broad terms, especially `confinement`, are retained for sensitivity and may retrieve many irrelevant records.

## How known records were found

No seeds were supplied. A PubMed systematic-review pilot was used to identify related reviews; 20 review-filtered titles were inspected and six abstracts fetched. The candidate reviews covered recommendations, children, mental health, or broader quarantine effects, but did not provide a directly screened and scope-matched included-study benchmark from the PubMed abstracts, so none was entered as a benchmark set. A separate title/abstract pilot inspected 35 candidate titles and fetched seven abstracts; six empirical records clearly met the broad eligibility criteria and were added to the `relevant` development set. The strategy was checked against those six records (all retrieved). They were used during vocabulary development; there is no held-out validation set, and independent recall was not estimated.

## Critic dispositions

Two fresh-context PRESS-structured internal critique rounds were completed. In round 1, F1 (COVID-19 MeSH) was accepted as a risk because that descriptor falls after the simulated date; F2 was resolved by adding physical distancing and movement-restriction variants and re-evaluating without known losses; F3 was accepted as a tool warning after checking that MeSH and title/abstract terms translate to the intended fields; F4 was accepted as a limitation because no independent records were available. Round 2 reviewed version 5. R2-01, the request for a COVID-19-specific heading, was accepted for the same as-of reason. Neither round left a must-fix finding open.

## Open risks for the peer reviewer

The six-record development set is small, was found through PubMed pilots and is not independent validation. The outcome vocabulary was intentionally not ANDed, so screening burden will be high. Broad coronavirus, pandemic and confinement wording contributes noise. The COVID-19 MeSH heading was excluded to honor the simulated 2020 date, which could miss records whose later indexing has no matching title/abstract words. The tool continues to flag `automatic_term_mapping` for the explicitly tagged MeSH descriptors; PubMed's translated query was inspected and showed the intended MeSH Terms and Title/Abstract fields. Review the strategy in PubMed and conduct an independent PRESS review before use.
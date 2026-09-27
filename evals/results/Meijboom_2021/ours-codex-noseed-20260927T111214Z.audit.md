# PubMed search strategy: audit

Generated 2026-09-27T11:27:12+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Patients retransitioning from a biosimilar TNF-alpha inhibitor back to the originator biologic
- Framework: PECO
- Scope confirmed by user: no (User said no clarification was possible, so these are working assumptions and scope was not confirmed. No known relevant articles were supplied. PubMed searches are bounded through 2021-02-12 by the harness; final query carries publication-date and PubMed entry-date ceilings. No language, study-design, or other limits. Standard-depth discovery used systematic-review and precise pilot searches plus screened neighbours. Forward-switching systematic reviews were not used as benchmarks because their populations/transition do not meet eligibility. A discovered candidate outside the as-of PubMed corpus was removed from the relevant set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| TNF inhibitor biosimilars/reference biologics | search | This is the medication class at the core of the question; a biosimilar block can be identified in MeSH or text. Specific disease and TNF-inhibitor population details are screened to avoid unnecessary loss. |
| Switching back from biosimilar to originator/reference biologic | search | The direction of transition defines the topic. Broad wording and Drug Substitution indexing are searched, while screening confirms the actual sequence and product class. |
| Patients receiving TNF-alpha inhibitors | screen | Disease and patient population may not be consistently named in records; screen records for human TNF-inhibitor switchbacks. |
| Clinical, safety, immunogenicity, persistence and switching frequency outcomes | screen | Do not require outcome wording in abstracts; it is inconsistently reported. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2021-02-12
- Total records: 443 (446 before limits)
- Limits and filters: `("1800/01/01"[Date - Publication] : "2021/02/12"[Date - Publication])` (Harness requires excluding literature published after 2021-02-12.); `("1800/01/01"[Date - Entry] : "2021/02/12"[Date - Entry])` (Reproduce the PubMed record set available by the required as-of date.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 5,827 |
| 47 | `#24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46` | 5,123 |
| 48 | `#23 AND #47` | 446 |
| 49 | `#48 AND ("1800/01/01"[Date - Publication] : "2021/02/12"[Date - Publication])` | 443 |
| 50 | `#49 AND ("1800/01/01"[Date - Entry] : "2021/02/12"[Date - Entry])` | 443 |

### Strategy (single line, for copying into PubMed)

```text
((("Biosimilar Pharmaceuticals"[Mesh] OR Biosimilar[tiab] OR biosimilar*[tiab] OR "follow-on biologic"[tiab] OR "follow-on biologics"[tiab] OR "subsequent entry biologic"[tiab] OR "subsequent entry biologics"[tiab] OR "reference product"[tiab] OR "reference biologic"[tiab] OR "originator biologic"[tiab] OR "originator infliximab"[tiab] OR CT-P13[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR SB2[tiab] OR Flixabi[tiab] OR etanercept biosimilar*[tiab] OR adalimumab biosimilar*[tiab] OR infliximab biosimilar*[tiab] OR Remicade[tiab] OR Humira[tiab] OR Enbrel[tiab]) AND ("Drug Substitution"[Mesh] OR "reverse switching"[tiab] OR "reverse switch"[tiab] OR "switching back"[tiab] OR "switch back"[tiab] OR switchback[tiab] OR "switch-back"[tiab] OR "switch back to originator"[tiab:~2] OR "switching back to originator"[tiab:~2] OR "back to originator"[tiab:~2] OR "back to reference product"[tiab:~2] OR "back to reference biologic"[tiab:~2] OR "return to originator"[tiab:~2] OR "return to reference product"[tiab:~2] OR "biosimilar to originator"[tiab:~3] OR "biosimilar to reference"[tiab:~3] OR "from biosimilar to Remicade"[tiab:~2] OR "biosimilar to Remicade"[tiab:~2] OR "switch Humira"[tiab:~4] OR "switch Enbrel"[tiab:~4] OR "switch Remicade"[tiab:~4] OR "switch originator"[tiab:~4] OR "switch reference"[tiab:~4])) AND (("1800/01/01"[Date - Publication] : "2021/02/12"[Date - Publication]))) AND (("1800/01/01"[Date - Entry] : "2021/02/12"[Date - Entry]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| biosimilar | 5,123 | 0 |
| switchback | 5,827 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 421 | initial | none | Initial two-block strategy; each core topic component has MeSH and title/abstract terms. TNF disease/population and outcomes are screened. Final query will carry a publication-date ceiling of 2021-02-12. |
| 2 | 427 | switchback: +9 / -9 | none | Replaced PubMed phrase-index warnings for return/back-to-originator variants with proximity syntax to permit flexible wording; all previously retrieved relevant records must remain retrieved. |
| 3 | 427 | biosimilar: +1 / -1; switchback: +1 / -1 | none | Quoted both MeSH headings explicitly to remove ATM translation warnings; no other terms changed. |
| 4 | 446 | biosimilar: +4 / -0; switchback: +5 / -0 | none | Resolved F1 from the same-context PRESS-structured critic by adding Humira, Enbrel, and Remicade brand terms plus switch-to-brand/originator/reference proximity variants. Existing known records must remain retrieved. |
| 5 | 443 | limits/combination | 33538298 | Applied the required harness publication-date ceiling as an explicit PubMed limit so audited counts match the delivered query. |
| 6 | 443 | limits/combination | none | Removed a discovered record not present in PubMed by the 2021-02-12 as-of date; all remaining validation records remain within the required date scope. |
| 7 | 443 | limits/combination | none | Added an explicit PubMed entry-date ceiling to the copyable query so the as-of database window is reproducible in addition to the publication-date cutoff. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (same-context critic; reviewed packet-1.md only): 1 findings; F1 must-fix open
- Round 2 on version 4 (same-context critic; reviewed packet-2.md only): 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 527 NCBI requests logged (131 from cache); strategy sha256 d3d976a1f87b._

## Rationale

The strategy ANDs two topic concepts: biosimilar/reference-biologic terminology and switching-back/reverse-switch terminology. The two blocks each include a MeSH heading and title/abstract wording. Biosimilar Pharmaceuticals and Drug Substitution are searched exploded; the MeSH lookup found no narrower headings for either. Text wording includes biosimilar variants, follow-on/subsequent-entry terms, named TNF inhibitor biosimilars and originators, reverse/switchback terms, and proximity combinations for varied word order. Disease, patient details, and clinical outcomes are screened rather than required in the query. No language or study-design filter is used. Publication-date and PubMed entry-date ceilings reproduce the required 2021-02-12 cutoff.

## How known records were found

The user supplied no seeds. PubMed discovery used a systematic-review-oriented query (34 records), a focused reverse-switch pilot (21 records), a broader biosimilar/switching pilot, and related-record searching. Selected review abstracts were checked, but no dedicated eligible included-study benchmark was assembled. The neighbor command returned 107 candidates; abstracts were fetched for the top 30. Two pre-cutoff primary reports were screened in as relevant development records. The strategy retrieved both (relative recall 100% against this development set); this is not independent validation and does not estimate sensitivity. No held-out validation set was available.

## Critic dispositions

Two same-context PRESS-structured internal critic rounds were completed because no fresh-context reviewer was available. Round 1 raised F1 about missing proximity to non-infliximab TNF originator brand names. Humira, Enbrel, and additional switch-to-brand/originator/reference proximity variants were added; round 2 marked F1 resolved. No must-fix finding remains open. The required publication-date and PubMed entry-date ceilings were evaluated in the final strategy; the internal critique is not PRESS peer review.

## Open risks for the peer reviewer

The switchback concept is lexically fragile: authors may describe a return to an originator without using reverse or switchback, and records not indexed with Drug Substitution may use other wording. That heading is broad and intentionally retained for recall. Only two eligible pre-cutoff records were available for development, with no independent benchmark; the 100% relative recall figure is therefore a weak check. The 443-record result still requires screening. An information specialist should review product-name coverage, transition variants, MeSH choices, date handling, and the complete PubMed line before use.

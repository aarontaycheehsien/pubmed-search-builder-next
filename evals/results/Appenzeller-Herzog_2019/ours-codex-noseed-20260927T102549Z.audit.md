# PubMed search strategy: audit

Generated 2026-09-27T10:41:22+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User has no known relevant articles and cannot answer questions during this run; proceeded on reasonable assumptions without scope confirmation. No language or age limits. Search evidence bounded to records published on or before 2018-12-23. Standard depth. Comparative outcome and design criteria are screening criteria. Because the user could not clarify scope, "common therapies" was taken to mean conventional copper-directed pharmacotherapy (chelators and zinc salts); no language or age limit. Herbal regimens and liver transplantation are outside this assumed scope. Historical cutoff applied through as_of and publication date.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The target disease is central, consistently named, and indexed. |
| Wilson disease therapies | search | The intervention is inherent to this effectiveness question; chelators and zinc therapies are searchable by controlled vocabulary and names. No comparator-specific or outcome block is required. |
| Comparative effectiveness and outcomes | screen | Comparators and outcomes are inconsistently named in records and are assessed during screening. |
| Eligible study designs | screen | No design restriction was specified; no study-design filter will be applied. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2018-12-23
- Total records: 4,062 (4,065 before limits)
- Limits and filters: `1800:2018/12/23[dp]` (User-specified publication date cutoff: retrieve literature published on or before 2018-12-23.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 |
| 2 | `Wilson[tiab]` | 11,101 |
| 3 | `"wilson disease"[tiab]` | 1,523 |
| 4 | `"wilson's disease"[tiab]` | 4,158 |
| 5 | `"wilson disease"[tiab:~2]` | 5,660 |
| 6 | `hepatolenticular degeneration[tiab]` | 946 |
| 7 | `"progressive lenticular degeneration"[tiab]` | 10 |
| 8 | `"copper storage disease"[tiab]` | 25 |
| 9 | `ATP7B[tiab]` | 1,016 |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 12,896 |
| 11 | `"Penicillamine"[Mesh]` | 7,878 |
| 12 | `"Trientine"[Mesh]` | 380 |
| 13 | `"Zinc"[Mesh]` | 58,485 |
| 14 | `"Zinc Compounds"[Mesh]` | 12,484 |
| 15 | `"Chelating Agents"[Mesh]` | 30,724 |
| 16 | `penicillamine[tiab]` | 6,853 |
| 17 | `"D-penicillamine"[tiab]` | 3,268 |
| 18 | `"D penicillamine"[tiab]` | 3,268 |
| 19 | `trientine[tiab]` | 219 |
| 20 | `triethylenetetramine[tiab]` | 360 |
| 21 | `Syprine[tiab]` | 4 |
| 22 | `zinc[tiab]` | 108,490 |
| 23 | `"zinc acetate"[tiab]` | 817 |
| 24 | `"zinc sulfate"[tiab]` | 1,531 |
| 25 | `"zinc salts"[tiab]` | 358 |
| 26 | `tetrathiomolybdate[tiab]` | 351 |
| 27 | `"ammonium tetrathiomolybdate"[tiab]` | 84 |
| 28 | `dimercaprol[tiab]` | 623 |
| 29 | `chelating[tiab]` | 20,248 |
| 30 | `chelation[tiab]` | 13,461 |
| 31 | `treat*[tiab]` | 5,019,714 |
| 32 | `therap*[tiab]` | 2,661,898 |
| 33 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32` | 6,473,253 |
| 34 | `#10 AND #33` | 4,065 |
| 35 | `#34 AND 1800:2018/12/23[dp]` | 4,062 |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR Wilson[tiab] OR "wilson disease"[tiab] OR "wilson's disease"[tiab] OR "wilson disease"[tiab:~2] OR hepatolenticular degeneration[tiab] OR "progressive lenticular degeneration"[tiab] OR "copper storage disease"[tiab] OR ATP7B[tiab]) AND ("Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc"[Mesh] OR "Zinc Compounds"[Mesh] OR "Chelating Agents"[Mesh] OR penicillamine[tiab] OR "D-penicillamine"[tiab] OR "D penicillamine"[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR Syprine[tiab] OR zinc[tiab] OR "zinc acetate"[tiab] OR "zinc sulfate"[tiab] OR "zinc salts"[tiab] OR tetrathiomolybdate[tiab] OR "ammonium tetrathiomolybdate"[tiab] OR dimercaprol[tiab] OR chelating[tiab] OR chelation[tiab] OR treat*[tiab] OR therap*[tiab])) AND (1800:2018/12/23[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson | 6,473,253 | 0 |
| therapy | 12,896 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 3,186 | initial | none | Initial Wilson disease AND therapy strategy; MeSH and broad free-text terms, publication cutoff per run instructions. No user seeds; term set based on indexed headings and common therapy nomenclature. |
| 2 | 4,062 | wilson: +1 / -1; therapy: +1 / -1 | none | After screening similar records from the 2009 treatment review: included five human treatment-outcome studies. Added broad Wilson[tiab] from all development records and Zinc[Mesh] observed on relevant records; removed zero-yield Kinnier-Wilson phrase and ambiguous BAL acronym. Retained treatment/therapy stems for high sensitivity; no design/outcome block. |
| 3 | 4,062 | limits/combination | none | Extended screening of similar-record candidates from the 2009 treatment review added PMID 17063115 (comparative penicillamine/zinc outcomes) and 26067812 (therapy-related immune adverse events) to development set. Strategy unchanged; both should be retrieved. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 3: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 469 NCBI requests logged (158 from cache); strategy sha256 d811fd4b6baa._

## Rationale

The search uses two AND-ed blocks: Wilson disease and conventional anticopper pharmacotherapy. The formal MeSH disease heading is `Hepatolenticular Degeneration`; its explosion adds no narrower headings in the MeSH lookup. The therapy block uses exploded MeSH headings for penicillamine, trientine, zinc and zinc compounds, and chelating agents, plus title/abstract variants for D-penicillamine, trientine, zinc salts, tetrathiomolybdate, dimercaprol, chelation, treatment and therapy. Broad treatment and therapy stems remain to favor recall. Comparators, outcomes and study designs stay at screening because they are inconsistently reported and no design restriction was requested. The publication-date limit reflects the requested 2018-12-23 cutoff; there are no other language, age or design limits. The assumed scope is conventional copper-directed medicines; herbal regimens and transplantation are outside that assumption.

## How known records were found

The user supplied no known articles. A Wilson disease query with PubMed's systematic-review filter returned 15 candidates. Abstract screening identified the 2009 review of chelators and zinc in initial Wilson disease treatment (PMID 19210288) as a close prior review. Its included-study reference list was not available through the script's reference-neighbor function, so it was not used as a benchmark. Thirty similar-record candidates linked to that review were fetched and screened; seven human comparative therapy outcome or safety studies were added to the development set. No records were held out, and there is no independent validation or benchmark set. The seven-record set was used during strategy development.

## Critic dispositions

Two fresh-context PRESS-structured internal critique rounds were completed. Both returned pass verdicts in all six domains and no findings; no strategy changes were required. These automated reviews are internal quality assurance, not PRESS peer review.

## Open risks for the peer reviewer

The scope was not confirmed with the user. ?Common therapies? was interpreted as conventional copper-directed drug/mineral regimens. The development set came from PubMed similar-record links around one prior review, so it is not independent and may not represent all relevant therapies or study types. Relative recall was 7/7 on this small set; sensitivity is not established. Broad terms such as `Wilson[tiab]`, `zinc[tiab]`, `treat*[tiab]` and `therap*[tiab]` are retained intentionally and may add screening workload. Comparator and outcome eligibility must be determined during screening. This PubMed draft needs PRESS peer review by an information specialist before use.

# PubMed search strategy: audit

Generated 2026-09-27T11:05:04+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Source of mesenchymal stem cells for the management of osteoarthritis of the knee
- Framework: PICO (source is the intervention variant of interest)
- Scope confirmed by user: no (User supplied no known relevant articles and cannot answer questions during this run; scope roles and eligibility assumptions were set from the review question and not confirmed. No web search. Use PubMed/NCBI commands only and exclude records published after 2022-05-10 from retrieval/evaluation. The question is interpreted as comparing tissue sources of mesenchymal cells used clinically to manage knee OA; the source is screened rather than AND-ed because source labels can be variably reported. The final query includes an explicit PubMed publication-date range ending 2022-05-10; protocol as_of also bounds PubMed entry dates at 2022-05-10, so both publication eligibility and available-record cutoff are respected.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Osteoarthritis of the knee | search | The target condition and joint are central and typically named or indexed. |
| Mesenchymal stromal/stem cells | search | The intervention is central and has a broad searchable vocabulary including stromal and stem terminology. |
| Tissue source of administered mesenchymal cells | screen | This is the comparison of interest, but source-specific terms may be inconsistently named and requiring them would risk recall; capture and compare sources during screening. |
| Clinical management and outcomes | screen | Outcomes are inconsistently reported and should not be a required search block. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2022-05-10
- Total records: 2,737 (2,742 before limits)
- Limits and filters: `1800/01/01:2022/05/10[dp]` (User-requested publication cutoff; exclude literature published after 2022-05-10.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Osteoarthritis, Knee"[Mesh]` | 25,328 |
| 2 | `"Osteoarthritis"[Mesh]` | 73,454 |
| 3 | `osteoarthrit*[tiab]` | 81,326 |
| 4 | `osteoarthrosis[tiab]` | 3,446 |
| 5 | `gonarthrosis[tiab]` | 1,122 |
| 6 | `"degenerative joint disease"[tiab]` | 2,782 |
| 7 | `"knee osteoarthritis"[tiab]` | 14,094 |
| 8 | `"osteoarthritis of the knee"[tiab]` | 3,217 |
| 9 | `"osteoarthritis of knee"[tiab]` | 177 |
| 10 | `"osteoarthrosis of the knee"[tiab]` | 172 |
| 11 | `"osteoarthrosis of knee"[tiab]` | 8 |
| 12 | `"osteoarthritis knee"[tiab:~2]` | 19,937 |
| 13 | `"osteoarthrosis knee"[tiab:~2]` | 326 |
| 14 | `"degenerative joint disease knee"[tiab:~2]` | 87 |
| 15 | `(OA[tiab] AND knee[tiab])` | 13,579 |
| 16 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 107,292 |
| 17 | `"Mesenchymal Stem Cells"[Mesh]` | 47,452 |
| 18 | `"Mesenchymal Stem Cell Transplantation"[Mesh]` | 14,289 |
| 19 | `"mesenchymal stem cell*"[tiab]` | 54,213 |
| 20 | `"mesenchymal stromal cell*"[tiab]` | 8,927 |
| 21 | `"multipotent stromal cell*"[tiab]` | 494 |
| 22 | `"mesenchymal progenitor cell*"[tiab]` | 1,088 |
| 23 | `stem cell*[tiab]` | 312,453 |
| 24 | `MSC[tiab]` | 23,221 |
| 25 | `MSCs[tiab]` | 30,890 |
| 26 | `"mesenchymal stem cell"[tiab:~2]` | 14,627 |
| 27 | `"mesenchymal stromal cell"[tiab:~2]` | 2,501 |
| 28 | `#17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27` | 328,761 |
| 29 | `#16 AND #28` | 2,742 |
| 30 | `#29 AND 1800/01/01:2022/05/10[dp]` | 2,737 |

### Strategy (single line, for copying into PubMed)

```text
(("Osteoarthritis, Knee"[Mesh] OR "Osteoarthritis"[Mesh] OR osteoarthrit*[tiab] OR osteoarthrosis[tiab] OR gonarthrosis[tiab] OR "degenerative joint disease"[tiab] OR "knee osteoarthritis"[tiab] OR "osteoarthritis of the knee"[tiab] OR "osteoarthritis of knee"[tiab] OR "osteoarthrosis of the knee"[tiab] OR "osteoarthrosis of knee"[tiab] OR "osteoarthritis knee"[tiab:~2] OR "osteoarthrosis knee"[tiab:~2] OR "degenerative joint disease knee"[tiab:~2] OR (OA[tiab] AND knee[tiab])) AND ("Mesenchymal Stem Cells"[Mesh] OR "Mesenchymal Stem Cell Transplantation"[Mesh] OR "mesenchymal stem cell*"[tiab] OR "mesenchymal stromal cell*"[tiab] OR "multipotent stromal cell*"[tiab] OR "mesenchymal progenitor cell*"[tiab] OR stem cell*[tiab] OR MSC[tiab] OR MSCs[tiab] OR "mesenchymal stem cell"[tiab:~2] OR "mesenchymal stromal cell"[tiab:~2])) AND (1800/01/01:2022/05/10[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| knee_oa | 328,761 | 0 |
| msc | 107,292 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,178 | initial | none | Initial high-sensitivity two-block draft with MeSH and text-word coverage; source and outcomes screened, with publication-date cutoff through 2022-05-10. |
| 2 | 2,737 | msc: +1 / -0 | none | Added stem cell*[tiab] within the MSC block after internal PRESS critique identified relevant studies may use generic stem-cell wording. Knee OA remains the AND context to control noise. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1 (Same-context critic; no fresh-context reviewer was available without delegation, so this is PRESS-structured internal critique only.): 1 findings; F1 should-fix open
- Round 2 on version 2 (Same-context second review because a separate reviewer context was unavailable; this is internal PRESS-structured QA, not specialist peer review.): 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 265 NCBI requests logged (57 from cache); strategy sha256 f011323e2474._


## Rationale

The question was interpreted as a review of clinical use of mesenchymal stromal/stem cells for knee osteoarthritis, with tissue source as the comparison of interest. The knee osteoarthritis and MSC concepts are searched as two required blocks. `"Osteoarthritis, Knee"[Mesh]` is included alongside the exploded `"Osteoarthritis"[Mesh]` heading; free-text terms cover osteoarthritis/osteoarthrosis, gonarthrosis, knee wording and the OA abbreviation paired with knee. For the intervention, the exploded `"Mesenchymal Stem Cells"[Mesh]` and `"Mesenchymal Stem Cell Transplantation"[Mesh]` headings are paired with stromal, stem, progenitor and acronym variants. Generic `stem cell*[tiab]` was added after internal critique to avoid missing records that do not spell out mesenchymal in the abstract. Tissue source and outcomes are handled at screening because they may not be named consistently. The only limit is the user-required publication date through 2022-05-10; the workspace also constrained PubMed entry dates through that day.

## How known records were found

The user had no seed articles. A PubMed systematic-review query identified PMID 33850849, a review comparing MSCs from different sources for knee osteoarthritis. Its reference links returned 23 candidate records. Titles and available abstracts were screened against the recorded clinical knee OA and administered MSC eligibility criteria; nine records were included in the `relevant` development set. These were discovered through a prior review's reference list, but the available citation links did not establish that each was among that review's included studies, so they are not presented as a formal review-inclusion benchmark. No held-out validation set was available and no term mining was done from any validation records.

## Critic dispositions

Round 1 was a same-context PRESS-structured internal critique. It raised F1, a should-fix concern that generic stem-cell wording could be absent from the abstract's mesenchymal terminology. `stem cell*[tiab]` was added; the count rose from 2,178 to 2,737, and none of the nine development records was lost. Round 2 found the concern resolved. No must-fix finding remains open. These internal rounds are not PRESS peer review by an information specialist.

## Open risks for the peer reviewer

The central assumption is that the review wants to identify clinical MSC use across tissue sources and compare sources during screening, including trials of one source, rather than retrieve only head-to-head source-comparison studies. If the intended eligibility is head-to-head comparisons only, clarify that before screening; the current query does not require a source comparison. The generic stem-cell term and broad exploded osteoarthritis heading add records that will need screening. The nine known records are a small, non-independent development set discovered through a single prior review's citation list; the reported relative recall is not sensitivity, and no independent validation was possible. The scope could not be confirmed with the user during this run. PRESS peer review by an information specialist remains pending.

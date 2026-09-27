# PubMed search strategy: audit

Generated 2026-09-27T10:53:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: topic-based conceptual review
- Scope confirmed by user: no (User requested no follow-up during this run; scope and eligibility are provisional assumptions. Historical search boundary: records published on or before 2018-11-17. No known relevant articles supplied; no language or other limits.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The clinical topic must be identifiable; use broad depressive disorder terms and MeSH. |
| Relapse or recurrence | search | The review is specifically about depressive relapse and recurrence; this is a defining topic concept. |
| Psychological theories or models | screen | Theory labels are diverse and inconsistently indexed; screen retrieved records for substantive psychological accounts of relapse/recurrence. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2018-11-17
- Total records: 17,383 (17,415 before limits)
- Limits and filters: `("1800/01/01"[dp] : "2018/11/17"[dp])` (Explicit user-requested publication cutoff; PubMed as_of separately restricts records entered by 2018-11-17.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 |
| 3 | `"Depression"[Mesh]` | 112,392 |
| 4 | `depress*[tiab]` | 419,763 |
| 5 | `"depressive disorder"[tiab]` | 24,917 |
| 6 | `"depressive disorders"[tiab]` | 8,950 |
| 7 | `"major depression"[tiab]` | 22,341 |
| 8 | `"major depressive disorder"[tiab]` | 20,240 |
| 9 | `"unipolar depression"[tiab]` | 2,526 |
| 10 | `"depressive illness"[tiab]` | 3,351 |
| 11 | `melanchol*[tiab]` | 2,939 |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 460,494 |
| 13 | `"Recurrence"[Mesh]` | 178,366 |
| 14 | `relaps*[tiab]` | 163,847 |
| 15 | `recurren*[tiab]` | 496,927 |
| 16 | `recrudescen*[tiab]` | 3,173 |
| 17 | `"new episode"[tiab]` | 664 |
| 18 | `"new episodes"[tiab]` | 691 |
| 19 | `"subsequent episode"[tiab]` | 161 |
| 20 | `"subsequent episodes"[tiab]` | 449 |
| 21 | `"future episode"[tiab]` | 22 |
| 22 | `"future episodes"[tiab]` | 252 |
| 23 | `"repeat episode"[tiab]` | 44 |
| 24 | `"repeat episodes"[tiab]` | 124 |
| 25 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 706,784 |
| 26 | `#12 AND #25` | 17,415 |
| 27 | `#26 AND ("1800/01/01"[dp] : "2018/11/17"[dp])` | 17,383 |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Depression"[Mesh] OR depress*[tiab] OR "depressive disorder"[tiab] OR "depressive disorders"[tiab] OR "major depression"[tiab] OR "major depressive disorder"[tiab] OR "unipolar depression"[tiab] OR "depressive illness"[tiab] OR melanchol*[tiab]) AND ("Recurrence"[Mesh] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR "new episode"[tiab] OR "new episodes"[tiab] OR "subsequent episode"[tiab] OR "subsequent episodes"[tiab] OR "future episode"[tiab] OR "future episodes"[tiab] OR "repeat episode"[tiab] OR "repeat episodes"[tiab])) AND (("1800/01/01"[dp] : "2018/11/17"[dp]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 706,784 | 0 |
| relapse_recurrence | 460,494 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 16,983 | initial | none | Initial broad two-block search; theory screened due inconsistent labeling; publication cutoff added per task. |
| 2 | 17,383 | depression: +1 / -0 | none | Added the Depression MeSH heading observed on screened relevant records, while retaining broad text and recurrence terms. |
| 3 | 17,383 | limits/combination | none | Added two screened citation records that explicitly analyze or propose theory/models of depressive recurrence; broader literature remains screening-based. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (same-context critic): 0 findings; 
- Round 2 on version 3: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 444 NCBI requests logged (115 from cache); strategy sha256 3ebcb0b06039._


## Rationale

The strategy searches depressive disorders and relapse/recurrence as the two defining topic concepts. It uses the exploded MeSH headings `Depressive Disorder`, `Major Depressive Disorder`, `Depression`, and `Recurrence`, paired with explicit title/abstract words for records without MeSH indexing and older or variable wording. The psychological theory/model concept is screened rather than required in the query because terminology is diverse and may not appear in abstracts or indexing. The publication-date limit is required by the task; PubMed's as-of setting also restricts records to those entered by 2018-11-17, reproducing the historical search boundary. No other limits or filters were used.

## How known records were found

No articles were supplied by the user. A PubMed search for systematic reviews on depressive relapse/recurrence and psychological mechanisms identified PMID 30075313, a systematic review and meta-synthesis of risk factors and mechanisms. Its 50 PubMed-linked reference candidates were retrieved and screened by title/abstract; four records were judged relevant to the stated psychological-theory scope (PMIDs 20132925, 21895384, 25688431, and 27069286). These four plus PMID 30075313 form the five-record development set. No records were held out, and no independent validation set was available.

## Critic dispositions

Two PRESS-structured internal critic rounds had no findings left open. Round 1 was a same-context review; round 2 used a fresh-context reviewer on the updated development set. The strategy terms were unchanged in round 2.

## Open risks for the peer reviewer

The five-record development set is small and was used during strategy construction; its 100% relative recall is not an independent validation result and does not estimate sensitivity. The final query is intentionally broad and returned 17,383 records, so screening burden may be substantial. Psychological-theory eligibility is not enforced by the search, and records that describe mechanisms without an explicit depression or relapse/recurrence label may be missed. The historical PubMed entry-date boundary excludes records added after 2018-11-17, even if their publication date is earlier. This PubMed-only draft needs PRESS peer review by an information specialist before use.

# PubMed search strategy: audit

Generated 2026-09-27T15:38:23+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / symptom course
- Scope confirmed by user: no (User requested no questions during this run; scope roles and eligibility were set from the question without user confirmation. Assumed broad populations, trauma types, languages, and study designs; no additional limits. Records published after 2016-01-24 excluded by as_of to honor the requested historical cutoff.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and post-traumatic stress symptoms | search | The condition/symptom domain defines the review topic and is expected to be named in records; broad controlled vocabulary and text terms can retrieve diagnosed and subthreshold post-traumatic stress. |
| Traumatic event or trauma exposure | screen | Trauma is inherent to PTSD but its event wording is heterogeneous and not required in the abstract or indexing; screen for an eligible event context. |
| Longitudinal symptom trajectories/course | screen | Trajectory, course, and repeated symptom measurement are eligibility features with variable labels; requiring a separate block risks missing relevant longitudinal reports. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2016-01-24
- Total records: 31,980 (32,074 before limits)
- Limits and filters: `1800:2016/01/24[dp]` (Required by the user's as-of date of 2016-01-24; excludes records with publication dates after that date. The workspace also applies the same as-of bound to PubMed entry date for historical reproducibility.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 |
| 2 | `PTSD[tiab]` | 15,732 |
| 3 | `"posttraumatic stress disorder"[tiab]` | 12,500 |
| 4 | `"post-traumatic stress disorder"[tiab]` | 7,081 |
| 5 | `"post traumatic stress disorder"[tiab]` | 7,081 |
| 6 | `"posttraumatic stress"[tiab]` | 14,174 |
| 7 | `"post-traumatic stress"[tiab]` | 8,160 |
| 8 | `"post traumatic stress"[tiab]` | 8,160 |
| 9 | `posttraumatic stress disorder*[tiab]` | 12,654 |
| 10 | `post-traumatic stress disorder*[tiab]` | 7,263 |
| 11 | `post traumatic stress disorder*[tiab]` | 7,263 |
| 12 | `posttraumatic stress symptom*[tiab]` | 1,177 |
| 13 | `post-traumatic stress symptom*[tiab]` | 474 |
| 14 | `post traumatic stress symptom*[tiab]` | 474 |
| 15 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14` | 32,074 |
| 16 | `#15 AND 1800:2016/01/24[dp]` | 31,980 |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR "posttraumatic stress disorder"[tiab] OR "post-traumatic stress disorder"[tiab] OR "post traumatic stress disorder"[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR posttraumatic stress disorder*[tiab] OR post-traumatic stress disorder*[tiab] OR post traumatic stress disorder*[tiab] OR posttraumatic stress symptom*[tiab] OR post-traumatic stress symptom*[tiab] OR post traumatic stress symptom*[tiab])) AND (1800:2016/01/24[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 31,980 | initial | none | Initial one-block PTSD strategy with MeSH descriptor and spelling/morphology variants; trauma and trajectory are screened per scope; date cutoff follows request; benchmark screened from prior review references. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; F1 must-fix open
- Round 2 on version 1: 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 96 NCBI requests logged (30 from cache); strategy sha256 7c93732b844b._

## Rationale

The strategy searches one core concept: PTSD and post-traumatic stress symptoms. It uses the exploded `"Stress Disorders, Post-Traumatic"[Mesh]` descriptor plus title/abstract variants for PTSD, posttraumatic stress disorder, and post-traumatic stress symptoms. The descriptor's scope note covers stress disorders with symptoms lasting more than one month; the accompanying text words also cover symptom-focused and not-yet-indexed records. MeSH lookup found no narrower headings, and exploded and `[Mesh:noexp]` counts were both 25,369. UK/US spelling is not relevant to these terms; closed, hyphenated, and spaced forms are represented. The text layer uses safe truncation only on long stems.

Trauma exposure and repeated measurement/trajectory were left for screening because event descriptions and trajectory labels vary, while PTSD is the defining topic. No age, language, study-design, or other methodological filters were added. The publication-date limit is required by the requested cutoff; the workspace additionally applied the same `as_of` bound to PubMed entry date during evaluation.

## How known records were found

No user-supplied known articles were available. A PubMed pilot combining PTSD terms, trajectory/course wording, and `systematic[sb]` returned 50 records; the displayed titles included two closely matched reviews (PMIDs 23593134 and 25733025). The review at PMID 23593134 focused on PTSD prevalence and trajectories in trauma-exposed populations. `psb neighbors` returned 29 cited records for screening; title and abstract screening included 9 records (PMIDs 12046673, 16529915, 16585441, 16848647, 17012689, 17530151, 18000197, 18629750, and 18725431) in the benchmark set. This screened reference subset was not used for term mining. No separate held-out validation set was created. The benchmark's cited-record status and scope are less independent than a complete included-study list verified from the review's tables.

## Critic dispositions

Two fresh-context PRESS-structured internal critic rounds were completed. Round 1 finding F1 flagged that the publication-date limit was present in the strategy but absent from `protocol.json`. The protocol now records the user's explicit publication-date cutoff and rationale. Round 2 marked F1 resolved; no must-fix findings remain open. This automated critique is internal quality assurance, not librarian PRESS peer review.

## Open risks for the peer reviewer

There were no user seeds, and only 9 screened records from one prior review's citation set were used, so 100% relative recall is not an estimate of sensitivity. The strategy can miss studies that report only general distress or resilience after trauma without naming PTSD/post-traumatic stress in PubMed fields or MeSH. Some benchmark records may be cited rather than included studies in the prior review because inclusion status could not be checked from its PubMed abstract. The single broad PTSD block is intentional for recall; screen retrieved records for trauma exposure and repeated symptom assessment/trajectory eligibility. Have an information specialist check the vocabulary, benchmark provenance, scope, and PubMed date handling before use.
# PubMed search strategy: audit

Generated 2026-09-27T15:28:49+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO
- Scope confirmed by user: no (User requested proceeding without questions. Assumed PICO intervention-effectiveness scope; searched anxiety-related disorders AND CBT. Long-term follow-up/outcomes and comparator are screened, not searched. No age, language, or study-design restriction was applied. The run's as_of value is 2017-08-24 and the final search also applies a publication-date limit through that date per the harness. No known relevant articles were supplied. The six-month threshold is an explicit working assumption for screening pilot records only; the protocol should define it before the review search is run. Scope confirmation was not requested because the user asked not to pause.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety-related disorders | search | The target condition is central, searchable, and represented by controlled vocabulary and title/abstract terms. |
| Cognitive behavioral therapy | search | The intervention defines the review topic and has searchable controlled vocabulary and text variants. |
| Long-term outcomes / follow-up | screen | Follow-up duration and outcomes are eligibility features and are inconsistently reported in searchable fields. |
| Comparators | screen | Comparators are not required to identify eligible CBT intervention studies. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2017-08-24
- Total records: 15,738 (15,795 before limits)
- Limits and filters: `("1800/01/01"[dp] : "2017/08/24"[dp])` (Publication-date cutoff required by this run: include records published through 2017-08-24 and exclude later publications.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Anxiety Disorders"[Mesh]` | 75,155 |
| 2 | `"Phobic Disorders"[Mesh]` | 12,282 |
| 3 | `"Panic Disorder"[Mesh]` | 6,597 |
| 4 | `"Obsessive-Compulsive Disorder"[Mesh]` | 14,139 |
| 5 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 28,555 |
| 6 | `anxi*[tiab]` | 167,029 |
| 7 | `phobi*[tiab]` | 10,712 |
| 8 | `agoraphobi*[tiab]` | 3,183 |
| 9 | `panic[tiab]` | 13,408 |
| 10 | `"panic disorder"[tiab]` | 8,365 |
| 11 | `"social anxiety"[tiab]` | 4,792 |
| 12 | `"obsessive compulsive"[tiab]` | 15,107 |
| 13 | `"obsessive-compulsive"[tiab]` | 15,107 |
| 14 | `OCD[tiab]` | 7,878 |
| 15 | `PTSD[tiab]` | 18,640 |
| 16 | `"post-traumatic stress"[tiab]` | 9,637 |
| 17 | `"posttraumatic stress"[tiab]` | 16,639 |
| 18 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 245,854 |
| 19 | `Cognitive Therapy[Mesh]` | 24,064 |
| 20 | `"Behavior Therapy"[Mesh]` | 66,990 |
| 21 | `"cognitive behavioral therapy"[tiab]` | 6,806 |
| 22 | `"cognitive behaviour therapy"[tiab]` | 1,404 |
| 23 | `"cognitive behavior therapy"[tiab]` | 1,954 |
| 24 | `"cognitive behavioral treatment"[tiab]` | 1,140 |
| 25 | `"cognitive behavioural treatment"[tiab]` | 336 |
| 26 | `"cognitive behavior treatment"[tiab]` | 31 |
| 27 | `"cognitive behaviour treatment"[tiab]` | 11 |
| 28 | `"cognitive behavioral intervention"[tiab]` | 539 |
| 29 | `"cognitive behavioural intervention"[tiab]` | 162 |
| 30 | `"cognitive behavior intervention"[tiab]` | 11 |
| 31 | `"cognitive behaviour intervention"[tiab]` | 2 |
| 32 | `CBT[tiab]` | 8,158 |
| 33 | `"cognitive therapy"[tiab]` | 2,592 |
| 34 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 72,609 |
| 35 | `#18 AND #34` | 15,795 |
| 36 | `#35 AND ("1800/01/01"[dp] : "2017/08/24"[dp])` | 15,738 |

### Strategy (single line, for copying into PubMed)

```text
(("Anxiety Disorders"[Mesh] OR "Phobic Disorders"[Mesh] OR "Panic Disorder"[Mesh] OR "Obsessive-Compulsive Disorder"[Mesh] OR "Stress Disorders, Post-Traumatic"[Mesh] OR anxi*[tiab] OR phobi*[tiab] OR agoraphobi*[tiab] OR panic[tiab] OR "panic disorder"[tiab] OR "social anxiety"[tiab] OR "obsessive compulsive"[tiab] OR "obsessive-compulsive"[tiab] OR OCD[tiab] OR PTSD[tiab] OR "post-traumatic stress"[tiab] OR "posttraumatic stress"[tiab]) AND (Cognitive Therapy[Mesh] OR "Behavior Therapy"[Mesh] OR "cognitive behavioral therapy"[tiab] OR "cognitive behaviour therapy"[tiab] OR "cognitive behavior therapy"[tiab] OR "cognitive behavioral treatment"[tiab] OR "cognitive behavioural treatment"[tiab] OR "cognitive behavior treatment"[tiab] OR "cognitive behaviour treatment"[tiab] OR "cognitive behavioral intervention"[tiab] OR "cognitive behavioural intervention"[tiab] OR "cognitive behavior intervention"[tiab] OR "cognitive behaviour intervention"[tiab] OR CBT[tiab] OR "cognitive therapy"[tiab])) AND (("1800/01/01"[dp] : "2017/08/24"[dp]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety_disorders | 72,609 | 0 |
| cognitive_behavioral_therapy | 245,854 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 9,683 | initial | none | Initial two-block strategy: MeSH and text terms for anxiety-related diagnoses and CBT; long-term follow-up screened, with the run-mandated publication cutoff. |
| 2 | 6,073 | anxiety_disorders: +5 / -5; cognitive_behavioral_therapy: +1 / -1 | none | Quoted MeSH descriptors to remove automatic term mapping dependence and used the Cognitive Therapy heading label current before 2019. No known records lost. |
| 3 | 9,683 | cognitive_behavioral_therapy: +1 / -1 | none | Replaced a quoted, unmapped legacy MeSH label with the 2017 Cognitive Therapy[Mesh] label; PubMed translates it to the current CBT MeSH heading. Retained as searchable controlled vocabulary and verified retrieval. |
| 4 | 15,738 | cognitive_behavioral_therapy: +5 / -0 | none | Addressed round-1 critique: added Behavior Therapy[Mesh] and American/British intervention phrase variants; no known relevant records lost. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 4 findings; F1 document resolved, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 455 NCBI requests logged (228 from cache); strategy sha256 ae680a27660f._

## Rationale

The strategy requires two concepts: anxiety-related disorders and cognitive behavioral therapy. Anxiety and CBT define the topic and are represented in MeSH and title/abstract text. “Long-term outcomes” is left for screening because follow-up duration and outcomes are not consistently named in abstracts; comparator is also screened. For development screening only, long term was treated as at least six months after treatment. The review protocol should set its own follow-up threshold before screening begins.

The condition block includes exploded Anxiety Disorders, Phobic Disorders, Panic Disorder, Obsessive-Compulsive Disorder, and Stress Disorders, Post-Traumatic headings, plus spelling and wording variants. This assumes “anxiety-related disorders” includes OCD and PTSD as well as anxiety disorders and phobias. The intervention block includes the historical `Cognitive Therapy[Mesh]` label and `Behavior Therapy[Mesh]`, with text variants for therapy, treatment, and intervention. PubMed translated `Cognitive Therapy[Mesh]` to the current CBT MeSH term; the translation warning was retained in the audit trail. No `:noexp` terms were used. The publication-date cutoff through 2017-08-24 was required by the run instructions. No age, language, or study-design filters were applied.

## How known records were found

No user-supplied seed articles were available. A PubMed pilot for anxiety-related conditions, CBT, and follow-up wording returned a sample of 100 titles. Seven plausible primary studies were fetched with abstracts; five met the working condition/intervention/at-least-six-month follow-up criteria and were added to the `relevant` development set. Two were excluded because their stated follow-up was only one or three months. PubMed searches also identified and abstract-screened prior reviews on pediatric anxiety, older adults, and transdiagnostic CBT. Their included-study lists were not extracted, so no benchmark set was created. No records were held out; all five screened records were used as development checks. Their 100% relative recall is not independent validation and is not an estimate of sensitivity.

## Critic dispositions

- F1 (document): resolved. The `psb eval` translation shows the field-tagged `Cognitive Therapy[Mesh]` term mapped to `"cognitive behavioral therapy"[MeSH Terms]` and returned records.
- F2 (should-fix): resolved. Added `"Behavior Therapy"[Mesh]`; the final count rose, and no known development record was lost.
- F3 (should-fix): resolved. Added American and British spelling/order variants for cognitive behavioral intervention phrases; no known development record was lost.
- F4 (document): accepted risk. No user-supplied seeds or independent validation records were available. The five records remain a small development set.

## Open risks for peer review

The phrase “anxiety-related disorders” may or may not include OCD and PTSD; this draft includes both to preserve recall. The six-month follow-up threshold is an assumption, not user-confirmed protocol eligibility. Only five screened development records were available, so the strategy has weak empirical validation despite retrieving all five. The `Cognitive Therapy[Mesh]` translation should be checked against the intended historical PubMed/MeSH version. This PubMed-only strategy will miss records not indexed in PubMed and needs PRESS peer review by an information specialist before use.

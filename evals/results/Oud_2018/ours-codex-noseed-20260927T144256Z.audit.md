# PubMed search strategy: audit

Generated 2026-09-27T14:56:22+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Specialized psychotherapies for adults with borderline personality disorder
- Framework: PICO (intervention effectiveness; psychotherapy types screened rather than separately required)
- Scope confirmed by user: no (No known relevant articles were supplied. User requested no questions or pause; scope choices are assumptions and proceeded without confirmation. Requested historical cutoff treated as PubMed entry-date bound through 2015-03-27. No language, age, or study-design PubMed limits applied; age and specialized modality are screened. No web search or post-cutoff literature used. The publication-date restriction is a task-imposed historical limit, recorded explicitly after internal critique; it is separate from PubMed entry-date bound as_of.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Borderline personality disorder | search | Target condition; reliably named in text and indexed. |
| Psychotherapy | search | Intervention class in the question; specialized modalities will be screened and common named forms included as within-block vocabulary. |
| Adults | screen | Age indexing and abstract reporting can be incomplete; assess adult eligibility at screening. |
| Specialized psychotherapy modality | screen | Specific modalities vary and may be inconsistently named; screen whether an eligible specialized psychotherapy is evaluated. |
| Comparators, outcomes, and study design | screen | Not required in the topic query; screen intervention evaluation and eligible study designs. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2015-03-27
- Total records: 1,880 (1,883 before limits)
- Limits and filters: `1800/01/01:2015/03/27[dp]` (User requested a historical search as of 2015-03-27 and explicitly excluded literature published after that date. The workspace separately applies the PubMed entry-date cutoff.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `Borderline Personality Disorder[Mesh]` | 5,413 |
| 2 | `"borderline personality disorder"[tiab]` | 4,215 |
| 3 | `"borderline personality disorders"[tiab]` | 271 |
| 4 | `"borderline personality"[tiab]` | 4,863 |
| 5 | `"personality disorder, borderline"[tiab]` | 22 |
| 6 | `"borderline personality pathology"[tiab]` | 35 |
| 7 | `BPD[tiab]` | 6,222 |
| 8 | `"emotionally unstable personality disorder"[tiab]` | 24 |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 10,830 |
| 10 | `Psychotherapy[Mesh]` | 165,482 |
| 11 | `Behavior Therapy[Mesh]` | 57,482 |
| 12 | `Psychoanalytic Therapy[Mesh]` | 15,004 |
| 13 | `psychotherap*[tiab]` | 37,596 |
| 14 | `"psychological therap*"[tiab]` | 1,199 |
| 15 | `"psychological treatment"[tiab]` | 1,719 |
| 16 | `"psychological treatments"[tiab]` | 1,048 |
| 17 | `"behavior therap*"[tiab]` | 3,612 |
| 18 | `"behaviour therap*"[tiab]` | 1,833 |
| 19 | `"dialectical behavio* therap*"[tiab]` | 428 |
| 20 | `"dialectical behavio* treatment"[tiab]` | 4 |
| 21 | `"mentalization-based treatment"[tiab]` | 40 |
| 22 | `"mentalisation-based treatment"[tiab]` | 8 |
| 23 | `"mentalization based treatment"[tiab]` | 40 |
| 24 | `"mentalisation based treatment"[tiab]` | 8 |
| 25 | `"transference-focused psychotherapy"[tiab]` | 46 |
| 26 | `"transference focused psychotherapy"[tiab]` | 46 |
| 27 | `"schema-focused therap*"[tiab]` | 32 |
| 28 | `"schema focused therap*"[tiab]` | 32 |
| 29 | `"schema therap*"[tiab]` | 76 |
| 30 | `STEPPS[tiab]` | 30 |
| 31 | `"systems training for emotional predictability and problem solving"[tiab]` | 16 |
| 32 | `"dynamic deconstructive psychotherapy"[tiab]` | 13 |
| 33 | `"cognitive analytic therap*"[tiab]` | 57 |
| 34 | `"psychodynamic therap*"[tiab]` | 361 |
| 35 | `"interpersonal psychotherapy"[tiab]` | 648 |
| 36 | `"interpersonal therap*"[tiab]` | 270 |
| 37 | `"manual-assisted cognitive treatment"[tiab]` | 3 |
| 38 | `"manual assisted cognitive treatment"[tiab]` | 3 |
| 39 | `"client-centered therap*"[tiab]` | 72 |
| 40 | `"client centred therap*"[tiab]` | 16 |
| 41 | `"general psychiatric management"[tiab]` | 14 |
| 42 | `DBT[tiab]` | 1,420 |
| 43 | `MBT[tiab]` | 1,537 |
| 44 | `TFP[tiab]` | 1,103 |
| 45 | `"cognitive behavioral therap*"[tiab]` | 5,059 |
| 46 | `"cognitive behavioural therap*"[tiab]` | 2,219 |
| 47 | `"cognitive-behavioral therapy"[tiab]` | 4,838 |
| 48 | `"cognitive-behavioural therapy"[tiab]` | 2,146 |
| 49 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48` | 181,413 |
| 50 | `#9 AND #49` | 1,883 |
| 51 | `#50 AND 1800/01/01:2015/03/27[dp]` | 1,880 |

### Strategy (single line, for copying into PubMed)

```text
((Borderline Personality Disorder[Mesh] OR "borderline personality disorder"[tiab] OR "borderline personality disorders"[tiab] OR "borderline personality"[tiab] OR "personality disorder, borderline"[tiab] OR "borderline personality pathology"[tiab] OR BPD[tiab] OR "emotionally unstable personality disorder"[tiab]) AND (Psychotherapy[Mesh] OR Behavior Therapy[Mesh] OR Psychoanalytic Therapy[Mesh] OR psychotherap*[tiab] OR "psychological therap*"[tiab] OR "psychological treatment"[tiab] OR "psychological treatments"[tiab] OR "behavior therap*"[tiab] OR "behaviour therap*"[tiab] OR "dialectical behavio* therap*"[tiab] OR "dialectical behavio* treatment"[tiab] OR "mentalization-based treatment"[tiab] OR "mentalisation-based treatment"[tiab] OR "mentalization based treatment"[tiab] OR "mentalisation based treatment"[tiab] OR "transference-focused psychotherapy"[tiab] OR "transference focused psychotherapy"[tiab] OR "schema-focused therap*"[tiab] OR "schema focused therap*"[tiab] OR "schema therap*"[tiab] OR STEPPS[tiab] OR "systems training for emotional predictability and problem solving"[tiab] OR "dynamic deconstructive psychotherapy"[tiab] OR "cognitive analytic therap*"[tiab] OR "psychodynamic therap*"[tiab] OR "interpersonal psychotherapy"[tiab] OR "interpersonal therap*"[tiab] OR "manual-assisted cognitive treatment"[tiab] OR "manual assisted cognitive treatment"[tiab] OR "client-centered therap*"[tiab] OR "client centred therap*"[tiab] OR "general psychiatric management"[tiab] OR DBT[tiab] OR MBT[tiab] OR TFP[tiab] OR "cognitive behavioral therap*"[tiab] OR "cognitive behavioural therap*"[tiab] OR "cognitive-behavioral therapy"[tiab] OR "cognitive-behavioural therapy"[tiab])) AND (1800/01/01:2015/03/27[dp])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 18 | 18 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bpd | 181,413 | 0 |
| psychotherapy | 10,830 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,880 | initial | none | Initial two-block recall-first draft; includes current historical MeSH and text terms, with adult and modality eligibility screened. |
| 2 | 1,880 | psychotherapy: +4 / -4 | none | Removed duplicate vocabulary, an unmatched phrase, and a short truncation; omitted Cognitive Behavioral Therapy MeSH because that descriptor was introduced in 2019, after the requested date. Kept eligibility by age and named modality for screening. |
| 3 | 1,880 | limits/combination | none | Corrected set provenance: eight screened candidates were linked from the prior review but not verified as included studies; reclassified them as relevant discoveries, not an external benchmark. This makes all relative recall development-only. |
| 4 | 1,880 | limits/combination | none | Kept development records under one relevant set and removed empty, unverified benchmark; critic disposition records that independent validation was unavailable and development recall is non-independent. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F1 must-fix accepted-risk
- Round 2 on version 3: 2 findings; F1 must-fix accepted-risk, F2 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 713 NCBI requests logged (364 from cache); strategy sha256 458a76ca20b6._


## Rationale

Borderline personality disorder and psychotherapy are the only AND-ed concepts because both define the review topic and can be searched reliably. Adults and the exact specialized modality remain screening criteria, as both can be incompletely reported or inconsistently named. Comparators, outcomes, and study designs are also screened. The strategy combines the exploded `Psychotherapy[Mesh]` heading with `Behavior Therapy[Mesh]` and `Psychoanalytic Therapy[Mesh]`, plus `[tiab]` text terms for general psychotherapy wording and named approaches. No age or study-design filter is used. The date range is retained because the task explicitly requires a 2015-03-27 cutoff. The evaluator reported Automatic Term Mapping warnings for explicitly tagged MeSH phrases; the translation evidence shows them mapped as MeSH terms.

## How known records were found

The user supplied no known records. At standard depth, a PubMed search identified the Cochrane systematic review *Psychological therapies for people with borderline personality disorder* (PMID 22895952), and its PubMed linked-reference/neighbor candidates were used for discovery. I screened the 49 returned candidate records' abstracts against the stated eligibility criteria; 18 primary empirical psychotherapy records were included as `relevant`. Ten were used for vocabulary ranking and eight were held aside from term mining during drafting, but the candidate pool was not a verified list of the prior review's included studies. All 18 are therefore reported as development records, not an independent validation set or external benchmark. No independent recall estimate is available.

## Critic dispositions

- Round 1 finding F1 (date limit missing from scope summary): accepted as a task-imposed restriction. The protocol now records the publication-date cutoff and its reason.
- Round 2 finding F2 (no independent benchmark): accepted as a limitation because no user seeds or verified independent included-study set were available in this run. The audit labels all measured recall as development relative recall.
- The internal critic found no open must-fix findings. This is PRESS-structured internal QA, not information-specialist peer review.

## Open risks for the peer reviewer

The relative recall of 18/18 applies only to the screened development records and does not estimate sensitivity for the full eligible literature. Broad acronyms (`BPD`, `DBT`, `MBT`, and `TFP`) and the broad psychotherapy MeSH explosion are retained for sensitivity and may add noise. Adult status and whether a modality meets the protocol's definition of "specialized or structured" require screening. Please verify the scope and date cutoff and have an information specialist conduct PRESS peer review before the search is used.

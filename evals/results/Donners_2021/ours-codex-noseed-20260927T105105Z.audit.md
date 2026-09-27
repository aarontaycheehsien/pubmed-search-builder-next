# PubMed search strategy: audit

Generated 2026-09-27T11:05:58+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In humans, what are the pharmacokinetics of emicizumab and their association with efficacy in haemophilia A?
- Framework: PECO/exposure-focused drug review
- Scope confirmed by user: no (The user requested no questions, so scope roles and limits were set from the supplied eligibility and were not user-confirmed. No known relevant articles were supplied. Standard-depth discovery used PubMed/MeSH through psb only; no web search was used. PubMed requests were bounded by Entry Date through 2020-10-22. The systematic[sb] pilot with emicizumab plus pharmacokinetic/pharmacometric terms found no PK-focused review; two broader review candidates were not converted into a benchmark set. No publication-language, population, design, or substantive publication-date limit was applied. Ten eligible primary records were screened: seven development records used for vocabulary mining and three held out from mining for validation.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Emicizumab, ACE910, or factor VIII-mimetic bispecific antibody | search | The drug is the defining searchable topic and should be named reliably in titles, abstracts, or MeSH. |
| Humans with haemophilia A, including healthy-volunteer bridging studies | screen | Humans and population eligibility can be screened; human filters risk excluding unindexed studies and healthy-volunteer bridging work. |
| Pharmacokinetics/exposure and associated efficacy or bleeding rate | screen | Eligibility allows PK/exposure and/or associated efficacy; reporting terms are inconsistent and should not be required as an AND block. |
| Clinical trial, pharmacokinetic, or pharmacometric study | screen | Design labels vary; eligibility is determined during screening rather than with an unvalidated study-design filter. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2020-10-22
- Total records: 234
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `emicizumab[nm]` | 161 |
| 2 | `emicizumab[tiab]` | 193 |
| 3 | `ACE910[tiab]` | 29 |
| 4 | `"ACE 910"[tiab]` | 1 |
| 5 | `"ACE-910"[tiab]` | 1 |
| 6 | `"emicizumab-kxwh"[tiab]` | 3 |
| 7 | `Hemlibra[tiab]` | 13 |
| 8 | `"factor VIII mimetic"[tiab]` | 8 |
| 9 | `"factor VIII-mimetic"[tiab]` | 8 |
| 10 | `"anti-factor IXa/X bispecific antibody"[tiab]` | 4 |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 234 |

### Strategy (single line, for copying into PubMed)

```text
(emicizumab[nm] OR emicizumab[tiab] OR ACE910[tiab] OR "ACE 910"[tiab] OR "ACE-910"[tiab] OR "emicizumab-kxwh"[tiab] OR Hemlibra[tiab] OR "factor VIII mimetic"[tiab] OR "factor VIII-mimetic"[tiab] OR "anti-factor IXa/X bispecific antibody"[tiab])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,746 | initial | none | Initial single-block emicizumab strategy; specific drug supplementary concept, bispecific antibody MeSH descriptor, and development-name, brand, and mechanism phrase variants. No population, outcome, design, or language filters. |
| 2 | 2,746 | emicizumab: +0 / -1 | none | Removed one quoted phrase PubMed reported as not found; no relevant set record depended on it. |
| 3 | 234 | emicizumab: +0 / -1 | none | Dropped the generic Antibodies, Bispecific MeSH descriptor after its 2,683-record line count and a 20-record random sample showed broad unrelated antibody/cancer and molecular-engineering literature. The specific emicizumab Supplementary Concept term remains as the controlled-vocabulary layer; no development record was lost. |
| 4 | 234 | emicizumab: +1 / -0 | none | Added the spaced ACE 910 variant after the critic identified it; PubMed reported one result (PMID 30398480), a review record that was not added to the eligible development set. All seven known relevant records remain retrieved. PubMed normalizes emicizumab[nm] to emicizumab[Supplementary Concept] (count 161); this is the intended drug-specific supplementary heading. |
| 5 | 234 | limits/combination | none | Re-evaluated against three additional screened records reserved as a held-out validation set after vocabulary mining; all three were retrieved. No terms were mined from this set and no strategy change was made. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; F1 should-fix open, F2 should-fix open
- Round 2 on version 4: 2 findings; F1 should-fix resolved, F2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 178 NCBI requests logged (63 from cache); strategy sha256 2a2ba460f7e6._

## Rationale

Only emicizumab/ACE910 is AND-required because it defines the drug exposure under review and is reliably named or indexed. Humans (including healthy-volunteer bridging studies), PK/exposure or bleeding-rate outcomes, and clinical/pharmacometric design remain screening criteria. No validated human or study-design filter was needed, and no population, language, or substantive date limit was applied. PubMed's specific emicizumab supplementary concept was queried as `emicizumab[nm]`; PubMed normalizes it to `"emicizumab"[Supplementary Concept]` (161 records under the workspace bound). This is the expected specific heading mapping, not a broad automatic expansion. Name and mechanism free-text variants cover records without that heading. A generic `"Antibodies, Bispecific"[Mesh]` term was tested but removed: its line count was 2,683 and a random sample showed unrelated antibody/cancer and molecular-engineering records. One unused phrase reported by PubMed as not found was also removed.

## How known records were found

No user-supplied seeds were available. At standard depth, PubMed pilot searches covered emicizumab/ACE910 with PK, pharmacometric, exposure, or bleeding language, plus a review search. Twelve records were screened from titles and abstracts within the requested cutoff: ten eligible primary clinical/pharmacology records and two excluded records (a safety-focused analysis without eligible PK/exposure or efficacy reporting, and a narrative review). Seven eligible records were assigned to the development set and used for term mining (PMIDs 30230257, 29296836, 29214439, 28691557, 31003963, 26626991, 32504271). Three eligible records were held out from term mining and used for semi-independent validation (PMIDs 31697801, 31515851, 27223146). All ten were retrieved. A targeted emicizumab systematic-review search with pharmacokinetic/pharmacometric terms returned zero records; a broader `systematic[sb]` search returned two review candidates, but no review-derived benchmark set was assembled. The reference-neighbor lookup for one candidate returned zero candidates.

## Critic dispositions

Two fresh-context PRESS-structured internal critique rounds were completed. Round 1 asked to document the supplementary-heading translation and add the spaced `ACE 910` variant. The strategy includes `"ACE 910"[tiab]` (one record); all seven development records remained retrieved. PubMed's reported normalization of `emicizumab[nm]` to `"emicizumab"[Supplementary Concept]` was verified and documented. Both findings were marked resolved in round 2. The automated critique is internal QA and is not an information-specialist PRESS peer review.

## Open risks for the peer reviewer

There were no known user-supplied seeds and no review-derived benchmark, so development recall is not independent and the three-record validation set is small and semi-independent. The final 234-record count is topic-only; eligibility and study design still require screening. The `as_of` boundary constrains PubMed Entry Date through 2020-10-22, while the copied strategy itself has no publication-date limit; counts run at a later date may differ. Please verify current PubMed translation, terminology, and final syntax before execution, and check whether other databases or trial registries are needed for the review.

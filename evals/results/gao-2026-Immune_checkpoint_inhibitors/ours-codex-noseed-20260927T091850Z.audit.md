# PubMed search strategy: audit

Generated 2026-09-27T09:36:50+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Immune checkpoint inhibitors plus chemotherapy for early triple-negative breast cancer
- Framework: PICO (intervention effectiveness)
- Scope confirmed by user: no (User requested no questions during this run; scope and roles were decided from the question without confirmation. Interpreted early as non-metastatic/curative-intent disease and will screen stage, neoadjuvant/adjuvant, and treatment intent rather than AND them. Combination intervention block requires both checkpoint-inhibitor and chemotherapy vocabulary. No language, study-design, or other limits. Historical search cutoff is 2025-01-31 (PubMed entry date). The PubMed strategy also applies an explicit publication-date range through 2025-01-31 because the tool's as_of setting independently bounds PubMed entry date.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Triple-negative breast cancer | search | Core population condition, reliably named and indexed; searching the broad condition supports retrieval where early-stage status is omitted. |
| Immune checkpoint inhibitor with chemotherapy | search | The combination intervention defines the review topic; both components are required within this block. |
| Early-stage/non-metastatic disease | screen | Eligibility property often omitted or variably phrased in titles and abstracts; assess at screening. |
| Clinical outcomes | screen | Outcomes are not specified and should not be required in the search. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2025-01-31
- Total records: 1,587 (1,591 before limits)
- Limits and filters: `("1800/01/01"[dp] : "2025/01/31"[dp])` (Required by the review protocol and user instruction: exclude records with a publication date after 2025-01-31.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Triple Negative Breast Neoplasms"[Mesh]` | 12,839 |
| 2 | `"triple negative breast cancer"[tiab]` | 19,872 |
| 3 | `"triple-negative breast cancer"[tiab]` | 19,872 |
| 4 | `"triple negative breast neoplasm"[tiab]` | 12 |
| 5 | `"triple-negative breast neoplasm"[tiab]` | 12 |
| 6 | `"triple negative breast carcinoma"[tiab]` | 308 |
| 7 | `"triple-negative breast carcinoma"[tiab]` | 308 |
| 8 | `TNBC[tiab]` | 14,325 |
| 9 | `eTNBC[tiab]` | 18 |
| 10 | `"ER-negative PR-negative HER2-negative breast cancer"[tiab]` | 2 |
| 11 | `"ER negative PR negative HER2 negative breast cancer"[tiab]` | 2 |
| 12 | `("ER-negative"[tiab] AND "HER2-negative"[tiab] AND breast[tiab])` | 286 |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 22,892 |
| 14 | `(("Immune Checkpoint Inhibitors"[Mesh] OR "Antineoplastic Agents, Immunological"[Mesh] OR "Programmed Cell Death 1 Receptor"[Mesh] OR "B7-H1 Antigen"[Mesh] OR "CTLA-4 Antigen"[Mesh] OR "Nivolumab"[Mesh] OR "Ipilimumab"[Mesh] OR "pembrolizumab"[Supplementary Concept] OR "atezolizumab"[Supplementary Concept] OR "durvalumab"[Supplementary Concept] OR "avelumab"[Supplementary Concept] OR "cemiplimab"[Supplementary Concept] OR "Immunotherapy"[Mesh] OR immunotherap*[tiab] OR "immune checkpoint inhibitor"[tiab] OR "immune checkpoint inhibitors"[tiab] OR "checkpoint inhibitor"[tiab] OR "checkpoint inhibitors"[tiab] OR "checkpoint blockade"[tiab] OR "PD-1 inhibitor"[tiab] OR "PD-1 inhibitors"[tiab] OR "PD-L1 inhibitor"[tiab] OR "PD-L1 inhibitors"[tiab] OR "anti-PD-1"[tiab] OR "anti-PD-L1"[tiab] OR pembrolizumab[tiab] OR atezolizumab[tiab] OR durvalumab[tiab] OR nivolumab[tiab] OR avelumab[tiab] OR ipilimumab[tiab] OR cemiplimab[tiab] OR dostarlimab[tiab] OR tislelizumab[tiab] OR toripalimab[tiab]) AND ("Antineoplastic Combined Chemotherapy Protocols"[Mesh] OR "Chemotherapy, Adjuvant"[Mesh] OR chemotherap*[tiab] OR cytotoxic*[tiab] OR taxane*[tiab] OR anthracycline*[tiab] OR platinum[tiab] OR carboplatin[tiab] OR cisplatin[tiab] OR paclitaxel[tiab] OR "nab-paclitaxel"[tiab] OR docetaxel[tiab] OR doxorubicin[tiab] OR epirubicin[tiab] OR cyclophosphamide[tiab] OR fluorouracil[tiab] OR gemcitabine[tiab]))` | 88,617 |
| 15 | `#14` | 88,617 |
| 16 | `#13 AND #15` | 1,591 |
| 17 | `#16 AND ("1800/01/01"[dp] : "2025/01/31"[dp])` | 1,587 |

### Strategy (single line, for copying into PubMed)

```text
(("Triple Negative Breast Neoplasms"[Mesh] OR "triple negative breast cancer"[tiab] OR "triple-negative breast cancer"[tiab] OR "triple negative breast neoplasm"[tiab] OR "triple-negative breast neoplasm"[tiab] OR "triple negative breast carcinoma"[tiab] OR "triple-negative breast carcinoma"[tiab] OR TNBC[tiab] OR eTNBC[tiab] OR "ER-negative PR-negative HER2-negative breast cancer"[tiab] OR "ER negative PR negative HER2 negative breast cancer"[tiab] OR ("ER-negative"[tiab] AND "HER2-negative"[tiab] AND breast[tiab])) AND ((("Immune Checkpoint Inhibitors"[Mesh] OR "Antineoplastic Agents, Immunological"[Mesh] OR "Programmed Cell Death 1 Receptor"[Mesh] OR "B7-H1 Antigen"[Mesh] OR "CTLA-4 Antigen"[Mesh] OR "Nivolumab"[Mesh] OR "Ipilimumab"[Mesh] OR "pembrolizumab"[Supplementary Concept] OR "atezolizumab"[Supplementary Concept] OR "durvalumab"[Supplementary Concept] OR "avelumab"[Supplementary Concept] OR "cemiplimab"[Supplementary Concept] OR "Immunotherapy"[Mesh] OR immunotherap*[tiab] OR "immune checkpoint inhibitor"[tiab] OR "immune checkpoint inhibitors"[tiab] OR "checkpoint inhibitor"[tiab] OR "checkpoint inhibitors"[tiab] OR "checkpoint blockade"[tiab] OR "PD-1 inhibitor"[tiab] OR "PD-1 inhibitors"[tiab] OR "PD-L1 inhibitor"[tiab] OR "PD-L1 inhibitors"[tiab] OR "anti-PD-1"[tiab] OR "anti-PD-L1"[tiab] OR pembrolizumab[tiab] OR atezolizumab[tiab] OR durvalumab[tiab] OR nivolumab[tiab] OR avelumab[tiab] OR ipilimumab[tiab] OR cemiplimab[tiab] OR dostarlimab[tiab] OR tislelizumab[tiab] OR toripalimab[tiab]) AND ("Antineoplastic Combined Chemotherapy Protocols"[Mesh] OR "Chemotherapy, Adjuvant"[Mesh] OR chemotherap*[tiab] OR cytotoxic*[tiab] OR taxane*[tiab] OR anthracycline*[tiab] OR platinum[tiab] OR carboplatin[tiab] OR cisplatin[tiab] OR paclitaxel[tiab] OR "nab-paclitaxel"[tiab] OR docetaxel[tiab] OR doxorubicin[tiab] OR epirubicin[tiab] OR cyclophosphamide[tiab] OR fluorouracil[tiab] OR gemcitabine[tiab])))) AND (("1800/01/01"[dp] : "2025/01/31"[dp]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 6 | 6 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| tnbc | 88,617 | 0 |
| regimen | 22,892 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,054 | initial | none | Initial draft: two recall-first blocks from question scope. Early-stage status remains for screening; MeSH plus title/abstract terms used for TNBC and both components of regimen. |
| 2 | 1,054 | regimen: +1 / -1 | none | Expanded benchmark with a separately screened KEYNOTE-522 survival report from an early-stage TNBC systematic review's reference set; made supplementary-concept field tags explicit after PubMed translation warning. |
| 3 | 1,054 | regimen: +1 / -1 | none | Quoted supplementary-concept names to make the field-tagged drug headings explicit in PubMed syntax; benchmark set contains six screened early-TNBC treatment reports. |
| 4 | 1,591 | regimen: +1 / -1 | none | Addressed critic finding F1 by adding generic Immunotherapy MeSH and immunotherap* title/abstract terms as a recall backstop; reviewed count and benchmark retention. |
| 5 | 1,591 | limits/combination | none | Added the eligible January 2025 ALEXANDRA/IMpassion030 report found in the search-result sample to the development set; the screened commentary PMID 39881092 was excluded. |
| 6 | 1,587 | limits/combination | none | Added the user-required publication-date range through 2025-01-31; the workspace as_of bound independently limits PubMed entry date through that date. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (Same-context critic: no separate fresh-context reviewer was available; reviewed the packet independently against the six PRESS domains.): 1 findings; F1 should-fix open
- Round 2 on version 6 (Same-context critic: no separate fresh-context reviewer was available; reviewed the updated packet independently against the six PRESS domains.): 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 399 NCBI requests logged (172 from cache); strategy sha256 dd4334d63200._


## Rationale

- The two searched concepts are triple-negative breast cancer and the combined checkpoint-inhibitor/chemotherapy intervention. Early-stage status remains a screening decision because it may be expressed as primary, resectable, neoadjuvant, adjuvant, stage II/III, or not repeated in the abstract. Outcomes are not searched.
- The population block uses the exploded MeSH heading `Triple Negative Breast Neoplasms` and title/abstract wording for the full phrase, acronym, and receptor-negative descriptions. Hyphenated and spaced forms are included; PubMed normalizes some of these to identical translations.
- The intervention block includes class and target MeSH, specific checkpoint drugs (including supplementary concepts), generic immunotherapy terms, and title/abstract drug names. Its chemotherapy half combines the MeSH headings for antineoplastic combination protocols and adjuvant chemotherapy with chemotherapy wording and common regimen agents. Both halves must match.
- No MeSH headings were restricted with `:noexp`. No study design, language, age, or population limit was applied. The only explicit limit is the user-required publication-date range through 2025-01-31. The workspace also applies the same `as_of` cutoff to PubMed entry date.

## How known records were found

No user-supplied seeds were available. PubMed searches identified relevant prior reviews, including PMIDs 39207778, 37612624, 33482345, and 36412440. Reference candidates were gathered from two review citation lists (37 and 25 records; 62 list entries total, with overlap possible) and title-screened; abstracts were fetched for records appearing potentially eligible. Six early-TNBC treatment reports became the benchmark: PMIDs 31095287, 32053137, 32101663, 32966830, 35139274, and 35182721. The benchmark is composed of reports from prior reviews and is an external relative-recall check, not a held-out validation sample.

A 12-record sample from the final topic search was also title-screened. The January 2025 ALEXANDRA/IMpassion030 report (PMID 39883436) met eligibility and was added as a development record. A commentary (PMID 39881092) was excluded. No separate validation set was held out. Relative recall was 6/6 (100%) against the benchmark and 1/1 (100%) against the development set; these figures do not estimate absolute sensitivity.

## Critic dispositions

Both reviews were same-context PRESS-structured internal critiques because no separate fresh-context reviewer was available. Round 1 raised F1 (should-fix): generic immunotherapy wording could provide a backstop when abstracts omit a drug name or explicit checkpoint label. Round 2 marked F1 resolved after adding `"Immunotherapy"[Mesh]` and `immunotherap*[tiab]`; the search retained every known record. The publication-date limit was subsequently added to honor the user?s exact cutoff and evaluated separately, retaining all seven known records. No must-fix findings remain. This internal review is not PRESS peer review.

## Open risks for the peer reviewer

- The broad immunotherapy safety net and checkpoint/chemotherapy combination terms are intended to favor recall; some records will be irrelevant and require screening.
- Early-stage eligibility is deliberately not an AND block, so locally advanced, metastatic, mixed-stage, or unclear-stage records may appear.
- The benchmark contains six reports drawn from prior reviews, and the development check contains one record found in the strategy sample. There is no independent held-out validation set; 100% relative recall on these sets should not be interpreted as sensitivity.
- The publication-date filter and PubMed entry-date cutoff are both applied. Records with ambiguous or corrected publication dates may need manual date review.

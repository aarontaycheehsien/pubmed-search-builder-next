# PubMed search strategy: audit

Generated 2026-09-27T11:23:30+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: no (The user asked not to be queried during this run. Assumed a broad PCC-style topic question and provisionally AND-ed viral metagenomics with terrestrial farm-animal population (livestock and poultry); farmed fish/aquaculture is excluded. No language, geography or study-design limits. Publication date bound is 2019-02-22 inclusive; records after that date are out of scope. No known relevant articles were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Virus metagenomics | search | The method and viral subject define the topic; include metagenomics, virome, viral sequencing and related indexed terminology. |
| Farm animals | search | The population is explicit in the question; include broad livestock, poultry and farmed animal wording and species headings. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2019-02-22
- Total records: 822 (824 before limits)
- Limits and filters: `("1800/01/01"[dp] : "2019/02/22"[dp])` (Required by the historical 2019-02-22 search date. The workspace also bounds PubMed entry date to that date.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `("Metagenomics"[Mesh] AND "Viruses"[Mesh])` | 693 |
| 2 | `("Viruses"[Mesh] AND "High-Throughput Nucleotide Sequencing"[Mesh])` | 2,566 |
| 3 | `virom*[tiab]` | 824 |
| 4 | `(metagenom*[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab]))` | 1,969 |
| 5 | `((virus*[tiab] OR viral[tiab] OR phage*[tiab]) AND ("deep sequencing"[tiab] OR "next generation sequencing"[tiab] OR "high throughput sequencing"[tiab] OR "shotgun sequencing"[tiab] OR "unbiased sequencing"[tiab] OR "sequence independent"[tiab] OR "sequence-independent"[tiab]))` | 4,600 |
| 6 | `#1 OR #2 OR #3 OR #4 OR #5` | 7,408 |
| 7 | `"Animals, Domestic"[Mesh]` | 34,427 |
| 8 | `"Livestock"[Mesh]` | 3,200 |
| 9 | `"Poultry"[Mesh]` | 147,415 |
| 10 | `"Cattle"[Mesh]` | 341,776 |
| 11 | `"Swine"[Mesh]` | 214,731 |
| 12 | `"Goats"[Mesh]` | 30,623 |
| 13 | `"Sheep"[Mesh]` | 116,801 |
| 14 | `"Horses"[Mesh]` | 67,676 |
| 15 | `"Chickens"[Mesh]` | 117,975 |
| 16 | `"Ducks"[Mesh]` | 10,534 |
| 17 | `"Turkeys"[Mesh]` | 10,103 |
| 18 | `"farm animal"[tiab]` | 833 |
| 19 | `"farm animals"[tiab]` | 3,038 |
| 20 | `"food animal"[tiab]` | 898 |
| 21 | `"food animals"[tiab]` | 1,313 |
| 22 | `"food-producing animal"[tiab]` | 68 |
| 23 | `"food-producing animals"[tiab]` | 1,032 |
| 24 | `"food producing animal"[tiab]` | 68 |
| 25 | `"food producing animals"[tiab]` | 1,032 |
| 26 | `"production animal"[tiab]` | 126 |
| 27 | `"production animals"[tiab]` | 294 |
| 28 | `livestock[tiab]` | 21,337 |
| 29 | `poultry[tiab]` | 25,731 |
| 30 | `cattle[tiab]` | 79,355 |
| 31 | `bovine*[tiab]` | 190,300 |
| 32 | `cow[tiab]` | 29,456 |
| 33 | `cows[tiab]` | 45,405 |
| 34 | `calf[tiab]` | 43,460 |
| 35 | `calves[tiab]` | 24,856 |
| 36 | `swine[tiab]` | 42,358 |
| 37 | `pig[tiab]` | 127,282 |
| 38 | `pigs[tiab]` | 115,344 |
| 39 | `porcine*[tiab]` | 79,249 |
| 40 | `sheep[tiab]` | 87,044 |
| 41 | `ovine*[tiab]` | 20,472 |
| 42 | `goat*[tiab]` | 31,547 |
| 43 | `caprine*[tiab]` | 3,169 |
| 44 | `horse*[tiab]` | 80,001 |
| 45 | `equine*[tiab]` | 29,201 |
| 46 | `chicken*[tiab]` | 92,941 |
| 47 | `broiler*[tiab]` | 16,896 |
| 48 | `duck*[tiab]` | 13,075 |
| 49 | `turkey[tiab]` | 32,530 |
| 50 | `turkeys[tiab]` | 5,927 |
| 51 | `geese[tiab]` | 1,928 |
| 52 | `goose[tiab]` | 2,645 |
| 53 | `#7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52` | 1,219,850 |
| 54 | `#6 AND #53` | 824 |
| 55 | `#54 AND ("1800/01/01"[dp] : "2019/02/22"[dp])` | 822 |

### Strategy (single line, for copying into PubMed)

```text
((("Metagenomics"[Mesh] AND "Viruses"[Mesh]) OR ("Viruses"[Mesh] AND "High-Throughput Nucleotide Sequencing"[Mesh]) OR virom*[tiab] OR (metagenom*[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab])) OR ((virus*[tiab] OR viral[tiab] OR phage*[tiab]) AND ("deep sequencing"[tiab] OR "next generation sequencing"[tiab] OR "high throughput sequencing"[tiab] OR "shotgun sequencing"[tiab] OR "unbiased sequencing"[tiab] OR "sequence independent"[tiab] OR "sequence-independent"[tiab]))) AND ("Animals, Domestic"[Mesh] OR "Livestock"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Goats"[Mesh] OR "Sheep"[Mesh] OR "Horses"[Mesh] OR "Chickens"[Mesh] OR "Ducks"[Mesh] OR "Turkeys"[Mesh] OR "farm animal"[tiab] OR "farm animals"[tiab] OR "food animal"[tiab] OR "food animals"[tiab] OR "food-producing animal"[tiab] OR "food-producing animals"[tiab] OR "food producing animal"[tiab] OR "food producing animals"[tiab] OR "production animal"[tiab] OR "production animals"[tiab] OR livestock[tiab] OR poultry[tiab] OR cattle[tiab] OR bovine*[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine*[tiab] OR sheep[tiab] OR ovine*[tiab] OR goat*[tiab] OR caprine*[tiab] OR horse*[tiab] OR equine*[tiab] OR chicken*[tiab] OR broiler*[tiab] OR duck*[tiab] OR turkey[tiab] OR turkeys[tiab] OR geese[tiab] OR goose[tiab])) AND (("1800/01/01"[dp] : "2019/02/22"[dp]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| viral_metagenomics | 1,219,850 | 0 |
| farm_animals | 7,408 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 98,650 | initial | none | Initial two-block draft: broad viral metagenomic/sequencing terms AND farm-animal headings/species terms; dates limited by protocol as_of 2019-02-22. |
| 2 | 806 | viral_metagenomics: +4 / -16; farm_animals: +2 / -1 | none | Narrowed the topic block after the first count showed 98,650 records: paired virus headings with metagenomics/sequencing, required virus plus metagenomic or sequencing text except virome; replaced invalid pig* truncation with pig/pigs. |
| 3 | 804 | limits/combination | none | Added the required publication-date limit through 2019-02-22; workspace as_of independently bounds PubMed entry date to the same date. |
| 4 | 822 | farm_animals: +16 / -0 | none | Addressed critic round 1: added food-animal/population phrases and species MeSH headings confirmed in the development records. Recorded the reasonable no-question assumption that farm animals means terrestrial livestock and poultry, excluding aquaculture. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 3 findings; F1 should-fix open, F2 should-fix open, F3 document open
- Round 2 on version 4: 3 findings; F1 should-fix resolved, F2 should-fix resolved, F3 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 513 NCBI requests logged (150 from cache); strategy sha256 f0ded529f54b._

## Rationale

The PCC-style scope searches two concepts: virus metagenomics/virome methods and farm-animal populations. The topic block combines the MeSH headings `Metagenomics`, `Viruses`, and `High-Throughput Nucleotide Sequencing` in paired pathways, with title/abstract terms for metagenomics, virome, viral sequencing, and sequencing approaches. `Virome` was not used as a MeSH heading because the inspected heading was introduced in 2021, after the requested 2019 cutoff; its text terms remain included. The population block uses exploded `Animals, Domestic`, `Livestock`, and `Poultry` headings, species headings present in screened records, and food-animal and species wording. The date range is retained because the run is explicitly frozen at 2019-02-22; PubMed entry date is also bounded to that date in the workspace.

## How known records were found

No articles were supplied. A systematic-review pilot returned zero records. Two dated PubMed pilots returned 472 and 77 records; titles from the pilot samples were screened, and ten candidate abstracts were fetched and reviewed. Nine records were included in the `relevant` development set and one uncertain record was left out because its abstract did not confirm virus-specific metagenomic analysis. No records were held out for validation. The nine records are development evidence only; no independent validation set was available.

## Critic dispositions

- F1: resolved by adding food-animal, food-producing-animal, and production-animal phrases; the scope assumption explicitly excludes aquaculture.
- F2: resolved by adding MeSH headings for cattle, swine, goats, sheep, horses, chickens, ducks, and turkeys.
- F3: accepted risk. The audit reports the nine records as a development set, makes no claim of absolute sensitivity, and states that independent recall was not estimated.

## Open risks for the peer reviewer

The scope assumes "farm animals" means terrestrial livestock and poultry; farmed fish and other aquaculture species are excluded because clarification was unavailable. Exploded `Animals, Domestic` may retrieve companion-animal papers, and broad viral sequencing terms may retrieve studies that do not use metagenomics as intended. The final 20-title sample included likely off-topic or targeted-sequencing records; those broad terms remain to favor sensitivity, and the returned records need screening against eligibility criteria. The 9/9 relative retrieval result is based on records used during development and does not estimate absolute recall. Recall was not independently estimated; the strategy is empirically unvalidated. PRESS peer review by an information specialist remains necessary before use.

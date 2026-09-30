# PubMed search strategy: audit

Generated 2026-09-30T13:49:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC (scoping/topic search)
- Scope confirmed by user: no (User requested a no-wait run and supplied no seed articles; proceeded with these assumptions. 'Farm animals' interpreted broadly as food-producing terrestrial livestock and poultry plus clearly farmed aquatic animals. Search is intentionally sensitive to metagenomic/virome terminology; viral relevance and exact production context can require full-text screening. No publication-date or language limit. The required PubMed Entrez entry-date cutoff is 2019-02-22 via PSB_AS_OF.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viral metagenomics / virome studies | search | Defining method/topic. Search metagenomics and virome terminology with MeSH and free text; no additional AND block for viruses because the vocabulary itself targets viral metagenomic work and many relevant studies may describe viral findings without naming viruses in the title or abstract. |
| Farmed/domesticated animals | search | Population/context requested. Search domestic/farm/livestock terms and relevant animal headings/species; specific species may be named without the umbrella category, so probe as a category. |
| Viral targets/findings | screen | Included records must concern viruses, but papers may report viral analyses or findings without naming them in title/abstract; assess at screening to avoid losing method papers. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:48:08+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 1,079
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Metagenomics[Mesh]` | 5,229 | none |
| 2 | `metagenom*[tiab]` | 11,213 | none |
| 3 | `virome[tiab]` | 667 | none |
| 4 | `virom*[tiab]` | 824 | none |
| 5 | `viral metagenomics[tiab]` | 251 | none |
| 6 | `viral metagenomic*[tiab]` | 343 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 13,013 | none |
| 8 | `Animals, Domestic[Mesh]` | 34,427 | none |
| 9 | `livestock[tiab]` | 21,337 | none |
| 10 | `farm animal*[tiab]` | 3,666 | none |
| 11 | `farm animals[tiab]` | 3,038 | none |
| 12 | `farmed animal*[tiab]` | 195 | none |
| 13 | `domestic animal*[tiab]` | 8,110 | none |
| 14 | `domesticated animal*[tiab]` | 735 | none |
| 15 | `food-producing animal*[tiab]` | 1,078 | none |
| 16 | `cattle[tiab]` | 79,355 | none |
| 17 | `bovine[tiab]` | 189,144 | none |
| 18 | `swine[tiab]` | 42,358 | none |
| 19 | `pig[tiab]` | 127,282 | none |
| 20 | `pigs[tiab]` | 115,325 | none |
| 21 | `porcine[tiab]` | 79,145 | none |
| 22 | `poultry[tiab]` | 25,731 | none |
| 23 | `chicken[tiab]` | 68,650 | none |
| 24 | `chickens[tiab]` | 34,114 | none |
| 25 | `avian[tiab]` | 50,972 | none |
| 26 | `sheep[tiab]` | 87,044 | none |
| 27 | `ovine[tiab]` | 20,361 | none |
| 28 | `goat[tiab]` | 19,304 | none |
| 29 | `goats[tiab]` | 18,753 | none |
| 30 | `caprine[tiab]` | 3,127 | none |
| 31 | `horse[tiab]` | 33,966 | none |
| 32 | `horses[tiab]` | 30,374 | none |
| 33 | `equine[tiab]` | 28,778 | none |
| 34 | `buffalo[tiab]` | 9,137 | none |
| 35 | `camel[tiab]` | 3,210 | none |
| 36 | `farmed fish[tiab]` | 733 | none |
| 37 | `aquaculture[tiab]` | 9,036 | none |
| 38 | `farmed shrimp[tiab]` | 63 | none |
| 39 | `Fishes[Mesh]` | 183,474 | none |
| 40 | `Aquaculture[Mesh]` | 12,633 | none |
| 41 | `fish[tiab]` | 154,466 | none |
| 42 | `fishes[tiab]` | 19,728 | none |
| 43 | `aquatic animal*[tiab]` | 1,573 | none |
| 44 | `shellfish[tiab]` | 5,993 | none |
| 45 | `shrimp[tiab]` | 9,789 | none |
| 46 | `prawn[tiab]` | 1,403 | none |
| 47 | `salmon[tiab]` | 14,743 | none |
| 48 | `trout[tiab]` | 15,264 | none |
| 49 | `carp[tiab]` | 9,326 | none |
| 50 | `tilapia[tiab]` | 4,036 | none |
| 51 | `crustacean*[tiab]` | 9,623 | none |
| 52 | `mollusc*[tiab]` | 13,916 | none |
| 53 | `mollusk*[tiab]` | 4,193 | none |
| 54 | `oyster[tiab]` | 5,353 | none |
| 55 | `mussel[tiab]` | 6,542 | none |
| 56 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55` | 1,154,844 | none |
| 57 | `#7 AND #56` | 1,079 | none |

### Strategy (single line, for copying into PubMed)

```text
((Metagenomics[Mesh] OR metagenom*[tiab] OR virome[tiab] OR virom*[tiab] OR viral metagenomics[tiab] OR viral metagenomic*[tiab]) AND (Animals, Domestic[Mesh] OR livestock[tiab] OR farm animal*[tiab] OR farm animals[tiab] OR farmed animal*[tiab] OR domestic animal*[tiab] OR domesticated animal*[tiab] OR food-producing animal*[tiab] OR cattle[tiab] OR bovine[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR poultry[tiab] OR chicken[tiab] OR chickens[tiab] OR avian[tiab] OR sheep[tiab] OR ovine[tiab] OR goat[tiab] OR goats[tiab] OR caprine[tiab] OR horse[tiab] OR horses[tiab] OR equine[tiab] OR buffalo[tiab] OR camel[tiab] OR farmed fish[tiab] OR aquaculture[tiab] OR farmed shrimp[tiab] OR Fishes[Mesh] OR Aquaculture[Mesh] OR fish[tiab] OR fishes[tiab] OR aquatic animal*[tiab] OR shellfish[tiab] OR shrimp[tiab] OR prawn[tiab] OR salmon[tiab] OR trout[tiab] OR carp[tiab] OR tilapia[tiab] OR crustacean*[tiab] OR mollusc*[tiab] OR mollusk*[tiab] OR oyster[tiab] OR mussel[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Farmed/domesticated animals | 1 | `Metagenomics[Mesh] AND Animals[Mesh]` | 2,513 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| viral_metagenomics | 1,154,844 | 0 |
| farm_animals | 13,013 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 806 | initial | none | First broad draft from question alone; searched metagenomics/virome plus farmed/domesticated-animal vocabulary; viral eligibility screened to protect recall. |
| 2 | 1,079 | farm_animals: +17 / -0 | none | Expanded farm_animals for farmed aquatic animals in response to internal critic: added Fishes and Aquaculture MeSH plus fish and aquaculture species terminology. Retained the user-required Entrez entry-date bound; no publication-date limit. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 2 findings; R1-01 must-fix open, R1-02 must-fix open
- Round 2 on version 2: 2 findings; R1-01 must-fix resolved, R1-02 must-fix rejected
- Round 3 on version 2: 2 findings; R1-01 must-fix resolved, R1-02 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 635 NCBI requests logged (300 from cache); strategy sha256 7310b8355df6._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [],
    "issues": []
  },
  "vocabulary": [
    {
      "requested": "Metagenomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:48:08+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D056186",
          "name": "Metagenomics",
          "type": "descriptor",
          "scope_note": "The systematic study of the GENOMES of assemblages of organisms.",
          "tree_numbers": [
            "H01.158.273.343.350.261"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D056186",
      "preferred_label": "Metagenomics",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Metagenomics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:48:08+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000829",
          "name": "Animals, Domestic",
          "type": "descriptor",
          "scope_note": "Animals which have become adapted through breeding in captivity to a life intimately associated with humans. They include animals domesticated by humans to live and breed in a tame condition on farms or ranches for economic reasons, including LIVESTOCK (specifically CATTLE; SHEEP; HORSES; etc.), POULTRY; and those raised or kept for pleasure and companionship, e.g., PETS; or specifically DOGS; ...",
          "tree_numbers": [
            "B01.050.050.116"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000829",
      "preferred_label": "Animals, Domestic",
      "type": "descriptor",
      "location": "vocabulary:7",
      "term": {
        "text": "Animals, Domestic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fishes",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:48:08+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005399",
          "name": "Fishes",
          "type": "descriptor",
          "scope_note": "A group of cold-blooded, aquatic vertebrates having gills, fins, a cartilaginous or bony endoskeleton, and elongated bodies covered with scales.",
          "tree_numbers": [
            "B01.050.150.900.493"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005399",
      "preferred_label": "Fishes",
      "type": "descriptor",
      "location": "vocabulary:38",
      "term": {
        "text": "Fishes",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Aquaculture",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:48:08+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017756",
          "name": "Aquaculture",
          "type": "descriptor",
          "scope_note": "The farming, breeding, rearing, and harvesting of plants and animals in all types of water environments including ponds, rivers, lakes, and the ocean.",
          "tree_numbers": [
            "J01.040.168"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017756",
      "preferred_label": "Aquaculture",
      "type": "descriptor",
      "location": "vocabulary:39",
      "term": {
        "text": "Aquaculture",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"metagenomics\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"virome\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"viral metagenomics\"[Title/Abstract] OR \"viral metagenomic*\"[Title/Abstract]) AND (\"animals, domestic\"[MeSH Terms] OR \"livestock\"[Title/Abstract] OR \"farm animal*\"[Title/Abstract] OR \"farm animals\"[Title/Abstract] OR \"farmed animal*\"[Title/Abstract] OR \"domestic animal*\"[Title/Abstract] OR \"domesticated animal*\"[Title/Abstract] OR \"food producing animal*\"[Title/Abstract] OR \"cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"poultry\"[Title/Abstract] OR \"chicken\"[Title/Abstract] OR \"chickens\"[Title/Abstract] OR \"avian\"[Title/Abstract] OR \"sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat\"[Title/Abstract] OR \"goats\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse\"[Title/Abstract] OR \"horses\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"buffalo\"[Title/Abstract] OR \"camel\"[Title/Abstract] OR \"farmed fish\"[Title/Abstract] OR \"aquaculture\"[Title/Abstract] OR \"farmed shrimp\"[Title/Abstract] OR \"fishes\"[MeSH Terms] OR \"aquaculture\"[MeSH Terms] OR \"fish\"[Title/Abstract] OR \"fishes\"[Title/Abstract] OR \"aquatic animal*\"[Title/Abstract] OR \"shellfish\"[Title/Abstract] OR \"shrimp\"[Title/Abstract] OR \"prawn\"[Title/Abstract] OR \"salmon\"[Title/Abstract] OR \"trout\"[Title/Abstract] OR \"carp\"[Title/Abstract] OR \"tilapia\"[Title/Abstract] OR \"crustacean*\"[Title/Abstract] OR \"mollusc*\"[Title/Abstract] OR \"mollusk*\"[Title/Abstract] OR \"oyster\"[Title/Abstract] OR \"mussel\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "3f1c1eff894dd3099dc5d26eec76196873496d4423d33aa4850705e430c68412",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility includes farmed aquatic animals, but the population block has no bare fish or aquatic-animal term; farmed fish, aquaculture, and farmed shrimp do not cover that category explicitly."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two search blocks are combined with AND and terms within each block with OR, consistent with the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied MeSH headings are verified and map to the intended metagenomics and domestic-animal concepts."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The aquatic-animal eligibility is represented narrowly by farmed fish, aquaculture, and farmed shrimp; records naming fish or aquatic species without those phrases may be missed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported searches have no syntax errors or translation issues, and no phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The evaluated query includes an entry-date cutoff of 2019-02-22 despite the protocol saying there is no date limit. This excludes later-indexed records and needs resolution."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "Eligibility includes farmed aquatic animals, but the population block does not include the bare term fish or a broad aquatic-animal term. The existing phrases farmed fish and farmed shrimp, plus aquaculture, do not ensure retrieval when a record names fish or an aquatic species without those expressions.",
          "recommendation": "Add tested bare aquatic-population terms, including fish[tiab] and appropriate aquatic-animal/species vocabulary, while retaining screening for whether the animals were farmed.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query adds an entry-date range ending 2019-02-22, while the protocol states there is no date limit. This limits retrieval to older records and conflicts with the stated scope.",
          "recommendation": "Remove the entry-date cutoff for an unrestricted search, or document and obtain approval for a historical cutoff if that is intended; then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "3f652bdd2fa5351a37d63d8a07ee03ef60ee043c2a7b839c3221a30e6fef471e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Version 2 adds bare fish and aquatic-animal terms and species vocabulary; farmed status remains a screening decision."
        },
        "operators": {
          "verdict": "pass",
          "note": "The metagenomics and population blocks use OR within each block and AND between blocks."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied Metagenomics, Animals, Domestic, Fishes, and Aquaculture headings have corresponding MeSH translations."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Population terms include bare aquatic terms and relevant species; metagenomics and virome terms fit the method concept."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No query errors, translation issues, or phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2019-02-22 Entrez entry-date bound is explicitly required by the user's run harness and recorded in protocol.as_of. No publication-date [dp] filter is used; the protocol wording is clarified accordingly."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "Eligibility includes farmed aquatic animals, but the original population block lacked bare fish and broad aquatic-animal terms.",
          "recommendation": "Add tested bare aquatic-population terms and appropriate aquatic-animal/species vocabulary while screening for whether animals were farmed.",
          "status": "resolved",
          "response": "Version 2 adds fish[tiab], fishes[tiab], aquatic animal*[tiab], shellfish[tiab], and multiple aquatic-species terms. The updated evaluation retains all seven known relevant records."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query adds an entry-date range ending 2019-02-22, while the protocol states there is no date limit. This limits retrieval to older records and conflicts with the stated scope.",
          "recommendation": "Remove the entry-date cutoff for an unrestricted search, or document and obtain approval for a historical cutoff if that is intended; then rerun the complete evaluation.",
          "status": "rejected",
          "response": "This finding misreads the run instructions. The user explicitly required PSB_AS_OF=2019-02-22 for every command and prohibited a publication-date [dp] limit. The protocol records the required Entrez date bound in as_of; the search uses [edat], not [dp]. The protocol note now states this distinction explicitly."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "26525d6555fea1be696418c4a6c451c5285e6e14098467ea587842902399f1c9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Version 2 includes bare fish and aquatic-animal terms plus aquatic species vocabulary, addressing the farmed aquatic-animal eligibility. Farmed status remains a screening decision."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy combines the metagenomics and population blocks with AND and combines terms within each block with OR, consistent with the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Metagenomics, Animals, Domestic, Fishes, and Aquaculture headings are present, with corresponding MeSH translations and no reported translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The method block includes metagenomics, virome, and viral-metagenomics terminology. The population block includes broad farm and domestic-animal terms, livestock species, and aquatic-animal and species terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported searches have no syntax errors, translation issues, or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The protocol records the required 2019-02-22 Entrez entry-date cutoff via PSB_AS_OF and states that there is no publication-date or language limit. The evaluated query uses [edat], not [dp]."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "Eligibility includes farmed aquatic animals, but the original population block lacked bare fish and broad aquatic-animal terms.",
          "recommendation": "Add tested bare aquatic-population terms and appropriate aquatic-animal/species vocabulary while screening for whether animals were farmed.",
          "status": "resolved",
          "response": "Version 2 adds fish[tiab], fishes[tiab], aquatic animal*[tiab], shellfish[tiab], and multiple aquatic-species terms. The updated evaluation retains all seven known relevant records."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query adds an entry-date range ending 2019-02-22, while the protocol states there is no date limit. This limits retrieval to later-indexed records and conflicts with the stated scope.",
          "recommendation": "Remove the entry-date cutoff for an unrestricted search, or document and obtain approval for a historical cutoff if that is intended; then rerun the complete evaluation.",
          "status": "rejected",
          "response": "The packet states that the run instructions require PSB_AS_OF=2019-02-22 for every command and prohibit a publication-date [dp] limit. The protocol records the required Entrez entry-date bound in as_of and clarifies the distinction; the query uses [edat], not [dp]."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-10-01T12:43:47+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: no (User asked to proceed without questions. Assumed a broad topic-map scope covering terrestrial food-producing livestock and poultry plus farmed aquatic animals; companion animals, wildlife-only, and human-only studies excluded. No seeds were supplied. No language or publication-date limit. PubMed entry-date snapshot is pinned via PSB_AS_OF=2019-02-22 for every command; no publication-date limit is added. Scope assumption refined after internal critique: farmed aquatic animals includes finfish, shellfish/mollusks, and crustaceans; wild aquatic animals without a farmed context remain excluded. Scope was not confirmed because the user asked not to pause. The required 2019-02-22 as_of value intentionally restricts the search to records with PubMed Entrez entry dates on or before that day to simulate the requested historical PubMed state. It is not a publication-date eligibility criterion; no [dp] limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viruses and viral communities | search | The topic is specifically viral metagenomics; viral identity is required, but records may name only a specific virus or viral family. |
| Metagenomics and viral community sequencing | search | The method defines the topic; search broad method synonyms and the virome/viral sequencing terminology. |
| Food-producing farm animals, including livestock, poultry, and farmed aquatic animals | search | Farm-animal context defines the population; records may name only a farmed species rather than the category. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:41:48+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 986
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Viruses"[Mesh]` | 759,255 | none |
| 2 | `virus*[tiab]` | 687,408 | none |
| 3 | `viral[tiab]` | 333,289 | none |
| 4 | `virome[tiab]` | 667 | none |
| 5 | `virom*[tiab]` | 824 | none |
| 6 | `phage*[tiab]` | 48,158 | none |
| 7 | `circovirus*[tiab]` | 2,095 | none |
| 8 | `parvovirus*[tiab]` | 8,485 | none |
| 9 | `astrovirus*[tiab]` | 1,380 | none |
| 10 | `enterovirus*[tiab]` | 9,880 | none |
| 11 | `picornavirus*[tiab]` | 2,617 | none |
| 12 | `rotavirus*[tiab]` | 14,061 | none |
| 13 | `coronavirus*[tiab]` | 10,069 | none |
| 14 | `calicivirus*[tiab]` | 1,774 | none |
| 15 | `adenovirus*[tiab]` | 43,325 | none |
| 16 | `herpesvirus*[tiab]` | 24,687 | none |
| 17 | `papillomavirus*[tiab]` | 36,311 | none |
| 18 | `polyomavirus*[tiab]` | 5,040 | none |
| 19 | `pestivirus*[tiab]` | 1,224 | none |
| 20 | `bocavirus*[tiab]` | 1,023 | none |
| 21 | `picobirnavirus*[tiab]` | 144 | none |
| 22 | `anellovirus*[tiab]` | 146 | none |
| 23 | `reovirus*[tiab]` | 3,898 | none |
| 24 | `"CRESS-DNA"[tiab]` | 52 | none |
| 25 | `PRRSV[tiab]` | 2,573 | none |
| 26 | `PEDV[tiab]` | 730 | none |
| 27 | `BVDV[tiab]` | 2,405 | none |
| 28 | `BEV[tiab]` | 760 | none |
| 29 | `NDV[tiab]` | 3,029 | none |
| 30 | `IBV[tiab]` | 1,496 | none |
| 31 | `AIV[tiab]` | 2,737 | none |
| 32 | `PCV-2[tiab]` | 235 | none |
| 33 | `PCV-3[tiab]` | 31 | none |
| 34 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 1,115,757 | none |
| 35 | `"Metagenomics"[Mesh]` | 5,229 | none |
| 36 | `metagenom*[tiab]` | 11,213 | none |
| 37 | `metagenome*[tiab]` | 3,784 | none |
| 38 | `virom*[tiab]` | 824 | none |
| 39 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 40 | `"next-generation sequencing"[tiab]` | 26,834 | none |
| 41 | `"high throughput sequencing"[tiab]` | 10,541 | none |
| 42 | `"high-throughput sequencing"[tiab]` | 10,541 | none |
| 43 | `metatranscriptom*[tiab]` | 995 | none |
| 44 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 45 | `"shotgun sequencing"[tiab]` | 1,193 | none |
| 46 | `shotgun[tiab]` | 7,534 | none |
| 47 | `"viral community"[tiab]` | 168 | none |
| 48 | `"viral communities"[tiab]` | 240 | none |
| 49 | `"viral metagenomics"[tiab]` | 251 | none |
| 50 | `"viral metagenome"[tiab]` | 58 | none |
| 51 | `#35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50` | 68,020 | none |
| 52 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 53 | `"Livestock"[Mesh]` | 3,200 | none |
| 54 | `"Poultry"[Mesh]` | 147,415 | none |
| 55 | `"Cattle"[Mesh]` | 341,776 | none |
| 56 | `"Swine"[Mesh]` | 214,731 | none |
| 57 | `"Sheep"[Mesh]` | 116,801 | none |
| 58 | `"Goats"[Mesh]` | 30,623 | none |
| 59 | `"Fishes"[Mesh]` | 183,474 | none |
| 60 | `"Aquaculture"[Mesh]` | 12,633 | none |
| 61 | `livestock[tiab]` | 21,337 | none |
| 62 | `"farm animal"[tiab]` | 833 | none |
| 63 | `"farm animals"[tiab]` | 3,038 | none |
| 64 | `poultry[tiab]` | 25,731 | none |
| 65 | `cattle[tiab]` | 79,355 | none |
| 66 | `bovine[tiab]` | 189,144 | none |
| 67 | `cow[tiab]` | 29,456 | none |
| 68 | `cows[tiab]` | 45,341 | none |
| 69 | `calf[tiab]` | 43,460 | none |
| 70 | `calves[tiab]` | 24,854 | none |
| 71 | `swine[tiab]` | 42,358 | none |
| 72 | `pig[tiab]` | 127,282 | none |
| 73 | `pigs[tiab]` | 115,325 | none |
| 74 | `piglet[tiab]` | 5,096 | none |
| 75 | `piglets[tiab]` | 15,534 | none |
| 76 | `porcine[tiab]` | 79,145 | none |
| 77 | `sheep[tiab]` | 87,044 | none |
| 78 | `ovine[tiab]` | 20,361 | none |
| 79 | `ewe[tiab]` | 5,288 | none |
| 80 | `lamb[tiab]` | 9,836 | none |
| 81 | `lambs[tiab]` | 14,624 | none |
| 82 | `goat*[tiab]` | 31,547 | none |
| 83 | `caprine[tiab]` | 3,127 | none |
| 84 | `chicken*[tiab]` | 92,941 | none |
| 85 | `broiler*[tiab]` | 16,896 | none |
| 86 | `duck*[tiab]` | 13,075 | none |
| 87 | `turkey[tiab]` | 32,530 | none |
| 88 | `turkeys[tiab]` | 5,917 | none |
| 89 | `goose[tiab]` | 2,645 | none |
| 90 | `geese[tiab]` | 1,928 | none |
| 91 | `fish[tiab]` | 154,467 | none |
| 92 | `fishes[tiab]` | 19,728 | none |
| 93 | `aquaculture[tiab]` | 9,036 | none |
| 94 | `"farmed fish"[tiab]` | 733 | none |
| 95 | `salmon[tiab]` | 14,743 | none |
| 96 | `trout[tiab]` | 15,264 | none |
| 97 | `carp[tiab]` | 9,326 | none |
| 98 | `tilapia[tiab]` | 4,036 | none |
| 99 | `shrimp[tiab]` | 9,789 | none |
| 100 | `prawn[tiab]` | 1,403 | none |
| 101 | `oyster[tiab]` | 5,353 | none |
| 102 | `"Crustacea"[Mesh]` | 41,727 | none |
| 103 | `"Mollusca"[Mesh]` | 58,139 | none |
| 104 | `crustacean*[tiab]` | 9,623 | none |
| 105 | `shellfish[tiab]` | 5,993 | none |
| 106 | `mollusc*[tiab]` | 13,916 | none |
| 107 | `mollusk*[tiab]` | 4,193 | none |
| 108 | `bivalve*[tiab]` | 5,958 | none |
| 109 | `scallop*[tiab]` | 3,302 | none |
| 110 | `mussel*[tiab]` | 9,019 | none |
| 111 | `clam*[tiab]` | 91,171 | none |
| 112 | `crab*[tiab]` | 11,898 | none |
| 113 | `lobster*[tiab]` | 3,405 | none |
| 114 | `abalone[tiab]` | 995 | none |
| 115 | `#52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96 OR #97 OR #98 OR #99 OR #100 OR #101 OR #102 OR #103 OR #104 OR #105 OR #106 OR #107 OR #108 OR #109 OR #110 OR #111 OR #112 OR #113 OR #114` | 1,561,540 | none |
| 116 | `#34 AND #51 AND #115` | 986 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Viruses"[Mesh] OR virus*[tiab] OR viral[tiab] OR virome[tiab] OR virom*[tiab] OR phage*[tiab] OR circovirus*[tiab] OR parvovirus*[tiab] OR astrovirus*[tiab] OR enterovirus*[tiab] OR picornavirus*[tiab] OR rotavirus*[tiab] OR coronavirus*[tiab] OR calicivirus*[tiab] OR adenovirus*[tiab] OR herpesvirus*[tiab] OR papillomavirus*[tiab] OR polyomavirus*[tiab] OR pestivirus*[tiab] OR bocavirus*[tiab] OR picobirnavirus*[tiab] OR anellovirus*[tiab] OR reovirus*[tiab] OR "CRESS-DNA"[tiab] OR PRRSV[tiab] OR PEDV[tiab] OR BVDV[tiab] OR BEV[tiab] OR NDV[tiab] OR IBV[tiab] OR AIV[tiab] OR PCV-2[tiab] OR PCV-3[tiab]) AND ("Metagenomics"[Mesh] OR metagenom*[tiab] OR metagenome*[tiab] OR virom*[tiab] OR "next generation sequencing"[tiab] OR "next-generation sequencing"[tiab] OR "high throughput sequencing"[tiab] OR "high-throughput sequencing"[tiab] OR metatranscriptom*[tiab] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR "shotgun sequencing"[tiab] OR shotgun[tiab] OR "viral community"[tiab] OR "viral communities"[tiab] OR "viral metagenomics"[tiab] OR "viral metagenome"[tiab]) AND ("Animals, Domestic"[Mesh] OR "Livestock"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Fishes"[Mesh] OR "Aquaculture"[Mesh] OR livestock[tiab] OR "farm animal"[tiab] OR "farm animals"[tiab] OR poultry[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR piglet[tiab] OR piglets[tiab] OR porcine[tiab] OR sheep[tiab] OR ovine[tiab] OR ewe[tiab] OR lamb[tiab] OR lambs[tiab] OR goat*[tiab] OR caprine[tiab] OR chicken*[tiab] OR broiler*[tiab] OR duck*[tiab] OR turkey[tiab] OR turkeys[tiab] OR goose[tiab] OR geese[tiab] OR fish[tiab] OR fishes[tiab] OR aquaculture[tiab] OR "farmed fish"[tiab] OR salmon[tiab] OR trout[tiab] OR carp[tiab] OR tilapia[tiab] OR shrimp[tiab] OR prawn[tiab] OR oyster[tiab] OR "Crustacea"[Mesh] OR "Mollusca"[Mesh] OR crustacean*[tiab] OR shellfish[tiab] OR mollusc*[tiab] OR mollusk*[tiab] OR bivalve*[tiab] OR scallop*[tiab] OR mussel*[tiab] OR clam*[tiab] OR crab*[tiab] OR lobster*[tiab] OR abalone[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 34 | 34 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Viruses and viral communities | 1 | `disease*[tiab] OR infect*[tiab] OR pathogen*[tiab]` | 798 | 0/30 |
| Viruses and viral communities | 2 | `disease*[tiab] OR infect*[tiab] OR pathogen*[tiab]` | 1,182 | 0/30 |
| Food-producing farm animals, including livestock, poultry, and farmed aquatic animals | 1 | `Animals[Mesh] OR animal*[tiab]` | 3,053 | 0/30 |
| Food-producing farm animals, including livestock, poultry, and farmed aquatic animals | 2 | `Animals[Mesh] OR animal*[tiab]` | 4,207 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virus | 6,020 | 0 |
| metagenomics | 113,610 | 0 |
| farm_animals | 7,391 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | First structured draft; three required topic blocks with MeSH and broad text terms, using only records screened in from PubMed pilot samples for development. |
| 2 | 0 | virus: +6 / -0; metagenomics: +11 / -0; farm_animals: +47 / -0 | none | First structured draft; three required topic blocks with MeSH and broad text terms, using only records screened in from PubMed pilot samples for development. |
| 3 | 20,045 | farm_animals: +4 / -1 | none | Replaced short invalid pig* truncation with explicit pig, pigs, piglet, and piglets variants. |
| 4 | 704 | metagenomics: +0 / -2 | none | Removed unrestricted sequenc* and the broad High-Throughput Nucleotide Sequencing heading, which inflated retrieval beyond standard screening capacity; retained metagenomic/virome terms and explicit NGS/high-throughput sequencing phrases. |
| 5 | 983 | virus: +18 / -0; metagenomics: +7 / -0; farm_animals: +13 / -0 | none | Expanded virus-family and named-virus wording after the category critic finding; added explicit shotgun, viral-community and method MeSH terms; extended the declared farmed-aquatic scope to shellfish/crustaceans and indexed/text-word coverage. Added six screened pilot records to development. |
| 6 | 986 | virus: +9 / -0 | none | Added named-virus acronyms and common viral disease terms from screened records to address the open-ended taxon concern. Expanded protocol notes to state explicitly that the mandated 2019-02-22 bound is Entrez entry date for the historical PubMed snapshot, not publication-date eligibility. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4 (Fresh-context PRESS-structured internal critic.): 4 findings; R1-TRANS-01 should-fix open, R1-TEXT-01 should-fix open, R1-SCOPE-01 should-fix open, R1-FILTER-01 must-fix open
- Round 2 on version 5 (Fresh-context PRESS-structured internal critic.): 4 findings; R1-TRANS-01 should-fix open, R1-TEXT-01 should-fix resolved, R1-SCOPE-01 should-fix resolved, R1-FILTER-01 must-fix open
- Round 3 on version 6 (Fresh-context closing verification after two revision rounds.): 4 findings; R1-TRANS-01 should-fix open, R1-TEXT-01 should-fix resolved, R1-SCOPE-01 should-fix resolved, R1-FILTER-01 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1704 NCBI requests logged (951 from cache); strategy sha256 071b604a479c._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:farm_animals",
        "blocking": false,
        "requires_review": true,
        "id": "I-0b3f5bccffad386dd2e7"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:farm_animals",
        "blocking": false,
        "requires_review": true,
        "id": "I-0b3f5bccffad386dd2e7"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "Q000821",
          "name": "virology",
          "type": "qualifier",
          "scope_note": "Used with organs, animals, and higher plants and with diseases for virologic studies. For bacteria, rickettsia, and fungi, microbiology is used; for parasites, parasitology is used.",
          "tree_numbers": [
            "Y05.070.010"
          ],
          "entry_terms": 1,
          "mapped_to": null
        },
        {
          "ui": "D014780",
          "name": "Viruses",
          "type": "descriptor",
          "scope_note": "Minute infectious agents whose genomes are composed of DNA or RNA, but not both. They are characterized by a lack of independent metabolism and the inability to replicate outside living host cells.",
          "tree_numbers": [
            "B04"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014780",
      "preferred_label": "Viruses",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Metagenomics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Metagenomics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D059014",
          "name": "High-Throughput Nucleotide Sequencing",
          "type": "descriptor",
          "scope_note": "Techniques of nucleotide sequence analysis that increase the range, complexity, sensitivity, and accuracy of results by greatly increasing the scale of operations and thus the number of nucleotides, and the number of copies of each nucleotide sequenced. The sequencing may be done by analysis of the synthesis or ligation products, hybridization to preexisting sequences, etc.",
          "tree_numbers": [
            "E05.393.760.319"
          ],
          "entry_terms": 29,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D059014",
      "preferred_label": "High-Throughput Nucleotide Sequencing",
      "type": "descriptor",
      "location": "vocabulary:43",
      "term": {
        "text": "\"High-Throughput Nucleotide Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
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
      "location": "vocabulary:50",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D058751",
          "name": "Livestock",
          "type": "descriptor",
          "scope_note": "Domesticated farm animals raised for home use or profit but excluding POULTRY. Typically livestock includes CATTLE; SHEEP; HORSES; SWINE; GOATS; and others.",
          "tree_numbers": [
            "B01.050.050.116.500"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D058751",
      "preferred_label": "Livestock",
      "type": "descriptor",
      "location": "vocabulary:51",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011200",
          "name": "Poultry",
          "type": "descriptor",
          "scope_note": "Domesticated birds raised for food. It typically includes CHICKENS; TURKEYS, DUCKS; GEESE; and others.",
          "tree_numbers": [
            "B01.050.050.116.625",
            "B01.050.150.900.248.690",
            "G07.203.300.600.750",
            "J02.500.600.750"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011200",
      "preferred_label": "Poultry",
      "type": "descriptor",
      "location": "vocabulary:52",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002417",
          "name": "Cattle",
          "type": "descriptor",
          "scope_note": "Domesticated bovine animals of the genus Bos, usually kept on a farm or ranch and used for the production of meat or dairy products or for heavy labor.",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.380.271"
          ],
          "entry_terms": 36,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002417",
      "preferred_label": "Cattle",
      "type": "descriptor",
      "location": "vocabulary:53",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013552",
          "name": "Swine",
          "type": "descriptor",
          "scope_note": "Any of various animals that constitute the family Suidae and comprise stout-bodied, short-legged omnivorous mammals with thick skin, usually covered with coarse bristles, a rather long mobile snout, and small tail. Included are the genera Babyrousa, Phacochoerus (wart hogs), and Sus, the latter containing the domestic pig (see SUS SCROFA).",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.880"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013552",
      "preferred_label": "Swine",
      "type": "descriptor",
      "location": "vocabulary:54",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012756",
          "name": "Sheep",
          "type": "descriptor",
          "scope_note": "Any of the ruminant mammals with curved horns in the genus Ovis, family Bovidae. They possess lachrymal grooves and interdigital glands, which are absent in GOATS.",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.380.791"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012756",
      "preferred_label": "Sheep",
      "type": "descriptor",
      "location": "vocabulary:55",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006041",
          "name": "Goats",
          "type": "descriptor",
          "scope_note": "Any of numerous agile, hollow-horned RUMINANTS of the genus Capra, in the family Bovidae, closely related to the SHEEP.",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.380.513"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006041",
      "preferred_label": "Goats",
      "type": "descriptor",
      "location": "vocabulary:56",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fishes",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
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
      "location": "vocabulary:57",
      "term": {
        "text": "\"Fishes\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Aquaculture",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
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
      "location": "vocabulary:58",
      "term": {
        "text": "\"Aquaculture\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Crustacea",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003445",
          "name": "Crustacea",
          "type": "descriptor",
          "scope_note": "A large subphylum of mostly marine ARTHROPODS containing over 42,000 species. They include familiar arthropods such as lobsters (NEPHROPIDAE), crabs (BRACHYURA), shrimp (PENAEIDAE), and barnacles (THORACICA).",
          "tree_numbers": [
            "B01.050.500.131.365"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003445",
      "preferred_label": "Crustacea",
      "type": "descriptor",
      "location": "vocabulary:100",
      "term": {
        "text": "\"Crustacea\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mollusca",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:41:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008974",
          "name": "Mollusca",
          "type": "descriptor",
          "scope_note": "A phylum of the kingdom Metazoa. Mollusca have soft, unsegmented bodies with an anterior head, a dorsal visceral mass, and a ventral foot. Most are encased in a protective calcareous shell. It includes the classes GASTROPODA; BIVALVIA; CEPHALOPODA; Aplacophora; Scaphopoda; Polyplacophora; and Monoplacophora.",
          "tree_numbers": [
            "B01.050.500.644"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008974",
      "preferred_label": "Mollusca",
      "type": "descriptor",
      "location": "vocabulary:101",
      "term": {
        "text": "\"Mollusca\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Viruses\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virome\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"circovirus*\"[Title/Abstract] OR \"parvovirus*\"[Title/Abstract] OR \"astrovirus*\"[Title/Abstract] OR \"enterovirus*\"[Title/Abstract] OR \"picornavirus*\"[Title/Abstract] OR \"rotavirus*\"[Title/Abstract] OR \"coronavirus*\"[Title/Abstract] OR \"calicivirus*\"[Title/Abstract] OR \"adenovirus*\"[Title/Abstract] OR \"herpesvirus*\"[Title/Abstract] OR \"papillomavirus*\"[Title/Abstract] OR \"polyomavirus*\"[Title/Abstract] OR \"pestivirus*\"[Title/Abstract] OR \"bocavirus*\"[Title/Abstract] OR \"picobirnavirus*\"[Title/Abstract] OR \"anellovirus*\"[Title/Abstract] OR \"reovirus*\"[Title/Abstract] OR \"CRESS-DNA\"[Title/Abstract] OR \"PRRSV\"[Title/Abstract] OR \"PEDV\"[Title/Abstract] OR \"BVDV\"[Title/Abstract] OR \"BEV\"[Title/Abstract] OR \"NDV\"[Title/Abstract] OR \"IBV\"[Title/Abstract] OR \"AIV\"[Title/Abstract] OR \"PCV-2\"[Title/Abstract] OR \"PCV-3\"[Title/Abstract]) AND (\"Metagenomics\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"metagenome*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"metatranscriptom*\"[Title/Abstract] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"shotgun sequencing\"[Title/Abstract] OR \"shotgun\"[Title/Abstract] OR \"viral community\"[Title/Abstract] OR \"viral communities\"[Title/Abstract] OR \"viral metagenomics\"[Title/Abstract] OR \"viral metagenome\"[Title/Abstract]) AND (\"animals, domestic\"[MeSH Terms] OR \"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Fishes\"[MeSH Terms] OR \"Aquaculture\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm animal\"[Title/Abstract] OR \"farm animals\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"piglet\"[Title/Abstract] OR \"piglets\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"ewe\"[Title/Abstract] OR \"lamb\"[Title/Abstract] OR \"lambs\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"fish\"[Title/Abstract] OR \"Fishes\"[Title/Abstract] OR \"Aquaculture\"[Title/Abstract] OR \"farmed fish\"[Title/Abstract] OR \"salmon\"[Title/Abstract] OR \"trout\"[Title/Abstract] OR \"carp\"[Title/Abstract] OR \"tilapia\"[Title/Abstract] OR \"shrimp\"[Title/Abstract] OR \"prawn\"[Title/Abstract] OR \"oyster\"[Title/Abstract] OR \"Crustacea\"[MeSH Terms] OR \"Mollusca\"[MeSH Terms] OR \"crustacean*\"[Title/Abstract] OR \"shellfish\"[Title/Abstract] OR \"mollusc*\"[Title/Abstract] OR \"mollusk*\"[Title/Abstract] OR \"bivalve*\"[Title/Abstract] OR \"scallop*\"[Title/Abstract] OR \"mussel*\"[Title/Abstract] OR \"clam*\"[Title/Abstract] OR \"crab*\"[Title/Abstract] OR \"lobster*\"[Title/Abstract] OR \"abalone\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "70d21e4a147f1d6d71affaa4c64c67d8d7632562376e63477a5ada80672ebba0",
      "note": "Fresh-context PRESS-structured internal critic.",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The virus block does not cover records that identify only a specific virus or viral family, despite the scope rationale. The method block also lacks explicit terms for viral-community sequencing and common approaches such as shotgun sequencing."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within concepts and AND across the three required concepts match the stated scope. The duplicated virom* term is redundant but does not change retrieval."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The strategy includes useful virus, metagenomics, livestock, poultry, fish, and aquaculture headings. Consider headings for farmed aquatic groups not represented by fish, such as shellfish or crustaceans, if those populations remain in scope."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The text words cover many major livestock and poultry species, but do not cover specific virus names without virus-related wording, several common sequencing descriptions, or a broad range of farmed aquatic animals."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed translation warnings or errors. The equivalent hyphenated and unhyphenated phrase variants translate redundantly, but no syntax failure is shown."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The displayed query applies an entry-date ceiling of 2019-02-22, although the strategy lists no limits and the eligibility criteria specify no date restriction. Confirm whether this is only the historical evaluation snapshot; remove or update it for a current search."
        }
      },
      "findings": [
        {
          "id": "R1-TRANS-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "virus",
          "finding": "The scope says records may name only a specific virus or viral family, but the virus block relies on virus*, viral, virome/virom*, and phage*. Those terms can miss records indexed or described only by a virus or family name.",
          "recommendation": "Add and test a suitable set of virus and viral-family names or broader name variants against relevant records, then rerun the complete evaluation. Do not treat the 28 already-retrieved known records as evidence that this coverage is sufficient.",
          "status": "open"
        },
        {
          "id": "R1-TEXT-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The method block includes metagenomics, virome, metatranscriptomics, and general sequencing phrases, but lacks explicit terms for viral-community sequencing and commonly used descriptions such as shotgun sequencing or metagenomic sequencing.",
          "recommendation": "Develop and test explicit method expressions that cover viral-community and shotgun/metagenomic sequencing, retaining terms that improve eligible-record retrieval; rerun the complete evaluation after changes.",
          "status": "open"
        },
        {
          "id": "R1-SCOPE-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The searched population includes farmed aquatic animals, while the text words name fish and a few aquatic species (including shrimp, prawn, and oyster). They do not clearly cover other farmed aquatic groups such as shellfish and crustaceans, or many species within those groups.",
          "recommendation": "Clarify the intended farmed-aquatic scope and add and test appropriate group and species names and subject headings, or narrow the scope explicitly. Rerun the complete evaluation after changes.",
          "status": "open"
        },
        {
          "id": "R1-FILTER-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": null,
          "finding": "The displayed search query restricts entry dates through 2019-02-22, while the strategy declares no limits and the eligibility criteria contain no date cutoff. If used as written now, it excludes later records.",
          "recommendation": "Remove the entry-date ceiling or update it to the intended search date, and document any deliberate cutoff. Confirm whether the displayed date is only the historical evaluation snapshot. Reevaluate the final query with the intended date handling.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "b0dcc2d977cd4589325194fd971793b54961231ad6f0a3612e7016b4b2ff7724",
      "note": "Fresh-context PRESS-structured internal critic.",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The expanded virus block adds specific virus and family names, but the open-ended scope includes any virus and records naming only a particular virus or family. Known-record retrieval does not prove that this category is fully covered."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within the three concepts and AND across the required concepts match the stated scope. No optional block is proposed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings cover viruses, metagenomics and sequencing, livestock and poultry, and aquatic groups including fishes, crustaceans, and mollusks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The method block now includes shotgun sequencing and viral-community expressions. Population terms cover the named terrestrial and farmed aquatic groups, with broad group terms and species examples."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no translation issues or warnings. The phrase expressions shown do not use proximity operators."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The displayed final query still limits entry dates through 2019-02-22. The packet does not establish that this is only a historical evaluation snapshot or document an intended cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-TRANS-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "virus",
          "finding": "The scope allows records that identify only a specific virus or viral family. The expanded block adds a number of virus and family names, but does not establish coverage for the full scope of any virus.",
          "recommendation": "Continue developing and testing specific-virus and viral-family expressions, including names that may appear without virus-related wording. Rerun the complete evaluation after any changes; do not treat retrieval of the known records alone as proof of sufficient coverage.",
          "status": "open"
        },
        {
          "id": "R1-TEXT-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The method block previously lacked explicit viral-community and shotgun sequencing expressions.",
          "recommendation": "Add and test explicit viral-community and shotgun/metagenomic sequencing expressions, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current block includes shotgun sequencing, shotgun, viral community/communities, viral metagenomics, and viral metagenome expressions. The packet reports a complete evaluation for version 5."
        },
        {
          "id": "R1-SCOPE-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The population block previously did not clearly cover farmed aquatic groups such as shellfish and crustaceans or a broad range of species.",
          "recommendation": "Add and test appropriate aquatic group and species names and subject headings, or narrow the scope explicitly. Rerun the complete evaluation after changes.",
          "status": "resolved",
          "response": "The current block includes Crustacea and Mollusca headings, crustacean and shellfish terms, mollusk/mollusc and bivalve terms, and several aquatic species. These additions align with the stated farmed aquatic scope."
        },
        {
          "id": "R1-FILTER-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": null,
          "finding": "The displayed query restricts entry dates through 2019-02-22, while the strategy declares no limits and eligibility specifies no date cutoff. If used as displayed, later records are excluded.",
          "recommendation": "Remove the entry-date ceiling or update it to the intended search date, and document any deliberate cutoff. Clarify whether the displayed date belongs only to the historical evaluation snapshot, then evaluate the query with the intended date handling.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "1c84c68a82738e7894df295d7b1cb459debc8276b31fcbb08b49ee32e603b2a8",
      "note": "Fresh-context closing verification after two revision rounds.",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Version 6 adds nine virus names or abbreviations, but the open scope includes any virus and records may name only a specific virus or family. The 34 known records are retrieved, but that does not establish coverage of the full scope."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within the three concepts and AND across them match the stated scope. No optional block is proposed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for viruses, metagenomics and sequencing, domestic animals, livestock, poultry, fishes, aquaculture, crustaceans, and mollusks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The method block now includes shotgun and viral-community expressions. Population terms cover terrestrial farm animals and the named farmed aquatic groups with group terms and species examples."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no translation issues, warnings, or errors. Redundant hyphenated and unhyphenated phrase translations do not show a syntax failure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The strategy documents 2019-02-22 as an intentional PubMed entry-date snapshot for historical evaluation, not a publication-date eligibility limit."
        }
      },
      "findings": [
        {
          "id": "R1-TRANS-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "virus",
          "finding": "The scope allows records that identify only a specific virus or viral family. Version 6 adds several names and abbreviations, but does not establish coverage for the open-ended scope of any virus.",
          "recommendation": "Continue developing and testing specific-virus and viral-family expressions, including names that may appear without virus-related wording. Reevaluate the complete strategy after changes; do not treat known-record retrieval alone as proof of sufficient coverage.",
          "status": "open"
        },
        {
          "id": "R1-TEXT-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The method block previously lacked explicit viral-community and shotgun sequencing expressions.",
          "recommendation": "Add and test explicit viral-community and shotgun/metagenomic sequencing expressions, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Version 6 includes shotgun sequencing, shotgun, viral community and communities, viral metagenomics, and viral metagenome expressions."
        },
        {
          "id": "R1-SCOPE-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The population block previously did not clearly cover farmed aquatic groups such as shellfish and crustaceans or a broad range of species.",
          "recommendation": "Add and test appropriate aquatic group and species names and subject headings, or narrow the scope explicitly. Rerun the complete evaluation after changes.",
          "status": "resolved",
          "response": "Version 6 includes Crustacea and Mollusca headings, crustacean and shellfish terms, mollusk/mollusc and bivalve terms, and multiple aquatic species."
        },
        {
          "id": "R1-FILTER-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": null,
          "finding": "The displayed query restricts entry dates through 2019-02-22, while the strategy declares no limits and eligibility specifies no date cutoff.",
          "recommendation": "Remove the entry-date ceiling or update it to the intended search date, and document any deliberate cutoff.",
          "status": "resolved",
          "response": "The strategy now documents 2019-02-22 as the intended historical PubMed entry-date snapshot, with no publication-date eligibility limit."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-0b3f5bccffad386dd2e7",
          "status": "accepted-risk",
          "response": "The farm-animal block changed after its category probes, and the probe budget is spent. Accept the stale-probe warning for this evaluation and screen records against the farmed-animal eligibility criteria.",
          "evidence": "Validation identifies category_probe_stale_budget_spent for farm_animals. The two recorded probes screened 30 records each and found no relevant records; the current block includes aquatic group headings and terms."
        }
      ]
    }
  ]
}
```


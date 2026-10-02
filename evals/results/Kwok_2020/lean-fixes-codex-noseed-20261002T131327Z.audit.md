# PubMed search strategy: audit

Generated 2026-10-02T13:42:30+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: no (User requested no follow-up questions. Assumed PCC scoping/topic-map framing; viruses, metagenomics/viromics, and farm animals are required concepts, with study design and individual virus/species eligibility screened. Farmed aquatic species are included as production animals by assumption. No known relevant records supplied. The run harness requires work as of 2019-02-22 and PSB_AS_OF=2019-02-22 on every command; this is an Entrez date-entry bound, not a publication-date limit, and no [dp] limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viruses | search | Viruses define the organism focus of the question and are named in indexing or title/abstract text. |
| Metagenomics and viromics | search | Metagenomic sequencing is the focal method and has controlled vocabulary and reliable text terms; include virome/viromics wording for records that do not say metagenomics. |
| Farm animals | search | The question explicitly restricts the population to farm animals; search common livestock species and production-animal wording because a generic animal heading is too broad. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:40:14+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 1,060
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Viruses"[Mesh]` | 759,255 | none |
| 2 | `virus*[tiab]` | 687,408 | none |
| 3 | `viral[tiab]` | 333,289 | none |
| 4 | `virolog*[tiab]` | 36,884 | none |
| 5 | `virome[tiab]` | 667 | none |
| 6 | `viromic*[tiab]` | 42 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 1,073,749 | none |
| 8 | `"Metagenomics"[Mesh]` | 5,229 | none |
| 9 | `"Metagenome"[Mesh]` | 5,897 | none |
| 10 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 11 | `metagenom*[tiab]` | 11,213 | none |
| 12 | `virom*[tiab]` | 824 | none |
| 13 | `"high throughput sequencing"[tiab]` | 10,541 | none |
| 14 | `"high-throughput sequencing"[tiab]` | 10,541 | none |
| 15 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 16 | `"next-generation sequencing"[tiab]` | 26,834 | none |
| 17 | `"deep sequencing"[tiab]` | 6,483 | none |
| 18 | `"shotgun sequencing"[tiab]` | 1,193 | none |
| 19 | `"massively parallel sequencing"[tiab]` | 1,756 | none |
| 20 | `"sequence-independent"[tiab]` | 1,107 | none |
| 21 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 70,093 | none |
| 22 | `"Livestock"[Mesh]` | 3,200 | none |
| 23 | `"Poultry"[Mesh]` | 147,415 | none |
| 24 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 25 | `"Cattle"[Mesh]` | 341,776 | none |
| 26 | `"Swine"[Mesh]` | 214,731 | none |
| 27 | `"Sheep"[Mesh]` | 116,801 | none |
| 28 | `"Goats"[Mesh]` | 30,623 | none |
| 29 | `"Horses"[Mesh]` | 67,676 | none |
| 30 | `"Rabbits"[Mesh]` | 337,179 | none |
| 31 | `livestock[tiab]` | 21,337 | none |
| 32 | `"farm animal"[tiab]` | 833 | none |
| 33 | `"farm animals"[tiab]` | 3,038 | none |
| 34 | `"production animal"[tiab]` | 126 | none |
| 35 | `"production animals"[tiab]` | 294 | none |
| 36 | `"food animal"[tiab]` | 898 | none |
| 37 | `"food animals"[tiab]` | 1,313 | none |
| 38 | `cattle[tiab]` | 79,355 | none |
| 39 | `bovin*[tiab]` | 190,666 | none |
| 40 | `cow[tiab]` | 29,456 | none |
| 41 | `cows[tiab]` | 45,341 | none |
| 42 | `calf[tiab]` | 43,460 | none |
| 43 | `calves[tiab]` | 24,854 | none |
| 44 | `swine[tiab]` | 42,358 | none |
| 45 | `pig[tiab]` | 127,282 | none |
| 46 | `pigs[tiab]` | 115,325 | none |
| 47 | `porcin*[tiab]` | 79,429 | none |
| 48 | `poultry[tiab]` | 25,731 | none |
| 49 | `fowl[tiab]` | 6,948 | none |
| 50 | `chicken*[tiab]` | 92,941 | none |
| 51 | `broiler*[tiab]` | 16,896 | none |
| 52 | `turkey[tiab]` | 32,530 | none |
| 53 | `turkeys[tiab]` | 5,917 | none |
| 54 | `duck*[tiab]` | 13,075 | none |
| 55 | `goose[tiab]` | 2,645 | none |
| 56 | `geese[tiab]` | 1,928 | none |
| 57 | `sheep[tiab]` | 87,044 | none |
| 58 | `ovine[tiab]` | 20,361 | none |
| 59 | `goat*[tiab]` | 31,547 | none |
| 60 | `caprin*[tiab]` | 3,608 | none |
| 61 | `horse*[tiab]` | 80,001 | none |
| 62 | `equine*[tiab]` | 29,202 | none |
| 63 | `rabbit*[tiab]` | 252,771 | none |
| 64 | `camel*[tiab]` | 9,598 | none |
| 65 | `alpaca*[tiab]` | 1,132 | none |
| 66 | `aquaculture[tiab]` | 9,036 | none |
| 67 | `aquacultur*[tiab]` | 9,364 | none |
| 68 | `fish[tiab]` | 154,467 | none |
| 69 | `salmon[tiab]` | 14,743 | none |
| 70 | `salmonids[tiab]` | 2,043 | none |
| 71 | `trout*[tiab]` | 15,375 | none |
| 72 | `tilapia*[tiab]` | 4,095 | none |
| 73 | `carp*[tiab]` | 43,260 | none |
| 74 | `shrimp[tiab]` | 9,789 | none |
| 75 | `prawn*[tiab]` | 1,678 | none |
| 76 | `oyster*[tiab]` | 7,043 | none |
| 77 | `mussel*[tiab]` | 9,019 | none |
| 78 | `farmed fish[tiab]` | 733 | none |
| 79 | `farmed salmon[tiab]` | 257 | none |
| 80 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79` | 1,774,006 | none |
| 81 | `#7 AND #21 AND #80` | 1,060 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Viruses"[Mesh] OR virus*[tiab] OR viral[tiab] OR virolog*[tiab] OR virome[tiab] OR viromic*[tiab]) AND ("Metagenomics"[Mesh] OR "Metagenome"[Mesh] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR metagenom*[tiab] OR virom*[tiab] OR "high throughput sequencing"[tiab] OR "high-throughput sequencing"[tiab] OR "next generation sequencing"[tiab] OR "next-generation sequencing"[tiab] OR "deep sequencing"[tiab] OR "shotgun sequencing"[tiab] OR "massively parallel sequencing"[tiab] OR "sequence-independent"[tiab]) AND ("Livestock"[Mesh] OR "Poultry"[Mesh] OR "Animals, Domestic"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR "Rabbits"[Mesh] OR livestock[tiab] OR "farm animal"[tiab] OR "farm animals"[tiab] OR "production animal"[tiab] OR "production animals"[tiab] OR "food animal"[tiab] OR "food animals"[tiab] OR cattle[tiab] OR bovin*[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcin*[tiab] OR poultry[tiab] OR fowl[tiab] OR chicken*[tiab] OR broiler*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck*[tiab] OR goose[tiab] OR geese[tiab] OR sheep[tiab] OR ovine[tiab] OR goat*[tiab] OR caprin*[tiab] OR horse*[tiab] OR equine*[tiab] OR rabbit*[tiab] OR camel*[tiab] OR alpaca*[tiab] OR aquaculture[tiab] OR aquacultur*[tiab] OR fish[tiab] OR salmon[tiab] OR salmonids[tiab] OR trout*[tiab] OR tilapia*[tiab] OR carp*[tiab] OR shrimp[tiab] OR prawn*[tiab] OR oyster*[tiab] OR mussel*[tiab] OR farmed fish[tiab] OR farmed salmon[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virus | 5,516 | 0 |
| metagenomics | 131,354 | 0 |
| farm_animals | 7,777 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 926 | initial | none | Initial three-block PCC strategy; includes broad sequencing synonyms and farm-species vocabulary from the screened pilot records. |
| 2 | 929 | metagenomics: +1 / -0 | none | Added verified MeSH descriptor Metagenome (introduced 2010) to the metagenomics block after vocabulary review; no terms were added from held-out records. |
| 3 | 1,060 | farm_animals: +10 / -0 | none | Addressed F1-TR-01 by adding bare in-scope farmed aquatic species terms and screening farmed status; documented that the Entrez cutoff is mandatory under the run harness, not an optional search limit. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; F1-TR-01 should-fix open, F1-LF-01 must-fix open
- Round 2 on version 3: 2 findings; F1-TR-01 should-fix resolved, F1-LF-01 must-fix accepted-risk
- Round 3 on version 3: 2 findings; F1-TR-01 should-fix resolved, F1-LF-01 must-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1016 NCBI requests logged (500 from cache); strategy sha256 f4191aaf4637._

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
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "\"Metagenomics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Metagenome",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D054892",
          "name": "Metagenome",
          "type": "descriptor",
          "scope_note": "A collective genome representative of the many organisms, primarily microorganisms, existing in a community.",
          "tree_numbers": [
            "G05.360.340.550"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D054892",
      "preferred_label": "Metagenome",
      "type": "descriptor",
      "location": "vocabulary:8",
      "term": {
        "text": "\"Metagenome\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"High-Throughput Nucleotide Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006736",
          "name": "Horses",
          "type": "descriptor",
          "scope_note": "Large, hoofed mammals of the family EQUIDAE. Horses are active day and night with most of the day spent seeking and consuming food. Feeding peaks occur in the early morning and late afternoon, and there are several daily periods of rest.",
          "tree_numbers": [
            "B01.050.150.900.649.313.984.235.472"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006736",
      "preferred_label": "Horses",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rabbits",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:40:14+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011817",
          "name": "Rabbits",
          "type": "descriptor",
          "scope_note": "A burrowing plant-eating mammal with hind limbs that are longer than its fore limbs. It belongs to the family Leporidae of the order Lagomorpha, and in contrast to hares, possesses 22 instead of 24 pairs of chromosomes.",
          "tree_numbers": [
            "B01.050.150.900.649.313.968.700"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011817",
      "preferred_label": "Rabbits",
      "type": "descriptor",
      "location": "vocabulary:28",
      "term": {
        "text": "\"Rabbits\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Viruses\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virolog*\"[Title/Abstract] OR \"virome\"[Title/Abstract] OR \"viromic*\"[Title/Abstract]) AND (\"Metagenomics\"[MeSH Terms] OR \"Metagenome\"[MeSH Terms] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"deep sequencing\"[Title/Abstract] OR \"shotgun sequencing\"[Title/Abstract] OR \"massively parallel sequencing\"[Title/Abstract] OR \"sequence-independent\"[Title/Abstract]) AND (\"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"animals, domestic\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Rabbits\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm animal\"[Title/Abstract] OR \"farm animals\"[Title/Abstract] OR \"production animal\"[Title/Abstract] OR \"production animals\"[Title/Abstract] OR \"food animal\"[Title/Abstract] OR \"food animals\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovin*\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"porcin*\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"fowl\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprin*\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine*\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"camel*\"[Title/Abstract] OR \"alpaca*\"[Title/Abstract] OR \"aquaculture\"[Title/Abstract] OR \"aquacultur*\"[Title/Abstract] OR \"fish\"[Title/Abstract] OR \"salmon\"[Title/Abstract] OR \"salmonids\"[Title/Abstract] OR \"trout*\"[Title/Abstract] OR \"tilapia*\"[Title/Abstract] OR \"carp*\"[Title/Abstract] OR \"shrimp\"[Title/Abstract] OR \"prawn*\"[Title/Abstract] OR \"oyster*\"[Title/Abstract] OR \"mussel*\"[Title/Abstract] OR \"farmed fish\"[Title/Abstract] OR \"farmed salmon\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "fe2b134212a6ed62a0a7ca5065c6b4b9693620306c915133f97a4e3356daf7b8",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The population block restricts aquatic coverage to aquaculture wording and the phrases farmed fish and farmed salmon. Add bare aquatic-species wording so relevant records are not missed when farming status is absent from the title or abstract."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are combined with AND and terms within each block with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified, and no heading translation errors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The aquatic population terms are narrowed to aquaculture wording or phrases containing farmed. See F1-TR-01."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed strategy and PubMed translation have no reported syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The user-requested as-of date is mandated by the run harness. I will retain and disclose the Entrez date-entry bound; it is not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1-TR-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "farm_animals",
          "finding": "Eligibility includes farmed aquatic species, but the population block uses aquaculture terms and only the phrases farmed fish and farmed salmon. It can miss records that name an aquatic species without those phrases.",
          "recommendation": "Add bare aquatic-species terms, including fish and salmon, and screen retrieved records for farmed status. Consider other in-scope aquatic species if applicable.",
          "status": "open"
        },
        {
          "id": "F1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query is limited to records with an Entrez date from 1800-01-01 through 2019-02-22. The stated question and eligibility have no time restriction, and the packet's run date is 2026-10-02.",
          "recommendation": "Use the intended current search date or remove the date-entry ceiling if the search is meant to be unrestricted. Rerun the complete evaluation after changing the filter.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "56c2c907583394b13f27b4bb9e831a6f6326a589b3e1c07d04031de5f83b6f89",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The aquatic population terms now include bare species wording; farmed status can be assessed during screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy combines the three required concept blocks with AND and terms within each block with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified, with no heading translation errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The added aquatic terms address the prior concern that population wording required aquaculture or farmed phrasing."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors, translation issues, or PubMed warning list."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date-entry bound is required by the run harness and is explicitly documented as distinct from a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1-TR-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "farm_animals",
          "finding": "The earlier population block narrowed aquatic coverage to aquaculture wording and phrases containing farmed.",
          "recommendation": "Add bare aquatic-species terms and screen retrieved records for farmed status.",
          "status": "resolved",
          "response": "Bare aquatic terms were added, including fish, salmon, salmonids, trout, tilapia, carp, shrimp, prawn, oyster, and mussel. Eligibility includes farmed aquatic species, and farming status can be screened."
        },
        {
          "id": "F1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query is limited to records with an Entrez date from 1800-01-01 through 2019-02-22, although the stated question and eligibility have no time restriction.",
          "recommendation": "Use the intended current search date or remove the date-entry ceiling if the search is meant to be unrestricted; disclose the bound and rerun the complete evaluation after changing it.",
          "status": "accepted-risk",
          "response": "The packet and protocol now document that the run harness requires an as-of date of 2019-02-22 and PSB_AS_OF on every command. The Entrez date-entry bound is retained under that constraint; it is not a publication-date limit."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "56c2c907583394b13f27b4bb9e831a6f6326a589b3e1c07d04031de5f83b6f89",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The aquatic population block now includes bare species terms, and eligibility directs reviewers to screen for farmed status."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three required concept blocks are combined with AND, with terms within each block combined by OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified and identifies no heading translation errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Bare aquatic species terms address the earlier concern about requiring aquaculture or farmed wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current strategy has no reported syntax errors, translation issues, or PubMed warning list."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date-entry bound remains an accepted risk under the documented run-harness as-of requirement; it is identified as distinct from a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1-TR-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "farm_animals",
          "finding": "Eligibility includes farmed aquatic species, but the earlier population block relied on aquaculture terms and phrases containing farmed, potentially missing records that name an aquatic species without those phrases.",
          "recommendation": "Add bare aquatic-species terms and screen retrieved records for farmed status.",
          "status": "resolved",
          "response": "Bare aquatic terms were added, including fish, salmon, salmonids, trout, tilapia, carp, shrimp, prawn, oyster, and mussel. Eligibility includes farmed aquatic species, and farming status can be screened."
        },
        {
          "id": "F1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query is limited to records with an Entrez date from 1800-01-01 through 2019-02-22, although the stated question and eligibility have no time restriction.",
          "recommendation": "Use the intended current search date or remove the date-entry ceiling if the search is meant to be unrestricted; disclose the bound and rerun the complete evaluation after changing it.",
          "status": "accepted-risk",
          "response": "The packet and protocol document that the run harness requires an as-of date of 2019-02-22 and PSB_AS_OF on every command. The Entrez date-entry bound is retained under that constraint; it is not a publication-date limit."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-30T13:12:46+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC (scoping-style topic question)
- Scope confirmed by user: no (User asked to proceed without questions; scope assumptions recorded, and scope was not user-confirmed. No known relevant articles supplied. Treat this as a broad topic/scoping search. Farm animals means terrestrial production species including livestock, poultry, rabbits, and camelids; aquaculture and aquatic farmed species are excluded. PubMed snapshot is bounded by Entrez date 2019-02-22 (PSB_AS_OF); no publication-date filter.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viruses | search | The review is specifically about viral rather than bacterial, fungal, or general microbiome metagenomics; virus is usually named or indexed. |
| Metagenomics and virome methods | search | The method defines the topic; use broad metagenomic, viromic, and high-throughput sequencing language to avoid requiring one exact label. |
| Farmed/production animals | search | Animal production context is central and generally searchable by animal species and livestock terms. Include terrestrial livestock and poultry, including rabbits and camelids; aquatic farmed species (aquaculture) are outside this operational scope. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:11:05+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 910
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Viruses"[Mesh]` | 759,255 | none |
| 2 | `"Bacteriophages"[Mesh]` | 56,898 | none |
| 3 | `virus*[tiab]` | 687,407 | none |
| 4 | `viral[tiab]` | 333,289 | none |
| 5 | `virolog*[tiab]` | 36,884 | none |
| 6 | `phage*[tiab]` | 48,158 | none |
| 7 | `bacteriophage*[tiab]` | 34,910 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 1,097,524 | none |
| 9 | `"Metagenomics"[Mesh]` | 5,229 | none |
| 10 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 11 | `metagenom*[tiab]` | 11,213 | none |
| 12 | `metagenome*[tiab]` | 3,784 | none |
| 13 | `virom*[tiab]` | 824 | none |
| 14 | `"high throughput sequencing"[tiab]` | 10,541 | none |
| 15 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 16 | `"deep sequencing"[tiab]` | 6,483 | none |
| 17 | `"massively parallel sequencing"[tiab]` | 1,756 | none |
| 18 | `"sequence independent amplification"[tiab]` | 65 | none |
| 19 | `SISPA[tiab]` | 43 | none |
| 20 | `NGS[tiab]` | 9,104 | none |
| 21 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 66,884 | none |
| 22 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 23 | `"Livestock"[Mesh]` | 3,200 | none |
| 24 | `"Poultry"[Mesh]` | 147,415 | none |
| 25 | `"Animal Husbandry"[Mesh]` | 20,395 | none |
| 26 | `"Cattle"[Mesh]` | 341,776 | none |
| 27 | `"Swine"[Mesh]` | 214,731 | none |
| 28 | `"Sheep"[Mesh]` | 116,801 | none |
| 29 | `"Goats"[Mesh]` | 30,623 | none |
| 30 | `"Horses"[Mesh]` | 67,676 | none |
| 31 | `"Chickens"[Mesh]` | 117,975 | none |
| 32 | `"Turkeys"[Mesh]` | 10,103 | none |
| 33 | `"Ducks"[Mesh]` | 10,534 | none |
| 34 | `"Geese"[Mesh]` | 2,682 | none |
| 35 | `"Rabbits"[Mesh]` | 337,179 | none |
| 36 | `"Camelus"[Mesh]` | 3,639 | none |
| 37 | `livestock[tiab]` | 21,337 | none |
| 38 | `"farm animal"[tiab]` | 833 | none |
| 39 | `"farm animals"[tiab]` | 3,038 | none |
| 40 | `"production animal"[tiab]` | 126 | none |
| 41 | `"production animals"[tiab]` | 294 | none |
| 42 | `"domestic animal"[tiab]` | 1,137 | none |
| 43 | `"domestic animals"[tiab]` | 7,245 | none |
| 44 | `cattle[tiab]` | 79,355 | none |
| 45 | `bovine[tiab]` | 189,144 | none |
| 46 | `cow[tiab]` | 29,456 | none |
| 47 | `cows[tiab]` | 45,341 | none |
| 48 | `calf[tiab]` | 43,460 | none |
| 49 | `calves[tiab]` | 24,854 | none |
| 50 | `swine[tiab]` | 42,358 | none |
| 51 | `pig[tiab]` | 127,282 | none |
| 52 | `pigs[tiab]` | 115,325 | none |
| 53 | `porcine[tiab]` | 79,145 | none |
| 54 | `piglet*[tiab]` | 17,109 | none |
| 55 | `sheep[tiab]` | 87,044 | none |
| 56 | `ovine[tiab]` | 20,361 | none |
| 57 | `lamb[tiab]` | 9,836 | none |
| 58 | `lambs[tiab]` | 14,624 | none |
| 59 | `goat[tiab]` | 19,304 | none |
| 60 | `goats[tiab]` | 18,753 | none |
| 61 | `caprine[tiab]` | 3,127 | none |
| 62 | `poultry[tiab]` | 25,731 | none |
| 63 | `chicken[tiab]` | 68,650 | none |
| 64 | `chickens[tiab]` | 34,114 | none |
| 65 | `broiler*[tiab]` | 16,896 | none |
| 66 | `turkey[tiab]` | 32,530 | none |
| 67 | `turkeys[tiab]` | 5,917 | none |
| 68 | `duck[tiab]` | 7,963 | none |
| 69 | `ducks[tiab]` | 5,494 | none |
| 70 | `geese[tiab]` | 1,928 | none |
| 71 | `horse[tiab]` | 33,966 | none |
| 72 | `horses[tiab]` | 30,374 | none |
| 73 | `equine[tiab]` | 28,778 | none |
| 74 | `foal*[tiab]` | 4,850 | none |
| 75 | `rabbit*[tiab]` | 252,771 | none |
| 76 | `camel*[tiab]` | 9,598 | none |
| 77 | `camelid*[tiab]` | 1,411 | none |
| 78 | `alpaca*[tiab]` | 1,132 | none |
| 79 | `llama*[tiab]` | 1,459 | none |
| 80 | `buffalo*[tiab]` | 10,572 | none |
| 81 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80` | 1,542,509 | none |
| 82 | `#8 AND #21 AND #81` | 910 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Viruses"[Mesh] OR "Bacteriophages"[Mesh] OR virus*[tiab] OR viral[tiab] OR virolog*[tiab] OR phage*[tiab] OR bacteriophage*[tiab]) AND ("Metagenomics"[Mesh] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR metagenom*[tiab] OR metagenome*[tiab] OR virom*[tiab] OR "high throughput sequencing"[tiab] OR "next generation sequencing"[tiab] OR "deep sequencing"[tiab] OR "massively parallel sequencing"[tiab] OR "sequence independent amplification"[tiab] OR SISPA[tiab] OR NGS[tiab]) AND ("Animals, Domestic"[Mesh] OR "Livestock"[Mesh] OR "Poultry"[Mesh] OR "Animal Husbandry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR "Chickens"[Mesh] OR "Turkeys"[Mesh] OR "Ducks"[Mesh] OR "Geese"[Mesh] OR "Rabbits"[Mesh] OR "Camelus"[Mesh] OR livestock[tiab] OR "farm animal"[tiab] OR "farm animals"[tiab] OR "production animal"[tiab] OR "production animals"[tiab] OR "domestic animal"[tiab] OR "domestic animals"[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR piglet*[tiab] OR sheep[tiab] OR ovine[tiab] OR lamb[tiab] OR lambs[tiab] OR goat[tiab] OR goats[tiab] OR caprine[tiab] OR poultry[tiab] OR chicken[tiab] OR chickens[tiab] OR broiler*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck[tiab] OR ducks[tiab] OR geese[tiab] OR horse[tiab] OR horses[tiab] OR equine[tiab] OR foal*[tiab] OR rabbit*[tiab] OR camel*[tiab] OR camelid*[tiab] OR alpaca*[tiab] OR llama*[tiab] OR buffalo*[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 21 | 21 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virus | 3,459 | 0 |
| metagenomics | 124,753 | 0 |
| farm_animals | 7,714 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 872 | initial | none | Initial three-block draft from question-defined scope; added broad viral terms, metagenomic/viromic/HTS terms, and named livestock/poultry categories with MeSH plus tiab vocabulary. Terms informed by MeSH lookups and 21 screened pilot records. |
| 2 | 910 | farm_animals: +8 / -0 | none | Round 1 critic revision: added MeSH and text-word terms for rabbits and camelids; explicitly excluded aquaculture from terrestrial farm-animal scope, marked scope unconfirmed as user requested no questions, and clarified development-only status of screened records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 3 findings; R1-1 should-fix open, R1-2 should-fix open, R1-3 document open
- Round 2 on version 2: 3 findings; R1-1 should-fix resolved, R1-2 should-fix resolved, R1-3 document resolved
- Round 3 on version 2: 3 findings; R1-1 should-fix resolved, R1-2 should-fix resolved, R1-3 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1021 NCBI requests logged (143 from cache); strategy sha256 d862f5ed4135._

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
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "requested": "Bacteriophages",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001435",
          "name": "Bacteriophages",
          "type": "descriptor",
          "scope_note": "Viruses whose hosts are bacterial cells.",
          "tree_numbers": [
            "B04.123"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001435",
      "preferred_label": "Bacteriophages",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Bacteriophages\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Metagenomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"Metagenomics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animal Husbandry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000822",
          "name": "Animal Husbandry",
          "type": "descriptor",
          "scope_note": "The science of breeding, feeding and care of domestic animals; includes housing and nutrition.",
          "tree_numbers": [
            "J01.040.090"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000822",
      "preferred_label": "Animal Husbandry",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "\"Animal Husbandry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chickens",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002645",
          "name": "Chickens",
          "type": "descriptor",
          "scope_note": "Common name for the species Gallus gallus, the domestic fowl, in the family Phasianidae, order GALLIFORMES. It is descended from the red jungle fowl of SOUTHEAST ASIA.",
          "tree_numbers": [
            "B01.050.150.900.248.350.150",
            "B01.050.150.900.248.690.192"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002645",
      "preferred_label": "Chickens",
      "type": "descriptor",
      "location": "vocabulary:29",
      "term": {
        "text": "\"Chickens\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Turkeys",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014422",
          "name": "Turkeys",
          "type": "descriptor",
          "scope_note": "Large woodland game BIRDS in the subfamily Meleagridinae, family Phasianidae, order GALLIFORMES. Formerly they were considered a distinct family, Melegrididae.",
          "tree_numbers": [
            "B01.050.150.900.248.350.800",
            "B01.050.150.900.248.690.800"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014422",
      "preferred_label": "Turkeys",
      "type": "descriptor",
      "location": "vocabulary:30",
      "term": {
        "text": "\"Turkeys\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ducks",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004372",
          "name": "Ducks",
          "type": "descriptor",
          "scope_note": "A water bird in the order Anseriformes (subfamily Anatinae (true ducks)) with a broad blunt bill, short legs, webbed feet, and a waddling gait.",
          "tree_numbers": [
            "B01.050.150.900.248.050.200",
            "B01.050.150.900.248.690.345"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004372",
      "preferred_label": "Ducks",
      "type": "descriptor",
      "location": "vocabulary:31",
      "term": {
        "text": "\"Ducks\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Geese",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005777",
          "name": "Geese",
          "type": "descriptor",
          "scope_note": "Any of various large waterfowl in the order Anseriformes, especially those of the genera Anser (gray geese) and Branta (black geese). They are larger than ducks but smaller than swans, prefer FRESH WATER, and occur primarily in the northern hemisphere.",
          "tree_numbers": [
            "B01.050.150.900.248.050.350",
            "B01.050.150.900.248.690.492"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005777",
      "preferred_label": "Geese",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "\"Geese\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rabbits",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Rabbits\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Camelus",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:11:05+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002162",
          "name": "Camelus",
          "type": "descriptor",
          "scope_note": "Two-toed, hoofed mammals with four legs, a big-lipped snout, and a humped back belonging to the family Camelidae. They are native to North Africa, and Western and Central Asia.",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.190.180"
          ],
          "entry_terms": 14,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002162",
      "preferred_label": "Camelus",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "\"Camelus\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Viruses\"[MeSH Terms] OR \"Bacteriophages\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virolog*\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"bacteriophage*\"[Title/Abstract]) AND (\"Metagenomics\"[MeSH Terms] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"metagenome*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"high throughput sequencing\"[Title/Abstract] OR \"next generation sequencing\"[Title/Abstract] OR \"deep sequencing\"[Title/Abstract] OR \"massively parallel sequencing\"[Title/Abstract] OR \"sequence independent amplification\"[Title/Abstract] OR \"SISPA\"[Title/Abstract] OR \"NGS\"[Title/Abstract]) AND (\"animals, domestic\"[MeSH Terms] OR \"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Animal Husbandry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Chickens\"[MeSH Terms] OR \"Turkeys\"[MeSH Terms] OR \"Ducks\"[MeSH Terms] OR \"Geese\"[MeSH Terms] OR \"Rabbits\"[MeSH Terms] OR \"Camelus\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm animal\"[Title/Abstract] OR \"farm animals\"[Title/Abstract] OR \"production animal\"[Title/Abstract] OR \"production animals\"[Title/Abstract] OR \"domestic animal\"[Title/Abstract] OR \"domestic animals\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"piglet*\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"lamb\"[Title/Abstract] OR \"lambs\"[Title/Abstract] OR \"goat\"[Title/Abstract] OR \"Goats\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"chicken\"[Title/Abstract] OR \"Chickens\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"Turkeys\"[Title/Abstract] OR \"duck\"[Title/Abstract] OR \"Ducks\"[Title/Abstract] OR \"Geese\"[Title/Abstract] OR \"horse\"[Title/Abstract] OR \"Horses\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"foal*\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"camel*\"[Title/Abstract] OR \"camelid*\"[Title/Abstract] OR \"alpaca*\"[Title/Abstract] OR \"llama*\"[Title/Abstract] OR \"buffalo*\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "da964adb408d77727d3b7ed659f06d58dd619c17272ac7d67b6fdf6fcb3ea8be",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The three Boolean blocks reflect the stated concepts, but the farm-animal vocabulary does not cover several plausible production species. All 21 known records were retrieved, though that set was used during development and is not independent validation."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each concept and AND combines the three concepts, consistent with the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified and shows their translations. The domestic-animal heading is broad, but conjunction with the virus and method blocks limits its effect."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The animal text words emphasize common livestock and poultry but omit other plausible farmed species, creating a risk for records indexed or described only by those species."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query and PubMed translation preserve the intended grouping. The packet reports no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility filter is applied. The entry-date cutoff is documented as an as-of boundary rather than a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The farm-animal block names cattle, swine, sheep, goats, horses, and poultry species, but omits other plausible production animals such as rabbits and camelids. Records whose titles and abstracts identify only an omitted species may not meet this block.",
          "recommendation": "Add appropriate MeSH and title/abstract terms for additional in-scope production species, at minimum rabbits; define whether camelids and other regionally farmed species are in scope, then add their terms if included.",
          "status": "open"
        },
        {
          "id": "R1-2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The scope rationale says aquatic farmed species are an uncertain boundary and will be screened if retrieved, while the searched animal block contains no aquatic species terms. As written, records about aquatic farmed species alone are unlikely to be retrieved for that screening.",
          "recommendation": "Clarify whether aquatic farmed species are in scope. If they are to be screened, add suitable aquaculture and farmed aquatic-species terms; otherwise document that they are outside the search scope.",
          "status": "open"
        },
        {
          "id": "R1-3",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "The known-record set has 100% retrieval, but the packet identifies it as development data rather than independent validation. This supports coverage of those records, not broader sensitivity.",
          "recommendation": "Describe the 21-record result as development-set coverage and avoid presenting it as independent validation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "e5ab746dd174c8e8e79106e7b7c23decb2817f203d0b3d19c3e4b29db09d11e1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The revised scope explicitly includes terrestrial livestock, poultry, rabbits, and camelids, and excludes aquaculture. The animal block now has rabbit and camelid-related terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines terms within each concept and AND combines the three concepts. The known-record set is explicitly identified as development data, not independent validation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified and shows their translations. The rabbit and Camelus headings support the expanded animal scope."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised animal block adds rabbit*, camel*, camelid*, alpaca*, llama*, and buffalo* alongside livestock and poultry terms, covering the newly specified rabbit and camelid scope."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query and PubMed translation preserve the intended three-block grouping. The packet reports no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility filters are applied. The entry-date cutoff is documented as an as-of boundary, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier animal block omitted plausible production species, including rabbits and camelids.",
          "recommendation": "Add terms for in-scope production species and state whether camelids and other regionally farmed species are included.",
          "status": "resolved",
          "response": "The revised scope explicitly includes rabbits and camelids; the block adds \"Rabbits\"[Mesh], rabbit*[tiab], \"Camelus\"[Mesh], camel*[tiab], camelid*[tiab], alpaca*[tiab], and llama*[tiab]. It also adds buffalo*[tiab]."
        },
        {
          "id": "R1-2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier scope left the status of aquatic farmed species uncertain while the search lacked aquatic-species terms.",
          "recommendation": "Clarify whether aquatic farmed species are in scope and add terms if they are to be screened.",
          "status": "resolved",
          "response": "The revised scope explicitly excludes aquaculture and aquatic farmed species, so no aquatic terms are required for this operational scope."
        },
        {
          "id": "R1-3",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "The 21 known records were development data, so their 100% retrieval does not constitute independent validation.",
          "recommendation": "Describe the result as development-set coverage and avoid presenting it as independent validation.",
          "status": "resolved",
          "response": "The packet labels the set as records screened relevant during the build and states that it was used for development, not independent validation."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "e5ab746dd174c8e8e79106e7b7c23decb2817f203d0b3d19c3e4b29db09d11e1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The scope explicitly includes terrestrial livestock, poultry, rabbits, and camelids, and excludes aquaculture. The animal block reflects that scope."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines terms within each concept and AND combines the three concepts. The known-record set is identified as development data, not independent validation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the MeSH headings as verified and shows their translations, including the headings added for rabbits and camels."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The animal block includes rabbit and camelid terms alongside livestock and poultry terms, consistent with the stated scope."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query and PubMed translation preserve the intended three-block grouping. The packet reports no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility filters are applied. The entry-date cutoff is documented as an as-of boundary, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier animal block omitted plausible production species, including rabbits and camelids.",
          "recommendation": "Add terms for in-scope production species and state whether camelids and other regionally farmed species are included.",
          "status": "resolved",
          "response": "The revised scope explicitly includes rabbits and camelids. The block adds \"Rabbits\"[Mesh], rabbit*[tiab], \"Camelus\"[Mesh], camel*[tiab], camelid*[tiab], alpaca*[tiab], and llama*[tiab]."
        },
        {
          "id": "R1-2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier scope left the status of aquatic farmed species uncertain while the search lacked aquatic-species terms.",
          "recommendation": "Clarify whether aquatic farmed species are in scope and add terms if they are to be screened.",
          "status": "resolved",
          "response": "The revised scope explicitly excludes aquaculture and aquatic farmed species, so aquatic terms are not required for this operational scope."
        },
        {
          "id": "R1-3",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "The 21 known records were development data, so their 100% retrieval does not constitute independent validation.",
          "recommendation": "Describe the result as development-set coverage and avoid presenting it as independent validation.",
          "status": "resolved",
          "response": "The packet identifies the records as screened during the build and states they were used for development, not independent validation."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


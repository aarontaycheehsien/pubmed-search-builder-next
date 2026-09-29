# PubMed search strategy: audit

Generated 2026-09-28T23:00:08+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC (scoping review)
- Scope confirmed by user: no (User asked to proceed without clarification. Assumed a PCC-style scoping question, interpreting farm animals as food-producing livestock, poultry, camelids, buffalo/bison, quail, and rabbits; farmed aquatic species are outside this operational scope. Search cutoff is PubMed entry date 2019-02-22 via PSB_AS_OF; no publication-date limit. No known relevant articles were supplied. This scope was not confirmed by the user. Screening excludes reviews and protocols, but broad search vocabulary may retrieve them.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Virus/virome metagenomics | search | The defining method/topic: included studies must use metagenomic approaches to characterize viruses or viromes; searchable by method and virus/virome wording or indexing. |
| Farm animals | search | The population/context is explicit. The block names livestock and poultry and includes additional food-producing camelids, buffalo/bison, and quail; a category probe checks for records naming only other species. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:58:36+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 1,444
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `(("Metagenomics"[Mesh] OR "Genomics"[Mesh] OR metagenom*[tiab]) AND ("Virology"[Mesh] OR "Viruses"[Mesh] OR virus*[tiab] OR viral[tiab] OR virom*[tiab]))` | 5,821 | none |
| 2 | `("High-Throughput Nucleotide Sequencing"[Mesh] AND ("Virology"[Mesh] OR "Viruses"[Mesh] OR virus*[tiab] OR viral[tiab] OR virom*[tiab]))` | 2,939 | none |
| 3 | `(sequenc*[tiab] AND ((next[tiab] AND generation[tiab]) OR (high[tiab] AND throughput[tiab]) OR deep[tiab] OR shotgun[tiab]) AND (virus*[tiab] OR viral[tiab] OR virom*[tiab]))` | 5,654 | none |
| 4 | `virom*[tiab]` | 824 | none |
| 5 | `#1 OR #2 OR #3 OR #4` | 11,730 | none |
| 6 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 7 | `"Livestock"[Mesh]` | 3,200 | none |
| 8 | `"Poultry"[Mesh]` | 147,415 | none |
| 9 | `"Cattle"[Mesh]` | 341,776 | none |
| 10 | `"Swine"[Mesh]` | 214,731 | none |
| 11 | `"Sheep"[Mesh]` | 116,801 | none |
| 12 | `"Goats"[Mesh]` | 30,623 | none |
| 13 | `"Horses"[Mesh]` | 67,676 | none |
| 14 | `"Chickens"[Mesh]` | 117,975 | none |
| 15 | `"Ducks"[Mesh]` | 10,534 | none |
| 16 | `"Geese"[Mesh]` | 2,682 | none |
| 17 | `"Turkeys"[Mesh]` | 10,103 | none |
| 18 | `"Rabbits"[Mesh]` | 337,179 | none |
| 19 | `farm animal*[tiab]` | 3,666 | none |
| 20 | `livestock[tiab]` | 21,337 | none |
| 21 | `poultry[tiab]` | 25,731 | none |
| 22 | `cattle[tiab]` | 79,355 | none |
| 23 | `bovine[tiab]` | 189,144 | none |
| 24 | `calf[tiab]` | 43,460 | none |
| 25 | `calves[tiab]` | 24,854 | none |
| 26 | `cow[tiab]` | 29,456 | none |
| 27 | `cows[tiab]` | 45,341 | none |
| 28 | `pig[tiab]` | 127,282 | none |
| 29 | `pigs[tiab]` | 115,325 | none |
| 30 | `swine[tiab]` | 42,358 | none |
| 31 | `porcine[tiab]` | 79,145 | none |
| 32 | `hog[tiab]` | 3,731 | none |
| 33 | `hogs[tiab]` | 718 | none |
| 34 | `chicken*[tiab]` | 92,941 | none |
| 35 | `fowl[tiab]` | 6,948 | none |
| 36 | `avian[tiab]` | 50,972 | none |
| 37 | `turkey[tiab]` | 32,530 | none |
| 38 | `turkeys[tiab]` | 5,917 | none |
| 39 | `duck*[tiab]` | 13,075 | none |
| 40 | `goose[tiab]` | 2,645 | none |
| 41 | `geese[tiab]` | 1,928 | none |
| 42 | `sheep[tiab]` | 87,044 | none |
| 43 | `lamb[tiab]` | 9,836 | none |
| 44 | `lambs[tiab]` | 14,624 | none |
| 45 | `ovine[tiab]` | 20,361 | none |
| 46 | `goat[tiab]` | 19,304 | none |
| 47 | `goats[tiab]` | 18,753 | none |
| 48 | `caprine[tiab]` | 3,127 | none |
| 49 | `horse*[tiab]` | 80,001 | none |
| 50 | `equine[tiab]` | 28,777 | none |
| 51 | `rabbit*[tiab]` | 252,771 | none |
| 52 | `"Camelus"[Mesh]` | 3,639 | none |
| 53 | `"Camelids, New World"[Mesh]` | 2,181 | none |
| 54 | `"Buffaloes"[Mesh]` | 5,971 | none |
| 55 | `"Bison"[Mesh]` | 778 | none |
| 56 | `"Quail"[Mesh]` | 8,742 | none |
| 57 | `camel*[tiab]` | 9,598 | none |
| 58 | `camelid*[tiab]` | 1,411 | none |
| 59 | `buffalo*[tiab]` | 10,572 | none |
| 60 | `bison[tiab]` | 1,108 | none |
| 61 | `alpaca*[tiab]` | 1,132 | none |
| 62 | `llama*[tiab]` | 1,459 | none |
| 63 | `quail*[tiab]` | 8,607 | none |
| 64 | `#6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63` | 1,594,965 | none |
| 65 | `#5 AND #64` | 1,444 | none |

### Strategy (single line, for copying into PubMed)

```text
(((("Metagenomics"[Mesh] OR "Genomics"[Mesh] OR metagenom*[tiab]) AND ("Virology"[Mesh] OR "Viruses"[Mesh] OR virus*[tiab] OR viral[tiab] OR virom*[tiab])) OR ("High-Throughput Nucleotide Sequencing"[Mesh] AND ("Virology"[Mesh] OR "Viruses"[Mesh] OR virus*[tiab] OR viral[tiab] OR virom*[tiab])) OR (sequenc*[tiab] AND ((next[tiab] AND generation[tiab]) OR (high[tiab] AND throughput[tiab]) OR deep[tiab] OR shotgun[tiab]) AND (virus*[tiab] OR viral[tiab] OR virom*[tiab])) OR virom*[tiab]) AND ("Animals, Domestic"[Mesh] OR "Livestock"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR "Chickens"[Mesh] OR "Ducks"[Mesh] OR "Geese"[Mesh] OR "Turkeys"[Mesh] OR "Rabbits"[Mesh] OR farm animal*[tiab] OR livestock[tiab] OR poultry[tiab] OR cattle[tiab] OR bovine[tiab] OR calf[tiab] OR calves[tiab] OR cow[tiab] OR cows[tiab] OR pig[tiab] OR pigs[tiab] OR swine[tiab] OR porcine[tiab] OR hog[tiab] OR hogs[tiab] OR chicken*[tiab] OR fowl[tiab] OR avian[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck*[tiab] OR goose[tiab] OR geese[tiab] OR sheep[tiab] OR lamb[tiab] OR lambs[tiab] OR ovine[tiab] OR goat[tiab] OR goats[tiab] OR caprine[tiab] OR horse*[tiab] OR equine[tiab] OR rabbit*[tiab] OR "Camelus"[Mesh] OR "Camelids, New World"[Mesh] OR "Buffaloes"[Mesh] OR "Bison"[Mesh] OR "Quail"[Mesh] OR camel*[tiab] OR camelid*[tiab] OR buffalo*[tiab] OR bison[tiab] OR alpaca*[tiab] OR llama*[tiab] OR quail*[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 24 | 24 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Farm animals | 1 | `animal*[tiab] OR mammal*[tiab] OR bird*[tiab] OR ruminant*[tiab] OR domesticated[tiab] OR farmed[tiab]` | 514 | 0/30 |
| Farm animals | 2 | `animal*[tiab] OR mammal*[tiab] OR bird*[tiab] OR ruminant*[tiab] OR domesticated[tiab] OR farmed[tiab]` | 919 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| viral_metagenomics | 1,594,965 | 0 |
| farm_animals | 11,730 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 638 | initial | none | Baseline evaluation after adding 23 screened discovery records. |
| 2 | 19,729 | viral_metagenomics: +2 / -0 | none | Expanded the virus/metagenomics block with the pre-2019 High-Throughput Nucleotide Sequencing MeSH descriptor and broad virus-plus-sequencing text to catch records that name sequencing rather than metagenomics. Added one clearly eligible pilot record discovered on screening. |
| 3 | 1,288 | viral_metagenomics: +1 / -1 | none | Removed the over-broad any-sequencing branch after it raised results above budget. Kept High-Throughput Nucleotide Sequencing MeSH and restricted title/abstract sequencing to next-generation, high-throughput, deep, or shotgun sequencing with viral wording. |
| 4 | 1,444 | viral_metagenomics: +2 / -2; farm_animals: +12 / -0 | none | Addressed critic round 1: added the verified Viruses[Mesh] heading to method-constrained viral branches; added Camelus/Camelids New World, Buffaloes, Bison, Quail MeSH and corresponding bare title/abstract species words as plausible food-producing farm-animal members; updated eligibility/assumptions. Retained the Entrez-date cutoff because the user and harness explicitly require the 2019-02-22 historical index state; no [dp] limit. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 3 findings; R1-F1 must-fix open, R1-F2 should-fix open, R1-F3 should-fix open
- Round 2 on version 4: 3 findings; R1-F1 must-fix rejected, R1-F2 should-fix resolved, R1-F3 should-fix resolved
- Round 3 on version 4: 3 findings; R1-F1 must-fix rejected, R1-F2 should-fix resolved, R1-F3 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1022 NCBI requests logged (463 from cache); strategy sha256 47579cc83560._

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
      "requested": "Metagenomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
        "text": "\"Metagenomics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Genomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D023281",
          "name": "Genomics",
          "type": "descriptor",
          "scope_note": "The systematic study of the complete DNA sequences (GENOME) of organisms. Included is construction of complete genetic, physical, and transcript maps, and the analysis of this structural genomic information on a global scale such as in GENOME WIDE ASSOCIATION STUDIES.",
          "tree_numbers": [
            "H01.158.273.180.350",
            "H01.158.273.343.350"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D023281",
      "preferred_label": "Genomics",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Genomics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Virology",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
          "ui": "D014773",
          "name": "Virology",
          "type": "descriptor",
          "scope_note": "The study of the structure, growth, function, genetics, and reproduction of viruses, and VIRUS DISEASES.",
          "tree_numbers": [
            "H01.158.273.540.859"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014773",
      "preferred_label": "Virology",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Virology\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "requested": "Virology",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
          "ui": "D014773",
          "name": "Virology",
          "type": "descriptor",
          "scope_note": "The study of the structure, growth, function, genetics, and reproduction of viruses, and VIRUS DISEASES.",
          "tree_numbers": [
            "H01.158.273.540.859"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014773",
      "preferred_label": "Virology",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Virology\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chickens",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Chickens\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ducks",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Ducks\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Geese",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "\"Geese\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Turkeys",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "\"Turkeys\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rabbits",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "\"Rabbits\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Camelus",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
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
      "location": "vocabulary:72",
      "term": {
        "text": "\"Camelus\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Camelids, New World",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002161",
          "name": "Camelids, New World",
          "type": "descriptor",
          "scope_note": "Camelidae of the Americas. The extant species are those originating from South America and include alpacas, llamas, guanicos, and vicunas.",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.190.090"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002161",
      "preferred_label": "Camelids, New World",
      "type": "descriptor",
      "location": "vocabulary:73",
      "term": {
        "text": "\"Camelids, New World\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Buffaloes",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002020",
          "name": "Buffaloes",
          "type": "descriptor",
          "scope_note": "Ruminants of the family Bovidae consisting of Bubalus arnee and Syncerus caffer. This concept is differentiated from BISON, which refers to Bison bison and Bison bonasus.",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.380.135"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002020",
      "preferred_label": "Buffaloes",
      "type": "descriptor",
      "location": "vocabulary:74",
      "term": {
        "text": "\"Buffaloes\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bison",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016164",
          "name": "Bison",
          "type": "descriptor",
          "scope_note": "A genus of the family Bovidae having two species: B. bison and B. bonasus. This concept is differentiated from BUFFALOES, which refers to Bubalus arnee and Syncerus caffer.",
          "tree_numbers": [
            "B01.050.150.900.649.313.500.380.120"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016164",
      "preferred_label": "Bison",
      "type": "descriptor",
      "location": "vocabulary:75",
      "term": {
        "text": "\"Bison\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Quail",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:58:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011784",
          "name": "Quail",
          "type": "descriptor",
          "scope_note": "Common name for two distinct groups of BIRDS in the order GALLIFORMES: the New World or American quails of the family Odontophoridae and the Old World quails in the genus COTURNIX, family Phasianidae.",
          "tree_numbers": [
            "B01.050.150.900.248.350.650"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011784",
      "preferred_label": "Quail",
      "type": "descriptor",
      "location": "vocabulary:76",
      "term": {
        "text": "\"Quail\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(((\"Metagenomics\"[MeSH Terms] OR \"Genomics\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract]) AND (\"Virology\"[MeSH Terms] OR \"Viruses\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract])) OR (\"High-Throughput Nucleotide Sequencing\"[MeSH Terms] AND (\"Virology\"[MeSH Terms] OR \"Viruses\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract])) OR (\"sequenc*\"[Title/Abstract] AND ((\"next\"[Title/Abstract] AND \"generation\"[Title/Abstract]) OR (\"high\"[Title/Abstract] AND \"throughput\"[Title/Abstract]) OR \"deep\"[Title/Abstract] OR \"shotgun\"[Title/Abstract]) AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract])) OR \"virom*\"[Title/Abstract]) AND (\"animals, domestic\"[MeSH Terms] OR \"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Chickens\"[MeSH Terms] OR \"Ducks\"[MeSH Terms] OR \"Geese\"[MeSH Terms] OR \"Turkeys\"[MeSH Terms] OR \"Rabbits\"[MeSH Terms] OR \"farm animal*\"[Title/Abstract] OR \"Livestock\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"hog\"[Title/Abstract] OR \"hogs\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"fowl\"[Title/Abstract] OR \"avian\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"Turkeys\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"Geese\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"lamb\"[Title/Abstract] OR \"lambs\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat\"[Title/Abstract] OR \"Goats\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"Camelus\"[MeSH Terms] OR \"camelids, new world\"[MeSH Terms] OR \"Buffaloes\"[MeSH Terms] OR \"Bison\"[MeSH Terms] OR \"Quail\"[MeSH Terms] OR \"camel*\"[Title/Abstract] OR \"camelid*\"[Title/Abstract] OR \"buffalo*\"[Title/Abstract] OR \"Bison\"[Title/Abstract] OR \"alpaca*\"[Title/Abstract] OR \"llama*\"[Title/Abstract] OR \"quail*\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "083da13c7c17241cbc588559f9fb07a24975bac67ed8dfefd211fe504520d8bf",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two search blocks reflect the stated concepts. The farm animal terms cover the named livestock and poultry concepts, and virom*[tiab] provides a standalone virome route."
        },
        "operators": {
          "verdict": "pass",
          "note": "The OR terms within each block and AND between concepts match the search roles. The sequencing expressions use explicit Boolean combinations; no phrase or proximity warnings are shown."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The viral block uses Virology[Mesh] but omits Viruses[Mesh], which could retrieve records indexed for viruses without virus wording in searchable text."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The population text vocabulary lacks some food-producing farm species named only by species, including camel and buffalo, and poultry species such as quail. The clean probes screened only 60 sampled records and do not establish that these omissions are harmless."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed translations show no errors, warnings, or translation issues, and the strategy has no lint findings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The executed search applies an Entry Date limit ending 2019-02-22, although the question and eligibility criteria give no date restriction. This excludes later indexed records."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query is limited to PubMed entry dates through 2019-02-22. No date limit is justified by the question or eligibility criteria, so the reported 1,288 records cannot represent a current search.",
          "recommendation": "Remove the Entry Date cutoff unless the review protocol explicitly requires it, then rerun and document the full strategy evaluation.",
          "status": "open"
        },
        {
          "id": "R1-F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The virus block includes Virology[Mesh] but not Viruses[Mesh]. Relevant records indexed under Viruses without virus or virome wording in title/abstract may be missed.",
          "recommendation": "Assess and add Viruses[Mesh] to the viral block, then rerun the complete evaluation.",
          "status": "open"
        },
        {
          "id": "R1-F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The farm animal block does not explicitly name several plausible food-producing farm species, such as camel, buffalo, and quail. The two category probes screened 60 records without finding relevant omissions, but that sample does not resolve this vocabulary gap.",
          "recommendation": "Add appropriate bare species names and applicable subject headings for in-scope farm species, then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "c04c68f354aabec20ce2497d8bbbb839f448c2c12daa7ef51217dc45bc687952",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two searched concepts match the stated topic under the documented scope assumptions."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Boolean structure uses OR within concepts and AND between concepts; all alternatives have explicit fields."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Viruses[Mesh] was added alongside Virology[Mesh]; livestock and added food-producing species headings are represented."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Species-wording gaps identified in round 1 were addressed with bare species names and corresponding headings."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no syntax, translation, lint, or field issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date cutoff is required for this run: the user explicitly instructed us to work as of 2019-02-22, keep PSB_AS_OF set for every command, and exclude records added to PubMed after that date. The strategy uses the resulting [edat] restriction and no [dp] limit."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query remains limited to PubMed entry dates through 2019-02-22, although the question and eligibility criteria state no date restriction. The reported 1,444 records therefore do not represent an unrestricted search.",
          "recommendation": "Remove the Entry Date cutoff unless the review protocol explicitly requires it, then rerun and document the full strategy evaluation.",
          "status": "rejected",
          "response": "This finding conflicts with the run instructions. The user required a 2019-02-22 historical PubMed index, required PSB_AS_OF to remain set for every command, and prohibited post-cutoff PubMed records. The query therefore correctly carries an [edat] bound through 2019-02-22. No [dp] limit was added, as instructed. The count is explicitly reported for that historical entry-date bound, not as a current unrestricted search."
        },
        {
          "id": "R1-F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier draft omitted Viruses[Mesh] from the viral block.",
          "recommendation": "Add Viruses[Mesh] to the viral block and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current viral block includes Viruses[Mesh] in its metagenomics and high-throughput sequencing branches; PubMed translated and evaluated the heading without warnings."
        },
        {
          "id": "R1-F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier draft did not explicitly name several in-scope food-producing farm species, including camelids, buffalo/bison, and quail.",
          "recommendation": "Add appropriate bare species names and applicable subject headings for the in-scope farm species, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current farm-animal block now includes Camelus, Camelids, Buffaloes, Bison, and Quail headings and camel*, camelid*, buffalo*, bison, alpaca*, llama*, and quail* title/abstract terms."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-0b3f5bccffad386dd2e7",
          "status": "accepted-risk",
          "response": "Accept this review warning because the two category probes were screened before the last viral-block and species-vocabulary edits, and the probe budget is spent. The final population block now includes the species raised by the critique. The earlier 0/30 and 0/30 findings are supportive but do not establish category coverage for the current full query; this remains a limitation for human peer review.",
          "evidence": "The current evaluation marks farm_animals as category_probe_stale_budget_spent. The two stored probes report 0 relevant among 30 screened each. The final block adds Camelus/Camelids, Buffaloes, Bison, and Quail MeSH headings and corresponding free-text terms; the final version retrieves all 24 screened development records."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "c04c68f354aabec20ce2497d8bbbb839f448c2c12daa7ef51217dc45bc687952",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two search blocks match the stated concepts and documented scope. The population block includes the specified farm animals, and the viral block includes metagenomics and sequencing routes plus a standalone virome term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Boolean structure combines alternatives within concepts and intersects the two concepts. The sequencing expressions use explicit Boolean combinations."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The viral block now includes Viruses[Mesh] alongside Virology[Mesh]. Relevant livestock and additional in-scope species headings are present."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The added camel, buffalo/bison, and quail vocabulary addresses the species gaps from round 1. All 24 screened development records are retrieved; the stale category probes remain an accepted limitation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no syntax, translation, lint, or field issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date cutoff is justified by the documented instruction to use the PubMed index as of 2019-02-22 and exclude later-added records. The strategy does not apply a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query uses an Entry Date cutoff through 2019-02-22.",
          "recommendation": "Retain the cutoff only for the instructed historical PubMed index and report the count for that bound.",
          "status": "rejected",
          "response": "The run instructions require the 2019-02-22 historical index, require PSB_AS_OF for every command, and exclude records added after the cutoff. The [edat] bound implements those instructions; no [dp] limit was added."
        },
        {
          "id": "R1-F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier draft omitted Viruses[Mesh] from the viral block.",
          "recommendation": "Add Viruses[Mesh] to the viral block and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current viral block includes Viruses[Mesh] in its metagenomics and high-throughput sequencing branches, and the heading translated and evaluated without warnings."
        },
        {
          "id": "R1-F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The earlier draft did not explicitly name several in-scope food-producing farm species, including camelids, buffalo/bison, and quail.",
          "recommendation": "Add appropriate bare species names and applicable subject headings for the in-scope farm species, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current block includes Camelus, Camelids, Buffaloes, Bison, and Quail headings, with corresponding camel, camelid, buffalo, bison, alpaca, llama, and quail title/abstract terms."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-0b3f5bccffad386dd2e7",
          "status": "accepted-risk",
          "response": "Accept the stale-probe warning as a documented limitation. Both category probes were screened before the final population-vocabulary edits, and the probe budget is spent.",
          "evidence": "The two stored probes found 0 relevant records among 30 screened each. The final block adds the species raised by the critique and retrieves all 24 screened development records; the probes do not establish category coverage for the final block."
        }
      ]
    }
  ]
}
```


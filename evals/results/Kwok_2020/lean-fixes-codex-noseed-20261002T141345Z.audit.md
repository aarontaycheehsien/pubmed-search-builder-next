# PubMed search strategy: audit

Generated 2026-10-02T14:27:59+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: no (Proceeding without clarification at the user's request. Assumes farm animals means livestock and other animals raised for food or agricultural production, including poultry; associated vectors are included when directly sampled from a named farm-animal host, as with cattle-parasitizing ticks. Farm-production environmental samples count only when explicitly connected to farm animals. Farming of aquatic species is not explicitly included; rabbits and geese are treated as in-scope farmed taxa. Entrez date is bounded by PSB_AS_OF=2019-02-22 for this run; no publication-date limit. No known relevant records were supplied. No web search used. The systematic[sb] candidate query found no matching review; a 50-record pilot sample was screened by title, six candidates were fetched by abstract, and five were included as a development set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Metagenomics and viromics methods | search | The method defines the review and is named in MeSH or title/abstract terms; virome terminology also represents viral metagenomic work. |
| Viruses and phages | search | The viral target is central and identifiable through virus, viral, phage, virome, and relevant indexing terms. |
| Farmed/domestic animals | search | The animal population is central and can be searched with domestic animal/livestock headings and species terms. |
| Use, findings, and applications of viral metagenomics | screen | Outcomes and applications are not consistently named and are handled at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:26:30+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 773
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Metagenomics"[Mesh]` | 5,229 | none |
| 2 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 3 | `metagenom*[tiab]` | 11,213 | none |
| 4 | `virom*[tiab]` | 824 | none |
| 5 | `"next-generation sequencing"[tiab]` | 26,834 | none |
| 6 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 7 | `"high-throughput sequencing"[tiab]` | 10,541 | none |
| 8 | `"high throughput sequencing"[tiab]` | 10,541 | none |
| 9 | `"shotgun sequencing"[tiab]` | 1,193 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 62,182 | none |
| 11 | `"Viruses"[Mesh]` | 759,255 | none |
| 12 | `"Virology"[Mesh]` | 5,387 | none |
| 13 | `virus*[tiab]` | 687,408 | none |
| 14 | `viral[tiab]` | 333,289 | none |
| 15 | `phage*[tiab]` | 48,158 | none |
| 16 | `virom*[tiab]` | 824 | none |
| 17 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16` | 1,088,328 | none |
| 18 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 19 | `"Livestock"[Mesh]` | 3,200 | none |
| 20 | `"Poultry"[Mesh]` | 147,415 | none |
| 21 | `"Cattle"[Mesh]` | 341,776 | none |
| 22 | `"Swine"[Mesh]` | 214,731 | none |
| 23 | `"Sheep"[Mesh]` | 116,801 | none |
| 24 | `"Goats"[Mesh]` | 30,623 | none |
| 25 | `"Horses"[Mesh]` | 67,676 | none |
| 26 | `livestock[tiab]` | 21,337 | none |
| 27 | `"farm animal"[tiab]` | 833 | none |
| 28 | `"farm animals"[tiab]` | 3,038 | none |
| 29 | `"food animal"[tiab]` | 898 | none |
| 30 | `"food animals"[tiab]` | 1,313 | none |
| 31 | `cattle[tiab]` | 79,355 | none |
| 32 | `bovine[tiab]` | 189,144 | none |
| 33 | `cow[tiab]` | 29,456 | none |
| 34 | `cows[tiab]` | 45,341 | none |
| 35 | `calf[tiab]` | 43,460 | none |
| 36 | `calves[tiab]` | 24,854 | none |
| 37 | `swine[tiab]` | 42,358 | none |
| 38 | `pig[tiab]` | 127,282 | none |
| 39 | `pigs[tiab]` | 115,325 | none |
| 40 | `piglet[tiab]` | 5,096 | none |
| 41 | `piglets[tiab]` | 15,534 | none |
| 42 | `porcine[tiab]` | 79,145 | none |
| 43 | `hog[tiab]` | 3,731 | none |
| 44 | `hogs[tiab]` | 718 | none |
| 45 | `poultry[tiab]` | 25,731 | none |
| 46 | `chicken*[tiab]` | 92,941 | none |
| 47 | `hen[tiab]` | 13,136 | none |
| 48 | `hens[tiab]` | 11,058 | none |
| 49 | `turkey[tiab]` | 32,530 | none |
| 50 | `turkeys[tiab]` | 5,917 | none |
| 51 | `duck[tiab]` | 7,963 | none |
| 52 | `ducks[tiab]` | 5,494 | none |
| 53 | `sheep[tiab]` | 87,044 | none |
| 54 | `ovine[tiab]` | 20,361 | none |
| 55 | `goat*[tiab]` | 31,547 | none |
| 56 | `caprine[tiab]` | 3,127 | none |
| 57 | `horse*[tiab]` | 80,001 | none |
| 58 | `equine[tiab]` | 28,778 | none |
| 59 | `buffalo[tiab]` | 9,137 | none |
| 60 | `camel[tiab]` | 3,210 | none |
| 61 | `camels[tiab]` | 2,296 | none |
| 62 | `"Rabbits"[Mesh]` | 337,179 | none |
| 63 | `rabbit*[tiab]` | 252,771 | none |
| 64 | `goose[tiab]` | 2,645 | none |
| 65 | `geese[tiab]` | 1,928 | none |
| 66 | `#18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65` | 1,558,104 | none |
| 67 | `#10 AND #17 AND #66` | 773 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Metagenomics"[Mesh] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR metagenom*[tiab] OR virom*[tiab] OR "next-generation sequencing"[tiab] OR "next generation sequencing"[tiab] OR "high-throughput sequencing"[tiab] OR "high throughput sequencing"[tiab] OR "shotgun sequencing"[tiab]) AND ("Viruses"[Mesh] OR "Virology"[Mesh] OR virus*[tiab] OR viral[tiab] OR phage*[tiab] OR virom*[tiab]) AND ("Animals, Domestic"[Mesh] OR "Livestock"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR livestock[tiab] OR "farm animal"[tiab] OR "farm animals"[tiab] OR "food animal"[tiab] OR "food animals"[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR piglet[tiab] OR piglets[tiab] OR porcine[tiab] OR hog[tiab] OR hogs[tiab] OR poultry[tiab] OR chicken*[tiab] OR hen[tiab] OR hens[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck[tiab] OR ducks[tiab] OR sheep[tiab] OR ovine[tiab] OR goat*[tiab] OR caprine[tiab] OR horse*[tiab] OR equine[tiab] OR buffalo[tiab] OR camel[tiab] OR camels[tiab] OR "Rabbits"[Mesh] OR rabbit*[tiab] OR goose[tiab] OR geese[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| metagenomics | 125,147 | 0 |
| virus | 3,105 | 0 |
| farm_animals | 6,908 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 270 | initial | none | Initial recall-first draft. Two blocks follow the PCC scope; MeSH plus free text for both. Discovery sample screened to seed vocabulary; no review benchmark found. |
| 2 | 559 | viral_metagenomics: +0 / -4; metagenomics: +4 / -0; virus: +6 / -0 | none | Reworked the viral metagenomics concept into method, viral target, and farm-animal blocks to avoid a compound block; added virome terms to both method and virus blocks so virome-only wording satisfies both concepts. |
| 3 | 773 | metagenomics: +5 / -0; farm_animals: +4 / -0 | none | Critic revision 1: added free-text next-generation, high-throughput, and shotgun sequencing terms to broaden method retrieval for unindexed records; added Rabbits MeSH, rabbit*, goose, and geese for farmed taxa treated as in scope. Kept no publication-date limit. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-TW-01 should-fix open, R1-TW-02 should-fix open
- Round 2 on version 3: 2 findings; R1-TW-01 should-fix resolved, R1-TW-02 should-fix resolved
- Round 3 on version 3: 2 findings; R1-TW-01 should-fix resolved, R1-TW-02 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 507 NCBI requests logged (203 from cache); strategy sha256 132bc669425b._

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
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"High-Throughput Nucleotide Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Virology",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Virology\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rabbits",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:26:30+00:00",
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
      "location": "vocabulary:60",
      "term": {
        "text": "\"Rabbits\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Metagenomics\"[MeSH Terms] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"shotgun sequencing\"[Title/Abstract]) AND (\"Viruses\"[MeSH Terms] OR \"Virology\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"virom*\"[Title/Abstract]) AND (\"animals, domestic\"[MeSH Terms] OR \"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm animal\"[Title/Abstract] OR \"farm animals\"[Title/Abstract] OR \"food animal\"[Title/Abstract] OR \"food animals\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"piglet\"[Title/Abstract] OR \"piglets\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"hog\"[Title/Abstract] OR \"hogs\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"hen\"[Title/Abstract] OR \"hens\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"duck\"[Title/Abstract] OR \"ducks\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"buffalo\"[Title/Abstract] OR \"camel\"[Title/Abstract] OR \"camels\"[Title/Abstract] OR \"Rabbits\"[MeSH Terms] OR \"rabbit*\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "504f5803bbfd75cc2a953b48a96249dbb1e5d2f22c77f8a62247e79fa7e8a910",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The query translation preserves the three concept blocks and their AND combination. The explicit singular and plural animal phrases avoid relying on phrase stemming."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within concepts and AND across methods, viruses, and farm animals match the stated searchable scope. Outcomes and applications are appropriately left for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified. The domestic-animal heading is broad, but that is consistent with screening out companion-animal-only records."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The method block relies on metagenom* and virom* as free-text terms; high-throughput sequencing is included only as a MeSH heading. The animal text-word list also omits some farmed species, including geese and rabbits, despite the broad farm-animal eligibility."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors or translation issues, and the field tags and Boolean structure are coherent."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive study or publication-date filters are applied. The entry-date cutoff is explicitly documented as the run's as-of boundary."
        }
      },
      "findings": [
        {
          "id": "R1-TW-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The method block has no title/abstract terms for sequencing approaches that may be reported without the words metagenomics or viromics. High-Throughput Nucleotide Sequencing is present only as a MeSH heading, so unindexed records using terms such as next-generation sequencing, high-throughput sequencing, or shotgun sequencing may be missed.",
          "recommendation": "Consider adding tested title/abstract expressions for relevant sequencing-method terminology, including next-generation and high-throughput sequencing and shotgun sequencing, while retaining the explicit metagenom* and virom* terms.",
          "status": "open"
        },
        {
          "id": "R1-TW-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The animal text-word list omits geese and rabbits, which can be farmed animals. The Poultry heading may retrieve indexed goose records, but it does not ensure coverage of unindexed records or records without that heading.",
          "recommendation": "If geese and rabbits fall within the intended farm-animal scope, add tested title/abstract terms for goose/geese and rabbit/rabbits. Confirm whether other farmed taxa are in scope and represent them or state their exclusion.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "ef3f5915bf629e1a54608a4ee65e2829d78ee1e81098e817fae553ddf08d2f65",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The query retains the three searched concepts and combines them with AND. The named method and animal terms appear in their own blocks; the explicit singular and plural animal phrases are retained."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within each concept and AND across methods, viruses, and farm animals match the stated searchable scope. Applications remain for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports no translation issues. The broad domestic-animal heading is consistent with screening out companion-animal-only studies; the species headings and text terms add coverage."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The method block now includes explicit next-generation, high-throughput, and shotgun sequencing phrases while retaining metagenom* and virom*. Goose/geese and rabbit terms have been added. The five retrieved known records are development records, so their retrieval does not establish independent validation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query has no syntax errors, translation issues, or warning-list entries. The phrase variants are explicitly quoted; the reported translation normalizes spacing and hyphenation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive study-design or publication-date filters are reported. The entry-date boundary is documented as the as-of date, 2019-02-22."
        }
      },
      "findings": [
        {
          "id": "R1-TW-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The method block lacked title/abstract terms for sequencing approaches that may be reported without the words metagenomics or viromics.",
          "recommendation": "Add tested title/abstract expressions for next-generation, high-throughput, and shotgun sequencing while retaining metagenom* and virom*.",
          "status": "resolved",
          "response": "The version 3 method block adds all three sequencing-method phrase variants and retains the earlier terms."
        },
        {
          "id": "R1-TW-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The animal text-word list omitted geese and rabbits, which may fall within the farm-animal scope.",
          "recommendation": "Add tested goose/geese and rabbit/rabbits terms if these taxa are in scope.",
          "status": "resolved",
          "response": "The version 3 farm-animal block adds goose, geese, rabbit*, and the Rabbits heading, with those taxa recorded as in scope under the user's proceed-with-assumptions instruction."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "ef3f5915bf629e1a54608a4ee65e2829d78ee1e81098e817fae553ddf08d2f65",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three searched concepts are represented in their own blocks and combined with AND. The method block retains metagenom* and virom*, and the animal block includes the previously requested goose/geese and rabbit terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within each concept and AND across methods, viruses, and farm animals match the stated search scope. Applications remain for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes the reported method, virus, domestic-animal, livestock, and species headings. The broad domestic-animal heading is consistent with screening out companion-animal-only studies."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The method block includes the previously requested next-generation, high-throughput, and shotgun sequencing phrases while retaining metagenom* and virom*. The animal block includes goose/geese and rabbit terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors, translation issues, or warning-list entries. The phrase variants are explicitly quoted and the reported translations normalize spacing and hyphenation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive study-design or publication-date filters are reported. The Entrez date boundary is documented as the run's as-of date, 2019-02-22."
        }
      },
      "findings": [
        {
          "id": "R1-TW-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The method block lacked title/abstract terms for sequencing approaches that may be reported without the words metagenomics or viromics.",
          "recommendation": "Add tested title/abstract expressions for next-generation, high-throughput, and shotgun sequencing while retaining metagenom* and virom*.",
          "status": "resolved",
          "response": "The version 3 method block adds the requested sequencing-method phrase variants and retains the earlier terms."
        },
        {
          "id": "R1-TW-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The animal text-word list omitted geese and rabbits, which may fall within the farm-animal scope.",
          "recommendation": "Add tested goose/geese and rabbit/rabbits terms if these taxa are in scope.",
          "status": "resolved",
          "response": "The version 3 farm-animal block adds goose, geese, rabbit*, and the Rabbits heading; the packet records these taxa as in scope."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


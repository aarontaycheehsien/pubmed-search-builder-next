# PubMed search strategy: audit

Generated 2026-09-30T15:46:04+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC (scoping-style topic map)
- Scope confirmed by user: no (User asked to proceed without questions; scope assumptions are provisional. Interpreted farm animals as domesticated agricultural livestock and poultry, with other farmed species eligible if clear from the record; aquatic farmed species are outside this provisional scope. No seeds supplied. No date, language, or geography limits; PubMed inclusion is bounded by Entrez date 2019-02-22 via as_of, not publication date.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viruses | search | The subject matter is explicitly viral; virus terminology and viral MeSH headings are searchable. |
| Metagenomics and viromics methods | search | The method defines the review topic and is generally named in titles, abstracts, or indexing. |
| Farm animals and livestock species | search | The population distinguishes this topic; a category block will include the group label and named member species. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T15:44:17+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 5,789
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Viruses[Mesh]` | 759,255 | none |
| 2 | `"DNA Viruses"[Mesh]` | 273,794 | none |
| 3 | `"RNA Viruses"[Mesh]` | 440,928 | none |
| 4 | `virus[tiab]` | 635,595 | none |
| 5 | `viruses[tiab]` | 155,778 | none |
| 6 | `viral[tiab]` | 333,289 | none |
| 7 | `virome*[tiab]` | 780 | none |
| 8 | `phage*[tiab]` | 48,158 | none |
| 9 | `bacteriophage*[tiab]` | 34,910 | none |
| 10 | `"RNA, Viral"[Mesh]` | 76,473 | none |
| 11 | `"DNA, Viral"[Mesh]` | 87,180 | none |
| 12 | `"Genome, Viral"[Mesh]` | 58,113 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 1,098,749 | none |
| 14 | `Metagenomics[Mesh]` | 5,229 | none |
| 15 | `Metagenome[Mesh]` | 5,897 | none |
| 16 | `Genomics[Mesh]` | 105,464 | none |
| 17 | `metagenom*[tiab]` | 11,213 | none |
| 18 | `virom*[tiab]` | 824 | none |
| 19 | `metatranscriptom*[tiab]` | 995 | none |
| 20 | `NGS[tiab]` | 9,104 | none |
| 21 | `HTS[tiab]` | 5,029 | none |
| 22 | `"next-generation sequencing"[tiab]` | 26,834 | none |
| 23 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 24 | `"high-throughput sequencing"[tiab]` | 10,541 | none |
| 25 | `"shotgun sequencing"[tiab]` | 1,193 | none |
| 26 | `"deep sequencing"[tiab]` | 6,483 | none |
| 27 | `"sequence-independent amplification"[tiab]` | 65 | none |
| 28 | `unbiased[tiab]` | 19,721 | none |
| 29 | `metavirom*[tiab]` | 45 | none |
| 30 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 31 | `"Sequence Analysis, DNA"[Mesh]` | 222,713 | none |
| 32 | `#14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31` | 387,263 | none |
| 33 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 34 | `Livestock[Mesh]` | 3,200 | none |
| 35 | `Poultry[Mesh]` | 147,415 | none |
| 36 | `Cattle[Mesh]` | 341,776 | none |
| 37 | `Swine[Mesh]` | 214,731 | none |
| 38 | `Sheep[Mesh]` | 116,801 | none |
| 39 | `Goats[Mesh]` | 30,623 | none |
| 40 | `Chickens[Mesh]` | 117,975 | none |
| 41 | `Ducks[Mesh]` | 10,534 | none |
| 42 | `Geese[Mesh]` | 2,682 | none |
| 43 | `Turkeys[Mesh]` | 10,103 | none |
| 44 | `Horses[Mesh]` | 67,676 | none |
| 45 | `livestock[tiab]` | 21,337 | none |
| 46 | `poultry[tiab]` | 25,731 | none |
| 47 | `"farm animal"[tiab]` | 833 | none |
| 48 | `"farm animals"[tiab]` | 3,038 | none |
| 49 | `"production animal"[tiab]` | 126 | none |
| 50 | `"production animals"[tiab]` | 294 | none |
| 51 | `"domestic animal"[tiab]` | 1,137 | none |
| 52 | `"domestic animals"[tiab]` | 7,245 | none |
| 53 | `cattle[tiab]` | 79,355 | none |
| 54 | `bovine[tiab]` | 189,144 | none |
| 55 | `cow[tiab]` | 29,456 | none |
| 56 | `cows[tiab]` | 45,341 | none |
| 57 | `swine[tiab]` | 42,358 | none |
| 58 | `pig[tiab]` | 127,282 | none |
| 59 | `pigs[tiab]` | 115,325 | none |
| 60 | `porcine[tiab]` | 79,145 | none |
| 61 | `sheep[tiab]` | 87,044 | none |
| 62 | `ovine[tiab]` | 20,361 | none |
| 63 | `goat*[tiab]` | 31,547 | none |
| 64 | `caprine[tiab]` | 3,127 | none |
| 65 | `chicken*[tiab]` | 92,941 | none |
| 66 | `avian[tiab]` | 50,972 | none |
| 67 | `turkey[tiab]` | 32,530 | none |
| 68 | `turkeys[tiab]` | 5,917 | none |
| 69 | `duck*[tiab]` | 13,075 | none |
| 70 | `geese[tiab]` | 1,928 | none |
| 71 | `goose[tiab]` | 2,645 | none |
| 72 | `horse*[tiab]` | 80,001 | none |
| 73 | `equine[tiab]` | 28,778 | none |
| 74 | `yak[tiab]` | 730 | none |
| 75 | `yaks[tiab]` | 398 | none |
| 76 | `camel*[tiab]` | 9,598 | none |
| 77 | `buffalo[tiab]` | 9,137 | none |
| 78 | `rabbit*[tiab]` | 252,771 | none |
| 79 | `#33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78` | 1,452,784 | none |
| 80 | `#13 AND #32 AND #79` | 5,789 | none |

### Strategy (single line, for copying into PubMed)

```text
((Viruses[Mesh] OR "DNA Viruses"[Mesh] OR "RNA Viruses"[Mesh] OR virus[tiab] OR viruses[tiab] OR viral[tiab] OR virome*[tiab] OR phage*[tiab] OR bacteriophage*[tiab] OR "RNA, Viral"[Mesh] OR "DNA, Viral"[Mesh] OR "Genome, Viral"[Mesh]) AND (Metagenomics[Mesh] OR Metagenome[Mesh] OR Genomics[Mesh] OR metagenom*[tiab] OR virom*[tiab] OR metatranscriptom*[tiab] OR NGS[tiab] OR HTS[tiab] OR "next-generation sequencing"[tiab] OR "next generation sequencing"[tiab] OR "high-throughput sequencing"[tiab] OR "shotgun sequencing"[tiab] OR "deep sequencing"[tiab] OR "sequence-independent amplification"[tiab] OR unbiased[tiab] OR metavirom*[tiab] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR "Sequence Analysis, DNA"[Mesh]) AND ("Animals, Domestic"[Mesh] OR Livestock[Mesh] OR Poultry[Mesh] OR Cattle[Mesh] OR Swine[Mesh] OR Sheep[Mesh] OR Goats[Mesh] OR Chickens[Mesh] OR Ducks[Mesh] OR Geese[Mesh] OR Turkeys[Mesh] OR Horses[Mesh] OR livestock[tiab] OR poultry[tiab] OR "farm animal"[tiab] OR "farm animals"[tiab] OR "production animal"[tiab] OR "production animals"[tiab] OR "domestic animal"[tiab] OR "domestic animals"[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR sheep[tiab] OR ovine[tiab] OR goat*[tiab] OR caprine[tiab] OR chicken*[tiab] OR avian[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck*[tiab] OR geese[tiab] OR goose[tiab] OR horse*[tiab] OR equine[tiab] OR yak[tiab] OR yaks[tiab] OR camel*[tiab] OR buffalo[tiab] OR rabbit*[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 21 | 21 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virus | 24,910 | 0 |
| metagenomics | 128,351 | 0 |
| farm_animals | 36,342 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 22,918 | initial | none | Initial recall-first draft with separate virus, sequencing/metagenomics, and terrestrial farm-animal blocks; includes MeSH category and named species because farm animals are a category. Vocabulary informed by the 21 screened pilot discoveries. |
| 2 | 1,340 | metagenomics: +0 / -1 | none | Removed broad standalone sequenc*[tiab] after its line count exceeded one million and expanded the final set beyond workload budget; retained metagenomics, viromics, named sequencing approaches and sequencing acronyms. |
| 3 | 5,789 | virus: +3 / -0; metagenomics: +3 / -0 | none | Added metavirom* per internal review and added viral-genome/DNA/RNA and sequencing MeSH headings ranked from the screened relevant set; these are topic/method headings rather than specific pathogen filters. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; PRESS-R1-001 should-fix resolved, PRESS-R1-002 must-fix accepted-risk
- Round 2 on version 3: 2 findings; PRESS-R1-001 should-fix resolved, PRESS-R1-002 must-fix accepted-risk
- Round 3 on version 3: 2 findings; PRESS-R1-001 should-fix resolved, PRESS-R1-002 must-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1692 NCBI requests logged (3 from cache); strategy sha256 b4d5a3b49044._

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
      "checked_at": "2026-09-30T15:44:17+00:00",
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
        "text": "Viruses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "DNA Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004267",
          "name": "DNA Viruses",
          "type": "descriptor",
          "scope_note": "Viruses whose nucleic acid is DNA.",
          "tree_numbers": [
            "B04.280"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004267",
      "preferred_label": "DNA Viruses",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"DNA Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "RNA Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012328",
          "name": "RNA Viruses",
          "type": "descriptor",
          "scope_note": "Viruses whose genetic material is RNA.",
          "tree_numbers": [
            "B04.820"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012328",
      "preferred_label": "RNA Viruses",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"RNA Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "RNA, Viral",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012367",
          "name": "RNA, Viral",
          "type": "descriptor",
          "scope_note": "Ribonucleic acid that makes up the genetic material of viruses.",
          "tree_numbers": [
            "D13.444.735.828"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012367",
      "preferred_label": "RNA, Viral",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"RNA, Viral\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "DNA, Viral",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004279",
          "name": "DNA, Viral",
          "type": "descriptor",
          "scope_note": "Deoxyribonucleic acid that makes up the genetic material of viruses.",
          "tree_numbers": [
            "D13.444.308.568"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004279",
      "preferred_label": "DNA, Viral",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"DNA, Viral\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Genome, Viral",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016679",
          "name": "Genome, Viral",
          "type": "descriptor",
          "scope_note": "The complete genetic complement contained in a DNA or RNA molecule in a virus.",
          "tree_numbers": [
            "G05.360.340.358.840"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016679",
      "preferred_label": "Genome, Viral",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Genome, Viral\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Metagenomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "Metagenomics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Metagenome",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Metagenome",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Genomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "Genomics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"High-Throughput Nucleotide Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sequence Analysis, DNA",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017422",
          "name": "Sequence Analysis, DNA",
          "type": "descriptor",
          "scope_note": "A multistage process that includes cloning, physical mapping, subcloning, determination of the DNA SEQUENCE, and information analysis.",
          "tree_numbers": [
            "E05.393.760.700"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017422",
      "preferred_label": "Sequence Analysis, DNA",
      "type": "descriptor",
      "location": "vocabulary:30",
      "term": {
        "text": "\"Sequence Analysis, DNA\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Livestock",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Poultry",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "Cattle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Swine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Sheep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Goats",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chickens",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Chickens",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ducks",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Ducks",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Geese",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "Geese",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Turkeys",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "Turkeys",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:44:17+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "Horses",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"viruses\"[MeSH Terms] OR \"DNA Viruses\"[MeSH Terms] OR \"RNA Viruses\"[MeSH Terms] OR \"virus\"[Title/Abstract] OR \"viruses\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virome*\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"bacteriophage*\"[Title/Abstract] OR \"rna, viral\"[MeSH Terms] OR \"dna, viral\"[MeSH Terms] OR \"genome, viral\"[MeSH Terms]) AND (\"metagenomics\"[MeSH Terms] OR \"metagenome\"[MeSH Terms] OR \"genomics\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"metatranscriptom*\"[Title/Abstract] OR \"NGS\"[Title/Abstract] OR \"HTS\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"shotgun sequencing\"[Title/Abstract] OR \"deep sequencing\"[Title/Abstract] OR \"sequence-independent amplification\"[Title/Abstract] OR \"unbiased\"[Title/Abstract] OR \"metavirom*\"[Title/Abstract] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"sequence analysis, dna\"[MeSH Terms]) AND (\"animals, domestic\"[MeSH Terms] OR \"livestock\"[MeSH Terms] OR \"poultry\"[MeSH Terms] OR \"cattle\"[MeSH Terms] OR \"swine\"[MeSH Terms] OR (\"sheep, domestic\"[MeSH Terms] OR \"sheep\"[MeSH Terms]) OR \"goats\"[MeSH Terms] OR \"chickens\"[MeSH Terms] OR \"ducks\"[MeSH Terms] OR \"geese\"[MeSH Terms] OR \"turkeys\"[MeSH Terms] OR \"horses\"[MeSH Terms] OR \"livestock\"[Title/Abstract] OR \"poultry\"[Title/Abstract] OR \"farm animal\"[Title/Abstract] OR \"farm animals\"[Title/Abstract] OR \"production animal\"[Title/Abstract] OR \"production animals\"[Title/Abstract] OR \"domestic animal\"[Title/Abstract] OR \"domestic animals\"[Title/Abstract] OR \"cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"avian\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"yak\"[Title/Abstract] OR \"yaks\"[Title/Abstract] OR \"camel*\"[Title/Abstract] OR \"buffalo\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "bcd6c125b8b220b6747d12caac9e270a3883095332fbddf193307abe78572369",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The listed eligibility species have corresponding title/abstract terms in the farm-animal block, including bare species names or tested wildcard forms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are combined with AND, and their synonyms with OR; this matches the stated searchable concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied MeSH headings are reported as verified, and the animal headings cover the named livestock and poultry groups. Genomics is broad, but its use in the combined strategy is not a technical error."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Consider adding metavirom*[tiab] as an explicit method synonym; the existing virom* term does not begin with that form. Re-evaluate the complete strategy after adding it."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translations show no syntax errors or warnings, and the final Boolean expression is well formed."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The protocol's as_of date imposes the required Entrez-date cutoff; no publication-date [dp] limit is used."
        }
      },
      "findings": [
        {
          "id": "PRESS-R1-001",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The method block includes virom*[tiab] but not metavirom*[tiab]. The latter is a distinct term form that may occur in records describing metaviromics or a metavirome.",
          "recommendation": "Test and consider adding metavirom*[tiab], then rerun the complete search evaluation.",
          "status": "resolved",
          "response": "Added metavirom*[tiab] and re-evaluated the complete strategy as version 3. All 21 screened development records remained retrieved; the strategy returned 5,789 records and had no validation blockers or review-required items."
        },
        {
          "id": "PRESS-R1-002",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies 1800/01/01 through 2019/02/22 on Entry Date. The protocol says there are no date limits, while its note confirms this cutoff bounds inclusion; records entered after that date are excluded.",
          "recommendation": "Remove the Entry Date ceiling unless a 2019-02-22 cutoff is part of the confirmed review scope. Rebuild and fully re-evaluate the query after the change.",
          "status": "accepted-risk",
          "response": "Retained the 2019-02-22 Entry Date ceiling because the user's harness explicitly requires PubMed to be simulated as of that date and requires PSB_AS_OF on every command. The protocol records this as as_of, an Entrez-date inventory bound, not a publication-date [dp] search limit; no [dp] clause is present. Removing it would violate the user's explicit instructions."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "595d73fe3aaeb06b65b2a12aee8030bd41c012b01e33d3607b1b3eb6643267f9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named livestock and poultry species have their own title/abstract terms in the farm-animal block, including bare names or tested wildcard forms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three searchable concepts are combined with AND, and synonyms within each concept are combined with OR, matching the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the supplied MeSH headings as verified. The animal headings cover the named livestock and poultry groups; broader headings are acceptable within this recall-oriented strategy."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised method block includes metavirom*[tiab]. The virus, method, and animal blocks include relevant free-text terms, and the development records remain retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translations show no syntax errors or warnings, and the final Boolean expression is well formed."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2019-02-22 Entry Date ceiling is retained as the explicitly documented PubMed as-of inventory bound; there is no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "PRESS-R1-001",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The method block initially lacked metavirom*[tiab], a distinct term form from virom*[tiab].",
          "recommendation": "Add and test metavirom*[tiab], then rerun the complete search evaluation.",
          "status": "resolved",
          "response": "Added metavirom*[tiab] and re-evaluated the complete strategy as version 3. All 21 screened development records remain retrieved."
        },
        {
          "id": "PRESS-R1-002",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entry Date ceiling of 2019-02-22, although the protocol says there are no date limits.",
          "recommendation": "Remove the ceiling unless the cutoff is part of the confirmed review scope, then rebuild and fully re-evaluate the query.",
          "status": "accepted-risk",
          "response": "Retained as the user's required PubMed as-of inventory bound, documented in the protocol. It is an Entry Date cutoff, not a publication-date search limit; no [dp] clause is present."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "595d73fe3aaeb06b65b2a12aee8030bd41c012b01e33d3607b1b3eb6643267f9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named livestock and poultry species have their own title/abstract terms in the farm-animal block, including bare names or tested wildcard forms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three searchable concepts are combined with AND, and synonyms within each concept with OR, matching the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the supplied MeSH headings as verified. Animal headings cover the named livestock and poultry groups."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised method block includes metavirom*[tiab], and the packet reports that all 21 development records remain retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translations show no syntax errors or warnings, and the final Boolean expression is well formed."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2019-02-22 Entry Date ceiling is documented as the required PubMed as-of inventory bound; no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "PRESS-R1-001",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The initial method block lacked metavirom*[tiab], a distinct term form from virom*[tiab].",
          "recommendation": "Add and test metavirom*[tiab], then rerun the complete search evaluation.",
          "status": "resolved",
          "response": "Added metavirom*[tiab] and reevaluated the complete strategy as version 3. All 21 development records remain retrieved."
        },
        {
          "id": "PRESS-R1-002",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entry Date ceiling of 2019-02-22, although the protocol says there are no date limits.",
          "recommendation": "Remove the ceiling unless the cutoff is part of the confirmed review scope, then rebuild and fully reevaluate the query.",
          "status": "accepted-risk",
          "response": "Retained as the user's required PubMed as-of inventory bound and documented in the protocol. It is an Entry Date cutoff, not a publication-date search limit; no [dp] clause is present."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


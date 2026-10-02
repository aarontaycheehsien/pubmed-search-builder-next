# PubMed search strategy: audit

Generated 2026-10-02T14:11:37+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: no (User supplied no known relevant articles and cannot answer during the run; scope is unconfirmed. Broad PCC assumption: viruses/viral communities AND metagenomics/sequencing AND farmed animals. Includes terrestrial livestock, poultry, horses, and farmed aquatic animals; excludes companion animals, wildlife, environmental-only studies, and non-metagenomic single-target testing at screening. No language, publication-date, design, or other limits. PubMed is bounded by Entrez date with PSB_AS_OF=2019-02-22 on every command; no [dp] limit. Screened two pilot samples (review-focused query and topic query) and abstracts for candidate primary records; no matching systematic review was identified in the review-focused sample. Ten primary records were screened in and split into 7 development records and 3 held-out validation records before term mining. A non-systematic review was used only for discovery; no external benchmark set was assembled. Candidate discovery is limited to the searches and samples recorded in this workspace.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viruses and viral communities | search | The review concerns viruses; virus/viral/virome terminology is central and searchable. |
| Metagenomics and viral metagenomic methods | search | Metagenomics defines the method/topic and is expected to be named in eligible records. |
| Farmed animals | search | The population is explicit in the question; include terrestrial livestock, poultry, and farmed aquatic animals, with species screened for eligibility. |
| Specimen and sample types | screen | Samples vary and may not be named consistently in titles or abstracts. |
| Study design and outcomes | screen | No design or outcome restriction was specified. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:09:35+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 8,299
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Viruses[Mesh]` | 759,255 | none |
| 2 | `Genome, Viral[Mesh]` | 58,113 | none |
| 3 | `RNA, Viral[Mesh]` | 76,473 | none |
| 4 | `virus*[tiab]` | 687,408 | none |
| 5 | `viral[tiab]` | 333,289 | none |
| 6 | `virolog*[tiab]` | 36,884 | none |
| 7 | `virome*[tiab]` | 780 | none |
| 8 | `phage*[tiab]` | 48,158 | none |
| 9 | `bacteriophage*[tiab]` | 34,910 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 1,101,684 | none |
| 11 | `Metagenomics[Mesh]` | 5,229 | none |
| 12 | `High-Throughput Nucleotide Sequencing[Mesh]` | 28,190 | none |
| 13 | `Genomics[Mesh]` | 105,464 | none |
| 14 | `metagenom*[tiab]` | 11,213 | none |
| 15 | `meta-genom*[tiab]` | 186 | none |
| 16 | `shotgun sequenc*[tiab]` | 1,538 | none |
| 17 | `high-throughput sequenc*[tiab]` | 10,786 | none |
| 18 | `high throughput sequenc*[tiab]` | 10,786 | none |
| 19 | `next-generation sequenc*[tiab]` | 27,343 | none |
| 20 | `next generation sequenc*[tiab]` | 27,343 | none |
| 21 | `deep sequenc*[tiab]` | 6,739 | none |
| 22 | `massively parallel sequenc*[tiab]` | 1,761 | none |
| 23 | `sequence-independent[tiab]` | 1,107 | none |
| 24 | `unbiased sequenc*[tiab]` | 51 | none |
| 25 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 162,024 | none |
| 26 | `Animals[Mesh]` | 22,808,303 | none |
| 27 | `Animal Husbandry[Mesh]` | 20,395 | none |
| 28 | `Livestock[Mesh]` | 3,200 | none |
| 29 | `Poultry[Mesh]` | 147,415 | none |
| 30 | `Aquaculture[Mesh]` | 12,633 | none |
| 31 | `Crustacea[Mesh]` | 41,727 | none |
| 32 | `Mollusca[Mesh]` | 58,139 | none |
| 33 | `Shellfish[Mesh]` | 4,446 | none |
| 34 | `Cattle[Mesh]` | 341,776 | none |
| 35 | `Swine[Mesh]` | 214,731 | none |
| 36 | `Sheep[Mesh]` | 116,801 | none |
| 37 | `Goats[Mesh]` | 30,623 | none |
| 38 | `Horses[Mesh]` | 67,676 | none |
| 39 | `Chickens[Mesh]` | 117,975 | none |
| 40 | `farm animal*[tiab]` | 3,666 | none |
| 41 | `farmed animal*[tiab]` | 195 | none |
| 42 | `livestock[tiab]` | 21,337 | none |
| 43 | `domestic animal*[tiab]` | 8,110 | none |
| 44 | `domesticated animal*[tiab]` | 735 | none |
| 45 | `animal husbandry[tiab]` | 1,735 | none |
| 46 | `cattle[tiab]` | 79,355 | none |
| 47 | `bovine[tiab]` | 189,144 | none |
| 48 | `cow[tiab]` | 29,456 | none |
| 49 | `cows[tiab]` | 45,341 | none |
| 50 | `calf[tiab]` | 43,460 | none |
| 51 | `calves[tiab]` | 24,854 | none |
| 52 | `beef[tiab]` | 24,718 | none |
| 53 | `dairy[tiab]` | 48,419 | none |
| 54 | `swine[tiab]` | 42,358 | none |
| 55 | `porcine[tiab]` | 79,145 | none |
| 56 | `pig[tiab]` | 127,282 | none |
| 57 | `pigs[tiab]` | 115,325 | none |
| 58 | `piglet*[tiab]` | 17,109 | none |
| 59 | `sheep[tiab]` | 87,044 | none |
| 60 | `ovine[tiab]` | 20,361 | none |
| 61 | `lamb[tiab]` | 9,836 | none |
| 62 | `lambs[tiab]` | 14,624 | none |
| 63 | `goat*[tiab]` | 31,547 | none |
| 64 | `caprine[tiab]` | 3,127 | none |
| 65 | `horse*[tiab]` | 80,001 | none |
| 66 | `equine[tiab]` | 28,778 | none |
| 67 | `poultry[tiab]` | 25,731 | none |
| 68 | `chicken*[tiab]` | 92,941 | none |
| 69 | `broiler*[tiab]` | 16,896 | none |
| 70 | `turkey[tiab]` | 32,530 | none |
| 71 | `turkeys[tiab]` | 5,917 | none |
| 72 | `duck*[tiab]` | 13,075 | none |
| 73 | `goose[tiab]` | 2,645 | none |
| 74 | `geese[tiab]` | 1,928 | none |
| 75 | `fowl[tiab]` | 6,948 | none |
| 76 | `aquaculture[tiab]` | 9,036 | none |
| 77 | `fish farm*[tiab]` | 1,587 | none |
| 78 | `farmed fish[tiab]` | 733 | none |
| 79 | `eel[tiab]` | 4,638 | none |
| 80 | `eels[tiab]` | 3,179 | none |
| 81 | `salmon[tiab]` | 14,743 | none |
| 82 | `trout[tiab]` | 15,264 | none |
| 83 | `carp[tiab]` | 9,326 | none |
| 84 | `tilapia[tiab]` | 4,036 | none |
| 85 | `crustacean*[tiab]` | 9,623 | none |
| 86 | `shellfish[tiab]` | 5,993 | none |
| 87 | `mollusc*[tiab]` | 13,916 | none |
| 88 | `mollusk*[tiab]` | 4,193 | none |
| 89 | `shrimp[tiab]` | 9,789 | none |
| 90 | `shrimps[tiab]` | 1,687 | none |
| 91 | `prawn*[tiab]` | 1,678 | none |
| 92 | `oyster*[tiab]` | 7,043 | none |
| 93 | `mussel*[tiab]` | 9,019 | none |
| 94 | `clam*[tiab]` | 91,171 | none |
| 95 | `scallop*[tiab]` | 3,302 | none |
| 96 | `crab*[tiab]` | 11,898 | none |
| 97 | `lobster*[tiab]` | 3,405 | none |
| 98 | `abalone*[tiab]` | 1,018 | none |
| 99 | `#26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96 OR #97 OR #98` | 22,923,691 | none |
| 100 | `#10 AND #25 AND #99` | 8,299 | none |

### Strategy (single line, for copying into PubMed)

```text
((Viruses[Mesh] OR Genome, Viral[Mesh] OR RNA, Viral[Mesh] OR virus*[tiab] OR viral[tiab] OR virolog*[tiab] OR virome*[tiab] OR phage*[tiab] OR bacteriophage*[tiab]) AND (Metagenomics[Mesh] OR High-Throughput Nucleotide Sequencing[Mesh] OR Genomics[Mesh] OR metagenom*[tiab] OR meta-genom*[tiab] OR shotgun sequenc*[tiab] OR high-throughput sequenc*[tiab] OR high throughput sequenc*[tiab] OR next-generation sequenc*[tiab] OR next generation sequenc*[tiab] OR deep sequenc*[tiab] OR massively parallel sequenc*[tiab] OR sequence-independent[tiab] OR unbiased sequenc*[tiab]) AND (Animals[Mesh] OR Animal Husbandry[Mesh] OR Livestock[Mesh] OR Poultry[Mesh] OR Aquaculture[Mesh] OR Crustacea[Mesh] OR Mollusca[Mesh] OR Shellfish[Mesh] OR Cattle[Mesh] OR Swine[Mesh] OR Sheep[Mesh] OR Goats[Mesh] OR Horses[Mesh] OR Chickens[Mesh] OR farm animal*[tiab] OR farmed animal*[tiab] OR livestock[tiab] OR domestic animal*[tiab] OR domesticated animal*[tiab] OR animal husbandry[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR beef[tiab] OR dairy[tiab] OR swine[tiab] OR porcine[tiab] OR pig[tiab] OR pigs[tiab] OR piglet*[tiab] OR sheep[tiab] OR ovine[tiab] OR lamb[tiab] OR lambs[tiab] OR goat*[tiab] OR caprine[tiab] OR horse*[tiab] OR equine[tiab] OR poultry[tiab] OR chicken*[tiab] OR broiler*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck*[tiab] OR goose[tiab] OR geese[tiab] OR fowl[tiab] OR aquaculture[tiab] OR fish farm*[tiab] OR farmed fish[tiab] OR eel[tiab] OR eels[tiab] OR salmon[tiab] OR trout[tiab] OR carp[tiab] OR tilapia[tiab] OR crustacean*[tiab] OR shellfish[tiab] OR mollusc*[tiab] OR mollusk*[tiab] OR shrimp[tiab] OR shrimps[tiab] OR prawn*[tiab] OR oyster*[tiab] OR mussel*[tiab] OR clam*[tiab] OR scallop*[tiab] OR crab*[tiab] OR lobster*[tiab] OR abalone*[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virus | 115,809 | 0 |
| metagenomics | 920,434 | 0 |
| farm_animals | 11,531 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 8,250 | initial | none | First three-block draft, broad recall-first vocabulary. |
| 2 | 8,299 | virus: +2 / -0; farm_animals: +17 / -0 | none | Revision after critic: added crustacean and mollusc/shellfish population vocabulary, plus viral genome and viral RNA MeSH headings mined from development records. Retained the required Entrez-date snapshot bound as_of=2019-02-22; it is not a publication-date [dp] limit. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 2 findings; F1 should-fix open, F2 must-fix open
- Round 2 on version 2: 2 findings; F1 should-fix resolved, F2 must-fix rejected
- Round 3 on version 2: 2 findings; F1 should-fix resolved, F2 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 924 NCBI requests logged (318 from cache); strategy sha256 3ac190a77e43._

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
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "requested": "Genome, Viral",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Genome, Viral",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "RNA, Viral",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "RNA, Viral",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Metagenomics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "Metagenomics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "High-Throughput Nucleotide Sequencing",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Genomics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "Genomics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000818",
          "name": "Animals",
          "type": "descriptor",
          "scope_note": "Unicellular or multicellular, heterotrophic organisms, that have sensation and the power of voluntary movement. Under the older five kingdom paradigm, Animalia was one of the kingdoms. Under the modern three domain model, Animalia represents one of the many groups in the domain EUKARYOTA.",
          "tree_numbers": [
            "B01.050"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000818",
      "preferred_label": "Animals",
      "type": "descriptor",
      "location": "vocabulary:24",
      "term": {
        "text": "Animals",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animal Husbandry",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Animal Husbandry",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "Livestock",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "Poultry",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Aquaculture",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Aquaculture",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Crustacea",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Crustacea",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mollusca",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Mollusca",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Shellfish",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012758",
          "name": "Shellfish",
          "type": "descriptor",
          "scope_note": "Aquatic invertebrates belonging to the phylum MOLLUSCA or the subphylum CRUSTACEA, and used as food.",
          "tree_numbers": [
            "G07.203.300.600.875.700",
            "J02.500.600.875.700"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012758",
      "preferred_label": "Shellfish",
      "type": "descriptor",
      "location": "vocabulary:31",
      "term": {
        "text": "Shellfish",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Cattle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "Swine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "Sheep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Goats",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Horses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chickens",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:09:35+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Chickens",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"viruses\"[MeSH Terms] OR \"genome, viral\"[MeSH Terms] OR \"rna, viral\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virolog*\"[Title/Abstract] OR \"virome*\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"bacteriophage*\"[Title/Abstract]) AND (\"metagenomics\"[MeSH Terms] OR \"high throughput nucleotide sequencing\"[MeSH Terms] OR \"genomics\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"meta genom*\"[Title/Abstract] OR \"shotgun sequenc*\"[Title/Abstract] OR \"high throughput sequenc*\"[Title/Abstract] OR \"high throughput sequenc*\"[Title/Abstract] OR \"next generation sequenc*\"[Title/Abstract] OR \"next generation sequenc*\"[Title/Abstract] OR \"deep sequenc*\"[Title/Abstract] OR \"massively parallel sequenc*\"[Title/Abstract] OR \"sequence-independent\"[Title/Abstract] OR \"unbiased sequenc*\"[Title/Abstract]) AND (\"animals\"[MeSH Terms] OR \"animal husbandry\"[MeSH Terms] OR \"livestock\"[MeSH Terms] OR \"poultry\"[MeSH Terms] OR \"aquaculture\"[MeSH Terms] OR \"crustacea\"[MeSH Terms] OR \"mollusca\"[MeSH Terms] OR \"shellfish\"[MeSH Terms] OR \"cattle\"[MeSH Terms] OR \"swine\"[MeSH Terms] OR (\"sheep, domestic\"[MeSH Terms] OR \"sheep\"[MeSH Terms]) OR \"goats\"[MeSH Terms] OR \"horses\"[MeSH Terms] OR \"chickens\"[MeSH Terms] OR \"farm animal*\"[Title/Abstract] OR \"farmed animal*\"[Title/Abstract] OR \"livestock\"[Title/Abstract] OR \"domestic animal*\"[Title/Abstract] OR \"domesticated animal*\"[Title/Abstract] OR \"animal husbandry\"[Title/Abstract] OR \"cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"beef\"[Title/Abstract] OR \"dairy\"[Title/Abstract] OR \"swine\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"piglet*\"[Title/Abstract] OR \"sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"lamb\"[Title/Abstract] OR \"lambs\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"poultry\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"fowl\"[Title/Abstract] OR \"aquaculture\"[Title/Abstract] OR \"fish farm*\"[Title/Abstract] OR \"farmed fish\"[Title/Abstract] OR \"eel\"[Title/Abstract] OR \"eels\"[Title/Abstract] OR \"salmon\"[Title/Abstract] OR \"trout\"[Title/Abstract] OR \"carp\"[Title/Abstract] OR \"tilapia\"[Title/Abstract] OR \"crustacean*\"[Title/Abstract] OR \"shellfish\"[Title/Abstract] OR \"mollusc*\"[Title/Abstract] OR \"mollusk*\"[Title/Abstract] OR \"shrimp\"[Title/Abstract] OR \"shrimps\"[Title/Abstract] OR \"prawn*\"[Title/Abstract] OR \"oyster*\"[Title/Abstract] OR \"mussel*\"[Title/Abstract] OR \"clam*\"[Title/Abstract] OR \"scallop*\"[Title/Abstract] OR \"crab*\"[Title/Abstract] OR \"lobster*\"[Title/Abstract] OR \"abalone*\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "167fa1b01f93394463b150a758183d8ecace6563d64856b694f3b7ef9236b75a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three blocks reflect the stated searchable concepts, and specimen types and study design remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The terms are ORed within concept blocks and the three blocks are ANDed, matching the documented scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied MeSH headings are verified and translate as intended. Broad headings such as Animals and Genomics favor recall, with a likely precision cost."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The farmed aquatic animal vocabulary is fish-centered. The scope includes farmed aquatic animals broadly, but the text words do not name other potentially eligible groups such as shrimp, prawns, or shellfish."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied terms and Boolean combination have no reported syntax errors, translation issues, or lint findings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The evaluated query applies an Entrez-date upper bound of 2019-02-22 even though the protocol says there is no publication-date limit. Remove the snapshot bound for the unrestricted review search and rerun the evaluation."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The farmed aquatic animals block has aquaculture and fish-related terms, but no text words for other farmed aquatic animal groups. Eligible records about shrimp, prawns, or shellfish may not mention aquaculture or farm/farmed fish in the title or abstract.",
          "recommendation": "Add appropriate names and spelling variants for the aquatic animal groups within the confirmed eligibility scope, then evaluate the revised strategy against relevant records.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluated query is bounded by 2019-02-22 [edat], while the protocol specifies no publication-date limit. As written, it excludes records entered after that date.",
          "recommendation": "Remove the historical Entrez-date bound from the review search and rerun the full evaluation without a date limit.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "3bb2d1b68e9221153edae04782770ecea065e32b111bb7cbbe444cf55ae3750f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three searched concepts match the stated scope; specimen types and study design remain screening criteria. Farmed aquatic animals are explicitly included."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each concept block, and the virus, metagenomics, and farm-animal blocks are ANDed, matching the documented scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied MeSH headings are verified and translate as intended. Broad headings such as Animals and Genomics may reduce precision, but support recall."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revision adds text words for crustaceans, shellfish, and mollusks, including shrimp, prawns, and multiple shellfish taxa, addressing the aquatic-vocabulary gap. No phrase warnings are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors, translation issues, lint findings, or PubMed warning lists."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No review filters or publication-date limits are applied. The only date bound is the required Entrez snapshot as_of=2019-02-22, represented as [edat] in the evaluated query; the strategy includes no [dp] restriction."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The farmed aquatic-animal vocabulary previously omitted text words for groups such as shrimp, prawns, and shellfish.",
          "recommendation": "Add appropriate names and spelling variants for aquatic animal groups within the confirmed eligibility scope, then evaluate the revised strategy against relevant records.",
          "status": "resolved",
          "response": "The revision adds Crustacea, Mollusca, and Shellfish headings and text words for crustaceans, shellfish, mollusks, shrimp, prawns, and other aquatic taxa. The evaluation reports no known records lost and all 10 known records retrieved."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query still applies an Entrez-date range ending 2019-02-22, despite the protocol specifying no date limit. The snapshot bound excludes records entered after that date; remove it from the review search and rerun the full evaluation.",
          "recommendation": "Remove the historical Entrez-date bound from the review search and rerun the full evaluation without a date limit.",
          "status": "rejected",
          "response": "The finding conflates a publication-date limit with the user-required database snapshot. The harness explicitly requires PSB_AS_OF=2019-02-22 on every command and prohibits post-cutoff PubMed literature; protocol.as_of records that snapshot. The evaluated translation shows an [edat] bound ending 2019/02/22 and contains no [dp] clause. Removing [edat] would violate the requested snapshot, so this finding is rejected."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "3bb2d1b68e9221153edae04782770ecea065e32b111bb7cbbe444cf55ae3750f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The virus, metagenomics, and farmed-animal blocks match the stated searchable concepts; sample types and study design remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The terms are ORed within each concept block and the three blocks are ANDed, consistent with the documented scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports that the headings translate as intended. Broad headings may affect precision, while supporting recall."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised strategy includes text words for crustaceans, shellfish, mollusks, shrimp, prawns, and other aquatic taxa. All 10 known records were retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors, translation issues, or lint findings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The [edat] bound represents the required 2019-02-22 database snapshot; the translated strategy has no publication-date [dp] restriction."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier farmed aquatic-animal vocabulary omitted text words for groups such as shrimp, prawns, and shellfish.",
          "recommendation": "Add names and spelling variants for aquatic animal groups within the eligibility scope and evaluate the revised strategy.",
          "status": "resolved",
          "response": "The current strategy adds Crustacea, Mollusca, and Shellfish headings, plus text words for crustaceans, shellfish, mollusks, shrimp, prawns, and other aquatic taxa. The evaluation reports all 10 known records retrieved."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluated query has an Entrez-date upper bound of 2019-02-22, although the protocol specifies no publication-date limit.",
          "recommendation": "Remove any unintended historical date restriction; retain only a database-snapshot bound if required by the review run.",
          "status": "rejected",
          "response": "The packet identifies 2019-02-22 as the required snapshot date, and the translated query applies it as [edat]. The packet reports no [dp] publication-date clause. The evidence therefore supports treating this as the snapshot boundary, not a review publication-date limit."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


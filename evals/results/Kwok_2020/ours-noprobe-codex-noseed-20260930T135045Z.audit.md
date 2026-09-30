# PubMed search strategy: audit

Generated 2026-09-30T14:33:24+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: Method + application context (scoping/map question)
- Scope confirmed by user: no (User cannot answer questions during this run and asked to proceed. Assumed a broad scoping question covering viral metagenomics/virome studies in terrestrial farmed or domesticated animals (including livestock and poultry); farmed aquatic animals are not included unless framed as farm animals in the record. This is an operational scope assumption, not user-confirmed. No language or publication-date limit. PubMed records are bounded by Entrez date through PSB_AS_OF=2019-02-22; no [dp] cutoff. No known relevant articles supplied. Standard-depth discovery: the review-only PubMed pilot found three unrelated records; a 100-record random sample from the focused virus-metagenomics/farm-animal pilot was screened by title/abstract and seven in-scope primary studies were added to the development relevant set. An optional viral-target loss sample of 30 records had no relevant records; because only seven development records are known (below the 15-record safety threshold), the virus block was left out. The final strategy count exceeds the optional-block count, but remains within workload budget. A 20-record category probe drawn from method records indexed as Animals but outside the farm-animal block yielded no eligible records or missing farmed species terms.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viral metagenomics / virome sequencing | search | The defining method is named in relevant reports by metagenomics, virome, viral community sequencing, or related sequencing language; searched as a broad method block. |
| Viruses as the metagenomic target | optional | Virus is the topic-defining target but some abstracts may describe sequencing without naming viruses consistently; test as an optional block before deciding whether to AND. |
| Farmed/domestic animals | search | The animal application context is part of the question; authors generally identify host species and animal indexing, so use a broad category block including farm-animal terms and named livestock/poultry members. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:32:17+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 8,180
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Metagenomics"[Mesh]` | 5,229 | none |
| 2 | `"Genomics"[Mesh]` | 105,464 | none |
| 3 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 4 | `metagenom*[tiab]` | 11,213 | none |
| 5 | `virom*[tiab]` | 824 | none |
| 6 | `"viral metagenom*"[tiab]` | 434 | none |
| 7 | `"virus metagenom*"[tiab]` | 23 | none |
| 8 | `"viral microbiom*"[tiab]` | 9 | none |
| 9 | `viromic*[tiab]` | 42 | none |
| 10 | `"viral community"[tiab]` | 168 | none |
| 11 | `"virus communit*"[tiab]` | 68 | none |
| 12 | `"unbiased sequencing"[tiab]` | 35 | none |
| 13 | `"deep sequencing"[tiab]` | 6,483 | none |
| 14 | `"shotgun sequencing"[tiab]` | 1,193 | none |
| 15 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 16 | `"high throughput sequencing"[tiab]` | 10,541 | none |
| 17 | `"metagenomic sequencing"[tiab]` | 834 | none |
| 18 | `"metatranscriptom*"[tiab]` | 995 | none |
| 19 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18` | 160,245 | none |
| 20 | `"Livestock"[Mesh]` | 3,200 | none |
| 21 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 22 | `"Poultry"[Mesh]` | 147,415 | none |
| 23 | `"Cattle"[Mesh]` | 341,776 | none |
| 24 | `"Swine"[Mesh]` | 214,731 | none |
| 25 | `"Sheep"[Mesh]` | 116,801 | none |
| 26 | `"Goats"[Mesh]` | 30,623 | none |
| 27 | `"Horses"[Mesh]` | 67,676 | none |
| 28 | `"Rabbits"[Mesh]` | 337,179 | none |
| 29 | `livestock[tiab]` | 21,337 | none |
| 30 | `"farm animal*"[tiab]` | 3,666 | none |
| 31 | `"food animal*"[tiab]` | 2,071 | none |
| 32 | `"production animal*"[tiab]` | 410 | none |
| 33 | `"domestic animal*"[tiab]` | 8,110 | none |
| 34 | `cattle[tiab]` | 79,355 | none |
| 35 | `bovine[tiab]` | 189,144 | none |
| 36 | `cow[tiab]` | 29,456 | none |
| 37 | `cows[tiab]` | 45,341 | none |
| 38 | `calf[tiab]` | 43,460 | none |
| 39 | `calves[tiab]` | 24,854 | none |
| 40 | `swine[tiab]` | 42,358 | none |
| 41 | `pig[tiab]` | 127,282 | none |
| 42 | `pigs[tiab]` | 115,325 | none |
| 43 | `porcine[tiab]` | 79,145 | none |
| 44 | `poultry[tiab]` | 25,731 | none |
| 45 | `chicken*[tiab]` | 92,941 | none |
| 46 | `turkey[tiab]` | 32,530 | none |
| 47 | `turkeys[tiab]` | 5,917 | none |
| 48 | `duck[tiab]` | 7,963 | none |
| 49 | `ducks[tiab]` | 5,494 | none |
| 50 | `goose[tiab]` | 2,645 | none |
| 51 | `geese[tiab]` | 1,928 | none |
| 52 | `avian[tiab]` | 50,972 | none |
| 53 | `sheep[tiab]` | 87,044 | none |
| 54 | `ovine[tiab]` | 20,361 | none |
| 55 | `goat*[tiab]` | 31,547 | none |
| 56 | `caprine[tiab]` | 3,127 | none |
| 57 | `horse*[tiab]` | 80,001 | none |
| 58 | `equine[tiab]` | 28,778 | none |
| 59 | `rabbit*[tiab]` | 252,771 | none |
| 60 | `#20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59` | 1,569,128 | none |
| 61 | `#19 AND #60` | 8,180 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Metagenomics"[Mesh] OR "Genomics"[Mesh] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR metagenom*[tiab] OR virom*[tiab] OR "viral metagenom*"[tiab] OR "virus metagenom*"[tiab] OR "viral microbiom*"[tiab] OR viromic*[tiab] OR "viral community"[tiab] OR "virus communit*"[tiab] OR "unbiased sequencing"[tiab] OR "deep sequencing"[tiab] OR "shotgun sequencing"[tiab] OR "next generation sequencing"[tiab] OR "high throughput sequencing"[tiab] OR "metagenomic sequencing"[tiab] OR "metatranscriptom*"[tiab]) AND ("Livestock"[Mesh] OR "Animals, Domestic"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR "Rabbits"[Mesh] OR livestock[tiab] OR "farm animal*"[tiab] OR "food animal*"[tiab] OR "production animal*"[tiab] OR "domestic animal*"[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR poultry[tiab] OR chicken*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck[tiab] OR ducks[tiab] OR goose[tiab] OR geese[tiab] OR avian[tiab] OR sheep[tiab] OR ovine[tiab] OR goat*[tiab] OR caprine[tiab] OR horse*[tiab] OR equine[tiab] OR rabbit*[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Viruses as the metagenomic target | left out | 8,180 / 1,369 | 83.3% | none | 0/30 (up to 10% of removed records could be relevant) | The 30-record loss sample from this unchanged base query was screened and contained no clearly eligible studies. The strategy now has seven screened relevant development records, fewer than the 15-record minimum required to establish that an AND block is safe. Leave the viral-target block out to preserve recall; this returns 8,180 records, within the 10,000 standard budget. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Farmed/domestic animals | 1 | `Animals[Mesh]` | 108,205 | 0/20 |
| Farmed/domestic animals | 2 | `Animals[Mesh]` | 106,030 | 0/20 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virome_metagenomics | 1,569,128 | 0 |
| farm_animals | 160,245 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first two-block draft; MeSH plus broad metagenomic/sequence vocabulary and farm animal category members. No seed records supplied; no matching prior review identified in review-only pilot. |
| 2 | 8,180 | farm_animals: +2 / -1 | none | Fix invalid three-character truncation by enumerating cow/cows; continue with broad category member vocabulary. |
| 3 | 8,180 | limits/combination | none | Add virus-target block as optional because viral target is topic-defining but may be absent from abstracts; measure count reduction and losses before deciding. |
| 4 | 14,302 | virome_metagenomics: +3 / -0 | none | Add screened-set MeSH term Metagenome and phage terminology supported by records in the development set; update protocol audit notes. |
| 5 | 8,356 | virome_metagenomics: +0 / -2 | none | Retain the mined Metagenome heading; remove phage terms after line-count review showed they raised the set beyond the screening budget and overlapped virome terms. Recheck optional decision against revised block. |
| 6 | 8,180 | virome_metagenomics: +0 / -1 | none | Remove Metagenome heading after comparison showed it added 176 records without improving retrieval of the seven known relevant records; restore the exact base query used for the existing optional loss sample and update the decision to reflect the seven-record development set. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 6: 2 findings; F1 should-fix accepted-risk, F2 should-fix open
- Round 2 on version 6: 2 findings; F1 should-fix accepted-risk, F2 should-fix resolved
- Round 3 on version 6: 2 findings; F1 should-fix accepted-risk, F2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1542 NCBI requests logged (929 from cache); strategy sha256 476d144dfd00._

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
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"High-Throughput Nucleotide Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rabbits",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:32:17+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Rabbits\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Metagenomics\"[MeSH Terms] OR \"Genomics\"[MeSH Terms] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"viral metagenom*\"[Title/Abstract] OR \"virus metagenom*\"[Title/Abstract] OR \"viral microbiom*\"[Title/Abstract] OR \"viromic*\"[Title/Abstract] OR \"viral community\"[Title/Abstract] OR \"virus communit*\"[Title/Abstract] OR \"unbiased sequencing\"[Title/Abstract] OR \"deep sequencing\"[Title/Abstract] OR \"shotgun sequencing\"[Title/Abstract] OR \"next generation sequencing\"[Title/Abstract] OR \"high throughput sequencing\"[Title/Abstract] OR \"metagenomic sequencing\"[Title/Abstract] OR \"metatranscriptom*\"[Title/Abstract]) AND (\"Livestock\"[MeSH Terms] OR \"animals, domestic\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Rabbits\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm animal*\"[Title/Abstract] OR \"food animal*\"[Title/Abstract] OR \"production animal*\"[Title/Abstract] OR \"domestic animal*\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"duck\"[Title/Abstract] OR \"ducks\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"avian\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 6,
      "review_sha256": "13a3baaf9080668ddae733be873ae805c117765bfaa37fa9a5d1f37a062937a9",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The population block covers the stated livestock and poultry examples, but the protocol leaves farmed aquatic animals outside scope by assumption. Confirm that boundary or include aquatic farm animals if they are eligible."
        },
        "operators": {
          "verdict": "pass",
          "note": "The method and population blocks are OR-combined internally and AND-combined appropriately; the optional viral-target block was conservatively left out."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The farm-animal category probe is marked stale after a method-block change, so it does not verify the current strategy population coverage."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words include the named livestock and poultry examples as bare terms, alongside broader farm-animal wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query and translations show no syntax or translation errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limit is applied; the Entrez-date boundary is reported consistently as the search as-of limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The question and eligibility refer broadly to farmed or domesticated animals, while the operational scope excludes farmed aquatic animals unless records frame them as farm animals. The packet identifies this as an unconfirmed assumption, and the search has no aquatic-animal terms.",
          "recommendation": "Make the aquatic-animal boundary explicit in the review scope. If farmed aquatic animals are eligible, add appropriate population terms and headings, then rerun the complete evaluation.",
          "status": "accepted-risk",
          "response": "The packet records the terrestrial-only operational assumption and notes that scope could not be confirmed during this run. The limitation is transparent, but aquatic farm-animal studies may be missed."
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The farm-animal category probe is marked stale, while the current method block differs from the probe query: the probe includes \"Metagenome\"[Mesh], which was removed from the current strategy. Its 0/20 result therefore does not establish population-block coverage for the current strategy.",
          "recommendation": "Rerun the category probe using the current method block and farm-animal block, then update the probe status and its evidence.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "d8326888eed3deb3d4b2a54d12661ce7c7d2c201609d13b4ac5ce7fb62014b30",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy covers the stated terrestrial farm-animal scope. The exclusion of farmed aquatic animals is explicitly documented as an operational assumption."
        },
        "operators": {
          "verdict": "pass",
          "note": "Method and animal terms are OR-combined within their blocks and AND-combined across blocks. The optional viral-target block is left out with a documented recall rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The second category probe uses the current method block, without the removed Metagenome heading, and found no relevant records outside the farm-animal block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes broad farm-animal wording and bare names for the listed livestock and poultry members."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query translates without errors or warnings, and the known relevant records are retrieved."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date filter is applied; the Entrez-date boundary is reported consistently as the search as-of limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The question and eligibility refer broadly to farmed or domesticated animals, while the operational scope excludes farmed aquatic animals unless records frame them as farm animals. The packet identifies this as an unconfirmed assumption, and the search has no aquatic-animal terms.",
          "recommendation": "Make the aquatic-animal boundary explicit in the review scope. If farmed aquatic animals are eligible, add appropriate population terms and headings, then rerun the complete evaluation.",
          "status": "accepted-risk",
          "response": "The packet explicitly records a terrestrial-only operational scope and notes that it is an unconfirmed assumption. The limitation is transparent, though aquatic farm-animal studies may be missed."
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The first farm-animal category probe used a method query containing \"Metagenome\"[Mesh], which is absent from the current strategy, so that probe alone did not establish population-block coverage for the current strategy.",
          "recommendation": "Rerun the category probe using the current method block and farm-animal block, then update the probe status and evidence.",
          "status": "resolved",
          "response": "A second category probe was run with the current method block and found no relevant records outside the farm-animal block."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "d8326888eed3deb3d4b2a54d12661ce7c7d2c201609d13b4ac5ce7fb62014b30",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy covers the stated terrestrial farm-animal scope. The packet explicitly records the exclusion of farmed aquatic animals as an unconfirmed operational assumption."
        },
        "operators": {
          "verdict": "pass",
          "note": "Method and animal terms are OR-combined within their blocks and AND-combined across blocks. The optional viral-target block is left out with a documented recall rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports a second category probe using the current method block; it found no relevant records outside the farm-animal block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes broad farm-animal wording and bare names for the listed livestock and poultry members."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query translates without errors or warnings, and all seven known relevant development records are retrieved."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date filter is applied. The Entrez-date boundary is reported consistently as the search as-of limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The question and eligibility refer broadly to farmed or domesticated animals, while the operational scope excludes farmed aquatic animals unless records frame them as farm animals. The packet identifies this as an unconfirmed assumption, and the search has no aquatic-animal terms.",
          "recommendation": "Make the aquatic-animal boundary explicit in the review scope. If farmed aquatic animals are eligible, add appropriate population terms and headings, then rerun the complete evaluation.",
          "status": "accepted-risk",
          "response": "The packet explicitly records the terrestrial-only operational scope and identifies it as an unconfirmed assumption. The limitation is transparent, though aquatic farm-animal studies may be missed."
        },
        {
          "id": "F2",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The first farm-animal category probe used a method query containing \"Metagenome\"[Mesh], which is absent from the current strategy, so that probe alone did not establish population-block coverage for the current strategy.",
          "recommendation": "Rerun the category probe using the current method block and farm-animal block, then update the probe status and evidence.",
          "status": "resolved",
          "response": "A second category probe was run with the current method block; it found no relevant records among the 20 screened outside the farm-animal block."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-28T21:58:13+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: no (User asked to proceed without clarification. Assumed a scoping-style PCC question about viral metagenomics in farmed or managed production animals, including livestock, poultry, aquaculture and managed honeybees. Species/managed groups are a category; category probes were completed. Farm/agricultural context is optional and was left out after its loss sample included relevant studies lacking setting terms. No seeds supplied. PSB_AS_OF=2019-02-22 was set for every command; no publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Viruses | search | The review concerns viral agents, which are reliably named/indexed; broad virus vocabulary will be used. |
| Metagenomics and viral sequencing approaches | search | Metagenomic sequencing is the defining method/topic and is searchable by method terms and indexing. |
| Farmed or managed production animals | search | The population is central and searchable, but records may name a species rather than the farm context; category includes livestock, poultry, aquaculture and managed honeybees. |
| Farm/agricultural context wording | optional | Farm context is searchable but papers may identify the species without stating farm setting in title/abstract; test before requiring. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:56:28+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 8,512
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Viruses"[Mesh]` | 759,255 | none |
| 2 | `virus*[tiab]` | 687,406 | none |
| 3 | `viral[tiab]` | 333,289 | none |
| 4 | `virome[tiab]` | 667 | none |
| 5 | `phage*[tiab]` | 48,158 | none |
| 6 | `bacteriophage*[tiab]` | 34,910 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 1,092,395 | none |
| 8 | `"Metagenomics"[Mesh]` | 5,229 | none |
| 9 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 10 | `metagenom*[tiab]` | 11,213 | none |
| 11 | `virom*[tiab]` | 824 | none |
| 12 | `metavirom*[tiab]` | 45 | none |
| 13 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 14 | `NGS[tiab]` | 9,104 | none |
| 15 | `"high throughput sequencing"[tiab]` | 10,541 | none |
| 16 | `HTS[tiab]` | 5,029 | none |
| 17 | `"deep sequencing"[tiab]` | 6,483 | none |
| 18 | `"shotgun sequencing"[tiab]` | 1,193 | none |
| 19 | `"Genomics"[Mesh]` | 105,464 | none |
| 20 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 165,291 | none |
| 21 | `"Livestock"[Mesh]` | 3,200 | none |
| 22 | `"Poultry"[Mesh]` | 147,415 | none |
| 23 | `"Cattle"[Mesh]` | 341,776 | none |
| 24 | `"Swine"[Mesh]` | 214,731 | none |
| 25 | `"Sheep"[Mesh]` | 116,801 | none |
| 26 | `"Goats"[Mesh]` | 30,623 | none |
| 27 | `"Horses"[Mesh]` | 67,676 | none |
| 28 | `"Rabbits"[Mesh]` | 337,179 | none |
| 29 | `"Chickens"[Mesh]` | 117,975 | none |
| 30 | `"Ducks"[Mesh]` | 10,534 | none |
| 31 | `"Geese"[Mesh]` | 2,682 | none |
| 32 | `"Turkeys"[Mesh]` | 10,103 | none |
| 33 | `"Aquaculture"[Mesh]` | 12,633 | none |
| 34 | `"Fishes"[Mesh]` | 183,474 | none |
| 35 | `livestock[tiab]` | 21,337 | none |
| 36 | `"farm animal"[tiab]` | 833 | none |
| 37 | `cattle[tiab]` | 79,355 | none |
| 38 | `bovine[tiab]` | 189,144 | none |
| 39 | `cow[tiab]` | 29,456 | none |
| 40 | `cows[tiab]` | 45,341 | none |
| 41 | `calf[tiab]` | 43,460 | none |
| 42 | `calves[tiab]` | 24,854 | none |
| 43 | `pig[tiab]` | 127,282 | none |
| 44 | `pigs[tiab]` | 115,325 | none |
| 45 | `swine[tiab]` | 42,358 | none |
| 46 | `porcine[tiab]` | 79,145 | none |
| 47 | `sheep[tiab]` | 87,044 | none |
| 48 | `ovine[tiab]` | 20,361 | none |
| 49 | `goat[tiab]` | 19,304 | none |
| 50 | `goats[tiab]` | 18,753 | none |
| 51 | `caprine[tiab]` | 3,127 | none |
| 52 | `horse[tiab]` | 33,966 | none |
| 53 | `horses[tiab]` | 30,374 | none |
| 54 | `equine[tiab]` | 28,777 | none |
| 55 | `poultry[tiab]` | 25,731 | none |
| 56 | `chicken[tiab]` | 68,650 | none |
| 57 | `chickens[tiab]` | 34,114 | none |
| 58 | `broiler*[tiab]` | 16,896 | none |
| 59 | `turkey[tiab]` | 32,530 | none |
| 60 | `turkeys[tiab]` | 5,917 | none |
| 61 | `duck[tiab]` | 7,963 | none |
| 62 | `ducks[tiab]` | 5,494 | none |
| 63 | `goose[tiab]` | 2,645 | none |
| 64 | `geese[tiab]` | 1,928 | none |
| 65 | `rabbit*[tiab]` | 252,771 | none |
| 66 | `aquaculture[tiab]` | 9,036 | none |
| 67 | `fish[tiab]` | 154,466 | none |
| 68 | `fishes[tiab]` | 19,728 | none |
| 69 | `salmon[tiab]` | 14,743 | none |
| 70 | `trout[tiab]` | 15,264 | none |
| 71 | `carp[tiab]` | 9,326 | none |
| 72 | `tilapia[tiab]` | 4,036 | none |
| 73 | `shrimp[tiab]` | 9,789 | none |
| 74 | `"Bees"[Mesh]` | 12,094 | none |
| 75 | `bee[tiab]` | 11,008 | none |
| 76 | `bees[tiab]` | 8,295 | none |
| 77 | `honeybee*[tiab]` | 5,113 | none |
| 78 | `"honey bee"[tiab]` | 3,312 | none |
| 79 | `"honey bees"[tiab]` | 2,405 | none |
| 80 | `apis mellifera[tiab]` | 4,460 | none |
| 81 | `apiculture[tiab]` | 172 | none |
| 82 | `"Animals"[Mesh]` | 22,808,302 | none |
| 83 | `animal*[tiab]` | 1,038,502 | none |
| 84 | `#21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83` | 22,993,219 | none |
| 85 | `#7 AND #20 AND #84` | 8,512 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Viruses"[Mesh] OR virus*[tiab] OR viral[tiab] OR virome[tiab] OR phage*[tiab] OR bacteriophage*[tiab]) AND ("Metagenomics"[Mesh] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR metagenom*[tiab] OR virom*[tiab] OR metavirom*[tiab] OR "next generation sequencing"[tiab] OR NGS[tiab] OR "high throughput sequencing"[tiab] OR HTS[tiab] OR "deep sequencing"[tiab] OR "shotgun sequencing"[tiab] OR "Genomics"[Mesh]) AND ("Livestock"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR "Rabbits"[Mesh] OR "Chickens"[Mesh] OR "Ducks"[Mesh] OR "Geese"[Mesh] OR "Turkeys"[Mesh] OR "Aquaculture"[Mesh] OR "Fishes"[Mesh] OR livestock[tiab] OR "farm animal"[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR pig[tiab] OR pigs[tiab] OR swine[tiab] OR porcine[tiab] OR sheep[tiab] OR ovine[tiab] OR goat[tiab] OR goats[tiab] OR caprine[tiab] OR horse[tiab] OR horses[tiab] OR equine[tiab] OR poultry[tiab] OR chicken[tiab] OR chickens[tiab] OR broiler*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck[tiab] OR ducks[tiab] OR goose[tiab] OR geese[tiab] OR rabbit*[tiab] OR aquaculture[tiab] OR fish[tiab] OR fishes[tiab] OR salmon[tiab] OR trout[tiab] OR carp[tiab] OR tilapia[tiab] OR shrimp[tiab] OR "Bees"[Mesh] OR bee[tiab] OR bees[tiab] OR honeybee*[tiab] OR "honey bee"[tiab] OR "honey bees"[tiab] OR apis mellifera[tiab] OR apiculture[tiab] OR "Animals"[Mesh] OR animal*[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 12 | 12 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Farm/agricultural context wording | left out | 8,512 / 420 | 95.1% | 22033597, 23627112, 25399116, 26223320, 27619795, 28501627, 29368024, 30521535, 30678330, 30738361, 30783771 | 0/30 (up to 10% of removed records could be relevant) | Leave farm/agricultural context out. This 30-record refresh sample had no eligible additions, while the current known development set contains 11 records lost by requiring the context block. The candidate reduces the count by 95.1%, but known losses violate the AND decision rule; screen production setting during eligibility review. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Farmed or managed production animals | 1 | `Animals[Mesh] OR animal*[tiab]` | 4,638 | 0/30 |
| Farmed or managed production animals | 2 | `Animals[Mesh] OR animal*[tiab]` | 7,010 | 2/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| viral | 119,125 | 0 |
| metagenomics | 916,248 | 0 |
| farmed_animals | 11,639 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first draft: searched viral agent, metagenomics/sequencing, and farmed animal category; tested farm/agricultural wording as optional. Added two eligible records screened from a broad pilot sample; no seed or prior-review benchmark was available. |
| 2 | 1,032 | viral: +6 / -0; metagenomics: +11 / -0; farmed_animals: +53 / -0 | none | Initial recall-first draft with MeSH and title/abstract terms across virus, metagenomics, and farmed-animal category; farm/agricultural context retained as optional for measured testing. Two pilot records screened relevant. |
| 3 | 1,496 | metagenomics: +1 / -0 | none | Addressed critic F1 by adding Genomics[Mesh], the previous indexing heading for Metagenomics (2003-2009); re-evaluate recall and validation after the vocabulary change. |
| 4 | 1,552 | farmed_animals: +8 / -0 | none | Added managed honeybees as a farmed production group after the category probe surfaced eligible bee metagenomic/virome studies; updated scope assumption and population block. Also retained Genomics[Mesh] after PRESS-structured review identified it as prior indexing for Metagenomics. |
| 5 | 8,512 | farmed_animals: +2 / -0 | none | Category probe 2 found two relevant managed-honeybee records, which were added as development records and covered by Bees[Mesh]/bee terms. Following the category protocol for multiple relevant findings, added the broader Animals[Mesh]/animal*[tiab] wording; evaluate its impact alongside historical Genomics heading. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (Same-context critic: no separate fresh-context reviewer is available in this run. Reviewed the packet independently against the six PRESS domains.): 1 findings; F1 should-fix open
- Round 2 on version 5 (Same-context critic revision round: reviewed the current packet and carried the prior finding forward. No separate fresh-context reviewer is available.): 1 findings; F1 should-fix resolved
- Round 3 on version 5 (Same-context closing critic: verified prior dispositions and current evidence; this environment did not provide a separate fresh-context reviewer.): 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1153 NCBI requests logged (670 from cache); strategy sha256 bf5e3d2a55a9._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:farmed_animals",
        "pmids": [
          "25399116",
          "30521535"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-7a36b2d321ebff07d003"
      }
    ],
    "issues": [
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:farmed_animals",
        "pmids": [
          "25399116",
          "30521535"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-7a36b2d321ebff07d003"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"High-Throughput Nucleotide Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Genomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Genomics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rabbits",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Rabbits\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chickens",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Chickens\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ducks",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Ducks\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Geese",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Geese\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Turkeys",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "requested": "Aquaculture",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Aquaculture\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fishes",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Fishes\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bees",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001516",
          "name": "Bees",
          "type": "descriptor",
          "scope_note": "Insect members of the superfamily Apoidea, found almost everywhere, particularly on flowers. About 3500 species occur in North America. They differ from most WASPS in that their young are fed honey and pollen rather than animal food.",
          "tree_numbers": [
            "B01.050.500.131.617.720.500.500.875.387"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001516",
      "preferred_label": "Bees",
      "type": "descriptor",
      "location": "vocabulary:72",
      "term": {
        "text": "\"Bees\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:56:28+00:00",
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
      "location": "vocabulary:80",
      "term": {
        "text": "\"Animals\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Viruses\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virome\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"bacteriophage*\"[Title/Abstract]) AND (\"Metagenomics\"[MeSH Terms] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"metavirom*\"[Title/Abstract] OR \"next generation sequencing\"[Title/Abstract] OR \"NGS\"[Title/Abstract] OR \"high throughput sequencing\"[Title/Abstract] OR \"HTS\"[Title/Abstract] OR \"deep sequencing\"[Title/Abstract] OR \"shotgun sequencing\"[Title/Abstract] OR \"Genomics\"[MeSH Terms]) AND (\"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Rabbits\"[MeSH Terms] OR \"Chickens\"[MeSH Terms] OR \"Ducks\"[MeSH Terms] OR \"Geese\"[MeSH Terms] OR \"Turkeys\"[MeSH Terms] OR \"Aquaculture\"[MeSH Terms] OR \"Fishes\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm animal\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat\"[Title/Abstract] OR \"Goats\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse\"[Title/Abstract] OR \"Horses\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"chicken\"[Title/Abstract] OR \"Chickens\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"Turkeys\"[Title/Abstract] OR \"duck\"[Title/Abstract] OR \"Ducks\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"Geese\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"Aquaculture\"[Title/Abstract] OR \"fish\"[Title/Abstract] OR \"Fishes\"[Title/Abstract] OR \"salmon\"[Title/Abstract] OR \"trout\"[Title/Abstract] OR \"carp\"[Title/Abstract] OR \"tilapia\"[Title/Abstract] OR \"shrimp\"[Title/Abstract] OR \"Bees\"[MeSH Terms] OR \"bee\"[Title/Abstract] OR \"Bees\"[Title/Abstract] OR \"honeybee*\"[Title/Abstract] OR \"honey bee\"[Title/Abstract] OR \"honey bees\"[Title/Abstract] OR \"apis mellifera\"[Title/Abstract] OR \"apiculture\"[Title/Abstract] OR \"Animals\"[MeSH Terms] OR \"animal*\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "95008cb11e97f6035a3aba74e1186fade23cc7277a46e824dd6e78baecd5a1b0",
      "note": "Same-context critic: no separate fresh-context reviewer is available in this run. Reviewed the packet independently against the six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The question is represented as viral agents AND sequencing/metagenomics AND farmed animal population; the optional setting was tested and left out on measured losses. Category probe is complete."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR terms are grouped within concepts and the three required concepts are ANDed; no NOT operator or proximity clauses."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "MeSH record for Metagenomics reports Genomics as its previous indexing (2003-2009); add this heading so older records can be retrieved."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks have text-word coverage for virus/virome, sequencing methods and animal species; truncation stems have at least four characters."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are field-tagged, translations are clean, and no phrase warnings or syntax defects remain."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, or design filter is applied; the Entrez cutoff is imposed by the harness."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The Metagenomics MeSH descriptor reports previous indexing under Genomics (2003-2009), but the current block does not include that predecessor heading.",
          "recommendation": "Add \"Genomics\"[Mesh] to the metagenomics block and rerun evaluation to check impact and known-record retrieval.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "59101cc92c6e2fdd9e026e670e64aa65846aeb19c8bd814c80e2bcda58f263fa",
      "note": "Same-context critic revision round: reviewed the current packet and carried the prior finding forward. No separate fresh-context reviewer is available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The broad animal category now covers named food-production species and managed bees, with generic animal wording added after the two relevant category-probe findings. Farm context remains optional and is left out based on multiple known losses."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR terms are grouped within each concept, and the three core blocks are ANDed. No NOT or proximity constructs are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The Metagenomics descriptor and its previous indexing heading Genomics are both included; Viruses and animal-group headings are explicitly tagged and verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Virus/virome, sequencing and species layers include title/abstract terms; common farmed species and managed honeybees are represented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current query translates without PubMed warnings, phrase issues, or syntax defects."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, or study-design filters are used; the Entrez cutoff is harness-imposed."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The Metagenomics MeSH descriptor reports previous indexing under Genomics (2003-2009), but the current block does not include that predecessor heading.",
          "recommendation": "Add \"Genomics\"[Mesh] to the metagenomics block and rerun evaluation to check impact and known-record retrieval.",
          "status": "resolved",
          "response": "Added \"Genomics\"[Mesh]. The follow-up evaluation showed no known-record losses and 12/12 screened development records retrieved. The total count grew from 1,032 to 1,496 with that addition, and later to 8,512 after the required animal-category widening."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-7a36b2d321ebff07d003",
          "status": "accepted-risk",
          "response": "The two-probe standard budget was spent; both relevant findings from probe 2 (PMIDs 25399116 and 30521535) were added to the development set. The population block now includes Bees[Mesh], bee/apiculture terms, and the broader Animals[Mesh]/animal*[tiab] layer; the measured final count is 8,512 and all 12 development records are retrieved. Residual category-only wording risks remain for human screening.",
          "evidence": "Probe 1 screened 30 and found 0 relevant; probe 2 screened 30 and found 2 relevant (25399116, 30521535). The final broadened query count is 8,512, within the 10,000 workload budget, with 12/12 relevant development records retrieved and no misses."
        }
      ]
    },
    {
      "round": 3,
      "strategy_version": 5,
      "review_sha256": "59101cc92c6e2fdd9e026e670e64aa65846aeb19c8bd814c80e2bcda58f263fa",
      "closing": true,
      "note": "Same-context closing critic: verified prior dispositions and current evidence; this environment did not provide a separate fresh-context reviewer.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The population and method blocks align with the recorded PCC scope; the optional farm-context block remains excluded based on observed losses."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Boolean structure remains grouped OR blocks combined with AND."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Genomics[Mesh] was added for historical indexing; no known records were lost."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current population block includes species plus the broader animal layer, and all relevant screened records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The bound evaluation has no translation, phrase, or syntax issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No ad hoc limits or filters are applied; the Entrez cutoff is externally imposed by the harness."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "metagenomics",
          "finding": "The Metagenomics MeSH descriptor reports previous indexing under Genomics (2003-2009), but the current block does not include that predecessor heading.",
          "recommendation": "Add \"Genomics\"[Mesh] to the metagenomics block and rerun evaluation to check impact and known-record retrieval.",
          "status": "resolved",
          "response": "Added \"Genomics\"[Mesh]. The follow-up evaluation showed no known-record losses and 12/12 screened development records retrieved."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-7a36b2d321ebff07d003",
          "status": "accepted-risk",
          "response": "The category probe budget is spent. Two relevant managed-honeybee records were found and added; the category was widened with Bees[Mesh], bee/apiculture terms, and Animals[Mesh]/animal*[tiab]. The resulting query is within the workload budget and retrieves all known development records. Additional animal-member gaps may remain for screening.",
          "evidence": "The two screened probes found 0/30 and 2/30 relevant records, respectively. Both relevant PMIDs from probe 2 are in the development set. The current evaluation reports 8,512 results and 12/12 relative recall against the relevant development set, with no misses."
        }
      ]
    }
  ]
}
```


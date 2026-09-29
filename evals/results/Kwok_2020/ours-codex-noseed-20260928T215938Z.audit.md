# PubMed search strategy: audit

Generated 2026-09-28T22:24:01+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: yes (User asked to proceed without questions; scope is assumed to cover primary research on viral metagenomics/viromes in terrestrial farm animals, including livestock and poultry (with rabbits, horses, buffalo and camels included as farmed species). Aquaculture species are outside this working interpretation because the question says farm animals; confirm this boundary during protocol review. No language or publication-date limits. Standard depth and 10,000-record screening workload default. PubMed record-entry cutoff is 2019-02-22 via PSB_AS_OF; no publication-date limit is applied. The relevant discovery pool was split into development and validation only after the term-rank diagnostic; no ranked term was adopted, but the split is less independent than a genuinely held-out set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Virus metagenomics and animal viromes | search | The review topic requires metagenomic sequencing or profiling of viral communities; these methods are generally named in titles, abstracts, or indexing. |
| Farmed and livestock animals | search | The population is definitional, but records may name a species rather than the farm-animal category; include common livestock and poultry members and probe broader animal terminology. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:22:57+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 734
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("Metagenomics"[Mesh] AND "Viruses"[Mesh])` | 693 | none |
| 2 | `(metagenom*[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab] OR bacteriophag*[tiab]))` | 1,994 | none |
| 3 | `virom*[tiab]` | 824 | none |
| 4 | `("metagenomic sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab]))` | 190 | none |
| 5 | `("shotgun sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab]))` | 128 | none |
| 6 | `("high-throughput sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab]))` | 930 | none |
| 7 | `("next-generation sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab]))` | 2,216 | none |
| 8 | `("deep sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab]))` | 1,451 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 6,233 | none |
| 10 | `"Livestock"[Mesh]` | 3,200 | none |
| 11 | `"Poultry"[Mesh]` | 147,415 | none |
| 12 | `"Cattle"[Mesh]` | 341,776 | none |
| 13 | `"Swine"[Mesh]` | 214,731 | none |
| 14 | `"Sheep"[Mesh]` | 116,801 | none |
| 15 | `"Goats"[Mesh]` | 30,623 | none |
| 16 | `"Horses"[Mesh]` | 67,676 | none |
| 17 | `"Rabbits"[Mesh]` | 337,179 | none |
| 18 | `"Buffaloes"[Mesh]` | 5,971 | none |
| 19 | `"Camelus"[Mesh]` | 3,639 | none |
| 20 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 21 | `livestock[tiab]` | 21,337 | none |
| 22 | `"farm animal"[tiab]` | 833 | none |
| 23 | `"farm animals"[tiab]` | 3,038 | none |
| 24 | `"domestic animal"[tiab]` | 1,137 | none |
| 25 | `"domestic animals"[tiab]` | 7,245 | none |
| 26 | `cattle[tiab]` | 79,355 | none |
| 27 | `bovine[tiab]` | 189,144 | none |
| 28 | `cow[tiab]` | 29,456 | none |
| 29 | `cows[tiab]` | 45,341 | none |
| 30 | `calf[tiab]` | 43,460 | none |
| 31 | `calves[tiab]` | 24,854 | none |
| 32 | `swine[tiab]` | 42,358 | none |
| 33 | `pig[tiab]` | 127,282 | none |
| 34 | `pigs[tiab]` | 115,325 | none |
| 35 | `piglet*[tiab]` | 17,109 | none |
| 36 | `porcine[tiab]` | 79,145 | none |
| 37 | `sheep[tiab]` | 87,044 | none |
| 38 | `ovine[tiab]` | 20,361 | none |
| 39 | `goat*[tiab]` | 31,547 | none |
| 40 | `caprine[tiab]` | 3,127 | none |
| 41 | `poultry[tiab]` | 25,731 | none |
| 42 | `chicken*[tiab]` | 92,941 | none |
| 43 | `hen[tiab]` | 13,136 | none |
| 44 | `hens[tiab]` | 11,058 | none |
| 45 | `broiler*[tiab]` | 16,896 | none |
| 46 | `turkey*[tiab]` | 35,828 | none |
| 47 | `duck*[tiab]` | 13,075 | none |
| 48 | `goose[tiab]` | 2,645 | none |
| 49 | `geese[tiab]` | 1,928 | none |
| 50 | `horse*[tiab]` | 80,001 | none |
| 51 | `equine[tiab]` | 28,777 | none |
| 52 | `rabbit*[tiab]` | 252,771 | none |
| 53 | `buffalo*[tiab]` | 10,572 | none |
| 54 | `camel*[tiab]` | 9,598 | none |
| 55 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54` | 1,566,197 | none |
| 56 | `#9 AND #55` | 734 | none |

### Strategy (single line, for copying into PubMed)

```text
((("Metagenomics"[Mesh] AND "Viruses"[Mesh]) OR (metagenom*[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab] OR bacteriophag*[tiab])) OR virom*[tiab] OR ("metagenomic sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab])) OR ("shotgun sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab])) OR ("high-throughput sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab])) OR ("next-generation sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab])) OR ("deep sequencing"[tiab] AND (virus*[tiab] OR viral[tiab] OR virom*[tiab] OR phage*[tiab]))) AND ("Livestock"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR "Rabbits"[Mesh] OR "Buffaloes"[Mesh] OR "Camelus"[Mesh] OR "Animals, Domestic"[Mesh] OR livestock[tiab] OR "farm animal"[tiab] OR "farm animals"[tiab] OR "domestic animal"[tiab] OR "domestic animals"[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR piglet*[tiab] OR porcine[tiab] OR sheep[tiab] OR ovine[tiab] OR goat*[tiab] OR caprine[tiab] OR poultry[tiab] OR chicken*[tiab] OR hen[tiab] OR hens[tiab] OR broiler*[tiab] OR turkey*[tiab] OR duck*[tiab] OR goose[tiab] OR geese[tiab] OR horse*[tiab] OR equine[tiab] OR rabbit*[tiab] OR buffalo*[tiab] OR camel*[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 19 | 19 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Farmed and livestock animals | 1 | `(Animals[Mesh] OR animal*[tiab])` | 3,521 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virus_metagenomics | 1,566,197 | 0 |
| farm_animals | 6,233 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad MeSH plus text-word blocks for viral metagenomics and farmed/livestock species; no seeds supplied, using a screened precision pilot. |
| 2 | 732 | farm_animals: +3 / -1 | none | Replace invalid three-letter truncation pig* with explicit pig/pigs and four-letter piglet* morphology. |
| 3 | 732 | virus_metagenomics: +0 / -1 | none | Remove the phrase-index absent and zero-hit clause ‘viral metagenom’; its intended adjacency and morphology are already covered by metagenom* AND viral[tiab] in the block. |
| 4 | 734 | farm_animals: +3 / -0 | none | Add verified MeSH species headings for rabbits, buffaloes, and Camelus, prompted by round-1 critic F1 and the explicit scope terms. Existing text terms retained; no known record should be lost. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; F1 should-fix open, F2 document accepted-risk
- Round 2 on version 4: 2 findings; F1 should-fix resolved, F2 document accepted-risk
- Round 3 on version 4: 2 findings; F1 should-fix resolved, F2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 946 NCBI requests logged (543 from cache); strategy sha256 1d7c4eaf88b0._

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
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rabbits",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "\"Rabbits\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Buffaloes",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"Buffaloes\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Camelus",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "\"Camelus\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:22:57+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "((\"Metagenomics\"[MeSH Terms] AND \"Viruses\"[MeSH Terms]) OR (\"metagenom*\"[Title/Abstract] AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"bacteriophag*\"[Title/Abstract])) OR \"virom*\"[Title/Abstract] OR (\"metagenomic sequencing\"[Title/Abstract] AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"phage*\"[Title/Abstract])) OR (\"shotgun sequencing\"[Title/Abstract] AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"phage*\"[Title/Abstract])) OR (\"high-throughput sequencing\"[Title/Abstract] AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"phage*\"[Title/Abstract])) OR (\"next-generation sequencing\"[Title/Abstract] AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"phage*\"[Title/Abstract])) OR (\"deep sequencing\"[Title/Abstract] AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"phage*\"[Title/Abstract]))) AND (\"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Rabbits\"[MeSH Terms] OR \"Buffaloes\"[MeSH Terms] OR \"Camelus\"[MeSH Terms] OR \"animals, domestic\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm animal\"[Title/Abstract] OR \"farm animals\"[Title/Abstract] OR \"domestic animal\"[Title/Abstract] OR \"domestic animals\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"piglet*\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"hen\"[Title/Abstract] OR \"hens\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"turkey*\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"buffalo*\"[Title/Abstract] OR \"camel*\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "b54002bd074e62bd726eacc6cd95f79224363bd613a649d9f1cfeca6204121fe",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searchable concepts reflect the stated eligibility. The protocol records the terrestrial-only interpretation and flags the aquaculture boundary for confirmation."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy ORs synonyms within each concept and ANDs the virus-metagenomics and farm-animal concepts; no problematic operator or proximity construction is shown."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The verified headings cover major livestock categories, but rabbits, buffalo, and camels are explicitly included in the working scope without corresponding species headings shown. Text-word coverage does not establish coverage of records indexed only under species headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes broad method and virome wording, plus bare animal-category and species names. The packet shows no translation issues or warning-list entries."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query has balanced grouping, valid field tags, and an entry-date bound; no syntax errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or other restrictive limits are applied. The packet reports the 2019-02-22 PubMed entry-date cutoff."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The working scope explicitly includes rabbits, buffalo, and camels, but the population block shows no corresponding species MeSH headings. Those taxa appear only as title/abstract terms; the packet does not demonstrate that the broader domestic-animal heading retrieves records indexed under these species when the abstract lacks the animal name.",
          "recommendation": "Add and test available MeSH headings for the explicitly included species, or document and verify that the existing heading coverage captures them. Rerun the complete evaluation after any change.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "finding": "The eligibility describes animals raised or kept in agricultural production, while the working interpretation excludes aquaculture. That boundary is recorded as an assumption, but the question alone does not resolve it.",
          "recommendation": "Confirm in the protocol whether farmed aquatic animals are in scope; add appropriate population terms and rerun the evaluation if they are.",
          "status": "accepted-risk",
          "response": "The packet explicitly records a terrestrial-farm-animal interpretation and says to confirm the aquaculture boundary during protocol review. Accepting that documented assumption for this draft."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "d38751e9bec4cbedb7a3c63530acc185973866e83d6f2b73cdc9362590aa6d3d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts match the stated eligibility. The protocol records a terrestrial farm-animal interpretation and flags the aquaculture boundary as an assumption for later confirmation."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within each concept, and the metagenomics and population blocks are combined with AND. No problematic operator construction is shown."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The population block now includes explicit Rabbits, Buffaloes, and Camelus MeSH headings. The packet reports PubMed counts for each and shows a complete rerun with all 27 known records retrieved."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes metagenomics, sequencing, and virome wording alongside animal-category and species text words. No translation issues are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query has balanced grouping and field tags, and the packet reports no syntax or validation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit is applied. The strategy uses the recorded 2019-02-22 PubMed entry-date cutoff."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The working scope explicitly includes rabbits, buffalo, and camels, but the population block shows no corresponding species MeSH headings. Those taxa appear only as title/abstract terms; the packet does not demonstrate that the broader domestic-animal heading retrieves records indexed under these species when the abstract lacks the animal name.",
          "recommendation": "Add and test available MeSH headings for the explicitly included species, or document and verify that the existing heading coverage captures them. Rerun the complete evaluation after any change.",
          "status": "resolved",
          "response": "The revised block adds \"Rabbits\"[Mesh], \"Buffaloes\"[Mesh], and \"Camelus\"[Mesh], with PubMed counts reported for all three. The complete evaluation was rerun and reports 27/27 known records retrieved, with no validation issues."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "finding": "The eligibility describes animals raised or kept in agricultural production, while the working interpretation excludes aquaculture. That boundary is recorded as an assumption, but the question alone does not resolve it.",
          "recommendation": "Confirm in the protocol whether farmed aquatic animals are in scope; add appropriate population terms and rerun the evaluation if they are.",
          "status": "accepted-risk",
          "response": "The packet explicitly records a terrestrial-farm-animal interpretation and says to confirm the aquaculture boundary during protocol review. Accepting that documented assumption for this draft."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "d38751e9bec4cbedb7a3c63530acc185973866e83d6f2b73cdc9362590aa6d3d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility is represented by virus-metagenomics and farm-animal search blocks. The packet records a terrestrial-farm-animal interpretation and flags the aquaculture boundary as an assumption for protocol review."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within each concept, and the two concept blocks are combined with AND."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The population block includes the Rabbits, Buffaloes, and Camelus MeSH headings requested by F1. The packet reports a complete evaluation and 27/27 known records retrieved."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes method, sequencing, virome, animal-category, and species text words. No translation issues or warning-list entries are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has balanced grouping and field tags; the packet reports no syntax or validation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The strategy uses the 2019-02-22 PubMed entry-date cutoff and applies no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The working scope explicitly includes rabbits, buffalo, and camels, but the population block shows no corresponding species MeSH headings. Those taxa appear only as title/abstract terms; the packet does not demonstrate that the broader domestic-animal heading retrieves records indexed under these species when the abstract lacks the animal name.",
          "recommendation": "Add and test available MeSH headings for the explicitly included species, or document and verify that the existing heading coverage captures them. Rerun the complete evaluation after any change.",
          "status": "resolved",
          "response": "The current population block includes \"Rabbits\"[Mesh], \"Buffaloes\"[Mesh], and \"Camelus\"[Mesh]. The packet reports counts for these headings, a complete evaluation, and 27/27 known records retrieved with no validation issues."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "finding": "The eligibility describes animals raised or kept in agricultural production, while the working interpretation excludes aquaculture. That boundary is recorded as an assumption, but the question alone does not resolve it.",
          "recommendation": "Confirm in the protocol whether farmed aquatic animals are in scope; add appropriate population terms and rerun the evaluation if they are.",
          "status": "accepted-risk",
          "response": "The packet records a terrestrial-farm-animal interpretation, excludes aquaculture from that working scope, and says to confirm the boundary during protocol review. Accepting that documented assumption for this draft."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


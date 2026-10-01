# PubMed search strategy: audit

Generated 2026-10-01T11:59:17+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC (population, concept, context)
- Scope confirmed by user: yes (User asked not to be contacted during this run; scope and roles are provisional working assumptions. No known relevant records were supplied. Interpreted 'farm animals' as farmed/livestock or other production animals, across species; companion animals are excluded. Interpreted 'virus metagenomics' as broad viral-community/metagenomic sequencing to detect or characterize viruses, rather than targeted testing for a single known virus. No language or publication-date limit is applied. PubMed records are bounded by Entrez date via PSB_AS_OF=2019-02-22.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Farmed and livestock animals | search | The population is central and should be named in searchable records; the animal category includes studies named only by a species or production animal. |
| Viruses and viral communities | search | The topic is specifically viral metagenomics; viral studies may identify a virus or virus family without saying virus metagenomics. |
| Metagenomics and metagenomic sequencing | search | The method defines the review topic, and authors name metagenomic or virome sequencing methods in searchable fields. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:57:32+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 6,236
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Animals, Domestic"[Mesh]` | 34,427 | none |
| 2 | `"Livestock"[Mesh]` | 3,200 | none |
| 3 | `"Poultry"[Mesh]` | 147,415 | none |
| 4 | `"Cattle"[Mesh]` | 341,776 | none |
| 5 | `"Swine"[Mesh]` | 214,731 | none |
| 6 | `"Sheep"[Mesh]` | 116,801 | none |
| 7 | `"Goats"[Mesh]` | 30,623 | none |
| 8 | `"Horses"[Mesh]` | 67,676 | none |
| 9 | `"Chickens"[Mesh]` | 117,975 | none |
| 10 | `"Ducks"[Mesh]` | 10,534 | none |
| 11 | `"Geese"[Mesh]` | 2,682 | none |
| 12 | `"Turkeys"[Mesh]` | 10,103 | none |
| 13 | `livestock[tiab]` | 21,337 | none |
| 14 | `farm*[tiab]` | 76,579 | none |
| 15 | `cattle[tiab]` | 79,355 | none |
| 16 | `bovine[tiab]` | 189,144 | none |
| 17 | `cow[tiab]` | 29,456 | none |
| 18 | `cows[tiab]` | 45,341 | none |
| 19 | `swine[tiab]` | 42,358 | none |
| 20 | `porcine[tiab]` | 79,145 | none |
| 21 | `poultry[tiab]` | 25,731 | none |
| 22 | `chicken*[tiab]` | 92,941 | none |
| 23 | `broiler*[tiab]` | 16,896 | none |
| 24 | `turkey[tiab]` | 32,530 | none |
| 25 | `turkeys[tiab]` | 5,917 | none |
| 26 | `duck*[tiab]` | 13,075 | none |
| 27 | `goose[tiab]` | 2,645 | none |
| 28 | `geese[tiab]` | 1,928 | none |
| 29 | `fowl[tiab]` | 6,948 | none |
| 30 | `sheep[tiab]` | 87,044 | none |
| 31 | `ovine[tiab]` | 20,361 | none |
| 32 | `lamb*[tiab]` | 85,381 | none |
| 33 | `goat*[tiab]` | 31,547 | none |
| 34 | `caprine[tiab]` | 3,127 | none |
| 35 | `horse*[tiab]` | 80,001 | none |
| 36 | `equine[tiab]` | 28,778 | none |
| 37 | `buffalo[tiab]` | 9,137 | none |
| 38 | `bison[tiab]` | 1,108 | none |
| 39 | `camel*[tiab]` | 9,598 | none |
| 40 | `alpaca*[tiab]` | 1,132 | none |
| 41 | `llama*[tiab]` | 1,459 | none |
| 42 | `rabbit*[tiab]` | 252,771 | none |
| 43 | `mink[tiab]` | 3,984 | none |
| 44 | `pig[tiab]` | 127,282 | none |
| 45 | `pigs[tiab]` | 115,325 | none |
| 46 | `hen[tiab]` | 13,136 | none |
| 47 | `hens[tiab]` | 11,058 | none |
| 48 | `"production animal"[tiab:~1]` | 2,855 | none |
| 49 | `"production animals"[tiab:~1]` | 771 | none |
| 50 | `"food animal"[tiab:~1]` | 3,072 | none |
| 51 | `"food animals"[tiab:~1]` | 3,424 | none |
| 52 | `"domestic animal"[tiab:~1]` | 1,211 | none |
| 53 | `"domestic animals"[tiab:~1]` | 7,515 | none |
| 54 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53` | 1,547,265 | none |
| 55 | `"Viruses"[Mesh]` | 759,255 | none |
| 56 | `"DNA Viruses"[Mesh]` | 273,794 | none |
| 57 | `"RNA Viruses"[Mesh]` | 440,928 | none |
| 58 | `"Bacteriophages"[Mesh]` | 56,898 | none |
| 59 | `virus*[tiab]` | 687,408 | none |
| 60 | `viral*[tiab]` | 335,954 | none |
| 61 | `virom*[tiab]` | 824 | none |
| 62 | `bacteriophag*[tiab]` | 34,976 | none |
| 63 | `phage*[tiab]` | 48,158 | none |
| 64 | `virion*[tiab]` | 26,388 | none |
| 65 | `"viral community"[tiab:~1]` | 291 | none |
| 66 | `"viral communities"[tiab:~1]` | 255 | none |
| 67 | `"virus community"[tiab:~1]` | 107 | none |
| 68 | `"virus communities"[tiab:~1]` | 47 | none |
| 69 | `"viral population"[tiab:~1]` | 1,149 | none |
| 70 | `"viral populations"[tiab:~1]` | 876 | none |
| 71 | `"virus population"[tiab:~1]` | 1,117 | none |
| 72 | `"virus populations"[tiab:~1]` | 975 | none |
| 73 | `#55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72` | 1,094,052 | none |
| 74 | `"Metagenomics"[Mesh]` | 5,229 | none |
| 75 | `"High-Throughput Nucleotide Sequencing"[Mesh]` | 28,190 | none |
| 76 | `"Sequence Analysis, DNA"[Mesh]` | 222,713 | none |
| 77 | `"Sequence Analysis, RNA"[Mesh]` | 16,939 | none |
| 78 | `"Whole Genome Sequencing"[Mesh]` | 5,354 | none |
| 79 | `metagenom*[tiab]` | 11,213 | none |
| 80 | `metagenome*[tiab]` | 3,784 | none |
| 81 | `virom*[tiab]` | 824 | none |
| 82 | `"shotgun sequencing"[tiab]` | 1,193 | none |
| 83 | `"next-generation sequencing"[tiab]` | 26,834 | none |
| 84 | `"next generation sequencing"[tiab]` | 26,834 | none |
| 85 | `"high-throughput sequencing"[tiab]` | 10,541 | none |
| 86 | `"high throughput sequencing"[tiab]` | 10,541 | none |
| 87 | `"massively parallel sequencing"[tiab]` | 1,756 | none |
| 88 | `"sequence-independent"[tiab]` | 1,107 | none |
| 89 | `"sequence independent"[tiab]` | 1,107 | none |
| 90 | `SISPA[tiab]` | 43 | none |
| 91 | `"unbiased sequencing"[tiab]` | 35 | none |
| 92 | `"deep sequencing"[tiab]` | 6,483 | none |
| 93 | `"viral community"[tiab:~1]` | 291 | none |
| 94 | `"viral communities"[tiab:~1]` | 255 | none |
| 95 | `"virus community"[tiab:~1]` | 107 | none |
| 96 | `"virus communities"[tiab:~1]` | 47 | none |
| 97 | `#74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89 OR #90 OR #91 OR #92 OR #93 OR #94 OR #95 OR #96` | 286,613 | none |
| 98 | `#54 AND #73 AND #97` | 6,236 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Animals, Domestic"[Mesh] OR "Livestock"[Mesh] OR "Poultry"[Mesh] OR "Cattle"[Mesh] OR "Swine"[Mesh] OR "Sheep"[Mesh] OR "Goats"[Mesh] OR "Horses"[Mesh] OR "Chickens"[Mesh] OR "Ducks"[Mesh] OR "Geese"[Mesh] OR "Turkeys"[Mesh] OR livestock[tiab] OR farm*[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR swine[tiab] OR porcine[tiab] OR poultry[tiab] OR chicken*[tiab] OR broiler*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck*[tiab] OR goose[tiab] OR geese[tiab] OR fowl[tiab] OR sheep[tiab] OR ovine[tiab] OR lamb*[tiab] OR goat*[tiab] OR caprine[tiab] OR horse*[tiab] OR equine[tiab] OR buffalo[tiab] OR bison[tiab] OR camel*[tiab] OR alpaca*[tiab] OR llama*[tiab] OR rabbit*[tiab] OR mink[tiab] OR pig[tiab] OR pigs[tiab] OR hen[tiab] OR hens[tiab] OR "production animal"[tiab:~1] OR "production animals"[tiab:~1] OR "food animal"[tiab:~1] OR "food animals"[tiab:~1] OR "domestic animal"[tiab:~1] OR "domestic animals"[tiab:~1]) AND ("Viruses"[Mesh] OR "DNA Viruses"[Mesh] OR "RNA Viruses"[Mesh] OR "Bacteriophages"[Mesh] OR virus*[tiab] OR viral*[tiab] OR virom*[tiab] OR bacteriophag*[tiab] OR phage*[tiab] OR virion*[tiab] OR "viral community"[tiab:~1] OR "viral communities"[tiab:~1] OR "virus community"[tiab:~1] OR "virus communities"[tiab:~1] OR "viral population"[tiab:~1] OR "viral populations"[tiab:~1] OR "virus population"[tiab:~1] OR "virus populations"[tiab:~1]) AND ("Metagenomics"[Mesh] OR "High-Throughput Nucleotide Sequencing"[Mesh] OR "Sequence Analysis, DNA"[Mesh] OR "Sequence Analysis, RNA"[Mesh] OR "Whole Genome Sequencing"[Mesh] OR metagenom*[tiab] OR metagenome*[tiab] OR virom*[tiab] OR "shotgun sequencing"[tiab] OR "next-generation sequencing"[tiab] OR "next generation sequencing"[tiab] OR "high-throughput sequencing"[tiab] OR "high throughput sequencing"[tiab] OR "massively parallel sequencing"[tiab] OR "sequence-independent"[tiab] OR "sequence independent"[tiab] OR SISPA[tiab] OR "unbiased sequencing"[tiab] OR "deep sequencing"[tiab] OR "viral community"[tiab:~1] OR "viral communities"[tiab:~1] OR "virus community"[tiab:~1] OR "virus communities"[tiab:~1])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Farmed and livestock animals | 1 | `Animals[Mesh] OR animal*[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR poultry[tiab] OR chicken[tiab] OR chickens[tiab] OR sheep[tiab] OR goat[tiab] OR horse[tiab] OR livestock[tiab]` | 21,181 | 0/30 |
| Viruses and viral communities | 1 | `metagenom*[tiab] OR metagenome*[tiab] OR virom*[tiab] OR Metagenomics[Mesh] OR Metagenome[Mesh]` | 756 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| farm_animals | 34,402 | 0 |
| viruses | 22,105 | 0 |
| metagenomics | 137,081 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial three-block draft built from PCC interpretation and screened records from one precise date-bounded pilot; no user seeds were supplied. |
| 2 | 0 | farm_animals: +48 / -0; viruses: +14 / -0; metagenomics: +21 / -0 | none | Initial three-block draft with MeSH and title/abstract terms; expanded production-animal species vocabulary from MeSH and the screened pilot set. |
| 3 | 6,236 | farm_animals: +10 / -5; viruses: +8 / -4; metagenomics: +4 / -2 | none | Fixed block serialization and short truncation errors; replaced wildcard phrases with explicit forms and tested any-order proximity variants. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-LF-01 must-fix rejected, R1-SY-01 document accepted-risk
- Round 2 on version 3: 2 findings; R1-LF-01 must-fix rejected, R1-SY-01 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 965 NCBI requests logged (368 from cache); strategy sha256 8628cde78ff4._

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
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"Animals, Domestic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Livestock\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Poultry\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Cattle\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Swine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "\"Sheep\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "\"Goats\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"Horses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chickens",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Chickens\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ducks",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Ducks\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Geese",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Geese\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Turkeys",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Turkeys\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:54",
      "term": {
        "text": "\"Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "DNA Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:55",
      "term": {
        "text": "\"DNA Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "RNA Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:56",
      "term": {
        "text": "\"RNA Viruses\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bacteriophages",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:57",
      "term": {
        "text": "\"Bacteriophages\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Metagenomics",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:72",
      "term": {
        "text": "\"Metagenomics\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:73",
      "term": {
        "text": "\"High-Throughput Nucleotide Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sequence Analysis, DNA",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
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
      "location": "vocabulary:74",
      "term": {
        "text": "\"Sequence Analysis, DNA\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sequence Analysis, RNA",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017423",
          "name": "Sequence Analysis, RNA",
          "type": "descriptor",
          "scope_note": "A multistage process that includes cloning, physical mapping, subcloning, sequencing, and information analysis of an RNA SEQUENCE.",
          "tree_numbers": [
            "E05.393.760.710"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017423",
      "preferred_label": "Sequence Analysis, RNA",
      "type": "descriptor",
      "location": "vocabulary:75",
      "term": {
        "text": "\"Sequence Analysis, RNA\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Whole Genome Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:57:32+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000073336",
          "name": "Whole Genome Sequencing",
          "type": "descriptor",
          "scope_note": "Techniques to determine the entire sequence of the GENOME of an organism or individual.",
          "tree_numbers": [
            "E05.393.760.700.825"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000073336",
      "preferred_label": "Whole Genome Sequencing",
      "type": "descriptor",
      "location": "vocabulary:76",
      "term": {
        "text": "\"Whole Genome Sequencing\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"animals, domestic\"[MeSH Terms] OR \"Livestock\"[MeSH Terms] OR \"Poultry\"[MeSH Terms] OR \"Cattle\"[MeSH Terms] OR \"Swine\"[MeSH Terms] OR \"Sheep\"[MeSH Terms] OR \"Goats\"[MeSH Terms] OR \"Horses\"[MeSH Terms] OR \"Chickens\"[MeSH Terms] OR \"Ducks\"[MeSH Terms] OR \"Geese\"[MeSH Terms] OR \"Turkeys\"[MeSH Terms] OR \"Livestock\"[Title/Abstract] OR \"farm*\"[Title/Abstract] OR \"Cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"Swine\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"Poultry\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"Turkeys\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"Geese\"[Title/Abstract] OR \"fowl\"[Title/Abstract] OR \"Sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"lamb*\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"buffalo\"[Title/Abstract] OR \"bison\"[Title/Abstract] OR \"camel*\"[Title/Abstract] OR \"alpaca*\"[Title/Abstract] OR \"llama*\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"mink\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"hen\"[Title/Abstract] OR \"hens\"[Title/Abstract] OR \"production animal\"[Title/Abstract:~1] OR \"production animals\"[Title/Abstract:~1] OR \"food animal\"[Title/Abstract:~1] OR \"food animals\"[Title/Abstract:~1] OR \"domestic animal\"[Title/Abstract:~1] OR \"domestic animals\"[Title/Abstract:~1]) AND (\"Viruses\"[MeSH Terms] OR \"DNA Viruses\"[MeSH Terms] OR \"RNA Viruses\"[MeSH Terms] OR \"Bacteriophages\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"bacteriophag*\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"virion*\"[Title/Abstract] OR \"viral community\"[Title/Abstract:~1] OR \"viral communities\"[Title/Abstract:~1] OR \"virus community\"[Title/Abstract:~1] OR \"virus communities\"[Title/Abstract:~1] OR \"viral population\"[Title/Abstract:~1] OR \"viral populations\"[Title/Abstract:~1] OR \"virus population\"[Title/Abstract:~1] OR \"virus populations\"[Title/Abstract:~1]) AND (\"Metagenomics\"[MeSH Terms] OR \"High-Throughput Nucleotide Sequencing\"[MeSH Terms] OR \"sequence analysis, dna\"[MeSH Terms] OR \"sequence analysis, rna\"[MeSH Terms] OR \"Whole Genome Sequencing\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"metagenome*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"shotgun sequencing\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"next-generation sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"high-throughput sequencing\"[Title/Abstract] OR \"massively parallel sequencing\"[Title/Abstract] OR \"sequence-independent\"[Title/Abstract] OR \"sequence-independent\"[Title/Abstract] OR \"SISPA\"[Title/Abstract] OR \"unbiased sequencing\"[Title/Abstract] OR \"deep sequencing\"[Title/Abstract] OR \"viral community\"[Title/Abstract:~1] OR \"viral communities\"[Title/Abstract:~1] OR \"virus community\"[Title/Abstract:~1] OR \"virus communities\"[Title/Abstract:~1]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "fe7396ed143bca95acc740e63aa49fb996203e10a811450deb61e5c368da3796",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three searched concepts align with the stated eligibility. Animal species and production-animal names appear as their own Title/Abstract terms; viral and metagenomic/sequence terms are represented in their respective blocks. The seven known relevant records are retrieved in all three blocks."
        },
        "operators": {
          "verdict": "pass",
          "note": "Each concept is combined internally with OR and the three concept blocks are combined with AND. No exclusion operator risks removing eligible records. The full expression is parenthesized."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed animal, virus, and sequencing headings are translated as MeSH terms; the packet reports no translation issues or PubMed errors. Text words supplement the headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover farm and production animal names, virus and viral-community language, and metagenomic, virome, shotgun, and other broad sequencing language. The method terms are intentionally broad enough to require eligibility screening. The category probes found no relevant records in the screened samples outside the animal or virus blocks (0/30 each), while the known relevant set is retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports null warning and error lists, no translation issues, and no validation issues. Proximity clauses were reviewed individually; see the documented accepted-risk finding."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez Date bound ending 2019-02-22 matches the explicit harness instruction to work as of 2019-02-22; it is an Entrez date bound, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query includes (\"1800/01/01\"[edat] : \"2019/02/22\"[edat]). The scope records no publication-date limit, but this Entrez Date bound caps retrieval at records added to PubMed by 2019-02-22; the packet's run date is 2026-10-01.",
          "recommendation": "Retain the Entrez Date ceiling required by the as-of simulation. Do not treat it as a publication-date limit.",
          "status": "rejected",
          "response": "Rejected: the user explicitly requires the 2019-02-22 simulation and says to retain the Entrez-date bound. The bound implements that as-of harness instruction; it is not a publication-date limit."
        },
        {
          "id": "R1-SY-01",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "The retained proximity expressions occur in animal phrases #48-53, virus/community and population phrases #65-72, and viral-community method phrases #93-96. Each uses ~1, allowing either word order and up to one intervening word; there are no wildcards in these proximity expressions. The packet shows these expressions translated individually and in the complete query without reported warnings or errors. This breadth may retrieve loose phrase matches, but screening is already required for the broad eligibility and method vocabulary.",
          "recommendation": "Retain these tested expressions for recall and screen their results; preserve the clause-specific proximity interpretation in the search record. If any expression is rewritten or removed, run a new complete evaluation.",
          "status": "accepted-risk",
          "response": "Accepted for this draft: the affected clauses and ~1 behavior are identified above; the expressions have no proximity wildcards and the packet reports successful individual and aggregate translation with no warnings or errors."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "fe7396ed143bca95acc740e63aa49fb996203e10a811450deb61e5c368da3796",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three blocks match the stated population, viral topic, and metagenomic/broad-sequencing method. The packet reports all seven known relevant records retrieved in each block, no misses, and no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines terms within each concept and AND combines the three concept blocks. The query is parenthesized and contains no exclusion operator."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The animal, virus, and sequencing MeSH terms are verified in the packet and translate without reported issues. Text words supplement them."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes animal species and production-animal wording, virus and viral-community wording, and metagenomic, virome, and broad sequencing terms. The screened category probes found 0 relevant records among 30 sampled outside each of the animal and virus blocks. The resulting count of 6,236 is below the workload budget of 10,000."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed warnings or errors, no translation issues, and complete validation without issues. The retained ~1 clauses were reviewed individually in round 1; their behavior and accepted-risk disposition remain unchanged."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2019-02-22 Entrez Date ceiling matches the protocol as_of value and the explicit PSB_AS_OF instruction recorded in the packet. It is an Entrez-date simulation bound, not a publication-date limit; the scope notes no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query has an Entrez Date ceiling of 2019-02-22. The packet's protocol sets as_of to 2019-02-22 and explicitly says PubMed records are bounded by Entrez date via PSB_AS_OF=2019-02-22; publication-date limits remain absent.",
          "recommendation": "Retain this bound for the instructed as-of simulation; do not interpret it as a publication-date limit.",
          "status": "rejected",
          "response": "Rejected: the packet confirms the user's explicit as-of 2019-02-22 instruction and says to apply that Entrez-date bound. It is not a publication-date limit."
        },
        {
          "id": "R1-SY-01",
          "domain": "syntax",
          "severity": "document",
          "kind": "syntax",
          "finding": "Proximity expressions remain in animal phrases #48-53, virus/community and population phrases #65-72, and viral-community method phrases #93-96. Each uses ~1, permitting either word order and up to one intervening word; none uses a wildcard. The packet reports successful individual and aggregate translation without warnings or errors. The broader matching behavior may admit loose phrase matches, which require screening.",
          "recommendation": "Retain these tested expressions for recall and screen their results; preserve the clause-specific interpretation in the search record. Any rewrite or removal requires a new complete evaluation.",
          "status": "accepted-risk",
          "response": "Accepted risk carried forward: clauses and ~1 behavior are specified, there are no proximity wildcards, and the packet reports no translation warnings or errors."
        }
      ],
      "issue_dispositions": [
        {
          "status": "rejected",
          "response": "The explicit as-of 2019-02-22 instruction requires the Entrez-date ceiling; it is not a publication-date limit.",
          "issue_id": "R1-LF-01"
        },
        {
          "status": "accepted-risk",
          "response": "Retain the interpreted, tested ~1 expressions for recall; screen results and reevaluate fully if they are changed.",
          "issue_id": "R1-SY-01"
        }
      ]
    }
  ]
}
```


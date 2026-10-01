# PubMed search strategy: audit

Generated 2026-10-01T11:22:47+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC
- Scope confirmed by user: no (User requested proceeding without questions. Scope assumed: primary studies of virus/virome characterization using metagenomic or metatranscriptomic methods in food-producing farmed animals, including farmed fish/aquaculture; broad organism and sample types, no language or date limits. Review articles may be searched to find candidate benchmark studies but are not eligible evidence. Scope not confirmed by user. PubMed availability bounded to Entrez date 2019-02-22 via PSB_AS_OF; no publication-date limit. No known relevant records were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Metagenomic methods | search | The method defines the topic and is named in searchable records. |
| Viruses and viral communities | search | The viral target defines the topic; studies may name only particular viruses or viral communities. |
| Farmed animals | search | The population defines the question; records may name animal species without saying livestock or farm animal. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:21:30+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 326
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Metagenomics[Mesh]` | 5,229 | none |
| 2 | `metagenom*[tiab]` | 11,213 | none |
| 3 | `metatranscriptom*[tiab]` | 995 | none |
| 4 | `virom*[tiab]` | 824 | none |
| 5 | `environmental genomics[tiab]` | 130 | none |
| 6 | `community genomics[tiab]` | 30 | none |
| 7 | `viral metagenom*[tiab]` | 434 | none |
| 8 | `viral metatranscriptom*[tiab]` | 2 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 13,551 | none |
| 10 | `Viruses[Mesh]` | 759,255 | none |
| 11 | `virus*[tiab]` | 687,408 | none |
| 12 | `viral[tiab]` | 333,289 | none |
| 13 | `virolog*[tiab]` | 36,884 | none |
| 14 | `virome[tiab]` | 667 | none |
| 15 | `viromes[tiab]` | 211 | none |
| 16 | `viromic*[tiab]` | 42 | none |
| 17 | `phage*[tiab]` | 48,158 | none |
| 18 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 1,092,592 | none |
| 19 | `Livestock[Mesh]` | 3,200 | none |
| 20 | `Poultry[Mesh]` | 147,415 | none |
| 21 | `Cattle[Mesh]` | 341,776 | none |
| 22 | `Swine[Mesh]` | 214,731 | none |
| 23 | `Sheep[Mesh]` | 116,801 | none |
| 24 | `Goats[Mesh]` | 30,623 | none |
| 25 | `Horses[Mesh]` | 67,676 | none |
| 26 | `Fishes[Mesh]` | 183,474 | none |
| 27 | `livestock[tiab]` | 21,337 | none |
| 28 | `farm animal*[tiab]` | 3,666 | none |
| 29 | `farmed animal*[tiab]` | 195 | none |
| 30 | `domestic animal*[tiab]` | 8,110 | none |
| 31 | `food animal*[tiab]` | 2,071 | none |
| 32 | `food-producing animal*[tiab]` | 1,078 | none |
| 33 | `food producing animal*[tiab]` | 1,078 | none |
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
| 46 | `avian[tiab]` | 50,972 | none |
| 47 | `turkey[tiab]` | 32,530 | none |
| 48 | `turkeys[tiab]` | 5,917 | none |
| 49 | `duck[tiab]` | 7,963 | none |
| 50 | `ducks[tiab]` | 5,494 | none |
| 51 | `goose[tiab]` | 2,645 | none |
| 52 | `geese[tiab]` | 1,928 | none |
| 53 | `sheep[tiab]` | 87,044 | none |
| 54 | `ovine[tiab]` | 20,361 | none |
| 55 | `lamb[tiab]` | 9,836 | none |
| 56 | `lambs[tiab]` | 14,624 | none |
| 57 | `goat*[tiab]` | 31,547 | none |
| 58 | `caprine[tiab]` | 3,127 | none |
| 59 | `horse*[tiab]` | 80,001 | none |
| 60 | `equine[tiab]` | 28,778 | none |
| 61 | `farmed fish[tiab]` | 733 | none |
| 62 | `aquaculture[tiab]` | 9,036 | none |
| 63 | `fisheries[tiab]` | 4,923 | none |
| 64 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63` | 1,418,846 | none |
| 65 | `#9 AND #18 AND #64` | 326 | none |

### Strategy (single line, for copying into PubMed)

```text
((Metagenomics[Mesh] OR metagenom*[tiab] OR metatranscriptom*[tiab] OR virom*[tiab] OR environmental genomics[tiab] OR community genomics[tiab] OR viral metagenom*[tiab] OR viral metatranscriptom*[tiab]) AND (Viruses[Mesh] OR virus*[tiab] OR viral[tiab] OR virolog*[tiab] OR virome[tiab] OR viromes[tiab] OR viromic*[tiab] OR phage*[tiab]) AND (Livestock[Mesh] OR Poultry[Mesh] OR Cattle[Mesh] OR Swine[Mesh] OR Sheep[Mesh] OR Goats[Mesh] OR Horses[Mesh] OR Fishes[Mesh] OR livestock[tiab] OR farm animal*[tiab] OR farmed animal*[tiab] OR domestic animal*[tiab] OR food animal*[tiab] OR food-producing animal*[tiab] OR food producing animal*[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR poultry[tiab] OR chicken*[tiab] OR avian[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck[tiab] OR ducks[tiab] OR goose[tiab] OR geese[tiab] OR sheep[tiab] OR ovine[tiab] OR lamb[tiab] OR lambs[tiab] OR goat*[tiab] OR caprine[tiab] OR horse*[tiab] OR equine[tiab] OR farmed fish[tiab] OR aquaculture[tiab] OR fisheries[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Viruses and viral communities | 1 | `RNA[tiab] OR DNA[tiab] OR genome*[tiab] OR sequence*[tiab]` | 425 | 0/30 |
| Viruses and viral communities | 2 | `RNA[tiab] OR DNA[tiab] OR genome*[tiab] OR sequence*[tiab]` | 425 | 0/30 |
| Farmed animals | 1 | `Animals[Mesh] OR animal*[tiab]` | 1,256 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| metagenomics | 123,104 | 0 |
| virus | 1,088 | 0 |
| farm_animals | 2,590 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad three-block strategy from assumed scope; MeSH plus text words for metagenomics, viruses and food-producing farmed animal members. No known records supplied; next discover and screen candidate reviews and pilots. |
| 2 | 0 | metagenomics: +8 / -0; virus: +8 / -0; farm_animals: +43 / -0 | none | Initial broad three-block strategy from assumed scope; MeSH plus text words for metagenomics, viruses and farmed-animal members. No known records supplied; next discover and screen candidate reviews and pilots. |
| 3 | 326 | limits/combination | none | Initial broad three-block strategy from assumed scope; MeSH plus text words for metagenomics, viruses and farmed-animal members. No known records supplied; next discover and screen candidate reviews and pilots. |
| 4 | 326 | farm_animals: +2 / -0 | none | Added the two explicit food-producing animal variants recommended by critic finding R1-1, then re-evaluated. The 11-record relative recall remains development-only; R1-2 is accepted as a reporting risk because no user-supplied or independent benchmark records were available. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-1 should-fix open, R1-2 should-fix open
- Round 2 on version 4: 2 findings; R1-1 should-fix resolved, R1-2 should-fix accepted-risk
- Round 3 on version 4: 2 findings; R1-1 should-fix resolved, R1-2 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 817 NCBI requests logged (371 from cache); strategy sha256 88c67c3bbef0._

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
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Metagenomics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "Viruses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Livestock",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Poultry",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Cattle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Swine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Sheep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Goats",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
        "text": "Horses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fishes",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:21:30+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "Fishes",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"metagenomics\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"metatranscriptom*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"environmental genomics\"[Title/Abstract] OR \"community genomics\"[Title/Abstract] OR \"viral metagenom*\"[Title/Abstract] OR \"viral metatranscriptom*\"[Title/Abstract]) AND (\"viruses\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virolog*\"[Title/Abstract] OR \"virome\"[Title/Abstract] OR \"viromes\"[Title/Abstract] OR \"viromic*\"[Title/Abstract] OR \"phage*\"[Title/Abstract]) AND (\"livestock\"[MeSH Terms] OR \"poultry\"[MeSH Terms] OR \"cattle\"[MeSH Terms] OR \"swine\"[MeSH Terms] OR (\"sheep, domestic\"[MeSH Terms] OR \"sheep\"[MeSH Terms]) OR \"goats\"[MeSH Terms] OR \"horses\"[MeSH Terms] OR \"fishes\"[MeSH Terms] OR \"livestock\"[Title/Abstract] OR \"farm animal*\"[Title/Abstract] OR \"farmed animal*\"[Title/Abstract] OR \"domestic animal*\"[Title/Abstract] OR \"food animal*\"[Title/Abstract] OR \"food producing animal*\"[Title/Abstract] OR \"food producing animal*\"[Title/Abstract] OR \"cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"poultry\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"avian\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"duck\"[Title/Abstract] OR \"ducks\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"lamb\"[Title/Abstract] OR \"lambs\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"farmed fish\"[Title/Abstract] OR \"aquaculture\"[Title/Abstract] OR \"fisheries\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "b90f2cb9cfeef6f132cc751eed096ae34a8d9efa6119db79510173e7a69271c8",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The farm-animal block lacks explicit text words for food-producing animals; add the hyphenated and unhyphenated variants and test them."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three required concepts are AND-ed; no optional block is present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Method, virus, and animal headings are relevant; poultry is represented separately from Livestock."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add explicit variants for food-producing animals and re-evaluate."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or translation problems were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No search limits are used; the PubMed Entrez date bound is documented."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria specify farmed or food-producing animals, but the textword block has food animal* without explicit food-producing animal variants.",
          "recommendation": "Add food-producing and food producing animal variants to the farm-animal block and run a complete evaluation.",
          "status": "open"
        },
        {
          "id": "R1-2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 100% known-record recall is based on 11 records from a screened pilot sample, and category probes screened only 30 records each; these do not provide independent validation.",
          "recommendation": "Report the result as development-set recall and seek additional independently sourced studies or broader screening if stronger validation is required.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "4ba6b10024d950c2d1e30946fea273c7725aa1d5529a86b9bf2c483fb8da3648",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The farm-animal block now includes both food-producing animal variants and named species."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three required concepts are AND-ed; all 11 known development records are retrieved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant MeSH headings cover method, viruses, and farm-animal groups; Poultry is separate from Livestock."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Method, viral-target, and animal text words include food-producing variants; category probes found no relevant records in their samples."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete strategy evaluation ran without syntax or translation problems."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are applied. The Entrez date bound is the database horizon, not a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria specify farmed or food-producing animals, but the textword block has food animal* without explicit food-producing animal variants.",
          "recommendation": "Add food-producing and food producing animal variants to the farm-animal block and run a complete evaluation.",
          "status": "resolved",
          "response": "Both food-producing animal*[tiab] and food producing animal*[tiab] are now in the farm-animal block. The complete evaluation reports 326 results, retrieves all 11 known records, and reports no regression."
        },
        {
          "id": "R1-2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 100% known-record recall is based on 11 records from a screened pilot sample, and category probes screened only 30 records each; these do not provide independent validation.",
          "recommendation": "Report the result as development-set recall and seek additional independently sourced studies or broader screening if stronger validation is required.",
          "status": "accepted-risk",
          "response": "The 11 records are identified as a screened pilot sample and the 100% figure as development-set recall only. Each category probe screened 30 records and found none relevant. No independent validation set was available, so stronger validation remains a limitation."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "4ba6b10024d950c2d1e30946fea273c7725aa1d5529a86b9bf2c483fb8da3648",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The farm-animal block includes both food-producing animal variants and named species."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three required concepts are AND-ed. All 11 known development records are retrieved; recall is not independent validation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant MeSH headings cover metagenomic methods, viruses, and animal groups, with Poultry separate from Livestock."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words include food-producing animal variants and named farm-animal species; probes found no eligible records in their samples."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete evaluation reports no syntax or translation problems."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are applied. The Entrez date bound is documented as the database horizon."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria specify farmed or food-producing animals, but the textword block initially lacked explicit food-producing animal variants.",
          "recommendation": "Add food-producing and food producing animal variants to the farm-animal block and run a complete evaluation.",
          "status": "resolved",
          "response": "Both food-producing animal*[tiab] and food producing animal*[tiab] are present. The complete evaluation reports 326 results, retrieves all 11 known records, and reports no regression."
        },
        {
          "id": "R1-2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 100% known-record recall is based on 11 records from a screened pilot sample, and category probes screened only 30 records each; these do not provide independent validation.",
          "recommendation": "Report the result as development-set recall and seek additional independently sourced studies or broader screening if stronger validation is required.",
          "status": "accepted-risk",
          "response": "The 11 records are identified as a screened pilot sample, and 100% recall is development-set recall. Each category probe screened 30 records and found none relevant. No independent validation set was available, so stronger validation remains a limitation."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


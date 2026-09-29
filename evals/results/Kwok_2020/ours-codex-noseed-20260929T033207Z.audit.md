# PubMed search strategy: audit

Generated 2026-09-29T03:47:19+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: PCC (scoping review)
- Scope confirmed by user: no (User asked to proceed without clarification. Assumed broad scoping-review scope across farmed/domesticated livestock, poultry, and farmed aquatic animals; species and study design will be screened. No known relevant articles supplied. PubMed is bounded by Entrez date 2019-02-22 through PSB_AS_OF; no publication-date limit is used. The first farm-animal category probe found one in-scope farmed-eel record, prompting aquatic-farming terms in the population block.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Virus metagenomics | search | Core topic; relevant studies must investigate viral metagenomics, although terminology may vary. |
| Farm animals/livestock | search | Population/context is central to the question and often named or indexed; as a category, records may name only a species or production class. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:46:40+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 318
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `(Metagenomics[Mesh] AND Viruses[Mesh])` | 693 | none |
| 2 | `(metagenom*[tiab] AND (virus*[tiab] OR viral[tiab]))` | 1,794 | none |
| 3 | `virom*[tiab]` | 824 | none |
| 4 | `#1 OR #2 OR #3` | 2,347 | none |
| 5 | `Animals, Domestic[Mesh]` | 34,427 | none |
| 6 | `Livestock[Mesh]` | 3,200 | none |
| 7 | `Poultry[Mesh]` | 147,415 | none |
| 8 | `Cattle[Mesh]` | 341,776 | none |
| 9 | `Swine[Mesh]` | 214,731 | none |
| 10 | `Sheep[Mesh]` | 116,801 | none |
| 11 | `Goats[Mesh]` | 30,623 | none |
| 12 | `Horses[Mesh]` | 67,676 | none |
| 13 | `(farm animal*[tiab] OR farmed animal*[tiab] OR livestock[tiab] OR poultry[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR sheep[tiab] OR ovine[tiab] OR goat[tiab] OR goats[tiab] OR caprine[tiab] OR horse[tiab] OR horses[tiab] OR equine[tiab] OR chicken*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck[tiab] OR ducks[tiab] OR geese[tiab] OR goose[tiab] OR buffalo[tiab] OR rabbit*[tiab] OR camel*[tiab] OR alpaca*[tiab])` | 1,106,773 | none |
| 14 | `Aquaculture[Mesh]` | 12,633 | none |
| 15 | `fish*[tiab]` | 215,105 | none |
| 16 | `aquacultur*[tiab]` | 9,364 | none |
| 17 | `eel[tiab]` | 4,638 | none |
| 18 | `salmon*[tiab]` | 94,346 | none |
| 19 | `trout*[tiab]` | 15,375 | none |
| 20 | `shrimp*[tiab]` | 10,498 | none |
| 21 | `prawn*[tiab]` | 1,678 | none |
| 22 | `mussel*[tiab]` | 9,019 | none |
| 23 | `oyster*[tiab]` | 7,043 | none |
| 24 | `carp*[tiab]` | 43,260 | none |
| 25 | `tilapia*[tiab]` | 4,095 | none |
| 26 | `catfish[tiab]` | 5,587 | none |
| 27 | `#5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 1,745,651 | none |
| 28 | `#4 AND #27` | 318 | none |

### Strategy (single line, for copying into PubMed)

```text
(((Metagenomics[Mesh] AND Viruses[Mesh]) OR (metagenom*[tiab] AND (virus*[tiab] OR viral[tiab])) OR virom*[tiab]) AND (Animals, Domestic[Mesh] OR Livestock[Mesh] OR Poultry[Mesh] OR Cattle[Mesh] OR Swine[Mesh] OR Sheep[Mesh] OR Goats[Mesh] OR Horses[Mesh] OR (farm animal*[tiab] OR farmed animal*[tiab] OR livestock[tiab] OR poultry[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR swine[tiab] OR pig[tiab] OR pigs[tiab] OR porcine[tiab] OR sheep[tiab] OR ovine[tiab] OR goat[tiab] OR goats[tiab] OR caprine[tiab] OR horse[tiab] OR horses[tiab] OR equine[tiab] OR chicken*[tiab] OR turkey[tiab] OR turkeys[tiab] OR duck[tiab] OR ducks[tiab] OR geese[tiab] OR goose[tiab] OR buffalo[tiab] OR rabbit*[tiab] OR camel*[tiab] OR alpaca*[tiab]) OR Aquaculture[Mesh] OR fish*[tiab] OR aquacultur*[tiab] OR eel[tiab] OR salmon*[tiab] OR trout*[tiab] OR shrimp*[tiab] OR prawn*[tiab] OR mussel*[tiab] OR oyster*[tiab] OR carp*[tiab] OR tilapia*[tiab] OR catfish[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 17 | 17 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Farm animals/livestock | 1 | `Animals[Mesh] OR animal*[tiab]` | 1,196 | 1/30 |
| Farm animals/livestock | 2 | `Animals[Mesh] OR animal*[tiab]` | 1,156 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| virus_metagenomics | 1,745,651 | 0 |
| farm_animals | 2,347 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 263 | initial | none | Initial recall-first strategy from the question; MeSH plus text words. No known relevant records were supplied. Added farm animal species terms because farm animal is a category; excluded Virome MeSH because it was introduced after the cutoff. |
| 2 | 0 | farm_animals: +13 / -0 | none | Expanded farm_animals block after category probe 1 found a relevant metagenomic study of farmed eel (PMID 25688234); added Aquaculture MeSH and farmed aquatic species words. |
| 3 | 318 | farm_animals: +13 / -0 | none | Corrected the too-short eel truncation to the singular literal after lint flagged it; aquatic animal vocabulary otherwise unchanged. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (Fresh-context internal critic reviewed packet-1.md only.): 1 findings; F1 must-fix open
- Round 2 on version 3 (Fresh-context internal critic reviewed packet-2.md only.): 1 findings; F1 must-fix rejected
- Round 3 on version 3 (Fresh-context closing critic reviewed packet-3.md only.): 1 findings; F1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 427 NCBI requests logged (100 from cache); strategy sha256 31e147f3d87f._

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
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "checked_at": "2026-09-29T03:46:40+00:00",
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
        "text": "Viruses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "Animals, Domestic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "Livestock",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "Poultry",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "Cattle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "Swine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "Sheep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "Goats",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Horses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Aquaculture",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:40+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "Aquaculture",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "((\"metagenomics\"[MeSH Terms] AND \"viruses\"[MeSH Terms]) OR (\"metagenom*\"[Title/Abstract] AND (\"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract])) OR \"virom*\"[Title/Abstract]) AND (\"animals, domestic\"[MeSH Terms] OR \"livestock\"[MeSH Terms] OR \"poultry\"[MeSH Terms] OR \"cattle\"[MeSH Terms] OR \"swine\"[MeSH Terms] OR (\"sheep, domestic\"[MeSH Terms] OR \"sheep\"[MeSH Terms]) OR \"goats\"[MeSH Terms] OR \"horses\"[MeSH Terms] OR (\"farm animal*\"[Title/Abstract] OR \"farmed animal*\"[Title/Abstract] OR \"livestock\"[Title/Abstract] OR \"poultry\"[Title/Abstract] OR \"cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"swine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"goat\"[Title/Abstract] OR \"goats\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"horse\"[Title/Abstract] OR \"horses\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"turkeys\"[Title/Abstract] OR \"duck\"[Title/Abstract] OR \"ducks\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"buffalo\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"camel*\"[Title/Abstract] OR \"alpaca*\"[Title/Abstract]) OR \"aquaculture\"[MeSH Terms] OR \"fish*\"[Title/Abstract] OR \"aquacultur*\"[Title/Abstract] OR \"eel\"[Title/Abstract] OR \"salmon*\"[Title/Abstract] OR \"trout*\"[Title/Abstract] OR \"shrimp*\"[Title/Abstract] OR \"prawn*\"[Title/Abstract] OR \"mussel*\"[Title/Abstract] OR \"oyster*\"[Title/Abstract] OR \"carp*\"[Title/Abstract] OR \"tilapia*\"[Title/Abstract] OR \"catfish\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "c9415fe287091240c1291336690243e5b6d3002862b866f6b52b36443fd2ccc6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The concepts are represented with MeSH and text words, and the listed livestock, poultry, and aquatic animal groups have direct terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks are combined with OR internally and AND across concepts, consistent with the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included MeSH headings are relevant to viral metagenomics and domestic or farm animal populations."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover metagenomic and viromic terminology and a range of named livestock, poultry, and aquatic animal groups."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query is syntactically coherent and has no reported PubMed diagnostics."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The required Entrez cutoff is explicit in protocol.as_of and PSB_AS_OF; it is the user's harness date condition, not a publication-date filter."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The complete query restricts Entrez date to 1800/01/01 through 2019-02-22, although the protocol declares no limits and the question gives no date boundary.",
          "recommendation": "Remove the upper bound or document and justify an explicitly intended cutoff.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": [],
      "note": "Fresh-context internal critic reviewed packet-1.md only."
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "c9415fe287091240c1291336690243e5b6d3002862b866f6b52b36443fd2ccc6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search represents metagenomic and viromic terminology and covers the population groups named in the eligibility criteria with direct headings or text words."
        },
        "operators": {
          "verdict": "pass",
          "note": "The virus-metagenomics and farm-animal terms are combined with OR within concepts and AND across the two required concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH headings cover metagenomics, viruses, domestic animals, livestock, poultry, named livestock groups, and aquaculture."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover metagenomic and viromic terminology, named terrestrial farm-animal groups, and farmed aquatic animal terminology and species."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query is coherently grouped, has no reported PubMed errors or warnings, and the recorded translation issues list is empty."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date boundary is explicitly documented as the requested as-of retrieval condition; the packet states that no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The complete query restricts Entrez date to 1800/01/01 through 2019-02-22, although the protocol declares no limits and the question gives no date boundary.",
          "recommendation": "Remove the upper bound or document and justify an explicitly intended cutoff.",
          "status": "rejected",
          "response": "Rejected based on the packet evidence: protocol.as_of is 2019-02-22, and the notes explicitly identify this as the user's Entrez retrieval cutoff through PSB_AS_OF while stating that no publication-date limit is used. The filter therefore implements the documented retrieval snapshot, rather than an unsupported publication-date restriction."
        }
      ],
      "issue_dispositions": [],
      "note": "Fresh-context internal critic reviewed packet-2.md only."
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "c9415fe287091240c1291336690243e5b6d3002862b866f6b52b36443fd2ccc6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy covers viral metagenomic terminology and the terrestrial and aquatic farmed animal groups specified in the eligibility criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are combined with OR within concepts and the two required concepts with AND."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included headings represent metagenomics, viruses, domestic and livestock animals, poultry, named livestock groups, and aquaculture."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover metagenomic and viromic terminology and named terrestrial and aquatic animal groups."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query is coherently grouped and has no reported PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "F1 is rejected: the packet documents 2019-02-22 as the requested Entrez retrieval cutoff through PSB_AS_OF and states that no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The complete query restricts Entrez date to 1800/01/01 through 2019-02-22, although the protocol declares no limits and the question gives no date boundary.",
          "recommendation": "Remove the upper bound or document and justify an explicitly intended cutoff.",
          "status": "rejected",
          "response": "Rejected based on the packet evidence: protocol.as_of is 2019-02-22, and the notes identify this as the Entrez retrieval cutoff through PSB_AS_OF while stating that no publication-date limit is used. The filter implements the documented retrieval snapshot, rather than an unsupported publication-date restriction."
        }
      ],
      "issue_dispositions": [],
      "note": "Fresh-context closing critic reviewed packet-3.md only."
    }
  ]
}
```


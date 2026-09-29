# PubMed search strategy: audit

Generated 2026-09-29T19:08:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Virus metagenomics in farm animals
- Framework: Method + application context
- Scope confirmed by user: no (User cannot answer questions during this run and asked to proceed. Assumed farm animals means animals kept for agricultural production, including livestock and poultry, with species-level records eligible even if they do not use the phrase farm animal. Included virus discovery, characterization, and surveillance studies that use metagenomic methods on farm-animal samples. Excluded wildlife and companion-animal-only studies, human-only studies, nonviral-only studies, and conventional single-virus studies without metagenomics. This is a method-plus-application-context question; viral target and farm-animal context are required concepts. No language or publication-date limits. PSB_AS_OF pins the Entrez-date cutoff to 2019-02-22; no publication-date limit is applied. Scope was not user-confirmed. Farmed aquatic species were not included in this run; the population assumption is terrestrial agricultural animals (livestock and poultry).)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Metagenomic analysis or sequencing | search | The method defines the topic and is named in titles, abstracts, or indexing; records may use metagenomics, metagenomic sequencing, or virome terminology. |
| Viruses studied through metagenomics | search | Viral targets define the review; papers may name only a viral family or specific virus, so this is probed as a category. |
| Farmed or livestock animals | search | Animal production context defines the review; authors may name only species (for example cattle, pigs, poultry, sheep, or goats), so this is probed as a category. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T19:06:47+00:00
- Records added to PubMed up to: 2019-02-22
- Total records: 5,924
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Metagenomics[Mesh]` | 5,229 | none |
| 2 | `Metagenome[Mesh]` | 5,897 | none |
| 3 | `Genomics[Mesh]` | 105,464 | none |
| 4 | `High-Throughput Nucleotide Sequencing[Mesh]` | 28,190 | none |
| 5 | `Sequence Analysis, DNA[Mesh]` | 222,713 | none |
| 6 | `metagenom*[tiab]` | 11,213 | none |
| 7 | `metagenome*[tiab]` | 3,784 | none |
| 8 | `virom*[tiab]` | 824 | none |
| 9 | `next generation sequenc*[tiab]` | 27,343 | none |
| 10 | `high-throughput sequencing[tiab]` | 10,541 | none |
| 11 | `deep sequenc*[tiab]` | 6,739 | none |
| 12 | `shotgun sequenc*[tiab]` | 1,538 | none |
| 13 | `unbiased sequenc*[tiab]` | 51 | none |
| 14 | `massively parallel sequenc*[tiab]` | 1,761 | none |
| 15 | `sequence-independent amplification[tiab]` | 65 | none |
| 16 | `SISPA[tiab]` | 43 | none |
| 17 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16` | 365,202 | none |
| 18 | `Viruses[Mesh]` | 759,255 | none |
| 19 | `virus*[tiab]` | 687,406 | none |
| 20 | `viral[tiab]` | 333,289 | none |
| 21 | `virome*[tiab]` | 780 | none |
| 22 | `phage*[tiab]` | 48,158 | none |
| 23 | `bacteriophage*[tiab]` | 34,910 | none |
| 24 | `Genome, Viral[Mesh]` | 58,113 | none |
| 25 | `DNA, Viral[Mesh]` | 87,180 | none |
| 26 | `#18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 1,097,509 | none |
| 27 | `Livestock[Mesh]` | 3,200 | none |
| 28 | `Poultry[Mesh]` | 147,415 | none |
| 29 | `Cattle[Mesh]` | 341,776 | none |
| 30 | `Swine[Mesh]` | 214,731 | none |
| 31 | `Sheep[Mesh]` | 116,801 | none |
| 32 | `Goats[Mesh]` | 30,623 | none |
| 33 | `Horses[Mesh]` | 67,676 | none |
| 34 | `Animals, Domestic[Mesh]` | 34,427 | none |
| 35 | `livestock[tiab]` | 21,337 | none |
| 36 | `farm animal*[tiab]` | 3,666 | none |
| 37 | `farmed animal*[tiab]` | 195 | none |
| 38 | `food animal*[tiab]` | 2,071 | none |
| 39 | `production animal*[tiab]` | 410 | none |
| 40 | `cattle[tiab]` | 79,355 | none |
| 41 | `bovine[tiab]` | 189,144 | none |
| 42 | `cow[tiab]` | 29,456 | none |
| 43 | `cows[tiab]` | 45,341 | none |
| 44 | `calf[tiab]` | 43,460 | none |
| 45 | `calves[tiab]` | 24,854 | none |
| 46 | `swine[tiab]` | 42,358 | none |
| 47 | `porcine[tiab]` | 79,145 | none |
| 48 | `pig[tiab]` | 127,282 | none |
| 49 | `pigs[tiab]` | 115,325 | none |
| 50 | `sheep[tiab]` | 87,044 | none |
| 51 | `ovine[tiab]` | 20,361 | none |
| 52 | `lamb*[tiab]` | 85,381 | none |
| 53 | `goat*[tiab]` | 31,547 | none |
| 54 | `caprine[tiab]` | 3,127 | none |
| 55 | `poultry[tiab]` | 25,731 | none |
| 56 | `chicken*[tiab]` | 92,941 | none |
| 57 | `broiler*[tiab]` | 16,896 | none |
| 58 | `turkey[tiab]` | 32,530 | none |
| 59 | `duck*[tiab]` | 13,075 | none |
| 60 | `goose[tiab]` | 2,645 | none |
| 61 | `geese[tiab]` | 1,928 | none |
| 62 | `horse*[tiab]` | 80,001 | none |
| 63 | `equine[tiab]` | 28,777 | none |
| 64 | `buffalo*[tiab]` | 10,572 | none |
| 65 | `camel*[tiab]` | 9,598 | none |
| 66 | `rabbit*[tiab]` | 252,771 | none |
| 67 | `yak[tiab]` | 730 | none |
| 68 | `yaks[tiab]` | 398 | none |
| 69 | `alpaca*[tiab]` | 1,132 | none |
| 70 | `llama*[tiab]` | 1,459 | none |
| 71 | `donkey[tiab]` | 1,368 | none |
| 72 | `donkeys[tiab]` | 1,152 | none |
| 73 | `mule*[tiab]` | 1,614 | none |
| 74 | `bison*[tiab]` | 1,162 | none |
| 75 | `deer[tiab]` | 10,365 | none |
| 76 | `cervid*[tiab]` | 1,274 | none |
| 77 | `reindeer[tiab]` | 1,432 | none |
| 78 | `#27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77` | 1,523,109 | none |
| 79 | `#17 AND #26 AND #78` | 5,924 | none |

### Strategy (single line, for copying into PubMed)

```text
((Metagenomics[Mesh] OR Metagenome[Mesh] OR Genomics[Mesh] OR High-Throughput Nucleotide Sequencing[Mesh] OR Sequence Analysis, DNA[Mesh] OR metagenom*[tiab] OR metagenome*[tiab] OR virom*[tiab] OR next generation sequenc*[tiab] OR high-throughput sequencing[tiab] OR deep sequenc*[tiab] OR shotgun sequenc*[tiab] OR unbiased sequenc*[tiab] OR massively parallel sequenc*[tiab] OR sequence-independent amplification[tiab] OR SISPA[tiab]) AND (Viruses[Mesh] OR virus*[tiab] OR viral[tiab] OR virome*[tiab] OR phage*[tiab] OR bacteriophage*[tiab] OR Genome, Viral[Mesh] OR DNA, Viral[Mesh]) AND (Livestock[Mesh] OR Poultry[Mesh] OR Cattle[Mesh] OR Swine[Mesh] OR Sheep[Mesh] OR Goats[Mesh] OR Horses[Mesh] OR Animals, Domestic[Mesh] OR livestock[tiab] OR farm animal*[tiab] OR farmed animal*[tiab] OR food animal*[tiab] OR production animal*[tiab] OR cattle[tiab] OR bovine[tiab] OR cow[tiab] OR cows[tiab] OR calf[tiab] OR calves[tiab] OR swine[tiab] OR porcine[tiab] OR pig[tiab] OR pigs[tiab] OR sheep[tiab] OR ovine[tiab] OR lamb*[tiab] OR goat*[tiab] OR caprine[tiab] OR poultry[tiab] OR chicken*[tiab] OR broiler*[tiab] OR turkey[tiab] OR duck*[tiab] OR goose[tiab] OR geese[tiab] OR horse*[tiab] OR equine[tiab] OR buffalo*[tiab] OR camel*[tiab] OR rabbit*[tiab] OR yak[tiab] OR yaks[tiab] OR alpaca*[tiab] OR llama*[tiab] OR donkey[tiab] OR donkeys[tiab] OR mule*[tiab] OR bison*[tiab] OR deer[tiab] OR cervid*[tiab] OR reindeer[tiab])) AND ("1800/01/01"[edat] : "2019/02/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 15 | 15 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Viruses studied through metagenomics | 1 | `metagenom*[tiab] OR Metagenome[Mesh]` | 762 | 0/30 |
| Viruses studied through metagenomics | 2 | `metagenom*[tiab] OR Metagenome[Mesh]` | 773 | 0/30 |
| Farmed or livestock animals | 1 | `Animals[Mesh] OR animal*[tiab] OR mammal*[tiab] OR vertebrat*[tiab]` | 22,398 | 0/30 |
| Farmed or livestock animals | 2 | `Animals[Mesh] OR animal*[tiab] OR mammal*[tiab] OR vertebrat*[tiab]` | 22,517 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| metagenomics | 134,092 | 0 |
| viruses | 24,752 | 0 |
| farm_animals | 35,563 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial three-block strategy; broad free-text and MeSH layers, developed from screened pilot records and MeSH lookups. |
| 2 | 5,861 | farm_animals: +4 / -2 | none | Fix invalid short truncations for cow and pig; retain explicit singular/plural variants. |
| 3 | 5,870 | viruses: +2 / -0 | none | Add Genome, Viral and DNA, Viral MeSH terms supported by development records; state explicitly that farmed aquatic species are outside the assumed terrestrial population scope. |
| 4 | 5,924 | metagenomics: +0 / -1; farm_animals: +11 / -0 | none | Round 1 critic changes: add common farmed species terms (yaks, alpacas/llamas, donkeys/mules, bison and farmed deer); remove the duplicated next-generation sequencing variant because PubMed translated both spellings identically. |
| 5 | 5,924 | metagenomics: +0 / -1 | none | Remove the remaining redundant sequencing spelling: PubMed translates high-throughput sequencing and high throughput sequencing identically. Re-evaluate on 15 development and 9 newly held-out records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5 (Same-context critic: no fresh-context reviewer was available; reviewed only critic/packet-1.md.): 1 findings; R1-aquatic-boundary document accepted-risk
- Round 2 on version 5 (Same-context critic: no fresh-context reviewer was available; reviewed only critic/packet-2.md.): 1 findings; R1-aquatic-boundary document accepted-risk
- Round 3 on version 5 (Same-context closing review: verified prior dispositions using only critic/packet-3.md; no fresh-context reviewer was available.): 1 findings; R1-aquatic-boundary document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1527 NCBI requests logged (789 from cache); strategy sha256 781a4b466e49._

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
        "location": "concept:viruses",
        "blocking": false,
        "requires_review": true,
        "id": "I-cd8ea44514bc0d83b158"
      },
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
        "location": "concept:viruses",
        "blocking": false,
        "requires_review": true,
        "id": "I-cd8ea44514bc0d83b158"
      },
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
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "requested": "Metagenome",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Metagenome",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Genomics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "Genomics",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "High-Throughput Nucleotide Sequencing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "High-Throughput Nucleotide Sequencing",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sequence Analysis, DNA",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "Sequence Analysis, DNA",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Viruses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "Viruses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Genome, Viral",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "Genome, Viral",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "DNA, Viral",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "DNA, Viral",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Livestock",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Livestock",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Poultry",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "Poultry",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cattle",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "Cattle",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Swine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Swine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Sheep",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Sheep",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Goats",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Goats",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Horses",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "Horses",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Animals, Domestic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:06:47+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Animals, Domestic",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"metagenomics\"[MeSH Terms] OR \"metagenome\"[MeSH Terms] OR \"genomics\"[MeSH Terms] OR \"high throughput nucleotide sequencing\"[MeSH Terms] OR \"sequence analysis, dna\"[MeSH Terms] OR \"metagenom*\"[Title/Abstract] OR \"metagenome*\"[Title/Abstract] OR \"virom*\"[Title/Abstract] OR \"next generation sequenc*\"[Title/Abstract] OR \"high throughput sequencing\"[Title/Abstract] OR \"deep sequenc*\"[Title/Abstract] OR \"shotgun sequenc*\"[Title/Abstract] OR \"unbiased sequenc*\"[Title/Abstract] OR \"massively parallel sequenc*\"[Title/Abstract] OR \"sequence independent amplification\"[Title/Abstract] OR \"SISPA\"[Title/Abstract]) AND (\"viruses\"[MeSH Terms] OR \"virus*\"[Title/Abstract] OR \"viral\"[Title/Abstract] OR \"virome*\"[Title/Abstract] OR \"phage*\"[Title/Abstract] OR \"bacteriophage*\"[Title/Abstract] OR \"genome, viral\"[MeSH Terms] OR \"dna, viral\"[MeSH Terms]) AND (\"livestock\"[MeSH Terms] OR \"poultry\"[MeSH Terms] OR \"cattle\"[MeSH Terms] OR \"swine\"[MeSH Terms] OR (\"sheep, domestic\"[MeSH Terms] OR \"sheep\"[MeSH Terms]) OR \"goats\"[MeSH Terms] OR \"horses\"[MeSH Terms] OR \"animals, domestic\"[MeSH Terms] OR \"livestock\"[Title/Abstract] OR \"farm animal*\"[Title/Abstract] OR \"farmed animal*\"[Title/Abstract] OR \"food animal*\"[Title/Abstract] OR \"production animal*\"[Title/Abstract] OR \"cattle\"[Title/Abstract] OR \"bovine\"[Title/Abstract] OR \"cow\"[Title/Abstract] OR \"cows\"[Title/Abstract] OR \"calf\"[Title/Abstract] OR \"calves\"[Title/Abstract] OR \"swine\"[Title/Abstract] OR \"porcine\"[Title/Abstract] OR \"pig\"[Title/Abstract] OR \"pigs\"[Title/Abstract] OR \"sheep\"[Title/Abstract] OR \"ovine\"[Title/Abstract] OR \"lamb*\"[Title/Abstract] OR \"goat*\"[Title/Abstract] OR \"caprine\"[Title/Abstract] OR \"poultry\"[Title/Abstract] OR \"chicken*\"[Title/Abstract] OR \"broiler*\"[Title/Abstract] OR \"turkey\"[Title/Abstract] OR \"duck*\"[Title/Abstract] OR \"goose\"[Title/Abstract] OR \"geese\"[Title/Abstract] OR \"horse*\"[Title/Abstract] OR \"equine\"[Title/Abstract] OR \"buffalo*\"[Title/Abstract] OR \"camel*\"[Title/Abstract] OR \"rabbit*\"[Title/Abstract] OR \"yak\"[Title/Abstract] OR \"yaks\"[Title/Abstract] OR \"alpaca*\"[Title/Abstract] OR \"llama*\"[Title/Abstract] OR \"donkey\"[Title/Abstract] OR \"donkeys\"[Title/Abstract] OR \"mule*\"[Title/Abstract] OR \"bison*\"[Title/Abstract] OR \"deer\"[Title/Abstract] OR \"cervid*\"[Title/Abstract] OR \"reindeer\"[Title/Abstract]) AND 1800/01/01:2019/02/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "df116a87ce5cca3567d702ec4f6cbf901e0d621a54976874f86c5ba5aebaf628",
      "note": "Same-context critic: no fresh-context reviewer was available; reviewed only critic/packet-1.md.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The method, viral target, and terrestrial farm-animal context are separately searched; assumptions are explicit."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR joins synonyms within blocks and AND joins the three required concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Every searched concept has validated MeSH and free-text layers; the evaluation reports no authority or translation blockers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy covers major farm-animal species and common sequencing/metagenomics expressions without unsupported short truncations."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current lint and translation checks report no syntax issues or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, or design filter is used; the effective cutoff is Entrez date via PSB_AS_OF."
        }
      },
      "findings": [
        {
          "id": "R1-aquatic-boundary",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The short question could include farmed aquatic animals; this run assumes terrestrial agricultural animals, including livestock and poultry.",
          "recommendation": "Keep this boundary visible for human review; expand the population block if the protocol includes aquaculture species.",
          "status": "accepted-risk",
          "response": "The user could not answer questions during this run and asked to proceed with documented assumptions. The protocol explicitly states the terrestrial farm-animal scope and excludes farmed aquatic species."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-cd8ea44514bc0d83b158",
          "status": "accepted-risk",
          "response": "The virus-category block changed only by removing a duplicate sequencing spelling from the separate method block; the removed high-throughput form had the same PubMed translation and count as the retained form. The two virus category probes were both screened clean (0/30 each), and no known record is lost.",
          "evidence": "The latest evaluation reports this stale-probe review issue, retains a count of 5,924, reports 100% relative recall on 15 development and 9 held-out records, and shows two earlier clean virus probes with 0/30 relevant records each. Both spellings had the same line count and translation in the prior evaluation."
        },
        {
          "issue_id": "I-0b3f5bccffad386dd2e7",
          "status": "accepted-risk",
          "response": "The farm-animal block was expanded with species terms after two clean probes, and a redundant method spelling was removed. The probe budget is exhausted, so freshness could not be re-established; adding terms broadens the farm-animal block, while the removed method spelling had an identical PubMed translation. This remains a human-review limitation.",
          "evidence": "The latest evaluation reports this stale-probe review issue, 0/30 relevant in each of the two earlier farm-animal probes, no known losses, and current 100% relative recall for both sets (15 development, 9 validation). The final query count is 5,924."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "df116a87ce5cca3567d702ec4f6cbf901e0d621a54976874f86c5ba5aebaf628",
      "note": "Same-context critic: no fresh-context reviewer was available; reviewed only critic/packet-2.md.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three blocks correspond to the method, viral target, and terrestrial agricultural population. The aquatic boundary is documented."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query has OR synonym blocks joined with AND and contains no NOT or proximity operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The current packet shows MeSH and title/abstract terms for each concept, with no live authority blockers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Farm-animal species coverage is broad and the redundant normalized sequencing terms have been removed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax, field, truncation, or phrase warnings remain in the current evaluation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No ad hoc limits or publication-date restriction are used; PSB_AS_OF supplies the Entrez cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-aquatic-boundary",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The short question could include farmed aquatic animals; this run assumes terrestrial agricultural animals, including livestock and poultry.",
          "recommendation": "Keep this boundary visible for human review; expand the population block if the protocol includes aquaculture species.",
          "status": "accepted-risk",
          "response": "The user could not answer questions during this run and asked to proceed with documented assumptions. The protocol explicitly states the terrestrial farm-animal scope and excludes farmed aquatic species."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-cd8ea44514bc0d83b158",
          "status": "accepted-risk",
          "response": "The virus-category block is stale only because one of two identically translated high-throughput sequencing spellings was removed from the method block. Both earlier virus probes were clean (0/30 relevant), and all 24 known records are currently retrieved.",
          "evidence": "The current evaluation reports a stale-probe review issue, two earlier virus probes with 0/30 relevant each, no known losses, 15 development records plus 9 held-out records at 100% relative recall, and final count 5,924. Prior line checks showed identical PubMed translations for both spellings."
        },
        {
          "issue_id": "I-0b3f5bccffad386dd2e7",
          "status": "accepted-risk",
          "response": "The farm-animal block only gained additional species terms after two clean samples; a duplicate method spelling was also removed. The probe budget is exhausted, so the latest category query could not be freshly sampled. This remains an explicit limitation for human review.",
          "evidence": "The current evaluation reports a stale-probe review issue, two earlier farm-animal probes with 0/30 relevant each, no known losses, 15 development records plus 9 held-out records at 100% relative recall, and final count 5,924."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "df116a87ce5cca3567d702ec4f6cbf901e0d621a54976874f86c5ba5aebaf628",
      "note": "Same-context closing review: verified prior dispositions using only critic/packet-3.md; no fresh-context reviewer was available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The scope assumptions and aquatic-species boundary are explicit and carried as a documented risk."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final AND/OR construction remains appropriate for the three topic concepts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The current validation confirms the vocabulary with no technical heading blockers."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy contains broad method, viral, and farm-animal text terms; revisions were fully evaluated."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax, field, phrase, or truncation issue is reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit was added; the entry-date bound is provided by PSB_AS_OF."
        }
      },
      "findings": [
        {
          "id": "R1-aquatic-boundary",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "block": "farm_animals",
          "finding": "The short question could include farmed aquatic animals; this run assumes terrestrial agricultural animals, including livestock and poultry.",
          "recommendation": "Keep this boundary visible for human review; expand the population block if the protocol includes aquaculture species.",
          "status": "accepted-risk",
          "response": "The user could not answer questions during this run and asked to proceed with documented assumptions. The protocol explicitly states the terrestrial farm-animal scope and excludes farmed aquatic species."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-cd8ea44514bc0d83b158",
          "status": "accepted-risk",
          "response": "The virus probe became technically stale because the duplicate high-throughput method spelling was removed. The removed term and retained term had identical PubMed translations and counts. Two earlier clean virus probes remain the supporting evidence; no known record was lost.",
          "evidence": "The latest evaluation reports this review issue, two prior virus probes at 0/30 relevant each, and 100% relative recall for 15 development plus 9 held-out records. It reports final count 5,924."
        },
        {
          "issue_id": "I-0b3f5bccffad386dd2e7",
          "status": "accepted-risk",
          "response": "The farm-animal block gained species terms after two clean samples; later method-term cleanup also changed the base query. The standard probe budget is exhausted, so freshness was not re-established. Treat this as a human-review limitation.",
          "evidence": "The latest evaluation reports this review issue, two prior farm-animal probes at 0/30 relevant each, and 100% relative recall for 15 development plus 9 held-out records. It reports final count 5,924."
        }
      ]
    }
  ]
}
```


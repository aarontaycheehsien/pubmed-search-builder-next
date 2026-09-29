# PubMed search strategy: audit

Generated 2026-09-28T21:38:00+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User requested no questions and asked for reasonable assumptions. Scope confirmation waived. No known relevant articles supplied. Assumed standard-depth workload budget (10,000). 'Common therapies' operationalized as D-penicillamine, trientine, zinc salts, and tetrathiomolybdate; comparative designs/outcomes and the exact comparator are screened rather than searched. Searches limited by PubMed entry date through 2018-12-23 via PSB_AS_OF; no publication-date limit. A PubMed similar-articles search from a 2009 systematic review yielded screened treatment-outcome records. A generic-treatment category probe identified PMID 11477856 as a potentially eligible regional regimen using unithiol and Gandou tablet; the therapy candidate will be widened. Review reference lists were not returned by psb neighbors.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The disease is the population-defining condition and is consistently named or indexed. |
| Common pharmacologic therapies for Wilson disease | optional | Therapy defines the topic, but treatment names vary and may be secondary in records; test its retrieval and loss before deciding whether to AND it. |
| Comparative intervention or comparator | screen | Comparators and direct comparative design may not be described consistently in titles, abstracts, or indexing. |
| Clinical effectiveness and harms | screen | Outcomes vary and are inconsistently named; assess at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:37:11+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 1,916
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Hepatolenticular Degeneration[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab]` | 5,545 | none |
| 3 | `wilson disease*[tiab]` | 5,584 | none |
| 4 | `"hepatolenticular degeneration"[tiab]` | 946 | none |
| 5 | `"progressive lenticular degeneration"[tiab]` | 10 | none |
| 6 | `"copper storage disease"[tiab]` | 25 | none |
| 7 | `Kinnier-Wilson[tiab]` | 38 | none |
| 8 | `Westphal-Strumpell[tiab]` | 26 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 7,280 | none |
| 10 | `Penicillamine[Mesh]` | 7,878 | none |
| 11 | `Trientine[Mesh]` | 380 | none |
| 12 | `Zinc Acetate[Mesh]` | 246 | none |
| 13 | `tetrathiomolybdate[nm]` | 293 | none |
| 14 | `penicillamine[tiab]` | 6,853 | none |
| 15 | `D-penicillamine[tiab]` | 3,268 | none |
| 16 | `trientine[tiab]` | 219 | none |
| 17 | `triethylenetetramine[tiab]` | 360 | none |
| 18 | `zinc[tiab]` | 108,490 | none |
| 19 | `zinc acetate[tiab]` | 817 | none |
| 20 | `zinc sulphate[tiab]` | 857 | none |
| 21 | `zinc salt*[tiab]` | 513 | none |
| 22 | `tetrathiomolybdate[tiab]` | 351 | none |
| 23 | `ammonium tetrathiomolybdate[tiab]` | 84 | none |
| 24 | `unithiol[tiab]` | 216 | none |
| 25 | `sodium dimercaptosuccinate[tiab]` | 11 | none |
| 26 | `sodium dimercaptopropanesulfonate[tiab]` | 5 | none |
| 27 | `dimercaprol[tiab]` | 623 | none |
| 28 | `Gandou[tiab]` | 14 | none |
| 29 | `Gandou tablet*[tiab]` | 5 | none |
| 30 | `Gandou decoction[tiab]` | 6 | none |
| 31 | `traditional Chinese medicine[tiab]` | 16,170 | none |
| 32 | `Chinese herbal medicine[tiab]` | 3,257 | none |
| 33 | `chelating agent*[tiab]` | 7,766 | none |
| 34 | `copper chelation[tiab]` | 197 | none |
| 35 | `copper-chelating[tiab]` | 323 | none |
| 36 | `anticopper[tiab]` | 79 | none |
| 37 | `decoppering[tiab]` | 61 | none |
| 38 | `Zinc[Mesh]` | 58,485 | none |
| 39 | `Zinc Sulfate[Mesh]` | 1,802 | none |
| 40 | `ZnSO4[tiab]` | 1,392 | none |
| 41 | `Dimercaprol[Mesh]` | 2,156 | none |
| 42 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41` | 166,070 | none |
| 43 | `#9 AND #42` | 1,916 | none |

### Strategy (single line, for copying into PubMed)

```text
((Hepatolenticular Degeneration[Mesh] OR "Wilson disease"[tiab] OR wilson disease*[tiab] OR "hepatolenticular degeneration"[tiab] OR "progressive lenticular degeneration"[tiab] OR "copper storage disease"[tiab] OR Kinnier-Wilson[tiab] OR Westphal-Strumpell[tiab]) AND (Penicillamine[Mesh] OR Trientine[Mesh] OR Zinc Acetate[Mesh] OR tetrathiomolybdate[nm] OR penicillamine[tiab] OR D-penicillamine[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR zinc acetate[tiab] OR zinc sulphate[tiab] OR zinc salt*[tiab] OR tetrathiomolybdate[tiab] OR ammonium tetrathiomolybdate[tiab] OR unithiol[tiab] OR sodium dimercaptosuccinate[tiab] OR sodium dimercaptopropanesulfonate[tiab] OR dimercaprol[tiab] OR Gandou[tiab] OR Gandou tablet*[tiab] OR Gandou decoction[tiab] OR traditional Chinese medicine[tiab] OR Chinese herbal medicine[tiab] OR chelating agent*[tiab] OR copper chelation[tiab] OR copper-chelating[tiab] OR anticopper[tiab] OR decoppering[tiab] OR Zinc[Mesh] OR Zinc Sulfate[Mesh] OR ZnSO4[tiab] OR Dimercaprol[Mesh])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |
| validation2 | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Common pharmacologic therapies for Wilson disease | AND-ed | 7,280 / 1,916 | 73.7% | none | 0/30 (up to 10% of removed records could be relevant) | Keep the therapy block AND-ed after the refreshed 30-record loss sample for the current version found no eligible pharmacologic treatment-outcome studies. The block still offers a material reduction; the known treatment-outcome set is fully retrieved. The sample included unrelated clinical Wilson papers and transplant studies, which are outside the stated pharmacologic-treatment scope. Earlier category probes found unithiol/Gandou, decoppering, and a historical BAL paper; the first two were added, and Dimercaprol MeSH was added for the BAL record. Residual category-probe uncertainty remains because the two-probe standard budget is spent. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Common pharmacologic therapies for Wilson disease | 1 | `treatment[tiab] OR treated[tiab] OR therapeutics[Mesh] OR drug therapy[sh]` | 1,476 | 1/30 |
| Common pharmacologic therapies for Wilson disease | 2 | `treatment[tiab] OR treated[tiab] OR therapeutics[Mesh] OR drug therapy[sh]` | 1,450 | 1/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 166,070 | 0 |
| therapy | 7,280 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 7,280 | initial | none | Initial disease-only block with tested optional named-therapy block; no user-supplied seeds. |
| 2 | 7,280 | wilson_disease: +4 / -4 | none | Widened therapy candidate with unithiol, sodium dimercaptosuccinate/DMPS, dimercaprol, Gandou, and Chinese herbal medicine after category probe; added 12 screened treatment-outcome studies and split four held-out validation records. |
| 3 | 7,280 | limits/combination | none | Added decoppering and broad chelation vocabulary after the second therapy category probe identified a longitudinal outcome study outside the member-only candidate. Probe budget exhausted; remaining category risk will be documented for the critic. |
| 4 | 7,280 | limits/combination | none | Added zinc and zinc sulfate MeSH plus ZnSO4 after an optional-loss sample surfaced a human treatment study indexed under zinc sulfate; split newly accumulated development records to keep additional records held out. |
| 5 | 1,959 | therapy: +34 / -0 | none | ANDed the therapy block after measured optional evaluation and refreshed loss sample; first version of the two-block strategy. |
| 6 | 1,904 | therapy: +0 / -3 | none | Removed the ambiguous broad Chelating Agents authority match and duplicate zinc sulfate text term flagged by live validation; specific agent MeSH terms, Zinc/Zinc Sulfate MeSH, and broad chelation text remain. Re-evaluate optional decision and loss sample because the AND-ed therapy block changed. |
| 7 | 1,916 | therapy: +1 / -0 | none | Added verified Dimercaprol MeSH after refreshed loss sample identified a historical human Wilson disease BAL treatment article; retained the text-name term and added the controlled heading to catch records without the generic drug name in text. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 7: 0 findings; 
- Round 2 on version 7: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 769 NCBI requests logged (342 from cache); strategy sha256 50d3b7f664a9._

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
        "location": "concept:therapy",
        "blocking": false,
        "requires_review": true,
        "id": "I-ab10832aa1d59d7ffa28"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:therapy",
        "blocking": false,
        "requires_review": true,
        "id": "I-ab10832aa1d59d7ffa28"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Hepatolenticular Degeneration",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006527",
          "name": "Hepatolenticular Degeneration",
          "type": "descriptor",
          "scope_note": "A rare autosomal recessive disease characterized by the deposition of copper in the BRAIN; LIVER; CORNEA; and other organs. It is caused by defects in the ATP7B gene encoding copper-transporting ATPase 2 (EC 3.6.3.4), also known as the Wilson disease protein. The overload of copper inevitably leads to progressive liver and neurological dysfunction such as LIVER CIRRHOSIS; TREMOR; ATAXIA and int...",
          "tree_numbers": [
            "C06.552.413",
            "C10.228.140.079.493",
            "C10.228.140.163.100.360",
            "C10.228.662.400",
            "C10.574.500.487",
            "C16.320.400.361",
            "C16.320.565.189.360",
            "C16.320.565.618.403",
            "C18.452.132.100.360",
            "C18.452.648.189.360",
            "C18.452.648.618.403"
          ],
          "entry_terms": 47,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006527",
      "preferred_label": "Hepatolenticular Degeneration",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Hepatolenticular Degeneration",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010396",
          "name": "Penicillamine",
          "type": "descriptor",
          "scope_note": "3-Mercapto-D-valine. The most characteristic degradation product of the penicillin antibiotics. It is used as an antirheumatic and as a chelating agent in Wilson's disease.",
          "tree_numbers": [
            "D02.886.030.786",
            "D12.125.166.786"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010396",
      "preferred_label": "Penicillamine",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "Penicillamine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014266",
          "name": "Trientine",
          "type": "descriptor",
          "scope_note": "An ethylenediamine derivative used as stabilizer for EPOXY RESINS, as ampholyte for ISOELECTRIC FOCUSING and as chelating agent for copper in HEPATOLENTICULAR DEGENERATION.",
          "tree_numbers": [
            "D02.092.782.258.368.880"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014266",
      "preferred_label": "Trientine",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "Trientine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019345",
          "name": "Zinc Acetate",
          "type": "descriptor",
          "scope_note": "A salt produced by the reaction of zinc oxide with acetic acid and used as an astringent, styptic, and emetic.",
          "tree_numbers": [
            "D02.241.081.018.165.750"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019345",
      "preferred_label": "Zinc Acetate",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "Zinc Acetate",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "tetrathiomolybdate",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C020809",
          "name": "tetrathiomolybdate",
          "type": "supplementary",
          "scope_note": "RN given refers to (MoS4)-2; chelates copper; inhibits CopB copper ATPase and cytokine proteins important for angiogenesis; structure",
          "tree_numbers": [
            "@14520"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C020809",
      "preferred_label": "tetrathiomolybdate",
      "type": "supplementary",
      "location": "vocabulary:12",
      "term": {
        "text": "tetrathiomolybdate",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "Zinc",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015032",
          "name": "Zinc",
          "type": "descriptor",
          "scope_note": "A metallic element of atomic number 30 and atomic weight 65.38. It is a necessary trace element in the diet, forming an essential part of many enzymes, and playing an important role in protein synthesis and in cell division. Zinc deficiency is associated with ANEMIA, short stature, HYPOGONADISM, impaired WOUND HEALING, and geophagia. It is known by the symbol Zn.",
          "tree_numbers": [
            "D01.268.556.940",
            "D01.268.956.906",
            "D01.552.544.940"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015032",
      "preferred_label": "Zinc",
      "type": "descriptor",
      "location": "vocabulary:37",
      "term": {
        "text": "Zinc",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Sulfate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019287",
          "name": "Zinc Sulfate",
          "type": "descriptor",
          "scope_note": "A compound given in the treatment of conditions associated with zinc deficiency such as acrodermatitis enteropathica. Externally, zinc sulfate is used as an astringent in lotions and eye drops. (Reynolds JEF(Ed): Martindale: The Extra Pharmacopoeia (electronic version). Micromedex, Inc, Englewood, CO, 1995)",
          "tree_numbers": [
            "D01.875.800.800.850.950",
            "D01.975.987"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019287",
      "preferred_label": "Zinc Sulfate",
      "type": "descriptor",
      "location": "vocabulary:38",
      "term": {
        "text": "Zinc Sulfate",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dimercaprol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:37:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004112",
          "name": "Dimercaprol",
          "type": "descriptor",
          "scope_note": "An anti-gas warfare agent that is effective against Lewisite (dichloro(2-chlorovinyl)arsine) and formerly known as British Anti-Lewisite or BAL. It acts as a chelating agent and is used in the treatment of arsenic, gold, and other heavy metal poisoning.",
          "tree_numbers": [
            "D02.886.489.180"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004112",
      "preferred_label": "Dimercaprol",
      "type": "descriptor",
      "location": "vocabulary:40",
      "term": {
        "text": "Dimercaprol",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"hepatolenticular degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"wilson disease*\"[Title/Abstract] OR \"hepatolenticular degeneration\"[Title/Abstract] OR \"progressive lenticular degeneration\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"Westphal-Strumpell\"[Title/Abstract]) AND (\"penicillamine\"[MeSH Terms] OR \"trientine\"[MeSH Terms] OR \"zinc acetate\"[MeSH Terms] OR \"tetrathiomolybdate\"[Supplementary Concept] OR \"penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"zinc salt*\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"unithiol\"[Title/Abstract] OR \"sodium dimercaptosuccinate\"[Title/Abstract] OR \"sodium dimercaptopropanesulfonate\"[Title/Abstract] OR \"dimercaprol\"[Title/Abstract] OR \"Gandou\"[Title/Abstract] OR \"gandou tablet*\"[Title/Abstract] OR \"gandou decoction\"[Title/Abstract] OR \"traditional chinese medicine\"[Title/Abstract] OR \"chinese herbal medicine\"[Title/Abstract] OR \"chelating agent*\"[Title/Abstract] OR \"copper chelation\"[Title/Abstract] OR \"copper-chelating\"[Title/Abstract] OR \"anticopper\"[Title/Abstract] OR \"decoppering\"[Title/Abstract] OR \"zinc\"[MeSH Terms] OR \"zinc sulfate\"[MeSH Terms] OR \"ZnSO4\"[Title/Abstract] OR \"dimercaprol\"[MeSH Terms]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 7,
      "review_sha256": "b5994dd3340760c4252d9df33a5af7a62b739c979389cfeb098a9aae09be0957",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Disease and named therapy concepts have bare-name coverage; no translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within blocks, AND combines disease and therapy, and comparator and outcome concepts remain for screening. The therapy block removes 73.7% of disease records; the current 30-record loss sample found 0 relevant records, while all 14 known records are retrieved. The sample still allows up to 10% of removed records to be relevant."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The disease and drug headings are verified in the packet and are paired with free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The therapy vocabulary covers named chelators, zinc, and regional regimens, including terms added after earlier category probes found eligible records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query translation is coherent, with no PubMed errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date limit matches the stated 2018-12-23 cutoff; no study-design or outcome filter is applied."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-ab10832aa1d59d7ffa28",
          "status": "accepted-risk",
          "response": "The staleness warning is valid and remains an acknowledged risk: the therapy block changed after the final category probe, and the two-probe budget is spent. The current version has a separate 30-record loss sample and retrieves all known records, supporting retention of the block while leaving uncertainty about unobserved eligible records.",
          "evidence": "Both earlier category probes found one eligible record in their 30-record samples. The packet reports that unithiol/Gandou, decoppering, and Dimercaprol MeSH were added in response. The current therapy-block loss sample screened 30 of 5,364 removed records and found none eligible; known-record retrieval is 14/14. The category probe history is marked stale, and the probe budget is 2/2."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 7,
      "review_sha256": "b5994dd3340760c4252d9df33a5af7a62b739c979389cfeb098a9aae09be0957",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Disease and named therapy concepts have bare-name coverage, and the packet reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within blocks, AND combines disease and therapy, and comparator and outcome concepts remain for screening. The therapy block reduces the disease set by 73.7%; the current loss sample found 0 relevant records, and all 14 known records are retrieved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The disease and drug headings are verified in the packet and paired with free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Therapy terms cover named chelators, zinc, and regional regimens, including terms added after earlier probes found eligible records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query translation is coherent, with no PubMed errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date limit matches the stated 2018-12-23 cutoff; no study-design or outcome filter is applied."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-ab10832aa1d59d7ffa28",
          "status": "accepted-risk",
          "response": "The staleness warning remains an acknowledged risk: the therapy block changed after the final category probe, and the two-probe budget is spent. The final strategy includes unithiol, Gandou, decoppering, and Dimercaprol MeSH, addressing the earlier probe findings. Residual uncertainty about unobserved eligible records remains accepted.",
          "evidence": "The two earlier category probes each found one eligible record in their 30-record samples. The final strategy includes unithiol and Gandou terms, decoppering, and Dimercaprol MeSH. The current therapy-block loss sample screened 30 of 5,364 removed records and found none eligible; known-record retrieval is 14/14. The category probe history is marked stale, and the probe budget is 2/2."
        }
      ]
    }
  ]
}
```


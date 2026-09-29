# PubMed search strategy: audit

Generated 2026-09-28T21:13:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: yes (User asked not to pause for clarification. Assumed common established pharmacologic therapies (chelators and zinc), while also retaining liver transplantation as a treatment option for severe disease; comparative benefit, treatment failure, and harms are screened. No known relevant articles were supplied. Harness requires PubMed records present by Entrez date 2018-12-23; no publication-date limit is used. A 2009 systematic review was found by a Wilson-disease MeSH systematic-review pilot; its PubMed reference-link lookup returned no candidate records, so no included-study benchmark set was available. Two precise pilots and category probes screened candidates within standard depth.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | Target condition; every eligible comparative treatment study must concern Wilson disease and the condition has a stable indexed name. |
| Wilson disease therapies | search | Intervention is central to comparative effectiveness; records may name a therapy member (e.g., chelator or zinc) without saying treatment in generic terms. |
| Therapy comparators | screen | Comparator is inconsistently named and handled more safely at screening. |
| Comparative effectiveness outcomes | screen | Comparative outcomes are inconsistently reported in titles and abstracts; screen for eligible outcome evidence. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:12:24+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 3,521
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `"Wilson Disease"[tiab]` | 5,545 | none |
| 3 | `"Wilson's Disease"[tiab]` | 4,158 | none |
| 4 | `"Wilsons Disease"[tiab]` | 4,135 | none |
| 5 | `"hepatolenticular degeneration"[tiab]` | 946 | none |
| 6 | `"progressive lenticular degeneration"[tiab]` | 10 | none |
| 7 | `"copper storage disease"[tiab]` | 25 | none |
| 8 | `"Kinnier-Wilson"[tiab]` | 38 | none |
| 9 | `"neurohepatic degeneration"[tiab]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 10 | `"hepatocerebral degeneration"[tiab]` | 142 | none |
| 11 | `"hepato-cerebral degeneration"[tiab]` | 10 | none |
| 12 | `pseudosclerosis[tiab]` | 55 | none |
| 13 | `"Westphal-Strumpell"[tiab]` | 26 | none |
| 14 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 7,337 | none |
| 15 | `"Drug Therapy"[Mesh]` | 1,305,324 | none |
| 16 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 17 | `"Trientine"[Mesh]` | 380 | none |
| 18 | `"Zinc Acetate"[Mesh]` | 246 | none |
| 19 | `"Liver Transplantation"[Mesh]` | 54,773 | none |
| 20 | `treat*[tiab]` | 5,019,714 | none |
| 21 | `therap*[tiab]` | 2,661,898 | none |
| 22 | `drug*[tiab]` | 1,523,320 | none |
| 23 | `pharmacotherap*[tiab]` | 32,759 | none |
| 24 | `chelati*[tiab]` | 32,153 | none |
| 25 | `penicillamine[tiab]` | 6,853 | none |
| 26 | `trientine[tiab]` | 219 | none |
| 27 | `triethylene tetramine[tiab]` | 74 | none |
| 28 | `zinc[tiab]` | 108,490 | none |
| 29 | `zinc acetate[tiab]` | 817 | none |
| 30 | `zinc sulfate[tiab]` | 1,531 | none |
| 31 | `tetrathiomolybdate[tiab]` | 351 | none |
| 32 | `ammonium tetrathiomolybdate[tiab]` | 84 | none |
| 33 | `liver transplant*[tiab]` | 55,108 | none |
| 34 | `hepatic transplant*[tiab]` | 1,078 | none |
| 35 | `"Zinc Sulfate"[Mesh]` | 1,802 | none |
| 36 | `"Dimercaprol"[Mesh]` | 2,156 | none |
| 37 | `zinc sulphate[tiab]` | 857 | none |
| 38 | `dimercaprol[tiab]` | 623 | none |
| 39 | `"British Anti-Lewisite"[tiab]` | 133 | none |
| 40 | `medication*[tiab]` | 283,168 | none |
| 41 | `intervention*[tiab]` | 865,515 | none |
| 42 | `management[tiab]` | 1,000,768 | none |
| 43 | `#15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42` | 8,559,975 | none |
| 44 | `#14 AND #43` | 3,521 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR "Wilson Disease"[tiab] OR "Wilson's Disease"[tiab] OR "Wilsons Disease"[tiab] OR "hepatolenticular degeneration"[tiab] OR "progressive lenticular degeneration"[tiab] OR "copper storage disease"[tiab] OR "Kinnier-Wilson"[tiab] OR "neurohepatic degeneration"[tiab] OR "hepatocerebral degeneration"[tiab] OR "hepato-cerebral degeneration"[tiab] OR pseudosclerosis[tiab] OR "Westphal-Strumpell"[tiab]) AND ("Drug Therapy"[Mesh] OR "Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc Acetate"[Mesh] OR "Liver Transplantation"[Mesh] OR treat*[tiab] OR therap*[tiab] OR drug*[tiab] OR pharmacotherap*[tiab] OR chelati*[tiab] OR penicillamine[tiab] OR trientine[tiab] OR triethylene tetramine[tiab] OR zinc[tiab] OR zinc acetate[tiab] OR zinc sulfate[tiab] OR tetrathiomolybdate[tiab] OR ammonium tetrathiomolybdate[tiab] OR liver transplant*[tiab] OR hepatic transplant*[tiab] OR "Zinc Sulfate"[Mesh] OR "Dimercaprol"[Mesh] OR zinc sulphate[tiab] OR dimercaprol[tiab] OR "British Anti-Lewisite"[tiab] OR medication*[tiab] OR intervention*[tiab] OR management[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Wilson disease therapies | 1 | `Hepatolenticular Degeneration[Mesh] OR Wilson Disease[tiab] OR Wilson's Disease[tiab]` | 3,817 | 0/30 |
| Wilson disease therapies | 2 | `treatment[tiab] OR drug*[tiab] OR medication*[tiab] OR intervention*[tiab] OR management[tiab] OR Treatment Outcome[Mesh]` | 12 | 0/12 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 8,559,975 | 0 |
| therapy | 7,337 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 3,434 | initial | none | Initial two-block PICO search with disease synonyms and broad plus established pharmacologic/transplant therapy vocabulary; comparator and outcomes screened. |
| 2 | 3,419 | therapy: +0 / -1 | none | Removed the Chelating Agents heading because authority verification was ambiguous; retained chelati* and named drug MeSH/free-text vocabulary. |
| 3 | 3,452 | wilson_disease: +5 / -0; therapy: +5 / -0 | none | Added specific MeSH and text-word synonyms from the condition heading and screened literature; added Zinc Sulfate and Dimercaprol for treatment-member coverage. |
| 4 | 3,521 | wilson_disease: +0 / -1; therapy: +3 / -0 | none | Replaced unsupported exact phrase with pseudosclerosis[tiab] and added medication/intervention/management wording; maintaining recall-first coverage. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4 (same-context critic: no fresh reviewer context was available under the active no-delegation instruction; reviewed the packet independently against all six PRESS domains.): 1 findings; f-limited-benchmark document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 804 NCBI requests logged (446 from cache); strategy sha256 0f556aaa47fd._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"neurohepatic degeneration\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:9",
        "blocking": false,
        "requires_review": true,
        "id": "I-3698fcf51ca8094ec5db"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"neurohepatic degeneration\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:9",
        "blocking": false,
        "requires_review": true,
        "id": "I-9817d0412b37bcfd49d0"
      }
    ],
    "issues": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"neurohepatic degeneration\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:9",
        "blocking": false,
        "requires_review": true,
        "id": "I-3698fcf51ca8094ec5db"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"neurohepatic degeneration\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:9",
        "blocking": false,
        "requires_review": true,
        "id": "I-9817d0412b37bcfd49d0"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Hepatolenticular Degeneration",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
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
        "text": "\"Hepatolenticular Degeneration\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Drug Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "Q000188",
          "name": "drug therapy",
          "type": "qualifier",
          "scope_note": "Used with disease headings for the treatment of disease by the administration of drugs, chemicals, and antibiotics. For diet therapy and radiotherapy, use specific subheadings. Excludes immunotherapy for which therapy is used.",
          "tree_numbers": [
            "Y11.020"
          ],
          "entry_terms": 3,
          "mapped_to": null
        },
        {
          "ui": "D004358",
          "name": "Drug Therapy",
          "type": "descriptor",
          "scope_note": "The use of DRUGS to treat a DISEASE or its symptoms. One example is the use of ANTINEOPLASTIC AGENTS to treat CANCER.",
          "tree_numbers": [
            "E02.319"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004358",
      "preferred_label": "Drug Therapy",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Drug Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Penicillamine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "\"Trientine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "\"Zinc Acetate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Liver Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016031",
          "name": "Liver Transplantation",
          "type": "descriptor",
          "scope_note": "The transference of a part of or an entire liver from one human or animal to another.",
          "tree_numbers": [
            "E02.095.147.725.490",
            "E04.210.650",
            "E04.936.450.490",
            "E04.936.580.490"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016031",
      "preferred_label": "Liver Transplantation",
      "type": "descriptor",
      "location": "vocabulary:18",
      "term": {
        "text": "\"Liver Transplantation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Sulfate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Zinc Sulfate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dimercaprol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:12:24+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"Dimercaprol\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson Disease\"[Title/Abstract] OR \"Wilson's Disease\"[Title/Abstract] OR \"Wilsons Disease\"[Title/Abstract] OR \"Hepatolenticular Degeneration\"[Title/Abstract] OR \"progressive lenticular degeneration\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"neurohepatic degeneration\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"hepato-cerebral degeneration\"[Title/Abstract] OR \"pseudosclerosis\"[Title/Abstract] OR \"Westphal-Strumpell\"[Title/Abstract]) AND (\"Drug Therapy\"[MeSH Terms] OR \"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Acetate\"[MeSH Terms] OR \"Liver Transplantation\"[MeSH Terms] OR \"treat*\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"drug*\"[Title/Abstract] OR \"pharmacotherap*\"[Title/Abstract] OR \"chelati*\"[Title/Abstract] OR \"Penicillamine\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylene tetramine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"Zinc Acetate\"[Title/Abstract] OR \"Zinc Sulfate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"liver transplant*\"[Title/Abstract] OR \"hepatic transplant*\"[Title/Abstract] OR \"Zinc Sulfate\"[MeSH Terms] OR \"Dimercaprol\"[MeSH Terms] OR \"zinc sulphate\"[Title/Abstract] OR \"Dimercaprol\"[Title/Abstract] OR \"British Anti-Lewisite\"[Title/Abstract] OR \"medication*\"[Title/Abstract] OR \"intervention*\"[Title/Abstract] OR \"management\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "be64e3c5e9f64aa8a3e7d43bae295d03d39faa715ca5c5ac097481cb88917234",
      "note": "same-context critic: no fresh reviewer context was available under the active no-delegation instruction; reviewed the packet independently against all six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The Wilson disease condition and therapies are required concepts. Comparators and outcomes are screened. The therapy category has two clean probes (0/30 and 0/12 eligible records outside the block). Scope assumptions are documented, including transplant as a severe-disease option."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines synonyms within each block and the two concepts are AND-ed. No NOT operators or proximity clauses are used in the delivered strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Hepatolenticular Degeneration descriptor is combined with title/abstract synonyms. Therapy coverage includes Drug Therapy and checked headings for penicillamine, trientine, zinc salts, dimercaprol and liver transplantation; exploded headings are used."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease layer includes Wilson, hepatolenticular and related historical names. The treatment layer includes generic treatment words and names for chelators, zinc formulations, tetrathiomolybdate and transplantation. Truncation stems meet the four-character minimum."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Terms are explicitly tagged [Mesh] or [tiab], parentheses are balanced, and the live PubMed translation has no technical blockers. The retained zero-hit MeSH synonym is addressed in the issue dispositions."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or study-design filter is applied. PubMed is bounded by Entrez date through 2018-12-23 as required by the run protocol."
        }
      },
      "findings": [
        {
          "id": "f-limited-benchmark",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "The development recall check is based on five records found during seed-free pilots; there is no independent benchmark set because the identified review's PubMed reference-link lookup returned no records.",
          "recommendation": "Seek the prior review's included-study list or an information specialist's independently assembled known-item set before interpreting retrieval completeness.",
          "status": "accepted-risk",
          "response": "This remains a documented limitation of a draft strategy. All five screened comparative records were retrieved (development relative recall 100%); this is not independent validation or a sensitivity estimate."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-3698fcf51ca8094ec5db",
          "status": "accepted-risk",
          "response": "This OR synonym is retained because it is an entry term for the verified Hepatolenticular Degeneration heading and could be useful in records where it appears in the title or abstract. PubMed returned no hits for the tagged phrase under the requested Entrez-date bound; that warning does not invalidate the other condition synonyms or the MeSH heading.",
          "evidence": "The exact clause count was 0, and PubMed's returned translation was \"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]. The term is an OR alternative in the condition block.",
          "query": "(\"neurohepatic degeneration\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        },
        {
          "issue_id": "I-9817d0412b37bcfd49d0",
          "status": "accepted-risk",
          "response": "The zero-hit diagnostic belongs to the same retained MeSH entry-term synonym. It is not a required clause: the condition block also contains the verified MeSH heading, common Wilson disease spellings, and other historical names. Keeping this low-cost OR synonym preserves a possible route for records with that wording.",
          "evidence": "The same exact clause returned 0 records, with PubMed warning \"No items found\" and translation \"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]. All five development records were retrieved by the condition block.",
          "query": "(\"neurohepatic degeneration\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        }
      ]
    }
  ]
}
```


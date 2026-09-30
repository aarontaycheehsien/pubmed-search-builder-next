# PubMed search strategy: audit

Generated 2026-09-30T16:34:22+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User has no known relevant articles and cannot answer clarification questions during this run; proceeded with stated assumption that common therapies means established medical drug therapies (chelators and zinc), not transplantation or supportive care. Scope was not user-confirmed. Work as of 2018-12-23 using PSB_AS_OF; no publication-date limit. No seeds supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The target condition is central to every eligible record and is reliably indexed or named; its historical name hepatolenticular degeneration is included. |
| Common medical drug therapies for Wilson disease | search | This is an intervention effectiveness question; treatment is commonly identified in indexing or abstracts. It is a category because eligible records may name a treatment member (such as penicillamine, trientine, or zinc) without saying drug therapy. |
| Comparative effectiveness and outcomes | screen | Comparators and outcomes are unreliable abstract-level requirements and are assessed during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T16:33:33+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 4,106
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `Wilson disease[tiab]` | 5,545 | none |
| 3 | `Wilson's disease[tiab]` | 4,158 | none |
| 4 | `Wilsons disease[tiab]` | 4,135 | none |
| 5 | `Wilson*[tiab]` | 11,437 | none |
| 6 | `hepatolenticular degeneration[tiab]` | 946 | none |
| 7 | `hepatocerebral degeneration[tiab]` | 142 | none |
| 8 | `hepato-neurologic Wilson disease[tiab]` | 1 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 12,969 | none |
| 10 | `"Drug Therapy"[Mesh]` | 1,305,324 | none |
| 11 | `"Chelation Therapy"[Mesh]` | 1,413 | none |
| 12 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 13 | `"Trientine"[Mesh]` | 380 | none |
| 14 | `"Zinc"[Mesh]` | 58,485 | none |
| 15 | `"Zinc Acetate"[Mesh]` | 246 | none |
| 16 | `penicillamine[tiab]` | 6,853 | none |
| 17 | `D-penicillamine[tiab]` | 3,268 | none |
| 18 | `d penicillamine[tiab]` | 3,268 | none |
| 19 | `cuprimine[tiab]` | 7 | none |
| 20 | `metalcaptase[tiab]` | 10 | none |
| 21 | `trientine[tiab]` | 219 | none |
| 22 | `triethylenetetramine[tiab]` | 360 | none |
| 23 | `triethylene tetramine[tiab]` | 74 | none |
| 24 | `trientine hydrochloride[tiab]` | 9 | none |
| 25 | `syprine[tiab]` | 4 | none |
| 26 | `zinc[tiab]` | 108,490 | none |
| 27 | `zinc salt*[tiab]` | 513 | none |
| 28 | `zinc acetate[tiab]` | 817 | none |
| 29 | `zinc sulfate[tiab]` | 1,531 | none |
| 30 | `zinc sulphate[tiab]` | 857 | none |
| 31 | `zinc therap*[tiab]` | 379 | none |
| 32 | `tetrathiomolybdate[tiab]` | 351 | none |
| 33 | `ammonium tetrathiomolybdate[tiab]` | 84 | none |
| 34 | `bis-choline tetrathiomolybdate[tiab]` | 6 | none |
| 35 | `chelati*[tiab]` | 32,153 | none |
| 36 | `anticopper[tiab]` | 79 | none |
| 37 | `anti-copper[tiab]` | 29 | none |
| 38 | `therap*[tiab]` | 2,661,898 | none |
| 39 | `treat*[tiab]` | 5,019,713 | none |
| 40 | `medication*[tiab]` | 283,167 | none |
| 41 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40` | 7,103,127 | none |
| 42 | `#9 AND #41` | 4,106 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR Wilson disease[tiab] OR Wilson's disease[tiab] OR Wilsons disease[tiab] OR Wilson*[tiab] OR hepatolenticular degeneration[tiab] OR hepatocerebral degeneration[tiab] OR hepato-neurologic Wilson disease[tiab]) AND ("Drug Therapy"[Mesh] OR "Chelation Therapy"[Mesh] OR "Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc"[Mesh] OR "Zinc Acetate"[Mesh] OR penicillamine[tiab] OR D-penicillamine[tiab] OR d penicillamine[tiab] OR cuprimine[tiab] OR metalcaptase[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR triethylene tetramine[tiab] OR trientine hydrochloride[tiab] OR syprine[tiab] OR zinc[tiab] OR zinc salt*[tiab] OR zinc acetate[tiab] OR zinc sulfate[tiab] OR zinc sulphate[tiab] OR zinc therap*[tiab] OR tetrathiomolybdate[tiab] OR ammonium tetrathiomolybdate[tiab] OR bis-choline tetrathiomolybdate[tiab] OR chelati*[tiab] OR anticopper[tiab] OR anti-copper[tiab] OR therap*[tiab] OR treat*[tiab] OR medication*[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 15 | 15 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Common medical drug therapies for Wilson disease | 1 | `Hepatolenticular Degeneration[Mesh] AND (drug*[tiab] OR agent*[tiab] OR regimen*[tiab] OR pharmacotherap*[tiab] OR anticopper[tiab] OR decopper*[tiab] OR liver transplantation[tiab])` | 163 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 7,103,127 | 0 |
| therapy | 12,969 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | First strategy draft: MeSH plus text words for Wilson disease and common anticopper drug therapies; disease and therapy are required by PICO, comparator/outcomes remain screening criteria. |
| 2 | 4,106 | wilson_disease: +0 / -2; therapy: +0 / -1 | none | Revision 2: Removed the ambiguous authority lookup for Chelating Agents and unsupported zero-hit/fallback historical text clauses. Equivalent disease coverage is retained by the verified Hepatolenticular Degeneration heading and other spelling variants; treatment coverage remains via drug headings and chelation text. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (Same-context critic: no fresh-context reviewer was available. Scope matches a PICO intervention effectiveness search under the documented assumption that common therapies means medical drug therapies, with comparators and outcomes screened. The verified Hepatolenticular Degeneration heading and text variants cover disease naming; drug therapy, chelation, named agents, and free-text therapy terms cover intervention naming. No comparison/outcome block or unvalidated design filter is used. The therapy-category probe screened 30 records with none relevant. All 15 screened development records are retrieved; this is not independent validation. Generic Wilson* and zinc/therapy terms remain broad, but the final count is within the 10,000 record screening budget.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 587 NCBI requests logged (313 from cache); strategy sha256 b607b78c8c9a._

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
      "requested": "Hepatolenticular Degeneration",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:33:33+00:00",
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
      "checked_at": "2026-09-30T16:33:33+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Drug Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chelation Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:33:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015913",
          "name": "Chelation Therapy",
          "type": "descriptor",
          "scope_note": "Therapy of heavy metal poisoning using agents which sequester the metal from organs or tissues and bind it firmly within the ring structure of a new compound which can be eliminated from the body.",
          "tree_numbers": [
            "E02.319.155"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015913",
      "preferred_label": "Chelation Therapy",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Chelation Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:33:33+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Penicillamine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:33:33+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Trientine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:33:33+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Zinc\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T16:33:33+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "\"Zinc Acetate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"wilson disease\"[Title/Abstract] OR \"wilson s disease\"[Title/Abstract] OR \"wilsons disease\"[Title/Abstract] OR \"wilson*\"[Title/Abstract] OR \"Hepatolenticular Degeneration\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"hepato neurologic wilson disease\"[Title/Abstract]) AND (\"Drug Therapy\"[MeSH Terms] OR \"Chelation Therapy\"[MeSH Terms] OR \"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc\"[MeSH Terms] OR \"Zinc Acetate\"[MeSH Terms] OR \"Penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"cuprimine\"[Title/Abstract] OR \"metalcaptase\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"triethylene tetramine\"[Title/Abstract] OR \"trientine hydrochloride\"[Title/Abstract] OR \"syprine\"[Title/Abstract] OR \"Zinc\"[Title/Abstract] OR \"zinc salt*\"[Title/Abstract] OR \"Zinc Acetate\"[Title/Abstract] OR \"zinc sulfate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"zinc therap*\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"bis choline tetrathiomolybdate\"[Title/Abstract] OR \"chelati*\"[Title/Abstract] OR \"anticopper\"[Title/Abstract] OR \"anti-copper\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"treat*\"[Title/Abstract] OR \"medication*\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "faebc5a2bd619d159a2f715e40617b58694d6fb31dc3ecf51d1a1837f93bfaf7",
      "note": "Same-context critic: no fresh-context reviewer was available. Scope matches a PICO intervention effectiveness search under the documented assumption that common therapies means medical drug therapies, with comparators and outcomes screened. The verified Hepatolenticular Degeneration heading and text variants cover disease naming; drug therapy, chelation, named agents, and free-text therapy terms cover intervention naming. No comparison/outcome block or unvalidated design filter is used. The therapy-category probe screened 30 records with none relevant. All 15 screened development records are retrieved; this is not independent validation. Generic Wilson* and zinc/therapy terms remain broad, but the final count is within the 10,000 record screening budget.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PICO population and intervention are searched; comparator and effectiveness outcomes are assessed at screening. Scope assumption is recorded."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are OR-expanded internally and AND-combined. No study-result or comparator terms are required."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The Wilson disease heading is verified; Drug Therapy, Chelation Therapy, Penicillamine, Trientine, Zinc, and Zinc Acetate passed validation. The ambiguous Chelating Agents lookup was removed."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text vocabulary includes Wilson disease aliases and common drug names, salt forms, spellings, and chelation/treatment wording. Member category was probed with no relevant hits outside the block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Evaluation reports no translation issues, technical blockers, phrase warnings, or All Fields fallbacks."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, age, or design filters were added. The Entrez date bound is supplied by PSB_AS_OF, with no [dp] limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


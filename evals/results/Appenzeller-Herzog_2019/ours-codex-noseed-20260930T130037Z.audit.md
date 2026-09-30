# PubMed search strategy: audit

Generated 2026-09-30T13:31:16+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions. Assumed the review concerns comparative clinical effectiveness of common disease-directed therapies in Wilson disease, including chelators and zinc; transplantation may qualify when evaluated comparatively. Comparators and outcomes are screened, not required search blocks. No language or publication-date limit. PubMed Entrez-date cutoff is 2018-12-23 (PSB_AS_OF); no publication-date limit is applied. No known relevant articles supplied; standard-depth discovery attempted, but no seed evidence can be assumed.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | Target disease; records may use Wilson disease, Wilson's disease, hepatolenticular degeneration, or its established MeSH heading. |
| Therapies for Wilson disease | search | Interventions define the comparative-effectiveness question; include named member therapies as well as general treatment wording and probe for member-only records. |
| Comparators | screen | Specific comparisons vary and are not consistently named in titles or abstracts. |
| Comparative effectiveness outcomes | screen | Effectiveness and safety outcomes are variably reported; screen for eligible comparisons. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:30:38+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 3,365
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Hepatolenticular Degeneration[Mesh]` | 5,697 | none |
| 2 | `wilson disease[tiab]` | 5,545 | none |
| 3 | `wilson's disease[tiab]` | 4,158 | none |
| 4 | `wilsons disease[tiab]` | 4,135 | none |
| 5 | `hepatolenticular degeneration[tiab]` | 946 | none |
| 6 | `hepatocerebral degeneration[tiab]` | 142 | none |
| 7 | `kinnier-wilson[tiab]` | 38 | none |
| 8 | `copper storage disease[tiab]` | 25 | none |
| 9 | `copper storage diseases[tiab]` | 7 | none |
| 10 | `westphal-strumpell[tiab]` | 26 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 7,326 | none |
| 12 | `Drug Therapy[Mesh]` | 1,305,324 | none |
| 13 | `Chelation Therapy[Mesh]` | 1,413 | none |
| 14 | `Penicillamine[Mesh]` | 7,878 | none |
| 15 | `Trientine[Mesh]` | 380 | none |
| 16 | `Zinc Acetate[Mesh]` | 246 | none |
| 17 | `Zinc Compounds[Mesh]` | 12,484 | none |
| 18 | `Liver Transplantation[Mesh]` | 54,773 | none |
| 19 | `treat*[tiab]` | 5,019,713 | none |
| 20 | `therap*[tiab]` | 2,661,898 | none |
| 21 | `pharmacotherap*[tiab]` | 32,759 | none |
| 22 | `drug therap*[tiab]` | 50,455 | none |
| 23 | `chelati*[tiab]` | 32,153 | none |
| 24 | `penicillamine[tiab]` | 6,853 | none |
| 25 | `D-penicillamine[tiab]` | 3,268 | none |
| 26 | `trientine[tiab]` | 219 | none |
| 27 | `triethylenetetramine[tiab]` | 360 | none |
| 28 | `zinc[tiab]` | 108,490 | none |
| 29 | `zinc therap*[tiab]` | 379 | none |
| 30 | `zinc acetate[tiab]` | 817 | none |
| 31 | `tetrathiomolybdate[tiab]` | 351 | none |
| 32 | `liver transplant*[tiab]` | 55,108 | none |
| 33 | `hepatic transplant*[tiab]` | 1,078 | none |
| 34 | `low copper diet[tiab]` | 81 | none |
| 35 | `copper restricted diet[tiab]` | 4 | none |
| 36 | `copper-restricted diet[tiab]` | 4 | none |
| 37 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36` | 7,048,189 | none |
| 38 | `#11 AND #37` | 3,365 | none |

### Strategy (single line, for copying into PubMed)

```text
((Hepatolenticular Degeneration[Mesh] OR wilson disease[tiab] OR wilson's disease[tiab] OR wilsons disease[tiab] OR hepatolenticular degeneration[tiab] OR hepatocerebral degeneration[tiab] OR kinnier-wilson[tiab] OR copper storage disease[tiab] OR copper storage diseases[tiab] OR westphal-strumpell[tiab]) AND (Drug Therapy[Mesh] OR Chelation Therapy[Mesh] OR Penicillamine[Mesh] OR Trientine[Mesh] OR Zinc Acetate[Mesh] OR Zinc Compounds[Mesh] OR Liver Transplantation[Mesh] OR treat*[tiab] OR therap*[tiab] OR pharmacotherap*[tiab] OR drug therap*[tiab] OR chelati*[tiab] OR penicillamine[tiab] OR D-penicillamine[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR zinc therap*[tiab] OR zinc acetate[tiab] OR tetrathiomolybdate[tiab] OR liver transplant*[tiab] OR hepatic transplant*[tiab] OR low copper diet[tiab] OR copper restricted diet[tiab] OR copper-restricted diet[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

No known relevant records were available, so recall was not estimated.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Therapies for Wilson disease | 1 | `(Hepatolenticular Degeneration[Mesh] OR wilson disease[tiab] OR wilson's disease[tiab])` | 3,896 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 83 | initial | none | Initial recall-first PICO strategy: disease and broad therapy/intervention blocks with named common members; comparators and outcomes screened. No limits; Entrez date cutoff 2018-12-23. |
| 2 | 3,359 | wilson_disease: +0 / -1; therapy: +3 / -2 | none | Removed ambiguous Chelating Agents heading after NCBI authority verification; dropped a phrase that PubMed fell back to All Fields and repaired the separated copper-restricted-diet wording. Retained the 2018-12-23 Entrez cutoff and no publication-date limit. |
| 3 | 3,365 | therapy: +1 / -0 | none | Added the verified Zinc Compounds[Mesh] heading in response to the internal subject-heading critique, retaining Zinc Acetate[Mesh] and zinc text words to cover the common therapy and broader indexed zinc formulations. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; F1 should-fix open, F2 document accepted-risk
- Round 2 on version 3: 2 findings; F1 should-fix resolved, F2 document accepted-risk
- Round 3 on version 3: 2 findings; F1 should-fix resolved, F2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 451 NCBI requests logged (215 from cache); strategy sha256 1e227bd6911b._

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
      "checked_at": "2026-09-30T13:30:38+00:00",
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
      "requested": "Drug Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:30:38+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "Drug Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chelation Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:30:38+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "Chelation Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:30:38+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "Penicillamine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:30:38+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Trientine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:30:38+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "Zinc Acetate",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Compounds",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:30:38+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017967",
          "name": "Zinc Compounds",
          "type": "descriptor",
          "scope_note": "Inorganic compounds that contain zinc as an integral part of the molecule.",
          "tree_numbers": [
            "D01.975"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017967",
      "preferred_label": "Zinc Compounds",
      "type": "descriptor",
      "location": "vocabulary:16",
      "term": {
        "text": "Zinc Compounds",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Liver Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:30:38+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "Liver Transplantation",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"hepatolenticular degeneration\"[MeSH Terms] OR \"wilson disease\"[Title/Abstract] OR \"wilson s disease\"[Title/Abstract] OR \"wilsons disease\"[Title/Abstract] OR \"hepatolenticular degeneration\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"kinnier-wilson\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"copper storage diseases\"[Title/Abstract] OR \"westphal-strumpell\"[Title/Abstract]) AND (\"drug therapy\"[MeSH Terms] OR \"chelation therapy\"[MeSH Terms] OR \"penicillamine\"[MeSH Terms] OR \"trientine\"[MeSH Terms] OR \"zinc acetate\"[MeSH Terms] OR \"zinc compounds\"[MeSH Terms] OR \"liver transplantation\"[MeSH Terms] OR \"treat*\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"pharmacotherap*\"[Title/Abstract] OR \"drug therap*\"[Title/Abstract] OR \"chelati*\"[Title/Abstract] OR \"penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"zinc therap*\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"liver transplant*\"[Title/Abstract] OR \"hepatic transplant*\"[Title/Abstract] OR \"low copper diet\"[Title/Abstract] OR \"copper restricted diet\"[Title/Abstract] OR \"copper restricted diet\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "3b7b579c76c896926d8a9b70fc7dba6710a4a6919a782cade40f7c832002fcb5",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The recorded PubMed translations preserve the intended disease and therapy terms. The packet reports no translation issues or query warnings."
        },
        "operators": {
          "verdict": "pass",
          "note": "The disease and therapy terms are ORed within their blocks, and the two searched concepts are ANDed. Comparators and outcomes remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The disease heading and several therapy headings are verified, but the therapy block relies on Zinc Acetate[Mesh] for indexed records and lacks a broader zinc heading. Consider adding a verified Zinc or Zinc Compounds heading to cover zinc therapy beyond acetate."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the disease aliases and named therapies in the protocol, including bare zinc and chelation stems. No protocol-named therapy is represented only by a phrase narrowed with parent wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint, syntax, or PubMed translation errors. The final query has the intended block structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limit is applied. The Entrez-date cutoff of 2018-12-23 is explicitly documented as the as-of date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The therapy block includes Zinc Acetate[Mesh] but no broader zinc heading. Since the protocol searches for zinc therapy without restricting the formulation, records indexed under another zinc heading may not be retrieved when their title or abstract does not mention zinc.",
          "recommendation": "Check the relevant current MeSH headings and consider adding an appropriate broader zinc heading, such as Zinc or Zinc Compounds, while retaining the existing text-word coverage.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The packet has no PMID seed or validation sets, so recall was not measured. The therapy probe screened 30 records outside the block and found none eligible; this is limited evidence about block completeness.",
          "recommendation": "Report the absence of recall validation as a limitation; test any relevant comparative studies against the strategy if they become available.",
          "status": "accepted-risk",
          "response": "Accepted and documented. No user-supplied or screened-in eligible records were available for recall estimation; the current therapy category probe screened 30 records and found none relevant, which does not establish recall."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "cb9e9149e1ec8d5effb7fe12eee11938b08040ae297ec0587cfe314e1ec64969",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The recorded translations retain the intended disease and therapy terms. The packet reports no translation issues or PubMed warnings."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each block, and the disease and therapy blocks are ANDed. Comparators and outcomes remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The current therapy block includes Zinc Compounds[Mesh], addressing the prior gap in broader indexed zinc coverage. The packet verifies this heading and reports no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes the stated disease names and aliases. The therapy block includes general treatment terms and bare names for the protocol-named therapies; zinc and tetrathiomolybdate are not restricted to phrases containing parent wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or syntax issues, and the final query translation preserves the intended two-block structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limit is applied. The Entrez-date cutoff is documented as the as-of date. No PMID sets are available, so recall remains unmeasured; the 30-record therapy probe is limited evidence and does not establish recall."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier version included Zinc Acetate[Mesh] but lacked broader zinc indexing coverage.",
          "recommendation": "Add an appropriate broader zinc heading while retaining the existing text-word coverage.",
          "status": "resolved",
          "response": "Resolved in version 3: Zinc Compounds[Mesh] is now included in the therapy block, and the packet verifies the heading."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "No PMID seed or validation sets are available, so recall was not measured. The therapy probe screened 30 records outside the block and found none eligible; this is limited evidence about block completeness.",
          "recommendation": "Report the absence of recall validation as a limitation and test any relevant comparative studies against the strategy if they become available.",
          "status": "accepted-risk",
          "response": "Accepted and documented. No user-supplied or screened-in eligible records were available for recall estimation. The category probe found no relevant records among 30 screened, which does not establish recall."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "cb9e9149e1ec8d5effb7fe12eee11938b08040ae297ec0587cfe314e1ec64969",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Recorded translations preserve the intended disease and therapy terms; the packet reports no translation issues or warnings."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each concept block, and the disease and therapy blocks are ANDed. Comparators and outcomes remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The therapy block now includes Zinc Compounds[Mesh], resolving the earlier gap in broader indexed zinc coverage."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include disease aliases, general treatment wording, and bare names for the named therapies."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or syntax issues, and the query retains the intended two-block structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limit is applied; the Entrez-date cutoff is documented as the as-of date. Recall remains unmeasured because no PMID sets are available."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier strategy lacked broader zinc indexing coverage beyond Zinc Acetate[Mesh].",
          "recommendation": "Add an appropriate broader zinc heading while retaining text-word coverage.",
          "status": "resolved",
          "response": "Resolved in version 3: Zinc Compounds[Mesh] is included in the therapy block and verified in the packet."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "No PMID seed or validation sets are available, so recall was not measured. The therapy probe screened 30 records outside the block and found none eligible; this is limited evidence about block completeness.",
          "recommendation": "Report the absence of recall validation as a limitation and test relevant comparative studies against the strategy if they become available.",
          "status": "accepted-risk",
          "response": "Accepted and documented. No user-supplied or screened-in eligible records were available for recall estimation. The probe found no relevant records among 30 screened, which does not establish recall."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


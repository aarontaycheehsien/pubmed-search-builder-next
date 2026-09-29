# PubMed search strategy: audit

Generated 2026-09-28T20:57:33+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: yes (User asked to proceed without follow-up. Assumed common therapies are conventional anti-copper pharmacotherapies (D-penicillamine, trientine, zinc salts, tetrathiomolybdate); herbal regimens and liver transplantation are outside scope. No age, language, study-design, or publication-date limits. PubMed records are bounded by Entrez date through 2018-12-23 (PSB_AS_OF), not by publication date. No known relevant articles were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The disease is the defining population and is expected to be named or indexed in relevant treatment studies. |
| Common Wilson disease therapies | search | Treatment is central to the question and commonly named; probe for papers that identify only individual therapy members. |
| Comparators between therapies | screen | Comparative arms are inconsistently named in title, abstract, or indexing; assess at screening. |
| Clinical effectiveness and safety outcomes | screen | Outcome reporting varies and should not be required for retrieval. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T20:56:44+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 1,911
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Hepatolenticular Degeneration[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab]` | 5,545 | none |
| 3 | `"Wilson's disease"[tiab]` | 4,158 | none |
| 4 | `Wilson's[tiab]` | 4,762 | none |
| 5 | `hepatolenticular degenera*[tiab]` | 946 | none |
| 6 | `hepatocerebral degenera*[tiab]` | 142 | none |
| 7 | `neurohepatic[tiab]` | 7 | none |
| 8 | `progressive lenticular degenera*[tiab]` | 10 | none |
| 9 | `pseudosclerosis[tiab]` | 55 | none |
| 10 | `"copper storage disease"[tiab]` | 25 | none |
| 11 | `"Kinnier-Wilson"[tiab]` | 38 | none |
| 12 | `"Westphal-Strumpell"[tiab]` | 26 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 7,896 | none |
| 14 | `Penicillamine[Mesh]` | 7,878 | none |
| 15 | `Trientine[Mesh]` | 380 | none |
| 16 | `Zinc[Mesh]` | 58,485 | none |
| 17 | `Zinc Sulfate[Mesh]` | 1,802 | none |
| 18 | `Zinc Acetate[Mesh]` | 246 | none |
| 19 | `Dimercaprol[Mesh]` | 2,156 | none |
| 20 | `tetrathiomolybdate[nm]` | 293 | none |
| 21 | `penicillamine[tiab]` | 6,853 | none |
| 22 | `D-penicillamine[tiab]` | 3,268 | none |
| 23 | `D penicillamine[tiab]` | 3,268 | none |
| 24 | `copper penicillaminate[tiab]` | 1 | none |
| 25 | `mercaptovaline[tiab]` | 5 | none |
| 26 | `Cuprimine[tiab]` | 7 | none |
| 27 | `Cuprenil[tiab]` | 21 | none |
| 28 | `trientine[tiab]` | 219 | none |
| 29 | `triethylenetetramine[tiab]` | 360 | none |
| 30 | `Syprine[tiab]` | 4 | none |
| 31 | `zinc[tiab]` | 108,490 | none |
| 32 | `zinc sulfate[tiab]` | 1,531 | none |
| 33 | `zinc sulphate[tiab]` | 857 | none |
| 34 | `zinc acetate[tiab]` | 817 | none |
| 35 | `zinc gluconate[tiab]` | 257 | none |
| 36 | `zinc salt*[tiab]` | 513 | none |
| 37 | `tetrathiomolybdate[tiab]` | 351 | none |
| 38 | `ammonium tetrathiomolybdate[tiab]` | 84 | none |
| 39 | `bis-choline tetrathiomolybdate[tiab]` | 6 | none |
| 40 | `WTX101[tiab]` | 3 | none |
| 41 | `chelating agent*[tiab]` | 7,766 | none |
| 42 | `copper chelat*[tiab]` | 1,179 | none |
| 43 | `anti-copper therap*[tiab]` | 6 | none |
| 44 | `anticopper therap*[tiab]` | 21 | none |
| 45 | `#14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44` | 147,049 | none |
| 46 | `#13 AND #45` | 1,911 | none |

### Strategy (single line, for copying into PubMed)

```text
((Hepatolenticular Degeneration[Mesh] OR "Wilson disease"[tiab] OR "Wilson's disease"[tiab] OR Wilson's[tiab] OR hepatolenticular degenera*[tiab] OR hepatocerebral degenera*[tiab] OR neurohepatic[tiab] OR progressive lenticular degenera*[tiab] OR pseudosclerosis[tiab] OR "copper storage disease"[tiab] OR "Kinnier-Wilson"[tiab] OR "Westphal-Strumpell"[tiab]) AND (Penicillamine[Mesh] OR Trientine[Mesh] OR Zinc[Mesh] OR Zinc Sulfate[Mesh] OR Zinc Acetate[Mesh] OR Dimercaprol[Mesh] OR tetrathiomolybdate[nm] OR penicillamine[tiab] OR D-penicillamine[tiab] OR D penicillamine[tiab] OR copper penicillaminate[tiab] OR mercaptovaline[tiab] OR Cuprimine[tiab] OR Cuprenil[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR Syprine[tiab] OR zinc[tiab] OR zinc sulfate[tiab] OR zinc sulphate[tiab] OR zinc acetate[tiab] OR zinc gluconate[tiab] OR zinc salt*[tiab] OR tetrathiomolybdate[tiab] OR ammonium tetrathiomolybdate[tiab] OR bis-choline tetrathiomolybdate[tiab] OR WTX101[tiab] OR chelating agent*[tiab] OR copper chelat*[tiab] OR anti-copper therap*[tiab] OR anticopper therap*[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Common Wilson disease therapies | 1 | `Hepatolenticular Degeneration[Mesh] AND (Drug Therapy[Mesh] OR treatment[tiab] OR therap*[tiab] OR medication*[tiab] OR pharmacotherap*[tiab])` | 689 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 147,049 | 0 |
| therapies | 7,896 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block PICO strategy; includes disease synonyms and standard anti-copper drug members identified from MeSH and screened treatment records. |
| 2 | 1,911 | wilson_disease: +1 / -1; therapies: +0 / -1 | none | Removed the ambiguous generic Chelating Agents descriptor because specific drug MeSH headings and broad free-text chelator wording cover the class; replaced the zero-hit neurohepatic degeneration stem with neurohepatic alone, which retrieves records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F1 must-fix rejected
- Round 2 on version 2: 1 findings; F1 must-fix rejected
- Round 3 on version 2: 1 findings; F1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 434 NCBI requests logged (149 from cache); strategy sha256 b3bcd64768a9._

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
      "checked_at": "2026-09-28T20:56:44+00:00",
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
      "checked_at": "2026-09-28T20:56:44+00:00",
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
      "checked_at": "2026-09-28T20:56:44+00:00",
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
      "requested": "Zinc",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:56:44+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "Zinc",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Sulfate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:56:44+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "Zinc Sulfate",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:56:44+00:00",
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
        "text": "Zinc Acetate",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dimercaprol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:56:44+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "Dimercaprol",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "tetrathiomolybdate",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T20:56:44+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "tetrathiomolybdate",
        "tag": "nm",
        "field": "nm"
      }
    }
  ],
  "translation": "(\"hepatolenticular degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"Wilson's disease\"[Title/Abstract] OR \"Wilson's\"[Title/Abstract] OR \"hepatolenticular degenera*\"[Title/Abstract] OR \"hepatocerebral degenera*\"[Title/Abstract] OR \"neurohepatic\"[Title/Abstract] OR \"progressive lenticular degenera*\"[Title/Abstract] OR \"pseudosclerosis\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"Westphal-Strumpell\"[Title/Abstract]) AND (\"penicillamine\"[MeSH Terms] OR \"trientine\"[MeSH Terms] OR \"zinc\"[MeSH Terms] OR \"zinc sulfate\"[MeSH Terms] OR \"zinc acetate\"[MeSH Terms] OR \"dimercaprol\"[MeSH Terms] OR \"tetrathiomolybdate\"[Supplementary Concept] OR \"penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"copper penicillaminate\"[Title/Abstract] OR \"mercaptovaline\"[Title/Abstract] OR \"Cuprimine\"[Title/Abstract] OR \"Cuprenil\"[Title/Abstract] OR \"trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"Syprine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"zinc sulfate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"zinc gluconate\"[Title/Abstract] OR \"zinc salt*\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"bis choline tetrathiomolybdate\"[Title/Abstract] OR \"WTX101\"[Title/Abstract] OR \"chelating agent*\"[Title/Abstract] OR \"copper chelat*\"[Title/Abstract] OR \"anti copper therap*\"[Title/Abstract] OR \"anticopper therap*\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "8a57f51883996f52ec598d7c7ea45d86b59d0da1e5a76a53cd1230cef217e040",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named eligible therapies have their own bare-name coverage: penicillamine/D-penicillamine, trientine, zinc, and tetrathiomolybdate. The strategy does not search for a direction of switching that would require a bidirectional process term."
        },
        "operators": {
          "verdict": "pass",
          "note": "The disease and therapy blocks are combined with AND, and terms within each block with OR. No operator issue is evident in the displayed strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH descriptors and a verified tetrathiomolybdate supplementary concept. The headings are combined with free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word block includes the named therapies and several aliases or spelling variants. All four known relevant records are retrieved, and the category probe found 0 relevant records among 30 screened outside the therapy block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no translation issues, diagnostics, or lint findings; the displayed final query has balanced block structure."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Every evaluated line applies an Entrez date-of-entry ceiling of 2018-12-23. This excludes records entered after that date, despite the protocol stating no date limits. The ceiling is disclosed in the notes, but the search horizon needs resolution."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez date-of-entry range ending 2018-12-23. The protocol says there are no publication-date limits, while the notes disclose that records entered after the cutoff are excluded. The four known records retrieved do not establish coverage beyond this cutoff.",
          "recommendation": "Set the intended search horizon. If the review is not explicitly limited to the 2018 snapshot, remove the entry-date ceiling or extend it to the intended search date, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "The 2018-12-23 Entrez entry-date ceiling is required by the user's explicit harness instruction to treat the run as a PubMed snapshot on that date and to leave PSB_AS_OF set on every command. The question does not ask for a current search. This is an Entrez-date snapshot bound, not a publication-date ([dp]) limit; the cutoff is also recorded in protocol.as_of and notes. I therefore reject the recommendation to remove or extend it."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "8a57f51883996f52ec598d7c7ea45d86b59d0da1e5a76a53cd1230cef217e040",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Each named eligible therapy has bare-name text coverage, and the strategy does not constrain retrieval to a direction of switching."
        },
        "operators": {
          "verdict": "pass",
          "note": "The disease and therapy blocks are combined with AND; terms within each block are combined with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the listed MeSH headings and tetrathiomolybdate supplementary concept, alongside text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The therapy block includes the named drugs and aliases. The four known relevant records are retrieved; the reported category probe found no relevant records among 30 screened."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no diagnostics, translation issues, or lint findings, and the displayed query has balanced blocks."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The query is bounded by Entrez entry date through 2018-12-23, matching protocol.as_of and the note identifying a PubMed snapshot bound. The protocol's statement of no publication-date limits does not conflict with this entry-date snapshot."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an Entrez date-of-entry range ending 2018-12-23. The protocol says there are no publication-date limits, while the notes disclose that records entered after that date are excluded. The four known records retrieved do not establish coverage beyond this cutoff.",
          "recommendation": "Set the intended search horizon. If the review is not explicitly limited to the 2018 snapshot, remove the entry-date ceiling or extend it to the intended search date, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "The packet records 2018-12-23 as protocol.as_of and states that PubMed records are bounded by Entrez date through that date, not by publication date. The query's entry-date ceiling implements that documented snapshot; the absence of a publication-date limit does not contradict it. The packet does not support removing or extending the ceiling."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "8a57f51883996f52ec598d7c7ea45d86b59d0da1e5a76a53cd1230cef217e040",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Named eligible therapies have bare-name coverage; the strategy does not restrict switching to one direction."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease and therapy blocks are joined with AND, and terms within each block with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH descriptors and the tetrathiomolybdate supplementary concept, combined with text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The therapy block covers the named drugs and aliases; all four known relevant records are retrieved, and none of 30 screened probe records was relevant."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no diagnostics, translation issues, or lint findings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "F1 was rejected in both earlier rounds. The documented Entrez entry-date ceiling matches protocol.as_of and the stated 2018 snapshot; it is not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entrez date-of-entry ceiling of 2018-12-23, excluding records entered after that date.",
          "recommendation": "Remove or extend the ceiling if the intended search horizon is later than the documented 2018 snapshot.",
          "status": "rejected",
          "response": "The packet documents 2018-12-23 as protocol.as_of and states that this is a PubMed Entrez entry-date snapshot bound, not a publication-date limit. The query implements that stated snapshot, so the recommendation to remove or extend the ceiling is rejected."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


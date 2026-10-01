# PubMed search strategy: audit

Generated 2026-10-01T12:19:16+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User cannot answer questions during this run and asked to proceed. Assumed common therapies means established medical anti-copper treatments (D-penicillamine, trientine, zinc salts, and tetrathiomolybdate where studied); includes treatment-specific studies and direct comparisons. Comparators, severity, and outcomes are screened rather than AND-ed. Liver transplantation and supportive management are outside this pharmacotherapy-focused interpretation. No user-supplied seeds; 38 candidates from a focused pilot were screened, and 24 were included across development and validation sets. A matching 2009 systematic review was identified, but its included studies could not be retrieved through psb neighbors, so no prior-review benchmark was assembled. The 5-record validation set was created after psb terms rank displayed candidates from all original 17 records; no ranked terms were added, but this set is not fully independent. Scope proceeded on assumptions and was not user-confirmed. PubMed records are bounded by Entrez date 2018-12-23; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | Target condition; records should identify Wilson disease or its established synonym hepatolenticular degeneration. |
| Common medical therapies for Wilson disease | search | Interventions are central to effectiveness; search named therapy members because records may name only a drug rather than a therapy class. |
| Therapy comparisons | screen | Comparators may not be named consistently in titles or abstracts. |
| Comparative outcomes/effectiveness | screen | Outcomes and effectiveness language is inconsistently reported and should not be required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:18:37+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 1,904
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab]` | 5,545 | none |
| 3 | `"Wilson's disease"[tiab]` | 4,158 | none |
| 4 | `"hepatolenticular degeneration"[tiab]` | 946 | none |
| 5 | `"hepatocerebral degeneration"[tiab]` | 142 | none |
| 6 | `"copper storage disease"[tiab]` | 25 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 7,294 | none |
| 8 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 9 | `"Trientine"[Mesh]` | 380 | none |
| 10 | `"Zinc Compounds"[Mesh]` | 12,484 | none |
| 11 | `"Zinc Sulfate"[Mesh]` | 1,802 | none |
| 12 | `"Zinc Acetate"[Mesh]` | 246 | none |
| 13 | `tetrathiomolybdate[nm]` | 293 | none |
| 14 | `penicillamine[tiab]` | 6,853 | none |
| 15 | `"D-penicillamine"[tiab]` | 3,268 | none |
| 16 | `trientine[tiab]` | 219 | none |
| 17 | `triethylenetetramine[tiab]` | 360 | none |
| 18 | `zinc[tiab]` | 108,490 | none |
| 19 | `"zinc acetate"[tiab]` | 817 | none |
| 20 | `"zinc sulfate"[tiab]` | 1,531 | none |
| 21 | `"zinc sulphate"[tiab]` | 857 | none |
| 22 | `"zinc gluconate"[tiab]` | 257 | none |
| 23 | `tetrathiomolybdate[tiab]` | 351 | none |
| 24 | `"ammonium tetrathiomolybdate"[tiab]` | 84 | none |
| 25 | `chelat*[tiab]` | 62,346 | none |
| 26 | `chelator*[tiab]` | 18,911 | none |
| 27 | `chelation[tiab]` | 13,461 | none |
| 28 | `"anti-copper"[tiab]` | 29 | none |
| 29 | `anticopper[tiab]` | 79 | none |
| 30 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 181,703 | none |
| 31 | `#7 AND #30` | 1,904 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR "Wilson disease"[tiab] OR "Wilson's disease"[tiab] OR "hepatolenticular degeneration"[tiab] OR "hepatocerebral degeneration"[tiab] OR "copper storage disease"[tiab]) AND ("Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc Compounds"[Mesh] OR "Zinc Sulfate"[Mesh] OR "Zinc Acetate"[Mesh] OR tetrathiomolybdate[nm] OR penicillamine[tiab] OR "D-penicillamine"[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR "zinc acetate"[tiab] OR "zinc sulfate"[tiab] OR "zinc sulphate"[tiab] OR "zinc gluconate"[tiab] OR tetrathiomolybdate[tiab] OR "ammonium tetrathiomolybdate"[tiab] OR chelat*[tiab] OR chelator*[tiab] OR chelation[tiab] OR "anti-copper"[tiab] OR anticopper[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 19 | 19 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Common medical therapies for Wilson disease | 1 | `treat*[tiab] OR therap*[tiab] OR drug*[tiab] OR medication*[tiab] OR chelat*[tiab] OR chelation[tiab] OR anti-copper[tiab] OR anticopper[tiab]` | 1,279 | 0/30 |
| Common medical therapies for Wilson disease | 2 | `treat*[tiab] OR therap*[tiab] OR drug*[tiab] OR medication*[tiab] OR chelat*[tiab] OR chelation[tiab] OR anti-copper[tiab] OR anticopper[tiab]` | 1,277 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 181,703 | 0 |
| therapies | 7,294 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,853 | initial | none | Initial PICO strategy: condition and named established anti-copper therapies searched; comparators and outcomes left for screening; no date, language, age, or design limits. |
| 2 | 1,900 | wilson_disease: +0 / -2; therapies: +5 / -2 | none | Removed unsupported Kinnier-Wilson phrase and duplicate proximity disease term after PubMed phrase-index warning; removed Chelating Agents MeSH due ambiguous authority verification; added generic chelation/anti-copper text terms to retain broad therapy wording; tightened and documented scope from screened treatment candidates. |
| 3 | 1,904 | therapies: +3 / -1 | none | Add verified Zinc Acetate MeSH heading and text variants for zinc sulphate and zinc gluconate based on therapy vocabulary review; remove duplicate unhyphenated D-penicillamine phrase that PubMed translated identically to the hyphenated term. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (Same-context critic: no fresh-context reviewer session was available. Reviewed the supplied packet against the six PRESS domains. The 5-record validation set was split only after term ranking had viewed candidates from all 17 records; no terms were added from the ranking, but this set is not fully independent and that limitation must be disclosed.): 0 findings; 
- Round 2 on version 3 (Same-context closing critic: verified the round 1 assessment against the current packet. No findings were left open. The validation-set contamination caveat remains explicit in the workspace notes and should accompany any recall claim.): 0 findings; 
- Round 3 on version 3 (Same-context verification critic: reviewed the updated eligibility wording and expanded screened development set. No earlier findings required changes and no new must-fix or should-fix concern arose. The record set remains descriptive, and the validation split caveat remains disclosed.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 752 NCBI requests logged (420 from cache); strategy sha256 343c568e2d56._

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
      "checked_at": "2026-10-01T12:18:37+00:00",
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
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:18:37+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "\"Penicillamine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:18:37+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"Trientine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Compounds",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:18:37+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Zinc Compounds\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Sulfate",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:18:37+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Zinc Sulfate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:18:37+00:00",
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
        "text": "\"Zinc Acetate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "tetrathiomolybdate",
      "expected_type": "supplementary",
      "checked_at": "2026-10-01T12:18:37+00:00",
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
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"Wilson's disease\"[Title/Abstract] OR \"Hepatolenticular Degeneration\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract]) AND (\"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Compounds\"[MeSH Terms] OR \"Zinc Sulfate\"[MeSH Terms] OR \"Zinc Acetate\"[MeSH Terms] OR \"tetrathiomolybdate\"[Supplementary Concept] OR \"Penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"Zinc Acetate\"[Title/Abstract] OR \"Zinc Sulfate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"zinc gluconate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"chelat*\"[Title/Abstract] OR \"chelator*\"[Title/Abstract] OR \"chelation\"[Title/Abstract] OR \"anti-copper\"[Title/Abstract] OR \"anticopper\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "908182390dbc6bee3b3ba16f7a2f4f71f56132c1fbd763e17e3b87c50d7d35cb",
      "note": "Same-context critic: no fresh-context reviewer session was available. Reviewed the supplied packet against the six PRESS domains. The 5-record validation set was split only after term ranking had viewed candidates from all 17 records; no terms were added from the ranking, but this set is not fully independent and that limitation must be disclosed.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The question is treated as PICO. Wilson disease and common named anti-copper therapies are required searchable concepts; comparators and outcomes remain for screening. The assumed therapy scope is recorded, and scope_confirmed is false. The category therapy probe was screened twice with no clearly eligible generic-only study found."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR joins synonyms within each block and AND combines condition with intervention. No NOT is used in the final strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The condition heading and headings for penicillamine, trientine, zinc compounds, zinc sulfate, and zinc acetate have MeSH support; tetrathiomolybdate is a verified supplementary concept. Chelating Agents was removed because live authority validation returned an ambiguous duplicate record; named headings and generic chelation text remain."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text terms cover Wilson disease synonyms, named therapy members, zinc salt variants, and generic chelation/anti-copper wording. The query uses no unsupported Kinnier-Wilson phrase; the earlier warning was resolved by removal and re-evaluation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Every free-text term is explicitly field-tagged, controlled vocabulary is tagged, wildcard stems are sufficiently long, and the current evaluation has no translation issues or blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, design, or publication-date filter is used. PubMed is bounded by Entrez date 2018-12-23 as requested, not by publication date."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "908182390dbc6bee3b3ba16f7a2f4f71f56132c1fbd763e17e3b87c50d7d35cb",
      "closing": true,
      "note": "Same-context closing critic: verified the round 1 assessment against the current packet. No findings were left open. The validation-set contamination caveat remains explicit in the workspace notes and should accompany any recall claim.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The condition/intervention blocks follow the stated pharmacotherapy interpretation; comparators and outcomes are screened. Both category probes were screened with no clearly eligible generic-only treatment record."
        },
        "operators": {
          "verdict": "pass",
          "note": "Within-block OR and between-block AND are appropriate; no exclusions or filters are applied in the query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings and the tetrathiomolybdate supplementary concept are verified. The ambiguous Chelating Agents heading was removed, with explicit drug headings and text terms retained."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Disease synonyms, therapy names, zinc salt variants, and generic chelation terms are represented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current evaluation is complete with no syntax, authority, or translation blockers and no outstanding phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, or study-design limits are present. Entrez date cutoff is 2018-12-23; no publication-date limit is used."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "strategy_version": 3,
      "review_sha256": "fefe10a5d228505600c9d7391f7151a416c6f8b3ba34779be02ba1556432a2ab",
      "closing": true,
      "note": "Same-context verification critic: reviewed the updated eligibility wording and expanded screened development set. No earlier findings required changes and no new must-fix or should-fix concern arose. The record set remains descriptive, and the validation split caveat remains disclosed.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Allowing multi-patient case series while excluding single-patient case reports clarifies the therapy-effectiveness scope without changing the condition/intervention blocks or the screening treatment of comparators and outcomes."
        },
        "operators": {
          "verdict": "pass",
          "note": "The OR synonym blocks and AND between Wilson disease and common therapy remain appropriate; no NOT clause is used in the strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Previously verified MeSH and supplementary-concept terms remain valid. The expanded known set is retrieved without any new vocabulary changes; the unresolved Chelating Agents descriptor ambiguity remains avoided."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The vocabulary retains Wilson disease synonyms, named agents, zinc salt forms, and generic chelation language."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current evaluation is complete with no blockers or translation warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No extra age, language, publication-date, or study-design filters have been added; the Entrez-date cutoff remains 2018-12-23."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


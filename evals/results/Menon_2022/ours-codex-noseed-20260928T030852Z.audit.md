# PubMed search strategy: audit

Generated 2026-09-28T03:21:05+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Methodological rigour of systematic reviews in environmental health
- Framework: method + task (application context searched broadly)
- Scope confirmed by user: yes (User asked to proceed without questions. Assumed the target is systematic reviews about environmental determinants of human health, with methodological rigour as an eligibility/appraisal criterion rather than a required search block. Potential ambiguity: whether the user means reviews that explicitly evaluate methodological quality of environmental-health SRs, versus all such SRs whose rigour is to be assessed by this review. Applied PSB_AS_OF=2020-07-20 (Entrez date) to every command; no publication-date limit. No known relevant articles supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Systematic reviews | search | The review type defines the records being assessed and is usually named or indexed; search broadly with MeSH and title/abstract terms. |
| Environmental health topics | search | Application context is central to the question; use a broad environmental/health concept block, recognizing that some relevant reviews may name a specific exposure rather than environmental health. |
| Methodological rigour or quality appraisal | screen | This is the property of interest and may not be stated consistently in titles or abstracts; assess at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T03:20:22+00:00
- Records added to PubMed up to: 2020-07-20
- Total records: 9,783
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Systematic Reviews as Topic[Mesh]` | 6,347 | none |
| 2 | `systematic[sb]` | 165,969 | none |
| 3 | `systematic review[tiab]` | 160,742 | none |
| 4 | `systematic reviews[tiab]` | 30,250 | none |
| 5 | `systematic literature review[tiab]` | 11,090 | none |
| 6 | `systematic literature reviews[tiab]` | 505 | none |
| 7 | `umbrella review[tiab]` | 410 | none |
| 8 | `umbrella reviews[tiab]` | 40 | none |
| 9 | `meta-review[tiab]` | 209 | none |
| 10 | `meta[tiab] AND review[tiab]` | 96,416 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 217,641 | none |
| 12 | `Environmental Health[Mesh]` | 25,528 | none |
| 13 | `Environmental Exposure[Mesh]` | 309,210 | none |
| 14 | `Environmental Pollution[Mesh]` | 553,246 | none |
| 15 | `Air Pollution[Mesh]` | 59,328 | none |
| 16 | `Occupational Exposure[Mesh]` | 64,382 | none |
| 17 | `environment*[tiab]` | 1,016,489 | none |
| 18 | `environmental exposure[tiab]` | 7,564 | none |
| 19 | `environmental exposures[tiab]` | 6,391 | none |
| 20 | `environmental health[tiab]` | 9,584 | none |
| 21 | `environmental pollutant*[tiab]` | 7,573 | none |
| 22 | `environmental pollution[tiab]` | 7,249 | none |
| 23 | `environmental factor[tiab]` | 3,497 | none |
| 24 | `environmental factors[tiab]` | 65,553 | none |
| 25 | `air pollution[tiab]` | 27,926 | none |
| 26 | `air pollutant*[tiab]` | 9,409 | none |
| 27 | `air quality[tiab]` | 12,026 | none |
| 28 | `water pollution[tiab]` | 3,970 | none |
| 29 | `water pollutant*[tiab]` | 669 | none |
| 30 | `soil pollution[tiab]` | 1,171 | none |
| 31 | `chemical exposure[tiab]` | 2,332 | none |
| 32 | `chemical exposures[tiab]` | 1,469 | none |
| 33 | `pesticide exposure[tiab]` | 2,614 | none |
| 34 | `radiation exposure[tiab]` | 20,248 | none |
| 35 | `noise exposure[tiab]` | 4,479 | none |
| 36 | `toxicant*[tiab]` | 12,543 | none |
| 37 | `occupational exposure[tiab]` | 17,828 | none |
| 38 | `occupational exposures[tiab]` | 4,329 | none |
| 39 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 1,492,024 | none |
| 40 | `#11 AND #39` | 9,783 | none |

### Strategy (single line, for copying into PubMed)

```text
((Systematic Reviews as Topic[Mesh] OR systematic[sb] OR systematic review[tiab] OR systematic reviews[tiab] OR systematic literature review[tiab] OR systematic literature reviews[tiab] OR umbrella review[tiab] OR umbrella reviews[tiab] OR meta-review[tiab] OR (meta[tiab] AND review[tiab])) AND (Environmental Health[Mesh] OR Environmental Exposure[Mesh] OR Environmental Pollution[Mesh] OR Air Pollution[Mesh] OR Occupational Exposure[Mesh] OR environment*[tiab] OR environmental exposure[tiab] OR environmental exposures[tiab] OR environmental health[tiab] OR environmental pollutant*[tiab] OR environmental pollution[tiab] OR environmental factor[tiab] OR environmental factors[tiab] OR air pollution[tiab] OR air pollutant*[tiab] OR air quality[tiab] OR water pollution[tiab] OR water pollutant*[tiab] OR soil pollution[tiab] OR chemical exposure[tiab] OR chemical exposures[tiab] OR pesticide exposure[tiab] OR radiation exposure[tiab] OR noise exposure[tiab] OR toxicant*[tiab] OR occupational exposure[tiab] OR occupational exposures[tiab])) AND ("1800/01/01"[edat] : "2020/07/20"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| systematic_reviews | 1,492,024 | 0 |
| environmental_health | 217,641 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 8,068 | initial | none | Initial high-sensitivity draft: systematic-review terminology AND broad environmental health/exposure terminology, with methodology/rigour left for screening. |
| 2 | 8,650 | systematic_reviews: +1 / -1; environmental_health: +0 / -2 | none | Revised after PubMed flagged Systematic Review[Mesh] as unrecognized and authority validation marked two labels ambiguous. Removed the unresolved heading and added PubMed's broader systematic[sb] review filter; retained the validated MeSH descriptors Environmental Health, Environmental Exposure, Environmental Pollution and Air Pollution plus broad text variants. |
| 3 | 9,783 | systematic_reviews: +1 / -1; environmental_health: +12 / -0 | none | Addressed critic round 1: replaced meta review[tiab] with the explicit tested conjunction meta[tiab] AND review[tiab] to cover unhyphenated wording, and broadened environmental text words to include named air/water/soil, chemical, pesticide, radiation, noise, toxicant, and environmental-factor expressions. The eligibility interpretation remains environmental-health reviews; no scope change. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-01 should-fix resolved, R1-02 should-fix resolved
- Round 2 on version 3: 2 findings; R1-01 should-fix resolved, R1-02 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 430 NCBI requests logged (157 from cache); strategy sha256 6f6fc079d749._

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
      "requested": "Systematic Reviews as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:20:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000078202",
          "name": "Systematic Reviews as Topic",
          "type": "descriptor",
          "scope_note": "Works about a review of primary literature in health and health policy that attempt to identify, appraise, and synthesize all the empirical evidence that meets specified eligibility criteria to answer a given research question. It's conducted using explicit methods aimed at minimizing bias in order to produce more reliable findings regarding the effects of interventions for prevention, treatmen...",
          "tree_numbers": [
            "L01.462.500.682.759.575"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000078202",
      "preferred_label": "Systematic Reviews as Topic",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Systematic Reviews as Topic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:20:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004782",
          "name": "Environmental Health",
          "type": "descriptor",
          "scope_note": "The science of controlling or modifying those conditions, influences, or forces surrounding man which relate to promoting, establishing, and maintaining health.",
          "tree_numbers": [
            "H02.229"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004782",
      "preferred_label": "Environmental Health",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "Environmental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Exposure",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:20:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004781",
          "name": "Environmental Exposure",
          "type": "descriptor",
          "scope_note": "The exposure to potentially harmful chemical, physical, or biological agents in the environment or to environmental factors that may include ionizing radiation, pathogenic organisms, or toxic chemicals.",
          "tree_numbers": [
            "N06.850.460.350"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004781",
      "preferred_label": "Environmental Exposure",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "Environmental Exposure",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Pollution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:20:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004787",
          "name": "Environmental Pollution",
          "type": "descriptor",
          "scope_note": "Contamination of the air, bodies of water, or land with substances that are harmful to human health and the environment.",
          "tree_numbers": [
            "N06.850.460"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004787",
      "preferred_label": "Environmental Pollution",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "Environmental Pollution",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Air Pollution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:20:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000397",
          "name": "Air Pollution",
          "type": "descriptor",
          "scope_note": "The presence of contaminants or pollutant substances in the air (AIR POLLUTANTS) that interfere with human health or welfare, or produce other harmful environmental effects. The substances may include GASES; PARTICULATE MATTER; or volatile ORGANIC CHEMICALS.",
          "tree_numbers": [
            "N06.850.460.100"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000397",
      "preferred_label": "Air Pollution",
      "type": "descriptor",
      "location": "vocabulary:15",
      "term": {
        "text": "Air Pollution",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Occupational Exposure",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:20:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016273",
          "name": "Occupational Exposure",
          "type": "descriptor",
          "scope_note": "The exposure to potentially harmful chemical, physical, or biological agents that occurs as a result of one's occupation.",
          "tree_numbers": [
            "N06.850.460.350.600"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016273",
      "preferred_label": "Occupational Exposure",
      "type": "descriptor",
      "location": "vocabulary:16",
      "term": {
        "text": "Occupational Exposure",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"systematic reviews as topic\"[MeSH Terms] OR \"systematic\"[Filter] OR \"systematic review\"[Title/Abstract] OR \"systematic reviews\"[Title/Abstract] OR \"systematic literature review\"[Title/Abstract] OR \"systematic literature reviews\"[Title/Abstract] OR \"umbrella review\"[Title/Abstract] OR \"umbrella reviews\"[Title/Abstract] OR \"meta-review\"[Title/Abstract] OR (\"meta\"[Title/Abstract] AND \"review\"[Title/Abstract])) AND (\"environmental health\"[MeSH Terms] OR \"environmental exposure\"[MeSH Terms] OR \"environmental pollution\"[MeSH Terms] OR \"air pollution\"[MeSH Terms] OR \"occupational exposure\"[MeSH Terms] OR \"environment*\"[Title/Abstract] OR \"environmental exposure\"[Title/Abstract] OR \"environmental exposures\"[Title/Abstract] OR \"environmental health\"[Title/Abstract] OR \"environmental pollutant*\"[Title/Abstract] OR \"environmental pollution\"[Title/Abstract] OR \"environmental factor\"[Title/Abstract] OR \"environmental factors\"[Title/Abstract] OR \"air pollution\"[Title/Abstract] OR \"air pollutant*\"[Title/Abstract] OR \"air quality\"[Title/Abstract] OR \"water pollution\"[Title/Abstract] OR \"water pollutant*\"[Title/Abstract] OR \"soil pollution\"[Title/Abstract] OR \"chemical exposure\"[Title/Abstract] OR \"chemical exposures\"[Title/Abstract] OR \"pesticide exposure\"[Title/Abstract] OR \"radiation exposure\"[Title/Abstract] OR \"noise exposure\"[Title/Abstract] OR \"toxicant*\"[Title/Abstract] OR \"occupational exposure\"[Title/Abstract] OR \"occupational exposures\"[Title/Abstract]) AND 1800/01/01:2020/07/20[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "fb652208573c54e962e1ab5f2d4116b62c4081e33792dfcb445fe19a63dfd16f",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The translation mapped meta review[tiab] to meta-review[Title/Abstract], duplicating the hyphenated term."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within blocks and AND between the two searched concepts matches the recorded scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All retained headings were verified and translated without syntax errors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Specific environmental exposure reviews may not use environment wording; the pilot was selected using environmental-health terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors or translation warnings were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez cutoff is documented and no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "meta review[tiab] translated identically to meta-review[Title/Abstract], leaving the intended unhyphenated expression uncertain.",
          "recommendation": "Test meta[tiab] AND review[tiab] alongside the hyphenated phrase.",
          "status": "resolved",
          "response": "Replaced meta review[tiab] with the explicit conjunction meta[tiab] AND review[tiab]. The new PubMed translation is (meta[Title/Abstract] AND review[Title/Abstract]); evaluation increased the final count from 8,650 to 9,783 and retrieved all 11 development records with no known losses."
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Named exposure reviews may omit environment wording or the listed MeSH descriptors, and the pilot was drawn from environmental-health terminology.",
          "recommendation": "Identify representative named exposure and environmental-condition terms, test them against records, and add supported terms.",
          "status": "resolved",
          "response": "Kept the question's eligibility interpretation fixed and broadened only within the environmental-health block: added environmental factors, air quality, water pollution/pollutants, soil pollution, chemical exposure, pesticide exposure, radiation exposure, noise exposure, and toxicants. Each clause was tested in the full evaluation; the 11 development records remained retrieved and no losses were reported. The block remains a recall-oriented proxy for screening and may still miss reviews whose titles/abstracts and MeSH use only a highly specific exposure label."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "dbc2f096c5258b5b55853ce2062ac0d6d510a65301da91fa99d4be247d87a556",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "meta[tiab] AND review[tiab] translates as intended; other term translations match their fields."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within both concept blocks and AND between blocks matches the recorded scope; rigour remains for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Retained MeSH headings are verified and translate successfully."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Environmental wording has been broadened; the development sample does not independently establish sensitivity for records named only by a specific exposure."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax, translation, or PubMed warning issues are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date-entry cutoff is documented as 2020-07-20; no publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier meta review[tiab] translation duplicated the hyphenated phrase and left the unhyphenated expression uncertain.",
          "recommendation": "Test meta[tiab] AND review[tiab] alongside the hyphenated phrase.",
          "status": "resolved",
          "response": "The revised strategy uses meta[tiab] AND review[tiab], which translates to separate Title/Abstract terms. The full evaluation reports 9,783 results and retrieves all 11 development records, with no known losses."
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Reviews named by specific environmental exposures or conditions may omit general environmental wording or the listed MeSH descriptors; the pilot set was selected using environmental-health terminology.",
          "recommendation": "Identify representative named exposure and environmental-condition terms, test them against records, and add supported terms.",
          "status": "resolved",
          "response": "The environmental block was broadened with environmental factors, air quality, water pollution and pollutants, soil pollution, chemical and pesticide exposure, radiation exposure, noise exposure, and toxicants. Each clause was included in the complete evaluation; all 11 development records remained retrieved with no reported losses. Reviews using only a highly specific exposure label may still be missed."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


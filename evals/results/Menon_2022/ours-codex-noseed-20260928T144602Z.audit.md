# PubMed search strategy: audit

Generated 2026-09-28T15:00:26+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Methodological rigour of systematic reviews in environmental health
- Framework: method + task + application context (PCC-style scope)
- Scope confirmed by user: no (User asked not to pause. Assumptions: environmental health includes environmental medicine, environmental/occupational health, toxicology and population health topics caused by environmental exposures; the target includes studies assessing review conduct, methods, reporting, or bias, not only a single named appraisal tool. No known articles supplied. Scope roles set before discovery. No language/date/publication-type limits; PubMed record inclusion is bounded by Entrez date 2020-07-20 through the harness PSB_AS_OF, not [dp].)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Systematic reviews | search | The target objects being appraised; review type is named/indexed and can be searched broadly. |
| Environmental health | search | Defines the application context in the question; environmental and occupational health wording and indexing will be represented broadly. |
| Methodological rigour/quality of systematic reviews | optional | Central topic, but assessments may be labelled methodological quality, reporting quality, critical appraisal, risk of bias, or by tool name; test an explicit block before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T14:59:53+00:00
- Records added to PubMed up to: 2020-07-20
- Total records: 4,184
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Systematic Reviews as Topic"[Mesh]` | 6,347 | none |
| 2 | `systematic[sb]` | 165,969 | none |
| 3 | `"systematic review"[tiab]` | 160,742 | none |
| 4 | `"systematic reviews"[tiab]` | 30,250 | none |
| 5 | `"systematic literature review"[tiab]` | 11,090 | none |
| 6 | `"systematic literature reviews"[tiab]` | 505 | none |
| 7 | `"evidence synthesis"[tiab]` | 4,462 | none |
| 8 | `"research synthesis"[tiab]` | 540 | none |
| 9 | `meta-analy*[tiab]` | 176,011 | none |
| 10 | `"umbrella review"[tiab]` | 410 | none |
| 11 | `"umbrella reviews"[tiab]` | 40 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 294,848 | none |
| 13 | `"Environmental Health"[Mesh]` | 25,528 | none |
| 14 | `"Environmental Exposure"[Mesh]` | 309,210 | none |
| 15 | `"Occupational Health"[Mesh]` | 34,300 | none |
| 16 | `"Toxicology"[Mesh]` | 33,562 | none |
| 17 | `"environmental health"[tiab]` | 9,584 | none |
| 18 | `"environmental medicine"[tiab]` | 833 | none |
| 19 | `"environmental epidemiology"[tiab]` | 721 | none |
| 20 | `"environmental exposure"[tiab]` | 7,564 | none |
| 21 | `"environmental exposures"[tiab]` | 6,391 | none |
| 22 | `"exposure science"[tiab]` | 146 | none |
| 23 | `"exposure sciences"[tiab]` | 19 | none |
| 24 | `"occupational health"[tiab]` | 15,273 | none |
| 25 | `"occupational medicine"[tiab]` | 3,906 | none |
| 26 | `"occupational exposure"[tiab]` | 17,828 | none |
| 27 | `"occupational exposures"[tiab]` | 4,329 | none |
| 28 | `"environmental toxicology"[tiab]` | 939 | none |
| 29 | `"environmental and occupational"[tiab]` | 1,418 | none |
| 30 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 420,548 | none |
| 31 | `#12 AND #30` | 4,184 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Systematic Reviews as Topic"[Mesh] OR systematic[sb] OR "systematic review"[tiab] OR "systematic reviews"[tiab] OR "systematic literature review"[tiab] OR "systematic literature reviews"[tiab] OR "evidence synthesis"[tiab] OR "research synthesis"[tiab] OR meta-analy*[tiab] OR "umbrella review"[tiab] OR "umbrella reviews"[tiab]) AND ("Environmental Health"[Mesh] OR "Environmental Exposure"[Mesh] OR "Occupational Health"[Mesh] OR "Toxicology"[Mesh] OR "environmental health"[tiab] OR "environmental medicine"[tiab] OR "environmental epidemiology"[tiab] OR "environmental exposure"[tiab] OR "environmental exposures"[tiab] OR "exposure science"[tiab] OR "exposure sciences"[tiab] OR "occupational health"[tiab] OR "occupational medicine"[tiab] OR "occupational exposure"[tiab] OR "occupational exposures"[tiab] OR "environmental toxicology"[tiab] OR "environmental and occupational"[tiab])) AND ("1800/01/01"[edat] : "2020/07/20"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Methodological rigour/quality of systematic reviews | left out | 4,184 / 3,088 | 26.2% | none | 0/30 (up to 10% of removed records could be relevant) | The optional methods/quality block cuts 26.2%, below the roughly 30% materiality criterion. None of the 30 screened lost records evaluates or describes the methods/quality of systematic reviews themselves; they are reviews of environmental topics. Given the recall-first goal and the possibility that method assessment appears only in full text, leave this block out. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| systematic_reviews | 420,548 | 0 |
| environmental_health | 294,848 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 4,184 | initial | none | Initial broad two-block strategy with a separately tested optional methods/quality block; included MeSH, systematic[sb], broad text variants and relevant-record terms. |
| 2 | 4,184 | limits/combination | none | Corrected the optional MeSH candidate to the verified heading Bias after lookup found no Risk of Bias heading; keep quality block un-AND-ed pending fresh sample/decision. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 455 NCBI requests logged (237 from cache); strategy sha256 61ff81113191._

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
      "checked_at": "2026-09-28T14:59:53+00:00",
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
        "text": "\"Systematic Reviews as Topic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:59:53+00:00",
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
        "text": "\"Environmental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Exposure",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:59:53+00:00",
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
        "text": "\"Environmental Exposure\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Occupational Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:59:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016272",
          "name": "Occupational Health",
          "type": "descriptor",
          "scope_note": "The promotion and maintenance of physical and mental health in the work environment.",
          "tree_numbers": [
            "N01.400.525"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016272",
      "preferred_label": "Occupational Health",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Occupational Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Toxicology",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:59:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014116",
          "name": "Toxicology",
          "type": "descriptor",
          "scope_note": "The science concerned with the detection, chemical composition, and biological action of toxic substances or poisons and the treatment and prevention of toxic manifestations.",
          "tree_numbers": [
            "H01.158.891",
            "H02.884"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014116",
      "preferred_label": "Toxicology",
      "type": "descriptor",
      "location": "vocabulary:15",
      "term": {
        "text": "\"Toxicology\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Systematic Reviews as Topic\"[MeSH Terms] OR \"systematic\"[Filter] OR \"systematic review\"[Title/Abstract] OR \"systematic reviews\"[Title/Abstract] OR \"systematic literature review\"[Title/Abstract] OR \"systematic literature reviews\"[Title/Abstract] OR \"evidence synthesis\"[Title/Abstract] OR \"research synthesis\"[Title/Abstract] OR \"meta analy*\"[Title/Abstract] OR \"umbrella review\"[Title/Abstract] OR \"umbrella reviews\"[Title/Abstract]) AND (\"Environmental Health\"[MeSH Terms] OR \"Environmental Exposure\"[MeSH Terms] OR \"Occupational Health\"[MeSH Terms] OR \"Toxicology\"[MeSH Terms] OR \"Environmental Health\"[Title/Abstract] OR \"environmental medicine\"[Title/Abstract] OR \"environmental epidemiology\"[Title/Abstract] OR \"Environmental Exposure\"[Title/Abstract] OR \"environmental exposures\"[Title/Abstract] OR \"exposure science\"[Title/Abstract] OR \"exposure sciences\"[Title/Abstract] OR \"Occupational Health\"[Title/Abstract] OR \"occupational medicine\"[Title/Abstract] OR \"occupational exposure\"[Title/Abstract] OR \"occupational exposures\"[Title/Abstract] OR \"environmental toxicology\"[Title/Abstract] OR \"environmental and occupational\"[Title/Abstract]) AND 1800/01/01:2020/07/20[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "24583eb649a539009b5a7a0dfef4429b5fc4d750d08626122854849b6f050d5d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required searchable concepts are represented by their own terms: systematic review variants and environmental health/context wording. The optional methods and quality concept was tested as a separate block and left out with a stated recall-based rationale."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy ORs synonyms within each concept and ANDs the systematic-review and environmental-health blocks, consistent with the stated scope. The reported counts align with that structure."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verification for the selected MeSH headings. The headings provide broad coverage of systematic reviews, environmental health and exposure, occupational health, and toxicology."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover singular and plural systematic-review forms, evidence and research synthesis, meta-analysis, umbrella reviews, and environmental, exposure, occupational, and toxicology wording. The optional quality block includes relevant assessment labels and tool names; its omission is documented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translations show the intended Boolean grouping and field tags, with no reported errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-type limits are applied. The Entrez date boundary is disclosed as the as-of cutoff, and the packet distinguishes it from a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


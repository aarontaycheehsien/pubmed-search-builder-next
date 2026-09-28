# PubMed search strategy: audit

Generated 2026-09-28T19:32:17+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Methodological rigour of systematic reviews in environmental health
- Framework: method + application context (environmental health); systematic reviews are the review type under study
- Scope confirmed by user: no (User asked to proceed without questions; scope was not confirmed. Assumption: this concerns the methods/quality of systematic reviews in environmental health, including both methodological evaluations of review corpora and individual systematic reviews when their rigor is the object of review. No language, geography, or publication-date limits. PubMed records are bounded by Entrez date through PSB_AS_OF=2020-07-20, not a publication-date limit. No known relevant records were supplied; attempt standard-depth discovery, but if no records can be screened in, recall will remain unestimated and the strategy empirically unvalidated.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Systematic reviews and evidence syntheses | search | The review type is essential to eligibility and is usually identified in titles/abstracts or MeSH; include related review labels because records may name a review subtype rather than the general category. |
| Methodological rigour, quality, conduct, or reporting of reviews | optional | This topic-defining property is inconsistently reported and is not a category whose named members require probing. It was tested as an optional block and left out after screened losses showed relevant environmental-health systematic reviews do not consistently label rigor or quality in searchable metadata. |
| Environmental health application | optional | The application context is central but can be expressed through environmental exposures or specific environmental-health domains rather than the umbrella phrase; test before deciding whether to AND it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T19:31:09+00:00
- Records added to PubMed up to: 2020-07-20
- Total records: 5,600
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Systematic Reviews as Topic[Mesh]` | 6,347 | none |
| 2 | `Review Literature as Topic[Mesh]` | 18,599 | none |
| 3 | `Meta-Analysis[Mesh]` | 20,321 | none |
| 4 | `Meta-Analysis as Topic[Mesh]` | 20,321 | none |
| 5 | `systematic review[tiab]` | 160,742 | none |
| 6 | `systematic reviews[tiab]` | 30,250 | none |
| 7 | `systematic literature review[tiab]` | 11,090 | none |
| 8 | `systematic literature reviews[tiab]` | 505 | none |
| 9 | `umbrella review[tiab]` | 410 | none |
| 10 | `umbrella reviews[tiab]` | 40 | none |
| 11 | `overview of reviews[tiab]` | 144 | none |
| 12 | `overviews of reviews[tiab]` | 38 | none |
| 13 | `scoping review[tiab]` | 5,988 | none |
| 14 | `scoping reviews[tiab]` | 406 | none |
| 15 | `systematic map[tiab]` | 58 | none |
| 16 | `systematic maps[tiab]` | 14 | none |
| 17 | `systematic mapping[tiab]` | 394 | none |
| 18 | `meta-analysis[tiab]` | 152,699 | none |
| 19 | `meta-analyses[tiab]` | 38,218 | none |
| 20 | `meta-analy*[tiab]` | 176,011 | none |
| 21 | `evidence synthesis[tiab]` | 4,462 | none |
| 22 | `evidence syntheses[tiab]` | 234 | none |
| 23 | `research synthesis[tiab]` | 540 | none |
| 24 | `research syntheses[tiab]` | 84 | none |
| 25 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 303,826 | none |
| 26 | `Environment Design[Mesh]` | 7,235 | none |
| 27 | `Environmental Health[Mesh]` | 25,528 | none |
| 28 | `Environmental Exposure[Mesh]` | 309,210 | none |
| 29 | `Occupational Health[Mesh]` | 34,300 | none |
| 30 | `Air Pollution[Mesh]` | 59,328 | none |
| 31 | `Water Pollution[Mesh]` | 28,577 | none |
| 32 | `environmental health[tiab]` | 9,584 | none |
| 33 | `environmental exposure[tiab]` | 7,564 | none |
| 34 | `environmental exposures[tiab]` | 6,391 | none |
| 35 | `environmental epidemiology[tiab]` | 721 | none |
| 36 | `environmental toxicology[tiab]` | 939 | none |
| 37 | `environmental health science*[tiab]` | 587 | none |
| 38 | `exposure science[tiab]` | 146 | none |
| 39 | `exposure sciences[tiab]` | 19 | none |
| 40 | `environmental medicine[tiab]` | 833 | none |
| 41 | `"occupational and environmental health"[tiab]` | 540 | none |
| 42 | `occupational health[tiab]` | 15,273 | none |
| 43 | `air pollution[tiab]` | 27,926 | none |
| 44 | `water pollution[tiab]` | 3,970 | none |
| 45 | `chemical exposure[tiab]` | 2,332 | none |
| 46 | `chemical exposures[tiab]` | 1,469 | none |
| 47 | `environmental contaminant*[tiab]` | 6,008 | none |
| 48 | `environmental pollutant*[tiab]` | 7,573 | none |
| 49 | `environmental hazard*[tiab]` | 2,659 | none |
| 50 | `pesticide exposure[tiab]` | 2,614 | none |
| 51 | `toxicology[tiab]` | 38,146 | none |
| 52 | `built environment[tiab]` | 3,357 | none |
| 53 | `activity space*[tiab]` | 301 | none |
| 54 | `environmental determinant*[tiab]` | 2,006 | none |
| 55 | `#26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54` | 495,964 | none |
| 56 | `#25 AND #55` | 5,600 | none |

### Strategy (single line, for copying into PubMed)

```text
((Systematic Reviews as Topic[Mesh] OR Review Literature as Topic[Mesh] OR Meta-Analysis[Mesh] OR Meta-Analysis as Topic[Mesh] OR systematic review[tiab] OR systematic reviews[tiab] OR systematic literature review[tiab] OR systematic literature reviews[tiab] OR umbrella review[tiab] OR umbrella reviews[tiab] OR overview of reviews[tiab] OR overviews of reviews[tiab] OR scoping review[tiab] OR scoping reviews[tiab] OR systematic map[tiab] OR systematic maps[tiab] OR systematic mapping[tiab] OR meta-analysis[tiab] OR meta-analyses[tiab] OR meta-analy*[tiab] OR evidence synthesis[tiab] OR evidence syntheses[tiab] OR research synthesis[tiab] OR research syntheses[tiab]) AND (Environment Design[Mesh] OR Environmental Health[Mesh] OR Environmental Exposure[Mesh] OR Occupational Health[Mesh] OR Air Pollution[Mesh] OR Water Pollution[Mesh] OR environmental health[tiab] OR environmental exposure[tiab] OR environmental exposures[tiab] OR environmental epidemiology[tiab] OR environmental toxicology[tiab] OR environmental health science*[tiab] OR exposure science[tiab] OR exposure sciences[tiab] OR environmental medicine[tiab] OR "occupational and environmental health"[tiab] OR occupational health[tiab] OR air pollution[tiab] OR water pollution[tiab] OR chemical exposure[tiab] OR chemical exposures[tiab] OR environmental contaminant*[tiab] OR environmental pollutant*[tiab] OR environmental hazard*[tiab] OR pesticide exposure[tiab] OR toxicology[tiab] OR built environment[tiab] OR activity space*[tiab] OR environmental determinant*[tiab])) AND ("1800/01/01"[edat] : "2020/07/20"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 28 | 28 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Methodological rigour, quality, conduct, or reporting of reviews | left out | 5,600 / 3,385 | 39.6% | 8287841, 10193379, 10725502, 17428724, 17492303, 18629304, 18652979, 20064771, 23226111, 23525899, 23570911, 25455669, 27871551, 28350135, 30071659, 30400886, 30700018, 30806521, 31401745, 32096774, 32146339, 32217755, 32300088, 32477512 | 11/30 | A required rigor/quality block would lose the 11 newly screened environmental-health systematic reviews/meta-analyses from the refreshed sample, in addition to 13 earlier known records. This outcome/property is not reliably named, and the review aims to assess rigor across those reviews; therefore screen methodological rigor rather than require its metadata terms. |
| Environmental health application | AND-ed | 303,826 / 5,600 | 98.2% | none | 0/30 (up to 10% of removed records could be relevant) | Environmental-health context defines eligibility, and this block reduces the count by about 98% while retrieving all 17 screened development records, including the activity-spaces review discovered in the category probe. The refreshed 30-record loss sample contained no eligible records. The block was widened with Environment Design and activity-space terms after probing. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Systematic reviews and evidence syntheses | 1 | `review*[tiab] OR systematic[sb] OR Systematic Review[pt] OR Meta-Analysis[pt] OR Meta-Analysis[Mesh] OR evidence synthesis[tiab]` | 33,263 | 0/30 |
| Systematic reviews and evidence syntheses | 2 | `review*[tiab] OR systematic[sb] OR Systematic Review[pt] OR Meta-Analysis[pt] OR Meta-Analysis[Mesh] OR evidence synthesis[tiab]` | 33,974 | 0/30 |
| Environmental health application | 1 | `Exposure[Mesh] OR environmental*[tiab] OR exposure*[tiab] OR pollut*[tiab] OR occupational[tiab] OR toxin*[tiab] OR chemical*[tiab]` | 15,954 | 1/30 |
| Environmental health application | 2 | `Exposure[Mesh] OR environmental*[tiab] OR exposure*[tiab] OR pollut*[tiab] OR occupational[tiab] OR toxin*[tiab] OR chemical*[tiab]` | 15,763 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| systematic_reviews | 495,964 | 0 |
| environmental_health | 303,826 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first blocks drafted from question scope, MeSH lookup, and three screened environmental-health methodology records; method quality and application context tested as optional concepts. |
| 2 | 0 | limits/combination | none | Corrected Boolean parsing by explicitly quoting the environmental phrase containing the word and; then evaluated draft with dated PubMed access. |
| 3 | 303,826 | limits/combination | none | Set combine to default AND of block IDs; optional methods and context remain candidates for measured decisions. |
| 4 | 5,517 | environmental_health: +26 / -0 | none | AND-ed environmental context after its 30-record optional loss sample contained no eligible records and the block reduced screening burden substantially. |
| 5 | 5,249 | environmental_health: +0 / -1 | none | Removed the ambiguous Environmental Pollutants authority match; retain validated Environmental Exposure and explicit pollutant/exposure terms. |
| 6 | 5,600 | environmental_health: +4 / -0 | none | Category probe found one relevant environmental-health systematic review on activity spaces and environment design; added Environment Design MeSH and built-environment/activity-space terms. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 6: 0 findings; 
- Round 2 on version 6: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1466 NCBI requests logged (614 from cache); strategy sha256 5f16f3b6b511._

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
      "checked_at": "2026-09-28T19:31:09+00:00",
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
      "requested": "Review Literature as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012196",
          "name": "Review Literature as Topic",
          "type": "descriptor",
          "scope_note": "Works about published materials which provide an examination of recent or current literature. These articles can cover a wide range of subject matter at various levels of completeness and comprehensiveness based on analyses of literature that may include research findings. The review may reflect the state of the art and may also include reviews as a literary form.",
          "tree_numbers": [
            "L01.462.500.682.759"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012196",
      "preferred_label": "Review Literature as Topic",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Review Literature as Topic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Meta-Analysis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017418",
          "name": "Meta-Analysis",
          "type": "descriptor",
          "scope_note": "Works consisting of studies using a quantitative method of combining the results of independent studies (usually drawn from the published literature) and synthesizing summaries and conclusions which may be used to evaluate therapeutic effectiveness, plan new studies, etc. It is often an overview of clinical trials. It is usually called a meta-analysis by the author or sponsoring body and should...",
          "tree_numbers": [
            "V02.912.625.504",
            "V03.500.004",
            "V03.600"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017418",
      "preferred_label": "Meta-Analysis",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Meta-Analysis",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Meta-Analysis as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015201",
          "name": "Meta-Analysis as Topic",
          "type": "descriptor",
          "scope_note": "A quantitative method of combining the results of independent studies (usually drawn from the published literature) and synthesizing summaries and conclusions which may be used to evaluate therapeutic effectiveness, plan new studies, etc., with application chiefly in the areas of research and medicine.",
          "tree_numbers": [
            "E05.318.370.500",
            "E05.581.500.501",
            "N05.715.360.325.515",
            "N06.850.520.445.500"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015201",
      "preferred_label": "Meta-Analysis as Topic",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "Meta-Analysis as Topic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environment Design",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004779",
          "name": "Environment Design",
          "type": "descriptor",
          "scope_note": "The structuring of the environment to permit or promote specific patterns of behavior.",
          "tree_numbers": [
            "I01.283",
            "I01.880.709.359",
            "N06.230.145"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004779",
      "preferred_label": "Environment Design",
      "type": "descriptor",
      "location": "vocabulary:25",
      "term": {
        "text": "Environment Design",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "Environmental Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Exposure",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "Environmental Exposure",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Occupational Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "Occupational Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Air Pollution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Air Pollution",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Water Pollution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T19:31:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014876",
          "name": "Water Pollution",
          "type": "descriptor",
          "scope_note": "Contamination of bodies of water (such as LAKES; RIVERS; SEAS; and GROUNDWATER.)",
          "tree_numbers": [
            "N06.850.460.790"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014876",
      "preferred_label": "Water Pollution",
      "type": "descriptor",
      "location": "vocabulary:30",
      "term": {
        "text": "Water Pollution",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"systematic reviews as topic\"[MeSH Terms] OR \"review literature as topic\"[MeSH Terms] OR \"meta analysis as topic\"[MeSH Terms] OR \"meta analysis as topic\"[MeSH Terms] OR \"systematic review\"[Title/Abstract] OR \"systematic reviews\"[Title/Abstract] OR \"systematic literature review\"[Title/Abstract] OR \"systematic literature reviews\"[Title/Abstract] OR \"umbrella review\"[Title/Abstract] OR \"umbrella reviews\"[Title/Abstract] OR \"overview of reviews\"[Title/Abstract] OR \"overviews of reviews\"[Title/Abstract] OR \"scoping review\"[Title/Abstract] OR \"scoping reviews\"[Title/Abstract] OR \"systematic map\"[Title/Abstract] OR \"systematic maps\"[Title/Abstract] OR \"systematic mapping\"[Title/Abstract] OR \"meta-analysis\"[Title/Abstract] OR \"meta-analyses\"[Title/Abstract] OR \"meta analy*\"[Title/Abstract] OR \"evidence synthesis\"[Title/Abstract] OR \"evidence syntheses\"[Title/Abstract] OR \"research synthesis\"[Title/Abstract] OR \"research syntheses\"[Title/Abstract]) AND (\"environment design\"[MeSH Terms] OR \"environmental health\"[MeSH Terms] OR \"environmental exposure\"[MeSH Terms] OR \"occupational health\"[MeSH Terms] OR \"air pollution\"[MeSH Terms] OR \"water pollution\"[MeSH Terms] OR \"environmental health\"[Title/Abstract] OR \"environmental exposure\"[Title/Abstract] OR \"environmental exposures\"[Title/Abstract] OR \"environmental epidemiology\"[Title/Abstract] OR \"environmental toxicology\"[Title/Abstract] OR \"environmental health science*\"[Title/Abstract] OR \"exposure science\"[Title/Abstract] OR \"exposure sciences\"[Title/Abstract] OR \"environmental medicine\"[Title/Abstract] OR \"occupational and environmental health\"[Title/Abstract] OR \"occupational health\"[Title/Abstract] OR \"air pollution\"[Title/Abstract] OR \"water pollution\"[Title/Abstract] OR \"chemical exposure\"[Title/Abstract] OR \"chemical exposures\"[Title/Abstract] OR \"environmental contaminant*\"[Title/Abstract] OR \"environmental pollutant*\"[Title/Abstract] OR \"environmental hazard*\"[Title/Abstract] OR \"pesticide exposure\"[Title/Abstract] OR \"toxicology\"[Title/Abstract] OR \"built environment\"[Title/Abstract] OR \"activity space*\"[Title/Abstract] OR \"environmental determinant*\"[Title/Abstract]) AND 1800/01/01:2020/07/20[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 6,
      "review_sha256": "dad8057fa2aa0faa0c0f7246838334fa1aba98277c519d415a6a1cd2682a18e3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility's named review types are represented by their own text phrases or subject headings. Translation issues are empty, and the packet reports no query warnings or errors."
        },
        "operators": {
          "verdict": "pass",
          "note": "The review-type and environmental-health blocks are ORed internally and ANDed together as required by the stated scope. No process-direction terms or proximity operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes review and environmental-health headings; the packet reports verified headings and successful translation. The two Meta-Analysis headings translate identically, a harmless redundancy."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the review types named in eligibility and a range of environmental-health applications. The category probes and widened environmental block provide evidence for the retained application block; all 28 known relevant records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is parenthesized by block and combines the blocks with AND. The packet reports no syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, geography, or publication-date limits are applied. The documented Entrez date range ends at the stated as-of date and is not presented as a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "dad8057fa2aa0faa0c0f7246838334fa1aba98277c519d415a6a1cd2682a18e3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched review types are represented by their own text phrases or subject headings. The optional rigor block was tested and omitted based on relevant records lost, consistent with the stated scope."
        },
        "operators": {
          "verdict": "pass",
          "note": "Review types and environmental-health applications are ORed within their blocks, then ANDed. No process-direction or proximity terms are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes review and environmental-health subject headings. The duplicate Meta-Analysis headings translate identically and are harmless."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover the named review types and a range of environmental-health applications. The packet documents probing and widening the application block, and retrieval of all screened development records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query combines parenthesized concept blocks with AND. The packet reports no syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, geography, or publication-date limits are applied. The documented Entrez date range is not presented as a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


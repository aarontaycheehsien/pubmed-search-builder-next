# PubMed search strategy: audit

Generated 2026-09-28T19:00:16+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Methodological rigour of systematic reviews in environmental health
- Framework: method + task + application context
- Scope confirmed by user: no (User asked to proceed without questions; scope assumed to treat individual systematic reviews of human health and environmental exposures/determinants as the units to appraise for methodological rigour (rather than searching only meta-research papers that already evaluate reviews). No known relevant articles supplied. PubMed is bounded by Entrez date 2020-07-20 via PSB_AS_OF; no publication-date limit. Environmental health is treated as an optional category concept because relevant reviews may name only member exposures or outcomes.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Systematic reviews | search | The records to be appraised are systematic reviews; the review type is explicit and searchable. |
| Environmental health | optional | Application context defines the topic and is often searchable by explicit labels, but relevant reviews may name only a specific environmental exposure or health outcome; test before requiring it. |
| Methodological rigour or quality | screen | This is the appraisal property, often not stated consistently in title/abstract and best judged from the review's methods or appraisal results. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T18:58:53+00:00
- Records added to PubMed up to: 2020-07-20
- Total records: 5,267
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Systematic Reviews as Topic[Mesh]` | 6,347 | none |
| 2 | `systematic[sb]` | 165,969 | none |
| 3 | `"systematic review"[tiab]` | 160,742 | none |
| 4 | `"systematic reviews"[tiab]` | 30,250 | none |
| 5 | `"systematic literature review"[tiab]` | 11,090 | none |
| 6 | `"systematic literature reviews"[tiab]` | 505 | none |
| 7 | `"umbrella review"[tiab]` | 410 | none |
| 8 | `"umbrella reviews"[tiab]` | 40 | none |
| 9 | `"review of reviews"[tiab]` | 373 | none |
| 10 | `"evidence synthesis"[tiab]` | 4,462 | none |
| 11 | `"evidence syntheses"[tiab]` | 234 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 203,175 | none |
| 13 | `Environmental Health[Mesh]` | 25,528 | none |
| 14 | `Environmental Exposure[Mesh]` | 309,210 | none |
| 15 | `Occupational Exposure[Mesh]` | 64,382 | none |
| 16 | `Occupational Health[Mesh]` | 34,300 | none |
| 17 | `Occupational Diseases[Mesh]` | 134,256 | none |
| 18 | `Working Conditions[Mesh]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 19 | `Workplace[Mesh]` | 24,315 | none |
| 20 | `Dermatitis, Occupational[Mesh]` | 8,249 | none |
| 21 | `Shift Work Schedule[Mesh]` | 659 | none |
| 22 | `Air Pollution[Mesh]` | 59,328 | none |
| 23 | `Air Pollution, Indoor[Mesh]` | 13,995 | none |
| 24 | `Particulate Matter[Mesh]` | 64,939 | none |
| 25 | `Radon[Mesh]` | 6,106 | none |
| 26 | `Water Pollution[Mesh]` | 28,577 | none |
| 27 | `Water Supply[Mesh]` | 33,492 | none |
| 28 | `Water Microbiology[Mesh]` | 33,793 | none |
| 29 | `Vehicle Emissions[Mesh]` | 10,185 | none |
| 30 | `Cold Climate[Mesh]` | 2,939 | none |
| 31 | `Hot Temperature[Mesh]` | 119,536 | none |
| 32 | `"environmental health"[tiab]` | 9,584 | none |
| 33 | `environmental exposure*[tiab]` | 13,468 | none |
| 34 | `environmental toxicant*[tiab]` | 1,950 | none |
| 35 | `environmental pollut*[tiab]` | 14,708 | none |
| 36 | `environmental determinant*[tiab]` | 2,006 | none |
| 37 | `environmental epidemiolog*[tiab]` | 899 | none |
| 38 | `"air pollution"[tiab]` | 27,926 | none |
| 39 | `air pollutant*[tiab]` | 9,409 | none |
| 40 | `"water pollution"[tiab]` | 3,970 | none |
| 41 | `water distribution system*[tiab]` | 1,273 | none |
| 42 | `water supply[tiab]` | 10,119 | none |
| 43 | `waterborne[tiab]` | 7,287 | none |
| 44 | `"water borne"[tiab]` | 1,690 | none |
| 45 | `pesticide*[tiab]` | 49,652 | none |
| 46 | `radon[tiab]` | 6,782 | none |
| 47 | `diesel[tiab]` | 8,578 | none |
| 48 | `"diesel exhaust"[tiab]` | 2,522 | none |
| 49 | `"chemical exposure*"[tiab]` | 3,632 | none |
| 50 | `"occupational exposure*"[tiab]` | 21,001 | none |
| 51 | `"shift work"[tiab]` | 4,014 | none |
| 52 | `"night shift"[tiab]` | 2,168 | none |
| 53 | `"contact dermatitis"[tiab]` | 13,840 | none |
| 54 | `"occupational dermatitis"[tiab]` | 955 | none |
| 55 | `"built environment"[tiab]` | 3,357 | none |
| 56 | `"neighborhood environment"[tiab]` | 715 | none |
| 57 | `"neighbourhood environment"[tiab]` | 183 | none |
| 58 | `workplace[tiab]` | 37,576 | none |
| 59 | `working condition*[tiab]` | 10,316 | none |
| 60 | `"workplace polic*"[tiab]` | 333 | none |
| 61 | `"workplace environment"[tiab]` | 605 | none |
| 62 | `"noise exposure"[tiab]` | 4,479 | none |
| 63 | `"ambient temperature"[tiab]` | 17,080 | none |
| 64 | `"high ambient temperature"[tiab]` | 747 | none |
| 65 | `"low ambient temperature"[tiab]` | 334 | none |
| 66 | `temperature exposure*[tiab]` | 744 | none |
| 67 | `"environment-based"[tiab]` | 569 | none |
| 68 | `"environment based"[tiab]` | 569 | none |
| 69 | `"environmental design"[tiab]` | 264 | none |
| 70 | `"home environment"[tiab]` | 4,547 | none |
| 71 | `"noise regulation"[tiab]` | 25 | none |
| 72 | `"climate change"[tiab]` | 34,679 | none |
| 73 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72` | 891,547 | none |
| 74 | `#12 AND #73` | 5,267 | none |

### Strategy (single line, for copying into PubMed)

```text
((Systematic Reviews as Topic[Mesh] OR systematic[sb] OR "systematic review"[tiab] OR "systematic reviews"[tiab] OR "systematic literature review"[tiab] OR "systematic literature reviews"[tiab] OR "umbrella review"[tiab] OR "umbrella reviews"[tiab] OR "review of reviews"[tiab] OR "evidence synthesis"[tiab] OR "evidence syntheses"[tiab]) AND (Environmental Health[Mesh] OR Environmental Exposure[Mesh] OR Occupational Exposure[Mesh] OR Occupational Health[Mesh] OR Occupational Diseases[Mesh] OR Working Conditions[Mesh] OR Workplace[Mesh] OR Dermatitis, Occupational[Mesh] OR Shift Work Schedule[Mesh] OR Air Pollution[Mesh] OR Air Pollution, Indoor[Mesh] OR Particulate Matter[Mesh] OR Radon[Mesh] OR Water Pollution[Mesh] OR Water Supply[Mesh] OR Water Microbiology[Mesh] OR Vehicle Emissions[Mesh] OR Cold Climate[Mesh] OR Hot Temperature[Mesh] OR "environmental health"[tiab] OR environmental exposure*[tiab] OR environmental toxicant*[tiab] OR environmental pollut*[tiab] OR environmental determinant*[tiab] OR environmental epidemiolog*[tiab] OR "air pollution"[tiab] OR air pollutant*[tiab] OR "water pollution"[tiab] OR water distribution system*[tiab] OR water supply[tiab] OR waterborne[tiab] OR "water borne"[tiab] OR pesticide*[tiab] OR radon[tiab] OR diesel[tiab] OR "diesel exhaust"[tiab] OR "chemical exposure*"[tiab] OR "occupational exposure*"[tiab] OR "shift work"[tiab] OR "night shift"[tiab] OR "contact dermatitis"[tiab] OR "occupational dermatitis"[tiab] OR "built environment"[tiab] OR "neighborhood environment"[tiab] OR "neighbourhood environment"[tiab] OR workplace[tiab] OR working condition*[tiab] OR "workplace polic*"[tiab] OR "workplace environment"[tiab] OR "noise exposure"[tiab] OR "ambient temperature"[tiab] OR "high ambient temperature"[tiab] OR "low ambient temperature"[tiab] OR temperature exposure*[tiab] OR "environment-based"[tiab] OR "environment based"[tiab] OR "environmental design"[tiab] OR "home environment"[tiab] OR "noise regulation"[tiab] OR "climate change"[tiab])) AND ("1800/01/01"[edat] : "2020/07/20"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 18 | 18 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Environmental health | AND-ed | 203,175 / 5,267 | 97.4% | none | 0/30 (up to 10% of removed records could be relevant) | Keep the environmental-health block after expanding it to include the member-only categories found during screening. The latest 30-record outside-block sample (seed 91) had no eligible records; both eligible records found in the prior optional sample (PMIDs 18042349 and 28809653) were added to development and are now retrieved by the expanded block. The earlier full comparison reduced the systematic-review set by about 98%; the updated block continues to reduce it materially. This remains a sensitivity risk because category probes found member-only records and the broader category space cannot be exhausted. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Environmental health | 1 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab]` | 10,610 | not screened |
| Environmental health | 2 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab]` | 10,610 | 4/30 |
| Environmental health | 3 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab] OR workplace[tiab] OR radiation[tiab] OR heat[tiab] OR housing[tiab]` | 13,029 | not screened |
| Environmental health | 4 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab] OR workplace[tiab] OR radiation[tiab] OR heat[tiab] OR housing[tiab]` | 13,029 | 1/30 |
| Environmental health | 5 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab] OR workplace[tiab] OR radiation[tiab] OR heat[tiab] OR housing[tiab] OR determinant*[tiab] OR radon[tiab]` | 15,064 | not screened |
| Environmental health | 6 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab] OR workplace[tiab] OR radiation[tiab] OR heat[tiab] OR housing[tiab] OR determinant*[tiab] OR radon[tiab]` | 15,064 | not screened |
| Environmental health | 7 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab] OR workplace[tiab] OR radiation[tiab] OR heat[tiab] OR housing[tiab] OR determinant*[tiab] OR radon[tiab] OR shift*[tiab] OR dermatitis[tiab]` | 16,039 | not screened |
| Environmental health | 8 | `Environmental Exposure[Mesh] OR exposure*[tiab] OR pollutant*[tiab] OR contaminant*[tiab] OR chemical*[tiab] OR pesticide*[tiab] OR air[tiab] OR water[tiab] OR noise[tiab] OR climate[tiab] OR neighborhood[tiab] OR occupational[tiab] OR workplace[tiab] OR radiation[tiab] OR heat[tiab] OR housing[tiab] OR determinant*[tiab] OR radon[tiab] OR shift*[tiab] OR dermatitis[tiab]` | 16,039 | 1/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| systematic_review | 891,547 | 0 |
| environmental_health | 203,175 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 203,175 | initial | none | Initial two-concept search: systematic review type mandatory; environmental-health application context left optional for measured loss test. Vocabulary includes MeSH and title/abstract labels. |
| 2 | 203,175 | systematic_review: +9 / -10 | none | Removed the zero-hit, unrecognized Systematic Review[Mesh] clause after PubMed returned phrase-not-found and zero-hit evidence; retained the valid Systematic Reviews as Topic heading, validated systematic[sb] filter, and text words. Quoted multiword text phrases explicitly. |
| 3 | 203,175 | limits/combination | none | Category probe 2 identified relevant reviews named only by water system/waterborne health, shift-work, and occupational dermatitis terms. Added their bare member terms and applicable MeSH headings to the optional environmental-health category block. |
| 4 | 4,069 | environmental_health: +36 / -0 | none | Required environmental-health context after optional-loss screening (0 relevant of 30; 98.0% count reduction); block widened to cover four member-only reviews discovered by category probe. |
| 5 | 3,978 | environmental_health: +0 / -1 | none | Removed Environmental Pollutants[Mesh] after the live authority verifier returned duplicate records and a blocking ambiguity; other verified environment/exposure and member headings remain. |
| 6 | 4,035 | environmental_health: +2 / -0 | none | Added MeSH Air Pollutants and Particulate Matter, mined from the development relevant set, as high-sensitivity member terms. |
| 7 | 4,020 | environmental_health: +0 / -1 | none | Did not retain Air Pollutants[Mesh] because the authority verifier returned duplicate summaries and a blocking ambiguity; the block keeps air pollutant text and verified Particulate Matter[Mesh]. |
| 8 | 4,036 | environmental_health: +2 / -0 | none | Re-measured and retained environmental-health block after current 30-record loss sample found no relevant records; probe-derived radon and member terms included. |
| 9 | 4,082 | environmental_health: +1 / -0 | none | Added environmental determinant*[tiab] as the bare text-word form of the eligibility concept, following critic finding P1-02. |
| 10 | 5,020 | environmental_health: +7 / -0 | none | Added Occupational Health, Working Conditions, Workplace MeSH and workplace policy/environment text after screened probe 6 found an in-scope workplace environmental-determinants review. |
| 11 | 5,024 | environmental_health: +3 / -0 | none | Added Vehicle Emissions MeSH, diesel[tiab], and diesel exhaust[tiab] after screening probe 8 identified an eligible systematic review of diesel exposure and lung cancer. |
| 12 | 5,174 | environmental_health: +6 / -0 | none | The outside-block loss sample found an eligible ambient-temperature review (PMID 18042349). Added it to development and expanded the environmental-health block with temperature-specific MeSH and text terms, including ambient temperature wording. |
| 13 | 5,267 | environmental_health: +5 / -0 | none | Optional-context loss sampling found two relevant member-only records: PMID 18042349 on ambient temperature and PMID 28809653 on environment-based interventions. Added both to development and broadened environmental-health terms for temperature, built/home environment, noise regulation, and environment-based interventions. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 13: 1 findings; F1 must-fix resolved
- Round 2 on version 13: 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 3101 NCBI requests logged (1795 from cache); strategy sha256 9ebcc68bb7ee._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:environmental_health",
        "pmids": [
          "24473109"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-111541572eb1a07c5fc8"
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(Working Conditions[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/07/20\"[edat])",
        "translation": "\"working conditions\"[MeSH Terms] AND 1800/01/01:2020/07/20[Date - Entry]",
        "location": "line:18",
        "blocking": false,
        "requires_review": true,
        "id": "I-96df2d4e3fb0f99ded8e"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(Working Conditions[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/07/20\"[edat])",
        "translation": "\"working conditions\"[MeSH Terms] AND 1800/01/01:2020/07/20[Date - Entry]",
        "location": "line:18",
        "blocking": false,
        "requires_review": true,
        "id": "I-2f5bccd710fac585146d"
      }
    ],
    "issues": [
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:environmental_health",
        "pmids": [
          "24473109"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-111541572eb1a07c5fc8"
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(Working Conditions[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/07/20\"[edat])",
        "translation": "\"working conditions\"[MeSH Terms] AND 1800/01/01:2020/07/20[Date - Entry]",
        "location": "line:18",
        "blocking": false,
        "requires_review": true,
        "id": "I-96df2d4e3fb0f99ded8e"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(Working Conditions[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/07/20\"[edat])",
        "translation": "\"working conditions\"[MeSH Terms] AND 1800/01/01:2020/07/20[Date - Entry]",
        "location": "line:18",
        "blocking": false,
        "requires_review": true,
        "id": "I-2f5bccd710fac585146d"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Systematic Reviews as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
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
      "checked_at": "2026-09-28T18:58:53+00:00",
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
      "checked_at": "2026-09-28T18:58:53+00:00",
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
      "requested": "Occupational Exposure",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Occupational Exposure",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Occupational Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "Occupational Health",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Occupational Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009784",
          "name": "Occupational Diseases",
          "type": "descriptor",
          "scope_note": "Diseases caused by factors involved in one's employment.",
          "tree_numbers": [
            "C24"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009784",
      "preferred_label": "Occupational Diseases",
      "type": "descriptor",
      "location": "vocabulary:16",
      "term": {
        "text": "Occupational Diseases",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Working Conditions",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000092922",
          "name": "Working Conditions",
          "type": "descriptor",
          "scope_note": "Conditions of a WORKPLACE such as weather (e.g., indoor or outdoor), safety (e.g., exposure to hazardous materials), environment and workplace culture and management style.",
          "tree_numbers": [
            "N01.824.245.925.500",
            "N04.452.677.975.500"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000092922",
      "preferred_label": "Working Conditions",
      "type": "descriptor",
      "location": "vocabulary:17",
      "term": {
        "text": "Working Conditions",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Workplace",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017132",
          "name": "Workplace",
          "type": "descriptor",
          "scope_note": "Place or physical location of work or employment.",
          "tree_numbers": [
            "N01.824.245.925",
            "N04.452.677.975"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017132",
      "preferred_label": "Workplace",
      "type": "descriptor",
      "location": "vocabulary:18",
      "term": {
        "text": "Workplace",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dermatitis, Occupational",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009783",
          "name": "Dermatitis, Occupational",
          "type": "descriptor",
          "scope_note": "A recurrent contact dermatitis caused by substances found in the work place.",
          "tree_numbers": [
            "C17.800.174.255.700",
            "C17.800.815.255.700",
            "C24.270"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009783",
      "preferred_label": "Dermatitis, Occupational",
      "type": "descriptor",
      "location": "vocabulary:19",
      "term": {
        "text": "Dermatitis, Occupational",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Shift Work Schedule",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000073577",
          "name": "Shift Work Schedule",
          "type": "descriptor",
          "scope_note": "Job schedule in which working hours deviate from the standard hours (e.g., evening shift, night shift or rotating shift).",
          "tree_numbers": [
            "I03.946.225.250",
            "N04.452.677.650.250"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000073577",
      "preferred_label": "Shift Work Schedule",
      "type": "descriptor",
      "location": "vocabulary:20",
      "term": {
        "text": "Shift Work Schedule",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Air Pollution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Air Pollution",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Air Pollution, Indoor",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016902",
          "name": "Air Pollution, Indoor",
          "type": "descriptor",
          "scope_note": "The contamination of indoor air.",
          "tree_numbers": [
            "N06.850.460.100.080"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016902",
      "preferred_label": "Air Pollution, Indoor",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "Air Pollution, Indoor",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Particulate Matter",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D052638",
          "name": "Particulate Matter",
          "type": "descriptor",
          "scope_note": "Particles of any solid substance, generally under 30 microns in size, often noted as PM30. There is special concern with PM1 which can get down to PULMONARY ALVEOLI and induce MACROPHAGE ACTIVATION and PHAGOCYTOSIS leading to FOREIGN BODY REACTION and LUNG DISEASES.",
          "tree_numbers": [
            "D20.633"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D052638",
      "preferred_label": "Particulate Matter",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "Particulate Matter",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Radon",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011886",
          "name": "Radon",
          "type": "descriptor",
          "scope_note": "A naturally radioactive element with atomic symbol Rn, and atomic number 86. It is a member of the noble gas family found in soil, and is released during the decay of RADIUM.",
          "tree_numbers": [
            "D01.268.271.800",
            "D01.268.613.700",
            "D01.362.641.745",
            "D01.496.749.305.800"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011886",
      "preferred_label": "Radon",
      "type": "descriptor",
      "location": "vocabulary:24",
      "term": {
        "text": "Radon",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Water Pollution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Water Pollution",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Water Supply",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014881",
          "name": "Water Supply",
          "type": "descriptor",
          "scope_note": "Means or process of supplying water (as for a community) usually including reservoirs, tunnels, and pipelines and often the watershed from which the water is ultimately drawn. (Webster, 3d ed)",
          "tree_numbers": [
            "J01.293.821.500"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014881",
      "preferred_label": "Water Supply",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "Water Supply",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Water Microbiology",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014871",
          "name": "Water Microbiology",
          "type": "descriptor",
          "scope_note": "The presence of bacteria, viruses, and fungi in water. This term is not restricted to pathogenic organisms.",
          "tree_numbers": [
            "H01.158.273.540.274.777",
            "N06.850.425.450"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014871",
      "preferred_label": "Water Microbiology",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "Water Microbiology",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Vehicle Emissions",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001335",
          "name": "Vehicle Emissions",
          "type": "descriptor",
          "scope_note": "Gases, fumes, vapors, and ODORANTS escaping from the cylinders of a gasoline or diesel internal-combustion engine. (From McGraw-Hill Dictionary of Scientific and Technical Terms, 4th ed and Random House Unabridged Dictionary, 2d ed)",
          "tree_numbers": [
            "D20.832"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001335",
      "preferred_label": "Vehicle Emissions",
      "type": "descriptor",
      "location": "vocabulary:28",
      "term": {
        "text": "Vehicle Emissions",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cold Climate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003081",
          "name": "Cold Climate",
          "type": "descriptor",
          "scope_note": "A climate characterized by COLD TEMPERATURE for a majority of the time during the year.",
          "tree_numbers": [
            "G16.500.275.071.275",
            "N06.230.300.100.250.275"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003081",
      "preferred_label": "Cold Climate",
      "type": "descriptor",
      "location": "vocabulary:29",
      "term": {
        "text": "Cold Climate",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Hot Temperature",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T18:58:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006358",
          "name": "Hot Temperature",
          "type": "descriptor",
          "scope_note": "Presence of warmth or heat or a temperature notably higher than an accustomed norm.",
          "tree_numbers": [
            "G01.906.595.543",
            "G16.500.275.063.725.710.380",
            "G16.500.750.775.710.380",
            "N06.230.300.100.725.232",
            "N06.230.300.100.725.710.380"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006358",
      "preferred_label": "Hot Temperature",
      "type": "descriptor",
      "location": "vocabulary:30",
      "term": {
        "text": "Hot Temperature",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"systematic reviews as topic\"[MeSH Terms] OR \"systematic\"[Filter] OR \"systematic review\"[Title/Abstract] OR \"systematic reviews\"[Title/Abstract] OR \"systematic literature review\"[Title/Abstract] OR \"systematic literature reviews\"[Title/Abstract] OR \"umbrella review\"[Title/Abstract] OR \"umbrella reviews\"[Title/Abstract] OR \"review of reviews\"[Title/Abstract] OR \"evidence synthesis\"[Title/Abstract] OR \"evidence syntheses\"[Title/Abstract]) AND (\"environmental health\"[MeSH Terms] OR \"environmental exposure\"[MeSH Terms] OR \"occupational exposure\"[MeSH Terms] OR \"occupational health\"[MeSH Terms] OR \"occupational diseases\"[MeSH Terms] OR \"working conditions\"[MeSH Terms] OR \"workplace\"[MeSH Terms] OR \"dermatitis, occupational\"[MeSH Terms] OR \"shift work schedule\"[MeSH Terms] OR \"air pollution\"[MeSH Terms] OR \"air pollution, indoor\"[MeSH Terms] OR \"particulate matter\"[MeSH Terms] OR \"radon\"[MeSH Terms] OR \"water pollution\"[MeSH Terms] OR \"water supply\"[MeSH Terms] OR \"water microbiology\"[MeSH Terms] OR \"vehicle emissions\"[MeSH Terms] OR \"cold climate\"[MeSH Terms] OR \"hot temperature\"[MeSH Terms] OR \"environmental health\"[Title/Abstract] OR \"environmental exposure*\"[Title/Abstract] OR \"environmental toxicant*\"[Title/Abstract] OR \"environmental pollut*\"[Title/Abstract] OR \"environmental determinant*\"[Title/Abstract] OR \"environmental epidemiolog*\"[Title/Abstract] OR \"air pollution\"[Title/Abstract] OR \"air pollutant*\"[Title/Abstract] OR \"water pollution\"[Title/Abstract] OR \"water distribution system*\"[Title/Abstract] OR \"water supply\"[Title/Abstract] OR \"waterborne\"[Title/Abstract] OR \"water borne\"[Title/Abstract] OR \"pesticide*\"[Title/Abstract] OR \"radon\"[Title/Abstract] OR \"diesel\"[Title/Abstract] OR \"diesel exhaust\"[Title/Abstract] OR \"chemical exposure*\"[Title/Abstract] OR \"occupational exposure*\"[Title/Abstract] OR \"shift work\"[Title/Abstract] OR \"night shift\"[Title/Abstract] OR \"contact dermatitis\"[Title/Abstract] OR \"occupational dermatitis\"[Title/Abstract] OR \"built environment\"[Title/Abstract] OR \"neighborhood environment\"[Title/Abstract] OR \"neighbourhood environment\"[Title/Abstract] OR \"workplace\"[Title/Abstract] OR \"working condition*\"[Title/Abstract] OR \"workplace polic*\"[Title/Abstract] OR \"workplace environment\"[Title/Abstract] OR \"noise exposure\"[Title/Abstract] OR \"ambient temperature\"[Title/Abstract] OR \"high ambient temperature\"[Title/Abstract] OR \"low ambient temperature\"[Title/Abstract] OR \"temperature exposure*\"[Title/Abstract] OR \"environment-based\"[Title/Abstract] OR \"environment-based\"[Title/Abstract] OR \"environmental design\"[Title/Abstract] OR \"home environment\"[Title/Abstract] OR \"noise regulation\"[Title/Abstract] OR \"climate change\"[Title/Abstract]) AND 1800/01/01:2020/07/20[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 13,
      "review_sha256": "9740569e7ade1d72d5f68c7f6ab8baf89837cf5d058f16f7543720fd78387a8a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no unresolved translation issues. The Working Conditions heading maps to a MeSH term, though it returns zero records under this date-bounded search."
        },
        "operators": {
          "verdict": "pass",
          "note": "The systematic-review and environmental-health terms are ORed within their concepts, and the two concepts are combined with AND, consistent with the stated roles."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The search includes systematic-review and environmental/exposure headings. The zero-hit Working Conditions heading is an OR term and does not invalidate the query."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The category probe hit PMID 24473109 was inspected and its diesel-exhaust topic was added to the environmental-health block; the current evaluation retrieves all 18 development records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors or unresolved translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit is applied. The stated Entrez date cutoff is documented as the search snapshot date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The environmental-health block is AND-ed, but the latest category probe found an eligible record outside that block (PMID 24473109). The probe budget was exhausted while still finding a relevant record, so the current search misses known eligible evidence.",
          "recommendation": "Inspect the record’s title, abstract, and indexing terms; add appropriate environmental-health vocabulary and retest known relevant records and category probes. If the record cannot be captured reliably, reconsider requiring the environmental-health block.",
          "status": "resolved",
          "response": "Inspected PMID 24473109 and added Vehicle Emissions[Mesh], diesel[tiab], and diesel exhaust wording before the current packet evaluation. The current PubMed evaluation retrieves this record and all 18 development records with no known losses. The category probe budget is exhausted, so further untested member-only gaps remain an acknowledged risk."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-111541572eb1a07c5fc8",
          "status": "accepted-risk",
          "response": "The latest probe hit was revised into the current query and recovered. The warning persists because the standard probe budget was exhausted after a positive probe; no further probe was run. Unexhausted category members remain a sensitivity risk.",
          "evidence": "Category probe 8 reports PMID 24473109; the current evaluation reports 18/18 relevant development records retrieved, including PMID 24473109. The terms added include Vehicle Emissions[Mesh], diesel[tiab], and diesel exhaust wording."
        },
        {
          "issue_id": "I-96df2d4e3fb0f99ded8e",
          "status": "accepted-risk",
          "response": "This authority-valid MeSH heading is retained as one OR alternative, and its standalone zero count does not constrain retrieval. It still warrants documentation as a zero-hit line.",
          "evidence": "Exact clause: (Working Conditions[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/07/20\"[edat]); translation: \"working conditions\"[MeSH Terms] AND 1800/01/01:2020/07/20[Date - Entry]."
        },
        {
          "issue_id": "I-2f5bccd710fac585146d",
          "status": "accepted-risk",
          "response": "Retain as an authority-valid OR alternative despite zero retrieval; occupational health, workplace, and working-condition text terms provide overlapping coverage, though this individual MeSH line contributes no records at this cutoff.",
          "evidence": "Exact clause: (Working Conditions[Mesh]) AND (\"1800/01/01\"[edat] : \"2020/07/20\"[edat]); translation: \"working conditions\"[MeSH Terms] AND 1800/01/01:2020/07/20[Date - Entry]."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 13,
      "review_sha256": "9740569e7ade1d72d5f68c7f6ab8baf89837cf5d058f16f7543720fd78387a8a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no unresolved translation issue. The retained Working Conditions heading is authority-valid and its zero-hit status is documented."
        },
        "operators": {
          "verdict": "pass",
          "note": "Systematic-review alternatives and environmental-health alternatives are ORed within their concepts, and the concepts are combined with AND as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Systematic-review and environmental/exposure headings are included. The zero-hit Working Conditions heading is retained as an OR alternative and documented."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The earlier missed record, PMID 24473109, was inspected and relevant diesel-exhaust vocabulary was added. The current evaluation retrieves all 18 development records, including that record. The remaining member-only category risk is disclosed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors or unresolved translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit is applied; the Entrez date cutoff is documented as the search snapshot date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "scope",
          "finding": "The environmental-health block missed eligible PMID 24473109, and the category-probe budget was exhausted after a relevant record was found.",
          "recommendation": "Inspect the record, add appropriate vocabulary, and retest known relevant records; document remaining sensitivity risk if probing is exhausted.",
          "status": "resolved",
          "response": "PMID 24473109 was inspected; Vehicle Emissions[Mesh], diesel[tiab], and diesel-exhaust wording were added. The current evaluation retrieves this record and all 18 development records. The exhausted probe budget and residual category risk are documented."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-111541572eb1a07c5fc8",
          "status": "accepted-risk",
          "response": "The latest probe hit was added to the query and is now retrieved. The warning remains because the probe budget was exhausted after a positive probe; untested member-only gaps remain a stated sensitivity risk.",
          "evidence": "The packet reports PMID 24473109 among the probe findings and all 18 development records retrieved in the current evaluation, including PMID 24473109."
        },
        {
          "issue_id": "I-96df2d4e3fb0f99ded8e",
          "status": "accepted-risk",
          "response": "The authority-valid heading is retained as an OR alternative. Its standalone zero-hit status is documented and does not constrain retrieval.",
          "evidence": "The packet records the exact Working Conditions[Mesh] clause, its PubMed translation, and zero hits under the documented date-bounded query."
        },
        {
          "issue_id": "I-2f5bccd710fac585146d",
          "status": "accepted-risk",
          "response": "The authority-valid heading is retained as an OR alternative despite zero retrieval; overlapping occupational-health, workplace, and working-condition terms are present, and the zero-hit status is documented.",
          "evidence": "The packet records the exact Working Conditions[Mesh] clause, its PubMed translation, and zero hits under the documented date-bounded query."
        }
      ]
    }
  ]
}
```


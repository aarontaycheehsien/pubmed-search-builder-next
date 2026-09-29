# PubMed search strategy: audit

Generated 2026-09-28T21:51:37+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In people with suspected non-falciparum or Plasmodium vivax malaria in endemic countries, what is the diagnostic accuracy of rapid diagnostic tests for uncomplicated malaria?
- Framework: PIRD
- Scope confirmed by user: yes (User asked not to wait for clarification; roles were assigned from the stated PIRD question and eligibility criteria. No known relevant articles were supplied. Entrez retrieval is bounded by PSB_AS_OF=2013-06-09 on every command; no publication-date limit is applied. Standard-depth workload budget is 10,000 records. Endemic setting and uncomplicated disease are screened rather than searched. Endemic setting is tested as an optional block per scope guidance; uncomplicated severity remains a screening criterion.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum or Plasmodium vivax malaria | search | Target condition and population; every eligible case involves malaria, and species are candidate member terms. |
| Malaria rapid diagnostic tests | search | Index test; an eligible study must evaluate an RDT, usually named in the abstract or indexed. |
| Malaria-endemic setting | optional | Topic-defining setting; authors may name it explicitly, but local studies may only identify the endemic location. Test before deciding whether to AND. |
| Uncomplicated disease | screen | Severity and uncomplicated status are inconsistently named/indexed and can often be determined only from methods or full text. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:50:53+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 6,940
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Malaria, Vivax[Mesh]` | 2,872 | none |
| 3 | `malaria[tiab]` | 55,839 | none |
| 4 | `plasmodium[tiab]` | 34,635 | none |
| 5 | `vivax[tiab]` | 5,921 | none |
| 6 | `"P. vivax"[tiab]` | 2,944 | none |
| 7 | `non-falciparum[tiab]` | 55 | none |
| 8 | `nonfalciparum[tiab]` | 59 | none |
| 9 | `malariae[tiab]` | 888 | none |
| 10 | `ovale[tiab]` | 5,356 | none |
| 11 | `knowlesi[tiab]` | 866 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 79,517 | none |
| 13 | `Diagnostic Tests, Routine[Mesh]` | 7,136 | none |
| 14 | `Point-of-Care Testing[Mesh]` | 1 | none |
| 15 | `Antigens, Protozoan[Mesh]` | 12,579 | none |
| 16 | `"rapid diagnostic test*"[tiab]` | 1,321 | none |
| 17 | `"rapid test*"[tiab]` | 3,281 | none |
| 18 | `RDT[tiab]` | 653 | none |
| 19 | `RDTs[tiab]` | 303 | none |
| 20 | `immunochromatograph*[tiab]` | 1,749 | none |
| 21 | `dipstick*[tiab]` | 2,298 | none |
| 22 | `"lateral flow"[tiab]` | 720 | none |
| 23 | `"test strip*"[tiab]` | 1,328 | none |
| 24 | `HRP2[tiab]` | 168 | none |
| 25 | `pLDH[tiab]` | 158 | none |
| 26 | `aldolase[tiab]` | 5,870 | none |
| 27 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 28 | `OptiMAL[tiab]` | 235,534 | none |
| 29 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 284,750 | none |
| 30 | `#12 AND #29` | 6,940 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Malaria, Vivax[Mesh] OR malaria[tiab] OR plasmodium[tiab] OR vivax[tiab] OR "P. vivax"[tiab] OR non-falciparum[tiab] OR nonfalciparum[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab]) AND (Diagnostic Tests, Routine[Mesh] OR Point-of-Care Testing[Mesh] OR Antigens, Protozoan[Mesh] OR "rapid diagnostic test*"[tiab] OR "rapid test*"[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR dipstick*[tiab] OR "lateral flow"[tiab] OR "test strip*"[tiab] OR HRP2[tiab] OR pLDH[tiab] OR aldolase[tiab] OR Reagent Kits, Diagnostic[Mesh] OR OptiMAL[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 13 | 13 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Malaria-endemic setting | left out | 6,940 / 1,045 | 84.9% | 19860920, 20979601, 22471175, 22818643, 23345297, 23433230, 23692957 | 0/30 (up to 10% of removed records could be relevant) | The refreshed 30-record loss sample had no clearly eligible record, but the setting block would lose seven known relevant studies while cutting 84.9% of results. The measured known-record loss outweighs the estimated count reduction; screen the setting. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum or Plasmodium vivax malaria | 1 | `(Plasmodium[Mesh] OR plasmodium[tiab] OR parasite*[tiab])` | 3,128 | 0/30 |
| Non-falciparum or Plasmodium vivax malaria | 2 | `(Plasmodium[Mesh] OR plasmodium[tiab] OR parasite*[tiab])` | 3,958 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 284,750 | 0 |
| rapid_test | 79,517 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 6,163 | initial | none | Initial recall-first strategy: broad malaria concept AND malaria RDT concept; five screened development records; no outcome, setting, severity, or reference-standard block or limits. |
| 2 | 6,163 | rapid_test: +0 / -1 | none | Removed the current Rapid Diagnostic Tests MeSH term after its cutoff-specific evaluation returned zero records and PubMed said No items found; retained historical MeSH and text-word layers. RDT concept remains searched. |
| 3 | 6,163 | limits/combination | none | Added endemic setting as a tested optional concept (scope guidance); uncomplicated severity remains screen. Malaria category probe screened with no relevant member-only records. |
| 4 | 6,940 | rapid_test: +2 / -0 | none | Recovered missed relevant Colombian OptiMAL study (PMID 12596444) after terms miss showed its title uses the brand and its MeSH includes Reagent Kits, Diagnostic; added brand text and that MeSH heading. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 932 NCBI requests logged (550 from cache); strategy sha256 38a93e4d5003._

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
      "requested": "Malaria",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:50:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008288",
          "name": "Malaria",
          "type": "descriptor",
          "scope_note": "A protozoan disease caused in humans by four species of the PLASMODIUM genus: PLASMODIUM FALCIPARUM; PLASMODIUM VIVAX; PLASMODIUM OVALE; and PLASMODIUM MALARIAE; and transmitted by the bite of an infected female mosquito of the genus ANOPHELES. Malaria is endemic in parts of Asia, Africa, Central and South America, Oceania, and certain Caribbean islands. It is characterized by extreme exhaustio...",
          "tree_numbers": [
            "C01.610.752.530",
            "C01.920.852.750"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008288",
      "preferred_label": "Malaria",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Malaria",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Malaria, Vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:50:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016780",
          "name": "Malaria, Vivax",
          "type": "descriptor",
          "scope_note": "Malaria caused by PLASMODIUM VIVAX. This form of malaria is less severe than MALARIA, FALCIPARUM, but there is a higher probability for relapses to occur. Febrile paroxysms often occur every other day.",
          "tree_numbers": [
            "C01.610.752.530.700",
            "C01.920.852.750.700"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016780",
      "preferred_label": "Malaria, Vivax",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Malaria, Vivax",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:50:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003955",
          "name": "Diagnostic Tests, Routine",
          "type": "descriptor",
          "scope_note": "Diagnostic procedures, such as laboratory tests and x-rays, routinely performed on all individuals or specified categories of individuals in a specified situation, e.g., patients being admitted to the hospital. These include routine tests administered to neonates.",
          "tree_numbers": [
            "E01.370.395"
          ],
          "entry_terms": 27,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003955",
      "preferred_label": "Diagnostic Tests, Routine",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "Diagnostic Tests, Routine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Point-of-Care Testing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:50:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000067716",
          "name": "Point-of-Care Testing",
          "type": "descriptor",
          "scope_note": "Allows patient diagnoses in the physician’s office, in other ambulatory setting or at bedside. The results of care are timely, and allow rapid treatment to the patient. (from NIH Fact Sheet Point-of-Care Diagnostic Testing, 2010.)",
          "tree_numbers": [
            "N04.590.874.500"
          ],
          "entry_terms": 26,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000067716",
      "preferred_label": "Point-of-Care Testing",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "Point-of-Care Testing",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Antigens, Protozoan",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:50:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000953",
          "name": "Antigens, Protozoan",
          "type": "descriptor",
          "scope_note": "Any part or derivative of any protozoan that elicits immunity; malaria (Plasmodium) and trypanosome antigens are presently the most frequently encountered.",
          "tree_numbers": [
            "D12.776.820.125",
            "D23.050.293"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000953",
      "preferred_label": "Antigens, Protozoan",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "Antigens, Protozoan",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:50:53+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011933",
          "name": "Reagent Kits, Diagnostic",
          "type": "descriptor",
          "scope_note": "Commercially prepared reagent sets, with accessory devices, containing all of the major components and literature necessary to perform one or more designated diagnostic tests or procedures. They may be for laboratory or personal use.",
          "tree_numbers": [
            "D27.505.259.875",
            "D27.720.470.410.680",
            "E07.720"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011933",
      "preferred_label": "Reagent Kits, Diagnostic",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "Reagent Kits, Diagnostic",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"plasmodium\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract]) AND (\"diagnostic tests, routine\"[MeSH Terms] OR \"point of care testing\"[MeSH Terms] OR \"antigens, protozoan\"[MeSH Terms] OR \"rapid diagnostic test*\"[Title/Abstract] OR \"rapid test*\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"dipstick*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"test strip*\"[Title/Abstract] OR \"HRP2\"[Title/Abstract] OR \"pLDH\"[Title/Abstract] OR \"aldolase\"[Title/Abstract] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"OptiMAL\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "863517fa3072dcea1b04767c4e2f7348d4854e099027cf388819934e94d969c1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The recorded PubMed translations match the entered MeSH and title/abstract terms. The query has no translation issues or warnings requiring clause-specific review."
        },
        "operators": {
          "verdict": "pass",
          "note": "The malaria and rapid-test concept blocks are OR-combined and then AND-combined. The optional endemic-setting block was tested and left out; its 84.9% reduction would lose seven known relevant records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses verified MeSH descriptors for malaria and several diagnostic-test concepts, supplemented by free-text terms. The broad diagnostic headings are constrained by the malaria block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The malaria block covers the named Plasmodium/vivax and non-falciparum terms, including bare component terms; the test block includes rapid-test phrases, RDT variants, and test-method and antigen terms. The category probes found no relevant records outside the malaria block, and all 13 known relevant records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query and its component lines have no reported syntax errors, warnings, or validation blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility filter is added for uncomplicated status or endemic setting. The 1800-to-2013-06-09 entry-date bound is the stated as-of retrieval boundary, not an unexplained eligibility limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


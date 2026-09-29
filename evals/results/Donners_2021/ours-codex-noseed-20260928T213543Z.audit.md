# PubMed search strategy: audit

Generated 2026-09-28T21:56:19+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In humans, what are the pharmacokinetics of emicizumab and their association with efficacy in haemophilia A?
- Framework: PECO (drug exposure and associated outcomes)
- Scope confirmed by user: yes (Scope proceeded without clarification at user request. Human status, haemophilia A/healthy-volunteer context, report content and eligible design are screened; drug is the only required search block. PK/exposure and linked efficacy terminology is tested as optional. No known relevant records supplied. PubMed is bounded by Entrez date 2020-10-22 via PSB_AS_OF; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Emicizumab and development names | search | Required exposure/intervention; the question and eligibility criteria require emicizumab, ACE910, or its factor VIII-mimetic bispecific antibody description. |
| Pharmacokinetics/exposure and associated efficacy | optional | Topic-defining report content, but terms may be absent from titles/abstracts; test as an optional AND block. |
| Human clinical study and eligible design | screen | Human status, haemophilia A or healthy-volunteer bridging context, and study design will be assessed during screening; no restrictive species/design filter. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:55:46+00:00
- Records added to PubMed up to: 2020-10-22
- Total records: 1,652
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `emicizumab[nm]` | 161 | none |
| 2 | `emicizumab[tiab]` | 193 | none |
| 3 | `emicizumab-kxwh[tiab]` | 3 | none |
| 4 | `ACE910[tiab]` | 29 | none |
| 5 | `ACE-910[tiab]` | 1 | none |
| 6 | `Hemlibra[tiab]` | 13 | none |
| 7 | `"factor VIII mimetic"[tiab]` | 8 | none |
| 8 | `"anti-FIXa/FX"[tiab]` | 7 | none |
| 9 | `(bispecific[tiab] AND (factor VIII[tiab] OR FVIII[tiab] OR "factor IXa"[tiab] OR FIXa[tiab]))` | 111 | none |
| 10 | `bispecific[tiab]` | 4,198 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 4,322 | none |
| 12 | `Pharmacokinetics[Mesh]` | 319,459 | none |
| 13 | `pharmacokinetic*[tiab]` | 165,014 | none |
| 14 | `pharmacometric*[tiab]` | 628 | none |
| 15 | `pharmacodynamics[tiab]` | 20,585 | none |
| 16 | `exposure[tiab]` | 849,496 | none |
| 17 | `concentration*[tiab]` | 1,927,463 | none |
| 18 | `trough[tiab]` | 18,310 | none |
| 19 | `half-life[tiab]` | 72,685 | none |
| 20 | `clearance[tiab]` | 165,489 | none |
| 21 | `"exposure-response"[tiab]` | 3,547 | none |
| 22 | `efficacy[tiab]` | 826,305 | none |
| 23 | `effectiveness[tiab]` | 462,701 | none |
| 24 | `bleeding[tiab]` | 205,563 | none |
| 25 | `"bleeding rate"[tiab]` | 1,270 | none |
| 26 | `"annualized bleeding rate"[tiab]` | 83 | none |
| 27 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 4,268,938 | none |
| 28 | `#11 AND #27` | 1,652 | none |

### Strategy (single line, for copying into PubMed)

```text
((emicizumab[nm] OR emicizumab[tiab] OR emicizumab-kxwh[tiab] OR ACE910[tiab] OR ACE-910[tiab] OR Hemlibra[tiab] OR "factor VIII mimetic"[tiab] OR "anti-FIXa/FX"[tiab] OR (bispecific[tiab] AND (factor VIII[tiab] OR FVIII[tiab] OR "factor IXa"[tiab] OR FIXa[tiab])) OR bispecific[tiab]) AND (Pharmacokinetics[Mesh] OR pharmacokinetic*[tiab] OR pharmacometric*[tiab] OR pharmacodynamics[tiab] OR exposure[tiab] OR concentration*[tiab] OR trough[tiab] OR half-life[tiab] OR clearance[tiab] OR "exposure-response"[tiab] OR efficacy[tiab] OR effectiveness[tiab] OR bleeding[tiab] OR "bleeding rate"[tiab] OR "annualized bleeding rate"[tiab])) AND ("1800/01/01"[edat] : "2020/10/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Pharmacokinetics/exposure and associated efficacy | AND-ed | 4,322 / 1,652 | 61.8% | none | 0/30 (up to 10% of removed records could be relevant) | With the independent bispecific[tiab] alias included, the 15-term PK/exposure/efficacy block retains all 11 known relevant records, reduces 4,322 records to 1,652 (61.8%), and the refreshed random sample of 30 excluded records contains no eligible study. Although standalone bispecific wording adds noise, the final result remains within the standard 10,000-record budget and the sampled loss set did not justify dropping this topic-defining block. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| emicizumab | 4,268,938 | 0 |
| pk_efficacy | 4,322 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 233 | initial | none | Initial high-sensitivity drug block and candidate PK/exposure/efficacy content block; drug vocabulary includes MeSH supplementary concept entry terms and development descriptors. |
| 2 | 233 | emicizumab: +0 / -1 | none | Removed exact anti-factor IXa/factor X phrase after PubMed reported it was absent from the phrase index and omitted it from translation; retained the usable emicizumab, ACE910, Hemlibra, factor VIII mimetic and anti-FIXa/FX terms. Optional PK/exposure/efficacy concept remains measured. |
| 3 | 162 | pk_efficacy: +15 / -0 | none | ANDed optional PK/exposure/efficacy block after it retained all nine known relevant records, reduced results by 30.5%, and no eligible records were found among all 30 in the random loss sample. |
| 4 | 1,652 | emicizumab: +1 / -0 | none | Added the standalone bispecific[tiab] wording required by the scope and the internal critic, while preserving factor VIII mimetic and anti-FIXa/FX wording. Split the 11 screened relevant records into eight development and three semi-independent validation records before mining or revising further. |
| 5 | 175 | emicizumab: +1 / -1 | none | Revised the critic-requested standalone bispecific wording to a tested, target-specific expression pairing bispecific[tiab] with FVIII/FVIIIa or FIXa terminology. PubMed count testing showed the broad standalone term would increase the final count to 1,652, while the constrained alias produced 175 with no translation warnings; retain the specific expression for precision while covering the named antibody description. |
| 6 | 1,652 | emicizumab: +1 / -0 | none | Added the independent bispecific[tiab] synonym requested by the round-2 critic while retaining the target-specific bispecific plus factor VIII/FVIII/FIXa expression. The standalone version expands the screened final result to 1,652 records, within the 10,000-record standard workload budget; the optional block must be re-tested against this exact query. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-F1 must-fix open
- Round 2 on version 5: 1 findings; R1-F1 must-fix open
- Round 3 on version 6: 1 findings; R1-F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 509 NCBI requests logged (252 from cache); strategy sha256 491eb5b5fca5._

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
      "requested": "emicizumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T21:55:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C000608208",
          "name": "emicizumab",
          "type": "supplementary",
          "scope_note": "a humanized bispecific antibody mimicking the cofactor function of factor VIII",
          "tree_numbers": [
            "@233593"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C000608208",
      "preferred_label": "emicizumab",
      "type": "supplementary",
      "location": "vocabulary:1",
      "term": {
        "text": "emicizumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "Pharmacokinetics",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:55:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "Q000493",
          "name": "pharmacokinetics",
          "type": "qualifier",
          "scope_note": "Used for the mechanism, dynamics and kinetics of exogenous chemical and drug absorption, biotransformation, distribution, release, transport, uptake and elimination as a function of dosage, extent and rate of metabolic processes.",
          "tree_numbers": [
            "Y07.070",
            "Y08.040.060"
          ],
          "entry_terms": 2,
          "mapped_to": null
        },
        {
          "ui": "D010599",
          "name": "Pharmacokinetics",
          "type": "descriptor",
          "scope_note": "Dynamic and kinetic mechanisms of exogenous chemical DRUG LIBERATION; ABSORPTION; BIOLOGICAL TRANSPORT; TISSUE DISTRIBUTION; BIOTRANSFORMATION; elimination; and DRUG TOXICITY as a function of dosage, and rate of METABOLISM. LADMER, ADME and ADMET are abbreviations for liberation, absorption, distribution, metabolism, elimination, and toxicology.",
          "tree_numbers": [
            "G03.787",
            "G07.690.725"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010599",
      "preferred_label": "Pharmacokinetics",
      "type": "descriptor",
      "location": "vocabulary:15",
      "term": {
        "text": "Pharmacokinetics",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"emicizumab\"[Supplementary Concept] OR \"emicizumab\"[Title/Abstract] OR \"emicizumab-kxwh\"[Title/Abstract] OR \"ACE910\"[Title/Abstract] OR \"ACE-910\"[Title/Abstract] OR \"Hemlibra\"[Title/Abstract] OR \"factor VIII mimetic\"[Title/Abstract] OR \"anti-FIXa/FX\"[Title/Abstract] OR (\"bispecific\"[Title/Abstract] AND (\"factor viii\"[Title/Abstract] OR \"FVIII\"[Title/Abstract] OR \"factor IXa\"[Title/Abstract] OR \"FIXa\"[Title/Abstract])) OR \"bispecific\"[Title/Abstract]) AND (\"pharmacokinetics\"[MeSH Terms] OR \"pharmacokinetic*\"[Title/Abstract] OR \"pharmacometric*\"[Title/Abstract] OR \"pharmacodynamics\"[Title/Abstract] OR \"exposure\"[Title/Abstract] OR \"concentration*\"[Title/Abstract] OR \"trough\"[Title/Abstract] OR \"half-life\"[Title/Abstract] OR \"clearance\"[Title/Abstract] OR \"exposure-response\"[Title/Abstract] OR \"efficacy\"[Title/Abstract] OR \"effectiveness\"[Title/Abstract] OR \"bleeding\"[Title/Abstract] OR \"bleeding rate\"[Title/Abstract] OR \"annualized bleeding rate\"[Title/Abstract]) AND 1800/01/01:2020/10/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "f684c1c3357c0c1fe9f0cf2fb63063ed206db36718b4c3ab62a8dbf5bfd261ef",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The required drug concept includes the factor VIII-mimetic bispecific antibody description, but the text-word block has only the narrower phrase \"factor VIII mimetic\" (plus anti-FIXa/FX), with no standalone bispecific-antibody wording."
        },
        "operators": {
          "verdict": "pass",
          "note": "The synonym terms are ORed within blocks and the tested optional PK/exposure/efficacy block is ANDed with the required emicizumab block. The stated loss sample and retention rationale support this optional-block decision under the supplied rule."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies emicizumab as a Supplementary Concept and Pharmacokinetics as a MeSH descriptor; both are used with appropriate fields. No restrictive human or disease heading is needed given the screening plan."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add and test an independent text-word representation for the explicitly named bispecific-antibody description; the current factor VIII mimetic phrase does not cover records that use bispecific-antibody wording without that phrase."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The combined query is parenthesized correctly, field tags and Boolean operators are coherent, and the packet reports no syntax or translation errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive species or design filter is applied, consistent with screening human status, disease context, and design. The entry-date cutoff is disclosed as the as-of boundary, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility explicitly includes emicizumab's factor VIII-mimetic bispecific antibody description, but the drug block searches only the phrase \"factor VIII mimetic\" and anti-FIXa/FX; it does not search bispecific-antibody wording independently.",
          "recommendation": "Add and test an explicit text-word expression for bispecific antibody wording (including a standalone bispecific term if appropriate), then screen the added records and rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "8a4a8fb9a46fbaa18a72f2f73fcc230010bdcfc5ea117a00da738cd29c3a344d",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The emicizumab Supplementary Concept and Pharmacokinetics MeSH descriptor translate as intended, and the final query reports no translation errors. However, the required bispecific-antibody description is still represented only by a bispecific term conditioned on factor VIII/FVIII/factor IXa/FIXa wording; the prior finding requested an independent bispecific text-word representation."
        },
        "operators": {
          "verdict": "pass",
          "note": "Drug aliases are ORed, and the optional PK/exposure/efficacy block is ANDed as an explicitly tested choice. The packet reports all 11 known relevant records retained and a 30-record removed-record sample with no eligible studies, alongside a 29.7% reduction and rationale for retaining the block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies emicizumab as a Supplementary Concept and Pharmacokinetics as a MeSH descriptor, and both are used in suitable fields. Screening rather than restrictive human or disease headings is consistent with the stated plan."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The new bispecific expression still requires another factor VIII/FVIII/factor IXa/FIXa word. It therefore does not independently retrieve records describing the required drug as a bispecific antibody without those paired terms; R1-F1 remains open."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The combined Boolean structure is parenthesized coherently, field tags are consistent, and the packet reports no syntax, translation, or lint issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive species or design filter is applied, consistent with screening those criteria. The entry-date cutoff is disclosed as the 2020-10-22 as-of boundary, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility explicitly includes emicizumab's factor VIII-mimetic bispecific antibody description, but the drug block still has no independent bispecific-antibody text-word representation: its bispecific term is conditioned on factor VIII, FVIII, factor IXa, or FIXa wording.",
          "recommendation": "Add and test an independent bispecific-antibody text-word expression, including standalone bispecific wording as appropriate; screen the added records and rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "065cb775275f88d5d9876b0fa7796ae9bacb0cd6e0ab1e53121f3209f0509b7f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The emicizumab Supplementary Concept and Pharmacokinetics MeSH descriptor translate as intended. The required bispecific description now also has an independent bispecific[tiab] representation."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within concepts and the optional PK/exposure/efficacy block is ANDed based on its refreshed evaluation: 1,652 records, all 11 known relevant records retained, and 0 of 30 sampled excluded records eligible."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied vocabulary evidence verifies emicizumab as a Supplementary Concept and Pharmacokinetics as a MeSH descriptor, and the query uses the corresponding fields. Screening is appropriate for human status, disease context, and design."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy now includes standalone bispecific[tiab] alongside the narrower factor VIII/FVIII/factor IXa/FIXa expression, addressing the prior independent-wording gap."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The combined query is coherently parenthesized, uses consistent field tags, and reports no syntax, translation, lint, or validation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No restrictive human or design filter is applied, consistent with screening those criteria. The 2020-10-22 entry-date boundary is disclosed and no publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility explicitly includes emicizumab's factor VIII-mimetic bispecific antibody description, but the drug block initially lacked independent bispecific wording.",
          "recommendation": "Add and test an independent bispecific-antibody text-word expression, screen added records, and rerun the complete evaluation.",
          "status": "resolved",
          "response": "Resolved in v6: standalone bispecific[tiab] was added, and the complete evaluation was refreshed. The final set contains 1,652 records, retrieves all 11 known relevant records, and the 30-record sample of records excluded by the optional block contains no eligible studies. The independent term is broad, but the reported result remains within the 10,000-record workload budget."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


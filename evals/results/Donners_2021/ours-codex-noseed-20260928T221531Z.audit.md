# PubMed search strategy: audit

Generated 2026-09-28T22:27:44+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In humans, what are the pharmacokinetics of emicizumab and their association with efficacy in haemophilia A?
- Framework: PECO (drug exposure and reported outcomes)
- Scope confirmed by user: no (User supplied no known relevant articles and explicitly asked not to be asked questions. Proceeded without scope confirmation, using stated eligibility as screening criteria. No language, publication-date, human, or study-design limits. PubMed records are bounded by Entrez date 2020-10-22 via PSB_AS_OF. A 30% holdout was created after 11 screened relevant discoveries. The initial ten-record term-ranking output had already been inspected before the split; no ranked terms were added, but the resulting validation set is not fully independent.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Emicizumab and development names | search | The drug is the defining exposure, and eligible trials and pharmacokinetic studies reliably name emicizumab or ACE910. |
| Pharmacokinetics, exposure, or bleeding efficacy | optional | These are topic-defining reported outcomes that may be named in abstracts; test whether requiring their labels materially reduces screening without losing known relevant records. |
| Human participants, including healthy-volunteer bridging participants | screen | Human status is an eligibility criterion; a human filter can miss records and does not reliably capture mixed or bridging studies. |
| Haemophilia A population | screen | Emicizumab defines the exposure; population labels may be absent in bridging study records and will be checked at screening. |
| Clinical trial, pharmacokinetic, or pharmacometric study | screen | Design labels are inconsistently indexed; no ad hoc design filter will be required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:27:32+00:00
- Records added to PubMed up to: 2020-10-22
- Total records: 233
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `emicizumab[nm]` | 161 | none |
| 2 | `emicizumab[tiab]` | 193 | none |
| 3 | `ACE910[tiab]` | 29 | none |
| 4 | `ACE-910[tiab]` | 1 | none |
| 5 | `Hemlibra[tiab]` | 13 | none |
| 6 | `emicizumab-kxwh[tiab]` | 3 | none |
| 7 | `factor VIII mimetic[tiab]` | 8 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 233 | none |

### Strategy (single line, for copying into PubMed)

```text
((emicizumab[nm] OR emicizumab[tiab] OR ACE910[tiab] OR ACE-910[tiab] OR Hemlibra[tiab] OR emicizumab-kxwh[tiab] OR factor VIII mimetic[tiab])) AND ("1800/01/01"[edat] : "2020/10/22"[edat])
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
| Pharmacokinetics, exposure, or bleeding efficacy | left out | 233 / 179 | 23.2% | none | 0/30 (up to 10% of removed records could be relevant) | The candidate block reduces the core count by 23.2%, below the roughly 30% materiality guideline. Screened all 30 records in the current loss sample; none clearly met the clinical-trial, pharmacokinetic, or pharmacometric eligibility. Requiring outcome labels still carries avoidable recall risk, so leave this optional block out. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 233 | initial | none | Initial draft from protocol scope: searched emicizumab and its development/brand names; measured the combined PK/exposure or bleeding-efficacy topic as an optional candidate. No user seeds; using precision pilot and PubMed cutoff 2020-10-22. |
| 2 | 233 | emicizumab: +0 / -1 | none | Removed the hyphenated factor VIII-mimetic spelling after evaluation showed it translated identically to factor VIII mimetic[tiab] (both count 8); no expected retrieval loss because PubMed normalizes both to the same phrase. Retained the non-hyphenated form. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (Same-context critic: separate codex exec could not connect because the local CLI rejected the API certificate (UnknownIssuer). Review completed against the packet, but it is not independent reviewer input.): 0 findings; 
- Round 2 on version 2 (Same-context critic. The fresh-context Codex CLI remained unavailable because of certificate validation failure. This round reviews the current split and the unchanged query; it is not independent information-specialist review.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 295 NCBI requests logged (133 from cache); strategy sha256 e4894a800478._

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
      "checked_at": "2026-09-28T22:27:32+00:00",
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
    }
  ],
  "translation": "(\"emicizumab\"[Supplementary Concept] OR \"emicizumab\"[Title/Abstract] OR \"ACE910\"[Title/Abstract] OR \"ACE-910\"[Title/Abstract] OR \"Hemlibra\"[Title/Abstract] OR \"emicizumab-kxwh\"[Title/Abstract] OR \"factor viii mimetic\"[Title/Abstract]) AND 1800/01/01:2020/10/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "290ec9aee1736a6f072bfe7b4dfc121fb0f6d225a36102e0cf4f1b1f1f509eb3",
      "note": "Same-context critic: separate codex exec could not connect because the local CLI rejected the API certificate (UnknownIssuer). Review completed against the packet, but it is not independent reviewer input.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The only required AND concept is the emicizumab drug identity, with supplementary concept and title/abstract coverage for the development name, brand and factor VIII-mimetic wording. Human status, haemophilia A context, design and outcomes remain screened or tested optional; the optional outcome block was left out after its measured decision."
        },
        "operators": {
          "verdict": "pass",
          "note": "The block is an OR of identity synonyms and is the only required block; no NOT, date publication limit, or fragile directional process is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Emicizumab is a verified supplementary concept and is searched with [nm]. No unrelated descriptor is required as an AND block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The title/abstract layer covers emicizumab, ACE910/ACE-910, Hemlibra, emicizumab-kxwh, and factor VIII mimetic. The two factor VIII-mimetic spellings were observed to have identical translation and counts; the redundant spelling was removed and the retained strategy re-evaluated."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All clauses are field-tagged, PubMed translations are explicit, and the current evaluation reports no technical or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, human, design, or publication-date filter is used. PubMed is bounded by Entrez date through PSB_AS_OF 2020-10-22, as requested."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "7493fdf08f864293e84b76307aaca1d981dfdc5a4c8a8127918fc017d743c3b3",
      "note": "Same-context critic. The fresh-context Codex CLI remained unavailable because of certificate validation failure. This round reviews the current split and the unchanged query; it is not independent information-specialist review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The only required block is the drug identity, suitable for this focused question. Human, population and study design remain screening criteria. PK/efficacy labels were tested as an optional block and left out based on recorded evidence."
        },
        "operators": {
          "verdict": "pass",
          "note": "Correct OR grouping for identity variants; one search block, no NOT or unsupported proximity."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified supplementary concept emicizumab is tagged [nm], and is paired with title/abstract terms for records not indexed under it."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Drug, development, brand and factor VIII-mimetic terms are included. The final spelling set has no duplicate translation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The evaluation for the current development/validation sets reports no lint, syntax, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No ad hoc human, language, publication-date or design filter. The Entrez-date cutoff is recorded as requested."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```


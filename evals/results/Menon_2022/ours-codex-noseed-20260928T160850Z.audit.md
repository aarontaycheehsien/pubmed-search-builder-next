# PubMed search strategy: audit

Generated 2026-09-28T16:39:43+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Methodological rigour of systematic reviews in environmental health
- Framework: Method and application context
- Scope confirmed by user: no (User has no known relevant articles and cannot answer questions during the run; proceeded with reasonable assumptions. Interpreted the question as studies evaluating the methods of environmental-health systematic reviews, rather than methods used by reviews on environmental-health topics. No date, language, population, or publication-type limits requested. PubMed access is bounded by PSB_AS_OF=2020-07-20 (Entrez date), without a publication-date filter. No human confirmation of scope.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Environmental health | search | The application context defines the topic and is expected to be named in titles, abstracts, or indexing. |
| Systematic reviews | search | These are the objects whose methodological rigour is being evaluated and are usually identified as systematic reviews or meta-analyses. |
| Methodological rigour or quality of reviews | optional | This is the topic-defining assessment outcome, but evaluation studies may not name quality or rigour consistently; test as an optional block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T16:39:11+00:00
- Records added to PubMed up to: 2020-07-20
- Total records: 6,351
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Environmental Health"[Mesh]` | 25,528 | none |
| 2 | `"Environmental Exposure"[Mesh]` | 309,210 | none |
| 3 | `"Environmental Pollution"[Mesh]` | 553,246 | none |
| 4 | `"environmental health"[tiab]` | 9,584 | none |
| 5 | `"environmental medicine"[tiab]` | 833 | none |
| 6 | `"environmental epidemiolog*"[tiab]` | 899 | none |
| 7 | `"environmental toxicolog*"[tiab]` | 1,020 | none |
| 8 | `"environmental health science*"[tiab]` | 587 | none |
| 9 | `"environmental hazard*"[tiab]` | 2,659 | none |
| 10 | `"environmental exposure*"[tiab]` | 13,468 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 584,592 | none |
| 12 | `"Systematic Reviews as Topic"[Mesh]` | 6,347 | none |
| 13 | `"Meta-Analysis as Topic"[Mesh]` | 20,321 | none |
| 14 | `"Review Literature as Topic"[Mesh]` | 18,599 | none |
| 15 | `systematic review*[tiab]` | 175,484 | none |
| 16 | `meta-analy*[tiab]` | 176,011 | none |
| 17 | `"evidence synthesis"[tiab]` | 4,462 | none |
| 18 | `"research synthesis"[tiab]` | 540 | none |
| 19 | `umbrella review*[tiab]` | 437 | none |
| 20 | `overview*[tiab] AND review*[tiab]` | 74,285 | none |
| 21 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 362,110 | none |
| 22 | `#11 AND #21` | 6,351 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Environmental Health"[Mesh] OR "Environmental Exposure"[Mesh] OR "Environmental Pollution"[Mesh] OR "environmental health"[tiab] OR "environmental medicine"[tiab] OR "environmental epidemiolog*"[tiab] OR "environmental toxicolog*"[tiab] OR "environmental health science*"[tiab] OR "environmental hazard*"[tiab] OR "environmental exposure*"[tiab]) AND ("Systematic Reviews as Topic"[Mesh] OR "Meta-Analysis as Topic"[Mesh] OR "Review Literature as Topic"[Mesh] OR systematic review*[tiab] OR meta-analy*[tiab] OR "evidence synthesis"[tiab] OR "research synthesis"[tiab] OR umbrella review*[tiab] OR (overview*[tiab] AND review*[tiab]))) AND ("1800/01/01"[edat] : "2020/07/20"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Methodological rigour or quality of reviews | left out | 6,351 / 5,164 | 18.7% | none | 0/30 (up to 10% of removed records could be relevant) | The updated 26-term block, including assess*, apprais*, describ*, and compar*, reduces the core count by only 18.7% (6,351 to 5,164), below the skill's approximately 30% material-reduction criterion. The 30-record loss sample contained no clearly eligible record; one title-only commentary (PMID 16164539) had no abstract and remains uncertain. Leave the optional block out to retain broad retrieval and keep the final search within the 10,000-record workload budget. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| environmental_health | 362,110 | 0 |
| systematic_reviews | 584,592 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 6,351 | initial | none | Initial two-block strategy: environmental-health context AND systematic-review object; added a screened PubMed pilot record and kept review-quality terms optional pending measured losses and sample. |
| 2 | 6,351 | systematic_reviews: +0 / -1 | none | Removed the valid but zero-retrieval Systematic Review MeSH clause: PubMed returned 0 records and a phrase-index warning under the cutoff, while the text-word and Systematic Reviews as Topic layers remain. |
| 3 | 6,351 | limits/combination | none | Broadened the optional methodological-rigour block after the loss sample revealed eligible COSTER guidance used conduct/recommendation language rather than the narrower quality terms. Added practice, method, conduct, guidance, recommendation, guideline, standard, consensus, and framework variants. |
| 4 | 4,348 | methodological_rigour: +26 / -0 | none | AND-ed the optional methodological-rigour block after its broadened 30-record loss sample contained no eligible studies and the block cut the count by 31.5% without losing either known relevant record. |
| 5 | 5,164 | methodological_rigour: +4 / -0 | none | Added the bare eligibility action terms assess*, apprais*, describ*, and compar* to the methodological-rigour block in response to critic finding P2-F1; re-evaluated counts and known-record retrieval. |
| 6 | 6,351 | methodological_rigour: +0 / -30 | none | Left the tested methodological-rigour block out after adding the required bare action terms, because the expanded block reduced the core search by only 18.7%, below the approximate 30% threshold; its 30-record loss sample had no confirmed eligible records, with one abstract-less commentary remaining uncertain. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; P1-F1 should-fix rejected
- Round 2 on version 4: 2 findings; P1-F1 should-fix rejected, P2-F1 must-fix resolved
- Round 3 on version 6: 2 findings; P1-F1 should-fix rejected, P2-F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 984 NCBI requests logged (605 from cache); strategy sha256 14e8f101df1e._

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
      "requested": "Environmental Health",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T16:39:11+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "\"Environmental Health\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Exposure",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T16:39:11+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Environmental Exposure\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Environmental Pollution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T16:39:11+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Environmental Pollution\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Systematic Reviews as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T16:39:11+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Systematic Reviews as Topic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Meta-Analysis as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T16:39:11+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Meta-Analysis as Topic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Review Literature as Topic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T16:39:11+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Review Literature as Topic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Environmental Health\"[MeSH Terms] OR \"Environmental Exposure\"[MeSH Terms] OR \"Environmental Pollution\"[MeSH Terms] OR \"Environmental Health\"[Title/Abstract] OR \"environmental medicine\"[Title/Abstract] OR \"environmental epidemiolog*\"[Title/Abstract] OR \"environmental toxicolog*\"[Title/Abstract] OR \"environmental health science*\"[Title/Abstract] OR \"environmental hazard*\"[Title/Abstract] OR \"environmental exposure*\"[Title/Abstract]) AND (\"Systematic Reviews as Topic\"[MeSH Terms] OR \"Meta-Analysis as Topic\"[MeSH Terms] OR \"Review Literature as Topic\"[MeSH Terms] OR \"systematic review*\"[Title/Abstract] OR \"meta analy*\"[Title/Abstract] OR \"evidence synthesis\"[Title/Abstract] OR \"research synthesis\"[Title/Abstract] OR \"umbrella review*\"[Title/Abstract] OR (\"overview*\"[Title/Abstract] AND \"review*\"[Title/Abstract])) AND 1800/01/01:2020/07/20[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "67f46a17273703977b5c8b2550b232435aaac94026ef6bccdffa43e80e28aea7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts in the stated question and eligibility language have corresponding terms. The query translations preserve the intended fields and operators; no translation issues or warnings are reported in the packet."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are OR-combined internally and AND-combined in the final query. The optional assessment block was tested as an AND block; the packet reports a 31.5% reduction, no known relevant records lost, and 0/30 relevant records in the screened loss sample, while acknowledging residual recall risk."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied MeSH headings are reported as verified, and no heading mapping or syntax problems are reported. Free-text terms supplement the headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover environmental health/exposure contexts, systematic reviews and meta-analyses, and assessment/methodology language named in the scope. The known relevant development records are retrieved by all three blocks. No unsupported phrase warning or known-term omission is evidenced in the packet."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query and translations are shown, with no raw diagnostics, translation issues, or lint findings reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date ceiling is imposed by the user's harness instruction and PSB_AS_OF=2020-07-20 for this historical run. It is documented in protocol notes and is not a publication-date filter. The output will be labeled as bounded through 2020-07-20, not as a current search."
        }
      },
      "findings": [
        {
          "id": "P1-F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query contains an Entrez Date cutoff of 2020-07-20 even though protocol.limits is empty and no date limit was requested. The packet documents that this is the PSB_AS_OF access boundary, but records entered after the cutoff are absent from this result set.",
          "recommendation": "For a current search, rerun the complete strategy against PubMed through the intended search date, remove the fixed Entrez Date ceiling, and report the actual search date and any deliberate limits. If this packet's historical access boundary must be retained, label the results explicitly as bounded through 2020-07-20 and do not present them as current.",
          "status": "rejected",
          "response": "This finding does not apply to the requested run: the user explicitly instructed that PubMed be treated as of 2020-07-20 and that PSB_AS_OF remain set for every command. The skill applies this as an Entrez-date bound, not a publication-date [dp] limit. The protocol notes record the bound and the handoff will label the results accordingly."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "67f46a17273703977b5c8b2550b232435aaac94026ef6bccdffa43e80e28aea7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility action terms assess, appraise, describe, and compare were added to the optional methodological-rigour block as assess*, apprais*, describ*, and compar* and tested. The broadened block was then left out under the protocol's optional-concept rule because its measured reduction was 18.7%, below the approximately 30% threshold; the two required core blocks remain in the query."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are OR-combined internally and AND-combined in the final query. The optional quality block was tested as an AND block and reduced the candidate count by 31.5%; no known relevant development records were lost and the loss sample had 0/30 relevant records. The packet appropriately records residual recall uncertainty."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the supplied MeSH headings as verified and gives no heading-mapping or syntax issues. Free-text terms supplement the headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The bare-name action stems assess*, apprais*, describ*, and compar* were added to the optional methodological-rigour block and tested in the updated complete evaluation. The optional block was left out after testing because it did not meet the material-reduction criterion."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query and translations are supplied. The packet reports no raw diagnostics, translation issues, or lint findings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2020-07-20 Entrez-date ceiling is documented as the historical PSB_AS_OF access boundary, not a publication-date filter. The round-1 finding was rejected on that basis; results must be described as bounded through that date."
        }
      },
      "findings": [
        {
          "id": "P1-F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query contains an Entrez Date cutoff of 2020-07-20 even though protocol.limits is empty and no date limit was requested. The packet documents that this is the PSB_AS_OF access boundary, but records entered after the cutoff are absent from this result set.",
          "recommendation": "For a current search, rerun the complete strategy against PubMed through the intended search date, remove the fixed Entrez Date ceiling, and report the actual search date and any deliberate limits. If this packet's historical access boundary must be retained, label the results explicitly as bounded through 2020-07-20 and do not present them as current.",
          "status": "rejected",
          "response": "This finding does not apply to the requested run: the user explicitly instructed that PubMed be treated as of 2020-07-20 and that PSB_AS_OF remain set for every command. The skill applies this as an Entrez-date bound, not a publication-date [dp] limit. The protocol notes record the bound and the handoff will label the results accordingly."
        },
        {
          "id": "P2-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes studies that assess, appraise, describe, or compare the methodology of reviews. The assessment block does not search the bare names of these actions: it has phrases such as critical appraisal and quality assessment, but no assess*, apprais*, describ*, or compar* text-word expression. This fails the packet's explicit translation check for members named in eligibility.",
          "recommendation": "Add explicit tested bare-name text-word expressions for the eligibility actions (for example, assess*, apprais*, describ*, and compar*) to the methodological-rigour block, then perform another complete evaluation, including query diagnostics, counts, known-record retrieval, and optional-block loss assessment.",
          "status": "resolved",
          "response": "Added assess*[tiab], apprais*[tiab], describ*[tiab], and compar*[tiab] to the methodological-rigour block and ran a complete evaluation. The broadened block reduces the core query count by 18.7% (6,351 to 5,164), below the skill's approximate 30% material-reduction criterion, so the current measured decision is leave_out. The final strategy retains the two required environmental-health and systematic-review blocks; the historical evaluation shows the optional terms were explicitly tested."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "52125076955d40bbfc34cbc6ac594643c86a110c4f0df1d5c919c5856ca94fd8",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required environmental-health and systematic-review concepts have corresponding MeSH and title/abstract terms. The four eligibility actions assess, appraise, describe, and compare were added as assess*, apprais*, describ*, and compar* to the optional methodological-rigour block, then tested. That optional block was left out under the documented reduction criterion; the two required blocks remain in the current query."
        },
        "operators": {
          "verdict": "pass",
          "note": "The terms are OR-combined within each required block, and the two blocks are AND-combined. The optional methodological-rigour block was tested as an additional AND block; it reduced results by 18.7% (6,351 to 5,164), below the approximately 30% material-reduction criterion. The loss sample found no clearly eligible record, with one title-only commentary remaining uncertain, and the rationale for leaving the block out is recorded."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the supplied MeSH headings as verified and reports no heading-mapping or syntax issues. Free-text terms supplement the headings in both required blocks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The required blocks include environmental-health/exposure context and systematic-review/meta-analysis terminology. The eligibility action stems were explicitly added to and tested in the optional outcome block; the decision to leave that block out is supported by its measured reduction and loss-sample record. The two known relevant development records are retrieved by both required blocks and by the complete query."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query and PubMed translation are supplied. Diagnostics, translation issues, and lint findings are empty; no phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2020-07-20 Entrez Date ceiling is documented as the historical PSB_AS_OF access boundary rather than a publication-date filter. Results must be described as bounded through that date. The round-1 filter finding was rejected for this requested historical run."
        }
      },
      "findings": [
        {
          "id": "P1-F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query contains an Entrez Date cutoff of 2020-07-20 even though protocol.limits is empty and no date limit was requested. The packet documents that this is the PSB_AS_OF access boundary, but records entered after the cutoff are absent from this result set.",
          "recommendation": "For a current search, rerun the complete strategy through the intended search date, remove the fixed Entrez Date ceiling, and report the actual search date and any deliberate limits. If the historical access boundary is retained, label the results explicitly as bounded through 2020-07-20 and do not present them as current.",
          "status": "rejected",
          "response": "This finding does not apply to the requested run: the user explicitly instructed that PubMed be treated as of 2020-07-20 and that PSB_AS_OF remain set for every command. The protocol notes document this Entrez-date bound, not a publication-date filter; the results must be labeled accordingly."
        },
        {
          "id": "P2-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility includes studies that assess, appraise, describe, or compare review methodology, but the then-current assessment block lacked bare-name assess*, apprais*, describ*, and compar* text-word expressions.",
          "recommendation": "Add explicit tested bare-name text-word expressions for the eligibility actions to the methodological-rigour block, then perform another complete evaluation, including query diagnostics, counts, known-record retrieval, and optional-block loss assessment.",
          "status": "resolved",
          "response": "The four stems were added to the optional block and a complete evaluation was run. The updated block reduces the core count by 18.7%, below the approximate 30% material-reduction criterion, so it was left out. The current strategy retains the two required blocks, and the packet documents that the optional terms were tested."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


# PubMed search strategy: audit

Generated 2026-09-29T00:41:57+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis / longitudinal course
- Scope confirmed by user: no (The user requested no follow-up questions. Assumptions: broad human population and traumatic-event types; no language, publication-date, or study-design limits. PSB_AS_OF is set to 2016-01-24 for every command by the harness; no publication-date filter is added. No known relevant articles were supplied; proceed at standard depth as requested. Scope was not confirmed by the user.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder and post-traumatic stress symptoms | search | Core condition and symptom domain; the review cannot include records without post-traumatic stress symptoms, and these terms are normally named or indexed. |
| Symptom trajectories and longitudinal course | optional | Defines the topic, and trajectory/course labels are searchable, but longitudinal symptom studies may describe repeated change without naming a trajectory; test before deciding whether to AND. |
| Exposure to a traumatic event | optional | The question names trauma exposure, which is searchable by generic and event-type wording, but event labels vary. Test it as an optional AND block rather than require it without loss evidence. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T00:41:30+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,186
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `"Stress Disorders, Traumatic, Acute"[Mesh]` | 387 | none |
| 3 | `"PTSD"[tiab]` | 15,732 | none |
| 4 | `"posttraumatic stress disorder*"[tiab]` | 12,654 | none |
| 5 | `"post-traumatic stress disorder*"[tiab]` | 7,263 | none |
| 6 | `"post traumatic stress disorder*"[tiab]` | 7,263 | none |
| 7 | `"posttraumatic stress symptom*"[tiab]` | 1,177 | none |
| 8 | `"post-traumatic stress symptom*"[tiab]` | 474 | none |
| 9 | `"post traumatic stress symptom*"[tiab]` | 474 | none |
| 10 | `"PTSD symptom*"[tiab]` | 4,408 | none |
| 11 | `"acute stress disorder"[tiab]` | 469 | none |
| 12 | `PTSS[tiab]` | 510 | none |
| 13 | `posttraumatic stress[tiab]` | 14,174 | none |
| 14 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13` | 32,186 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR "Stress Disorders, Traumatic, Acute"[Mesh] OR "PTSD"[tiab] OR "posttraumatic stress disorder*"[tiab] OR "post-traumatic stress disorder*"[tiab] OR "post traumatic stress disorder*"[tiab] OR "posttraumatic stress symptom*"[tiab] OR "post-traumatic stress symptom*"[tiab] OR "post traumatic stress symptom*"[tiab] OR "PTSD symptom*"[tiab] OR "acute stress disorder"[tiab] OR PTSS[tiab] OR posttraumatic stress[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectories and longitudinal course | left out | 32,186 / 5,848 | 81.8% | 17641114, 21443298, 24845188, 26137356 | 0/30 (up to 10% of removed records could be relevant) | The updated 30-record sample had no additional clearly eligible records, but the current known set shows the block would lose four relevant studies (PMIDs 21443298, 24845188, 26137356, 17641114). Its roughly 81.8% reduction cannot justify that demonstrated recall loss. |
| Exposure to a traumatic event | left out | 32,186 / 24,929 | 22.5% | 26764215 | 0/30 (up to 10% of removed records could be relevant) | On the current evaluation the event block reduces retrieval by 22.5%, and the updated 30-record loss sample contained no eligible studies. It would still lose one screened relevant record (PMID 26764215), while PTSD itself implies trauma and event labels vary; leave the block out. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Exposure to a traumatic event | 1 | `PTSD[tiab] OR posttraumatic stress[tiab] OR posttraumatic stress disorder*[tiab] OR Stress Disorders, Post-Traumatic[Mesh]` | 7,366 | 1/30 |
| Exposure to a traumatic event | 2 | `(PTSD[tiab] OR posttraumatic stress[tiab] OR posttraumatic stress disorder*[tiab] OR Stress Disorders, Post-Traumatic[Mesh])` | 7,354 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 31,762 | initial | none | Initial scope-derived PTSD symptom block; trajectory/course tested as optional because studies may report repeated symptoms without trajectory labels. No screened relevant studies or known seeds available. |
| 2 | 31,919 | ptsd: +1 / -0 | none | Added bare PTSS abbreviation after internal critique and introduced trauma-event terms as a second optional block to address the over-budget warning. |
| 3 | 31,919 | limits/combination | none | Category probe found a relevant study identified by acute coronary syndrome rather than generic trauma wording (PMID 21500103); added that event member to the optional block before probing again. |
| 4 | 31,919 | limits/combination | none | A screened eligible trajectory study after earthquakes (PMID 26137356) named its event type rather than a generic trauma term; added the MeSH Natural Disasters heading and earthquake* to the optional event block. |
| 5 | 32,186 | ptsd: +1 / -0 | none | Added the high-coverage bare phrase posttraumatic stress[tiab] from objective development-set term ranking; it avoids requiring records to say disorder or symptoms explicitly. |
| 6 | 32,186 | limits/combination | none | Added PMID 17641114 under the broad assumption that repeated PTSS change after a potentially traumatic cancer diagnosis is in scope, even when an intervention is studied; added cancer[tiab] as this specific event member in the optional block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 3 findings; F1 must-fix open, F2 should-fix open, F3 should-fix open
- Round 2 on version 6: 3 findings; F1 must-fix open, F2 should-fix resolved, F3 should-fix resolved
- Round 3 on version 6: 4 findings; F1 document accepted-risk, F2 should-fix resolved, F3 should-fix resolved, F4 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1001 NCBI requests logged (545 from cache); strategy sha256 f13101ea4c20._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "over_workload_budget",
        "message": "32,186 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:trauma_event",
        "blocking": false,
        "requires_review": true,
        "id": "I-526ebe72a1e127eca333"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "32,186 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:trauma_event",
        "blocking": false,
        "requires_review": true,
        "id": "I-526ebe72a1e127eca333"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:41:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013313",
          "name": "Stress Disorders, Post-Traumatic",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders with symptoms that last more than one month.",
          "tree_numbers": [
            "F03.950.750.500"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013313",
      "preferred_label": "Stress Disorders, Post-Traumatic",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Traumatic, Acute",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:41:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D040701",
          "name": "Stress Disorders, Traumatic, Acute",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders that is characterized by the significant dissociative states seen immediately after overwhelming trauma. By definition it cannot last longer than 1 month, if it persists, a diagnosis of post-traumatic stress disorder (STRESS DISORDERS, POST-TRAUMATIC) is more appropriate.",
          "tree_numbers": [
            "F03.950.750.550"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D040701",
      "preferred_label": "Stress Disorders, Traumatic, Acute",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Stress Disorders, Traumatic, Acute\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"stress disorders, traumatic, acute\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"posttraumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"ptsd symptom*\"[Title/Abstract] OR \"acute stress disorder\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "da5e8c75f1787056c03b3fdb489cfad0b6eb9c7b2f3d6f9295d7b8555376e3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "MeSH and tiab blocks match the question, and the optional trajectory decision is supported by a relevant loss-sample record."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within the PTSD block; optional trajectory block was tested and left out to protect recall."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Both selected descriptors were verified."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add bare PTSS abbreviation as a common title/abstract synonym."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are field-tagged and PubMed translations show no syntax diagnostics."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The EDAT restriction is mandated by the harness cutoff and must be retained; it is not a publication-date filter."
        }
      },
      "findings": [
        {
          "id": "F1",
          "recommendation": "Remove EDAT or document and authorize it.",
          "kind": "filter",
          "status": "open",
          "severity": "must-fix",
          "finding": "The executed query adds EDAT 1800/01/01 through 2016/01/24 despite the stated absence of publication-date limits.",
          "domain": "limits_filters",
          "response": ""
        },
        {
          "id": "F2",
          "recommendation": "Add PTSS[tiab] and evaluate.",
          "kind": "lexical",
          "status": "open",
          "severity": "should-fix",
          "finding": "The symptom concept lacks bare PTSS[tiab].",
          "domain": "text_words",
          "response": ""
        },
        {
          "id": "F3",
          "recommendation": "Test a trauma-event block and inspect loss.",
          "kind": "scope",
          "status": "open",
          "severity": "should-fix",
          "finding": "Trauma-event screen concept was not evaluated as optional despite over-budget warning.",
          "domain": "text_words",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "evidence": "Only trajectory/course appears in the current optional-concept table.",
          "status": "rejected",
          "response": "The trauma-event concept still needs an optional-block test before this workload warning can be accepted."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "dbb54928c349b4acb4735611b94b81c3340c68fc86b1dac1b664c13e84330ea3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD is the required searchable concept; trajectory wording and traumatic-event labels remain optional because ablation and known-loss checks showed recall losses."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines the PTSD synonyms and no restrictive Boolean block or NOT is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "PTSD and acute stress disorder headings are included and verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current block includes bare PTSS, PTSD symptom variants, and posttraumatic stress wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Terms are field tagged and translation diagnostics are clear."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The entry-date bound is required by the harness cutoff and is not a publication-date [dp] limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "status": "open",
          "finding": "The query has an Entrez entry-date bound through 2016-01-24.",
          "recommendation": "Remove or document the required bound, while avoiding a publication-date filter.",
          "response": "The harness explicitly requires PSB_AS_OF=2016-01-24 for every command and prohibits a [dp] cutoff. The query bound is the required Entrez entry-date limit."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "status": "resolved",
          "finding": "The symptom concept lacked bare PTSS[tiab].",
          "recommendation": "Add PTSS[tiab] and evaluate.",
          "response": "Added PTSS[tiab] to the PTSD block and reran evaluation."
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "status": "resolved",
          "finding": "Trauma-event wording had not been tested as an optional concept.",
          "recommendation": "Test a trauma-event block and inspect known-record losses.",
          "response": "Tested it; retrieval fell 22.5% and known relevant PMID 26764215 was lost, so the block remains out of the query."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "Optional trajectory and trauma-event blocks were both evaluated. The trauma-event block lost PMID 26764215, so it was not used to narrow the query.",
          "evidence": "Ablation measured a 22.5% reduction with the trauma-event block and one known relevant loss."
        },
        {
          "issue_id": "I-526ebe72a1e127eca333",
          "status": "accepted-risk",
          "response": "The stale probe status is a residual risk after the core block was broadened and the two-probe budget was spent; this will be reported for human PRESS review.",
          "evidence": "Two 30-record probes were completed. The first found relevant PMID 21500103 and led to adding acute coronary syndrome; the second found no additional relevant records. Later core broadening made the probe stale."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "dbb54928c349b4acb4735611b94b81c3340c68fc86b1dac1b664c13e84330ea3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required PTSD and symptom block includes PTSD, PTSS, and posttraumatic stress wording. The optional trajectory and trauma-event blocks were tested and left out because each would lose known relevant records."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD synonyms are ORed together; neither optional concept is ANDed into the final strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included PTSD and acute stress disorder MeSH descriptors are verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The bare PTSS[tiab] term requested in the earlier review is present. The final block retrieves all 12 known relevant and validation records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current query has no syntax diagnostics. Its terms are field-tagged, and no proximity expressions require interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The query's EDAT upper bound of 2016-01-24 is mandated by PSB_AS_OF for every command. It limits Entrez entry date, not publication date; it is not a [dp] limit, and the protocol records no user-requested publication-date limit. Document this harness-imposed bound when reporting the search."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The executed query has an EDAT bound through 2016-01-24, imposed by the harness setting PSB_AS_OF.",
          "recommendation": "Report the harness-imposed Entrez entry-date bound and distinguish it from a publication-date [dp] limit.",
          "status": "accepted-risk",
          "response": "Accepted as a documented harness constraint: PSB_AS_OF requires the EDAT bound for every command. It is not a [dp] publication-date filter and does not represent a user-requested publication-date limit."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The symptom concept lacked bare PTSS[tiab].",
          "recommendation": "Add PTSS[tiab] and evaluate.",
          "status": "resolved",
          "response": "PTSS[tiab] is in the current PTSD block, which retrieves all 12 known relevant and validation records."
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Trauma-event wording had not been tested as an optional concept.",
          "recommendation": "Test a trauma-event block and inspect known-record losses.",
          "status": "resolved",
          "response": "The optional trauma-event block was evaluated. It reduces retrieval by 22.5% and loses known relevant PMID 26764215, so it remains out of the final query."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "The trauma-event category probe is stale because the candidate block gained terms after the two-probe budget was spent.",
          "recommendation": "If the trauma-event block is reconsidered for inclusion, run a fresh category probe on its current terms.",
          "status": "accepted-risk",
          "response": "The final strategy leaves this block out, so the stale probe does not change final retrieval. The current optional-block evaluation found a known relevant loss; report the stale probe as a limitation if the block is revisited."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "The workload warning has been reviewed: both searchable optional concepts were evaluated, and both were left out based on demonstrated losses of known relevant studies.",
          "evidence": "The trajectory block reduces retrieval by 81.8% and loses four known relevant records; the trauma-event block reduces retrieval by 22.5% and loses PMID 26764215. The final PTSD block retrieves all 12 known relevant and validation records."
        },
        {
          "issue_id": "I-526ebe72a1e127eca333",
          "status": "accepted-risk",
          "response": "The category probe became stale after the trauma-event candidate block gained terms beyond those tested in the second probe. The block is left out of the final strategy; if reconsidered, it needs a fresh probe.",
          "evidence": "The second probe tested a block including acute coronary syndrome wording; the current candidate additionally includes Natural Disasters MeSH, earthquake*, and cancer. The latest optional-block evaluation shows a 22.5% reduction and loss of known relevant PMID 26764215."
        }
      ]
    }
  ]
}
```


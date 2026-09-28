# PubMed search strategy: audit

Generated 2026-09-28T13:36:47+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis
- Scope confirmed by user: no (User asked to proceed without questions and has no known relevant articles. Assumed prognosis framework; PTSD is the required search block; symptom trajectories/course is optional and will be tested; trauma context is screened because it is inherent to PTSD and not safely required as a second block. No age, language, or study-design limits. The requested historical snapshot requires the PubMed Entrez date (date added) bound through 2016-01-24 via PSB_AS_OF, including records already in PubMed by then even if their publication date is later; no publication-date [dp] limit is applied. Scope not confirmed because the user asked not to pause.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder | search | The condition defines the target population and is expected to be named or indexed. |
| PTSD symptom trajectories or course over time | optional | This is a topic-defining outcome with recognizable labels, but studies may report trajectories without naming them consistently; test before deciding whether to AND it. |
| Traumatic event and trauma exposure context | screen | The traumatic event is inherent to PTSD, may only be described in context, and adding a separate trauma block could unnecessarily reduce recall. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T13:36:12+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 9,080
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `"post-traumatic stress disorder"[tiab]` | 7,081 | none |
| 4 | `"posttraumatic stress disorder"[tiab]` | 12,500 | none |
| 5 | `"post traumatic stress disorder"[tiab]` | 7,081 | none |
| 6 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 7 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 8 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 9 | `"post-traumatic neurosis"[tiab]` | 22 | none |
| 10 | `"posttraumatic neurosis"[tiab]` | 7 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 32,081 | none |
| 12 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 13 | `trajector*[tiab]` | 43,863 | none |
| 14 | `longitudinal[tiab]` | 168,713 | none |
| 15 | `follow-up[tiab]` | 703,004 | none |
| 16 | `"natural history"[tiab]` | 39,676 | none |
| 17 | `course[tiab]` | 460,316 | none |
| 18 | `courses[tiab]` | 59,665 | none |
| 19 | `"symptom change"[tiab]` | 558 | none |
| 20 | `"symptom changes"[tiab]` | 301 | none |
| 21 | `change[tiab]` | 811,160 | none |
| 22 | `changes[tiab]` | 1,644,280 | none |
| 23 | `"symptom pattern"[tiab]` | 345 | none |
| 24 | `"symptom patterns"[tiab]` | 611 | none |
| 25 | `pattern[tiab]` | 565,490 | none |
| 26 | `patterns[tiab]` | 523,313 | none |
| 27 | `chronicity[tiab]` | 7,037 | none |
| 28 | `persistence[tiab]` | 68,487 | none |
| 29 | `remission[tiab]` | 92,395 | none |
| 30 | `recovery[tiab]` | 341,793 | none |
| 31 | `remitting[tiab]` | 7,993 | none |
| 32 | `"over time"[tiab]` | 128,863 | none |
| 33 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32` | 4,556,696 | none |
| 34 | `#11 AND #33` | 9,080 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR "post-traumatic stress disorder"[tiab] OR "posttraumatic stress disorder"[tiab] OR "post traumatic stress disorder"[tiab] OR "post-traumatic stress"[tiab] OR "posttraumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "post-traumatic neurosis"[tiab] OR "posttraumatic neurosis"[tiab]) AND ("Longitudinal Studies"[Mesh] OR trajector*[tiab] OR longitudinal[tiab] OR follow-up[tiab] OR "natural history"[tiab] OR course[tiab] OR courses[tiab] OR "symptom change"[tiab] OR "symptom changes"[tiab] OR change[tiab] OR changes[tiab] OR "symptom pattern"[tiab] OR "symptom patterns"[tiab] OR pattern[tiab] OR patterns[tiab] OR chronicity[tiab] OR persistence[tiab] OR remission[tiab] OR recovery[tiab] OR remitting[tiab] OR "over time"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| PTSD symptom trajectories or course over time | AND-ed | 32,081 / 9,080 | 71.7% | none | 0/30 (up to 10% of removed records could be relevant) | After broadening the terms to include the protocol's bare-name change and pattern members, the block reduces the query from 32,081 to 9,080 (71.7%) and retrieves all four screened relevant development records. None of the 30 records in the refreshed loss sample clearly met the inclusion criteria; one prospective treatment-outcome paper was uncertain because repeated PTSD assessment times were not explicit in the abstract. The count reduction remains material and below the 10,000-record standard budget, so retain the block while flagging possible loss of sparsely described longitudinal studies for human review. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 4,556,696 | 0 |
| trajectory | 32,081 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first condition block drafted from PTSD MeSH lookup and broad historical/current name variants; trajectory/course held optional for empirical testing. |
| 2 | 32,081 | ptsd: +10 / -0 | none | Corrected strategy schema to term arrays; PTSD MeSH and title/abstract synonyms retained, broad course/trajectory candidate held optional. |
| 3 | 6,033 | trajectory: +17 / -0 | none | Moved the measured trajectory/course concept into the delivered AND strategy after passing the optional-block rule: material reduction, no known relevant loss, and 0/30 eligible in the loss sample. |
| 4 | 9,080 | trajectory: +4 / -0 | none | Added bare-name change/changes and pattern/patterns terms per critic R1-01. Clarified that the explicit Entrez-date as_of bound reproduces the harness's historical PubMed snapshot and is not a publication-date limit, addressing R1-02 without dropping the required cutoff. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-01 must-fix resolved, R1-02 must-fix rejected
- Round 2 on version 4: 2 findings; R1-01 must-fix resolved, R1-02 must-fix rejected
- Round 3 on version 4: 2 findings; R1-01 must-fix resolved, R1-02 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 413 NCBI requests logged (137 from cache); strategy sha256 941c4571d967._

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
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:36:12+00:00",
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
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:36:12+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008137",
          "name": "Longitudinal Studies",
          "type": "descriptor",
          "scope_note": "Studies in which variables relating to an individual or group of individuals are assessed over a period of time.",
          "tree_numbers": [
            "E05.318.372.500.750.500",
            "N05.715.360.330.500.750.500",
            "N06.850.520.450.500.750.500"
          ],
          "entry_terms": 32,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008137",
      "preferred_label": "Longitudinal Studies",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress disorder\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic neurosis\"[Title/Abstract] OR \"posttraumatic neurosis\"[Title/Abstract]) AND (\"Longitudinal Studies\"[MeSH Terms] OR \"trajector*\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"natural history\"[Title/Abstract] OR \"course\"[Title/Abstract] OR \"courses\"[Title/Abstract] OR \"symptom change\"[Title/Abstract] OR \"symptom changes\"[Title/Abstract] OR \"change\"[Title/Abstract] OR \"changes\"[Title/Abstract] OR \"symptom pattern\"[Title/Abstract] OR \"symptom patterns\"[Title/Abstract] OR \"pattern\"[Title/Abstract] OR \"patterns\"[Title/Abstract] OR \"chronicity\"[Title/Abstract] OR \"persistence\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"recovery\"[Title/Abstract] OR \"remitting\"[Title/Abstract] OR \"over time\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "8f560a694e25f333b18325bbd7743c82ab3df912a62904b219cc70ff776b04c7",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The trajectory block includes change and pattern only in phrases narrowed by symptom, although eligibility names change and patterns as separate course features."
        },
        "operators": {
          "verdict": "pass",
          "note": "The condition and optional course blocks are OR-combined internally and AND-combined as tested. The packet supports the optional block's workload rationale and reports its sample uncertainty."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The PTSD and Longitudinal Studies headings are verified in the packet and are relevant to their respective blocks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover PTSD naming variants and multiple course or longitudinal expressions. No phrase warnings or proximity operators are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed Boolean structure, field tags, and PubMed translations have no reported syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final query applies an Entrez-date upper bound of 2016-01-24 despite the protocol stating no publication-date limit. This excludes later PubMed entries and needs reconciliation with the intended search scope."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names change and patterns as course features, but the strategy searches only \"symptom change(s)\" and \"symptom pattern(s)\". It does not cover the named members by their own bare names, as required by the packet's translation check.",
          "recommendation": "Add and test bare-name expressions for change and pattern (including relevant singular and plural forms), then rerun the complete evaluation and reassess the optional block decision and workload.",
          "status": "resolved",
          "response": "Added change[tiab], changes[tiab], pattern[tiab], and patterns[tiab] to the trajectory block, refreshed the optional loss sample, re-evaluated the full strategy, and confirmed all four relevant development records remain retrieved. The count changed from 6,033 to 9,080; it remains under the 10,000 standard workload budget and the block still has a current optional decision."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query restricts Entrez dates to 1800-01-01 through 2016-01-24, while the protocol says there is no publication-date limit. This cutoff excludes records entered into PubMed after that date, regardless of their publication date.",
          "recommendation": "Reconcile the cutoff with the intended scope. If the search is intended to have no date restriction, remove the Entrez-date bound and rerun all counts and optional-block evaluation; if the cutoff is intentional, state and justify its scope explicitly.",
          "status": "rejected",
          "response": "The user and harness explicitly require treating the search date as 2016-01-24 and constraining PubMed to records already entered by that date. The protocol now states this Entrez-date bound and its purpose, including that records present by then may have later publication dates. No publication-date [dp] limit is used. Removing the bound would violate the task's explicit as-of instruction."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "0d1ceca90ef9cc7ab9ec889572812f1a645e31d5a11e90707199af812332ac9c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The trajectory block now includes bare change, changes, pattern, and patterns terms, addressing R1-01. The searched PTSD concept is represented by relevant MeSH and text-word variants."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks use OR internally and are AND-combined. The optional trajectory block has a documented workload rationale, loss sample, and acknowledged uncertainty."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the PTSD and Longitudinal Studies MeSH headings and their relevance to the respective blocks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover PTSD naming variants and multiple course and longitudinal expressions. No phrase warnings or proximity operators are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed Boolean structure, field tags, and PubMed translations report no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The protocol explains the 2016-01-24 Entrez-date bound as the requested historical search date and clarifies that no publication-date limit is applied, resolving R1-02."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names change and patterns as course features, but the earlier strategy searched only symptom-qualified phrases.",
          "recommendation": "Add and test bare-name expressions for change and pattern, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current trajectory block includes change[tiab], changes[tiab], pattern[tiab], and patterns[tiab]. The packet reports a complete reevaluation, all four relevant development records retrieved, and a current optional-block decision."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The earlier protocol did not reconcile the Entrez-date upper bound with the stated absence of a publication-date limit.",
          "recommendation": "Clarify whether the cutoff is intentional and justify its scope, or remove it and rerun the evaluation.",
          "status": "rejected",
          "response": "The packet states that the requested historical snapshot uses an Entrez-date bound through 2016-01-24, including records entered by then even if published later. It uses no publication-date limit."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "0d1ceca90ef9cc7ab9ec889572812f1a645e31d5a11e90707199af812332ac9c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "R1-01 was addressed: the trajectory block now includes bare change, changes, pattern, and patterns terms. The complete reevaluation reports all four relevant development records retrieved."
        },
        "operators": {
          "verdict": "pass",
          "note": "The condition and trajectory terms are OR-combined within their blocks, and the blocks are AND-combined. The optional block has a documented workload rationale and loss sample with its uncertainty acknowledged."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the PTSD and Longitudinal Studies MeSH headings and their relevance to the respective blocks."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy covers PTSD naming variants and multiple course and longitudinal expressions. No phrase warnings or proximity operators are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed Boolean structure, field tags, and PubMed translations report no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "R1-02 is accounted for: the protocol explains the 2016-01-24 Entrez-date bound as the requested historical snapshot and states that no publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names change and patterns as course features, while the earlier strategy searched only symptom-qualified phrases.",
          "recommendation": "Add and test bare-name expressions for change and pattern, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current trajectory block includes change[tiab], changes[tiab], pattern[tiab], and patterns[tiab]. The packet reports a complete reevaluation, all four relevant development records retrieved, and a current optional-block decision."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The earlier protocol did not reconcile the Entrez-date upper bound with the stated absence of a publication-date limit.",
          "recommendation": "Clarify whether the cutoff is intentional and justify its scope, or remove it and rerun the evaluation.",
          "status": "rejected",
          "response": "The packet states that the requested historical snapshot uses an Entrez-date bound through 2016-01-24, including records entered by then even if published later. It uses no publication-date limit."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


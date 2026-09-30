# PubMed search strategy: audit

Generated 2026-09-30T14:10:17+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis
- Scope confirmed by user: yes (User asked to proceed without questions. Assumed human studies and symptom patterns/course after any traumatic event, without restrictions by event type, age, language, or design. The traumatic event is screened because event types are heterogeneous and PTSD terminology already conveys trauma exposure; no separate trauma-event block was required. Symptom course/trajectory is optional and tested but left out because it demonstrably loses an eligible known record and only 11 development records are available. No user-supplied seeds; 11 records discovered and screened into a development set, so recall is not independently validated. Search is bounded by Entrez date 2016-01-24 via PSB_AS_OF; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| PTSD and post-traumatic stress symptoms | search | The condition/symptom domain defines the topic and is searchable; records may name symptom measures or symptom wording without the full PTSD label. |
| Symptom course, change, or trajectory over time | optional | Trajectory is the topic-defining outcome but may appear inconsistently in titles/abstracts, so test the block before deciding whether to AND it. |
| Exposure to a traumatic event | screen | Event types are broad and often reported only in context; screen for a traumatic event rather than require a fragile event block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:09:52+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,908
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Stress Disorders, Post-Traumatic[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `post-traumatic stress[tiab]` | 8,160 | none |
| 4 | `posttraumatic stress[tiab]` | 14,174 | none |
| 5 | `post traumatic stress[tiab]` | 8,160 | none |
| 6 | `post-traumatic stress disorder*[tiab]` | 7,263 | none |
| 7 | `posttraumatic stress disorder*[tiab]` | 12,654 | none |
| 8 | `post traumatic stress disorder*[tiab]` | 7,263 | none |
| 9 | `post-traumatic stress symptom*[tiab]` | 474 | none |
| 10 | `posttraumatic stress symptom*[tiab]` | 1,177 | none |
| 11 | `post traumatic stress symptom*[tiab]` | 474 | none |
| 12 | `PTSS[tiab]` | 510 | none |
| 13 | `posttraumatic symptom*[tiab]` | 403 | none |
| 14 | `"pediatric medical traumatic stress"[tiab]` | 5 | none |
| 15 | `"medical traumatic stress"[tiab]` | 10 | none |
| 16 | `trauma symptom*[tiab]` | 595 | none |
| 17 | `trauma-related symptom*[tiab]` | 200 | none |
| 18 | `traumatic stress symptom*[tiab]` | 626 | none |
| 19 | `"PTSD Checklist"[tiab]` | 541 | none |
| 20 | `PCL-C[tiab]` | 188 | none |
| 21 | `PCL-M[tiab]` | 57 | none |
| 22 | `PCL-S[tiab]` | 54 | none |
| 23 | `PCL-5[tiab]` | 63 | none |
| 24 | `"Impact of Event Scale"[tiab]` | 1,012 | none |
| 25 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 32,908 | none |

### Strategy (single line, for copying into PubMed)

```text
((Stress Disorders, Post-Traumatic[Mesh] OR PTSD[tiab] OR post-traumatic stress[tiab] OR posttraumatic stress[tiab] OR post traumatic stress[tiab] OR post-traumatic stress disorder*[tiab] OR posttraumatic stress disorder*[tiab] OR post traumatic stress disorder*[tiab] OR post-traumatic stress symptom*[tiab] OR posttraumatic stress symptom*[tiab] OR post traumatic stress symptom*[tiab] OR PTSS[tiab] OR posttraumatic symptom*[tiab] OR "pediatric medical traumatic stress"[tiab] OR "medical traumatic stress"[tiab] OR trauma symptom*[tiab] OR trauma-related symptom*[tiab] OR traumatic stress symptom*[tiab] OR "PTSD Checklist"[tiab] OR PCL-C[tiab] OR PCL-M[tiab] OR PCL-S[tiab] OR PCL-5[tiab] OR "Impact of Event Scale"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom course, change, or trajectory over time | left out | 32,908 / 8,283 | 74.8% | 10221639 | 0/30 (up to 10% of removed records could be relevant) | The refreshed loss sample found no clearly eligible additional record; PMID 9817630 and PMID 7263120 lacked sufficient abstract detail and remain uncertain. The earlier sample identified eligible longitudinal PTSD treatment study PMID 10221639. The current development set has 11 records, below the 15-record evidence threshold for AND-ing this block. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| PTSD and post-traumatic stress symptoms | 1 | `posttraumatic symptom*[tiab] OR trauma-related symptom*[tiab] OR traumatic stress symptom*[tiab] OR Stress Disorders, Post-Traumatic[Mesh]` | 60 | 1/30 |
| PTSD and post-traumatic stress symptoms | 2 | `posttraumatic symptom*[tiab] OR trauma-related symptom*[tiab] OR traumatic stress symptom*[tiab] OR medical traumatic stress[tiab] OR trauma symptom*[tiab] OR Stress Disorders, Post-Traumatic[Mesh]` | 249 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,261 | initial | none | Initial recall-first draft; one PTSD/post-traumatic stress symptom block with MeSH and free text. Trajectory/course is a tested optional block because it defines the topic but may be reported inconsistently. |
| 2 | 32,510 | ptsd_symptoms: +5 / -0 | none | Widened the category block with pediatric medical traumatic stress and trauma-symptom wording after probe 1 found an eligible longitudinal record without PTSD terminology. Probe 2 produced candidate records, but no additional clearly eligible records were confirmed; its full sample was screened. |
| 3 | 32,908 | ptsd_symptoms: +6 / -0 | none | Added full or version-specific PTSD symptom instrument names after testing the added yield. The screened sample did not confirm eligible additional studies, but instrument terms may retrieve unindexed PTSD symptom reports; ambiguous standalone acronyms PCL and IES were excluded. Existing known records remain the retrieval benchmark. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; F-R1-01 must-fix open, F-R1-02 should-fix open
- Round 2 on version 3: 2 findings; F-R1-01 must-fix rejected, F-R1-02 should-fix rejected
- Round 3 on version 3: 2 findings; F-R1-01 must-fix rejected, F-R1-02 should-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 650 NCBI requests logged (271 from cache); strategy sha256 c1b8012b295b._

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
        "message": "32,908 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:trajectory",
        "blocking": false,
        "requires_review": true,
        "id": "I-af36a83285447cf63c9c"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "32,908 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:trajectory",
        "blocking": false,
        "requires_review": true,
        "id": "I-af36a83285447cf63c9c"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:09:52+00:00",
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
        "text": "Stress Disorders, Post-Traumatic",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"posttraumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"posttraumatic stress symptom*\"[Title/Abstract] OR \"post traumatic stress symptom*\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"posttraumatic symptom*\"[Title/Abstract] OR \"pediatric medical traumatic stress\"[Title/Abstract] OR \"medical traumatic stress\"[Title/Abstract] OR \"trauma symptom*\"[Title/Abstract] OR \"trauma related symptom*\"[Title/Abstract] OR \"traumatic stress symptom*\"[Title/Abstract] OR \"PTSD Checklist\"[Title/Abstract] OR \"PCL-C\"[Title/Abstract] OR \"PCL-M\"[Title/Abstract] OR \"PCL-S\"[Title/Abstract] OR \"PCL-5\"[Title/Abstract] OR \"Impact of Event Scale\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "b3cb9887bfd1a7f64e8409eb1755ceaa99cbdb3c4ef89cd40d6be6e9a8d57695",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The translated query covers the entered MeSH and title/abstract terms; no translation issues or PubMed errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD and symptom terms are ORed in one broad block, consistent with the scope. The optional course block was tested and left out after it lost a known eligible record."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Stress Disorders, Post-Traumatic is verified as a MeSH descriptor. No MeSH translation error is reported."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The protocol rationale says eligible records may name symptom measures without the full PTSD label, but the block has no measure names such as PTSD Checklist/PCL or Impact of Event Scale. Consider testing these terms and screening their yield."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has no reported lint or PubMed syntax errors. The multiword and wildcard expressions shown have no proximity operators."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The query applies an Entrez entry-date ceiling of 2016-01-24, although the question and eligibility criteria specify no historical cutoff. This excludes later records and needs an explicit scope rationale or removal."
        }
      },
      "findings": [
        {
          "id": "F-R1-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits records to entry dates through 2016-01-24. The question and eligibility criteria do not specify a historical cutoff, and the protocol describes no publication-date restriction. The entry-date ceiling therefore excludes potentially eligible later studies.",
          "recommendation": "Remove the ceiling or set it to the intended search date, then rerun the complete evaluation and report the resulting count and known-record retrieval.",
          "status": "open"
        },
        {
          "id": "F-R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The protocol rationale says records may identify PTSD symptoms through symptom measures or symptom wording without the full PTSD label, but the text-word block includes no specific measure names or abbreviations.",
          "recommendation": "Consider testing relevant instrument names and abbreviations, including PTSD Checklist/PCL and Impact of Event Scale/IES, then screen the added yield and known-record retrieval before deciding whether to retain them.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload budget is exceeded, but the only optional searched concept, symptom course, was tested. AND-ing it would lose a known eligible record, PMID 10221639, and the current development set has only 11 records.",
          "evidence": "The base query returns 32,510 records against a 10,000-record budget. The trajectory block reduces the count to 8,146 but loses PMID 10221639; its loss sample found 0 relevant records among 30."
        },
        {
          "issue_id": "I-af36a83285447cf63c9c",
          "status": "accepted-risk",
          "response": "The optional block remains out because it loses a known eligible record and the development set is below the stated 15-record threshold. Additional independent validation remains unavailable in this packet.",
          "evidence": "The packet reports 11 screened development records discovered from a focused pilot query, no user-supplied seeds, and known loss of PMID 10221639 when the trajectory block is applied."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "da49971d44ae82a479875c777fab42d489337c908b5594a0ef9a78585cb6240e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched PTSD and symptom concept includes its named variants, including pediatric medical traumatic stress. Traumatic-event exposure is explicitly assigned to screening, and the optional trajectory block remains uncombined."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD and symptom terms are ORed in one broad block. The trajectory block was tested and left out; AND-ing it would lose known eligible PMID 10221639."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Stress Disorders, Post-Traumatic[Mesh] is used, and the packet reports no MeSH translation or syntax diagnostics."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Added and tested the PTSD Checklist, specific PCL versions, and full Impact of Event Scale phrase. Tested IES[tiab] separately; its added yield was dominated by unrelated acronym matches, and a 30-record sample found no clearly eligible PTSD trajectory study, so the standalone acronym was excluded while the spelled-out scale phrase remains."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint, PubMed error, or warning diagnostics. The multiword terms use no proximity operators or wildcarded proximity expressions."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The search still applies an Entrez entry-date ceiling of 2016-01-24. The packet documents that the ceiling was applied, but the question and eligibility criteria give no historical cutoff rationale."
        }
      },
      "findings": [
        {
          "id": "F-R1-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits records to entry dates through 2016-01-24. The question and eligibility criteria specify no historical cutoff; documenting the ceiling as PSB_AS_OF does not establish that it matches the intended search scope.",
          "recommendation": "Remove the ceiling or set it to the intended search date, then rerun the complete evaluation and report the resulting count and known-record retrieval.",
          "status": "rejected",
          "response": "Rejected: the task instructions explicitly require running the search as of 2016-01-24 and keep PSB_AS_OF set for every command. The Entrez-date ceiling is mandatory for this run and is not a publication-date [dp] limit."
        },
        {
          "id": "F-R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The block now includes PTSD Checklist/PCL variants and Impact of Event Scale, but it does not include the IES abbreviation requested in the earlier recommendation.",
          "recommendation": "Test IES[tiab], screen its yield and known-record retrieval, and rerun the complete evaluation before deciding whether to retain it.",
          "status": "rejected",
          "response": "Rejected as a query change after direct testing: the standalone acronym is highly ambiguous. The full “Impact of Event Scale” phrase and instrument-specific PCL forms remain. The tested IES added-yield sample showed substantial unrelated matches and no clearly eligible record."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is documented as a limitation. The optional trajectory concept was tested, and AND-ing it would lose a known eligible record. The other nonsearched concept, traumatic-event exposure, is explicitly assigned to screening because event types are heterogeneous and PTSD terminology conveys trauma exposure.",
          "evidence": "The current base query returns 32,908 records against a 10,000-record budget. The trajectory block reduces the count to 8,283 but loses PMID 10221639; the refreshed loss sample found 0 relevant records among 30. The category probes and term additions are documented in the packet."
        },
        {
          "issue_id": "I-af36a83285447cf63c9c",
          "status": "accepted-risk",
          "response": "The trajectory block remains out because it loses a known eligible record and the development set is below the stated 15-record threshold. The packet documents a focused pilot search and screening, but independent validation remains unavailable.",
          "evidence": "The development set contains 11 records and there were no user-supplied seeds. The refreshed loss sample found 0 relevant records among 30, while the earlier sample identified eligible PMID 10221639 as lost by the trajectory block."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "da49971d44ae82a479875c777fab42d489337c908b5594a0ef9a78585cb6240e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searchable PTSD and symptom block covers the named variants, including pediatric medical traumatic stress. Traumatic-event exposure is assigned to screening, and the optional trajectory block remains uncombined."
        },
        "operators": {
          "verdict": "pass",
          "note": "PTSD and symptom terms are ORed in one broad block. The tested trajectory block remains optional because applying it loses known eligible PMID 10221639."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Stress Disorders, Post-Traumatic MeSH descriptor is included; no MeSH translation or syntax errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy now includes PTSD Checklist, specific PCL variants, and the full Impact of Event Scale phrase. The standalone IES abbreviation was tested and rejected because its added yield was ambiguous and a 30-record sample found no clearly eligible trajectory study."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint, PubMed error, or warning diagnostics are reported. The multiword terms use no proximity operators or wildcarded proximity expressions."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date ceiling remains, as the task instructions require the search to run as of 2016-01-24. It is an Entrez entry-date limit, not a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "F-R1-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query limits records to entry dates through 2016-01-24, while the question and eligibility criteria state no historical cutoff.",
          "recommendation": "Remove the ceiling or set it to the intended search date, then rerun the complete evaluation.",
          "status": "rejected",
          "response": "Rejected: the task instructions require running the search as of 2016-01-24 and keeping PSB_AS_OF set for every command. The ceiling implements that required search date."
        },
        {
          "id": "F-R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier recommendation to test PTSD Checklist/PCL and Impact of Event Scale terms was handled; the follow-up recommendation to test standalone IES was evaluated separately.",
          "recommendation": "Retain the tested instrument terms; include IES only if its added yield supports doing so.",
          "status": "rejected",
          "response": "The strategy retains PTSD Checklist, PCL-C, PCL-M, PCL-S, PCL-5, and the full Impact of Event Scale phrase. Standalone IES was tested and rejected because its added-yield sample contained substantial unrelated matches and no clearly eligible record."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning remains an accepted limitation. The optional trajectory concept was tested, and AND-ing it would lose a known eligible record. Traumatic-event exposure is assigned to screening because event types are heterogeneous.",
          "evidence": "The base query returns 32,908 records against a 10,000-record budget. The trajectory block reduces the count to 8,283 but loses PMID 10221639; the refreshed loss sample found 0 relevant records among 30. Two category probes and instrument term additions are documented."
        },
        {
          "issue_id": "I-af36a83285447cf63c9c",
          "status": "accepted-risk",
          "response": "The trajectory block remains out because it loses a known eligible record and the available development set is below the stated threshold. Independent validation remains unavailable.",
          "evidence": "The development set contains 11 records and there were no user-supplied seeds. The refreshed loss sample found 0 relevant records among 30, while the earlier sample identified eligible PMID 10221639 as lost by the trajectory block."
        }
      ]
    }
  ]
}
```


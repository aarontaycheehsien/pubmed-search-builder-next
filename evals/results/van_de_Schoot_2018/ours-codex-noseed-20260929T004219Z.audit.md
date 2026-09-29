# PubMed search strategy: audit

Generated 2026-09-29T01:03:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: Prognosis / symptom course
- Scope confirmed by user: no (User requested that the run proceed without questions. Assumption: the target is longitudinal PTSD symptom course following trauma, including cohorts and study arms where repeated symptoms are reported; trauma type and study design are screening criteria. No known relevant articles were supplied. No language or publication-date limits. Harness cutoff applied via PSB_AS_OF=2016-01-24 (Entrez date), not a publication-date limit. Scope was not user-confirmed. Trauma exposure was tested as an optional category because the base set exceeded budget. The block was left out after its loss sample contained eligible treatment-related symptom courses without a named event; category probes found eligible ICU follow-up and treatment/deployment records outside the tested event block, demonstrating unreliable event labeling.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder symptoms | search | The review concerns PTSD symptom trajectories; PTSD symptoms are the topic-defining condition and should be named or indexed. |
| Symptom trajectory or course over time | optional | Trajectory/course labels define the topic but may not be consistently present in titles, abstracts, or indexing; test the block before deciding whether to AND it. |
| Exposure to a traumatic event | screen | PTSD implies trauma exposure, while eligible repeated symptom courses may be reported without the precipitating event or under varied medical and treatment contexts. A broad event block lost eligible records in the tested samples, so screen trauma eligibility. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T01:02:50+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 32,346
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `PTSD[tiab]` | 15,732 | none |
| 3 | `posttraumatic[tiab] AND stress[tiab] AND disorder*[tiab]` | 19,537 | none |
| 4 | `post-traumatic[tiab] AND stress[tiab] AND disorder*[tiab]` | 7,604 | none |
| 5 | `post traumatic[tiab] AND stress[tiab] AND disorder*[tiab]` | 7,604 | none |
| 6 | `posttraumatic[tiab] AND stress[tiab] AND symptom*[tiab]` | 11,271 | none |
| 7 | `post-traumatic[tiab] AND stress[tiab] AND symptom*[tiab]` | 3,835 | none |
| 8 | `post traumatic[tiab] AND stress[tiab] AND symptom*[tiab]` | 3,835 | none |
| 9 | `posttraumatic stress[tiab]` | 14,174 | none |
| 10 | `post-traumatic stress[tiab]` | 8,160 | none |
| 11 | `post traumatic stress[tiab]` | 8,160 | none |
| 12 | `PTSS[tiab]` | 510 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 32,346 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR PTSD[tiab] OR (posttraumatic[tiab] AND stress[tiab] AND disorder*[tiab]) OR (post-traumatic[tiab] AND stress[tiab] AND disorder*[tiab]) OR (post traumatic[tiab] AND stress[tiab] AND disorder*[tiab]) OR (posttraumatic[tiab] AND stress[tiab] AND symptom*[tiab]) OR (post-traumatic[tiab] AND stress[tiab] AND symptom*[tiab]) OR (post traumatic[tiab] AND stress[tiab] AND symptom*[tiab]) OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR post traumatic stress[tiab] OR PTSS[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 6 | 6 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Symptom trajectory or course over time | left out | 32,346 / 11,398 | 64.8% | 9650067, 11343529, 20723987, 21457944 | 1/30 | The updated 30-record loss sample found PMID 9650067 with repeated PTSD symptom assessments and improvement over time despite no course/trajectory terms. Earlier samples also found eligible treatment and ICU records missing trajectory vocabulary. Leave the block out to protect recall. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 32,194 | initial | none | Initial PTSD condition block with broad trajectory/course candidate; terms drafted from the review question, MeSH authority lookup, and screened benchmark studies. |
| 2 | 32,194 | limits/combination | none | Added a broad optional trauma-event block to test the searchable exposure concept because the current query exceeds the screening budget. |
| 3 | 32,194 | limits/combination | none | Category probe found an eligible repeated PTSD symptom follow-up after critical illness; broadened the trauma-event member block and re-evaluated. |
| 4 | 32,194 | limits/combination | none | Screened second trauma category probe; retained eligible repeated symptom courses without a reliably named traumatic event in the development set and reclassified event exposure to screening. Removed the optional trauma candidate because it was empirically unreliable. |
| 5 | 32,346 | ptsd: +1 / -0 | none | Added the title/abstract acronym PTSS for post-traumatic stress symptoms after a count check returned 510 PubMed records; the acronym is a focused high-sensitivity variant of the explicit symptom wording. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5 (same-context critic; no fresh-context reviewer was available): 1 findings; scope-assumption-intervention-course document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 475 NCBI requests logged (155 from cache); strategy sha256 602c04647af5._

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
        "message": "32,346 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "32,346 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:02:50+00:00",
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
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR (\"posttraumatic\"[Title/Abstract] AND \"stress\"[Title/Abstract] AND \"disorder*\"[Title/Abstract]) OR (\"post-traumatic\"[Title/Abstract] AND \"stress\"[Title/Abstract] AND \"disorder*\"[Title/Abstract]) OR (\"post-traumatic\"[Title/Abstract] AND \"stress\"[Title/Abstract] AND \"disorder*\"[Title/Abstract]) OR (\"posttraumatic\"[Title/Abstract] AND \"stress\"[Title/Abstract] AND \"symptom*\"[Title/Abstract]) OR (\"post-traumatic\"[Title/Abstract] AND \"stress\"[Title/Abstract] AND \"symptom*\"[Title/Abstract]) OR (\"post-traumatic\"[Title/Abstract] AND \"stress\"[Title/Abstract] AND \"symptom*\"[Title/Abstract]) OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"PTSS\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "6e2e0a8b0855c104ccbd222b6e0d1e053095abff3bf864d75848b3348b9a84cc",
      "note": "same-context critic; no fresh-context reviewer was available",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required PTSD block reflects the topic; trajectory labels were tested as optional and left out after relevant losses. Trauma exposure and study design remain screening criteria based on the loss samples and probe evidence."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD synonyms are OR-combined within one block; no NOT operators or unnecessary AND blocks are used. The proximity phrase is confined to the optional candidate and had no translation warning."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Stress Disorders, Post-Traumatic is the verified MeSH descriptor D013313. It is exploded by default; no narrower headings were returned."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block covers PTSD, PTSS, posttraumatic/post-traumatic/space-separated forms, disorder and symptom variants. The PTSS acronym was count-checked."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly field-tagged; lint and live translations reported no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, or design filters are used. The Entrez-date bound is supplied by PSB_AS_OF for the harness cutoff."
        }
      },
      "findings": [
        {
          "id": "scope-assumption-intervention-course",
          "domain": "translation",
          "severity": "document",
          "kind": "scope",
          "block": "ptsd",
          "finding": "The wording could mean natural-history symptom trajectories only or could include treatment-arm symptom courses. The run assumed repeated PTSD symptom outcomes in both observational and interventional primary studies are eligible.",
          "recommendation": "Have the review team confirm this assumption during protocol and PRESS review; if treatment response is out of scope, revise eligibility and rerun the search and validation.",
          "status": "accepted-risk",
          "response": "The user explicitly asked the run to proceed without questions and authorized reasonable assumptions. This interpretation is recorded in protocol.json and preserves recall across repeated symptom courses; the human review team should confirm it before use."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The standard workload budget is exceeded. Both searchable, topic-defining candidates were tested: the trajectory block reduced results by 64.8% but lost four screened relevant records, and the trauma-event block lost eligible records and category probes identified further eligible courses outside event wording. No tested restriction can be AND-ed without documented recall loss; retain the recall-first PTSD block and flag the screening load for the review team.",
          "evidence": "Current live evaluation returned 32,346 records against the 10,000-record budget. The trajectory candidate would return 11,398 and loses PMIDs 9650067, 11343529, 20723987 and 21457944. The trauma candidate loss sample contained eligible PMID 26763497; category probes screened 30 records each and found eligible follow-up after critical illness and treatment/deployment symptom courses. All nine build-discovered relevant records and six benchmark records are retrieved by the current query."
        }
      ]
    }
  ]
}
```


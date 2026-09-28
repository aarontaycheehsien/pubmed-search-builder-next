# PubMed search strategy: audit

Generated 2026-09-28T03:20:35+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO
- Scope confirmed by user: no (User requested proceeding without clarification. Assumed intervention-effectiveness PICO. Anxiety-related scope is operationalized broadly around anxiety disorders; OCD and trauma-related conditions require screening for fit rather than being assumed eligible. Long-term follow-up, outcomes, comparators, and study design are screened, not AND-ed. No known relevant articles supplied; as-of bound is PubMed entry date, with no publication-date limit. The standard-depth discovery search identified prior reviews; selected included-study reports with confirmed CBT and >=6-month post-treatment follow-up were screened into a benchmark set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety-related disorders | search | Target condition/population; include recognized anxiety disorders and broad anxiety terminology to maintain recall. |
| Cognitive behavioral therapy | search | Intervention; central searchable treatment concept reliably named and indexed. |
| Long-term outcomes/follow-up | screen | Follow-up length and outcomes are inconsistently reported in titles, abstracts, and indexing. |
| Eligible study designs | screen | No design restriction is specified; assess eligibility during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T03:19:50+00:00
- Records added to PubMed up to: 2017-08-24
- Total records: 16,407
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Anxiety Disorders[Mesh]` | 75,155 | none |
| 2 | `Obsessive-Compulsive Disorder[Mesh]` | 14,139 | none |
| 3 | `Stress Disorders, Post-Traumatic[Mesh]` | 28,555 | none |
| 4 | `anxiety[tiab]` | 151,430 | none |
| 5 | `anxious[tiab]` | 14,019 | none |
| 6 | `anxiety disorder*[tiab]` | 24,830 | none |
| 7 | `anxiety-related[tiab]` | 3,987 | none |
| 8 | `anxiety related[tiab]` | 3,987 | none |
| 9 | `generalized anxiety[tiab]` | 5,844 | none |
| 10 | `generalised anxiety[tiab]` | 673 | none |
| 11 | `panic disorder*[tiab]` | 8,745 | none |
| 12 | `panic attack*[tiab]` | 3,419 | none |
| 13 | `agoraphobia[tiab]` | 2,865 | none |
| 14 | `social phobia[tiab]` | 3,620 | none |
| 15 | `social anxi*[tiab]` | 4,818 | none |
| 16 | `specific phobia*[tiab]` | 968 | none |
| 17 | `simple phobia*[tiab]` | 288 | none |
| 18 | `separation anxi*[tiab]` | 1,376 | none |
| 19 | `obsessive-compulsive disorder*[tiab]` | 11,295 | none |
| 20 | `obsessive compulsive disorder*[tiab]` | 11,295 | none |
| 21 | `OCD[tiab]` | 7,878 | none |
| 22 | `PTSD[tiab]` | 18,640 | none |
| 23 | `posttraumatic stress disorder*[tiab]` | 14,806 | none |
| 24 | `post-traumatic stress disorder*[tiab]` | 8,583 | none |
| 25 | `post traumatic stress disorder*[tiab]` | 8,583 | none |
| 26 | `stress disorder* post-traumatic[tiab]` | 39 | none |
| 27 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 232,134 | none |
| 28 | `Cognitive Behavioral Therapy[Mesh]` | 24,064 | none |
| 29 | `Behavior Therapy[Mesh]` | 66,990 | none |
| 30 | `cognitive behavio* therap*[tiab]` | 12,875 | none |
| 31 | `cognitive behavio* treatment*[tiab]` | 1,786 | none |
| 32 | `cognitive behavio* intervention*[tiab]` | 1,241 | none |
| 33 | `cognitive behavio* psychotherap*[tiab]` | 226 | none |
| 34 | `cognitive therap*[tiab]` | 2,812 | none |
| 35 | `cognitive psychotherap*[tiab]` | 117 | none |
| 36 | `CBT[tiab]` | 8,158 | none |
| 37 | `exposure-based CBT[tiab]` | 35 | none |
| 38 | `exposure based CBT[tiab]` | 35 | none |
| 39 | `cognitive restructuring[tiab]` | 736 | none |
| 40 | `exposure therap*[tiab]` | 1,294 | none |
| 41 | `"exposure and response prevention"[tiab]` | 274 | none |
| 42 | `exposure-response prevention[tiab]` | 36 | none |
| 43 | `response prevention[tiab]` | 503 | none |
| 44 | `#28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43` | 74,766 | none |
| 45 | `#27 AND #44` | 16,407 | none |

### Strategy (single line, for copying into PubMed)

```text
((Anxiety Disorders[Mesh] OR Obsessive-Compulsive Disorder[Mesh] OR Stress Disorders, Post-Traumatic[Mesh] OR anxiety[tiab] OR anxious[tiab] OR anxiety disorder*[tiab] OR anxiety-related[tiab] OR anxiety related[tiab] OR generalized anxiety[tiab] OR generalised anxiety[tiab] OR panic disorder*[tiab] OR panic attack*[tiab] OR agoraphobia[tiab] OR social phobia[tiab] OR social anxi*[tiab] OR specific phobia*[tiab] OR simple phobia*[tiab] OR separation anxi*[tiab] OR obsessive-compulsive disorder*[tiab] OR obsessive compulsive disorder*[tiab] OR OCD[tiab] OR PTSD[tiab] OR posttraumatic stress disorder*[tiab] OR post-traumatic stress disorder*[tiab] OR post traumatic stress disorder*[tiab] OR stress disorder* post-traumatic[tiab]) AND (Cognitive Behavioral Therapy[Mesh] OR Behavior Therapy[Mesh] OR cognitive behavio* therap*[tiab] OR cognitive behavio* treatment*[tiab] OR cognitive behavio* intervention*[tiab] OR cognitive behavio* psychotherap*[tiab] OR cognitive therap*[tiab] OR cognitive psychotherap*[tiab] OR CBT[tiab] OR exposure-based CBT[tiab] OR exposure based CBT[tiab] OR cognitive restructuring[tiab] OR exposure therap*[tiab] OR "exposure and response prevention"[tiab] OR exposure-response prevention[tiab] OR response prevention[tiab])) AND ("1800/01/01"[edat] : "2017/08/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety | 74,766 | 0 |
| cbt | 232,134 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 16,054 | initial | none | Initial two-block recall-first strategy; MeSH plus title/abstract language for anxiety-related disorders and CBT; long-term follow-up screened at >=6 months; review-cited trials used as benchmark only. |
| 2 | 0 | cbt: +4 / -0 | none | Addressed round-1 text-word finding by adding standalone exposure therapy and exposure/response prevention wording for clearly identified CBT variants; ERP acronym omitted as ambiguous. Re-evaluated against screened benchmark. |
| 3 | 16,407 | cbt: +4 / -0 | none | Revised exposure and response prevention as a quoted phrase after lint identified the lowercase Boolean word; retained exposure therapy and response prevention text terms. Complete re-evaluation. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; R1-TW-01 should-fix resolved
- Round 2 on version 3: 1 findings; R1-TW-01 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 473 NCBI requests logged (218 from cache); strategy sha256 47f16942dc56._

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
      "requested": "Anxiety Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:19:50+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001008",
          "name": "Anxiety Disorders",
          "type": "descriptor",
          "scope_note": "Persistent and disabling ANXIETY.",
          "tree_numbers": [
            "F03.080"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001008",
      "preferred_label": "Anxiety Disorders",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Anxiety Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Obsessive-Compulsive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:19:50+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009771",
          "name": "Obsessive-Compulsive Disorder",
          "type": "descriptor",
          "scope_note": "An anxiety disorder characterized by recurrent, persistent obsessions or compulsions. Obsessions are the intrusive ideas, thoughts, or images that are experienced as senseless or repugnant. Compulsions are repetitive and seemingly purposeful behavior which the individual generally recognizes as senseless and from which the individual does not derive pleasure although it may provide a release fr...",
          "tree_numbers": [
            "F03.080.600"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009771",
      "preferred_label": "Obsessive-Compulsive Disorder",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Obsessive-Compulsive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:19:50+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "Stress Disorders, Post-Traumatic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:19:50+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015928",
          "name": "Cognitive Behavioral Therapy",
          "type": "descriptor",
          "scope_note": "A directive form of psychotherapy based on the interpretation of situations (cognitive structure of experiences) that determine how an individual feels and behaves. It is based on the premise that cognition, the process of acquiring knowledge and forming beliefs, is a primary determinant of mood and behavior. The therapy uses behavioral and verbal techniques to identify and correct negative thi...",
          "tree_numbers": [
            "F04.754.137.350"
          ],
          "entry_terms": 29,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015928",
      "preferred_label": "Cognitive Behavioral Therapy",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "Cognitive Behavioral Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:19:50+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001521",
          "name": "Behavior Therapy",
          "type": "descriptor",
          "scope_note": "The application of modern theories of learning and conditioning in the treatment of behavior disorders.",
          "tree_numbers": [
            "F04.754.137"
          ],
          "entry_terms": 30,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001521",
      "preferred_label": "Behavior Therapy",
      "type": "descriptor",
      "location": "vocabulary:28",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"anxiety disorders\"[MeSH Terms] OR \"obsessive compulsive disorder\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"anxiety\"[Title/Abstract] OR \"anxious\"[Title/Abstract] OR \"anxiety disorder*\"[Title/Abstract] OR \"anxiety-related\"[Title/Abstract] OR \"anxiety-related\"[Title/Abstract] OR \"generalized anxiety\"[Title/Abstract] OR \"generalised anxiety\"[Title/Abstract] OR \"panic disorder*\"[Title/Abstract] OR \"panic attack*\"[Title/Abstract] OR \"agoraphobia\"[Title/Abstract] OR \"social phobia\"[Title/Abstract] OR \"social anxi*\"[Title/Abstract] OR \"specific phobia*\"[Title/Abstract] OR \"simple phobia*\"[Title/Abstract] OR \"separation anxi*\"[Title/Abstract] OR \"obsessive compulsive disorder*\"[Title/Abstract] OR \"obsessive compulsive disorder*\"[Title/Abstract] OR \"OCD\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"stress disorder* post traumatic\"[Title/Abstract]) AND (\"cognitive behavioral therapy\"[MeSH Terms] OR \"behavior therapy\"[MeSH Terms] OR \"cognitive behavio* therap*\"[Title/Abstract] OR \"cognitive behavio* treatment*\"[Title/Abstract] OR \"cognitive behavio* intervention*\"[Title/Abstract] OR \"cognitive behavio* psychotherap*\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"cognitive psychotherap*\"[Title/Abstract] OR \"CBT\"[Title/Abstract] OR \"exposure based cbt\"[Title/Abstract] OR \"exposure based cbt\"[Title/Abstract] OR \"cognitive restructuring\"[Title/Abstract] OR \"exposure therap*\"[Title/Abstract] OR \"exposure and response prevention\"[Title/Abstract] OR \"exposure response prevention\"[Title/Abstract] OR \"response prevention\"[Title/Abstract]) AND 1800/01/01:2017/08/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "f079c8b0095b7ca81ed8ddee6cd1d018cf2ca8dd6ed5b9ed3bcc1acaba2ed268",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues, and all eight benchmark records are retrieved. PubMed normalizes some hyphenated and unhyphenated variants to the same expression, creating redundancy but no identified loss of coverage."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searched concepts are combined with AND, and terms within each concept are combined with OR. Follow-up and study design remain screening criteria, consistent with the stated rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The anxiety, obsessive-compulsive, post-traumatic stress, cognitive behavioral therapy, and behavior therapy headings are reported as verified. The protocol flags OCD and trauma-related conditions for screening fit."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The CBT block includes exposure-based CBT only when CBT is named. Because eligibility includes clearly identified CBT variants, records naming exposure therapy or exposure and response prevention without the CBT label may be missed. Benchmark coverage does not rule out this gap."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax errors or warnings, and the query has a successful translation and result count."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date bound ends on 2017-08-24 and has no publication-date limit. Follow-up and study design are screened rather than used as search filters."
        }
      },
      "findings": [
        {
          "id": "R1-TW-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include clearly identified CBT variants, but exposure-based CBT is searched only as a phrase containing CBT. The strategy may miss eligible records that name exposure therapy or exposure and response prevention without calling the intervention CBT.",
          "recommendation": "Consider adding standalone title/abstract terms for exposure therapy and exposure and response prevention, including common abbreviations, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Added exposure therap* and exposure and response prevention wording to the CBT block and reran the full evaluation; PubMed accepted the clauses and the benchmark remained fully retrieved. The ERP acronym was omitted because it is ambiguous and the spelled-out phrase is covered."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "722240b9b5be24b971bcf2316d86254893566cf3c2f3f2c16135b3db08cc1125",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues. The tested query retrieves all eight benchmark records, and the anxiety and CBT blocks each retrieve all eight. PubMed normalizes some hyphenated variants to the same expression, which adds redundancy but shows no coverage loss."
        },
        "operators": {
          "verdict": "pass",
          "note": "The anxiety and CBT blocks use OR internally and are combined with AND. Follow-up duration, outcomes, and study design remain screening criteria, consistent with the stated rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the anxiety, obsessive-compulsive, post-traumatic stress, cognitive behavioral therapy, and behavior therapy headings as verified. OCD and trauma-related conditions are flagged for screening fit."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised CBT block includes standalone exposure therapy and exposure and response prevention wording, addressing the earlier concern about variants named without a CBT label. The eight benchmark records are all retrieved; the packet gives a reason for omitting the ambiguous ERP acronym."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax warnings or errors and provides a successful query translation and result count."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The query uses the 2017-08-24 entry-date bound and no publication-date limit. Follow-up and study design are screened rather than imposed as search filters."
        }
      },
      "findings": [
        {
          "id": "R1-TW-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include clearly identified CBT variants, but exposure-based CBT was searched only as a phrase containing CBT. The strategy could miss eligible records naming exposure therapy or exposure and response prevention without calling the intervention CBT.",
          "recommendation": "Add standalone title/abstract terms for exposure therapy and exposure and response prevention, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The revised CBT block adds exposure therap*, exposure and response prevention, exposure-response prevention, and response prevention wording. The complete evaluation reports no syntax or translation issues and retains all eight benchmark records. The packet states that ERP was omitted because it is ambiguous and the spelled-out phrase is covered."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```


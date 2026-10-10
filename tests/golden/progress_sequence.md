**PSB · Step 1/7 Intake · Request**
To build the search I need:
1. The review question in plain language
2. Known relevant articles (PMIDs, DOIs or PMCIDs), if any (optional). These help identify useful search terms and check whether the search retrieves studies it should find.
3. Depth: quick, standard (default) or thorough
   Screening means checking retrieved articles for relevance to help improve and test the search strategy. More screening allows more extensive testing and refinement.
   - quick: targeted discovery, up to ~30 retrieved articles checked for relevance; no automatic held-out test; 1 critic revision round, then a closing round; fastest
   - standard: prior reviews, pilot and citation searches, up to ~150 candidates screened; a held-out test is proposed when at least 10 eligible studies were screened privately; 2 critic revision rounds, then a closing round
   - thorough: as standard, up to ~400 candidates screened; 3 critic revision rounds, then a closing round; takes longest
4. Required limits, such as dates or languages, if any
5. Progress messages: standard (default) or verbose
   - standard: short messages at each step
   - verbose: up to three extra detail lines on search, MeSH, term-mining and evaluation messages (how records were found, headings returned, block coverage); it never changes what is searched, screened or kept private, and you can switch at any time
Reply "proceed" to use the defaults (standard depth, standard messages, no limits) for anything you leave out.

---

**PSB · Step 1/7 Intake · Summary**
Question: Which treatments reduce asthma attacks in children?
- Depth: standard
- Required limits: English (translation budget)
- Known articles recorded: none yet (added in Step 3)
- Progress messages: standard
- Assumptions and notes: none
- Workspace: <workspace>
Next: Step 2/7 Scope: split the question into concepts and decide which are searched, screened or optional.

---

**PSB · Step 2/7 Scope · Summary**
Question: Which treatments reduce asthma attacks in children?

| Concept | Role | Why |
|---|---|---|
| Asthma | Searched | condition, reliably indexed |
| Children | Searched | population named in abstracts |
| Exacerbations | Screened | outcomes are reported unevenly |

2 searched · 1 screened · 0 optional concepts
Limits (applied to the search): English (translation budget)

Eligibility criteria (applied at screening):
- Include: children with asthma
- Include: any intervention
- Exclude: case reports

Scope confirmed by the user.
Next: Step 3/7 Known records: screen seeds, look for prior reviews, run pilot and citation searches, screen up to ~150 candidates (standard), then choose the allocation (psb allocate).

---

**PSB · Step 3/7 Known records · Set updated**
Set seeds (development): 0 → 2 records
- Use: used for term mining, diagnosing misses and repeated development checks
- Origin: user-supplied
- Added: 1, 2

---

**PSB · Step 3/7 Known records · Similar articles + Citation search, backward**
Found 4 candidate records linked to 2 known records (set seeds)
- Similar articles: 3
- Reference lists (backward): 2
- Already in a known-record set: 0 (excluded)
- Shown for screening: 4 records as candidate batch C1
- Screening queue: 4 candidates found (4 similar articles + backward citations) · 0 screened · 4 waiting
- Screening budget (decisions in all contexts): 0 of ~150 used · ~150 left (standard)
- Why: studies screened in become the known records that check whether the final search finds what it should; some screened only in the separate context can be held out unseen for one final test.
- Next: screen the 4 waiting candidates.

---

**PSB · Step 3/7 Known records · Pilot search**
Pilot search: 3 records for `asthma*[tiab]`
- Shown for screening: 3 records as candidate batch C2
- Screening queue: 6 candidates found (4 similar articles + backward citations, 2 pilot search) · 0 screened · 6 waiting
- Screening budget (decisions in all contexts): 0 of ~150 used · ~150 left (standard)
- Next: screen the 6 waiting candidates.

---

**PSB · Step 3/7 Known records · Screening**
Screened 4 candidates: 2 include · 1 exclude · 1 uncertain
- Similar articles + backward citations from 2 records (set seeds) (C1): 4 screened → 2 include
- Included but not yet in a set: 5, 6
- Screening queue: 6 candidates found (4 similar articles + backward citations, 2 pilot search) · 4 screened · 2 waiting
- Screening budget (decisions in all contexts): 4 of ~150 used · ~146 left (standard)
- Next: screen the 2 waiting candidates.

---

**PSB · Step 3/7 Known records · Screening**
Screened 1 candidate: 1 include · 0 exclude · 0 uncertain
- Pilot search `asthma*[tiab]` (C2): 1 screened → 1 include
- Included but not yet in a set: 3, 5, 6
- Screening queue: 6 candidates found (4 similar articles + backward citations, 2 pilot search) · 5 screened · 1 waiting
- Screening budget (decisions in all contexts): 5 of ~150 used · ~145 left (standard)
- Next: screen the 1 waiting candidate.

---

**PSB · Step 3/7 Known records · Set updated**
Set relevant (development): 0 → 3 records
- Use: used for term mining, diagnosing misses and repeated development checks
- Added: 3, 5, 6

---

**PSB · Step 3/7 Known records · Allocation**
No holdout is proposed: fewer than 10 eligible units.
- Eligible pool: 5 units (5 records); all of it is used for development
- Unexposed units: 0 of 5
- Next: psb allocate freezes this allocation

---

**PSB · Step 3/7 Known records · Allocation frozen**
Frozen: 5 units (5 records) for development · 0 units (0 records) held out · no holdout proposed: fewer than 10 eligible units

---

**PSB · Step 3/7 Known records · Summary**
Known records: 5 for development · 0 held out · 0 on comparison lists
- relevant (development): 3 records — used for term mining, diagnosing misses and repeated development checks
- seeds (development): 2 records — used for term mining, diagnosing misses and repeated development checks
- Allocation: frozen: 5 units (5 records) for development · 0 units (0 records) held out · no holdout proposed: fewer than 10 eligible units
- Candidate searches: 2 (1 neighbour search, 1 pilot search)
- Screening: 5 screened → 3 include · 1 exclude · 1 uncertain (separate context 0 · builder 5)
- Screening queue: 6 candidates found (4 similar articles + backward citations, 2 pilot search) · 5 screened · 1 waiting
- Screening budget (decisions in all contexts): 5 of ~150 used · ~145 left (standard)
- Why: studies screened in become the known records that check whether the final search finds what it should; some screened only in the separate context can be held out unseen for one final test.
- Included after the allocation, not in a set: none
- In a development set with no include decision: 1, 2
Next: Step 4/7 Vocabulary: build MeSH and [tiab] terms for each searched concept.

---

**PSB · Step 4/7 Vocabulary · Summary**
2 searched concept blocks · 4 terms
- Asthma (asthma): 2 terms — 1 MeSH · 1 text-word · 0 other
- Children (child): 2 terms — 1 MeSH · 1 text-word · 0 other
- Concepts not searched: Exacerbations (screen)
- MeSH lookups: 0 · MeSH records inspected: 0
- Term mining from development records: not run
- Lint: 0 errors · 0 warnings
Next: Step 5/7 Develop & revise: check counts and development retrieval, and fix misses one change at a time.

---

**PSB · Step 5/7 Develop & revise · Evaluation v1**
v1: 5 records
- Change: first draft
- Known-record retrieval: development sets: relevant 3/3 (100.0%), seeds 2/2 (100.0%)
- Missed known records: none
- Checks: 0 blockers · 0 need critic review · lint 0 errors, 0 warnings

---

**PSB · Step 5/7 Develop & revise · Summary**
1 version evaluated: 5 → 5 records
- Latest: v1 — first draft
- Known-record retrieval: development sets: relevant 3/3 (100.0%), seeds 2/2 (100.0%)
- Missed known records: none
- Known records lost along the way and not recovered: none
- Checks: 0 blockers · 0 need critic review · lint 0 errors, 0 warnings
Next: Step 6/7 Critic: fresh-context PRESS-structured review, up to 2 revision round(s) then a closing round (standard).

---

**PSB · Step 6/7 Critic · Round 1 packet**
Round 1 (revision 1 of 2) packet written for v1
- Packet: critic/packet-1.md
- A fresh-context reviewer reads only this packet; its reply is saved as critic/round-1.json

---

**PSB · Step 6/7 Critic · Round 1 result**
Round 1 (revision): 6 domains pass · 0 revise
- Revise: none
- Findings: 0 must-fix · 0 should-fix · 1 document
- Status: 0 open · 0 resolved · 0 rejected · 1 accepted-risk
- Open must-fix: none
- Check: passes

---

**PSB · Step 6/7 Critic · Summary**
1 critic round: 1 revision · 0 closing
- Round 1 (revision) on v1: 1 finding — 0 must-fix · 0 should-fix · 1 document
- Findings by latest status: 0 open · 0 resolved · 0 rejected · 1 accepted-risk
- Overridden: none
- Latest round reviewed the latest evaluation: yes
Next: Step 7/7 Deliver: the held-out test when records are reserved (psb holdout-test), then live revalidation and the protected final query (psb report).

---

**PSB · Step 7/7 Deliver · Report**
Delivered: final query validated live, 5 records
- Known-record retrieval: development sets: relevant 3/3 (100.0%), seeds 2/2 (100.0%)
- Held-out test: No held-out test was performed.
- Critic: 1 round (internal PRESS-structured critique, not PRESS peer review); overridden findings: none
- Files: final-query.txt · audit.md · validation-manifest.json
- This is a draft. It needs PRESS peer review by an information specialist before use.

---

**PSB · Step 7/7 Deliver · Final search**
Delivered: 5 records; every line revalidated live

Search strategy (single line, for PubMed):
```text
("Asthma"[Mesh] OR asthma*[tiab]) AND ("Child"[Mesh] OR child*[tiab])
```

Line by line:

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Asthma"[Mesh]` | 3 | none |
| 2 | `asthma*[tiab]` | 3 | none |
| 3 | `#1 OR #2` | 5 | none |
| 4 | `"Child"[Mesh]` | 4 | none |
| 5 | `child*[tiab]` | 4 | none |
| 6 | `#4 OR #5` | 5 | none |
| 7 | `#3 AND #6` | 5 | none |

Known-record retrieval and the held-out test:

- **Allocation:** Development: 5 units (5 records); held-out test: none; no holdout was proposed: fewer than 10 eligible units.
- **Result:** No held-out test was performed.
- **Test material and separation:** No holdout was proposed: fewer than 10 eligible units.
- **Interpretation:** These records were available for developing or improving the search. Their retrieval is a development check, not independent validation. No held-out retrieval test was performed.
- **Size context:** Not applicable: no held-out test was performed.
- **Delivery and next step:** Not applicable: no held-out test was performed.

Development checks:

| Set | Purpose | In PubMed | Retrieved | Retrieved % | Records Retrieved |
|---|---|---:|---:|---:|---:|
| relevant | development | 3 | 3 | 100.0% | 5 |
| seeds | development | 2 | 2 | 100.0% | 5 |

- Critic: 1 round (internal PRESS-structured critique, not PRESS peer review); overridden findings: none
- Files: final-query.txt · audit.md · validation-manifest.json
- This is a draft. It needs PRESS peer review by an information specialist before use.

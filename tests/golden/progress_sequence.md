**PSB · Step 1/7 Intake · Request**
To build the search I need:
1. The review question in plain language
2. Known relevant articles (PMIDs, DOIs or PMCIDs), if you have any (optional)
3. Depth: quick, standard (default) or thorough
4. Required limits, such as dates or languages, if any
Reply "proceed" to use the defaults for anything you leave out.

---

**PSB · Step 1/7 Intake · Summary**
Question: Which treatments reduce asthma attacks in children?
- Depth: standard
- Required limits: English (translation budget)
- Known articles recorded: none yet (added in Step 3)
- Assumptions and notes: none
- Workspace: <workspace>
Next: Step 2/7 Scope: split the question into concepts and decide which are searched, screened or optional.

---

**PSB · Step 2/7 Scope · Summary**
2 searched · 1 screened · 0 optional concepts
- Asthma (asthma): search — condition, reliably indexed
- Children (child): search — population named in abstracts
- Exacerbations (outcome): screen — outcomes are reported unevenly
- Limits: English (translation budget)
- Eligibility criteria: 2 include · 1 exclude
Scope confirmed by the user.
Next: Step 3/7 Known records: add seeds, look for prior reviews, run pilot and citation searches, and screen up to ~150 candidates (standard).

---

**PSB · Step 3/7 Known records · Set updated**
Set seeds (seed): 0 → 2 records
- Use: user-supplied; used for development and term mining
- Added: 1, 2

---

**PSB · Step 3/7 Known records · Similar articles + Citation search, backward**
Found 4 candidate records linked to 2 known records (set seeds)
- Similar articles: 3
- Reference lists (backward): 2
- Already in a known-record set: 0 (excluded)
- Shown for screening: 4 records as candidate batch C1

---

**PSB · Step 3/7 Known records · Pilot search**
Pilot search: 3 records for `asthma*[tiab]`
- Shown for screening: 3 records as candidate batch C2

---

**PSB · Step 3/7 Known records · Screening**
Screened 4 candidates: 2 include · 1 exclude · 1 uncertain
- Similar articles + backward citations from 2 records (set seeds) (C1): 4 screened → 2 include
- Screening budget used: 4 of ~150 (standard)
- Included but not yet in a set: 5, 6

---

**PSB · Step 3/7 Known records · Screening**
Screened 1 candidate: 1 include · 0 exclude · 0 uncertain
- Pilot search `asthma*[tiab]` (C2): 1 screened → 1 include
- Screening budget used: 5 of ~150 (standard)
- Included but not yet in a set: 3, 5, 6

---

**PSB · Step 3/7 Known records · Set updated**
Set relevant (relevant): 0 → 3 records
- Use: screened in during the build; used for development and term mining
- Added: 3, 5, 6

---

**PSB · Step 3/7 Known records · Summary**
Known relevant records: 5 for development · 0 held out (validation and benchmark)
- seeds (seed): 2 records — user-supplied; used for development and term mining
- relevant (relevant): 3 records — screened in during the build; used for development and term mining
- Held-out validation set: none (development records: 5)
- Candidate searches: 2 (1 neighbour search, 1 pilot search)
- Screening: 5 screened → 3 include · 1 exclude · 1 uncertain
- Screening budget used: 5 of ~150 (standard)
- Included but not in a set: none
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
Next: Step 5/7 Test & revise: evaluate counts and recall, and fix misses one change at a time.

---

**PSB · Step 5/7 Test & revise · Evaluation v1**
v1: 5 records
- Change: first draft
- Recall: seeds 2/2 (100.0%) · relevant 3/3 (100.0%)
- Missed known records: none
- Checks: 0 blockers · 0 need critic review · lint 0 errors, 0 warnings

---

**PSB · Step 5/7 Test & revise · Summary**
1 version evaluated: 5 → 5 records
- Latest: v1 — first draft
- Recall: seeds 2/2 (100.0%) · relevant 3/3 (100.0%)
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
Next: Step 7/7 Deliver: live revalidation and the protected final query (psb report).

---

**PSB · Step 7/7 Deliver · Report**
Delivered: final query validated live, 5 records
- Recall: seeds 2/2 (100.0%) · relevant 3/3 (100.0%)
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

Recall against known relevant records:

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |
| seeds | seed (user-supplied known relevant records; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall, not sensitivity: development sets were used to build the strategy.

- Critic: 1 round (internal PRESS-structured critique, not PRESS peer review); overridden findings: none
- Files: final-query.txt · audit.md · validation-manifest.json
- This is a draft. It needs PRESS peer review by an information specialist before use.

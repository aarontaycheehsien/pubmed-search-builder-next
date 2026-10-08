# Known records: discovery, screening and allocation

Retrieval can only be checked against records already known to be relevant. What a number means
depends on whether the builder (you) could see those records while developing the search, so every
record has a purpose, and some are held out for one final test.

| Term | Meaning |
|---|---|
| Candidate records | Found by a discovery search; not yet assessed for eligibility |
| Eligible reference records | Screened as eligible for this question; together they form the allocation pool |
| Development set | Used for term mining, diagnosing misses and repeated retrieval checks |
| Held-out test set | Reserved and unseen by the builder; used for one retrieval test of the frozen query |
| Comparison list | Records outside the allocation pool whose eligibility or separation cannot be established under this workflow (legacy `validation`/`benchmark` sets, unscreened user lists): checked and reported separately, not mined, never a held-out test |

"Seeds" is an informal word for papers the user supplied. In reports say "held-out records", never
"held-out seeds" or "validation set".

**Origin** is recorded separately from purpose: `user-supplied`, `prior-review`, `pilot-search`,
`similar-articles`, `citation-backward`, `citation-forward`. Similar articles are ranked by text and
MeSH similarity; they are not a citation search. Origin never establishes independence: a prior
review's included studies can serve development or testing, and similar-article or pilot-search
records share vocabulary with development records or your own queries (the held-out message says so).

## Order

1. Fix eligibility in `protocol.json` (Step 2) **before** examining any supplied paper.
2. Discover candidates and screen them, recording every decision.
3. `psb allocate --preview`, relay its message, record the user's choice with `psb allocate`.
4. Only then add later discoveries to development, mine terms and evaluate (Steps 4–5).

Do not put eligible records into a set before the allocation: `psb eval` would feed their retrieval
back to you, which exposes them.

## Discovery by depth

- **quick**: screen the supplied papers. Targeted extra discovery is allowed, up to about 30 screened
  candidates. No automatic holdout and no choice message: `psb allocate` freezes everything for
  development, and only development retrieval is reported. Papers the user reserves as a test are
  never mined: ask once, "A held-out test is a standard-depth step. Switch to standard depth and keep
  these papers reserved, or use them for development?" If you cannot ask, switch to standard depth,
  keep them reserved, and record the assumption in `protocol.json` `notes`.
- **standard / thorough**: find candidates through prior reviews, two or three complementary precise
  queries, and similar-article and citation searches. Screen about 150 (standard) or 400 (thorough)
  candidates at most.

Tools:

1. **Prior reviews.** `psb sample --purpose prior-reviews "<precise topic query> AND systematic[sb]"`.
   A prior review's **included studies** come from its included-studies table or a supplement: record
   where (`--source-ref "Table 2 of PMID 123"`). A reference list (`psb neighbors <review PMID> --links refs`)
   supplies candidates only. `psb` cannot read full text: the table comes from the user or another tool,
   otherwise the records stay candidates to screen. A review of a parent topic is still worth mining
   for candidates.
2. **Precise pilots.** Two or three narrow queries with `psb sample --purpose pilot`.
3. **Neighbours.** `psb neighbors --set <set> --links similar,citedin --exclude-known`.

## The separate screening context

A held-out record must never have been shown to you. Discovery and screening shown in your own
context expose every record you look at (titles in `psb sample`, abstracts in `psb fetch`), so when
your host can start a fresh context (a subagent or a separate session), let it discover and screen:

- It runs `psb sample ... --screening` and `psb fetch ... --abstracts --screening`. These write to the
  private store (`screening/`), not your `records.jsonl`, and record no exposure.
- It records every decision with `psb screen --context separate --file decisions.json`, where each
  entry is `{pmid, decision, reason, group, origin, evidence, source_ref}`. Its reasons and sources
  stay in the private store until the held-out test.
- It replies with PMIDs, decisions, origins and groups only: never titles, abstracts or descriptions.

A prompt for it: "You screen candidate records for a PubMed search build. Read protocol.json for the
eligibility criteria. Use only `python <skill>/scripts/psb.py --workspace <run-dir> sample|fetch
--screening` to see records, and record each decision with `psb screen --context separate`, giving a
reason, the evidence basis (title, abstract or full-text), the origin, and a study key in `group`
shared by reports of the same study (a trial registration ID, or a short key you choose). Reply with
PMIDs, decisions and group keys only; never describe a record."

Do not read `screening/` yourself. With no separate context available, screen yourself: every record
is then exposed, no holdout is proposed, and the report says why.

## Screening rules

- Include only when the record clearly meets every criterion you can judge; mark uncertain records
  uncertain. Uncertain, ineligible, unresolved and not-in-PubMed-by-`as_of` records stay out of the
  pool.
- Record every decision, including excludes. The record feeds the progress messages and the
  allocation; it never adds a record to a set.
- **Study groups.** Reports of the same study share a `group` key and form one allocation unit. A
  record without a key is its own unit, and the study count is then unverified (the allocation message
  and the held-out result say so).

## Exposure

A study group is **exposed** if you have seen any member's title, abstract, indexing, full text,
search-relevant description, or retrieval feedback. `psb` records exposure automatically whenever one
of your commands shows content (`fetch`, `sample`, `terms rank`, `terms miss`, adding to a development
set). Declare anything else: `psb exposure declare <PMIDs> --kind abstract|description|... --note "..."`.
**Unknown exposure is exposure**: a record is unexposed only if every member was screened in the
separate context and nothing showed it to you. Handling a PMID alone (resolving it, a neighbour list,
a count) is not exposure.

Exposed groups go to development. Moving a seen record out of development cannot make it independent,
so `psb set split` is withdrawn.

## Allocation

Let N be the eligible units and U the unexposed units.

| Condition | Proposed allocation |
|---|---|
| N = 0 | No record-based retrieval check |
| N < 10 | All development |
| N ≥ 10, U = 0 | All development |
| N ≥ 10, U > 0 | Holdout H = min((3N + 5) // 10, U); development N − H |

The held-out units are the first H unexposed units ordered by `sha256("{seed}:{unit id}")` (seed 1 by
default; the unit id is its lowest PMID), so the draw is identical on every machine. Examples: 20
unexposed units give 14/6; 20 units with two unexposed give 18/2; 15 give 10/5; 8 give 8/0. The
ten-unit trigger and the 30% fraction are operational defaults, not adequacy thresholds; there is no
minimum of three.

1. `psb allocate --preview` shows counts only. When a holdout is proposed it renders the fixed
   choice message: relay it verbatim, once, before any mining.
2. Record the reply: `psb allocate --keep-holdout` or `--all-development`. Honour a choice the user
   already made without asking again. If they asked you not to wait for answers, use
   `--proceed-default` (it keeps the holdout) and record the assumption in `notes`.
3. When no holdout is proposed, do not ask: `psb allocate` freezes everything for development and the
   message says why.
4. **A test set the user designates** replaces the automatic holdout: have it screened in the separate
   context, then `psb allocate --reserve <PMIDs>`. Ineligible papers are removed and listed; any prior
   exposure is disclosed in the result. A designated set stays reserved even when small.

The allocation is frozen in `allocation.json` and never changes:

- Later discoveries go to development (`psb set add development ... --purpose development`), except a
  report of a reserved study (same group key): `set add` keeps it out, never mines it, and leaves the
  test's denominators unchanged; if you saw it, its study is recorded as exposed.
- Never redraw because of retrieval results. Accidental exposure is recorded, not repaired by
  replacing records.
- Changing eligibility or `as_of` after the freeze makes the allocation stale: have the separate
  context re-screen the reserved records against the new criteria, then `psb allocate --rebind`.
  Removals are disclosed; nothing is added.

Until the held-out test, reserved records are never shown, fetched, sampled, mined, diagnosed or listed
to you: `psb` refuses those commands, skips reserved rows in samples and neighbour lists, and refuses
queries that name a reserved PMID. The critic is told only how many units are reserved.

## Comparison lists

Records you cannot screen into the pool (a user's unscreened list, a legacy `validation` or
`benchmark` set) go on a comparison list: `psb set add <name> <PMIDs> --purpose comparison`. Their
retrieval is checked and reported separately with fixed wording; they are not mined unless you pass
`--include-comparison`; they are never a held-out test. Legacy role names (`seed`, `relevant`,
`validation`, `benchmark`) are still accepted by `set add --role` and mapped to a purpose.

## When you have nothing

With no seeds, no matching prior review, and nothing screened in, say so plainly: the fixed
no-records text applies and the audit states it. Ask the user whether they can supply known articles
or name a related review before you continue, unless this is a quick search without seeds or the
user asked you to proceed with documented assumptions. Run `psb allocate` anyway: it records that the
pool was empty.

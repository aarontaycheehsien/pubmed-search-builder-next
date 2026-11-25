# Known relevant records

Recall can only be measured against records you already know are relevant. How you found them
decides what the number means, so each set has a role.

| Role | What it is | Use for mining? | What its recall means |
|---|---|---|---|
| `seed` | articles the user supplied | yes | development check; not independent |
| `relevant` | records you screened in during the build | yes | development check; not independent |
| `validation` | relevant records held out from mining | no | semi-independent (it is still consulted every eval) |
| `benchmark` | included studies of a prior review, screened for your scope | no | external relative recall |

OpenAlex is a second source of the same kinds of record. It is used only to find candidates,
which are mapped back to PMIDs; works with no PMID are outside PubMed's denominator and are
listed, not scored.

`psb eval` reports recall for every set. Records not in PubMed (or added after `as_of`) are
excluded from the denominator and listed.

How a record was found matters as much as its role. A record found by one of your keyword
searches uses the words you searched, and so do its similar and citing articles: retrieving it
again proves nothing about relevant papers worded differently. Only records no keyword search
led to (user seeds, a review's reference list) can show that. `psb eval` counts them as
`known_without_keyword_search`, and gives a lower bound on recall only from those that were also
held out of the build. When there are none it says so: the recall figures then check your
wording and do not estimate recall. Report it that way.

A reference list counts the same whichever index holds it: `neighbors:refs` (PubMed) and
`openalex:refs` (OpenAlex) are both independent. Two further tiers are reported on their own:

| Tier | Route | In the recall bound? |
|---|---|---|
| Forward citations of independent records | `--links citedin` from records that are themselves independent | no: citing papers share a research community and its vocabulary, and favour highly cited work |
| Frame sample | `psb sample --source openalex --purpose frame` | its own estimate, within the frame only |

Citing records of a pilot hit stay keyword-dependent, as now.

## Seeds

- Resolve DOIs and PMCIDs with `psb resolve`; add PMIDs with `psb set add seeds ... --role seed`.
- Fetch them (`psb fetch --set seeds`) after the concept roles are set. If a seed looks outside
  the scope, ask the user whether to keep it; do not widen the scope to fit it.

## Finding more records (standard and thorough depth)

Budget: screen at most about 150 candidates at `standard` and 400 at `thorough`.

1. **Prior reviews.** Search for systematic reviews on the topic with
   `psb sample --purpose prior-reviews "<precise topic query> AND systematic[sb]"`. If one
   matches your scope, its included studies are the strongest benchmark.
   Get them from the user, the review's reference list (`psb neighbors <review PMID> --links refs`),
   or its tables, and screen each against your eligibility criteria. Save them as `benchmark`.
   A review of a broader or parent topic (forward switching, when you want switching back) is
   still worth mining for candidates: its included studies may report your topic as a subgroup.
   - This step is the only source of records that do not depend on your own wording when the
     user gave no seeds, so do not give up after one query. PubMed holds a reference list mostly
     for reviews that are in PMC: the sample marks them `in_pmc`, and `psb neighbors` says when a
     review has none. If the first review has no list, try the next; if no review matches the
     scope, use the reference lists of two or three reviews on overlapping or broader topics.
   - Run `--links refs` on its own, not together with `similar` or `citedin`, so the records it
     finds are logged as coming from a reference list.
   - PubMed has no list for most reviews outside PMC. `psb sample --purpose prior-reviews` reports
     `refs_openalex`, the references OpenAlex holds for each review; follow those with
     `psb neighbors <PMID or DOI> --links refs --source openalex`. A review with no list in either
     index has no deposited list, not no references: use its tables or ask the user.
   - `psb sample --source openalex --purpose prior-reviews "<topic words>"` searches OpenAlex for
     reviews, including those in education, social science and nursing venues outside PubMed.
     The review is found by keyword; its reference list is still independent.
   - One review's reference list gives a benchmark with that review's scope. When `psb eval`
     reports that one review supplies more than 60% of the records found through reference
     lists, add a second review that covers a different searched concept.
2. **Precise pilots.** Run two or three narrow, high-precision queries (the core concepts in
   titles, for example) with `psb sample --purpose pilot`, and screen what they return. Pilot
   hits are for mining vocabulary. They cannot validate the strategy or an optional block.
3. **Neighbours.** `psb neighbors --set seeds --links similar,citedin --exclude-known` ranks
   records linked to several known records first. Screen before use.
4. **Where the known set is thin** (`thorough`). `psb known profile` compares the OpenAlex
   topics and decades of the known set with a spread sample of the current result, and names
   topics and decades that hold a sizeable share of the result and no known record. Look for a
   review there. The profile is not evidence of recall; never report it as such.
5. **Frame sample** (`thorough`). `psb sample --source openalex --purpose frame --topic T... --n 50`
   draws a seeded random sample of PubMed records in one or two OpenAlex topics that cover the
   question. It does not show whether the strategy retrieves them, and you must not check before
   screening. Screen every record, add every include to a `validation` set
   (`--source "OpenAlex frame sample"`), and `psb eval` reports recall within the frame with a 95%
   bound. Adding only the misses, or only the hits, biases the estimate; `psb eval` says the
   estimate is incomplete while any sampled record is unscreened or any include is in no set.

## Screening candidates

Screen each candidate's title and abstract (`psb fetch <pmids> --abstracts`) against the
`eligibility` criteria in `protocol.json`:

- include only when the record clearly meets every criterion you can judge from the abstract;
- mark uncertain records uncertain and leave them out of every set;
- keep a short reason for each include (it goes in the set's `note` or your working notes).

Record every decision, including excludes and uncertain records:
`psb screen --include ... --exclude ... --uncertain ... --reason "..."`. For a reason per
record, pass `--file decisions.json`, a list of `{pmid, decision, reason}`. The record only feeds
the progress messages: the screening counts, the source of each candidate and the budget used.
It never adds a record to a set.

Add includes with `psb set add relevant ... --role relevant --source "similar articles of seeds"`.
Never add unscreened pilot hits or neighbours to a set: they are candidates, not evidence.

## Holding records out

When development records reach about 10 or more, run `psb set split seeds --fraction 0.3` (or on
`relevant`) before mining. Do not mine the `validation` set. If you later add terms because of
a validation miss, report that the set became part of development.

## When you have nothing

With no seeds, no matching prior review, and nothing screened in, say so plainly: the strategy is
empirically unvalidated, recall is not estimated, and the audit must state it. Ask the user
whether they can supply known articles or name a related review before you continue, unless
this is a quick search without seeds or the user asked you to proceed with documented
assumptions. Those cases may proceed without recall measurement; record that limitation.

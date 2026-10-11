# Experimental Step 5 semantic miss hunting

Use only when the user or evaluation condition enables it. This is one bounded discovery
batch before the critic and held-out test, followed by one repair round. It seeks eligible
counterexamples to a provisional query; it cannot estimate absolute recall. It does not
change Step 3 discovery or automatically edit the query.

## Run the batch

Reserve 30 candidates from the build's existing screening allowance during Step 3: up to 25
for semantic misses and five for the incremental repair sample.
The total remains about 30/150/400 for quick/standard/thorough, not that allowance plus 30.
Freeze the allocation, build the provisional strategy and run a successful current `psb eval`.
Configure `OPENALEX_API_KEY` in the environment or the skill's `.env` if required by the
provider. OpenAlex access, quota and billing are separate from NCBI.

Write `semantic-queries.json`: a JSON list of one to three distinct natural-language paragraphs,
each at most 2,000 characters. Base them on the fixed eligibility criteria: population/setting,
intervention intent, and an alternative description of the same eligible study. Prepare all
prompts before inspecting results. Do not copy Boolean terms, gold identities, reserved records
or evaluation miss diagnoses into these prompts.

```bash
python scripts/psb.py --workspace <run-dir> miss-hunt --queries <run-dir>/semantic-queries.json --limit 25
```

Optional `--limit 1..30` reduces the screening queue; `--per-query 1..50` reduces retrieval per
prompt. The queue is further capped at the remaining build budget (unique PMIDs with screening
decisions, consistent with existing progress accounting). Repeated decisions and full-text
checks are counted separately. These limits are experimental defaults, not an established optimum.

The command:

1. Saves the strategy, scope, allocation hash and effective cutoff in a private request.
2. Calls OpenAlex `search.semantic`, requesting only identifiers; archives responses with times
   and hashes under `screening/semantic-miss-hunt/`. Never read that private directory in the
   builder context: it can contain reserved identifiers.
3. Uses direct PMIDs or unambiguous DOI matches; unresolved records stay out. Prompts are
   interleaved by rank, duplicate PMIDs combined, and source ranks retained.
4. Removes reserved records and recognised reports of reserved studies before retrieval
   feedback; skips records already screened or in a known-record set.
5. Verifies remaining PMIDs against PubMed availability, using Create Date when `as_of` is set.
   Legacy Entry Date workspaces cannot run retrospective semantic discovery.
6. Tests membership in the complete provisional strategy, including limits. Only available
   candidates absent from that strategy enter the queue. API errors are failures, never misses.

The public `semantic-miss-hunt.json` contains the frozen query, strategy hash, prompts, response
hashes, filtering counts and queued PMID provenance. It shows no titles or abstracts; retrieve
only queued records through `psb fetch --abstracts`. Relay its progress message as usual.
One completed batch is allowed per workspace. `miss-hunt --summary` reports later outcomes.

Interrupted requests can be retried with identical arguments and unchanged scientific inputs;
completed responses and pending selections are reused. Finishing an interrupted batch does
not duplicate candidate or exposure events. Failed calls may consume quota. If a process was killed while
holding `.miss-hunt.lock`, verify it is no longer running before removing that lock. Never
delete the request/response archive to reset the experiment.

## Screen, diagnose, then repair

- Record every include/exclude/uncertain decision with `psb screen`, a reason, evidence,
  study group and `--origin semantic-search`. Discovery is not an eligibility decision.
- Resolve potentially eligible uncertain records with targeted full-text checking when the
  uncertainty could affect vocabulary analysis. Use another tool or user-provided full text;
  PSB cannot read it. Record `--evidence full-text` and a source reference. Unresolved uncertainty
  stays uncertain and does not enter development.
- Add confirmed eligible misses to development only with `psb set add ... --purpose development
  --origin semantic-search`. Never redraw, enlarge or release the holdout for this loop.
  Use the existing companion/exposure procedure when a new report belongs to a reserved study;
  never mine it. Recognition after exposure must be disclosed.
- Run `psb eval` and `psb terms miss`. Distinguish missing vocabulary, over-structuring,
  inappropriate limits and missing searchable information. Explain retained misses.
- Before adding a term, explain the generalisable eligible concept it represents. An isolated
  distinctive phrase is insufficient evidence. Never add PMID/DOI clauses to pass a check.
- Record decisions and measure justified changes using the commands below. The check samples
  `(revised strategy) NOT (frozen provisional strategy)` within the remaining allowance,
  excluding triggering, protected and previously screened records. Screen the returned sample
  with `psb screen`. This is development evidence, not independent validation.
- Finish the single repair round, then the ordinary critic and one-shot held-out test. No new
  discovery after that test. Zero confirmed misses does not establish complete recall.

Write `repair-decisions.json` with one entry per confirmed eligible miss. For example:

```json
{
  "decisions": [{
    "pmid": "12345678",
    "diagnosis": "vocabulary",
    "disposition": "repair",
    "general_concept": "The eligible concept shared across independent studies",
    "rationale": "Why this concept belongs in the strategy",
    "evidence": ["Reference to a scope note or independent terminology evidence"]
  }],
  "known_loss_rationale": "",
  "sampling_limitation": ""
}
```

The example PMID is a placeholder. Diagnoses are `vocabulary`, `structure`, `limit` or
`searchable-information`; dispositions are `repair` or `retain-miss`. Every entry needs
rationale and evidence references; vocabulary repairs also need `general_concept`.
Explain known records lost or an inability to screen any incremental material in the
corresponding fields. These explanations require critic judgement; their presence is not proof.

```bash
python scripts/psb.py --workspace <run-dir> miss-hunt --repair-decisions <run-dir>/repair-decisions.json
# Apply justified edits to strategy.json, then:
python scripts/psb.py --workspace <run-dir> miss-hunt --check-repair --sample-size 5
# Fetch and screen returned sample PMIDs, then run eval and the ordinary critic workflow.
```

Run `--check-repair` even when there are no confirmed misses; no decisions file is needed
in that case unless a sampling limitation or known loss needs explanation. It records baseline,
revised and incremental result counts, known losses and retrieval of confirmed misses.
Identical retries reuse the measurement and journal events. Recheck after changing the query,
scope or decisions. `--sample-size` accepts 0–10 and is capped at the remaining allowance.

New semantic receipts require a current repair check and completed queues before final review.
The screening command enforces the shared unique-candidate budget for semantic builds and
generated experiments; repeated decisions/full-text checks are accounted for separately.
The final validation manifest binds discovery, decisions, measurement and relevant screening
history. Later edits invalidate it. Legacy version-1 discovery receipts remain readable.

The audit includes discovery counts, uncertainty, screening/full-text decisions and confirmed
records actually added to development. Provider dollar cost is null unless separately measured;
never interpret it as zero. Whole-run driver accounting supplies token/time costs.

## Retrospective interpretation

Create Date verifies availability, not historical abstract or MeSH state. OpenAlex's current
embeddings/rankings are not an earlier snapshot either. No publication-date filter substitutes
for PubMed availability. Describe current retrieval over date-eligible records, retain responses
for replay, and never claim historical reconstruction.

Evaluate final external gold recall and retrieval cost; discoveries are diagnostic. Use the
strict unseen and common-unseen paired scores in `evals/README.md`. Gold identities remain
evaluator-only. Tune on development topics, and test Step 3 semantic discovery separately.

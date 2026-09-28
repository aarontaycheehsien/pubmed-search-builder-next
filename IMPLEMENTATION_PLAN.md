# Protected PubMed query delivery

## Contract

`psb report` (including the compatible `--fresh` spelling) performs a complete live evaluation,
requires a current critic at every depth, and publishes `final-query.txt`, `audit.md`, and
`validation-manifest.json` from one snapshot. Technical defects cannot be waived. An incomplete
check or unresolved mandatory review prevents publication. `report --diagnostic` is explicitly
unfinished output. The result remains a draft for human PRESS peer review.

## Implementation

1. Add shared syntax/token and validation utilities. Check nested expressions, combinations,
   limits, field aliases, truncation and proximity. Preserve full structured diagnostics and
   their source locations. Stop evaluation success on technical blockers.
2. Verify canonical MeSH descriptors, supplementary concepts and qualifiers, including
   descriptor/qualifier compatibility. Preserve authority evidence and distinguish absent
   records from service failures and valid zero-hit records. Never silently rewrite queries.
3. Classify phrase-index warnings separately from zero results. Require clause-specific
   translation review: rewrite, remove, or explicitly accept with evidence. Suggest tested
   proximity, explicit AND, or morphological variants. Explain that ~0 ignores order and
   wildcards cannot be used in proximity. Never infer redundancy from seed coverage alone.
4. Save evaluation attempts separately from strategy versions. Bind attempts and critic
   evidence to strategy, protocol, effective dates, sets, diagnostic state and vocabulary.
   Count/timestamp changes alone do not invalidate critique; interpretation or known-hit
   changes do. Carry finding IDs and dispositions across numerically ordered rounds.
5. Enforce fresh validation at the library boundary. Archive old outputs, stage new artifacts,
   recheck input fingerprints and publish the manifest last. Failed or interrupted attempts
   cannot leave a current protected query. Include effective as-of bounds in the tested export.
6. Update workflow references and harness consumers, then synchronize tested source changes
   to the installed skill. Preserve existing search-run data.

## Verification

Exercise technical defects in every query location, more than eight diagnostics, line-only
errors, canonical/invalid/ambiguous/unavailable vocabulary, qualifiers, phrase fallbacks and
accepted reviews, stale/malformed/missing critic evidence, translation drift with equal counts,
partial evaluation, malformed NCBI responses, publication interruption, and byte-for-byte
query/audit/manifest agreement. Run the full pytest suite and skill validator. Include an
opt-in live smoke test that makes no fixed result-count assertions.

## Defaults

Quick/standard/thorough allow 1/2/3 critic rounds. No technical override. Every substantive
warning requires a disposition; informational notices do not. Legacy evidence is readable but
must be refreshed. Accepted phrase risks are bound to the exact clause and translation and
never waive another technical failure.

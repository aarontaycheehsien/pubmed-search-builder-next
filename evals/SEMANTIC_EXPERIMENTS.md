# Semantic miss-hunting experiment status

## 2026-10-11: implementation and connectivity checks

Offline tests cover provider filtering, historical PubMed availability, protection of reserved
records, crash recovery, repair decisions and sampling, shared budgets, delivery binding,
matched-run metadata and checkpoint sealing. They do not measure a recall improvement.

Connectivity probes in the development environment:

- OpenAlex semantic search returned two identifier records without a configured API key for
  “School based food and nutrition education interventions to improve adolescent dietary
  intake in randomized or controlled trials.” The probe requested two results. This establishes
  connectivity only; it does not establish matching quality, eligibility or miss yield.
- PubMed availability lookup for PMID 31452104 succeeded. This was a separate connectivity
  probe, not an evaluation result.
- Codex CLI 0.159.2 reported a login, but a minimal `codex exec` request failed with HTTP 401
  and an authentication-refresh error. No review-topic model experiment completed.

Live model experiments were deferred at the user's direction. No treatment-effect estimate
or recommendation to enable semantic discovery by default follows from these checks.

## Next live experiment

Use the checkpoint commands in [README.md](README.md#experimental-step-5-semantic-miss-hunting)
after restoring model authentication. Begin with development topics, including the Medeiros
school-based food and nutrition topic, then several contrasting development topics. Repeat with
independent checkpoints and fixed model, effort, date and total screening budget.

Measure external gold recall, common-unseen recall and final retrieval volume first. Report
incremental eligible yield, uncertainty, screening/full-text decisions and driver costs as
diagnostics. Record failed and incomplete runs. Preserve response archives and evaluator
pairing receipts; do not use held-out-topic misses for refinement. Step 3 semantic discovery
and additional providers remain separate future experiments.

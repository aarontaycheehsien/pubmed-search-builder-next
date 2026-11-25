# Diversifying known records with OpenAlex: plan

Status: proposal, nothing implemented. Motivated by development topics only; no held-out
strategy, audit or miss was read.

## The problem

Recall is only as well measured as the known set is diverse. `docs/recall-precision-plan.md`
shows the known set, not the vocabulary tools, is now the main limit:

- The two van_de_Schoot_2018 records every run missed (20061839, 20836603) were never in any
  known set, so no diagnostic could point at them.
- `INDEPENDENT_ROUTES` is `{"resolve", "neighbors:refs"}`. Apart from user seeds, the only
  wording-independent source is a PubMed reference list, which PubMed holds mostly for reviews
  in PMC. Kwok_2020 had 0 independent records in every early run.
- Eight of eleven AND-for-workload decisions rested on 8 to 14 independent records, below the
  20 that `OPTIONAL_MIN_INDEPENDENT` asks for.
- Several runs flagged that a single review of a neighbouring topic gives a benchmark skewed
  towards that topic.

So "diversify" here means two things: more routes that do not share the strategy's words, and
more anchors, so that one review's scope does not define the benchmark.

## What OpenAlex adds that PubMed does not

| Gap in PubMed | OpenAlex source | Wording-independent? |
|---|---|---|
| Reference lists only for PMC reviews | `referenced_works` for any work whose publisher deposits references | yes |
| Prior reviews only in MEDLINE/PubMed | reviews in education, social science, economics, nursing venues; their references mapped back to PMIDs | yes (the references, not the review search) |
| `citedin` only from PMC full text | `cited_by` across the index | depends on the origin record (see tiers) |
| No subject classification other than MeSH | topics and keywords, assigned by a classifier | no: still text-based, but different text |

The independence argument for a reference list does not change with the database: the review
may be found by keyword, but its authors, not our words, chose its references.

## Independence tiers

Every known record keeps the earliest batch that showed it (`progress.attribution`). Add a tier
to each route and report them separately in `known_without_keyword_search`:

| Tier | Routes | In the recall lower bound? |
|---|---|---|
| A | user seeds; PubMed or OpenAlex reference lists of a review | yes, as now |
| B | OpenAlex citing or cited works of a tier-A record | no: reported on its own until evaluation shows it behaves like tier A |
| C | OpenAlex topic or keyword searches | no: treated like a pilot |
| keyword | pilots, `similar`, neighbours of pilot hits | no, as now |

Tier B is the honest compromise. Citation links do not use our words, but citation neighbours
share a research community and its vocabulary, and favour highly cited work (Hirt et al.,
2023). Pooling it into the bound before measuring that would repeat the first-version error in
`recall-precision-plan.md`, where 95 pilot-derived records reported no loss and the search lost
4 of 53 gold records.

## Changes, one commit each

1. **OpenAlex client in psb.** Standard library only, as now. Reuse the request, retry and
   `include_pulled` handling of `openalex-search-builder/scripts/oasb/api.py` by copying, not
   by a dependency. `OPENALEX_API_KEY` from the environment, every request logged and cached in
   the workspace like NCBI requests. Map works to PMIDs through `ids.pmid`, falling back to DOI
   via `idconv`. Works without a PMID are listed, not scored: they are outside PubMed's
   denominator, as records outside PubMed already are.
2. **OpenAlex reference lists.** `psb neighbors <PMID|DOI> --links refs --source openalex`,
   route `openalex:refs`, added to `INDEPENDENT_ROUTES`. Report references found, mapped to
   PMIDs, and not in PubMed. `psb sample --purpose prior-reviews` gains
   `refs: {pubmed: n, openalex: n}` in place of the `in_pmc` guess, so the agent picks reviews
   that have a usable list. Fall back to OpenAlex automatically when PubMed has none.
3. **Prior reviews outside PubMed.** `psb sample --purpose prior-reviews --source openalex`,
   restricted to review-type works or titles naming a systematic, scoping or meta-analytic
   review. Only the review is found by keyword; its included studies arrive by tier A.
4. **Anchor concentration.** In `psb eval`, break tier-A records down by anchor review. When
   one review supplies more than about 60% of them, say so in the reading and in the progress
   message, and suggest a second review that covers a different searched concept. Fold the
   skew warning several runs raised into `references/known-records.md`.
5. **Known-set profile.** `psb known profile`: OpenAlex topics, publication years, source types
   and publication types of the known set against a random sample of the current result
   (`psb sample --random`, mapped through OpenAlex). It flags topics with result mass and no
   known record, and years before a key term came into use. It tells the agent where to look;
   it is not evidence of recall, and the audit must not present it as such.
6. **Tier-B citation chasing.** `psb neighbors --source openalex --links citing,references
   --set benchmark`, ranked by how many anchors each candidate links to (co-citation and
   coupling counts), screened like every neighbour. Reported as its own line in `psb eval`.
7. **Frame sample (thorough depth only).** A random, seeded sample from an OpenAlex frame (the
   review's one or two OpenAlex topics, PMIDs only), screened **before** anyone checks whether
   the PubMed strategy retrieves it. That gives a recall estimate within the frame from a
   second index, in the spirit of relative recall (Sampson et al., 2006) and capture-recapture
   (Kastner et al., 2009). Sampling only the strategy's misses would be cheaper and is
   forbidden: it biases the estimate downwards and turns diagnosis into tuning.
8. **Reporting.** The audit names each route in TARCiS terms (backward or forward citation
   searching, OpenAlex as the citation index, date, seeds; Hirt et al., 2024) and the PRISMA-S
   citation-searching item draws on it.

Rules unchanged: discoveries never change eligibility (Rule 1); nothing enters a set
unscreened; no term mining from `validation` or `benchmark`.

## How to test, cheapest first

Following `evals/README.md` and the order in `recall-precision-plan.md`:

1. **Offline tests** with recorded OpenAlex responses: PMID mapping, missing references,
   pulled works, route attribution, tier separation in `psb eval`.
2. **Replay, development topics only, no agent.** For the prior reviews that earlier
   development runs found, count gold PMIDs reachable through PubMed refs against OpenAlex
   refs, and through tier B. Check whether 20061839 and 20836603 become reachable. This uses
   the answer key, so it bounds what the routes can recover; it is not an agent result. If
   OpenAlex refs add little over PubMed refs on these topics, stop here.
3. **Sonnet runs, development topics, three a side** against `main`. Primary measures:
   tier-A records per run, runs reaching 20, anchor concentration. Then recall, result size and
   screening used. For tier B, the share of its screened-in records that are gold against the
   same share for tier A: if they are close across topics, that is the case for pooling it.
4. **Held-out topics, once, three runs a side**, logged in `heldout-ledger.jsonl`, only for a
   change that survives step 3.

## Risks and limits

- **Reference coverage is uneven.** OpenAlex reference coverage differs from Web of Science and
  Scopus and varies by publisher (Culbert et al., 2025). A missing list must read as "no list",
  never as "no references".
- **Budget.** OpenAlex charges per request and keys have a daily limit; this session's key ran
  out during the citation checks for this plan. Cache everything, and estimate cost before
  tier-B and frame-sample runs.
- **More screening.** Reference lists contain background and methods papers. The 150 and 400
  candidate budgets in `known-records.md` stay; OpenAlex routes compete within them.
- **Still one database.** Diversifying the known set improves the estimate of PubMed recall. It
  does not replace searching other databases, registries and grey literature
  (Greenhalgh & Peacock, 2005, found much of their evidence by citation tracking and personal
  knowledge, not database searching).

## References

- Culbert, J. et al. (2025). Reference coverage analysis of OpenAlex compared to Web of Science
  and Scopus. *Scientometrics*. https://doi.org/10.1007/s11192-025-05293-3
- Greenhalgh, T., & Peacock, R. (2005). Effectiveness and efficiency of search methods in
  systematic reviews of complex evidence: audit of primary sources. *BMJ*, 331, 1064.
  https://doi.org/10.1136/bmj.38636.593461.68
- Hirt, J., Nordhausen, T., Appenzeller-Herzog, C., & Ewald, H. (2023). Citation tracking for
  systematic literature searching: a scoping review. *Research Synthesis Methods*.
  https://doi.org/10.1002/jrsm.1635
- Hirt, J. et al. (2024). Guidance on terminology, application, and reporting of citation
  searching: the TARCiS statement. *BMJ*. https://doi.org/10.1136/bmj-2023-078384
- Kastner, M. et al. (2009). The capture-mark-recapture technique can be used as a stopping
  rule when searching in systematic reviews. *Journal of Clinical Epidemiology*, 62(2),
  149-157. https://doi.org/10.1016/j.jclinepi.2008.06.001
- Sampson, M. et al. (2006). An alternative to the hand searching gold standard: validating
  methodological search filters using relative recall. *BMC Medical Research Methodology*, 6,
  33. https://doi.org/10.1186/1471-2288-6-33

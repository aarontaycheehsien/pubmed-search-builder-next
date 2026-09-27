# PubMed search strategy: audit

Generated 2026-09-27T10:11:06+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In people with suspected non-falciparum or Plasmodium vivax malaria, what is the diagnostic accuracy of rapid diagnostic tests in endemic countries?
- Framework: PIRD
- Scope confirmed by user: no (User asked to proceed without clarification; scope was not user-confirmed. No user-supplied seeds. A cutoff-limited PubMed search did not identify a matching prior systematic review. One record with explicit uncomplicated and severe malaria, P. vivax, RDT evaluation, and species-specific performance was screened into the relevant development set. Five other promising pilot records were left out because the abstracts did not establish uncomplicated malaria. Relative recall is not independent validation. No post-cutoff publication records were considered.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Malaria | search | The target diagnosis is malaria, reliably indexed or named; retaining broad malaria species coverage protects mixed and incompletely specified evaluations. |
| Rapid diagnostic test | search | The index test is required for every eligible record and is identified by RDT, rapid-test wording, relevant test-kit indexing, or antigen-test descriptions. |
| Non-falciparum or Plasmodium vivax malaria | screen | Species-specific performance may be in full text or mixed-species records; do not require species terms. |
| Suspected or confirmed uncomplicated malaria in endemic settings | screen | Severity, suspected status, and endemic location are not consistently named in searchable metadata. |
| Eligible reference standard and diagnostic performance | screen | Reference methods and accuracy outcomes are not reliably indexed or reported in titles and abstracts. |

## Search details (PRISMA-S)

- Database and platform: MEDLINE via PubMed (NCBI E-utilities)
- Date the final counts were run: 2026-09-27
- Records added to PubMed up to: 2013-06-09
- Total records: 6,099 (6,102 before limits)
- Limits and filters: `("1800/01/01"[Date - Publication] : "2013/06/09"[Date - Publication]) AND ("1800/01/01"[Date - Entry] : "2013/06/09"[Date - Entry])` (Required to emulate the requested 2013-06-09 search and exclude both later publications and records entered into PubMed after the cutoff.)

### Strategy (line by line)

| # | Search | Results |
|---:|---|---:|
| 1 | `"Malaria"[Mesh]` | 50,641 |
| 2 | `"Malaria, Vivax"[Mesh]` | 2,872 |
| 3 | `"Plasmodium vivax"[Mesh]` | 3,745 |
| 4 | `malaria[tiab]` | 55,839 |
| 5 | `plasmodium[tiab]` | 34,635 |
| 6 | `paludism[tiab]` | 72 |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 74,079 |
| 8 | `"Diagnostic Tests, Routine"[Mesh]` | 7,136 |
| 9 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 |
| 10 | `"Antigens, Protozoan"[Mesh]` | 12,579 |
| 11 | `"rapid diagnostic test"[tiab]` | 579 |
| 12 | `"rapid diagnostic tests"[tiab]` | 769 |
| 13 | `"rapid test"[tiab]` | 2,005 |
| 14 | `"rapid tests"[tiab]` | 891 |
| 15 | `RDT[tiab]` | 653 |
| 16 | `RDTs[tiab]` | 303 |
| 17 | `immunochromatograph*[tiab]` | 1,749 |
| 18 | `"antigen detection"[tiab]` | 3,135 |
| 19 | `"antigen test"[tiab]` | 1,412 |
| 20 | `"antigen tests"[tiab]` | 519 |
| 21 | `dipstick[tiab]` | 2,112 |
| 22 | `"rapid diagnostic"[tiab]` | 2,352 |
| 23 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 47,356 |
| 24 | `#7 AND #23` | 6,102 |
| 25 | `#24 AND ("1800/01/01"[Date - Publication] : "2013/06/09"[Date - Publication]) AND ("1800/01/01"[Date - Entry] : "2013/06/09"[Date - Entry])` | 6,099 |

### Strategy (single line, for copying into PubMed)

```text
(("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR malaria[tiab] OR plasmodium[tiab] OR paludism[tiab]) AND ("Diagnostic Tests, Routine"[Mesh] OR "Reagent Kits, Diagnostic"[Mesh] OR "Antigens, Protozoan"[Mesh] OR "rapid diagnostic test"[tiab] OR "rapid diagnostic tests"[tiab] OR "rapid test"[tiab] OR "rapid tests"[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR "antigen detection"[tiab] OR "antigen test"[tiab] OR "antigen tests"[tiab] OR dipstick[tiab] OR "rapid diagnostic"[tiab])) AND (("1800/01/01"[Date - Publication] : "2013/06/09"[Date - Publication]) AND ("1800/01/01"[Date - Entry] : "2013/06/09"[Date - Entry]))
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 47,356 | 0 |
| rdt | 74,079 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 114,437 | initial | none | Initial broad PIRD strategy from scope: one combined malaria rapid diagnostic test block; species, uncomplicated/suspected status, setting, and reference standard screened. Includes MeSH and free-text layers; no protocol filters. |
| 2 | 6,083 | malaria_rdt: +0 / -20; malaria: +6 / -0; rdt: +14 / -0 | none | Revised after version 1 ORed disease and test terms together and returned an overbroad result. Scope permits two required searchable PIRD elements: broad malaria AND broad RDT/test vocabulary; vivax/non-falciparum, uncomplicated/suspected status, setting, and reference standard remain screening criteria. |
| 3 | 6,080 | limits/combination | none | Added explicit publication-date limit through 2013-06-09 per harness; PubMed entry-date cutoff remains applied by protocol as_of. Ran objective vocabulary ranking on screened relevant records. |
| 4 | 6,099 | rdt: +1 / -0 | none | Added the mined phrase rapid diagnostic to the RDT text layer because it occurred in all six screened relevant abstracts and covers wording where the noun is omitted; kept accuracy/reference terms as screening concepts. |
| 5 | 6,099 | limits/combination | none | Made the requested historical cutoff explicit in the copyable strategy using publication date and PubMed entry date through 2013-06-09; protocol as_of also enforces the entry-date boundary during evaluation. |
| 6 | 6,099 | limits/combination | none | Strictly re-screened pilot candidates against the stated uncomplicated-malaria criterion; removed five records whose abstracts did not establish uncomplicated status. Retained PMID 23345297 because the title and abstract explicitly cover uncomplicated and severe malaria, P. vivax, RDTs, endemic Malaysia, and reference-confirmed species-specific performance. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5 (same-context critic: reviewed the packet in the build context because a fresh-context reviewer was unavailable under this run's execution rules.): 0 findings; 
- Round 2 on version 6 (same-context critic: re-reviewed the updated packet after strict abstract screening; a fresh-context reviewer was unavailable under this run's execution rules.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 421 NCBI requests logged (167 from cache); strategy sha256 08c480e1ac46._


## Rationale

- The PIRD strategy requires malaria and the rapid diagnostic test. Non-falciparum/P. vivax detail, uncomplicated/suspected status, endemic setting, reference method, and accuracy measures remain screening criteria because PubMed records may omit them from searchable metadata.
- The malaria block uses exploded `Malaria` MeSH, with explicit vivax headings and `[tiab]` variants for malaria, Plasmodium, and paludism. The vivax headings overlap with the exploded Malaria heading but help with species-specific indexing.
- The test block combines `[tiab]` variants for rapid diagnostic tests, rapid tests, RDT, immunochromatography, antigen testing, and dipsticks with legacy MeSH headings for routine diagnostic tests, diagnostic reagent kits, and protozoan antigens. Those MeSH headings are broad and were retained to favor recall. MeSH explosion is on by default. The current `Rapid Diagnostic Tests` MeSH heading was introduced in 2023 and `Point-of-Care Testing` in 2016, so neither was used for this historical 2013 strategy.
- The only limits are publication date and PubMed entry date through 2013-06-09, as requested. No language, study-design, age, geography, or severity filters were added.

## How known records were found

No user-supplied seeds were available. Cutoff-limited searches for systematic reviews found no review matching the vivax/non-falciparum question; a review restricted to uncomplicated *P. falciparum* malaria was out of scope and not used as a benchmark. A focused pilot returned 159 records. Thirty titles were screened from the pilot sample and 12 abstracts were fetched for closer screening. PMID 23345297 was retained as the one clearly relevant development record because it explicitly evaluates RDTs in uncomplicated and severe malaria, includes *P. vivax*, reports species-specific performance against PCR-confirmed infection, and was conducted in endemic Malaysia. Five other promising candidates were left out because their abstracts did not establish the uncomplicated population; the remaining fetched candidates were excluded or uncertain for other eligibility elements. No records were held out for validation. Relative recall was 100% against this single development record, which is not independent validation.

## Critic dispositions

Two rounds reviewed the draft in the same context because a fresh-context reviewer was unavailable under the run rules. Both rounds passed the six PRESS-structured domains with no findings. This is internal critique, not independent information-specialist PRESS peer review.

## Open risks for the peer reviewer

The final strategy retrieves 6,099 records under the historical date bounds, so screening burden may be substantial. The legacy test MeSH headings are nonspecific and retained for recall; they may add non-RDT diagnostic studies. The development set has one record discovered from the pilot and there is no held-out or review-derived benchmark, so the strategy has not been independently validated. Check the full text of PMID 23345297 to confirm which species/severity strata contribute the reported accuracy results and whether it meets the intended reference-standard criteria. PRESS peer review by an information specialist remains pending.

# Frozen PubMed fixtures

This directory contains ten runnable fixtures. Gold sets include only included records that resolve to PubMed PMIDs. The five social and behavioural topics draw from published reviews; the five medical topics use included-record labels in the public SYNERGY data. The Cohen subsets come from one screening collection, rather than five independent reviews.

| Fixture | Topic | Gold PMIDs | Provenance and coverage |
|---|---|---:|---|
| `housing-first-criminal-justice` | Housing policy / criminal justice | 5 | All five included records in the review table resolved to PubMed. Search cutoff: July 2018. |
| `social-prescribing-older-adults` | Community services / ageing | 10 | Ten of twelve included articles resolved to PubMed; the remaining two did not have exact PubMed title matches. |
| `work-directed-return-to-work` | Labour / occupational policy | 11 | All eleven included articles (eight RCTs) resolved to PubMed. |
| `school-restorative-practice` | Education / school climate | 6 | PubMed-indexed subset of the review's 34 included-study table entries. |
| `healthcare-nudging` | Behavioural science / healthcare | 86 | Exact-title PubMed matches among 101 SYNERGY records labelled included; 15 unmatched titles are omitted. |
| `Cohen_2006_ADHD` | ADHD pharmacotherapy | 20 | Cohen SYNERGY subset; all included rows have unique PubMed IDs. |
| `Cohen_2006_UrinaryIncontinence` | Urinary-incontinence treatment | 40 | Cohen SYNERGY subset; all included rows have unique PubMed IDs. |
| `Cohen_2006_Antihistamines` | Antihistamine pharmacotherapy | 16 | Cohen SYNERGY subset; all included rows have unique PubMed IDs. |
| `Cohen_2006_Estrogens` | Estrogen pharmacotherapy | 80 | Cohen SYNERGY subset; all included rows have unique PubMed IDs. |
| `Cohen_2006_ACEInhibitors` | ACE-inhibitor pharmacotherapy | 41 | Cohen SYNERGY subset; all included rows have unique PubMed IDs. |

Each JSON fixture records its question, eligibility criteria, source provenance, three deterministic seeds, and gold PMIDs. When a review's exact search date was unavailable, `as_of` uses the day after the latest PubMed Entrez date in its gold set, as allowed by the evaluation schema. The SYNERGY topic questions are plain-language frames inferred from subset labels; their answer keys use only rows labelled `label_included=1`.

The candidate PMID sets were checked for duplicates within the new fixtures and against all existing fixture gold sets. No overlaps were found.

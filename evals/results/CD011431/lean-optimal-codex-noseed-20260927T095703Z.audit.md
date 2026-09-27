# PubMed strategy build log

## Scope and assumptions

- Review question: accuracy of malaria rapid diagnostic tests (RDTs) in suspected or confirmed uncomplicated non-falciparum / *Plasmodium vivax* malaria in endemic settings.
- No known relevant seed PMIDs were provided. No seed validation was possible.
- The search uses two essential blocks: malaria/species and rapid test/device. It does not require an accuracy term, reference-standard term, endemic-setting term, or study-design term. These are screening criteria; adding them would risk missing eligible diagnostic studies.
- The disease block is deliberately broad and includes malaria generally, because eligible studies may report species-specific results within mixed-species or all-malaria cohorts. This will retrieve falciparum-only work as noise. No `NOT falciparum` exclusion is used.
- The only limit is Publication Date through 2013-06-09, as requested. No language, age, geography, or publication-type limits were added.
- The CLI consulted the current NCBI MeSH service. MeSH records introduced after 2013 were excluded from the query. No post-2013 publications were intentionally used as evidence.

## Final PubMed query

The identical one-line query is saved in `final_strategy.txt`.

```text
("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR "Malaria"[tiab] OR "Infections, Plasmodium"[tiab] OR "Infection, Plasmodium"[tiab] OR "Plasmodium Infection"[tiab] OR "Plasmodium Infections"[tiab] OR "Paludism"[tiab] OR "Remittent Fever"[tiab] OR "Fever, Remittent"[tiab] OR "Marsh Fever"[tiab] OR "Fever, Marsh"[tiab] OR "Malaria, Vivax"[tiab] OR "Vivax Malaria"[tiab] OR "Plasmodium vivax Malaria"[tiab] OR "Malaria, Plasmodium vivax"[tiab] OR "Plasmodium vivax"[tiab] OR "Plasmodium vivaxs"[tiab] OR "vivax, Plasmodium"[tiab] OR "vivax"[tiab] OR "P. vivax"[tiab] OR "P vivax"[tiab] OR "non-falciparum"[tiab] OR "non falciparum"[tiab] OR "nonfalciparum"[tiab] OR "Plasmodium ovale"[tiab] OR "P. ovale"[tiab] OR "Plasmodium malariae"[tiab] OR "P. malariae"[tiab] OR "ovale"[tiab] OR "malariae"[tiab]) AND ("Reagent Kits, Diagnostic"[Mesh] OR "Reagent Kits, Diagnostic"[tiab] OR "Kits, Diagnostic Reagent"[tiab] OR "Diagnostic Reagent Kit"[tiab] OR "Kit, Diagnostic Reagent"[tiab] OR "Reagent Kit, Diagnostic"[tiab] OR "Diagnostic Reagent Kits"[tiab] OR "Diagnostic Test Kits"[tiab] OR "Diagnostic Test Kit"[tiab] OR "Kit, Diagnostic Test"[tiab] OR "Kits, Diagnostic Test"[tiab] OR "Test Kit, Diagnostic"[tiab] OR "Test Kits, Diagnostic"[tiab] OR "Diagnostic Reagents and Test Kits"[tiab] OR "In Vitro Diagnostic Devices"[tiab] OR "In Vitro Diagnostic Device"[tiab] OR "In Vitro Diagnostic Medical Device"[tiab] OR "In Vitro Diagnostic Medical Devices"[tiab] OR "rapid diagnostic test"[tiab] OR "rapid diagnostic tests"[tiab] OR "rapid test"[tiab] OR "rapid tests"[tiab] OR "rapid malaria test"[tiab] OR "rapid malaria tests"[tiab] OR "rapid card"[tiab] OR "rapid cards"[tiab] OR "RDT"[tiab] OR "RDTs"[tiab] OR "ICT"[tiab] OR "ICTs"[tiab] OR "immunochromatographic test"[tiab] OR "immunochromatographic tests"[tiab] OR "lateral flow"[tiab] OR "lateral-flow"[tiab] OR "lateral flow assay"[tiab] OR "lateral flow assays"[tiab] OR "test strip"[tiab] OR "test strips"[tiab] OR "bedside test"[tiab] OR "bedside tests"[tiab] OR "point of care"[tiab] OR "point-of-care"[tiab] OR immunochromatograph*[tiab] OR dipstick*[tiab] OR (rapid[tiab] AND (diagnos*[tiab] OR test*[tiab] OR detect*[tiab]))) AND ("1900/01/01"[Date - Publication] : "2013/06/09"[Date - Publication])
```

## MeSH work

### Disease and species block

- Lookups covered `malaria`, `malaria, vivax`, `Plasmodium vivax`, `non-falciparum malaria`, `Plasmodium infection`, and `Malaria, falciparum`.
- Included headings: `Malaria` (D008288), `Malaria, Vivax` (D016780), and `Plasmodium vivax` (D010966). The CLI records show `Malaria, Vivax` introduced in 1992; the malaria descriptor covers the human Plasmodium disease family and its tree includes Vivax, Falciparum, cerebral, avian, and blackwater-fever children. The Vivax heading and species heading add explicit coverage for this review's target.
- Entry terms from the included disease headings were added to `[tiab]`: Malaria; Plasmodium Infection(s); Infection(s), Plasmodium; Paludism; Remittent Fever / Fever, Remittent; Marsh Fever / Fever, Marsh; Malaria, Vivax; Vivax Malaria; Plasmodium vivax Malaria; Malaria, Plasmodium vivax; Plasmodium vivax; Plasmodium vivaxs; vivax, Plasmodium.
- `non-falciparum malaria` had no dedicated descriptor. The species and non-falciparum terms are included as text words. Falciparum is not excluded because mixed-species and all-malaria diagnostic studies may contain usable non-falciparum results.

### Test block

- Lookups covered rapid diagnostic test(s), diagnostic test kits, immunochromatographic test/assay, immunochromatography, lateral-flow assay, dipstick, strip test, point-of-care testing, ICT/RDT malaria, and diagnostic test.
- Included heading: `Reagent Kits, Diagnostic` (D011933; introduced 1978), exploded `[Mesh]`. Its narrower tree includes `Reagent Strips` (D011934), so the latter is retrieved by explosion. The descriptor's complete entry terms were added as `[tiab]`: Reagent Kits, Diagnostic; Kits, Diagnostic Reagent; Diagnostic Reagent Kit(s); Kit(s), Diagnostic Reagent; Reagent Kit(s), Diagnostic; Diagnostic Test Kit(s); Kit(s), Diagnostic Test; Test Kit(s), Diagnostic; Diagnostic Reagents and Test Kits; In Vitro Diagnostic Device(s); In Vitro Diagnostic Medical Device(s).
- `Rapid Diagnostic Tests` was found but excluded: NLM gives it a 2023 introduction year. `Point-of-Care Testing` was inspected and excluded because its introduction year is 2016. Neither belongs in a 2013-era strategy.
- `Immunoassay` (D007118; introduced 1967) was inspected. It has entry terms for immunochromatographic assays, but the heading covers many non-rapid tests and was not added as a MeSH heading. Relevant immunochromatographic terms are covered in `[tiab]` instead.
- Routine diagnostic tests and diagnostic test approval were rejected as out of scope. No relevant Supplementary Concept Records were identified for the disease or device concepts.

## PubMed CLI checks

All searches below included the publication date range shown in the final strategy; counts are NCBI CLI responses, not estimates.

| Check | Count |
|---|---:|
| Malaria block | 81,032 |
| Rapid-test text cluster | 173,388 |
| `Reagent Kits, Diagnostic` MeSH alone | 17,202 |
| Test block | 186,574 |
| First combined draft | 1,983 |
| Revised combined query | 1,903 |
| `Malaria` MeSH alone | 50,908 |
| `Malaria, Vivax` MeSH alone | 2,905 |
| `rapid[tiab] AND diagnos*[tiab] AND malaria[tiab]` | 1,151 |
| `immunochromatograph*[tiab] AND malaria[tiab]` | 152 |

PubMed's query translations were reviewed after each search. The combined query translated the explicit headings to MeSH Terms and the text terms to Title/Abstract. No useful additional concept heading was discovered via translation.

The final-query sample included PMID 24809203, “[Field evaluation of SD(BIOLINE) malaria antigen Plasmodium falciparum/Plasmodium vivax rapid test kit],” a 2013 record describing febrile patients at the China–Myanmar border, microscopy as reference, and sensitivity/specificity. It is a strong face-valid sample for the search. Other retrieved samples illustrate expected screening noise, including imported P. ovale case reports and falciparum treatment-monitoring studies.

### Tool limitation

The CLI's ESearch result IDs were not fully consistent with its fetch output: some result IDs could not be fetched, and at least one fetched record had publication year 2014 despite the query date range ending 2013-06-09. I therefore treat the reported counts and sample IDs as diagnostic checks, not certified date-limited yield. The query itself retains the requested date syntax; verify the date-limited result set directly in PubMed before screening and resolve the index-date discrepancy.

## Rationale and remaining caveats

- Disease plus rapid-test concepts keep the strategy sensitive. An accuracy, reference-standard, uncomplicated-disease, or endemic-country block could remove eligible papers whose abstracts omit those details.
- The search may retrieve falciparum-only studies, routine diagnostic kits, serology, or non-rapid tests. Screen for suspected/confirmed uncomplicated non-falciparum or vivax disease, actual RDT evaluation, accuracy against an eligible standard, and endemic setting.
- Because no seed records were supplied, there is no seed validation or empirical recall estimate.
- No post-2013 citation was used. A human information specialist should peer review this draft before it is treated as final; the skill's cited PRESS publication is from 2016 and was therefore not used under the requested cutoff.

## Reporting

- Database: PubMed
- Search date under the requested historical frame: 2013-06-09
- Limits: Publication Date 1900-01-01 through 2013-06-09
- Language, study design, age, and geography limits: none
- Strategy status: draft, requires human information-specialist review

from conftest import FakePubMed, record

from psb import terms
from psb.strategy import Strategy

STRATEGY = Strategy.from_dict({"blocks": [{"id": "c", "name": "", "terms": [
    '"Vesico-Ureteral Reflux"[Mesh]', "urinary tract infection*[tiab]", "UTI[tiab] OR UTIs[tiab]"]}]})


def test_coverage_is_truncation_and_hyphen_aware():
    memo = {}
    assert terms.covered("urinary tract infections", "tiab", STRATEGY, memo)
    assert terms.covered("urinary-tract infection", "tiab", STRATEGY, memo)
    assert terms.covered("UTIs", "tiab", STRATEGY, memo)
    assert not terms.covered("urinary infection", "tiab", STRATEGY, memo)
    assert terms.covered("Vesico-Ureteral Reflux", "mesh", STRATEGY, memo)
    assert not terms.covered("Child", "mesh", STRATEGY, memo)


def test_noise_filters():
    assert terms.noise_reason("Humans", "mesh") == "non_topical"
    assert terms.noise_reason("results", "tiab") == "section_label"
    assert terms.noise_reason("95 ci", "tiab") == "statistical"
    assert terms.noise_reason("IL-6", "tiab") is None


RECORDS = [
    record("1", "Renal scarring after febrile urinary tract infection", "DMSA scintigraphy detects renal scarring.",
           ["Humans", "Vesico-Ureteral Reflux", "Radionuclide Imaging"]),
    record("2", "Renal scarring in children", "Voiding cystourethrography and DMSA scintigraphy compared.",
           ["Humans", "Radionuclide Imaging"]),
    record("3", "Unrelated title", "Nothing shared here at all.", ["Humans"]),
]


def test_rank_scores_uncovered_terms_with_lift():
    pm = FakePubMed({'"renal scarring"[tiab]': {str(i) for i in range(10)}, "DMSA[tiab]": {"1", "2"},
                     '"Radionuclide Imaging"[Mesh]': {"1", "2", "3"}})
    result = terms.rank(pm, RECORDS, STRATEGY, fields=["tiab", "mesh"], budget=10)
    scored = {r["term"].lower(): r for r in result["scored"]}
    assert "renal scarring" in scored and scored["renal scarring"]["df"] == 2
    assert scored["renal scarring"]["lift"] is not None
    assert "humans" not in scored  # non-topical check tag
    assert all(not r["in_strategy"] for r in result["scored"])
    assert "urinary tract infection" not in scored  # already covered


def test_miss_report_lists_missing_vocabulary():
    evaluation = {"misses": [{"pmid": "2", "failing_blocks": ["c"], "lost_to_limits": False, "sets": ["seeds"]}]}
    [row] = terms.miss_report([RECORDS[1]], evaluation, STRATEGY)
    assert row["failing_blocks"] == ["c"]
    assert "Radionuclide Imaging" in row["mesh_not_in_strategy"] and "Humans" not in row["mesh_not_in_strategy"]
    assert any("dmsa scintigraphy" == t for t in row["text_not_in_strategy"])


def test_generic_terms_rank_after_distinctive_ones():
    pm = FakePubMed({})
    pm.count = lambda query: 3_000_000 if "scintigraphy" in query else 2
    result = terms.rank(pm, RECORDS, STRATEGY, fields=["tiab"], budget=40)
    order = [r["term"].lower() for r in result["scored"]]
    assert order.index("renal scarring") < order.index("scintigraphy")
    assert next(r for r in result["scored"] if r["term"].lower() == "scintigraphy")["generic"]


# -- why a block missed a record: wording taken from missed dev-topic records ---------------------

DIAGNOSIS = Strategy.from_dict({"blocks": [
    {"id": "virus", "name": "", "terms": ['"Viruses"[Mesh]', "virus*[tiab]", "viral[tiab]"]},
    {"id": "sequencing", "name": "", "terms": ['"Metagenomics"[Mesh]', "metagenom*[tiab]",
                                              '"high throughput sequencing"[tiab]']},
    {"id": "cbt", "name": "", "terms": ["cognitive behavio* therap*[tiab]", '"exposure therapy"[tiab:~1]']},
]})


def diagnose(rec, block):
    evaluation = {"misses": [{"pmid": rec["pmid"], "failing_blocks": [block]}]}
    [row] = terms.miss_report([rec], evaluation, DIAGNOSIS)
    [found] = row["diagnosis"]
    return row, found


def test_word_inside_a_longer_word_is_named_as_the_cause():
    rec = record("1", "Genome characterization of a porcine rotavirus B strain",
                 "Metagenomic sequencing revealed rotavirus B in feces from diseased piglets.")
    row, found = diagnose(rec, "virus")
    assert found["cause"] == "embedded_stem"
    assert found["embedded_stems"] == [{"term": "virus*[tiab]", "inside": ["rotavirus"]}]
    assert row["has_mesh"] is False  # not indexed: the MeSH layer could not have retrieved it either


def test_phrase_split_by_another_word_suggests_proximity():
    rec = record("2", "Genome characterization of a novel porcine bocavirus",
                 "Using a high-throughput DNA sequencing method, one DNA sequence was found.")
    _, found = diagnose(rec, "sequencing")
    assert found["cause"] == "phrase_gap"
    [gap] = found["phrase_gaps"]
    assert gap["found"] == "high throughput dna sequencing" and gap["words_between"] == 1
    assert gap["try"] == '"high throughput sequencing"[tiab:~1]'


def test_part_of_a_long_phrase_suggests_the_shorter_phrase():
    rec = record("3", "Brief eclectic psychotherapy for police officers",
                 "The treatment combines cognitive-behavioral and psychodynamic approaches.")
    _, found = diagnose(rec, "cbt")
    assert found["cause"] == "phrase_gap"
    [part] = found["partial_phrases"]
    assert part["matched"] == "cognitive behavio*" and part["absent"] == ["therap*"]
    assert part["try"] == '"cognitive behavio*"[tiab]'


def test_proximity_term_reports_only_a_gap_wider_than_its_distance():
    near = record("4", "Exposure based therapy", "")
    wide = record("5", "Exposure and other brief therapy", "")
    far = record("6", "Exposure", "x " * 20 + "therapy")
    block = DIAGNOSIS.block("cbt")
    assert "phrase_gaps" not in terms.diagnose_block(near, block)  # one word between: within ~1
    assert terms.diagnose_block(wide, block)["phrase_gaps"][0]["words_between"] == 3
    assert "phrase_gaps" not in terms.diagnose_block(far, block)  # title and abstract never join


def test_wildcard_phrase_gap_explains_that_proximity_is_ignored():
    block = Strategy.from_dict({"blocks": [{"id": "b", "name": "", "terms": ["growth mixture model*[tiab]"]}]}).block("b")
    [gap] = terms.diagnose_block(record("7", "Growth and mixture models"), block)["phrase_gaps"]
    assert gap["words_between"] == 1 and "wildcard" in gap["try"]


def test_record_without_block_wording_or_abstract_is_labelled():
    silent = record("8", "Discovery of a novel nidovirus in cattle", "We report the genetic characterization of a virus.")
    assert terms.diagnose_block(silent, DIAGNOSIS.block("sequencing")) == {"block": "sequencing", "cause": "no_block_wording"}
    assert terms.diagnose_block(record("9", "A porcine circovirus"), DIAGNOSIS.block("sequencing"))["cause"] == "no_abstract"


def test_short_stems_and_word_starts_are_not_reported_as_embedded():
    block = Strategy.from_dict({"blocks": [{"id": "b", "name": "", "terms": ["rate*[tiab]", "virus*[tiab]"]}]}).block("b")
    assert "embedded_stems" not in terms.diagnose_block(record("10", "Moderate and accurate viruses"), block)


def test_missing_vocabulary_lists_keywords_and_title_before_the_abstract():
    rec = record("11", "Latent trajectories of distress", "Aardvark abacus abdomen. " * 30, keywords=["Growth mixture modeling"])
    row, _ = diagnose(rec, "virus")
    found = row["text_not_in_strategy"]
    assert found[:2] == ["growth mixture modeling", "latent trajectories"]
    assert max(map(found.index, ["distress", "trajectories of distress"])) < found.index("aardvark abacus")


# -- mining gaps: substance names and plurals ------------------------------------------------------

def test_candidates_fold_singular_and_plural_and_offer_one_truncated_term():
    recs = [record("1", "A trajectory of distress"), record("2", "Trajectories of distress"), record("3", "Symptom trajectories")]
    rows = {r["term"]: r for r in terms.candidates(recs, ["tiab"])}
    row = rows["trajectories"]
    assert row["df"] == 3 and row["variants"] == ["trajectories", "trajectory"] and row["truncated"] == "trajector*"
    assert "trajectory" not in rows and "variants" not in rows["distress"]
    assert terms._singular("growth curves") == "growth curve" and terms._singular("viruses") == "virus"
    assert terms._singular("analysis") == "analysis" and terms._singular("status") == "status"


def test_rank_counts_the_truncated_form_in_pubmed(make_ws):
    ws, _ = make_ws({"trajector*[tiab]": {"1", "2", "3", "4"}, "x[tiab]": {"1"}})
    recs = [record("1", "A trajectory of distress"), record("2", "Trajectories of distress")]
    strategy = Strategy.from_dict({"blocks": [{"id": "b", "name": "", "terms": ["x[tiab]"]}]})
    scored = {r["term"]: r for r in terms.rank(ws.pubmed, recs, strategy, fields=["tiab"])["scored"]}
    assert scored["trajectories"]["query"] == "trajector*[tiab]" and scored["trajectories"]["background"] == 4


def test_substance_names_are_mined_unless_already_a_heading_of_the_record():
    recs = [dict(record("1", "Cetirizine trial", mesh=["Histamine H1 Antagonists"]), substances=["Histamine H1 Antagonists", "levocetirizine"]),
            dict(record("2", "Another trial"), substances=["levocetirizine"])]
    rows = [r for r in terms.candidates(recs, ["tiab", "mesh"]) if r["field"] == "nm"]
    assert [(r["term"], r["df"], r["sources"]) for r in rows] == [("levocetirizine", 2, ["substance"])]
    assert terms.background_query("levocetirizine", "nm") == '"levocetirizine"[nm]'
    assert not [r for r in terms.candidates(recs, ["tiab"]) if r["field"] == "nm"]


def test_miss_report_lists_substances_the_strategy_lacks():
    strategy = Strategy.from_dict({"blocks": [{"id": "b", "name": "", "terms": ['"cetirizine"[nm]', "x[tiab]"]}]})
    rec = dict(record("1", "A trial"), substances=["cetirizine", "levocetirizine"])
    [row] = terms.miss_report([rec], {"misses": [{"pmid": "1", "failing_blocks": ["b"]}]}, strategy)
    assert row["substances_not_in_strategy"] == ["levocetirizine"]

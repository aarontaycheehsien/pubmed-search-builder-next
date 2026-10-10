"""The as_of cutoff: Create Date [crdt] for new workspaces, Entry Date [edat] kept by older ones.

NLM resets a citation's Entry Date to its publication date when it is added more than a year later, so
an edat cutoff admits records created after the date (PMID 37333960: EDAT 2020/12/15, CRDT 2023/06/19).
A workspace made before cutoff.json keeps edat everywhere, so its allocation, receipts and delivery keep
their meaning; the field is recorded only where it is not edat."""

import os

import pytest

from psb import allocation, deliver, holdout
from psb.ncbi import PubMed
from psb.workspace import CUTOFF, WorkspaceError, read_json, write_json
from test_allocation import make_pool, through_critic
from test_closing_round import PASS, write_round

LEGACY_BINDING = {"query", "strategy_sha256", "review_sha256", "as_of", "allocation_sha256", "holdout_sha256",
                  "eligibility_sha256", "policy_version", "template_version"}


def delivered(make_ws, *, as_of="2030-01-01", legacy=False):
    """A held-out build delivered with ``as_of`` set; ``legacy`` removes cutoff.json, as in older workspaces."""
    ws, fake = make_pool(make_ws)
    if legacy:
        (ws.root / CUTOFF).unlink()
    protocol = ws.protocol()
    protocol["as_of"] = as_of
    write_json(ws.root / "protocol.json", protocol)
    allocation.freeze(ws, choice="keep-holdout")
    through_critic(ws)
    write_round(ws, 2, [], PASS, closing=True)
    receipt = holdout.run(ws)
    result = deliver.report(ws)
    assert result["ok"], result
    return ws, fake, receipt


def test_new_workspaces_bound_on_create_date_and_record_it(make_ws):
    ws, fake, receipt = delivered(make_ws)
    assert read_json(ws.root / CUTOFF) == {"version": 1, "field": "crdt"} and ws.pubmed.as_of_field == "crdt"
    evaluation = deliver.latest_evaluation(ws)
    assert evaluation["as_of_field"] == "crdt"
    assert evaluation["query"].endswith('AND ("1800/01/01"[crdt] : "2030/01/01"[crdt])')
    assert all("[crdt]" in line["query"] and "[edat]" not in line["query"] for line in evaluation["lines"])
    assert ws.allocation()["bindings"]["as_of_field"] == "crdt"
    assert receipt["binding"]["as_of_field"] == "crdt" and set(receipt["binding"]) == LEGACY_BINDING | {"as_of_field"}
    manifest = read_json(ws.root / "validation-manifest.json")
    assert manifest["as_of_field"] == "crdt" and "against PubMed records added up to 2030-01-01 (Create Date)" in \
        manifest["holdout"]["text"]
    assert "- Records added to PubMed up to: 2030-01-01 (Create Date [crdt])" in (ws.root / "audit.md").read_text(
        encoding="utf-8")
    assert deliver.verify_delivery(ws)["ok"] and allocation.state(ws)["stale"] == []


def test_older_workspaces_keep_entry_date_consistently(make_ws):
    ws, fake, receipt = delivered(make_ws, legacy=True)
    assert ws.as_of_field() == "edat" and ws.pubmed.as_of_field == "edat"
    evaluation = deliver.latest_evaluation(ws)
    assert "as_of_field" not in evaluation and evaluation["query"].endswith('("1800/01/01"[edat] : "2030/01/01"[edat])')
    assert "as_of_field" not in ws.allocation()["bindings"]
    assert set(receipt["binding"]) == LEGACY_BINDING  # the binding an older version wrote, unchanged
    manifest = read_json(ws.root / "validation-manifest.json")
    assert "as_of_field" not in manifest and "(Create Date)" not in manifest["holdout"]["text"]
    assert "- Records added to PubMed up to: 2030-01-01 (Entry Date [edat])" in (ws.root / "audit.md").read_text(
        encoding="utf-8")
    assert deliver.verify_delivery(ws)["ok"] and allocation.state(ws)["stale"] == []
    assert holdout.run(ws).get("repeat")  # the same binding: the stored receipt still matches


def test_a_changed_cutoff_field_makes_the_allocation_stale(make_ws):
    ws, _, _ = delivered(make_ws)
    saved = (ws.root / CUTOFF).read_text(encoding="utf-8")
    (ws.root / CUTOFF).unlink()
    assert allocation.state(ws)["stale"] == [
        "the effective date's field changed after the allocation was frozen (crdt, now edat)"]
    assert deliver.verify_delivery(ws)["ok"]  # the delivery itself does not move
    (ws.root / CUTOFF).write_text(saved, encoding="utf-8")
    assert allocation.state(ws)["stale"] == []
    write_json(ws.root / CUTOFF, {"version": 1, "field": "dp"})
    with pytest.raises(WorkspaceError, match="cutoff.json must be an object whose field is one of crdt, edat"):
        ws.pubmed.search("asthma*[tiab]")


def test_without_as_of_nothing_changes(make_ws, tmp_path, monkeypatch):
    """The same build with and without cutoff.json, no as_of: the same queries, hashes and bindings."""
    from psb import workspace as workspace_module
    for module in (allocation, workspace_module):  # allocation.json and sets carry their creation time
        monkeypatch.setattr(module, "now", lambda: "2026-01-01T00:00:00+00:00")
    found = []
    for legacy in (False, True):
        ws, _ = make_pool(make_ws)
        if legacy:
            (ws.root / CUTOFF).unlink()
        allocation.freeze(ws, choice="keep-holdout")
        evaluation = through_critic(ws)
        receipt = holdout.run(ws)
        assert "as_of_field" not in evaluation and "as_of_field" not in ws.allocation()["bindings"]
        assert set(receipt["binding"]) == LEGACY_BINDING and "[crdt]" not in evaluation["query"]
        found.append((evaluation["query"], evaluation["review_sha256"], {k: v for k, v in receipt["binding"].items()
                                                                          if k != "allocation_sha256"}))
        os.rename(ws.root, tmp_path / ("crdt" if not legacy else "legacy"))  # make_ws reuses tmp_path / "run"
    assert found[0] == found[1]


@pytest.mark.skipif(os.environ.get("PSB_LIVE_TESTS") != "1", reason="opt-in live NCBI check")
def test_live_create_date_excludes_a_record_with_a_backdated_entry_date():
    """PMID 37333960: DP 2020 Sep, EDAT 2020/12/15, CRDT 2023/06/19."""
    assert PubMed(as_of="2020-12-31").existing(["37333960"]) == set()
    assert PubMed(as_of="2020-12-31", as_of_field="edat").existing(["37333960"]) == {"37333960"}

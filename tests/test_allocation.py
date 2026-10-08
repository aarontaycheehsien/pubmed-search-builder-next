"""Allocation: the pool, units, exposure, the hash-ordered draw, the choice and the freeze."""

import json

import pytest

from conftest import record
from psb import allocation, cli, deliver, progress, reserved
from psb.evaluate import evaluate
from psb.workspace import WorkspaceError, write_json
from test_closing_round import PASS, write_round

POOL = [str(p) for p in range(101, 121)]
HELD = ["103", "104", "113", "114", "115", "118"]  # the sha256-order-v1 draw for POOL with seed 1
FULL = ['"Asthma"[Mesh]', "asthma*[tiab]"]
MESH_ONLY = ['"Asthma"[Mesh]']


def make_pool(make_ws, pool=POOL, *, builder=(), grouped=True, depth="standard", terms=FULL, origin="prior-review"):
    """A workspace whose eligible pool is ``pool``, screened in the separate context (``builder`` by the builder).
    The MeSH term misses the last six records; the text word finds them all."""
    atoms = {'"Asthma"[Mesh]': set(pool[:-6]) | {"1"}, "asthma*[tiab]": set(pool) | {"1"}}
    ws, fake = make_ws(atoms, {p: record(p, f"Record {p}", "Asthma.") for p in [*pool, "1"]},
                       question="Treatments for asthma?")
    protocol = ws.protocol()
    protocol.update(depth=depth, concepts=[{"id": "asthma", "name": "Asthma", "role": "search", "rationale": "topic"}],
                    eligibility={"include": ["asthma trials"], "exclude": []})
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": list(terms)}]})
    for pmid in pool:
        context = "builder" if pmid in builder else "separate"
        progress.record_screening(ws, include=[pmid], context=context, group=f"S{pmid}" if grouped else None,
                                  origin=[origin], evidence="abstract", reason=f"RCT {pmid}", source_ref="Table 2")
    return ws, fake


def through_critic(ws, number=1, **kwargs):
    """Evaluate the current strategy and record a passing critic round for it."""
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="draft")
    ws.save_attempt(evaluation)
    write_round(ws, number, [], PASS, **kwargs)
    return evaluation


def held(ws):
    return sorted((p for u in allocation.state(ws)["held"] for p in u["members"]), key=int)


@pytest.mark.parametrize("n,u,h", [(9, 9, 0), (10, 10, 3), (15, 15, 5), (20, 20, 6), (35, 35, 11), (55, 55, 17),
                                   (20, 2, 2), (20, 0, 0), (8, 8, 0)])
def test_holdout_size_rounds_half_up_with_integers(n, u, h):
    assert allocation.holdout_size(n, u) == h


def test_twenty_unexposed_units_split_fourteen_six_by_the_pinned_draw(make_ws):
    ws, _ = make_pool(make_ws)
    proposal = allocation.propose(ws)
    assert (proposal["N"], proposal["U"], proposal["H"]) == (20, 20, 6)
    assert proposal["development"] == {"units": 14, "records": 14} and proposal["studies"] == 20
    assert sorted((u["id"] for u in proposal["units"] if u["purpose"] == "holdout"), key=int) == HELD
    other = allocation.propose(ws, seed=2)
    assert sorted((u["id"] for u in other["units"] if u["purpose"] == "holdout"), key=int) != HELD


def test_two_unexposed_units_give_eighteen_two(make_ws):
    ws, _ = make_pool(make_ws, builder=POOL[:18])
    proposal = allocation.propose(ws)
    assert (proposal["N"], proposal["U"], proposal["H"]) == (20, 2, 2)
    assert sorted(u["id"] for u in proposal["units"] if u["purpose"] == "holdout") == POOL[18:]


def test_eight_units_stay_in_development_without_a_prompt(make_ws):
    ws, _ = make_pool(make_ws, pool=POOL[:8])
    proposal = allocation.propose(ws)
    assert proposal["H"] == 0 and proposal["reason"] == "small"
    message = progress.render(ws, "allocation-preview", {"proposal": proposal})["text"]
    assert message.splitlines()[1] == "No holdout is proposed: fewer than 10 eligible units."
    frozen = allocation.freeze(ws)
    assert frozen["choice"] is None and frozen["reason"] == "small" and frozen["H"] == 0
    assert ws.set_pmids("development") == set(POOL[:8]) and ws.reserved_pmids() == set()


def test_no_eligible_records_freezes_an_empty_allocation(make_ws):
    ws, _ = make_ws({"asthma*[tiab]": {"1"}})
    proposal = allocation.propose(ws)
    assert (proposal["N"], proposal["reason"]) == (0, "empty")
    assert progress.render(ws, "allocation-preview", {"proposal": proposal})["text"].splitlines()[1] == \
        "No holdout is proposed: no eligible reference records."
    assert allocation.freeze(ws)["N"] == 0
    from psb import holdout
    assert holdout.message(ws)["case"] == "no_records"


def test_the_choice_message_is_fixed_and_a_proposal_needs_a_choice(make_ws):
    ws, _ = make_pool(make_ws)
    proposal = allocation.propose(ws)
    assert progress.render(ws, "allocation-preview", {"proposal": proposal})["text"] == "\n".join([
        "**PSB · Step 3/7 Known records · Choose the allocation**",
        "**Choose how to use the eligible reference records**",
        "",
        "Eligible pool: **20 records representing 20 studies.**",
        "",
        "- **Development: 14 units (14 records)** — used for term mining, diagnosing misses, and improving the search.",
        "- **Held-out test: 6 units (6 records)** — reserved for one retrieval check after the query is finalised.",
        "",
        "**Separation:** 20 units of 20 were screened only in the separate context and never shown to the builder; "
        "the held-out units are drawn from these. The other 0 units were seen by the builder and go to development.",
        "",
        progress.CHOICE_EXPLAINED,
        "",
        "**Keep the proposed holdout**, or **use everything for development**?",
        "",
        "Using everything provides more development material but leaves no independent final test.",
    ])
    with pytest.raises(WorkspaceError, match="a holdout is proposed"):
        allocation.freeze(ws)
    assert ws.allocation() is None


@pytest.mark.parametrize("choice,h", [("keep-holdout", 6), ("proceed-default", 6), ("all-development", 0)])
def test_each_choice_is_recorded(make_ws, choice, h):
    ws, _ = make_pool(make_ws)
    frozen = allocation.freeze(ws, choice=choice)
    assert frozen["choice"] == choice and frozen["H"] == h and len(ws.reserved_pmids()) == h
    assert ws.set_pmids("development") == set(POOL) - ws.reserved_pmids()
    with pytest.raises(WorkspaceError, match="already frozen"):
        allocation.freeze(ws, choice=choice)


def test_keep_holdout_is_refused_when_none_is_proposed(make_ws):
    ws, _ = make_pool(make_ws, pool=POOL[:8])
    with pytest.raises(WorkspaceError, match="no holdout is proposed"):
        allocation.freeze(ws, choice="keep-holdout")


def test_reports_of_one_study_stay_together(make_ws):
    ws, _ = make_pool(make_ws)
    # 104 and 105 are reports of one study: a single unit, held out or developed together.
    progress.record_screening(ws, include=["105"], context="separate", group="S104")
    proposal = allocation.propose(ws)
    unit = next(u for u in proposal["units"] if "105" in u["members"])
    assert unit["members"] == ["104", "105"] and unit["id"] == "104" and proposal["N"] == 19
    assert proposal["studies"] == 19


def test_unknown_grouping_counts_pmids_and_leaves_studies_unverified(make_ws):
    ws, _ = make_pool(make_ws, grouped=False)
    proposal = allocation.propose(ws)
    assert proposal["N"] == 20 and proposal["studies"] is None
    assert all(u["grouping"] == "unverified" for u in proposal["units"])
    text = progress.render(ws, "allocation-preview", {"proposal": proposal})["text"]
    assert "Eligible pool: **20 records representing an unverified number of studies.**" in text


def test_quick_depth_never_proposes_a_holdout(make_ws):
    ws, _ = make_pool(make_ws, depth="quick")
    proposal = allocation.propose(ws)
    assert proposal["H"] == 0 and proposal["reason"] == "quick"
    with pytest.raises(WorkspaceError, match="standard-depth step"):
        allocation.freeze(ws, reserve=["101", "102"])
    assert allocation.freeze(ws)["reason"] == "quick"


def test_a_designated_set_replaces_the_automatic_holdout(make_ws):
    ws, _ = make_pool(make_ws)
    progress.record_screening(ws, exclude=["102"], context="separate")
    with pytest.raises(WorkspaceError, match="no screening decision"):
        allocation.freeze(ws, reserve=["101", "999"])
    frozen = allocation.freeze(ws, reserve=["101", "102", "110"])
    assert frozen["choice"] == "designated" and frozen["H"] == 2
    assert ws.reserved_pmids() == {"101", "110"}
    assert frozen["excluded"]["designated_removed"] == [{"pmid": "102", "reason": "screened exclude"}]


def test_unavailable_and_comparison_records_leave_the_pool(make_ws):
    ws, _ = make_pool(make_ws)
    progress.record_screening(ws, include=["999"], context="separate")  # not in PubMed
    ws.save_set("old", "comparison", ["120"])
    proposal = allocation.propose(ws)
    assert proposal["unavailable"] == ["999"] and proposal["on_comparison"] == ["120"] and proposal["N"] == 19


def test_records_the_builder_has_seen_are_exposed(make_ws, capsys):
    ws, _ = make_pool(make_ws)
    reserved.record(ws, ["101"], "abstract", "fetch")
    ws.save_set("seeds", "development", ["102"])
    reserved.record(ws, ["103"], "description", "declared", declared=True)
    progress.record_screening(ws, uncertain=["104"])
    progress.record_screening(ws, include=["104"], context="separate")  # an earlier builder decision still counts
    proposal = allocation.propose(ws)
    exposed = {u["id"]: u["exposure"] for u in proposal["units"] if u["exposed"]}
    assert set(exposed) == {"101", "102", "103", "104"} and proposal["U"] == 16
    assert exposed["101"] == [{"pmid": "101", "reasons": ["abstract shown by psb fetch"]}]
    assert "in a development set" in exposed["102"][0]["reasons"] and "not screened" not in exposed["102"][0]["reasons"]
    assert exposed["103"][0]["reasons"] == ["description declared"]
    assert exposed["104"][0]["reasons"] == ["screened by the builder"]


def test_cli_preview_freeze_and_status_show_counts_only(make_ws, capsys, monkeypatch):
    ws, _ = make_pool(make_ws)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    assert cli.main(["allocate", "--preview"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["H"] == 6 and "Choose how to use" in out["progress"]["text"]
    assert not any(p in out["progress"]["text"] for p in HELD)
    assert cli.main(["allocate"]) == 1 and "a holdout is proposed" in json.loads(capsys.readouterr().out)["error"]
    assert cli.main(["allocate", "--keep-holdout"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["allocation"]["holdout"] == {"units": 6, "records": 6}
    assert out["progress"]["text"].splitlines()[1] == ("Frozen: 14 units (14 records) for development · 6 units "
                                                       "(6 records) held out · you kept the proposed holdout")
    assert cli.main(["status"]) == 0
    status = capsys.readouterr().out
    assert not any(f'"{p}"' in status for p in HELD)
    assert "after the critic review, run the held-out test (psb holdout-test) before psb report" in status
    assert cli.main(["progress", "known-records"]) == 0
    assert "Known records: 14 for development · 6 held out · 0 on comparison lists" in capsys.readouterr().out


def test_eligibility_or_date_change_makes_the_allocation_stale_until_rebound(make_ws):
    ws, _ = make_pool(make_ws)
    allocation.freeze(ws, choice="keep-holdout")
    protocol = ws.protocol()
    protocol["eligibility"] = {"include": ["asthma trials in adults"], "exclude": []}
    write_json(ws.root / "protocol.json", protocol)
    assert allocation.state(ws)["stale"] == ["eligibility changed after the allocation was frozen"]
    through_critic(ws)
    from psb import holdout
    with pytest.raises(WorkspaceError, match="psb allocate --rebind"):
        holdout.run(ws)
    with pytest.raises(WorkspaceError, match="not re-screened"):
        allocation.rebind(ws)
    progress.record_screening(ws, include=[p for p in HELD if p != "115"], context="separate")
    progress.record_screening(ws, exclude=["115"], context="separate")
    event = allocation.rebind(ws)
    assert event["removed"] == ["115"] and "re-screened exclude" in event["reasons"]["115"]
    assert held(ws) == [p for p in HELD if p != "115"] and allocation.state(ws)["stale"] == []


def test_a_later_report_of_a_reserved_study_is_kept_out(make_ws, capsys, monkeypatch):
    ws, _ = make_pool(make_ws)
    allocation.freeze(ws, choice="keep-holdout")
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    progress.record_screening(ws, include=["150"], group="S113")  # the builder screened a companion of 113
    assert cli.main(["set", "add", "development", "150", "--purpose", "development"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["late_companions"] == 1 and "150" not in out["pmids"]
    assert "- Kept out: 1 record reporting a study reserved for the held-out test" in out["progress"]["text"]
    assert "150" in ws.reserved_pmids()
    late = allocation.state(ws)["late"]
    assert late[0]["unit"] == "113" and late[0]["exposed"] is True
    assert held(ws) == HELD  # denominators never change

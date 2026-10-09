"""The critic review budget: a review extension the user grants after the verification round, the
pre-flight that keeps the last rounds for a deliverable draft, and the rounds left in psb status."""

import json

import pytest

from psb import allocation, cli, deliver, holdout, progress, validation
from psb.evaluate import evaluate
from psb.workspace import WorkspaceError, read_json, write_json
from test_allocation import FULL, HELD, MESH_ONLY, make_pool
from test_closing_round import PASS
from test_deliver import evaluated
from test_guardrails import add_issue

REASON = "PubMed indexing changed between the verification round and psb report"


def eval_again(ws):
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="re-evaluated")
    ws.save_attempt(evaluation)
    return evaluation


def review(ws, number, *, epoch=1, closing=False):
    """A passing round on the latest evaluation, answering every mandatory issue review."""
    evaluation = ws.attempts()[-1]["evaluation"]
    write_json(ws.root / "critic" / f"round-{number}.json", {
        "round": number, **({"epoch": epoch} if epoch > 1 else {}), **({"closing": True} if closing else {}),
        "strategy_version": evaluation.get("version"), "review_sha256": evaluation["review_sha256"],
        "domains": PASS, "findings": [],
        "issue_dispositions": [{"issue_id": i["id"], "status": "accepted-risk", "response": "Reviewed",
                                "evidence": "Fixture"} for i in evaluation["validation"]["review_required"]]})


def verified(ws):
    """Standard depth: two revision rounds, the closing round and the verification round."""
    for number in (1, 2):
        review(ws, number)
    review(ws, 3, closing=True)
    review(ws, 4, closing=True)


def drift(ws):
    """A development record gains MeSH indexing after the last round: nobody changed the workspace."""
    fake = ws.pubmed
    fake.universe.add("4")
    fake.atoms[fake._key('"Asthma"[Mesh]')] = fake.atoms[fake._key('"Asthma"[Mesh]')] | {"4"}


def run(capsys, *argv):
    code = cli.main(list(argv))
    return code, json.loads(capsys.readouterr().out)


def test_an_extension_is_refused_while_a_round_is_left_or_the_review_is_current(make_ws):
    ws = evaluated(make_ws)
    with pytest.raises(WorkspaceError, match=r"no extension is needed: round 1 \(revision\) is still available"):
        deliver.extend_review(ws, REASON)
    review(ws, 1)
    review(ws, 2)
    with pytest.raises(WorkspaceError, match=r"round 3 \(closing\) is still available"):
        deliver.extend_review(ws, REASON)
    review(ws, 3, closing=True)
    with pytest.raises(WorkspaceError, match="no extension is needed: the closing round reviewed the current strategy"):
        deliver.extend_review(ws, REASON)
    drift(ws)
    eval_again(ws)
    with pytest.raises(WorkspaceError, match=r"round 4 \(verification\) is still available"):
        deliver.extend_review(ws, REASON)
    review(ws, 4, closing=True)  # the verification round reviews the drifted evaluation
    with pytest.raises(WorkspaceError, match="the closing round reviewed the current strategy"):
        deliver.extend_review(ws, REASON)
    with pytest.raises(WorkspaceError, match="give the reason"):
        deliver.extend_review(ws, "  ")
    assert deliver.report(ws)["ok"] and not (ws.root / "critic" / "extensions.json").exists()


def test_an_extension_after_drift_unblocks_delivery_and_is_disclosed(make_ws, capsys, monkeypatch):
    ws = evaluated(make_ws)
    verified(ws)
    assert deliver.report(ws)["ok"]
    drift(ws)
    result = deliver.report(ws)  # re-evaluates live: the review is stale and no round is left
    assert not result["ok"] and "critic_stale" in {b["code"] for b in result["blockers"]}
    with pytest.raises(deliver.ReviewExhausted, match="ask the user whether to extend the review"):
        deliver.critic_packet(ws)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    assert run(capsys, "status")[1]["critic_rounds_left"].startswith("none left")

    code, out = run(capsys, "critic", "extend", "--reason", REASON)
    assert code == 0 and out["epoch"] == 2 and out["after_round"] == 4
    assert out["progress"]["text"].splitlines()[:2] == [
        "**PSB · Step 6/7 Critic · Review extended**", f"Review budget extended at the user's request: {REASON}"]
    assert read_json(ws.root / "critic" / "extensions.json")[0]["reason"] == REASON
    assert (deliver.current_epoch(ws), deliver.epoch_kind(ws, 2)) == (2, "extension")
    assert run(capsys, "status")[1]["critic_rounds_left"] == (
        "extension: revision 0/1 used · 1 revision, closing and verification left")
    code, out = run(capsys, "critic", "packet")
    assert code == 0 and out["progress"]["text"].splitlines()[1] == (
        "Round 5 (extension revision 1 of 1) packet written for v1")
    packet = (ws.root / "critic" / "packet-5.md").read_text(encoding="utf-8")
    assert f"**Review extension.** The user extended the review budget after round 4: {REASON}." in packet
    assert '"epoch": 2' in packet and "repair" not in packet.lower().split("## complete evidence")[0]
    review(ws, 5, epoch=2)
    result = deliver.report(ws)
    assert result["ok"], result

    audit = (ws.root / "audit.md").read_text(encoding="utf-8")
    first_page = audit.split("## Question and scope")[0]
    assert f"Review budget extended at the user's request: {REASON}" in first_page
    assert "followed round 4" in first_page
    assert deliver.verify_delivery(ws)["ok"]
    extensions = ws.root / "critic" / "extensions.json"
    saved = extensions.read_text(encoding="utf-8")
    write_json(extensions, [{**json.loads(saved)[0], "reason": "edited later"}])
    assert deliver.verify_delivery(ws) == {"ok": False, "error": "critic evidence has changed"}
    extensions.write_text(saved, encoding="utf-8")
    assert deliver.verify_delivery(ws)["ok"]
    for stage in ("critic", "deliver"):
        assert f"review budget extended at the user's request: {REASON}".lower() in \
            run(capsys, "progress", stage)[1]["progress"]["text"].lower()
    with pytest.raises(WorkspaceError, match="already extended once"):
        deliver.extend_review(ws, "again")


def test_the_critic_digest_is_unchanged_without_an_extension(make_ws):
    ws = evaluated(make_ws)
    verified(ws)
    assert deliver.report(ws)["ok"]
    rounds = deliver.critic_rounds(ws)
    manifest = read_json(ws.root / "validation-manifest.json")
    assert manifest["critic_sha256"] == validation.digest(rounds) == deliver.critic_digest(rounds, [], [])
    overrides = [{"id": "F1", "round": 4, "response": "r"}]
    assert deliver.critic_digest(rounds, overrides, []) == validation.digest({"rounds": rounds, "overrides": overrides})
    assert "Review budget extended" not in (ws.root / "audit.md").read_text(encoding="utf-8")
    assert "extended" not in progress.render(ws, "stage:critic")["text"]


def test_a_repair_after_an_extension_gets_its_own_epoch(make_ws):
    ws, fake = make_pool(make_ws, terms=MESH_ONLY)
    allocation.freeze(ws, choice="keep-holdout")
    eval_again(ws)
    verified(ws)
    assert holdout.run(ws)["records"]["retrieved"] == 4
    assert deliver.report(ws)["ok"]
    fake.atoms[fake._key('"Asthma"[Mesh]')] = fake.atoms[fake._key('"Asthma"[Mesh]')] | {"116"}  # indexing drift
    assert "critic_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}

    deliver.extend_review(ws, REASON)
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "**Review extension.**" in packet and "**Held-out test.** 6 units are reserved" in packet
    assert "**Repair review.**" not in packet
    review(ws, 5, epoch=2)
    assert ws.reserved_pmids() == set(HELD) and not ws.released()  # the extension touched no held-out record
    assert "holdout_test_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}
    assert holdout.run(ws)["number"] == 2  # same strategy, reviewed again: the test runs for the new binding
    assert deliver.report(ws)["ok"]

    allocation.release(ws, "repair the two missed records")
    assert (deliver.current_epoch(ws), deliver.epoch_kind(ws, 3)) == (3, "repair")
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": FULL}]})
    eval_again(ws)
    rounds = deliver.critic_rounds(ws)
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "**Repair review.**" in packet and '"epoch": 3' in packet and "**Review extension.**" not in packet
    message = progress.render(ws, "critic-packet", {"rounds_before": rounds, "packet": "packet-6.md"})["text"]
    assert "Round 6 (repair revision 1 of 1) packet" in message
    review(ws, 6, epoch=3)
    result = deliver.report(ws)
    assert result["ok"], result
    assert f"Review budget extended at the user's request: {REASON}" in (ws.root / "audit.md").read_text(encoding="utf-8")


def test_the_last_rounds_wait_until_technical_blockers_are_fixed(make_ws, capsys, monkeypatch):
    ws = evaluated(make_ws)
    add_issue(ws.pubmed, monkeypatch, code="field_not_found", severity="warning")
    evaluation = eval_again(ws)
    assert [b["code"] for b in evaluation["validation"]["blockers"]] == ["field_not_found"]
    assert evaluation["validation"]["complete"]
    deliver.critic_packet(ws)  # revision 1 of 2 is not one of the last rounds
    review(ws, 1)
    with pytest.raises(WorkspaceError, match=r"technical blockers no critic round can clear \(field_not_found\).*"
                                             r"last revision round.*--anyway"):
        deliver.critic_packet(ws)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    code, out = run(capsys, "critic", "packet")
    assert code == 1 and "field_not_found" in out["error"] and not (ws.root / "critic" / "packet-2.md").exists()
    code, out = run(capsys, "critic", "packet", "--anyway")
    assert code == 0 and out["packet"].endswith("packet-2.md")
    review(ws, 2)
    with pytest.raises(WorkspaceError, match=r"before using the closing round"):
        deliver.critic_packet(ws)
    assert "round 3 (closing)" in deliver.critic_packet(ws, anyway=True).read_text(encoding="utf-8")


def test_mandatory_issue_reviews_do_not_hold_back_the_last_rounds(make_ws, monkeypatch):
    ws = evaluated(make_ws)
    add_issue(ws.pubmed, monkeypatch, code="quoted_phrase_not_found", severity="warning")
    evaluation = eval_again(ws)
    assert not evaluation["validation"]["blockers"] and evaluation["validation"]["review_required"]
    review(ws, 1)
    assert "round 2" in deliver.critic_packet(ws).read_text(encoding="utf-8")  # the critic answers these


def test_status_shows_the_critic_rounds_left(make_ws, capsys, monkeypatch):
    ws = evaluated(make_ws)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    left = lambda: run(capsys, "status")[1]["critic_rounds_left"]  # noqa: E731
    assert left() == "revision 0/2 used · 2 revisions, closing and verification left"
    review(ws, 1)
    assert left() == "revision 1/2 used · 1 revision, closing and verification left"
    review(ws, 2)
    assert left() == "revision 2/2 used · closing and verification left"
    review(ws, 3, closing=True)
    assert left() == "revision 2/2 used · closing used · verification left"
    review(ws, 4, closing=True)
    assert left() == ("none left — psb report if the last round reviewed the current evaluation; otherwise report "
                      "--diagnostic, a critic override, or a review extension the user grants")

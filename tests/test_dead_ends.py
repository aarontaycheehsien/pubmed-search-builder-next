"""Ways out of the delivery dead ends seen in evaluation runs.

- Correcting conversation metadata (scope_confirmed, notes) after a delivery needs only a fresh
  `psb report`, never a fresh critic.
- A change after the closing round gets one verification round, then no more.
- A judgment-level must-fix left open at closing can be overridden with a reason; the audit opens
  with the objection. Syntax and filter findings cannot be overridden.
"""

import json

import pytest

from psb import deliver
from psb.workspace import WorkspaceError, read_json, write_json
from test_closing_round import OPEN, PASS, REVISE, exhaust_revision_rounds, revise_strategy, write_round
from test_deliver import evaluated


def edit_protocol(ws, **changes):
    write_json(ws.root / "protocol.json", {**ws.protocol(), **changes})


def closed_with_open_must_fix(ws, finding=OPEN):
    exhaust_revision_rounds(ws)
    write_round(ws, 3, [finding], REVISE, closing=True)


def test_metadata_edit_after_delivery_needs_only_a_fresh_report(make_ws):
    ws = evaluated(make_ws)
    write_round(ws, 1, [], PASS)
    assert deliver.report(ws)["ok"]
    edit_protocol(ws, scope_confirmed=not ws.protocol().get("scope_confirmed"), notes="Roles were not confirmed.")
    verified = deliver.verify_delivery(ws)
    assert not verified["ok"]
    assert "protocol.scope_confirmed" in verified["error"] and "critic is still current" in verified["error"]
    assert deliver.report(ws)["ok"]  # same critic round, no new review
    assert deliver.verify_delivery(ws)["ok"]


def test_search_edit_after_delivery_still_needs_the_critic(make_ws):
    ws = evaluated(make_ws)
    write_round(ws, 1, [], PASS)
    assert deliver.report(ws)["ok"]
    edit_protocol(ws, limits=[{"clause": "english[la]", "rationale": "requested"}])
    verified = deliver.verify_delivery(ws)
    assert "protocol.limits" in verified["error"] and "review the change with the critic" in verified["error"]
    assert "critic_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_change_after_closing_round_gets_one_verification_round(make_ws):
    ws = evaluated(make_ws)
    exhaust_revision_rounds(ws)
    write_round(ws, 3, [{**OPEN, "status": "resolved", "response": "wheez*[tiab] added"}], PASS, closing=True)
    assert deliver.report(ws)["ok"]
    edit_protocol(ws, eligibility={"include": ["children with asthma"], "exclude": []})
    revise_strategy(ws)
    assert "critic_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "round 4 (verification)" in packet and '"closing": true' in packet
    write_round(ws, 4, [{**OPEN, "status": "resolved", "response": "still added"}], PASS, closing=True)
    assert deliver.report(ws)["ok"]
    edit_protocol(ws, eligibility={"include": ["adults with asthma"], "exclude": []})
    revise_strategy(ws)
    with pytest.raises(WorkspaceError, match="verification round has been used"):
        deliver.critic_packet(ws)


def test_verification_round_cannot_raise_new_substantive_findings(make_ws):
    ws = evaluated(make_ws)
    exhaust_revision_rounds(ws)
    write_round(ws, 3, [{**OPEN, "status": "resolved", "response": "added"}], PASS, closing=True)
    new = {"id": "F9", "domain": "operators", "severity": "must-fix", "kind": "structural", "finding": "late idea", "status": "open"}
    path = write_round(ws, 4, [{**OPEN, "status": "resolved", "response": "added"}, new], REVISE, closing=True)
    assert not deliver.check_round(ws, path)["ok"]


def test_no_revision_round_after_a_closing_round(make_ws):
    ws = evaluated(make_ws)
    exhaust_revision_rounds(ws)
    write_round(ws, 3, [{**OPEN, "status": "resolved", "response": "added"}], PASS, closing=True)
    write_round(ws, 4, [], PASS)
    assert "critic_invalid" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_open_judgment_must_fix_can_be_overridden_after_closing(make_ws):
    ws = evaluated(make_ws)
    closed_with_open_must_fix(ws)
    checked = deliver.check_round(ws, ws.root / "critic" / "round-3.json")
    assert checked["overridable"] == ["F1"]
    assert not deliver.report(ws)["ok"]
    deliver.override_finding(ws, "F1", "wheez*[tiab] retrieved no further known records and 0/30 sampled were relevant")
    result = deliver.report(ws)
    assert result["ok"]
    audit = (ws.root / "audit.md").read_text(encoding="utf-8")
    assert "## Delivered over an open critic objection" in audit and "0/30 sampled were relevant" in audit
    assert audit.index("open critic objection") < audit.index("## Question and scope")
    assert read_json(ws.root / "validation-manifest.json")["overridden_findings"] == ["F1"]
    assert deliver.verify_delivery(ws)["ok"]
    write_json(ws.root / "critic" / "overrides.json", [])  # removing the override invalidates the delivery
    assert not deliver.verify_delivery(ws)["ok"]


@pytest.mark.parametrize("kind", ["syntax", "filter"])
def test_technical_findings_cannot_be_overridden(make_ws, kind):
    ws = evaluated(make_ws)
    closed_with_open_must_fix(ws, {**OPEN, "kind": kind})
    with pytest.raises(WorkspaceError, match="cannot be overridden"):
        deliver.override_finding(ws, "F1", "disagree")
    write_json(ws.root / "critic" / "overrides.json", [{"id": "F1", "round": 3, "response": "disagree"}])
    assert "override_invalid" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_override_is_refused_before_the_closing_round(make_ws):
    ws = evaluated(make_ws)
    write_round(ws, 1, [OPEN], REVISE)
    with pytest.raises(WorkspaceError, match="only after the closing round"):
        deliver.override_finding(ws, "F1", "disagree")


def test_should_fix_and_resolved_findings_are_not_overridable(make_ws):
    ws = evaluated(make_ws)
    closed_with_open_must_fix(ws, {**OPEN, "severity": "should-fix"})
    with pytest.raises(WorkspaceError, match="only an open must-fix"):
        deliver.override_finding(ws, "F1", "disagree")


def test_override_lapses_after_a_verification_round(make_ws):
    ws = evaluated(make_ws)
    closed_with_open_must_fix(ws)
    deliver.override_finding(ws, "F1", "disagree on evidence")
    assert deliver.report(ws)["ok"]
    edit_protocol(ws, eligibility={"include": ["children with asthma"], "exclude": []})
    revise_strategy(ws)
    write_round(ws, 4, [OPEN], REVISE, closing=True)
    assert "critic_open" in {b["code"] for b in deliver.report(ws)["blockers"]}

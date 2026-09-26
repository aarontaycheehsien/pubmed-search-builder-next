import io
import json
import urllib.error
import xml.etree.ElementTree as ET

import pytest

from psb import ncbi
from psb.cache import Cache, cache_key
from psb.http import Policy, Transport, TransportError, redact_url
from psb.ncbi import NcbiError, PubMed, body_error, parse_article
from psb.translation import translation_issues


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class ScriptedTransport:
    def __init__(self, bodies):
        self.bodies = list(bodies)
        self.calls = []

    def request(self, url, params, **kwargs):
        self.calls.append((url, dict(params)))
        return self.bodies.pop(0)


def esearch_body(count, ids=(), translation="", errors=None):
    return json.dumps({"esearchresult": {"count": str(count), "idlist": list(ids), "querytranslation": translation,
                                         "errorlist": errors or {}}}).encode()


def test_body_error_detects_outages_but_not_phrase_lists():
    assert body_error(b'{"esearchresult": {"ERROR": "Search Backend failed"}}') == "Search Backend failed"
    assert body_error(b"<eFetchResult><ERROR>boom</ERROR></eFetchResult>") == "boom"
    assert body_error(esearch_body(0, errors={"phrasesnotfound": ["zzz"]})) is None


def test_search_retries_body_errors_and_logs(monkeypatch):
    monkeypatch.setattr(ncbi.time, "sleep", lambda s: None)
    transport = ScriptedTransport([b'{"esearchresult": {"ERROR": "temporarily unavailable"}}', esearch_body(5, ["1"])])
    log = []
    pm = PubMed(transport=transport, log=log.append)
    assert pm.search("asthma[tiab]", retmax=1)["count"] == 5
    assert len(transport.calls) == 2
    assert log[-1]["endpoint"] == "esearch.fcgi" and log[-1]["cache"] is False
    assert "api_key" not in log[-1]["params"]


def test_rejected_query_is_not_retried():
    transport = ScriptedTransport([b'{"esearchresult": {"ERROR": "Cannot search because the number of wildcards (*) exceeds 256"}}'])
    with pytest.raises(NcbiError, match="rejected"):
        PubMed(transport=transport).search("x*[tiab]")


def test_as_of_bounds_pubmed_searches():
    transport = ScriptedTransport([esearch_body(1)])
    PubMed(transport=transport, as_of="2018-05-01").search("asthma[tiab]")
    params = transport.calls[0][1]
    assert (params["datetype"], params["maxdate"]) == ("edat", "2018/05/01")


def test_cache_serves_repeat_requests_and_excludes_credentials(tmp_path):
    transport = ScriptedTransport([esearch_body(3)])
    pm = PubMed(transport=transport, cache=Cache(tmp_path))
    pm.api_key = "SECRET"
    assert pm.count("a[tiab]") == 3 and pm.count("a[tiab]") == 3
    assert len(transport.calls) == 1
    assert "SECRET" not in "".join(p.read_text() for p in tmp_path.glob("*/*.json"))
    assert cache_key("e", {"term": "x", "api_key": "1"}) == cache_key("e", {"term": "x", "api_key": "2"})


def test_translation_issues():
    codes = {i["code"] for i in translation_issues("cat*[tiab] OR asthma", '"cat"[Title/Abstract] OR asthma[All Fields]',
                                                    [{"from": "asthma", "to": "asthma[All Fields]"}], None,
                                                    {"phrasesnotfound": ["zzzz"]})}
    assert {"truncation_dropped", "automatic_term_mapping", "all_fields", "phrase_not_found"} <= codes


def test_parse_article():
    xml = """<PubmedArticle><MedlineCitation Status="MEDLINE"><PMID>42</PMID><Article><Journal><Title>J</Title>
    <JournalIssue><PubDate><Year>2019</Year></PubDate></JournalIssue></Journal><ArticleTitle>A <i>title</i></ArticleTitle>
    <Abstract><AbstractText Label="METHODS">We did it.</AbstractText></Abstract>
    <PublicationTypeList><PublicationType>Randomized Controlled Trial</PublicationType></PublicationTypeList></Article>
    <MeshHeadingList><MeshHeading><DescriptorName UI="D001249" MajorTopicYN="Y">Asthma</DescriptorName>
    <QualifierName>therapy</QualifierName></MeshHeading></MeshHeadingList>
    <KeywordList><Keyword>wheeze</Keyword></KeywordList></MedlineCitation>
    <PubmedData><ArticleIdList><ArticleId IdType="doi">10.1/x</ArticleId></ArticleIdList></PubmedData></PubmedArticle>"""
    record = parse_article(ET.fromstring(xml))
    assert record["pmid"] == "42" and record["title"] == "A title" and record["year"] == "2019"
    assert record["abstract"] == "METHODS: We did it." and record["doi"] == "10.1/x"
    assert record["mesh"][0] == {"ui": "D001249", "name": "Asthma", "major": True, "qualifiers": ["therapy"]}
    assert record["keywords"] == ["wheeze"] and record["status"] == "MEDLINE"


def test_transport_retries_transient_http_and_redacts():
    attempts = []

    def opener(request, timeout):
        attempts.append(request.full_url)
        if len(attempts) == 1:
            raise urllib.error.HTTPError(request.full_url, 503, "busy", {}, io.BytesIO(b"busy"))
        return FakeResponse(b"ok")

    transport = Transport(opener=opener, sleep=lambda s: None)
    assert transport.request("https://x/e", {"api_key": "K"}, policy=Policy(retries=2)) == b"ok"
    assert len(attempts) == 2

    def failing(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 400, "bad", {}, io.BytesIO(b"bad"))

    with pytest.raises(TransportError) as info:
        Transport(opener=failing, sleep=lambda s: None).request("https://x/e", {"api_key": "K"})
    assert "api_key=K" not in str(info.value)
    assert redact_url("https://x/e?api_key=K&term=a") == "https://x/e?api_key=%2A%2A%2A&term=a"

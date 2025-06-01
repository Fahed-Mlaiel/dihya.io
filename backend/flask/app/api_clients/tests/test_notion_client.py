# test_notion_client.py – Tests unitaires pour Notion API Client (pytest, mock)
import pytest
import os
from backend.flask.app.api_clients import notion_client

@pytest.fixture(autouse=True)
def patch_env(monkeypatch):
    monkeypatch.setenv("NOTION_API_TOKEN", "test-token")

@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    class DummyResp:
        def raise_for_status(self): pass
        def json(self): return {"id": "page123"}
    monkeypatch.setattr(notion_client.requests, "post", lambda *a, **k: DummyResp())

def test_create_page_success():
    page_id = notion_client.create_page("dbid", "Titre Test", {"Test": {"rich_text": [{"text": {"content": "val"}}]}})
    assert page_id == "page123"

def test_create_page_no_token(monkeypatch):
    monkeypatch.delenv("NOTION_API_TOKEN", raising=False)
    assert notion_client.create_page("dbid", "Titre") is None

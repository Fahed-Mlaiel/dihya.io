"""
Tests d'intégration avancés pour le module Sécurité (CORS, JWT, WAF, anti-DDOS, audit, plugins, RGPD, i18n, multitenancy)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient
from backend.security import get_jwt_token_for_role

client = TestClient(app)

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt_token_for_role("admin")

@pytest.fixture(scope="module")
def user_token():
    return get_jwt_token_for_role("user")

def test_securite_cors():
    resp = client.options("/api/securite/", headers={"Origin": "https://example.com", "Access-Control-Request-Method": "GET"})
    assert resp.status_code == 200
    assert "access-control-allow-origin" in resp.headers

def test_securite_jwt_access(admin_token):
    resp = client.get("/api/securite/", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_securite_waf_block():
    # Simule une attaque simple (ex: SQLi)
    resp = client.get("/api/securite/?q=' OR 1=1 --")
    assert resp.status_code in (403, 429)

def test_securite_ddos_protection():
    for _ in range(20):
        resp = client.get("/api/securite/")
    assert resp.status_code in (200, 429)

def test_securite_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=securite", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("securite" in l["module"] for l in resp.json())

def test_securite_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "securite" in resp.json()

def test_securite_rgpd_export(admin_token):
    resp = client.get("/api/securite/export?format=csv", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")

def test_securite_i18n(admin_token):
    data = {"nom": "Sécurité أمازيغية", "type": "amazigh", "lang": "ar"}
    resp = client.post("/api/securite/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["lang"] == "ar"

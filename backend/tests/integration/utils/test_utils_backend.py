"""
Tests d'intégration avancés pour les utilitaires backend (sécurité, audit, plugins, RGPD, i18n, multitenancy)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient
from backend.security import get_jwt_token_for_role

client = TestClient(app)

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt_token_for_role("admin")

def test_utils_healthcheck():
    resp = client.get("/api/utils/healthcheck")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_utils_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=utils", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("utils" in l["module"] for l in resp.json())

def test_utils_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "utils" in resp.json()

def test_utils_rgpd_export(admin_token):
    resp = client.get("/api/utils/export?format=csv", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")

def test_utils_i18n(admin_token):
    data = {"message": "مرحبا", "lang": "ar"}
    resp = client.post("/api/utils/echo", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.json()["lang"] == "ar"

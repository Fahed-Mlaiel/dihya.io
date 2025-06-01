"""
Tests d'intégration avancés pour les validateurs backend (sécurité, audit, plugins, RGPD, i18n, multitenancy)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient
from backend.security import get_jwt_token_for_role

client = TestClient(app)

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt_token_for_role("admin")

def test_validators_email():
    resp = client.post("/api/validators/email", json={"email": "test@dihya.ai"})
    assert resp.status_code == 200
    assert resp.json()["valid"] is True

def test_validators_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=validators", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("validators" in l["module"] for l in resp.json())

def test_validators_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "validators" in resp.json()

def test_validators_rgpd_export(admin_token):
    resp = client.get("/api/validators/export?format=csv", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")

def test_validators_i18n(admin_token):
    data = {"value": "مرحبا", "lang": "ar"}
    resp = client.post("/api/validators/echo", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.json()["lang"] == "ar"

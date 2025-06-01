"""
Tests d'intégration E2E avancés pour l'API Dihya (Python)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient
from backend.security import get_jwt_token_for_role

client = TestClient(app)

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt_token_for_role("admin")

def test_seo_robots():
    resp = client.get("/api/seo/robots.txt")
    assert resp.status_code == 200
    assert "User-agent" in resp.text

def test_audit_log(admin_token):
    resp = client.get("/api/audit/logs", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_fallback_ia(admin_token):
    data = {"question": "Test fallback", "lang": "fr"}
    resp = client.post("/api/ia/fallback", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "answer" in resp.json()

def test_plugins_active(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "seo" in resp.json()

def test_utils_healthcheck():
    resp = client.get("/api/utils/healthcheck")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_seo_sitemap():
    resp = client.get("/api/seo/sitemap.xml")
    assert resp.status_code == 200
    assert "<urlset" in resp.text

def test_validators_email():
    resp = client.post("/api/validators/email", json={"email": "test@dihya.ai"})
    assert resp.status_code == 200
    assert resp.json()["valid"] is True

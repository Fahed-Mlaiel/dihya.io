"""
Tests d'intégration avancés pour le module SEO (robots.txt, sitemap, logs structurés, plugins, i18n, audit)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient
from backend.security import get_jwt_token_for_role

client = TestClient(app)

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt_token_for_role("admin")

def test_seo_robots_txt():
    resp = client.get("/robots.txt")
    assert resp.status_code == 200
    assert "User-agent" in resp.text

def test_seo_sitemap():
    resp = client.get("/sitemap.xml")
    assert resp.status_code == 200
    assert "<urlset" in resp.text

def test_seo_logs_structures(admin_token):
    resp = client.get("/api/seo/logs", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_seo_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "seo" in resp.json()

def test_seo_i18n(admin_token):
    data = {"title": "SEO أمازيغي", "lang": "ar"}
    resp = client.post("/api/seo/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["lang"] == "ar"

def test_seo_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=seo", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("seo" in l["module"] for l in resp.json())

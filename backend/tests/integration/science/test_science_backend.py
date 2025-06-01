"""
Tests d'intégration avancés pour le module Science (REST, GraphQL, sécurité, i18n, plugins, audit, fallback IA, RGPD)
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

def test_science_list_admin(admin_token):
    resp = client.get("/api/science/", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert all("id" in r for r in resp.json())

def test_science_create_admin(admin_token):
    data = {"nom": "Lab Dihya", "type": "laboratoire", "lang": "fr"}
    resp = client.post("/api/science/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["nom"] == "Lab Dihya"

def test_science_create_user_forbidden(user_token):
    data = {"nom": "User Lab", "type": "recherche", "lang": "en"}
    resp = client.post("/api/science/", json=data, headers={"Authorization": f"Bearer {user_token}"})
    assert resp.status_code == 403

def test_science_i18n(admin_token):
    data = {"nom": "مختبر أمازيغي", "type": "amazigh", "lang": "ar"}
    resp = client.post("/api/science/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["lang"] == "ar"

def test_science_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "science" in resp.json()

def test_science_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=science", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("science" in l["module"] for l in resp.json())

def test_science_fallback_ia(admin_token):
    data = {"question": "Quels sont les projets en cours?", "lang": "fr"}
    resp = client.post("/api/ia/fallback", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "projet" in resp.json()["answer"]

def test_science_rgpd_export(admin_token):
    resp = client.get("/api/science/export?format=csv", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")

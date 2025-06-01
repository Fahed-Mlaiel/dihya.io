"""
Tests d'intégration avancés pour le module Sport (REST, GraphQL, sécurité, i18n, plugins, audit, fallback IA, RGPD)
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

def test_sport_list_admin(admin_token):
    resp = client.get("/api/sport/", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert all("id" in r for r in resp.json())

def test_sport_create_admin(admin_token):
    data = {"nom": "Sport Dihya", "type": "club", "lang": "fr"}
    resp = client.post("/api/sport/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["nom"] == "Sport Dihya"

def test_sport_create_user_forbidden(user_token):
    data = {"nom": "User Sport", "type": "association", "lang": "en"}
    resp = client.post("/api/sport/", json=data, headers={"Authorization": f"Bearer {user_token}"})
    assert resp.status_code == 403

def test_sport_i18n(admin_token):
    data = {"nom": "نادي أمازيغي", "type": "amazigh", "lang": "ar"}
    resp = client.post("/api/sport/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["lang"] == "ar"

def test_sport_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "sport" in resp.json()

def test_sport_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=sport", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("sport" in l["module"] for l in resp.json())

def test_sport_fallback_ia(admin_token):
    data = {"question": "Quels sports sont proposés?", "lang": "fr"}
    resp = client.post("/api/ia/fallback", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "sport" in resp.json()["answer"]

def test_sport_rgpd_export(admin_token):
    resp = client.get("/api/sport/export?format=csv", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")

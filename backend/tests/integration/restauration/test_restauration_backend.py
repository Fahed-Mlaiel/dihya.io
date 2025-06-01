"""
Tests d'intégration avancés pour le module Restauration (REST, GraphQL, sécurité, i18n, plugins, audit, fallback IA)
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

def test_restauration_list_admin(admin_token):
    resp = client.get("/api/restauration/", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert all("id" in r for r in resp.json())

def test_restauration_create_admin(admin_token):
    data = {"nom": "Test Resto", "type": "fusion", "lang": "fr"}
    resp = client.post("/api/restauration/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["nom"] == "Test Resto"

def test_restauration_create_user_forbidden(user_token):
    data = {"nom": "User Resto", "type": "bio", "lang": "en"}
    resp = client.post("/api/restauration/", json=data, headers={"Authorization": f"Bearer {user_token}"})
    assert resp.status_code == 403

def test_restauration_i18n(admin_token):
    data = {"nom": "مطعم أمازيغي", "type": "amazigh", "lang": "ar"}
    resp = client.post("/api/restauration/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["lang"] == "ar"

def test_restauration_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "restauration" in resp.json()

def test_restauration_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=restauration", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("restauration" in l["module"] for l in resp.json())

def test_restauration_fallback_ia(admin_token):
    data = {"question": "Quel est le plat du jour?", "lang": "fr"}
    resp = client.post("/api/ia/fallback", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "plat" in resp.json()["answer"]

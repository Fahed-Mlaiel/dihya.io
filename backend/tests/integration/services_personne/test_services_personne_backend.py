"""
Tests d'intégration avancés pour le module Services à la personne (REST, GraphQL, sécurité, i18n, plugins, audit, fallback IA, RGPD)
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

def test_services_personne_list_admin(admin_token):
    resp = client.get("/api/services_personne/", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert all("id" in r for r in resp.json())

def test_services_personne_create_admin(admin_token):
    data = {"nom": "Aide Dihya", "type": "aide", "lang": "fr"}
    resp = client.post("/api/services_personne/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["nom"] == "Aide Dihya"

def test_services_personne_create_user_forbidden(user_token):
    data = {"nom": "User Aide", "type": "garde", "lang": "en"}
    resp = client.post("/api/services_personne/", json=data, headers={"Authorization": f"Bearer {user_token}"})
    assert resp.status_code == 403

def test_services_personne_i18n(admin_token):
    data = {"nom": "خدمة أمازيغية", "type": "amazigh", "lang": "ar"}
    resp = client.post("/api/services_personne/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["lang"] == "ar"

def test_services_personne_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "services_personne" in resp.json()

def test_services_personne_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=services_personne", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("services_personne" in l["module"] for l in resp.json())

def test_services_personne_fallback_ia(admin_token):
    data = {"question": "Quels services proposez-vous?", "lang": "fr"}
    resp = client.post("/api/ia/fallback", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "service" in resp.json()["answer"]

def test_services_personne_rgpd_export(admin_token):
    resp = client.get("/api/services_personne/export?format=csv", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")

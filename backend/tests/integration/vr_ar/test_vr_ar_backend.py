"""
Tests d'intégration avancés pour le module VR/AR (REST, GraphQL, sécurité, i18n, plugins, audit, fallback IA, RGPD)
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

def test_vr_ar_list_admin(admin_token):
    resp = client.get("/api/vr_ar/", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert all("id" in r for r in resp.json())

def test_vr_ar_create_admin(admin_token):
    data = {"nom": "VR Dihya", "type": "vr", "lang": "fr"}
    resp = client.post("/api/vr_ar/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["nom"] == "VR Dihya"

def test_vr_ar_create_user_forbidden(user_token):
    data = {"nom": "User VR", "type": "ar", "lang": "en"}
    resp = client.post("/api/vr_ar/", json=data, headers={"Authorization": f"Bearer {user_token}"})
    assert resp.status_code == 403

def test_vr_ar_i18n(admin_token):
    data = {"nom": "واقع افتراضي أمازيغي", "type": "amazigh", "lang": "ar"}
    resp = client.post("/api/vr_ar/", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 201
    assert resp.json()["lang"] == "ar"

def test_vr_ar_plugin_integration(admin_token):
    resp = client.get("/api/plugins/active", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "vr_ar" in resp.json()

def test_vr_ar_audit_log(admin_token):
    resp = client.get("/api/audit/logs?module=vr_ar", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert any("vr_ar" in l["module"] for l in resp.json())

def test_vr_ar_fallback_ia(admin_token):
    data = {"question": "Quels services VR/AR proposez-vous?", "lang": "fr"}
    resp = client.post("/api/ia/fallback", json=data, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert "vr" in resp.json()["answer"] or "ar" in resp.json()["answer"]

def test_vr_ar_rgpd_export(admin_token):
    resp = client.get("/api/vr_ar/export?format=csv", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")

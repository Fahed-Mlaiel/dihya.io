import pytest
from flask import Flask, json
from app.routes.banque_finance.routes import app as banque_app

@pytest.fixture
def client():
    app = banque_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_banque_success(client):
    data = {
        "nom": "BNP Paribas",
        "code_bic": "BNPAFRPP",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/banque/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "Banque créée" in response.get_data(as_text=True)

def test_create_banque_invalid_bic(client):
    data = {
        "nom": "Société Générale",
        "code_bic": "123",
        "pays": "France",
        "tenant_id": 2
    }
    response = client.post("/banque/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "BIC est invalide" in response.get_data(as_text=True)

def test_update_banque(client):
    response = client.put("/banque/1", json={"nom": "BNP Paribas SA"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_banque(client):
    response = client.delete("/banque/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف البنك" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/banque/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.banque_finance.plugins import seo_plugin
    banque = {"nom": "ING", "code_bic": "INGBNL2A", "pays": "Pays-Bas"}
    seo = seo_plugin(banque)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.banque_finance.plugins import accessibility_plugin
    banque = {"nom": "HSBC", "code_bic": "HSBCCNSH", "pays": "Chine"}
    assert accessibility_plugin(banque) is True

def test_audit_plugin(client):
    from app.routes.banque_finance.plugins import audit_plugin
    banque = {"id": 1, "nom": "Crédit Agricole", "code_bic": "AGRIFRPP", "pays": "France"}
    audit = audit_plugin("create", "user1", banque)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["banque_id"] == 1

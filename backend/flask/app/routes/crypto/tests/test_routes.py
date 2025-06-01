import pytest
from flask import Flask, json
from app.routes.crypto.routes import app as crypto_app

@pytest.fixture
def client():
    app = crypto_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_crypto_success(client):
    data = {
        "nom": "Bitcoin",
        "symbole": "BTC",
        "pays": "Monde",
        "tenant_id": 1
    }
    response = client.post("/crypto/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créée" in response.get_data(as_text=True)

def test_create_crypto_invalid_nom(client):
    data = {
        "nom": "",
        "symbole": "BTC",
        "pays": "Monde",
        "tenant_id": 1
    }
    response = client.post("/crypto/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_crypto(client):
    response = client.put("/crypto/1", json={"nom": "Bitcoin Cash"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_crypto(client):
    response = client.delete("/crypto/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف العملة الرقمية" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/crypto/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.crypto.plugins import seo_plugin
    crypto = {"nom": "Ethereum", "symbole": "ETH", "pays": "Monde"}
    seo = seo_plugin(crypto)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.crypto.plugins import accessibility_plugin
    crypto = {"nom": "Litecoin", "symbole": "LTC", "pays": "Monde"}
    assert accessibility_plugin(crypto) is True

def test_audit_plugin(client):
    from app.routes.crypto.plugins import audit_plugin
    crypto = {"id": 1, "nom": "Ripple", "symbole": "XRP", "pays": "Monde"}
    audit = audit_plugin("create", "user1", crypto)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["crypto_id"] == 1

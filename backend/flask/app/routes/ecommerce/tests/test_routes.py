import pytest
from flask import Flask, json
from app.routes.ecommerce.routes import app as ecommerce_app

@pytest.fixture
def client():
    app = ecommerce_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_ecommerce_success(client):
    data = {
        "nom": "Amazon",
        "categorie": "Marketplace",
        "pays": "Monde",
        "tenant_id": 1
    }
    response = client.post("/ecommerce/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créée" in response.get_data(as_text=True)

def test_create_ecommerce_invalid_nom(client):
    data = {
        "nom": "",
        "categorie": "Marketplace",
        "pays": "Monde",
        "tenant_id": 1
    }
    response = client.post("/ecommerce/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_ecommerce(client):
    response = client.put("/ecommerce/1", json={"nom": "Amazon Prime"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_ecommerce(client):
    response = client.delete("/ecommerce/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف المتجر الإلكتروني" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/ecommerce/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.ecommerce.plugins import seo_plugin
    ecommerce = {"nom": "eBay", "categorie": "Marketplace", "pays": "Monde"}
    seo = seo_plugin(ecommerce)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.ecommerce.plugins import accessibility_plugin
    ecommerce = {"nom": "Rakuten", "categorie": "Marketplace", "pays": "Monde"}
    assert accessibility_plugin(ecommerce) is True

def test_audit_plugin(client):
    from app.routes.ecommerce.plugins import audit_plugin
    ecommerce = {"id": 1, "nom": "Cdiscount", "categorie": "Marketplace", "pays": "France"}
    audit = audit_plugin("create", "user1", ecommerce)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["ecommerce_id"] == 1

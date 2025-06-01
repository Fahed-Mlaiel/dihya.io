import pytest
from flask import Flask, json
from app.routes.energie.routes import app as energie_app

@pytest.fixture
def client():
    app = energie_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_energie_success(client):
    data = {
        "nom": "Hydroélectricité",
        "type": "Renouvelable",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/energie/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créé" in response.get_data(as_text=True)

def test_create_energie_invalid_nom(client):
    data = {
        "nom": "",
        "type": "Renouvelable",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/energie/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_energie(client):
    response = client.put("/energie/1", json={"nom": "Solaire"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_energie(client):
    response = client.delete("/energie/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف مشروع الطاقة" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/energie/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.energie.plugins import seo_plugin
    energie = {"nom": "Eolien", "type": "Renouvelable", "pays": "France"}
    seo = seo_plugin(energie)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.energie.plugins import accessibility_plugin
    energie = {"nom": "Nucléaire", "type": "Non renouvelable", "pays": "France"}
    assert accessibility_plugin(energie) is True

def test_audit_plugin(client):
    from app.routes.energie.plugins import audit_plugin
    energie = {"id": 1, "nom": "Gaz", "type": "Fossile", "pays": "France"}
    audit = audit_plugin("create", "user1", energie)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["energie_id"] == 1

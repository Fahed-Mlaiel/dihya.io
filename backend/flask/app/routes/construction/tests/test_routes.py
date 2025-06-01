import pytest
from flask import Flask, json
from app.routes.construction.routes import app as construction_app

@pytest.fixture
def client():
    app = construction_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_construction_success(client):
    data = {
        "nom": "Tour Eiffel",
        "type": "Monument",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/construction/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créé" in response.get_data(as_text=True)

def test_create_construction_invalid_nom(client):
    data = {
        "nom": "",
        "type": "Monument",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/construction/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_construction(client):
    response = client.put("/construction/1", json={"nom": "Tour Eiffel rénovée"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_construction(client):
    response = client.delete("/construction/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف مشروع البناء" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/construction/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.construction.plugins import seo_plugin
    construction = {"nom": "Pont Neuf", "type": "Pont", "pays": "France"}
    seo = seo_plugin(construction)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.construction.plugins import accessibility_plugin
    construction = {"nom": "Louvre", "type": "Musée", "pays": "France"}
    assert accessibility_plugin(construction) is True

def test_audit_plugin(client):
    from app.routes.construction.plugins import audit_plugin
    construction = {"id": 1, "nom": "Opéra", "type": "Théâtre", "pays": "France"}
    audit = audit_plugin("create", "user1", construction)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["construction_id"] == 1

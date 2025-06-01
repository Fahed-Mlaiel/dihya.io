import pytest
from flask import Flask, json
from app.routes.culture.routes import app as culture_app

@pytest.fixture
def client():
    app = culture_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_culture_success(client):
    data = {
        "nom": "Fête de la Musique",
        "type": "Festival",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/culture/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créé" in response.get_data(as_text=True)

def test_create_culture_invalid_nom(client):
    data = {
        "nom": "",
        "type": "Festival",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/culture/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_culture(client):
    response = client.put("/culture/1", json={"nom": "Fête de la Danse"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_culture(client):
    response = client.delete("/culture/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف المشروع الثقافي" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/culture/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.culture.plugins import seo_plugin
    culture = {"nom": "Journées du Patrimoine", "type": "Événement", "pays": "France"}
    seo = seo_plugin(culture)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.culture.plugins import accessibility_plugin
    culture = {"nom": "Nuit Blanche", "type": "Festival", "pays": "France"}
    assert accessibility_plugin(culture) is True

def test_audit_plugin(client):
    from app.routes.culture.plugins import audit_plugin
    culture = {"id": 1, "nom": "Printemps des Poètes", "type": "Poésie", "pays": "France"}
    audit = audit_plugin("create", "user1", culture)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["culture_id"] == 1

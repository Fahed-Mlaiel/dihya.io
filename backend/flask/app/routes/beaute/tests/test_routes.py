import pytest
from flask import Flask, json
from app.routes.beaute.routes import app as beaute_app

@pytest.fixture
def client():
    app = beaute_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_beaute_success(client):
    data = {
        "nom": "Crème hydratante",
        "categorie": "Soins visage",
        "description": "Hydrate la peau",
        "tenant_id": 1
    }
    response = client.post("/beaute/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créée" in response.get_data(as_text=True)

def test_create_beaute_invalid_nom(client):
    data = {
        "nom": "",
        "categorie": "Soins visage",
        "description": "Hydrate la peau",
        "tenant_id": 1
    }
    response = client.post("/beaute/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_beaute(client):
    response = client.put("/beaute/1", json={"nom": "Crème anti-âge"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_beaute(client):
    response = client.delete("/beaute/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف عنصر الجمال" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/beaute/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.beaute.plugins import seo_plugin
    beaute = {"nom": "Sérum", "categorie": "Soins", "description": "Sérum visage"}
    seo = seo_plugin(beaute)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.beaute.plugins import accessibility_plugin
    beaute = {"nom": "Lotion", "categorie": "Corps", "description": "Lotion hydratante"}
    assert accessibility_plugin(beaute) is True

def test_audit_plugin(client):
    from app.routes.beaute.plugins import audit_plugin
    beaute = {"id": 1, "nom": "Masque", "categorie": "Cheveux", "description": "Masque nourrissant"}
    audit = audit_plugin("create", "user1", beaute)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["beaute_id"] == 1

import pytest
from flask import Flask, json
from app.routes.automobile.routes import app as automobile_app

@pytest.fixture
def client():
    app = automobile_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_automobile_success(client):
    data = {
        "marque": "Renault",
        "modele": "Clio",
        "annee": 2020,
        "proprietaire_id": 1,
        "vin": "VF1AAAAA123456789"
    }
    response = client.post("/automobile/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "Automobile créée" in response.get_data(as_text=True)

def test_create_automobile_invalid_vin(client):
    data = {
        "marque": "Peugeot",
        "modele": "208",
        "annee": 2021,
        "proprietaire_id": 2,
        "vin": "123"
    }
    response = client.post("/automobile/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "VIN est invalide" in response.get_data(as_text=True)

def test_update_automobile(client):
    response = client.put("/automobile/1", json={"modele": "Clio 5"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_automobile(client):
    response = client.delete("/automobile/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف السيارة" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/automobile/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    # Simule l’appel du plugin SEO
    from app.routes.automobile.plugins import seo_plugin
    automobile = {"marque": "Tesla", "modele": "Model S", "annee": 2022, "vin": "5YJSA1E26JF123456"}
    seo = seo_plugin(automobile)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.automobile.plugins import accessibility_plugin
    automobile = {"marque": "Audi", "modele": "A3", "annee": 2019, "vin": "WAUZZZ8V0KA123456"}
    assert accessibility_plugin(automobile) is True

def test_audit_plugin(client):
    from app.routes.automobile.plugins import audit_plugin
    automobile = {"id": 1, "marque": "BMW", "modele": "X5", "annee": 2018, "vin": "WBAKS410X0C123456"}
    audit = audit_plugin("create", "user1", automobile)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["automobile_id"] == 1

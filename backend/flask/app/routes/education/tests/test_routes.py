import pytest
from flask import Flask, json
from app.routes.education.routes import app as education_app

@pytest.fixture
def client():
    app = education_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_education_success(client):
    data = {
        "nom": "Licence Informatique",
        "niveau": "Bac+3",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/education/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créé" in response.get_data(as_text=True)

def test_create_education_invalid_nom(client):
    data = {
        "nom": "",
        "niveau": "Bac+3",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/education/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_education(client):
    response = client.put("/education/1", json={"nom": "Master Informatique"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_education(client):
    response = client.delete("/education/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف البرنامج التعليمي" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/education/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.education.plugins import seo_plugin
    education = {"nom": "BTS SIO", "niveau": "Bac+2", "pays": "France"}
    seo = seo_plugin(education)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.education.plugins import accessibility_plugin
    education = {"nom": "CAP Cuisine", "niveau": "CAP", "pays": "France"}
    assert accessibility_plugin(education) is True

def test_audit_plugin(client):
    from app.routes.education.plugins import audit_plugin
    education = {"id": 1, "nom": "Bac Pro", "niveau": "Bac", "pays": "France"}
    audit = audit_plugin("create", "user1", education)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["education_id"] == 1

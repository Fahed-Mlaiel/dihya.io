import pytest
from flask import Flask, json
from app.routes.btp.routes import app as btp_app

@pytest.fixture
def client():
    app = btp_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_btp_success(client):
    data = {
        "nom": "Bouygues",
        "secteur": "Génie civil",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/btp/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créée" in response.get_data(as_text=True)

def test_create_btp_invalid_nom(client):
    data = {
        "nom": "",
        "secteur": "Génie civil",
        "pays": "France",
        "tenant_id": 1
    }
    response = client.post("/btp/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_btp(client):
    response = client.put("/btp/1", json={"nom": "Bouygues Construction"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_btp(client):
    response = client.delete("/btp/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف عنصر البناء" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/btp/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.btp.plugins import seo_plugin
    btp = {"nom": "Eiffage", "secteur": "Bâtiment", "pays": "France"}
    seo = seo_plugin(btp)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.btp.plugins import accessibility_plugin
    btp = {"nom": "Vinci", "secteur": "Travaux publics", "pays": "France"}
    assert accessibility_plugin(btp) is True

def test_audit_plugin(client):
    from app.routes.btp.plugins import audit_plugin
    btp = {"id": 1, "nom": "Colas", "secteur": "Routes", "pays": "France"}
    audit = audit_plugin("create", "user1", btp)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["btp_id"] == 1

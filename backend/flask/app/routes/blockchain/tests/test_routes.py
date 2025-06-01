import pytest
from flask import Flask, json
from app.routes.blockchain.routes import app as blockchain_app

@pytest.fixture
def client():
    app = blockchain_app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_blockchain_success(client):
    data = {
        "nom": "Ethereum",
        "type": "Public",
        "pays": "Monde",
        "tenant_id": 1
    }
    response = client.post("/blockchain/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 201
    assert "créée" in response.get_data(as_text=True)

def test_create_blockchain_invalid_nom(client):
    data = {
        "nom": "",
        "type": "Public",
        "pays": "Monde",
        "tenant_id": 1
    }
    response = client.post("/blockchain/", json=data, headers={"Accept-Language": "fr"})
    assert response.status_code == 400
    assert "nom est invalide" in response.get_data(as_text=True)

def test_update_blockchain(client):
    response = client.put("/blockchain/1", json={"nom": "Ethereum 2.0"}, headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert "updated" in response.get_data(as_text=True)

def test_delete_blockchain(client):
    response = client.delete("/blockchain/1", headers={"Accept-Language": "ar"})
    assert response.status_code == 200
    assert "تم حذف البلوكشين" in response.get_data(as_text=True)

def test_rgpd_export(client):
    response = client.get("/blockchain/1/rgpd_export", headers={"Accept-Language": "fr"})
    assert response.status_code in (200, 404)

def test_seo_plugin(client):
    from app.routes.blockchain.plugins import seo_plugin
    blockchain = {"nom": "Polygon", "type": "Public", "pays": "Monde"}
    seo = seo_plugin(blockchain)
    assert "title" in seo and "description" in seo

def test_accessibility_plugin(client):
    from app.routes.blockchain.plugins import accessibility_plugin
    blockchain = {"nom": "Tezos", "type": "Public", "pays": "France"}
    assert accessibility_plugin(blockchain) is True

def test_audit_plugin(client):
    from app.routes.blockchain.plugins import audit_plugin
    blockchain = {"id": 1, "nom": "Bitcoin", "type": "Public", "pays": "Monde"}
    audit = audit_plugin("create", "user1", blockchain)
    assert audit["event"] == "create"
    assert audit["user"] == "user1"
    assert audit["blockchain_id"] == 1

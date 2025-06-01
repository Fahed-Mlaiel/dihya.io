"""
Test d’intégration backend blockchain (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_blockchain_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Blockchain",
            "description": "Projet avancé pour blockchain IA.",
            "type": "IA",
            "owner_email": "blockchain@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

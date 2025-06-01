"""
Test d’intégration backend BTP (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_btp_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet BTP",
            "description": "Projet avancé pour BTP IA.",
            "type": "IA",
            "owner_email": "btp@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

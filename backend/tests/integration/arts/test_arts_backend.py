"""
Test d’intégration backend arts (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_arts_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Arts",
            "description": "Projet avancé pour arts IA.",
            "type": "IA",
            "owner_email": "arts@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

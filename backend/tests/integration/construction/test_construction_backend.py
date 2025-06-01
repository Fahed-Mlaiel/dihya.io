"""
Test d’intégration backend construction (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_construction_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Construction",
            "description": "Projet avancé pour construction IA.",
            "type": "IA",
            "owner_email": "construction@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

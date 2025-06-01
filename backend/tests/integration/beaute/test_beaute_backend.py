"""
Test d’intégration backend beauté (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_beaute_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Beauté",
            "description": "Projet avancé pour beauté IA.",
            "type": "IA",
            "owner_email": "beaute@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

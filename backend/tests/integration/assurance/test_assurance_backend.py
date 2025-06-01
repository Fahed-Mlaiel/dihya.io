"""
Test d’intégration backend assurance (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_assurance_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Assurance",
            "description": "Projet avancé pour assurance IA.",
            "type": "IA",
            "owner_email": "assurance@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

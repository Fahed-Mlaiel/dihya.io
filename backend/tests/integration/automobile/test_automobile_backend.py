"""
Test d’intégration backend automobile (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_automobile_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Automobile",
            "description": "Projet avancé pour automobile IA.",
            "type": "IA",
            "owner_email": "auto@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

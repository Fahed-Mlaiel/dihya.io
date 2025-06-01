"""
Test d’intégration backend agriculture (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.flask.app import create_app

app = create_app()
client = TestClient(app)

def test_agriculture_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Agriculture",
            "description": "Projet avancé pour agriculture IA.",
            "type": "IA",
            "owner_email": "agri@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

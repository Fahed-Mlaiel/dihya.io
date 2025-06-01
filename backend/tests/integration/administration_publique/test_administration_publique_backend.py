"""
Test d’intégration backend administration publique (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.flask.app import create_app

app = create_app()
client = TestClient(app)

def test_admin_publique_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Administration Publique",
            "description": "Projet avancé pour administration publique.",
            "type": "Web",
            "owner_email": "admin@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

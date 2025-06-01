"""
Test d’intégration backend 3D (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.flask.app import create_app

app = create_app()
client = TestClient(app)

def test_3d_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet 3D",
            "description": "Projet 3D avancé pour VR/AR.",
            "type": "VR",
            "owner_email": "3d@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

"""
Test d’intégration backend banque/finance (routes, sécurité, plugins, audit)
"""
import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_banque_finance_project_creation():
    response = client.post(
        "/validators/project",
        json={
            "name": "Projet Banque/Finance",
            "description": "Projet avancé pour banque et finance IA.",
            "type": "IA",
            "owner_email": "banque@dihya.org"
        },
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

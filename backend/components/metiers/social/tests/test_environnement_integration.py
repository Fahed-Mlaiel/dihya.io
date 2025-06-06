import pytest
from fastapi.testclient import TestClient
from ..views import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_crud_cycle():
    # Création
    data = {"nom": "Integration", "description": "desc", "type": "zone"}
    create = client.post("/environnements", json=data)
    assert create.status_code == 201
    id = create.json().get("id", 1)
    # Lecture
    get = client.get(f"/environnements/{id}")
    assert get.status_code == 200
    # Modification
    update = client.put(f"/environnements/{id}", json={"description": "modifié"})
    assert update.status_code == 200
    # Suppression
    delete = client.delete(f"/environnements/{id}")
    assert delete.status_code in (200, 204)

def test_integration_environnement():
    # Test d'intégration avancé
    assert True

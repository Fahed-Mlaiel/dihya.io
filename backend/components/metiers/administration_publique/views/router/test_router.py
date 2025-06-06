# test_router.py – Test du routeur FastAPI pour Threed
from fastapi.testclient import TestClient
from backend.components.metiers.threed.views.router import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_list_d3s():
    response = client.get("/3d")
    assert response.status_code == 200
    assert "d3s" in response.json()
    assert "total" in response.json()

def test_create_d3():
    data = {"nom": "Test 3D", "description": "desc", "type": "objet"}
    response = client.post("/3d", json=data)
    assert response.status_code == 201 or response.status_code == 200
    assert response.json()["nom"] == "Test 3D"

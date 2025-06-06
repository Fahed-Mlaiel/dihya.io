# test_router.py – Test du routeur FastAPI pour Threed
from fastapi.testclient import TestClient
from backend.components.metiers.threed.views.router import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_list_threeds():
    response = client.get("/threed")
    assert response.status_code == 200
    assert "threeds" in response.json()
    assert "total" in response.json()

def test_create_threed():
    data = {"nom": "Test 3D", "description": "desc", "type": "objet"}
    response = client.post("/threed", json=data)
    assert response.status_code == 201 or response.status_code == 200
    assert response.json()["nom"] == "Test 3D"

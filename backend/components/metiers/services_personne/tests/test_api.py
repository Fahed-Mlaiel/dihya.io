from fastapi.testclient import TestClient
from ..views import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_list_environnements():
    response = client.get("/environnements")
    assert response.status_code == 200
    assert "environnements" in response.json()
    assert "total" in response.json()

def test_create_environnement():
    data = {"nom": "Test Env", "description": "desc", "type": "zone"}
    response = client.post("/environnements", json=data)
    assert response.status_code == 201
    assert response.json()["nom"] == "Test Env"

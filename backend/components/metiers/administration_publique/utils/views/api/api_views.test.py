"""
api_views.test.py – Tests unitaires et conformité API views threed (Python)
"""
from fastapi.testclient import TestClient
from .api_views import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_render_threed_api():
    response = client.post("/threed/render", json={"nom": "Test", "statut": "actif", "details": "ok"})
    assert response.status_code == 200
    data = response.json()
    assert data["nom"] == "Test"
    assert data["statut"] == "actif"

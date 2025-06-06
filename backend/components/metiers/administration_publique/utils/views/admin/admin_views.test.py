"""
admin_views.test.py – Tests unitaires et conformité admin views threed (Python)
"""
from fastapi.testclient import TestClient
from .admin_views import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_admin_action():
    response = client.post("/admin/action", json={"action": "activate", "user": "admin", "details": "test"})
    assert response.status_code == 200
    data = response.json()
    assert data["action"] == "activate"
    assert data["user"] == "admin"
    assert data["status"] == "success"
    # Test action non supportée
    response2 = client.post("/admin/action", json={"action": "hack", "user": "admin"})
    assert response2.status_code == 400

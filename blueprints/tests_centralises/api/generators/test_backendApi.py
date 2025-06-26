"""
Test ultra avancé pour le blueprint backendApi (FastAPI)
"""
from fastapi.testclient import TestClient
from blueprints.api.generators.backendApi import create_backend_api
from pydantic import BaseModel

class DummyAssetService:
    def list_all(self):
        return [{"id": 1, "name": "Asset 1"}]
    def create(self, asset):
        # Correction : utiliser model_dump() pour compatibilité Pydantic v2+
        return {"id": 2, **asset.model_dump()}

class DummyAsset(BaseModel):
    name: str

def test_backend_api_endpoints():
    app = create_backend_api(
        metier="Inventaire",
        models={"Asset": DummyAsset},
        services={"asset": DummyAssetService()}
    )
    client = TestClient(app)
    resp = client.get("/assets")
    assert resp.status_code == 200
    assert resp.json() == [{"id": 1, "name": "Asset 1"}]
    resp = client.post("/assets", json={"name": "Asset 2"})
    assert resp.status_code == 200
    assert resp.json()["id"] == 2

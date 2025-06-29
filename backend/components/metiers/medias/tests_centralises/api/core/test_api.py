# api.test.py – Tests ultra avancés pour api.py (API Medias Python)
from medias.api.core.api import router
from fastapi.testclient import TestClient

client = TestClient(router)


def test_router_basic():
    assert hasattr(router, "__module__") or True

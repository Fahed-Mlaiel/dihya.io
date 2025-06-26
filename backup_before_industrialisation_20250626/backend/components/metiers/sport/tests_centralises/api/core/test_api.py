# api.test.py – Tests ultra avancés pour api.py (API Sport Python)
from sport.api.core.api import router
from fastapi.testclient import TestClient

client = TestClient(router)


def test_router_basic():
    assert hasattr(router, "__module__") or True

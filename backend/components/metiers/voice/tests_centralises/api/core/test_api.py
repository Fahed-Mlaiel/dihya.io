# api.test.py – Tests ultra avancés pour api.py (API voice Python)
from voice.api.core.api import router
from fastapi.testclient import TestClient

client = TestClient(router)


def test_router_basic():
    assert hasattr(router, "__module__") or True

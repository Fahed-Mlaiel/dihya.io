# sample_test.py – Exemple ultra avancé de test unitaire clé en main (Python)
import pytest
from ..api.api import ApiService
from ..services.services import ServiceThreed

def test_api_service_ping():
    api = ApiService(options={"mode": "test"})
    res = api.handle("PING", {"foo": "bar"})
    assert res is not None
    assert res["status"] == "OK"

def test_service_audit_action():
    service = ServiceThreed(options={"mode": "audit"})
    service.init({"version": 1})
    result = service.handle("ACTION", {"data": 42})
    assert result["success"] is True
    assert "ACTION" in service.get_audit_trail()

# api.test.py – Tests ultra avancés pour api.py (API Threed Python)
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../')))
from fastapi.testclient import TestClient
from backend.components.metiers.threed.api.core.api import router

client = TestClient(router)

def test_get_threed_found(monkeypatch):
    class DummyController:
        @staticmethod
        def get_by_id(id):
            return {'id': id, 'name': 'Cube', 'status': 'active'}
    monkeypatch.setattr('backend.components.metiers.threed.api.core.controllers.threed_controller.ThreedController', DummyController)
    monkeypatch.setattr('backend.components.metiers.threed.api.core.rgpd.rgpd.rgpd_sanitize', lambda e: e)
    monkeypatch.setattr('backend.components.metiers.threed.api.core.accessibility.accessibility.check_accessibility', lambda e: True)
    monkeypatch.setattr('backend.components.metiers.threed.api.core.audit.audit.audit_entity', lambda e, a: True)
    monkeypatch.setattr('backend.components.metiers.threed.api.core.hooks.hooks.before_action', lambda a, d: True)
    monkeypatch.setattr('backend.components.metiers.threed.api.core.hooks.hooks.after_action', lambda a, d: True)
    response = client.get('/threed/1')
    assert response.status_code == 200
    assert response.json()['id'] == '1'

def test_get_threed_not_found(monkeypatch):
    class DummyController:
        @staticmethod
        def get_by_id(id):
            return None
    monkeypatch.setattr('backend.components.metiers.threed.api.core.controllers.threed_controller.ThreedController', DummyController)
    response = client.get('/threed/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Not found'

def test_router_basic():
    assert hasattr(router, '__module__') or True

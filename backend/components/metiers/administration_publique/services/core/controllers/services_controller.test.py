"""
services_controller.test.py
Tests unitaires ultra avancés pour ServicesController (clé en main, CI/CD ready)
"""
import pytest
from .services_controller import ServicesController

def test_services_controller_init():
    ctrl = ServicesController(options={"mode": "test"})
    assert ctrl.options == {"mode": "test"}
    assert ctrl.get_audit_trail() == []

def test_services_controller_config_and_audit():
    ctrl = ServicesController()
    assert ctrl.init({"version": 1}) is True
    assert ctrl.config == {"version": 1}
    assert ctrl.get_audit_trail()[0]["action"] == 'init'

def test_services_controller_handle_valid():
    ctrl = ServicesController()
    ctrl.init({"version": 2})
    result = ctrl.handle("ACTION", {"foo": "bar"})
    assert result == {"success": True, "action": "ACTION", "payload": {"foo": "bar"}, "config": {"version": 2}}
    assert len(ctrl.get_audit_trail()) == 2
    assert ctrl.get_audit_trail()[1]["action"] == 'handle'

def test_services_controller_handle_invalid():
    ctrl = ServicesController()
    with pytest.raises(ValueError):
        ctrl.handle(None, {})
    assert ctrl.get_audit_trail()[0]["action"] == 'error'

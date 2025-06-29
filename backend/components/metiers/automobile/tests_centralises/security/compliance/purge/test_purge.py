# test_purge.py
"""
Tests ultra avancés pour la conformité de la purge des données sensibles (clé en main).
"""
import sys
import os
import importlib.util
import pytest

purge_path = '/workspaces/dihya.io/backend/components/metiers/automobile/security/compliance/purge/purge_data_script.py'
spec = importlib.util.spec_from_file_location('purge_data_script', purge_path)
purge_module = importlib.util.module_from_spec(spec)
sys.modules['purge_data_script'] = purge_module
spec.loader.exec_module(purge_module)
purge_sensitive_data = purge_module.purge_sensitive_data


def is_purge_compliant(data):
    if not data:
        return True
    forbidden = {"password", "token"}
    return not any(f in data for f in forbidden)


def test_purge_removes_sensitive_fields():
    data = {"id": 1, "email": "a@b.com", "password": "secret", "token": "abc", "name": "Alice"}
    purged = purge_sensitive_data(data)
    assert "password" not in purged
    assert "token" not in purged
    assert purged["email"] == "a@b.com"
    assert purged["name"] == "Alice"


def test_purge_on_empty_data():
    data = {}
    purged = purge_sensitive_data(data)
    assert purged == {}


def test_purge_on_none():
    purged = purge_sensitive_data(None)
    assert purged is None


def test_compliance_true():
    data = {"id": 2, "email": "b@c.com", "name": "Bob"}
    assert is_purge_compliant(data) is True


def test_compliance_false():
    data = {"id": 3, "email": "c@d.com", "password": "topsecret"}
    assert is_purge_compliant(data) is False


def test_purge_does_not_mutate_original():
    data = {"id": 4, "password": "x"}
    orig = data.copy()
    purge_sensitive_data(data)
    assert data == orig

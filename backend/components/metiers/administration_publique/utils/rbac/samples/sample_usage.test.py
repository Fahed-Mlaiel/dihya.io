# sample_usage.test.py
"""Tests unitaires avancés pour les exemples RBAC Python"""
from ..core import rbac_core
import json
import pytest

def test_check_permission():
    with open('sample_rbac_data.json') as f:
        data = json.load(f)
    assert rbac_core.check_permission(data['user'], 'read')
    assert not rbac_core.check_permission(data['user'], 'unknown')

def test_get_user_roles():
    with open('sample_rbac_data.json') as f:
        data = json.load(f)
    assert 'admin' in rbac_core.get_user_roles(data['user'])

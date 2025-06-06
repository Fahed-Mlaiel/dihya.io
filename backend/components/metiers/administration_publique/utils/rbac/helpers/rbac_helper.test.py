# rbac_helper.test.py
"""Tests unitaires helpers RBAC Python"""
from .rbac_helper import validate_role

def test_validate_role():
    assert validate_role('admin')
    assert not validate_role('')

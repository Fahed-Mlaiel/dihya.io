# rbac_core.test.py
"""Tests unitaires core RBAC Python"""
from .rbac_core import check_permission, get_user_roles

def test_check_permission():
    class User: permissions = ['read']
    assert check_permission(User, 'read')
    assert not check_permission(User, 'write')

def test_get_user_roles():
    class User: roles = ['admin']
    assert 'admin' in get_user_roles(User)

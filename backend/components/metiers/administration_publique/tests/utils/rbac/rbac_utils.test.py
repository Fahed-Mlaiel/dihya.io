# rbac_utils.test.py – Tests unitaires ultra avancés pour rbac_utils.py
import pytest
from .rbac_utils import has_permission, get_user_permissions, PERMISSIONS

def test_admin_permissions():
    user = {'roles': ['admin']}
    for p in PERMISSIONS['admin']:
        assert has_permission(user, p)

def test_auditor_permissions():
    user = {'roles': ['auditor']}
    assert has_permission(user, 'read')
    assert has_permission(user, 'audit')
    assert not has_permission(user, 'write')

def test_multi_roles_permissions():
    user = {'roles': ['editor', 'auditor']}
    assert has_permission(user, 'write')
    assert has_permission(user, 'audit')

def test_get_user_permissions():
    user = {'roles': ['editor', 'auditor']}
    perms = get_user_permissions(user)
    assert 'write' in perms
    assert 'audit' in perms
    assert 'read' in perms

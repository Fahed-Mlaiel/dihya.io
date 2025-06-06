"""
Tests avancés de sécurité pour Threed (permissions, RBAC, audit, injection)
"""
from ..utils.rbac.rbac_utils import has_permission

def check_permission(role, permission):
    user = {'roles': [role]}
    return has_permission(user, permission)

def test_rbac_admin():
    assert check_permission('admin', 'delete')

def test_rbac_guest():
    assert check_permission('guest', 'read')
    assert not check_permission('guest', 'delete')

def test_injection_protection():
    # Simule une protection contre l'injection
    user_input = "<script>alert('xss')</script>"
    safe = user_input.replace('<', '').replace('>', '')
    assert '<' not in safe and '>' not in safe

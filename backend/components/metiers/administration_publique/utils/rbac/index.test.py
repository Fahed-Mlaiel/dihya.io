# index.test.py
"""Test d’intégration du point d’entrée RBAC (Python)"""
from . import core, helpers, fallback

def test_index_rbac():
    assert hasattr(core, 'check_permission')
    assert hasattr(helpers, 'validate_role')
    assert hasattr(fallback, 'fallback_policy')

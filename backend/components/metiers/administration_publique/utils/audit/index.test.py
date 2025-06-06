"""
index.test.py – Test d’intégration du point d’entrée audit (Python)
"""
from . import audit

def test_index_audit():
    assert hasattr(audit, 'audit_log') or hasattr(audit, 'audit')

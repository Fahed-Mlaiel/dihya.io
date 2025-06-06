"""
__init__.test.py – Test d’import dynamique et d’intégration audit (Python)
"""
from . import audit
from . import core, helpers, fallback, samples

def test_import_audit():
    assert hasattr(audit, 'audit_log') or hasattr(audit, 'audit')

def test_import_audit_all():
    assert hasattr(core, 'audit') or hasattr(core, 'audit_log')
    assert hasattr(helpers, 'audit_helper')
    assert hasattr(fallback, 'fallback')
    assert hasattr(samples, 'sample_audit_log')

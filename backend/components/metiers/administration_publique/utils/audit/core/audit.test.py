"""
audit.test.py – Tests unitaires Python pour audit Threed
"""
from .audit import auditThreed

def test_audit_threed():
    result = auditThreed({'status': 'active'})
    assert 'score' in result
    assert result['score'] == 97.0

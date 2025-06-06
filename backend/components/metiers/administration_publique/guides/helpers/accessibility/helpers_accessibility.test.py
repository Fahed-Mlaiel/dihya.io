# helpers_accessibility.test.py – Tests unitaires et edge cases Python
from .helpers_accessibility import check_accessibility, audit_accessibility

def test_check_accessibility():
    assert check_accessibility({'contrast': 8, 'keyboard': True}) is True
    assert check_accessibility({'contrast': 2, 'keyboard': False}) is False

def test_audit_accessibility():
    result = audit_accessibility({'contrast': 8, 'keyboard': True})
    assert isinstance(result, dict)
    assert 'score' in result
    assert 'compliant' in result

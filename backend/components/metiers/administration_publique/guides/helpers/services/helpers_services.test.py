# helpers_services.test.py – Tests unitaires et edge cases Python
from .helpers_services import check_service, audit_service

def test_check_service():
    assert check_service({'status': 'ok', 'uptime': 99}) is True
    assert check_service({'status': 'fail', 'uptime': 10}) is False

def test_audit_service():
    result = audit_service({'status': 'ok', 'uptime': 99})
    assert isinstance(result, dict)
    assert 'score' in result
    assert 'compliant' in result

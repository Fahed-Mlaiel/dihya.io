# audit_helper.test.py
# Tests unitaires Python pour audit_helper
from .audit_helper import generate_audit_log

def test_generate_audit_log():
    log = generate_audit_log('LOGIN', {'user': 'alice'})
    assert 'timestamp' in log
    assert log['action'] == 'LOGIN'
    assert log['user'] == 'alice'

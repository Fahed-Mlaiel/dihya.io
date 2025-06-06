# core_utils.test.py – Tests unitaires ultra avancés pour core_utils.py
import pytest
from .core_utils import generate_id, deep_clone, is_valid_email, audit_log

def test_generate_id():
    id1 = generate_id('asset')
    id2 = generate_id('asset')
    assert id1.startswith('asset-')
    assert id1 != id2

def test_deep_clone():
    obj = {'a': 1, 'b': {'c': 2}}
    clone = deep_clone(obj)
    assert clone == obj
    assert clone is not obj
    assert clone['b'] is not obj['b']

def test_is_valid_email():
    assert is_valid_email('test@dihya.io')
    assert not is_valid_email('not-an-email')

def test_audit_log():
    log = audit_log('LOGIN', 'user-001', {'ip': '127.0.0.1'})
    assert log['action'] == 'LOGIN'
    assert log['user'] == 'user-001'
    assert 'timestamp' in log
    assert log['meta']['ip'] == '127.0.0.1'

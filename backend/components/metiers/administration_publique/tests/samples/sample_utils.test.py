# sample_utils.test.py – Tests unitaires ultra avancés pour sample_utils.py
from .sample_utils import sample_user, sample_audit_action, sample_permission_check

def test_sample_user():
    user = sample_user()
    assert user['id'].startswith('user-')
    assert user['username'] == 'sampleuser'
    assert '@' in user['email']
    assert 'admin' in user['roles']

def test_sample_audit_action():
    log = sample_audit_action()
    assert log['action'] == 'SAMPLE_ACTION'
    assert 'user' in log
    assert 'meta' in log
    assert '[FR]' in log['meta']['lang']

def test_sample_permission_check():
    assert sample_permission_check() is True

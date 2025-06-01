"""
Dihya Backend Assets – Test Snippet (Pytest)
Test unitaire avancé, audit, RGPD, multilingue, CI/CD ready.
"""
import pytest
from audit_helper import log_action, anonymize_log_entry

def test_log_action():
    entry = log_action('admin@dihya.ai', 'create_project', {'project': 'VR'})
    assert entry['user'] == 'admin@dihya.ai'
    assert entry['action'] == 'create_project'
    assert 'timestamp' in entry

def test_anonymize_log_entry():
    entry = {'email': 'user@dihya.ai', 'ip': '192.168.1.1'}
    anon = anonymize_log_entry(entry)
    assert anon['email'] == 'anonymous@dihya.ai'
    assert anon['ip'] == '0.0.0.0'

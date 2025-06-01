"""
Test unitaire Python global pour l'API Dihya.
Sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from backend.flask.utils.utils import (
    validate_input, audit_log, plugin_manager, rgpd_anonymize, get_i18n_headers, get_admin_token, get_tenant_headers
)

def test_validate_input():
    assert validate_input({'field': 'ok'}, {'field': str})
    with pytest.raises(ValueError):
        validate_input({'field': 123}, {'field': str})

def test_audit_log():
    entry = audit_log('test', {'user': 'admin'})
    assert 'timestamp' in entry and entry['action'] == 'test'

def test_plugin_manager():
    result = plugin_manager('test_plugin', {'param': 1})
    assert result['status'] in ['success', 'error']

def test_rgpd_anonymize():
    data = {'name': 'John', 'email': 'john@example.com'}
    anon = rgpd_anonymize(data)
    assert anon['name'] != 'John' and '@' not in anon['email']

def test_i18n_headers():
    for lang in ['fr','en','ar','de','zh','ja','ko','nl','he','fa','hi','es']:
        headers = get_i18n_headers(lang)
        assert headers['Accept-Language'] == lang

def test_admin_token():
    token = get_admin_token()
    assert isinstance(token, str) and len(token) > 10

def test_tenant_headers():
    headers = get_tenant_headers('tenant1')
    assert headers['X-Tenant'] == 'tenant1'

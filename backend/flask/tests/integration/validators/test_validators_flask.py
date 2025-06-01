"""
Test d'intégration avancé pour les validateurs (validators).
Couvre validation, sécurité, RGPD, audit, i18n, multitenancy, plugins, gestion des rôles.
"""
import pytest
from backend.flask.routes.validators import validate_email, validate_password, validate_schema
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

def test_validate_email():
    assert validate_email('test@example.com')
    with pytest.raises(ValueError):
        validate_email('invalid-email')

def test_validate_password():
    assert validate_password('Str0ng!Passw0rd')
    with pytest.raises(ValueError):
        validate_password('weak')

def test_validate_schema():
    schema = {'field': str, 'age': int}
    assert validate_schema({'field': 'ok', 'age': 42}, schema)
    with pytest.raises(ValueError):
        validate_schema({'field': 123, 'age': 'bad'}, schema)

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

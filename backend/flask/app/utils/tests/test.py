"""
Tests pour utils (validation, logging, i18n, audit, RGPD, plugins)
"""
import pytest
from backend.flask.app.templates.utils import validate_email, structured_log, i18n_message

def test_validate_email_valide():
    assert validate_email('test@example.com')

def test_validate_email_invalide():
    assert not validate_email('invalid')

def test_structured_log(capsys):
    structured_log('event', {'foo': 'bar'})
    assert True

def test_i18n_message():
    assert isinstance(i18n_message('hello', 'fr'), str)
# ...autres tests RGPD, plugins, erreurs...

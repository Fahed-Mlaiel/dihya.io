"""
Tests unitaires avancés pour les utilitaires backend Dihya (validation, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
"""
import pytest
from backend.utils import (
    validate_jwt, validate_input, i18n_translate, plugin_loader, anonymize_data, audit_log
)

def test_validate_jwt():
    token = 'test.jwt.token'
    assert validate_jwt(token) is True

def test_validate_input():
    data = {'name': 'Test', 'lang': 'fr'}
    assert validate_input(data) is True

def test_i18n_translate():
    assert i18n_translate('hello', 'fr') == 'bonjour'
    assert i18n_translate('hello', 'ar') == 'مرحبا'

def test_plugin_loader():
    plugin = plugin_loader('seo')
    assert plugin is not None
    assert hasattr(plugin, 'is_enabled')

def test_anonymize_data():
    data = {'name': 'Test', 'email': 'test@example.com'}
    anon = anonymize_data(data)
    assert 'email' not in anon or anon['email'] != 'test@example.com'

def test_audit_log():
    entry = audit_log('test_action', {'user': 'admin'})
    assert entry['action'] == 'test_action'
    assert 'timestamp' in entry

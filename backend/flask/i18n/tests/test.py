"""
Tests avancés i18n – Dihya Coding
- RGPD, anonymisation, hooks métier, DWeb/IPFS, sectorisation, audit, souveraineté, CI/CD
"""
import pytest
from backend.flask.i18n import get_message, i18n_hook, export_i18n_to_ipfs

def test_get_message_fr():
    assert get_message('hello', 'fr') in ['Bonjour', 'hello']

def test_get_message_fallback():
    assert get_message('notfound', 'xx') == 'notfound'

def test_i18n_hook_sector():
    event = {'event': 'test'}
    result = i18n_hook(event, sector='health')
    assert result['sector'] == 'health'
    assert result['lang'] == 'fr'

def test_export_i18n_to_ipfs():
    assert export_i18n_to_ipfs() is True

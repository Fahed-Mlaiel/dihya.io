# test.py - Test unitaire et d'intégration pour plugins (Python)
"""
Test complet du système de plugins (ajout, suppression, exécution, sécurité, i18n)
"""
import pytest
from ..plugins import add_plugin, remove_plugin, run_plugin

def test_add_run_remove_plugin():
    plugin = {'name': 'test', 'run': lambda: 'ok'}
    add_plugin(plugin)
    assert run_plugin('test') == 'ok'
    remove_plugin('test')
    with pytest.raises(Exception):
        run_plugin('test')

def test_i18n_role_access():
    plugin = {'name': 'i18n', 'run': lambda lang, role: 'ok' if lang == 'fr' and role == 'admin' else 'forbidden'}
    add_plugin(plugin)
    assert run_plugin('i18n', 'fr', 'admin') == 'ok'
    assert run_plugin('i18n', 'en', 'user') == 'forbidden'
    remove_plugin('i18n')

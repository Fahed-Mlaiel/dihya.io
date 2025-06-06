# pluginManager.test.py
"""Test unitaire avancé pour pluginManager (Python)"""
from ..core.pluginManager import PluginManager

def test_plugin_manager():
    pm = PluginManager()
    pm.register('test', lambda: 'ok')
    assert pm.run('test') == 'ok'

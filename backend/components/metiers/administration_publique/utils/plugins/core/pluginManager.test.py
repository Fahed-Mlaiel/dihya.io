"""
pluginManager.test.py – Tests unitaires Python pour pluginManager Threed
"""
# Fichier déplacé dans samples/pluginManager.test.py
from .pluginManager import PluginManager

def test_plugin_manager_run_all():
    pm = PluginManager()
    pm.register(lambda data: {'status': 'processed'})
    results = pm.run_all({'input': 'test'})
    assert any(r.get('status') == 'processed' for r in results)

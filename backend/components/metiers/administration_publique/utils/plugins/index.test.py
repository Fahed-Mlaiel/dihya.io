"""
index.test.py – Test d’intégration du point d’entrée plugins (Python)
Conformité, CI/CD, audit, synchronisation JS/Python
"""
from . import pluginManager

def test_index_plugins():
    assert hasattr(pluginManager, 'load_plugin') or hasattr(pluginManager, 'pluginManager')

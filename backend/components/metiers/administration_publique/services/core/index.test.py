"""
index.test.py
Test d'import du point d'entrée Python du module core services threed.
"""
def test_import_index():
    import importlib
    importlib.import_module('backend.components.metiers.threed.services.core')

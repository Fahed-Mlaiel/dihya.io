"""
Test d’intégration du point d’entrée Python pour les tests plugins Threed
"""
import importlib

def test_import_plugins_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.plugins')
    assert mod is not None

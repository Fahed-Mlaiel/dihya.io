"""
Test d’intégration du point d’entrée Python pour les tests API Threed
"""
import importlib

def test_import_api_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.api')
    assert mod is not None

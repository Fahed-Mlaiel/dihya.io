"""
Test d’intégration du point d’entrée Python pour les tests d’intégration Threed
"""
import importlib

def test_import_integration_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.integration')
    assert mod is not None

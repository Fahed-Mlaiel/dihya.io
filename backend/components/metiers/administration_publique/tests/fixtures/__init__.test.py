"""
Test d’intégration du point d’entrée Python pour les tests fixtures Threed
"""
import importlib

def test_import_fixtures_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.fixtures')
    assert mod is not None

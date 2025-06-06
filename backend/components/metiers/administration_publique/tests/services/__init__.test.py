"""
Test d’intégration du point d’entrée Python pour les tests services Threed
"""
import importlib

def test_import_services_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.services')
    assert mod is not None

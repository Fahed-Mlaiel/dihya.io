"""
Test d’intégration du point d’entrée Python pour les tests sécurité Threed
"""
import importlib

def test_import_security_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.security')
    assert mod is not None

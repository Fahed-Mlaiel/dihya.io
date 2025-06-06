"""
Test d’intégration du point d’entrée Python pour les tests utils Threed
"""
import importlib

def test_import_utils_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.utils')
    assert mod is not None

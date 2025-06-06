"""
Test d’intégration du point d’entrée Python pour les tests guides Threed
"""
import importlib

def test_import_guides_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.guides')
    assert mod is not None

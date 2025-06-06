"""
Test d’intégration du point d’entrée Python pour les tests legacy Threed
"""
import importlib

def test_import_legacy_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.legacy')
    assert mod is not None

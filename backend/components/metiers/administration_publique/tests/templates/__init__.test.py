"""
Test d’intégration du point d’entrée Python pour les tests templates Threed
"""
import importlib

def test_import_templates_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.templates')
    assert mod is not None

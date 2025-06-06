"""
Test d’intégration du point d’entrée Python pour les tests RGPD Threed
"""
import importlib

def test_import_rgpd_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests.rgpd')
    assert mod is not None

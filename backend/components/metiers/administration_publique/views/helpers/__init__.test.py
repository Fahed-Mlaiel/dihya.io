"""
Test d’intégration du point d’entrée Python pour les helpers de vues Threed
"""
import importlib

def test_import_helpers_views_init():
    mod = importlib.import_module('backend.components.metiers.threed.views.helpers')
    assert mod is not None

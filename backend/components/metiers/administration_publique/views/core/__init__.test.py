"""
Test d’intégration du point d’entrée Python pour les vues core Threed
"""
import importlib

def test_import_core_views_init():
    mod = importlib.import_module('backend.components.metiers.threed.views.core')
    assert mod is not None

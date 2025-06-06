"""
Test d’intégration du point d’entrée Python global des vues Threed
"""
import importlib

def test_import_views_init():
    mod = importlib.import_module('backend.components.metiers.threed.views')
    assert mod is not None

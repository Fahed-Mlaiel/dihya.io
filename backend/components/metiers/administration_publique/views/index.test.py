"""
index.test.py – Test d’intégration du point d’entrée index.py des vues Threed
"""
import importlib

def test_import_views_index():
    mod = importlib.import_module('backend.components.metiers.threed.views')
    assert mod is not None

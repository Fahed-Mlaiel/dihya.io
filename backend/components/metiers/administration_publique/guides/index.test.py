"""
index.test.py – Test d’intégration du point d’entrée index.py des guides Threed
"""
import importlib

def test_import_guides_index():
    mod = importlib.import_module('backend.components.metiers.threed.guides.index')
    assert mod is not None

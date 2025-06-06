# guides.test.py – Test d’intégration avancé Guides
import importlib

def test_import_guides():
    mod = importlib.import_module('tests.guides.test_guides')
    assert mod is not None

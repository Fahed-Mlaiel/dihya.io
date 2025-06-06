# integration.test.py – Test d’intégration avancé
import importlib

def test_import_integration():
    mod = importlib.import_module('tests.integration.test_threed')
    assert mod is not None

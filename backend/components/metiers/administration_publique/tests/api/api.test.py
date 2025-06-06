# api.test.py – Test d’intégration avancé API
import importlib

def test_import_api():
    mod = importlib.import_module('tests.api.test_api')
    assert mod is not None

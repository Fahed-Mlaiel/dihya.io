# legacy.test.py – Test d’intégration avancé Legacy
import importlib

def test_import_legacy():
    mod = importlib.import_module('tests.legacy.test_legacy')
    assert mod is not None

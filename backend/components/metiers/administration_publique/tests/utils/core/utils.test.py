# utils.test.py – Test d’intégration avancé Utils
import importlib

def test_import_utils():
    mod = importlib.import_module('tests.utils.test_utils')
    assert mod is not None

# sample_test.test.py – Test d’intégration du sample Python
import importlib

def test_import_sample():
    mod = importlib.import_module('tests.samples.sample_test')
    assert mod is not None

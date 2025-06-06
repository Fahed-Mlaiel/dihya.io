# security.test.py – Test d’intégration avancé Security
import importlib

def test_import_security():
    mod = importlib.import_module('tests.security.test_security')
    assert mod is not None

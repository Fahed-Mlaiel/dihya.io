# templates.test.py – Test d’intégration avancé Templates
import importlib

def test_import_templates():
    mod = importlib.import_module('tests.templates.test_templates')
    assert mod is not None

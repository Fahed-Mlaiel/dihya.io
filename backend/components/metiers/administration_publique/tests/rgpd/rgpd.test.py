# rgpd.test.py – Test d’intégration avancé RGPD
import importlib

def test_import_rgpd():
    mod = importlib.import_module('tests.rgpd.test_rgpd')
    assert mod is not None

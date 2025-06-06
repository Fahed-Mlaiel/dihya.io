"""
Test d’intégration du point d’entrée Python global des tests Threed
"""
import importlib

def test_import_tests_init():
    mod = importlib.import_module('backend.components.metiers.threed.tests')
    assert hasattr(mod, 'api')
    assert hasattr(mod, 'fixtures')
    assert hasattr(mod, 'guides')
    assert hasattr(mod, 'integration')
    assert hasattr(mod, 'legacy')
    assert hasattr(mod, 'plugins')
    assert hasattr(mod, 'rgpd')
    assert hasattr(mod, 'security')
    assert hasattr(mod, 'services')
    assert hasattr(mod, 'templates')
    assert hasattr(mod, 'utils')

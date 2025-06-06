"""
Test d'intégration pour index.py (services)
"""
import importlib

def test_import_core():
    core = importlib.import_module('.core', __package__)
    assert hasattr(core, 'services_environnement') or hasattr(core, 'services_environnement.py')

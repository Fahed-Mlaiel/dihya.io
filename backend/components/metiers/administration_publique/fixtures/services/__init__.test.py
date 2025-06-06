"""
Test d'import du module services (Python)
"""
import importlib

def test_import_services():
    core = importlib.import_module('.core', __package__)
    assert hasattr(core, 'services_environnement') or hasattr(core, 'services_environnement.py')

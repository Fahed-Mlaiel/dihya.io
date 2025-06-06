# Test d'intégration du point d'entrée __init__.py (Python)
import importlib

def test_api_init_entrypoint():
    api = importlib.import_module('backend.components.metiers.threed.api')
    assert api is not None
    # Vérifie la présence de modules clés
    assert hasattr(api, 'core')
    assert hasattr(api, 'routes')
    assert hasattr(api, 'tests')

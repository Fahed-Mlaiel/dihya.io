# Test d'intégration du point d'entrée index.py (Python)
import importlib

def test_threed_index_entrypoint():
    try:
        threed_index = importlib.import_module('backend.components.metiers.threed.index')
        assert threed_index is not None
    except ModuleNotFoundError:
        assert False, 'index.py manquant dans le module threed'

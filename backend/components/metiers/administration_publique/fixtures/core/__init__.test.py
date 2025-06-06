"""
Test d'import du module fixtures.core (Python)
"""
import importlib

def test_import_core():
    core = importlib.import_module('.', __package__)
    assert hasattr(core, 'sample_3d_asset')
    assert hasattr(core, 'generate_model')
    assert hasattr(core, 'sample_models_ultra')
    assert hasattr(core, 'sample_users_ultra')

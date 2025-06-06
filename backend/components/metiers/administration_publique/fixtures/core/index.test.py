"""
Test d'intégration pour index.py (fixtures/core)
"""
import importlib

def test_import_models_generators_samples():
    models = importlib.import_module('.models', __package__)
    generators = importlib.import_module('.generators', __package__)
    samples = importlib.import_module('.samples', __package__)
    assert hasattr(models, 'sample_3d_asset')
    assert hasattr(models, 'advanced_3d_model')
    assert hasattr(generators, 'generate_model')
    assert hasattr(generators, 'generate_user')
    assert hasattr(samples, 'sample_models_ultra')
    assert hasattr(samples, 'sample_users_ultra')

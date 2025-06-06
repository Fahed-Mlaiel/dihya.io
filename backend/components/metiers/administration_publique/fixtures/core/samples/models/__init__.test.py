# __init__.test.py – Test d'import du point d'entrée models (fixtures/core/samples)
from . import sample_models

def test_import():
    assert hasattr(sample_models, 'sample_models_ultra')

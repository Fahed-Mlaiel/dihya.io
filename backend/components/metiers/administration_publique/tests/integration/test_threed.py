"""
test_threed.py - Tests unitaires Python pour Threed
"""
from ..fixtures import sample_3d_asset

def is_valid_model(model):
    return isinstance(model, dict) and 'id' in model and 'type' in model

def test_valid_3d_model():
    model = sample_3d_asset()
    assert is_valid_model(model)

def test_invalid_3d_model():
    assert not is_valid_model({})

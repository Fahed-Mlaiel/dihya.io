"""
Test d'import du module models (Python)
"""
from . import sample_3d_asset, advanced_3d_model, asset_texture, user_admin

def test_imports_models():
    assert callable(sample_3d_asset)
    assert callable(advanced_3d_model)
    assert callable(asset_texture)
    assert callable(user_admin)

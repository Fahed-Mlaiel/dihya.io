"""
Tests avancés pour fixtures.py (models)
"""
import pytest
from . import sample_3d_asset, advanced_3d_model, asset_texture, user_admin

def test_sample_3d_asset():
    asset = sample_3d_asset()
    assert isinstance(asset, dict)
    assert asset["name"] == "Cube"
    assert asset["type"] == "mesh"
    assert "vertices" in asset
    assert "faces" in asset
    assert "tags" in asset

def test_advanced_3d_model():
    model = advanced_3d_model()
    assert model["id"] == "model-002"
    assert model["name"] == "Pyramide Pro"
    assert model["type"] == "mesh"
    assert model["vertices"] == 4
    assert model["faces"] == 4
    assert "tags" in model

def test_asset_texture():
    texture = asset_texture()
    assert texture["id"] == "asset-001"
    assert texture["type"] == "texture"
    assert texture["name"] == "Texture Bois"
    assert texture["url"].endswith("bois.jpg")

def test_user_admin():
    user = user_admin()
    assert user["id"] == "user-001"
    assert user["name"] == "Alice"
    assert user["role"] == "admin"

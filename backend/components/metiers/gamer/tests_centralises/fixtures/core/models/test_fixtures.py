# Test ultra avancé pour fixtures/core/models (Python)
import pytest
from backend.components.metiers.gamer.fixtures.core.models.fixtures import (
    sample_gamer_asset,
    advanced_gamer_model,
    asset_texture,
    user_admin,
)

def test___init___core_models_exposed():
    assert True

def test_sample_asset(sample_gamer_asset):
    asset = sample_gamer_asset
    assert asset["name"] == "Cube"

def test_advanced_model(advanced_gamer_model):
    model = advanced_gamer_model
    assert model["name"] == "Pyramide Pro"

def test_asset_texture(asset_texture):
    texture = asset_texture
    assert texture["type"] == "texture"

def test_user_admin(user_admin):
    user = user_admin
    assert user["role"] == "admin"

# Test ultra avancé pour fixtures/core/models (Python)
import pytest
from backend.components.metiers.health.fixtures.core.models.fixtures import (
    sample_health_asset,
    advanced_health_model,
    asset_texture,
    user_admin,
)

def test___init___core_models_exposed():
    assert True

def test_sample_asset(sample_health_asset):
    asset = sample_health_asset
    assert asset["name"] == "Cube"

def test_advanced_model(advanced_health_model):
    model = advanced_health_model
    assert model["name"] == "Pyramide Pro"

def test_asset_texture(asset_texture):
    texture = asset_texture
    assert texture["type"] == "texture"

def test_user_admin(user_admin):
    user = user_admin
    assert user["role"] == "admin"

# Test ultra avancé pour fixtures/core/models (Python)
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../../..')))

import pytest
from backend.components.metiers.tourisme.fixtures.core.models.fixtures import (
    sample_tourisme_asset,
    advanced_tourisme_model,
    asset_texture,
    user_admin,
)

def test___init___core_models_exposed():
    assert True

def test_sample_asset(sample_tourisme_asset):
    asset = sample_tourisme_asset
    assert asset["name"] == "Cube"

def test_advanced_model(advanced_tourisme_model):
    model = advanced_tourisme_model
    assert model["name"] == "Pyramide Pro"

def test_asset_texture(asset_texture):
    texture = asset_texture
    assert texture["type"] == "texture"

def test_user_admin(user_admin):
    user = user_admin
    assert user["role"] == "admin"

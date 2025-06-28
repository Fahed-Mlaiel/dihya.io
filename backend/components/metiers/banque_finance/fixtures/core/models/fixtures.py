"""
Fixtures ultra avancées pour le module Banque_Finance (Dihya Coding)
Inclut modèles Banque_Finance, assets, utilisateurs, et données de test pour tous les cas
métiers.
"""

import pytest


@pytest.fixture(scope="module")
def sample_banque_finance_asset():
    return {
        "name": "Cube",
        "type": "mesh",
        "vertices": 8,
        "faces": 12,
        "tags": ["test", "banque_finance", "sample"],
    }


@pytest.fixture(scope="module")
def advanced_banque_finance_model():
    return {
        "id": "model-002",
        "name": "Pyramide Pro",
        "type": "mesh",
        "vertices": 4,
        "faces": 4,
        "tags": ["pyramide", "pro", "banque_finance"],
    }


@pytest.fixture(scope="module")
def asset_texture():
    return {
        "id": "asset-001",
        "type": "texture",
        "name": "Texture Bois",
        "url": "/assets/bois.jpg",
    }


@pytest.fixture(scope="module")
def user_admin():
    return {"id": "user-001", "name": "Alice", "role": "admin"}


# Cette fichier a été déplacé vers models/fixtures.py

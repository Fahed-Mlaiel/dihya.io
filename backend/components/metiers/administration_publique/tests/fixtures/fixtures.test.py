# fixtures.test.py – Tests avancés d’intégration des fixtures
import pytest
from .fixtures import sample_3d_asset, sample_service, sample_user

def test_sample_3d_asset_structure():
    asset = sample_3d_asset()
    assert asset["id"].startswith("asset-")
    assert asset["type"] == "3d"
    assert "owner" in asset
    assert "created_at" in asset

def test_sample_service_structure():
    service = sample_service()
    assert service["id"].startswith("service-")
    assert service["status"] in ["ok", "maintenance", "error"]
    assert "compliance" in service
    assert service["compliance"]["rgpd"] in [True, False]

def test_sample_user_structure():
    user = sample_user()
    assert user["id"].startswith("user-")
    assert "roles" in user
    assert "email" in user

"""
Test ultra avancé pour le blueprint asset_service (Python)
"""
from blueprints.services.asset_service import AssetService

def test_asset_service():
    service = AssetService()
    asset = {"name": "Asset 1"}
    created = service.create(asset)
    assert created["name"] == "Asset 1"
    all_assets = service.list()
    assert any(a["name"] == "Asset 1" for a in all_assets)

# fixtures.py – Fixtures avancés pour tests 3D, métiers et services
# Respecte la modularité, la réutilisabilité et la conformité RGPD

def sample_3d_asset(**overrides):
    asset = {
        "id": "asset-001",
        "name": "Asset Test",
        "type": "3d",
        "owner": "user-001",
        "created_at": "2025-06-05T00:00:00Z"
    }
    asset.update(overrides)
    return asset

def sample_service(**overrides):
    service = {
        "id": "service-001",
        "name": "Service Test",
        "status": "ok",
        "environment": "production",
        "compliance": {"rgpd": True, "audit": True}
    }
    service.update(overrides)
    return service

def sample_user(**overrides):
    user = {
        "id": "user-001",
        "username": "testuser",
        "roles": ["admin"],
        "email": "test@dihya.io"
    }
    user.update(overrides)
    return user

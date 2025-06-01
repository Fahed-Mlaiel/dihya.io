# Fichier de fixtures pour tests backup avancé Dihya
import pytest

@pytest.fixture
def backup_payload():
    return {
        "project_id": "proj_fixture",
        "user_id": "user_fixture",
        "tenant_id": "tenant_fixture",
        "options": {"deep": True, "compress": True}
    }

@pytest.fixture
def mock_jwt_admin(monkeypatch):
    from backup_service import verify_jwt
    monkeypatch.setattr("backup_service.verify_jwt", lambda token: {"sub": "user_fixture", "role": "admin"})
    yield

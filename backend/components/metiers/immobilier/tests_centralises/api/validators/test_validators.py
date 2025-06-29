import pytest
from immobilier.api.validators.validators import validate_immobilier_entity


def test_validate_immobilier_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_immobilier_entity(data) is True


def test_validate_immobilier_entity_invalid():
    with pytest.raises(ValueError):
        validate_immobilier_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_immobilier_entity({"name": "Test", "status": "invalid"})

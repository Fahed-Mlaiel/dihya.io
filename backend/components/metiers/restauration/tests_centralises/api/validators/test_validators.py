import pytest
from restauration.api.validators.validators import validate_restauration_entity


def test_validate_restauration_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_restauration_entity(data) is True


def test_validate_restauration_entity_invalid():
    with pytest.raises(ValueError):
        validate_restauration_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_restauration_entity({"name": "Test", "status": "invalid"})

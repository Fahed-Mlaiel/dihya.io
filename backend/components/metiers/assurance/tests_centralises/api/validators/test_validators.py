import pytest
from assurance.api.validators.validators import validate_assurance_entity


def test_validate_assurance_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_assurance_entity(data) is True


def test_validate_assurance_entity_invalid():
    with pytest.raises(ValueError):
        validate_assurance_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_assurance_entity({"name": "Test", "status": "invalid"})

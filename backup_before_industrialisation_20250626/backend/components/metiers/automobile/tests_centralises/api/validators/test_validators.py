import pytest
from automobile.api.validators.validators import validate_automobile_entity


def test_validate_automobile_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_automobile_entity(data) is True


def test_validate_automobile_entity_invalid():
    with pytest.raises(ValueError):
        validate_automobile_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_automobile_entity({"name": "Test", "status": "invalid"})

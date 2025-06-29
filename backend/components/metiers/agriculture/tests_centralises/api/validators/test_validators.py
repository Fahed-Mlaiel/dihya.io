import pytest
from agriculture.api.validators.validators import validate_agriculture_entity


def test_validate_agriculture_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_agriculture_entity(data) is True


def test_validate_agriculture_entity_invalid():
    with pytest.raises(ValueError):
        validate_agriculture_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_agriculture_entity({"name": "Test", "status": "invalid"})

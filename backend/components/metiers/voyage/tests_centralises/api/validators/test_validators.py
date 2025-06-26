import pytest
from voyage.api.validators.validators import validate_voyage_entity


def test_validate_voyage_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_voyage_entity(data) is True


def test_validate_voyage_entity_invalid():
    with pytest.raises(ValueError):
        validate_voyage_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_voyage_entity({"name": "Test", "status": "invalid"})

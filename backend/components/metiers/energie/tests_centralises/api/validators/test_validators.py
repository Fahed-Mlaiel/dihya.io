import pytest
from energie.api.validators.validators import validate_energie_entity


def test_validate_energie_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_energie_entity(data) is True


def test_validate_energie_entity_invalid():
    with pytest.raises(ValueError):
        validate_energie_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_energie_entity({"name": "Test", "status": "invalid"})

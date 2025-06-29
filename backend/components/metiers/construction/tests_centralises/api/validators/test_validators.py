import pytest
from construction.api.validators.validators import validate_construction_entity


def test_validate_construction_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_construction_entity(data) is True


def test_validate_construction_entity_invalid():
    with pytest.raises(ValueError):
        validate_construction_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_construction_entity({"name": "Test", "status": "invalid"})

import pytest
from science.api.validators.validators import validate_science_entity


def test_validate_science_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_science_entity(data) is True


def test_validate_science_entity_invalid():
    with pytest.raises(ValueError):
        validate_science_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_science_entity({"name": "Test", "status": "invalid"})

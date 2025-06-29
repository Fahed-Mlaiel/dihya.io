import pytest
from culture.api.validators.validators import validate_culture_entity


def test_validate_culture_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_culture_entity(data) is True


def test_validate_culture_entity_invalid():
    with pytest.raises(ValueError):
        validate_culture_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_culture_entity({"name": "Test", "status": "invalid"})

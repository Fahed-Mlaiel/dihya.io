import pytest
from mode.api.validators.validators import validate_mode_entity


def test_validate_mode_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_mode_entity(data) is True


def test_validate_mode_entity_invalid():
    with pytest.raises(ValueError):
        validate_mode_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_mode_entity({"name": "Test", "status": "invalid"})

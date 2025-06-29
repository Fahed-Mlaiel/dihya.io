import pytest
from gamer.api.validators.validators import validate_gamer_entity


def test_validate_gamer_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_gamer_entity(data) is True


def test_validate_gamer_entity_invalid():
    with pytest.raises(ValueError):
        validate_gamer_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_gamer_entity({"name": "Test", "status": "invalid"})

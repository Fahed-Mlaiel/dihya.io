import pytest
from sport.api.validators.validators import validate_sport_entity


def test_validate_sport_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_sport_entity(data) is True


def test_validate_sport_entity_invalid():
    with pytest.raises(ValueError):
        validate_sport_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_sport_entity({"name": "Test", "status": "invalid"})

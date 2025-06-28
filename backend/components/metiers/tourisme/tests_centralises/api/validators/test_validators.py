import pytest
from tourisme.api.validators.validators import validate_tourisme_entity


def test_validate_tourisme_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_tourisme_entity(data) is True


def test_validate_tourisme_entity_invalid():
    with pytest.raises(ValueError):
        validate_tourisme_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_tourisme_entity({"name": "Test", "status": "invalid"})

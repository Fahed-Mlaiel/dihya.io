import pytest
from a_i.api.validators.validators import validate_a_i_entity


def test_validate_a_i_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_a_i_entity(data) is True


def test_validate_a_i_entity_invalid():
    with pytest.raises(ValueError):
        validate_a_i_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_a_i_entity({"name": "Test", "status": "invalid"})

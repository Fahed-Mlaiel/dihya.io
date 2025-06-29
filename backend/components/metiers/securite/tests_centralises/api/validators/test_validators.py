import pytest
from securite.api.validators.validators import validate_securite_entity


def test_validate_securite_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_securite_entity(data) is True


def test_validate_securite_entity_invalid():
    with pytest.raises(ValueError):
        validate_securite_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_securite_entity({"name": "Test", "status": "invalid"})

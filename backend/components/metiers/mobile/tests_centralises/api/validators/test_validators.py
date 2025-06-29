import pytest
from mobile.api.validators.validators import validate_mobile_entity


def test_validate_mobile_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_mobile_entity(data) is True


def test_validate_mobile_entity_invalid():
    with pytest.raises(ValueError):
        validate_mobile_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_mobile_entity({"name": "Test", "status": "invalid"})

import pytest
from threed.api.validators.validators import validate_threed_entity


def test_validate_threed_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_threed_entity(data) is True


def test_validate_threed_entity_invalid():
    with pytest.raises(ValueError):
        validate_threed_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_threed_entity({"name": "Test", "status": "invalid"})

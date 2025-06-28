import pytest
from health.api.validators.validators import validate_health_entity


def test_validate_health_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_health_entity(data) is True


def test_validate_health_entity_invalid():
    with pytest.raises(ValueError):
        validate_health_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_health_entity({"name": "Test", "status": "invalid"})

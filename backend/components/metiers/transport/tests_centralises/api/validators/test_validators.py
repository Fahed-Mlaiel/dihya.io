import pytest
from transport.api.validators.validators import validate_transport_entity


def test_validate_transport_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_transport_entity(data) is True


def test_validate_transport_entity_invalid():
    with pytest.raises(ValueError):
        validate_transport_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_transport_entity({"name": "Test", "status": "invalid"})

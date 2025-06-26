import pytest
from arts.api.validators.validators import validate_arts_entity


def test_validate_arts_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_arts_entity(data) is True


def test_validate_arts_entity_invalid():
    with pytest.raises(ValueError):
        validate_arts_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_arts_entity({"name": "Test", "status": "invalid"})

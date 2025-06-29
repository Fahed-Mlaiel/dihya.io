import pytest
from hotellerie.api.validators.validators import validate_hotellerie_entity


def test_validate_hotellerie_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_hotellerie_entity(data) is True


def test_validate_hotellerie_entity_invalid():
    with pytest.raises(ValueError):
        validate_hotellerie_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_hotellerie_entity({"name": "Test", "status": "invalid"})

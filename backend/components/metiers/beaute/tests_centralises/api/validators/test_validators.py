import pytest
from beaute.api.validators.validators import validate_beaute_entity


def test_validate_beaute_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_beaute_entity(data) is True


def test_validate_beaute_entity_invalid():
    with pytest.raises(ValueError):
        validate_beaute_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_beaute_entity({"name": "Test", "status": "invalid"})

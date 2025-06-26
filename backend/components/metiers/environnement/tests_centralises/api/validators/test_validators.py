import pytest
from environnement.api.validators.validators import validate_environnement_entity


def test_validate_environnement_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_environnement_entity(data) is True


def test_validate_environnement_entity_invalid():
    with pytest.raises(ValueError):
        validate_environnement_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_environnement_entity({"name": "Test", "status": "invalid"})

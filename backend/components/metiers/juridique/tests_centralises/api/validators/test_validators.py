import pytest
from juridique.api.validators.validators import validate_juridique_entity


def test_validate_juridique_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_juridique_entity(data) is True


def test_validate_juridique_entity_invalid():
    with pytest.raises(ValueError):
        validate_juridique_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_juridique_entity({"name": "Test", "status": "invalid"})

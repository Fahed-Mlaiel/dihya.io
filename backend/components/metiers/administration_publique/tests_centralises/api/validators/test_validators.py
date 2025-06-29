import pytest
from administration_publique.api.validators.validators import validate_administration_publique_entity


def test_validate_administration_publique_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_administration_publique_entity(data) is True


def test_validate_administration_publique_entity_invalid():
    with pytest.raises(ValueError):
        validate_administration_publique_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_administration_publique_entity({"name": "Test", "status": "invalid"})

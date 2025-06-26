import pytest
from sante.api.validators.validators import validate_sante_entity


def test_validate_sante_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_sante_entity(data) is True


def test_validate_sante_entity_invalid():
    with pytest.raises(ValueError):
        validate_sante_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_sante_entity({"name": "Test", "status": "invalid"})

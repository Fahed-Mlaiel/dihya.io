import pytest
from recherche.api.validators.validators import validate_recherche_entity


def test_validate_recherche_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_recherche_entity(data) is True


def test_validate_recherche_entity_invalid():
    with pytest.raises(ValueError):
        validate_recherche_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_recherche_entity({"name": "Test", "status": "invalid"})

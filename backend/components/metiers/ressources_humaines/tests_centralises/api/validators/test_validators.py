import pytest
from ressources_humaines.api.validators.validators import validate_ressources_humaines_entity


def test_validate_ressources_humaines_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_ressources_humaines_entity(data) is True


def test_validate_ressources_humaines_entity_invalid():
    with pytest.raises(ValueError):
        validate_ressources_humaines_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_ressources_humaines_entity({"name": "Test", "status": "invalid"})

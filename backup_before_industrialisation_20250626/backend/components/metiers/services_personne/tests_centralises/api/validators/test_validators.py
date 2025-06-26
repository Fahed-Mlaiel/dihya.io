import pytest
from services_personne.api.validators.validators import validate_services_personne_entity


def test_validate_services_personne_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_services_personne_entity(data) is True


def test_validate_services_personne_entity_invalid():
    with pytest.raises(ValueError):
        validate_services_personne_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_services_personne_entity({"name": "Test", "status": "invalid"})

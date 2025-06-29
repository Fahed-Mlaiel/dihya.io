import pytest
from medias.api.validators.validators import validate_medias_entity


def test_validate_medias_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_medias_entity(data) is True


def test_validate_medias_entity_invalid():
    with pytest.raises(ValueError):
        validate_medias_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_medias_entity({"name": "Test", "status": "invalid"})

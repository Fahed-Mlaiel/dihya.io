import pytest
from education.api.validators.validators import validate_education_entity


def test_validate_education_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_education_entity(data) is True


def test_validate_education_entity_invalid():
    with pytest.raises(ValueError):
        validate_education_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_education_entity({"name": "Test", "status": "invalid"})

import pytest
from social.api.validators.validators import validate_social_entity


def test_validate_social_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_social_entity(data) is True


def test_validate_social_entity_invalid():
    with pytest.raises(ValueError):
        validate_social_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_social_entity({"name": "Test", "status": "invalid"})

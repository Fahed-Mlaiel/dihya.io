import pytest
from seo.api.validators.validators import validate_seo_entity


def test_validate_seo_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_seo_entity(data) is True


def test_validate_seo_entity_invalid():
    with pytest.raises(ValueError):
        validate_seo_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_seo_entity({"name": "Test", "status": "invalid"})

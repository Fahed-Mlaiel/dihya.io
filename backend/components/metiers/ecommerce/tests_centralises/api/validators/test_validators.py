import pytest
from ecommerce.api.validators.validators import validate_ecommerce_entity


def test_validate_ecommerce_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_ecommerce_entity(data) is True


def test_validate_ecommerce_entity_invalid():
    with pytest.raises(ValueError):
        validate_ecommerce_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_ecommerce_entity({"name": "Test", "status": "invalid"})

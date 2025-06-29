import pytest
from crypto.api.validators.validators import validate_crypto_entity


def test_validate_crypto_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_crypto_entity(data) is True


def test_validate_crypto_entity_invalid():
    with pytest.raises(ValueError):
        validate_crypto_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_crypto_entity({"name": "Test", "status": "invalid"})

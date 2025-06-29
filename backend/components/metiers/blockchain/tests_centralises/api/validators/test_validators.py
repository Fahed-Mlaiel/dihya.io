import pytest
from blockchain.api.validators.validators import validate_blockchain_entity


def test_validate_blockchain_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_blockchain_entity(data) is True


def test_validate_blockchain_entity_invalid():
    with pytest.raises(ValueError):
        validate_blockchain_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_blockchain_entity({"name": "Test", "status": "invalid"})

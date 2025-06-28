import pytest
from industrie.api.validators.validators import validate_industrie_entity


def test_validate_industrie_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_industrie_entity(data) is True


def test_validate_industrie_entity_invalid():
    with pytest.raises(ValueError):
        validate_industrie_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_industrie_entity({"name": "Test", "status": "invalid"})

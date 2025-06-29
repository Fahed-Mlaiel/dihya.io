import pytest
from voice.api.validators.validators import validate_voice_entity


def test_validate_voice_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_voice_entity(data) is True


def test_validate_voice_entity_invalid():
    with pytest.raises(ValueError):
        validate_voice_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_voice_entity({"name": "Test", "status": "invalid"})

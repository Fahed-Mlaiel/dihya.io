import pytest
from video.api.validators.validators import validate_video_entity


def test_validate_video_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_video_entity(data) is True


def test_validate_video_entity_invalid():
    with pytest.raises(ValueError):
        validate_video_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_video_entity({"name": "Test", "status": "invalid"})

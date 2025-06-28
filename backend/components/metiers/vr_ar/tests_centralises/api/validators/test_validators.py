import pytest
from vr_ar.api.validators.validators import validate_vr_ar_entity


def test_validate_vr_ar_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_vr_ar_entity(data) is True


def test_validate_vr_ar_entity_invalid():
    with pytest.raises(ValueError):
        validate_vr_ar_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_vr_ar_entity({"name": "Test", "status": "invalid"})

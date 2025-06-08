import pytest
from backend.components.metiers.threed.api.validators.validators import validate_3d_entity

def test_validate_3d_entity_valid():
    data = {'name': 'Test', 'status': 'active'}
    assert validate_3d_entity(data) is True

def test_validate_3d_entity_invalid():
    with pytest.raises(ValueError):
        validate_3d_entity({'name': 123, 'status': 'active'})
    with pytest.raises(ValueError):
        validate_3d_entity({'name': 'Test', 'status': 'invalid'})

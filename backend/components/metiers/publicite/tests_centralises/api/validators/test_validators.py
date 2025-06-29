import pytest
from publicite.api.validators.validators import validate_publicite_entity


def test_validate_publicite_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_publicite_entity(data) is True


def test_validate_publicite_entity_invalid():
    with pytest.raises(ValueError):
        validate_publicite_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_publicite_entity({"name": "Test", "status": "invalid"})

import pytest
from banque_finance.api.validators.validators import validate_banque_finance_entity


def test_validate_banque_finance_entity_valid():
    data = {"name": "Test", "status": "active"}
    assert validate_banque_finance_entity(data) is True


def test_validate_banque_finance_entity_invalid():
    with pytest.raises(ValueError):
        validate_banque_finance_entity({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        validate_banque_finance_entity({"name": "Test", "status": "invalid"})

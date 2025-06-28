# banque_finance_controller.test.py – Test ultra avancé pour banque_finance_controller.py
# (API Banque_Finance)
from banque_finance.api.controllers.banque_finance_controller import (
    get_banque_finance,
    create_banque_finance,
    update_banque_finance,
    delete_banque_finance,
)


def test_get_banque_finance_exists():
    assert callable(get_banque_finance)


def test_create_banque_finance_exists():
    assert callable(create_banque_finance)


def test_update_banque_finance_exists():
    assert callable(update_banque_finance)


def test_delete_banque_finance_exists():
    assert callable(delete_banque_finance)


def test_get_banque_finance_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_banque_finance(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_banque_finance_not_found():
    # Test edge case : entité non trouvée
    from banque_finance.api.controllers.banque_finance_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import banque_finance.api.controllers.banque_finance_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_banque_finance(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_banque_finance_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_banque_finance(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_banque_finance_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_banque_finance({"status": "active"})
    with pytest.raises(ValueError):
        create_banque_finance({"name": "Test"})
    with pytest.raises(ValueError):
        create_banque_finance({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_banque_finance({"name": "Test", "status": "foo"})


def test_update_banque_finance_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_banque_finance(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_banque_finance_nominal():
    # Test suppression nominale
    assert delete_banque_finance(1) is True

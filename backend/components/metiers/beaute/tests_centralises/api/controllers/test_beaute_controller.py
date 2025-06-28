# beaute_controller.test.py – Test ultra avancé pour beaute_controller.py
# (API Beaute)
from beaute.api.controllers.beaute_controller import (
    get_beaute,
    create_beaute,
    update_beaute,
    delete_beaute,
)


def test_get_beaute_exists():
    assert callable(get_beaute)


def test_create_beaute_exists():
    assert callable(create_beaute)


def test_update_beaute_exists():
    assert callable(update_beaute)


def test_delete_beaute_exists():
    assert callable(delete_beaute)


def test_get_beaute_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_beaute(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_beaute_not_found():
    # Test edge case : entité non trouvée
    from beaute.api.controllers.beaute_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import beaute.api.controllers.beaute_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_beaute(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_beaute_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_beaute(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_beaute_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_beaute({"status": "active"})
    with pytest.raises(ValueError):
        create_beaute({"name": "Test"})
    with pytest.raises(ValueError):
        create_beaute({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_beaute({"name": "Test", "status": "foo"})


def test_update_beaute_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_beaute(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_beaute_nominal():
    # Test suppression nominale
    assert delete_beaute(1) is True

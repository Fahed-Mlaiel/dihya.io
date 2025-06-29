# restauration_controller.test.py – Test ultra avancé pour restauration_controller.py
# (API RestauratioN)
from restauration.api.controllers.restauration_controller import (
    get_restauration,
    create_restauration,
    update_restauration,
    delete_restauration,
)


def test_get_restauration_exists():
    assert callable(get_restauration)


def test_create_restauration_exists():
    assert callable(create_restauration)


def test_update_restauration_exists():
    assert callable(update_restauration)


def test_delete_restauration_exists():
    assert callable(delete_restauration)


def test_get_restauration_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_restauration(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_restauration_not_found():
    # Test edge case : entité non trouvée
    from restauration.api.controllers.restauration_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import restauration.api.controllers.restauration_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_restauration(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_restauration_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_restauration(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_restauration_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_restauration({"status": "active"})
    with pytest.raises(ValueError):
        create_restauration({"name": "Test"})
    with pytest.raises(ValueError):
        create_restauration({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_restauration({"name": "Test", "status": "foo"})


def test_update_restauration_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_restauration(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_restauration_nominal():
    # Test suppression nominale
    assert delete_restauration(1) is True

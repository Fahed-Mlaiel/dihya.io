# agriculture_controller.test.py – Test ultra avancé pour agriculture_controller.py
# (API Agriculture)
from agriculture.api.controllers.agriculture_controller import (
    get_agriculture,
    create_agriculture,
    update_agriculture,
    delete_agriculture,
)


def test_get_agriculture_exists():
    assert callable(get_agriculture)


def test_create_agriculture_exists():
    assert callable(create_agriculture)


def test_update_agriculture_exists():
    assert callable(update_agriculture)


def test_delete_agriculture_exists():
    assert callable(delete_agriculture)


def test_get_agriculture_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_agriculture(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_agriculture_not_found():
    # Test edge case : entité non trouvée
    from agriculture.api.controllers.agriculture_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import agriculture.api.controllers.agriculture_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_agriculture(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_agriculture_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_agriculture(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_agriculture_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_agriculture({"status": "active"})
    with pytest.raises(ValueError):
        create_agriculture({"name": "Test"})
    with pytest.raises(ValueError):
        create_agriculture({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_agriculture({"name": "Test", "status": "foo"})


def test_update_agriculture_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_agriculture(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_agriculture_nominal():
    # Test suppression nominale
    assert delete_agriculture(1) is True

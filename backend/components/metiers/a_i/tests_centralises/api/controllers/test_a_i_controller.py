# a_i_controller.test.py – Test ultra avancé pour a_i_controller.py
# (API A_I)
from a_i.api.controllers.a_i_controller import (
    get_a_i,
    create_a_i,
    update_a_i,
    delete_a_i,
)


def test_get_a_i_exists():
    assert callable(get_a_i)


def test_create_a_i_exists():
    assert callable(create_a_i)


def test_update_a_i_exists():
    assert callable(update_a_i)


def test_delete_a_i_exists():
    assert callable(delete_a_i)


def test_get_a_i_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_a_i(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_a_i_not_found():
    # Test edge case : entité non trouvée
    from a_i.api.controllers.a_i_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import a_i.api.controllers.a_i_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_a_i(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_a_i_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_a_i(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_a_i_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_a_i({"status": "active"})
    with pytest.raises(ValueError):
        create_a_i({"name": "Test"})
    with pytest.raises(ValueError):
        create_a_i({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_a_i({"name": "Test", "status": "foo"})


def test_update_a_i_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_a_i(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_a_i_nominal():
    # Test suppression nominale
    assert delete_a_i(1) is True

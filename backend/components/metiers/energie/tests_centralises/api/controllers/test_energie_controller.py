# energie_controller.test.py – Test ultra avancé pour energie_controller.py
# (API Energie)
from energie.api.controllers.energie_controller import (
    get_energie,
    create_energie,
    update_energie,
    delete_energie,
)


def test_get_energie_exists():
    assert callable(get_energie)


def test_create_energie_exists():
    assert callable(create_energie)


def test_update_energie_exists():
    assert callable(update_energie)


def test_delete_energie_exists():
    assert callable(delete_energie)


def test_get_energie_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_energie(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_energie_not_found():
    # Test edge case : entité non trouvée
    from energie.api.controllers.energie_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import energie.api.controllers.energie_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_energie(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_energie_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_energie(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_energie_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_energie({"status": "active"})
    with pytest.raises(ValueError):
        create_energie({"name": "Test"})
    with pytest.raises(ValueError):
        create_energie({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_energie({"name": "Test", "status": "foo"})


def test_update_energie_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_energie(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_energie_nominal():
    # Test suppression nominale
    assert delete_energie(1) is True

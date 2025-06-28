# voyage_controller.test.py – Test ultra avancé pour voyage_controller.py
# (API Voyage)
from voyage.api.controllers.voyage_controller import (
    get_voyage,
    create_voyage,
    update_voyage,
    delete_voyage,
)


def test_get_voyage_exists():
    assert callable(get_voyage)


def test_create_voyage_exists():
    assert callable(create_voyage)


def test_update_voyage_exists():
    assert callable(update_voyage)


def test_delete_voyage_exists():
    assert callable(delete_voyage)


def test_get_voyage_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_voyage(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_voyage_not_found():
    # Test edge case : entité non trouvée
    from voyage.api.controllers.voyage_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import voyage.api.controllers.voyage_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_voyage(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_voyage_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_voyage(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_voyage_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_voyage({"status": "active"})
    with pytest.raises(ValueError):
        create_voyage({"name": "Test"})
    with pytest.raises(ValueError):
        create_voyage({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_voyage({"name": "Test", "status": "foo"})


def test_update_voyage_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_voyage(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_voyage_nominal():
    # Test suppression nominale
    assert delete_voyage(1) is True

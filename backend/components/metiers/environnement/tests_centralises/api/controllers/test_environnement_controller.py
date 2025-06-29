# environnement_controller.test.py – Test ultra avancé pour environnement_controller.py
# (API Environnement)
from environnement.api.controllers.environnement_controller import (
    get_environnement,
    create_environnement,
    update_environnement,
    delete_environnement,
)


def test_get_environnement_exists():
    assert callable(get_environnement)


def test_create_environnement_exists():
    assert callable(create_environnement)


def test_update_environnement_exists():
    assert callable(update_environnement)


def test_delete_environnement_exists():
    assert callable(delete_environnement)


def test_get_environnement_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_environnement(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_environnement_not_found():
    # Test edge case : entité non trouvée
    from environnement.api.controllers.environnement_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import environnement.api.controllers.environnement_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_environnement(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_environnement_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_environnement(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_environnement_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_environnement({"status": "active"})
    with pytest.raises(ValueError):
        create_environnement({"name": "Test"})
    with pytest.raises(ValueError):
        create_environnement({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_environnement({"name": "Test", "status": "foo"})


def test_update_environnement_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_environnement(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_environnement_nominal():
    # Test suppression nominale
    assert delete_environnement(1) is True

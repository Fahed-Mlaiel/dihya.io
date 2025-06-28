# securite_controller.test.py – Test ultra avancé pour securite_controller.py
# (API Securite)
from securite.api.controllers.securite_controller import (
    get_securite,
    create_securite,
    update_securite,
    delete_securite,
)


def test_get_securite_exists():
    assert callable(get_securite)


def test_create_securite_exists():
    assert callable(create_securite)


def test_update_securite_exists():
    assert callable(update_securite)


def test_delete_securite_exists():
    assert callable(delete_securite)


def test_get_securite_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_securite(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_securite_not_found():
    # Test edge case : entité non trouvée
    from securite.api.controllers.securite_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import securite.api.controllers.securite_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_securite(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_securite_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_securite(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_securite_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_securite({"status": "active"})
    with pytest.raises(ValueError):
        create_securite({"name": "Test"})
    with pytest.raises(ValueError):
        create_securite({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_securite({"name": "Test", "status": "foo"})


def test_update_securite_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_securite(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_securite_nominal():
    # Test suppression nominale
    assert delete_securite(1) is True

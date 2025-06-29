# recherche_controller.test.py – Test ultra avancé pour recherche_controller.py
# (API Recherche)
from recherche.api.controllers.recherche_controller import (
    get_recherche,
    create_recherche,
    update_recherche,
    delete_recherche,
)


def test_get_recherche_exists():
    assert callable(get_recherche)


def test_create_recherche_exists():
    assert callable(create_recherche)


def test_update_recherche_exists():
    assert callable(update_recherche)


def test_delete_recherche_exists():
    assert callable(delete_recherche)


def test_get_recherche_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_recherche(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_recherche_not_found():
    # Test edge case : entité non trouvée
    from recherche.api.controllers.recherche_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import recherche.api.controllers.recherche_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_recherche(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_recherche_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_recherche(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_recherche_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_recherche({"status": "active"})
    with pytest.raises(ValueError):
        create_recherche({"name": "Test"})
    with pytest.raises(ValueError):
        create_recherche({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_recherche({"name": "Test", "status": "foo"})


def test_update_recherche_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_recherche(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_recherche_nominal():
    # Test suppression nominale
    assert delete_recherche(1) is True

# sport_controller.test.py – Test ultra avancé pour sport_controller.py
# (API Sport)
from sport.api.controllers.sport_controller import (
    get_sport,
    create_sport,
    update_sport,
    delete_sport,
)


def test_get_sport_exists():
    assert callable(get_sport)


def test_create_sport_exists():
    assert callable(create_sport)


def test_update_sport_exists():
    assert callable(update_sport)


def test_delete_sport_exists():
    assert callable(delete_sport)


def test_get_sport_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_sport(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_sport_not_found():
    # Test edge case : entité non trouvée
    from sport.api.controllers.sport_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import sport.api.controllers.sport_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_sport(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_sport_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_sport(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_sport_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_sport({"status": "active"})
    with pytest.raises(ValueError):
        create_sport({"name": "Test"})
    with pytest.raises(ValueError):
        create_sport({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_sport({"name": "Test", "status": "foo"})


def test_update_sport_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_sport(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_sport_nominal():
    # Test suppression nominale
    assert delete_sport(1) is True

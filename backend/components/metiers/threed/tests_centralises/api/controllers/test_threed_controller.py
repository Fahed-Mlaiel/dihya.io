# threed_controller.test.py – Test ultra avancé pour threed_controller.py
# (API Threed)
from threed.api.controllers.threed_controller import (
    get_threed,
    create_threed,
    update_threed,
    delete_threed,
)


def test_get_threed_exists():
    assert callable(get_threed)


def test_create_threed_exists():
    assert callable(create_threed)


def test_update_threed_exists():
    assert callable(update_threed)


def test_delete_threed_exists():
    assert callable(delete_threed)


def test_get_threed_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_threed(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_threed_not_found():
    # Test edge case : entité non trouvée
    from threed.api.controllers.threed_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import threed.api.controllers.threed_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_threed(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_threed_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_threed(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_threed_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_threed({"status": "active"})
    with pytest.raises(ValueError):
        create_threed({"name": "Test"})
    with pytest.raises(ValueError):
        create_threed({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_threed({"name": "Test", "status": "foo"})


def test_update_threed_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_threed(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_threed_nominal():
    # Test suppression nominale
    assert delete_threed(1) is True

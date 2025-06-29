# mode_controller.test.py – Test ultra avancé pour mode_controller.py
# (API Mode)
from mode.api.controllers.mode_controller import (
    get_mode,
    create_mode,
    update_mode,
    delete_mode,
)


def test_get_mode_exists():
    assert callable(get_mode)


def test_create_mode_exists():
    assert callable(create_mode)


def test_update_mode_exists():
    assert callable(update_mode)


def test_delete_mode_exists():
    assert callable(delete_mode)


def test_get_mode_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_mode(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_mode_not_found():
    # Test edge case : entité non trouvée
    from mode.api.controllers.mode_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import mode.api.controllers.mode_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_mode(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_mode_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_mode(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_mode_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_mode({"status": "active"})
    with pytest.raises(ValueError):
        create_mode({"name": "Test"})
    with pytest.raises(ValueError):
        create_mode({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_mode({"name": "Test", "status": "foo"})


def test_update_mode_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_mode(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_mode_nominal():
    # Test suppression nominale
    assert delete_mode(1) is True

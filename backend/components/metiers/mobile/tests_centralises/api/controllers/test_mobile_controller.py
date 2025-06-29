# mobile_controller.test.py – Test ultra avancé pour mobile_controller.py
# (API Mobile)
from mobile.api.controllers.mobile_controller import (
    get_mobile,
    create_mobile,
    update_mobile,
    delete_mobile,
)


def test_get_mobile_exists():
    assert callable(get_mobile)


def test_create_mobile_exists():
    assert callable(create_mobile)


def test_update_mobile_exists():
    assert callable(update_mobile)


def test_delete_mobile_exists():
    assert callable(delete_mobile)


def test_get_mobile_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_mobile(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_mobile_not_found():
    # Test edge case : entité non trouvée
    from mobile.api.controllers.mobile_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import mobile.api.controllers.mobile_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_mobile(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_mobile_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_mobile(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_mobile_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_mobile({"status": "active"})
    with pytest.raises(ValueError):
        create_mobile({"name": "Test"})
    with pytest.raises(ValueError):
        create_mobile({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_mobile({"name": "Test", "status": "foo"})


def test_update_mobile_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_mobile(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_mobile_nominal():
    # Test suppression nominale
    assert delete_mobile(1) is True

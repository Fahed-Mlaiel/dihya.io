# vr_ar_controller.test.py – Test ultra avancé pour vr_ar_controller.py
# (API vr_ar)
from vr_ar.api.controllers.vr_ar_controller import (
    get_vr_ar,
    create_vr_ar,
    update_vr_ar,
    delete_vr_ar,
)


def test_get_vr_ar_exists():
    assert callable(get_vr_ar)


def test_create_vr_ar_exists():
    assert callable(create_vr_ar)


def test_update_vr_ar_exists():
    assert callable(update_vr_ar)


def test_delete_vr_ar_exists():
    assert callable(delete_vr_ar)


def test_get_vr_ar_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_vr_ar(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_vr_ar_not_found():
    # Test edge case : entité non trouvée
    from vr_ar.api.controllers.vr_ar_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import vr_ar.api.controllers.vr_ar_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_vr_ar(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_vr_ar_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_vr_ar(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_vr_ar_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_vr_ar({"status": "active"})
    with pytest.raises(ValueError):
        create_vr_ar({"name": "Test"})
    with pytest.raises(ValueError):
        create_vr_ar({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_vr_ar({"name": "Test", "status": "foo"})


def test_update_vr_ar_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_vr_ar(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_vr_ar_nominal():
    # Test suppression nominale
    assert delete_vr_ar(1) is True

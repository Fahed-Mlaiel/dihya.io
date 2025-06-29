# hotellerie_controller.test.py – Test ultra avancé pour hotellerie_controller.py
# (API Hotellerie)
from hotellerie.api.controllers.hotellerie_controller import (
    get_hotellerie,
    create_hotellerie,
    update_hotellerie,
    delete_hotellerie,
)


def test_get_hotellerie_exists():
    assert callable(get_hotellerie)


def test_create_hotellerie_exists():
    assert callable(create_hotellerie)


def test_update_hotellerie_exists():
    assert callable(update_hotellerie)


def test_delete_hotellerie_exists():
    assert callable(delete_hotellerie)


def test_get_hotellerie_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_hotellerie(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_hotellerie_not_found():
    # Test edge case : entité non trouvée
    from hotellerie.api.controllers.hotellerie_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import hotellerie.api.controllers.hotellerie_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_hotellerie(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_hotellerie_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_hotellerie(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_hotellerie_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_hotellerie({"status": "active"})
    with pytest.raises(ValueError):
        create_hotellerie({"name": "Test"})
    with pytest.raises(ValueError):
        create_hotellerie({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_hotellerie({"name": "Test", "status": "foo"})


def test_update_hotellerie_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_hotellerie(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_hotellerie_nominal():
    # Test suppression nominale
    assert delete_hotellerie(1) is True

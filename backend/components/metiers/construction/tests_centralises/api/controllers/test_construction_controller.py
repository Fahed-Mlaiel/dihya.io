# construction_controller.test.py – Test ultra avancé pour construction_controller.py
# (API Construction)
from construction.api.controllers.construction_controller import (
    get_construction,
    create_construction,
    update_construction,
    delete_construction,
)


def test_get_construction_exists():
    assert callable(get_construction)


def test_create_construction_exists():
    assert callable(create_construction)


def test_update_construction_exists():
    assert callable(update_construction)


def test_delete_construction_exists():
    assert callable(delete_construction)


def test_get_construction_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_construction(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_construction_not_found():
    # Test edge case : entité non trouvée
    from construction.api.controllers.construction_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import construction.api.controllers.construction_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_construction(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_construction_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_construction(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_construction_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_construction({"status": "active"})
    with pytest.raises(ValueError):
        create_construction({"name": "Test"})
    with pytest.raises(ValueError):
        create_construction({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_construction({"name": "Test", "status": "foo"})


def test_update_construction_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_construction(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_construction_nominal():
    # Test suppression nominale
    assert delete_construction(1) is True

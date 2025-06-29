# arts_controller.test.py – Test ultra avancé pour arts_controller.py
# (API Arts)
from arts.api.controllers.arts_controller import (
    get_arts,
    create_arts,
    update_arts,
    delete_arts,
)


def test_get_arts_exists():
    assert callable(get_arts)


def test_create_arts_exists():
    assert callable(create_arts)


def test_update_arts_exists():
    assert callable(update_arts)


def test_delete_arts_exists():
    assert callable(delete_arts)


def test_get_arts_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_arts(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_arts_not_found():
    # Test edge case : entité non trouvée
    from arts.api.controllers.arts_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import arts.api.controllers.arts_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_arts(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_arts_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_arts(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_arts_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_arts({"status": "active"})
    with pytest.raises(ValueError):
        create_arts({"name": "Test"})
    with pytest.raises(ValueError):
        create_arts({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_arts({"name": "Test", "status": "foo"})


def test_update_arts_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_arts(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_arts_nominal():
    # Test suppression nominale
    assert delete_arts(1) is True

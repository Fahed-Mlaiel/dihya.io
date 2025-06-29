# tourisme_controller.test.py – Test ultra avancé pour tourisme_controller.py
# (API Tourisme)
from tourisme.api.controllers.tourisme_controller import (
    get_tourisme,
    create_tourisme,
    update_tourisme,
    delete_tourisme,
)


def test_get_tourisme_exists():
    assert callable(get_tourisme)


def test_create_tourisme_exists():
    assert callable(create_tourisme)


def test_update_tourisme_exists():
    assert callable(update_tourisme)


def test_delete_tourisme_exists():
    assert callable(delete_tourisme)


def test_get_tourisme_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_tourisme(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_tourisme_not_found():
    # Test edge case : entité non trouvée
    from tourisme.api.controllers.tourisme_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import tourisme.api.controllers.tourisme_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_tourisme(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_tourisme_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_tourisme(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_tourisme_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_tourisme({"status": "active"})
    with pytest.raises(ValueError):
        create_tourisme({"name": "Test"})
    with pytest.raises(ValueError):
        create_tourisme({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_tourisme({"name": "Test", "status": "foo"})


def test_update_tourisme_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_tourisme(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_tourisme_nominal():
    # Test suppression nominale
    assert delete_tourisme(1) is True

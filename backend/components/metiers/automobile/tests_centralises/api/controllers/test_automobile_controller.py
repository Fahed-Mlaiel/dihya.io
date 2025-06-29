# automobile_controller.test.py – Test ultra avancé pour automobile_controller.py
# (API Automobile)
from automobile.api.controllers.automobile_controller import (
    get_automobile,
    create_automobile,
    update_automobile,
    delete_automobile,
)


def test_get_automobile_exists():
    assert callable(get_automobile)


def test_create_automobile_exists():
    assert callable(create_automobile)


def test_update_automobile_exists():
    assert callable(update_automobile)


def test_delete_automobile_exists():
    assert callable(delete_automobile)


def test_get_automobile_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_automobile(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_automobile_not_found():
    # Test edge case : entité non trouvée
    from automobile.api.controllers.automobile_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import automobile.api.controllers.automobile_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_automobile(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_automobile_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_automobile(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_automobile_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_automobile({"status": "active"})
    with pytest.raises(ValueError):
        create_automobile({"name": "Test"})
    with pytest.raises(ValueError):
        create_automobile({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_automobile({"name": "Test", "status": "foo"})


def test_update_automobile_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_automobile(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_automobile_nominal():
    # Test suppression nominale
    assert delete_automobile(1) is True

# health_controller.test.py – Test ultra avancé pour health_controller.py
# (API Health)
from health.api.controllers.health_controller import (
    get_health,
    create_health,
    update_health,
    delete_health,
)


def test_get_health_exists():
    assert callable(get_health)


def test_create_health_exists():
    assert callable(create_health)


def test_update_health_exists():
    assert callable(update_health)


def test_delete_health_exists():
    assert callable(delete_health)


def test_get_health_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_health(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_health_not_found():
    # Test edge case : entité non trouvée
    from health.api.controllers.health_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import health.api.controllers.health_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_health(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_health_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_health(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_health_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_health({"status": "active"})
    with pytest.raises(ValueError):
        create_health({"name": "Test"})
    with pytest.raises(ValueError):
        create_health({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_health({"name": "Test", "status": "foo"})


def test_update_health_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_health(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_health_nominal():
    # Test suppression nominale
    assert delete_health(1) is True

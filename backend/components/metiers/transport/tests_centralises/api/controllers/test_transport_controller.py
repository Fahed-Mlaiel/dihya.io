# transport_controller.test.py – Test ultra avancé pour transport_controller.py
# (API Transport)
from transport.api.controllers.transport_controller import (
    get_transport,
    create_transport,
    update_transport,
    delete_transport,
)


def test_get_transport_exists():
    assert callable(get_transport)


def test_create_transport_exists():
    assert callable(create_transport)


def test_update_transport_exists():
    assert callable(update_transport)


def test_delete_transport_exists():
    assert callable(delete_transport)


def test_get_transport_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_transport(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_transport_not_found():
    # Test edge case : entité non trouvée
    from transport.api.controllers.transport_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import transport.api.controllers.transport_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_transport(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_transport_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_transport(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_transport_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_transport({"status": "active"})
    with pytest.raises(ValueError):
        create_transport({"name": "Test"})
    with pytest.raises(ValueError):
        create_transport({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_transport({"name": "Test", "status": "foo"})


def test_update_transport_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_transport(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_transport_nominal():
    # Test suppression nominale
    assert delete_transport(1) is True

# ecommerce_controller.test.py – Test ultra avancé pour ecommerce_controller.py
# (API Ecommerce)
from ecommerce.api.controllers.ecommerce_controller import (
    get_ecommerce,
    create_ecommerce,
    update_ecommerce,
    delete_ecommerce,
)


def test_get_ecommerce_exists():
    assert callable(get_ecommerce)


def test_create_ecommerce_exists():
    assert callable(create_ecommerce)


def test_update_ecommerce_exists():
    assert callable(update_ecommerce)


def test_delete_ecommerce_exists():
    assert callable(delete_ecommerce)


def test_get_ecommerce_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_ecommerce(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_ecommerce_not_found():
    # Test edge case : entité non trouvée
    from ecommerce.api.controllers.ecommerce_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import ecommerce.api.controllers.ecommerce_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_ecommerce(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_ecommerce_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_ecommerce(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_ecommerce_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_ecommerce({"status": "active"})
    with pytest.raises(ValueError):
        create_ecommerce({"name": "Test"})
    with pytest.raises(ValueError):
        create_ecommerce({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_ecommerce({"name": "Test", "status": "foo"})


def test_update_ecommerce_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_ecommerce(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_ecommerce_nominal():
    # Test suppression nominale
    assert delete_ecommerce(1) is True

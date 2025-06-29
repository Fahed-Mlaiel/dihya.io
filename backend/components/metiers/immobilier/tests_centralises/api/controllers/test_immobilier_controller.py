# immobilier_controller.test.py – Test ultra avancé pour immobilier_controller.py
# (API Immobilier)
from immobilier.api.controllers.immobilier_controller import (
    get_immobilier,
    create_immobilier,
    update_immobilier,
    delete_immobilier,
)


def test_get_immobilier_exists():
    assert callable(get_immobilier)


def test_create_immobilier_exists():
    assert callable(create_immobilier)


def test_update_immobilier_exists():
    assert callable(update_immobilier)


def test_delete_immobilier_exists():
    assert callable(delete_immobilier)


def test_get_immobilier_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_immobilier(1)
    assert result["id"] == 1
    assert result["name"] == "Bien Ultra"
    assert result["status"] == "active"


def test_get_immobilier_not_found():
    # Test edge case : entité non trouvée
    from immobilier.api.controllers.immobilier_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import immobilier.api.controllers.immobilier_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_immobilier(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_immobilier_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_immobilier(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_immobilier_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_immobilier({"status": "active"})
    with pytest.raises(ValueError):
        create_immobilier({"name": "Test"})
    with pytest.raises(ValueError):
        create_immobilier({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_immobilier({"name": "Test", "status": "foo"})


def test_update_immobilier_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_immobilier(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_immobilier_nominal():
    # Test suppression nominale
    assert delete_immobilier(1) is True

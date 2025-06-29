# administration_publique_controller.test.py – Test ultra avancé pour administration_publique_controller.py
# (API administration_publique)
from administration_publique.api.controllers.administration_publique_controller import (
    get_administration_publique,
    create_administration_publique,
    update_administration_publique,
    delete_administration_publique,
)


def test_get_administration_publique_exists():
    assert callable(get_administration_publique)


def test_create_administration_publique_exists():
    assert callable(create_administration_publique)


def test_update_administration_publique_exists():
    assert callable(update_administration_publique)


def test_delete_administration_publique_exists():
    assert callable(delete_administration_publique)


def test_get_administration_publique_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_administration_publique(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_administration_publique_not_found():
    # Test edge case : entité non trouvée
    from administration_publique.api.controllers.administration_publique_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import administration_publique.api.controllers.administration_publique_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_administration_publique(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_administration_publique_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_administration_publique(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_administration_publique_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_administration_publique({"status": "active"})
    with pytest.raises(ValueError):
        create_administration_publique({"name": "Test"})
    with pytest.raises(ValueError):
        create_administration_publique({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_administration_publique({"name": "Test", "status": "foo"})


def test_update_administration_publique_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_administration_publique(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_administration_publique_nominal():
    # Test suppression nominale
    assert delete_administration_publique(1) is True

# services_personne_controller.test.py – Test ultra avancé pour services_personne_controller.py
# (API ServicesPersonne)
from services_personne.api.controllers.services_personne_controller import (
    get_services_personne,
    create_services_personne,
    update_services_personne,
    delete_services_personne,
)


def test_get_services_personne_exists():
    assert callable(get_services_personne)


def test_create_services_personne_exists():
    assert callable(create_services_personne)


def test_update_services_personne_exists():
    assert callable(update_services_personne)


def test_delete_services_personne_exists():
    assert callable(delete_services_personne)


def test_get_services_personne_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_services_personne(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_services_personne_not_found():
    # Test edge case : entité non trouvée
    from services_personne.api.controllers.services_personne_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import services_personne.api.controllers.services_personne_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_services_personne(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_services_personne_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_services_personne(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_services_personne_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_services_personne({"status": "active"})
    with pytest.raises(ValueError):
        create_services_personne({"name": "Test"})
    with pytest.raises(ValueError):
        create_services_personne({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_services_personne({"name": "Test", "status": "foo"})


def test_update_services_personne_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_services_personne(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_services_personne_nominal():
    # Test suppression nominale
    assert delete_services_personne(1) is True

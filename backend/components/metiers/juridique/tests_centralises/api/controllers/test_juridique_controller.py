# juridique_controller.test.py – Test ultra avancé pour juridique_controller.py
# (API Juridique)
from juridique.api.controllers.juridique_controller import (
    get_juridique,
    create_juridique,
    update_juridique,
    delete_juridique,
)


def test_get_juridique_exists():
    assert callable(get_juridique)


def test_create_juridique_exists():
    assert callable(create_juridique)


def test_update_juridique_exists():
    assert callable(update_juridique)


def test_delete_juridique_exists():
    assert callable(delete_juridique)


def test_get_juridique_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_juridique(1)
    assert result["id"] == 1
    assert result["name"] == "Dossier Ultra"
    assert result["status"] == "active"


def test_get_juridique_not_found():
    # Test edge case : entité non trouvée
    from juridique.api.controllers.juridique_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import juridique.api.controllers.juridique_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_juridique(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_juridique_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_juridique(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_juridique_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_juridique({"status": "active"})
    with pytest.raises(ValueError):
        create_juridique({"name": "Test"})
    with pytest.raises(ValueError):
        create_juridique({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_juridique({"name": "Test", "status": "foo"})


def test_update_juridique_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_juridique(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_juridique_nominal():
    # Test suppression nominale
    assert delete_juridique(1) is True

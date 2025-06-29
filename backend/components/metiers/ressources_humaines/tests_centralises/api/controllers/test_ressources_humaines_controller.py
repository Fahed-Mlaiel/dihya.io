# ressources_humaines_controller.test.py – Test ultra avancé pour ressources_humaines_controller.py
# (API Ressources_humaines)
from ressources_humaines.api.controllers.ressources_humaines_controller import (
    get_ressources_humaines,
    create_ressources_humaines,
    update_ressources_humaines,
    delete_ressources_humaines,
)


def test_get_ressources_humaines_exists():
    assert callable(get_ressources_humaines)


def test_create_ressources_humaines_exists():
    assert callable(create_ressources_humaines)


def test_update_ressources_humaines_exists():
    assert callable(update_ressources_humaines)


def test_delete_ressources_humaines_exists():
    assert callable(delete_ressources_humaines)


def test_get_ressources_humaines_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_ressources_humaines(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_ressources_humaines_not_found():
    # Test edge case : entité non trouvée
    from ressources_humaines.api.controllers.ressources_humaines_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import ressources_humaines.api.controllers.ressources_humaines_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_ressources_humaines(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_ressources_humaines_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_ressources_humaines(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_ressources_humaines_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_ressources_humaines({"status": "active"})
    with pytest.raises(ValueError):
        create_ressources_humaines({"name": "Test"})
    with pytest.raises(ValueError):
        create_ressources_humaines({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_ressources_humaines({"name": "Test", "status": "foo"})


def test_update_ressources_humaines_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_ressources_humaines(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_ressources_humaines_nominal():
    # Test suppression nominale
    assert delete_ressources_humaines(1) is True

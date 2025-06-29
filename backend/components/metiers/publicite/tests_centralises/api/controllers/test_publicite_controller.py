# publicite_controller.test.py – Test ultra avancé pour publicite_controller.py
# (API Publicite)
from publicite.api.controllers.publicite_controller import (
    get_publicite,
    create_publicite,
    update_publicite,
    delete_publicite,
)


def test_get_publicite_exists():
    assert callable(get_publicite)


def test_create_publicite_exists():
    assert callable(create_publicite)


def test_update_publicite_exists():
    assert callable(update_publicite)


def test_delete_publicite_exists():
    assert callable(delete_publicite)


def test_get_publicite_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_publicite(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_publicite_not_found():
    # Test edge case : entité non trouvée
    from publicite.api.controllers.publicite_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import publicite.api.controllers.publicite_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_publicite(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_publicite_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_publicite(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_publicite_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_publicite({"status": "active"})
    with pytest.raises(ValueError):
        create_publicite({"name": "Test"})
    with pytest.raises(ValueError):
        create_publicite({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_publicite({"name": "Test", "status": "foo"})


def test_update_publicite_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_publicite(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_publicite_nominal():
    # Test suppression nominale
    assert delete_publicite(1) is True

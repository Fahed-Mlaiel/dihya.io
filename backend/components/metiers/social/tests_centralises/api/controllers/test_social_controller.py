# social_controller.test.py – Test ultra avancé pour social_controller.py
# (API Social)
from social.api.controllers.social_controller import (
    get_social,
    create_social,
    update_social,
    delete_social,
)


def test_get_social_exists():
    assert callable(get_social)


def test_create_social_exists():
    assert callable(create_social)


def test_update_social_exists():
    assert callable(update_social)


def test_delete_social_exists():
    assert callable(delete_social)


def test_get_social_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_social(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_social_not_found():
    # Test edge case : entité non trouvée
    from social.api.controllers.social_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import social.api.controllers.social_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_social(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_social_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_social(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_social_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_social({"status": "active"})
    with pytest.raises(ValueError):
        create_social({"name": "Test"})
    with pytest.raises(ValueError):
        create_social({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_social({"name": "Test", "status": "foo"})


def test_update_social_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_social(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_social_nominal():
    # Test suppression nominale
    assert delete_social(1) is True

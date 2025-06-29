# industrie_controller.test.py – Test ultra avancé pour industrie_controller.py
# (API Industrie)
from industrie.api.controllers.industrie_controller import (
    get_industrie,
    create_industrie,
    update_industrie,
    delete_industrie,
)


def test_get_industrie_exists():
    assert callable(get_industrie)


def test_create_industrie_exists():
    assert callable(create_industrie)


def test_update_industrie_exists():
    assert callable(update_industrie)


def test_delete_industrie_exists():
    assert callable(delete_industrie)


def test_get_industrie_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_industrie(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_industrie_not_found():
    # Test edge case : entité non trouvée
    from industrie.api.controllers.industrie_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import industrie.api.controllers.industrie_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_industrie(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_industrie_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_industrie(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_industrie_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_industrie({"status": "active"})
    with pytest.raises(ValueError):
        create_industrie({"name": "Test"})
    with pytest.raises(ValueError):
        create_industrie({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_industrie({"name": "Test", "status": "foo"})


def test_update_industrie_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_industrie(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_industrie_nominal():
    # Test suppression nominale
    assert delete_industrie(1) is True

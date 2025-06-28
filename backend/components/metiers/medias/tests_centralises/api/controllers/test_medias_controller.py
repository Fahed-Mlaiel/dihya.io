# medias_controller.test.py – Test ultra avancé pour medias_controller.py
# (API Medias)
from medias.api.controllers.medias_controller import (
    get_medias,
    create_medias,
    update_medias,
    delete_medias,
)


def test_get_medias_exists():
    assert callable(get_medias)


def test_create_medias_exists():
    assert callable(create_medias)


def test_update_medias_exists():
    assert callable(update_medias)


def test_delete_medias_exists():
    assert callable(delete_medias)


def test_get_medias_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_medias(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_medias_not_found():
    # Test edge case : entité non trouvée
    from medias.api.controllers.medias_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import medias.api.controllers.medias_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_medias(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_medias_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_medias(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_medias_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_medias({"status": "active"})
    with pytest.raises(ValueError):
        create_medias({"name": "Test"})
    with pytest.raises(ValueError):
        create_medias({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_medias({"name": "Test", "status": "foo"})


def test_update_medias_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_medias(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_medias_nominal():
    # Test suppression nominale
    assert delete_medias(1) is True

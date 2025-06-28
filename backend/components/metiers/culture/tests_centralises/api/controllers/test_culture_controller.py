# culture_controller.test.py – Test ultra avancé pour culture_controller.py
# (API Culture)
from culture.api.controllers.culture_controller import (
    get_culture,
    create_culture,
    update_culture,
    delete_culture,
)


def test_get_culture_exists():
    assert callable(get_culture)


def test_create_culture_exists():
    assert callable(create_culture)


def test_update_culture_exists():
    assert callable(update_culture)


def test_delete_culture_exists():
    assert callable(delete_culture)


def test_get_culture_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_culture(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_culture_not_found():
    # Test edge case : entité non trouvée
    from culture.api.controllers.culture_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import culture.api.controllers.culture_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_culture(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_culture_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_culture(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_culture_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_culture({"status": "active"})
    with pytest.raises(ValueError):
        create_culture({"name": "Test"})
    with pytest.raises(ValueError):
        create_culture({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_culture({"name": "Test", "status": "foo"})


def test_update_culture_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_culture(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_culture_nominal():
    # Test suppression nominale
    assert delete_culture(1) is True

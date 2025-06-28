# assurance_controller.test.py – Test ultra avancé pour assurance_controller.py
# (API Assurance)
from assurance.api.controllers.assurance_controller import (
    get_assurance,
    create_assurance,
    update_assurance,
    delete_assurance,
)


def test_get_assurance_exists():
    assert callable(get_assurance)


def test_create_assurance_exists():
    assert callable(create_assurance)


def test_update_assurance_exists():
    assert callable(update_assurance)


def test_delete_assurance_exists():
    assert callable(delete_assurance)


def test_get_assurance_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_assurance(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_assurance_not_found():
    # Test edge case : entité non trouvée
    from assurance.api.controllers.assurance_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import assurance.api.controllers.assurance_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_assurance(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_assurance_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_assurance(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_assurance_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_assurance({"status": "active"})
    with pytest.raises(ValueError):
        create_assurance({"name": "Test"})
    with pytest.raises(ValueError):
        create_assurance({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_assurance({"name": "Test", "status": "foo"})


def test_update_assurance_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_assurance(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_assurance_nominal():
    # Test suppression nominale
    assert delete_assurance(1) is True

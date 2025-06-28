# science_controller.test.py – Test ultra avancé pour science_controller.py
# (API Science)
from science.api.controllers.science_controller import (
    get_science,
    create_science,
    update_science,
    delete_science,
)


def test_get_science_exists():
    assert callable(get_science)


def test_create_science_exists():
    assert callable(create_science)


def test_update_science_exists():
    assert callable(update_science)


def test_delete_science_exists():
    assert callable(delete_science)


def test_get_science_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_science(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_science_not_found():
    # Test edge case : entité non trouvée
    from science.api.controllers.science_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import science.api.controllers.science_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_science(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_science_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_science(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_science_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_science({"status": "active"})
    with pytest.raises(ValueError):
        create_science({"name": "Test"})
    with pytest.raises(ValueError):
        create_science({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_science({"name": "Test", "status": "foo"})


def test_update_science_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_science(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_science_nominal():
    # Test suppression nominale
    assert delete_science(1) is True

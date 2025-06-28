# education_controller.test.py – Test ultra avancé pour education_controller.py
# (API Education)
from education.api.controllers.education_controller import (
    get_education,
    create_education,
    update_education,
    delete_education,
)


def test_get_education_exists():
    assert callable(get_education)


def test_create_education_exists():
    assert callable(create_education)


def test_update_education_exists():
    assert callable(update_education)


def test_delete_education_exists():
    assert callable(delete_education)


def test_get_education_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_education(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_education_not_found():
    # Test edge case : entité non trouvée
    from education.api.controllers.education_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import education.api.controllers.education_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_education(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_education_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_education(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_education_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_education({"status": "active"})
    with pytest.raises(ValueError):
        create_education({"name": "Test"})
    with pytest.raises(ValueError):
        create_education({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_education({"name": "Test", "status": "foo"})


def test_update_education_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_education(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_education_nominal():
    # Test suppression nominale
    assert delete_education(1) is True

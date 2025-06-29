# seo_controller.test.py – Test ultra avancé pour seo_controller.py
# (API Seo)
from seo.api.controllers.seo_controller import (
    get_seo,
    create_seo,
    update_seo,
    delete_seo,
)


def test_get_seo_exists():
    assert callable(get_seo)


def test_create_seo_exists():
    assert callable(create_seo)


def test_update_seo_exists():
    assert callable(update_seo)


def test_delete_seo_exists():
    assert callable(delete_seo)


def test_get_seo_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_seo(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_seo_not_found():
    # Test edge case : entité non trouvée
    from seo.api.controllers.seo_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import seo.api.controllers.seo_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_seo(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_seo_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_seo(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_seo_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_seo({"status": "active"})
    with pytest.raises(ValueError):
        create_seo({"name": "Test"})
    with pytest.raises(ValueError):
        create_seo({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_seo({"name": "Test", "status": "foo"})


def test_update_seo_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_seo(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_seo_nominal():
    # Test suppression nominale
    assert delete_seo(1) is True

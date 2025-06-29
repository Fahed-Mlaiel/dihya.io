# sante_controller.test.py – Test ultra avancé pour sante_controller.py
# (API Sante)
from sante.api.controllers.sante_controller import (
    get_sante,
    create_sante,
    update_sante,
    delete_sante,
)


def test_get_sante_exists():
    assert callable(get_sante)


def test_create_sante_exists():
    assert callable(create_sante)


def test_update_sante_exists():
    assert callable(update_sante)


def test_delete_sante_exists():
    assert callable(delete_sante)


def test_get_sante_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_sante(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_sante_not_found():
    # Test edge case : entité non trouvée
    from sante.api.controllers.sante_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import sante.api.controllers.sante_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_sante(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_sante_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_sante(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_sante_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_sante({"status": "active"})
    with pytest.raises(ValueError):
        create_sante({"name": "Test"})
    with pytest.raises(ValueError):
        create_sante({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_sante({"name": "Test", "status": "foo"})


def test_update_sante_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_sante(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_sante_nominal():
    # Test suppression nominale
    assert delete_sante(1) is True

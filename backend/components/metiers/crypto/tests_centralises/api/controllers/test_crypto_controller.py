# crypto_controller.test.py – Test ultra avancé pour crypto_controller.py
# (API Crypto)
from crypto.api.controllers.crypto_controller import (
    get_crypto,
    create_crypto,
    update_crypto,
    delete_crypto,
)


def test_get_crypto_exists():
    assert callable(get_crypto)


def test_create_crypto_exists():
    assert callable(create_crypto)


def test_update_crypto_exists():
    assert callable(update_crypto)


def test_delete_crypto_exists():
    assert callable(delete_crypto)


def test_get_crypto_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_crypto(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_crypto_not_found():
    # Test edge case : entité non trouvée
    from crypto.api.controllers.crypto_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import crypto.api.controllers.crypto_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_crypto(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_crypto_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_crypto(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_crypto_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_crypto({"status": "active"})
    with pytest.raises(ValueError):
        create_crypto({"name": "Test"})
    with pytest.raises(ValueError):
        create_crypto({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_crypto({"name": "Test", "status": "foo"})


def test_update_crypto_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_crypto(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_crypto_nominal():
    # Test suppression nominale
    assert delete_crypto(1) is True

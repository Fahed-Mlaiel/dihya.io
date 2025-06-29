# blockchain_controller.test.py – Test ultra avancé pour blockchain_controller.py
# (API Blockchain)
from blockchain.api.controllers.blockchain_controller import (
    get_blockchain,
    create_blockchain,
    update_blockchain,
    delete_blockchain,
)


def test_get_blockchain_exists():
    assert callable(get_blockchain)


def test_create_blockchain_exists():
    assert callable(create_blockchain)


def test_update_blockchain_exists():
    assert callable(update_blockchain)


def test_delete_blockchain_exists():
    assert callable(delete_blockchain)


def test_get_blockchain_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_blockchain(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_blockchain_not_found():
    # Test edge case : entité non trouvée
    from blockchain.api.controllers.blockchain_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import blockchain.api.controllers.blockchain_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_blockchain(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_blockchain_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_blockchain(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_blockchain_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_blockchain({"status": "active"})
    with pytest.raises(ValueError):
        create_blockchain({"name": "Test"})
    with pytest.raises(ValueError):
        create_blockchain({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_blockchain({"name": "Test", "status": "foo"})


def test_update_blockchain_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_blockchain(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_blockchain_nominal():
    # Test suppression nominale
    assert delete_blockchain(1) is True

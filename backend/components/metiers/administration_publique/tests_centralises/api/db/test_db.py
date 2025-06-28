# db.test.py – Tests ultra avancés pour db.py (API administration_publique Python)
from administration_publique.api.db.db import db_find_by_id, db_insert, db_update, db_delete
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../../../../")
    ),
)


def test_db_find_by_id():
    result = db_find_by_id("administration_publique", 1)
    assert isinstance(result, dict)
    assert result["id"] == 1


def test_db_insert():
    data = {"name": "Test", "status": "active"}
    result = db_insert("administration_publique", data)
    assert result["name"] == "Test"
    assert "id" in result


def test_db_update():
    data = {"name": "Test", "status": "active"}
    result = db_update("administration_publique", 1, data)
    assert result["id"] == 1


def test_db_delete():
    assert db_delete("administration_publique", 1) is True

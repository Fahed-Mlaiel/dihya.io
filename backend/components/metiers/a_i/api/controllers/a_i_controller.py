"""
a_i_controller.py – Contrôleur ultra avancé API A_I (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_a_i_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/a_i/{id}")
def get_a_i(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("a_i", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/a_i")
def create_a_i(data: dict):
    before_action("create", data)
    validate_a_i_entity(data)
    created = db_insert("a_i", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/a_i/{id}")
def update_a_i(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_a_i_entity(data)
    updated = db_update("a_i", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/a_i/{id}")
def delete_a_i(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("a_i", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse A_IController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class A_IController:
    @staticmethod
    def get_by_id(id):
        return get_a_i(id)

    @staticmethod
    def create(data):
        return create_a_i(data)

    @staticmethod
    def update(id, data):
        return update_a_i(id, data)

    @staticmethod
    def delete(id):
        return delete_a_i(id)

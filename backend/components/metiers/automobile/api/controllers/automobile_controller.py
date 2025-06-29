"""
automobile_controller.py – Contrôleur ultra avancé API Automobile (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_automobile_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/automobile/{id}")
def get_automobile(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("automobile", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/automobile")
def create_automobile(data: dict):
    before_action("create", data)
    validate_automobile_entity(data)
    created = db_insert("automobile", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/automobile/{id}")
def update_automobile(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_automobile_entity(data)
    updated = db_update("automobile", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/automobile/{id}")
def delete_automobile(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("automobile", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse AutomobileController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class AutomobileController:
    @staticmethod
    def get_by_id(id):
        return get_automobile(id)

    @staticmethod
    def create(data):
        return create_automobile(data)

    @staticmethod
    def update(id, data):
        return update_automobile(id, data)

    @staticmethod
    def delete(id):
        return delete_automobile(id)

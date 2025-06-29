"""
construction_controller.py – Contrôleur ultra avancé API Construction (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_construction_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/construction/{id}")
def get_construction(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("construction", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/construction")
def create_construction(data: dict):
    before_action("create", data)
    validate_construction_entity(data)
    created = db_insert("construction", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/construction/{id}")
def update_construction(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_construction_entity(data)
    updated = db_update("construction", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/construction/{id}")
def delete_construction(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("construction", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse ConstructionController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class ConstructionController:
    @staticmethod
    def get_by_id(id):
        return get_construction(id)

    @staticmethod
    def create(data):
        return create_construction(data)

    @staticmethod
    def update(id, data):
        return update_construction(id, data)

    @staticmethod
    def delete(id):
        return delete_construction(id)

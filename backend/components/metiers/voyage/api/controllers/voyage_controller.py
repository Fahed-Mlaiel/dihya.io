"""
voyage_controller.py – Contrôleur ultra avancé API Voyage (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_voyage_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/voyage/{id}")
def get_voyage(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("voyage", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/voyage")
def create_voyage(data: dict):
    before_action("create", data)
    validate_voyage_entity(data)
    created = db_insert("voyage", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/voyage/{id}")
def update_voyage(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_voyage_entity(data)
    updated = db_update("voyage", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/voyage/{id}")
def delete_voyage(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("voyage", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse VoyageController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class VoyageController:
    @staticmethod
    def get_by_id(id):
        return get_voyage(id)

    @staticmethod
    def create(data):
        return create_voyage(data)

    @staticmethod
    def update(id, data):
        return update_voyage(id, data)

    @staticmethod
    def delete(id):
        return delete_voyage(id)

"""
restauration_controller.py – Contrôleur ultra avancé API RestauratioN (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_restauration_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/restauration/{id}")
def get_restauration(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("restauration", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/restauration")
def create_restauration(data: dict):
    before_action("create", data)
    validate_restauration_entity(data)
    created = db_insert("restauration", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/restauration/{id}")
def update_restauration(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_restauration_entity(data)
    updated = db_update("restauration", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/restauration/{id}")
def delete_restauration(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("restauration", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse RestauratioNController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class RestauratioNController:
    @staticmethod
    def get_by_id(id):
        return get_restauration(id)

    @staticmethod
    def create(data):
        return create_restauration(data)

    @staticmethod
    def update(id, data):
        return update_restauration(id, data)

    @staticmethod
    def delete(id):
        return delete_restauration(id)

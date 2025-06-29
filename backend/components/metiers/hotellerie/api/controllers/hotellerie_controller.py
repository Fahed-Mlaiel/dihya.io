"""
hotellerie_controller.py – Contrôleur ultra avancé API Hotellerie (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_hotellerie_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/hotellerie/{id}")
def get_hotellerie(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("hotellerie", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/hotellerie")
def create_hotellerie(data: dict):
    before_action("create", data)
    validate_hotellerie_entity(data)
    created = db_insert("hotellerie", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/hotellerie/{id}")
def update_hotellerie(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_hotellerie_entity(data)
    updated = db_update("hotellerie", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/hotellerie/{id}")
def delete_hotellerie(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("hotellerie", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse HotellerieController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class HotellerieController:
    @staticmethod
    def get_by_id(id):
        return get_hotellerie(id)

    @staticmethod
    def create(data):
        return create_hotellerie(data)

    @staticmethod
    def update(id, data):
        return update_hotellerie(id, data)

    @staticmethod
    def delete(id):
        return delete_hotellerie(id)

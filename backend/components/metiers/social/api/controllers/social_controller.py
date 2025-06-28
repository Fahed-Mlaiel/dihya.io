"""
social_controller.py – Contrôleur ultra avancé API Social (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_social_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/social/{id}")
def get_social(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("social", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/social")
def create_social(data: dict):
    before_action("create", data)
    validate_social_entity(data)
    created = db_insert("social", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/social/{id}")
def update_social(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_social_entity(data)
    updated = db_update("social", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/social/{id}")
def delete_social(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("social", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse SocialController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class SocialController:
    @staticmethod
    def get_by_id(id):
        return get_social(id)

    @staticmethod
    def create(data):
        return create_social(data)

    @staticmethod
    def update(id, data):
        return update_social(id, data)

    @staticmethod
    def delete(id):
        return delete_social(id)

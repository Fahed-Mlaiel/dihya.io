"""
ressources_humaines_controller.py – Contrôleur ultra avancé API Ressources_humaines (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_ressources_humaines_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/ressources_humaines/{id}")
def get_ressources_humaines(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("ressources_humaines", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/ressources_humaines")
def create_ressources_humaines(data: dict):
    before_action("create", data)
    validate_ressources_humaines_entity(data)
    created = db_insert("ressources_humaines", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/ressources_humaines/{id}")
def update_ressources_humaines(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_ressources_humaines_entity(data)
    updated = db_update("ressources_humaines", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/ressources_humaines/{id}")
def delete_ressources_humaines(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("ressources_humaines", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse Ressources_humainesController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class Ressources_humainesController:
    @staticmethod
    def get_by_id(id):
        return get_ressources_humaines(id)

    @staticmethod
    def create(data):
        return create_ressources_humaines(data)

    @staticmethod
    def update(id, data):
        return update_ressources_humaines(id, data)

    @staticmethod
    def delete(id):
        return delete_ressources_humaines(id)

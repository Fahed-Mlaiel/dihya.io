"""
administration_publique_controller.py – Contrôleur ultra avancé API administration_publique (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_administration_publique_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/administration_publique/{id}")
def get_administration_publique(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("administration_publique", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/administration_publique")
def create_administration_publique(data: dict):
    before_action("create", data)
    validate_administration_publique_entity(data)
    created = db_insert("administration_publique", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/administration_publique/{id}")
def update_administration_publique(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_administration_publique_entity(data)
    updated = db_update("administration_publique", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/administration_publique/{id}")
def delete_administration_publique(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("administration_publique", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse administration_publiqueController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class administration_publiqueController:
    @staticmethod
    def get_by_id(id):
        return get_administration_publique(id)

    @staticmethod
    def create(data):
        return create_administration_publique(data)

    @staticmethod
    def update(id, data):
        return update_administration_publique(id, data)

    @staticmethod
    def delete(id):
        return delete_administration_publique(id)

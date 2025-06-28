"""
services_personne_controller.py – Contrôleur ultra avancé API ServicesPersonne (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_services_personne_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/services_personne/{id}")
def get_services_personne(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("services_personne", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/services_personne")
def create_services_personne(data: dict):
    before_action("create", data)
    validate_services_personne_entity(data)
    created = db_insert("services_personne", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/services_personne/{id}")
def update_services_personne(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_services_personne_entity(data)
    updated = db_update("services_personne", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/services_personne/{id}")
def delete_services_personne(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("services_personne", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse ServicesPersonneController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class ServicesPersonneController:
    @staticmethod
    def get_by_id(id):
        return get_services_personne(id)

    @staticmethod
    def create(data):
        return create_services_personne(data)

    @staticmethod
    def update(id, data):
        return update_services_personne(id, data)

    @staticmethod
    def delete(id):
        return delete_services_personne(id)

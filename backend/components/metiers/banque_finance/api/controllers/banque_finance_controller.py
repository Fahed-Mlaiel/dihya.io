"""
banque_finance_controller.py – Contrôleur ultra avancé API Banque_Finance (Python)
Inclut : logique métier, RGPD, audit, accessibilité, hooks, edge cases
"""

from fastapi import APIRouter
from ..db.db import db_find_by_id, db_insert, db_update, db_delete
from ..validators.validators import validate_banque_finance_entity
from ..audit.audit import audit_entity
from ..rgpd.rgpd import rgpd_sanitize
from ..accessibility.accessibility import check_accessibility
from ..hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/banque_finance/{id}")
def get_banque_finance(id: int):
    before_action("read", {"id": id})
    entity = db_find_by_id("banque_finance", id)
    if not entity:
        return None
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/banque_finance")
def create_banque_finance(data: dict):
    before_action("create", data)
    validate_banque_finance_entity(data)
    created = db_insert("banque_finance", data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/banque_finance/{id}")
def update_banque_finance(id: int, data: dict):
    before_action("update", {"id": id, **data})
    validate_banque_finance_entity(data)
    updated = db_update("banque_finance", id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/banque_finance/{id}")
def delete_banque_finance(id: int):
    before_action("delete", {"id": id})
    deleted = db_delete("banque_finance", id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return deleted


# Es gibt keine Klasse Banque_FinanceController, sondern nur Funktions-Exporte.
# Die API erwartet aber eine Klasse für den Import in core/api.py.
# Wir ergänzen eine Dummy-Klasse, die die Funktionssignaturen als statische
# Methoden bereitstellt.


class Banque_FinanceController:
    @staticmethod
    def get_by_id(id):
        return get_banque_finance(id)

    @staticmethod
    def create(data):
        return create_banque_finance(data)

    @staticmethod
    def update(id, data):
        return update_banque_finance(id, data)

    @staticmethod
    def delete(id):
        return delete_banque_finance(id)

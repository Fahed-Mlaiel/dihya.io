# api.py – Point d’entrée FastAPI ultra avancé pour l’API Banque_Finance (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis banque_finance (le PYTHONPATH est déjà sur
# backend/components/metiers)
from banque_finance.api.controllers.banque_finance_controller import Banque_FinanceController
from banque_finance.api.rgpd.rgpd import rgpd_sanitize
from banque_finance.api.accessibility.accessibility import check_accessibility
from banque_finance.api.audit.audit import audit_entity
from banque_finance.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/banque_finance/{id}")
async def get_banque_finance(id: str):
    before_action("read", {"id": id})
    entity = Banque_FinanceController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/banque_finance")
async def create_banque_finance(data: dict):
    before_action("create", data)
    created = Banque_FinanceController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/banque_finance/{id}")
async def update_banque_finance(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = Banque_FinanceController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/banque_finance/{id}")
async def delete_banque_finance(id: str):
    before_action("delete", {"id": id})
    deleted = Banque_FinanceController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

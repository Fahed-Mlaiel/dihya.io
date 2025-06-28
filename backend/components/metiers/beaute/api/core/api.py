# api.py – Point d’entrée FastAPI ultra avancé pour l’API Beaute (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis beaute (le PYTHONPATH est déjà sur
# backend/components/metiers)
from beaute.api.controllers.beaute_controller import BeauteController
from beaute.api.rgpd.rgpd import rgpd_sanitize
from beaute.api.accessibility.accessibility import check_accessibility
from beaute.api.audit.audit import audit_entity
from beaute.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/beaute/{id}")
async def get_beaute(id: str):
    before_action("read", {"id": id})
    entity = BeauteController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/beaute")
async def create_beaute(data: dict):
    before_action("create", data)
    created = BeauteController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/beaute/{id}")
async def update_beaute(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = BeauteController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/beaute/{id}")
async def delete_beaute(id: str):
    before_action("delete", {"id": id})
    deleted = BeauteController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

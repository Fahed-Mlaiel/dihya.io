# api.py – Point d’entrée FastAPI ultra avancé pour l’API Assurance (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis assurance (le PYTHONPATH est déjà sur
# backend/components/metiers)
from assurance.api.controllers.assurance_controller import AssuranceController
from assurance.api.rgpd.rgpd import rgpd_sanitize
from assurance.api.accessibility.accessibility import check_accessibility
from assurance.api.audit.audit import audit_entity
from assurance.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/assurance/{id}")
async def get_assurance(id: str):
    before_action("read", {"id": id})
    entity = AssuranceController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/assurance")
async def create_assurance(data: dict):
    before_action("create", data)
    created = AssuranceController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/assurance/{id}")
async def update_assurance(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = AssuranceController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/assurance/{id}")
async def delete_assurance(id: str):
    before_action("delete", {"id": id})
    deleted = AssuranceController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

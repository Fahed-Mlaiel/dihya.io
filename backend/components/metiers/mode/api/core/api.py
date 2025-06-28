# api.py – Point d’entrée FastAPI ultra avancé pour l’API Mode (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis mode (le PYTHONPATH est déjà sur
# backend/components/metiers)
from mode.api.controllers.mode_controller import ModeController
from mode.api.rgpd.rgpd import rgpd_sanitize
from mode.api.accessibility.accessibility import check_accessibility
from mode.api.audit.audit import audit_entity
from mode.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/mode/{id}")
async def get_mode(id: str):
    before_action("read", {"id": id})
    entity = ModeController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/mode")
async def create_mode(data: dict):
    before_action("create", data)
    created = ModeController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/mode/{id}")
async def update_mode(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = ModeController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/mode/{id}")
async def delete_mode(id: str):
    before_action("delete", {"id": id})
    deleted = ModeController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

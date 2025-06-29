# api.py – Point d’entrée FastAPI ultra avancé pour l’API Mobile (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis mobile (le PYTHONPATH est déjà sur
# backend/components/metiers)
from mobile.api.controllers.mobile_controller import MobileController
from mobile.api.rgpd.rgpd import rgpd_sanitize
from mobile.api.accessibility.accessibility import check_accessibility
from mobile.api.audit.audit import audit_entity
from mobile.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/mobile/{id}")
async def get_mobile(id: str):
    before_action("read", {"id": id})
    entity = MobileController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/mobile")
async def create_mobile(data: dict):
    before_action("create", data)
    created = MobileController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/mobile/{id}")
async def update_mobile(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = MobileController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/mobile/{id}")
async def delete_mobile(id: str):
    before_action("delete", {"id": id})
    deleted = MobileController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

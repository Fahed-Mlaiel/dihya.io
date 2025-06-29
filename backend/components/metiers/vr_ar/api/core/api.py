# api.py – Point d’entrée FastAPI ultra avancé pour l’API vr_ar (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis vr_ar (le PYTHONPATH est déjà sur
# backend/components/metiers)
from vr_ar.api.controllers.vr_ar_controller import vr_arController
from vr_ar.api.rgpd.rgpd import rgpd_sanitize
from vr_ar.api.accessibility.accessibility import check_accessibility
from vr_ar.api.audit.audit import audit_entity
from vr_ar.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/vr_ar/{id}")
async def get_vr_ar(id: str):
    before_action("read", {"id": id})
    entity = vr_arController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/vr_ar")
async def create_vr_ar(data: dict):
    before_action("create", data)
    created = vr_arController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/vr_ar/{id}")
async def update_vr_ar(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = vr_arController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/vr_ar/{id}")
async def delete_vr_ar(id: str):
    before_action("delete", {"id": id})
    deleted = vr_arController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

# api.py – Point d’entrée FastAPI ultra avancé pour l’API Arts (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis arts (le PYTHONPATH est déjà sur
# backend/components/metiers)
from arts.api.controllers.arts_controller import ArtsController
from arts.api.rgpd.rgpd import rgpd_sanitize
from arts.api.accessibility.accessibility import check_accessibility
from arts.api.audit.audit import audit_entity
from arts.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/arts/{id}")
async def get_arts(id: str):
    before_action("read", {"id": id})
    entity = ArtsController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/arts")
async def create_arts(data: dict):
    before_action("create", data)
    created = ArtsController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/arts/{id}")
async def update_arts(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = ArtsController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/arts/{id}")
async def delete_arts(id: str):
    before_action("delete", {"id": id})
    deleted = ArtsController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

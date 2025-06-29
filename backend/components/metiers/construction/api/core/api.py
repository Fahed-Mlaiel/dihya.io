# api.py – Point d’entrée FastAPI ultra avancé pour l’API Construction (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis construction (le PYTHONPATH est déjà sur
# backend/components/metiers)
from construction.api.controllers.construction_controller import ConstructionController
from construction.api.rgpd.rgpd import rgpd_sanitize
from construction.api.accessibility.accessibility import check_accessibility
from construction.api.audit.audit import audit_entity
from construction.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/construction/{id}")
async def get_construction(id: str):
    before_action("read", {"id": id})
    entity = ConstructionController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/construction")
async def create_construction(data: dict):
    before_action("create", data)
    created = ConstructionController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/construction/{id}")
async def update_construction(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = ConstructionController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/construction/{id}")
async def delete_construction(id: str):
    before_action("delete", {"id": id})
    deleted = ConstructionController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

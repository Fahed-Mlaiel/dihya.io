# api.py – Point d’entrée FastAPI ultra avancé pour l’API Agriculture (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis agriculture (le PYTHONPATH est déjà sur
# backend/components/metiers)
from agriculture.api.controllers.agriculture_controller import AgricultureController
from agriculture.api.rgpd.rgpd import rgpd_sanitize
from agriculture.api.accessibility.accessibility import check_accessibility
from agriculture.api.audit.audit import audit_entity
from agriculture.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/agriculture/{id}")
async def get_agriculture(id: str):
    before_action("read", {"id": id})
    entity = AgricultureController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/agriculture")
async def create_agriculture(data: dict):
    before_action("create", data)
    created = AgricultureController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/agriculture/{id}")
async def update_agriculture(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = AgricultureController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/agriculture/{id}")
async def delete_agriculture(id: str):
    before_action("delete", {"id": id})
    deleted = AgricultureController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

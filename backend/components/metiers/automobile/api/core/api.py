# api.py – Point d’entrée FastAPI ultra avancé pour l’API Automobile (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis automobile (le PYTHONPATH est déjà sur
# backend/components/metiers)
from automobile.api.controllers.automobile_controller import AutomobileController
from automobile.api.rgpd.rgpd import rgpd_sanitize
from automobile.api.accessibility.accessibility import check_accessibility
from automobile.api.audit.audit import audit_entity
from automobile.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/automobile/{id}")
async def get_automobile(id: str):
    before_action("read", {"id": id})
    entity = AutomobileController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/automobile")
async def create_automobile(data: dict):
    before_action("create", data)
    created = AutomobileController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/automobile/{id}")
async def update_automobile(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = AutomobileController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/automobile/{id}")
async def delete_automobile(id: str):
    before_action("delete", {"id": id})
    deleted = AutomobileController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

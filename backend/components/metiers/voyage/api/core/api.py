# api.py – Point d’entrée FastAPI ultra avancé pour l’API Voyage (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis voyage (le PYTHONPATH est déjà sur
# backend/components/metiers)
from voyage.api.controllers.voyage_controller import VoyageController
from voyage.api.rgpd.rgpd import rgpd_sanitize
from voyage.api.accessibility.accessibility import check_accessibility
from voyage.api.audit.audit import audit_entity
from voyage.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/voyage/{id}")
async def get_voyage(id: str):
    before_action("read", {"id": id})
    entity = VoyageController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/voyage")
async def create_voyage(data: dict):
    before_action("create", data)
    created = VoyageController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/voyage/{id}")
async def update_voyage(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = VoyageController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/voyage/{id}")
async def delete_voyage(id: str):
    before_action("delete", {"id": id})
    deleted = VoyageController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

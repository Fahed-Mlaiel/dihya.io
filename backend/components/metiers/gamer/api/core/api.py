# api.py – Point d’entrée FastAPI ultra avancé pour l’API Gamer (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis gamer (le PYTHONPATH est déjà sur
# backend/components/metiers)
from gamer.api.controllers.gamer_controller import GamerController
from gamer.api.rgpd.rgpd import rgpd_sanitize
from gamer.api.accessibility.accessibility import check_accessibility
from gamer.api.audit.audit import audit_entity
from gamer.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/gamer/{id}")
async def get_gamer(id: str):
    before_action("read", {"id": id})
    entity = GamerController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/gamer")
async def create_gamer(data: dict):
    before_action("create", data)
    created = GamerController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/gamer/{id}")
async def update_gamer(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = GamerController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/gamer/{id}")
async def delete_gamer(id: str):
    before_action("delete", {"id": id})
    deleted = GamerController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

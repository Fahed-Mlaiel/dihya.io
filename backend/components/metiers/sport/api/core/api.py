# api.py – Point d’entrée FastAPI ultra avancé pour l’API Sport (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis sport (le PYTHONPATH est déjà sur
# backend/components/metiers)
from sport.api.controllers.sport_controller import SportController
from sport.api.rgpd.rgpd import rgpd_sanitize
from sport.api.accessibility.accessibility import check_accessibility
from sport.api.audit.audit import audit_entity
from sport.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/sport/{id}")
async def get_sport(id: str):
    before_action("read", {"id": id})
    entity = SportController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/sport")
async def create_sport(data: dict):
    before_action("create", data)
    created = SportController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/sport/{id}")
async def update_sport(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = SportController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/sport/{id}")
async def delete_sport(id: str):
    before_action("delete", {"id": id})
    deleted = SportController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

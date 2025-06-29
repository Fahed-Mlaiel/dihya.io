# api.py – Point d’entrée FastAPI ultra avancé pour l’API Industrie (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis industrie (le PYTHONPATH est déjà sur
# backend/components/metiers)
from industrie.api.controllers.industrie_controller import IndustrieController
from industrie.api.rgpd.rgpd import rgpd_sanitize
from industrie.api.accessibility.accessibility import check_accessibility
from industrie.api.audit.audit import audit_entity
from industrie.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/industrie/{id}")
async def get_industrie(id: str):
    before_action("read", {"id": id})
    entity = IndustrieController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/industrie")
async def create_industrie(data: dict):
    before_action("create", data)
    created = IndustrieController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/industrie/{id}")
async def update_industrie(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = IndustrieController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/industrie/{id}")
async def delete_industrie(id: str):
    before_action("delete", {"id": id})
    deleted = IndustrieController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

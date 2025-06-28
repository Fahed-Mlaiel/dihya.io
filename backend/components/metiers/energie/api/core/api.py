# api.py – Point d’entrée FastAPI ultra avancé pour l’API Energie (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis energie (le PYTHONPATH est déjà sur
# backend/components/metiers)
from energie.api.controllers.energie_controller import EnergieController
from energie.api.rgpd.rgpd import rgpd_sanitize
from energie.api.accessibility.accessibility import check_accessibility
from energie.api.audit.audit import audit_entity
from energie.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/energie/{id}")
async def get_energie(id: str):
    before_action("read", {"id": id})
    entity = EnergieController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/energie")
async def create_energie(data: dict):
    before_action("create", data)
    created = EnergieController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/energie/{id}")
async def update_energie(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = EnergieController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/energie/{id}")
async def delete_energie(id: str):
    before_action("delete", {"id": id})
    deleted = EnergieController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

# api.py – Point d’entrée FastAPI ultra avancé pour l’API Environnement (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis environnement (le PYTHONPATH est déjà sur
# backend/components/metiers)
from environnement.api.controllers.environnement_controller import EnvironnementController
from environnement.api.rgpd.rgpd import rgpd_sanitize
from environnement.api.accessibility.accessibility import check_accessibility
from environnement.api.audit.audit import audit_entity
from environnement.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/environnement/{id}")
async def get_environnement(id: str):
    before_action("read", {"id": id})
    entity = EnvironnementController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/environnement")
async def create_environnement(data: dict):
    before_action("create", data)
    created = EnvironnementController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/environnement/{id}")
async def update_environnement(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = EnvironnementController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/environnement/{id}")
async def delete_environnement(id: str):
    before_action("delete", {"id": id})
    deleted = EnvironnementController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

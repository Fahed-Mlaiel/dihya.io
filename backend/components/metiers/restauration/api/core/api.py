# api.py – Point d’entrée FastAPI ultra avancé pour l’API RestauratioN (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis restauration (le PYTHONPATH est déjà sur
# backend/components/metiers)
from restauration.api.controllers.restauration_controller import RestauratioNController
from restauration.api.rgpd.rgpd import rgpd_sanitize
from restauration.api.accessibility.accessibility import check_accessibility
from restauration.api.audit.audit import audit_entity
from restauration.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/restauration/{id}")
async def get_restauration(id: str):
    before_action("read", {"id": id})
    entity = RestauratioNController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/restauration")
async def create_restauration(data: dict):
    before_action("create", data)
    created = RestauratioNController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/restauration/{id}")
async def update_restauration(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = RestauratioNController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/restauration/{id}")
async def delete_restauration(id: str):
    before_action("delete", {"id": id})
    deleted = RestauratioNController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

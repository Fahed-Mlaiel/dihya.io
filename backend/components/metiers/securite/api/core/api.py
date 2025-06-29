# api.py – Point d’entrée FastAPI ultra avancé pour l’API Securite (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis securite (le PYTHONPATH est déjà sur
# backend/components/metiers)
from securite.api.controllers.securite_controller import SecuriteController
from securite.api.rgpd.rgpd import rgpd_sanitize
from securite.api.accessibility.accessibility import check_accessibility
from securite.api.audit.audit import audit_entity
from securite.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/securite/{id}")
async def get_securite(id: str):
    before_action("read", {"id": id})
    entity = SecuriteController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/securite")
async def create_securite(data: dict):
    before_action("create", data)
    created = SecuriteController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/securite/{id}")
async def update_securite(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = SecuriteController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/securite/{id}")
async def delete_securite(id: str):
    before_action("delete", {"id": id})
    deleted = SecuriteController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

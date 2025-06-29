# api.py – Point d’entrée FastAPI ultra avancé pour l’API Publicite (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis publicite (le PYTHONPATH est déjà sur
# backend/components/metiers)
from publicite.api.controllers.publicite_controller import PubliciteController
from publicite.api.rgpd.rgpd import rgpd_sanitize
from publicite.api.accessibility.accessibility import check_accessibility
from publicite.api.audit.audit import audit_entity
from publicite.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/publicite/{id}")
async def get_publicite(id: str):
    before_action("read", {"id": id})
    entity = PubliciteController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/publicite")
async def create_publicite(data: dict):
    before_action("create", data)
    created = PubliciteController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/publicite/{id}")
async def update_publicite(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = PubliciteController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/publicite/{id}")
async def delete_publicite(id: str):
    before_action("delete", {"id": id})
    deleted = PubliciteController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

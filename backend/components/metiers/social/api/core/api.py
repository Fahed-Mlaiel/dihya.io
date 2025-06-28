# api.py – Point d’entrée FastAPI ultra avancé pour l’API Social (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis social (le PYTHONPATH est déjà sur
# backend/components/metiers)
from social.api.controllers.social_controller import SocialController
from social.api.rgpd.rgpd import rgpd_sanitize
from social.api.accessibility.accessibility import check_accessibility
from social.api.audit.audit import audit_entity
from social.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/social/{id}")
async def get_social(id: str):
    before_action("read", {"id": id})
    entity = SocialController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/social")
async def create_social(data: dict):
    before_action("create", data)
    created = SocialController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/social/{id}")
async def update_social(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = SocialController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/social/{id}")
async def delete_social(id: str):
    before_action("delete", {"id": id})
    deleted = SocialController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

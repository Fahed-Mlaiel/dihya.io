# api.py – Point d’entrée FastAPI ultra avancé pour l’API Seo (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis seo (le PYTHONPATH est déjà sur
# backend/components/metiers)
from seo.api.controllers.seo_controller import SeoController
from seo.api.rgpd.rgpd import rgpd_sanitize
from seo.api.accessibility.accessibility import check_accessibility
from seo.api.audit.audit import audit_entity
from seo.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/seo/{id}")
async def get_seo(id: str):
    before_action("read", {"id": id})
    entity = SeoController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/seo")
async def create_seo(data: dict):
    before_action("create", data)
    created = SeoController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/seo/{id}")
async def update_seo(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = SeoController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/seo/{id}")
async def delete_seo(id: str):
    before_action("delete", {"id": id})
    deleted = SeoController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

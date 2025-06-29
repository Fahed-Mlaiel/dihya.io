# api.py – Point d’entrée FastAPI ultra avancé pour l’API Threed (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis threed (le PYTHONPATH est déjà sur
# backend/components/metiers)
from threed.api.controllers.threed_controller import ThreedController
from threed.api.rgpd.rgpd import rgpd_sanitize
from threed.api.accessibility.accessibility import check_accessibility
from threed.api.audit.audit import audit_entity
from threed.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/threed/{id}")
async def get_threed(id: str):
    before_action("read", {"id": id})
    entity = ThreedController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/threed")
async def create_threed(data: dict):
    before_action("create", data)
    created = ThreedController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/threed/{id}")
async def update_threed(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = ThreedController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/threed/{id}")
async def delete_threed(id: str):
    before_action("delete", {"id": id})
    deleted = ThreedController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}


@router.get("/threed/ultra-cube")
async def get_ultra_cube():
    entity = {
        "id": "ultra-cube",
        "label": {"fr": "Cube Ultra", "en": "Ultra Cube"},
        "description": {"fr": "Modèle 3D avancé pour visualisation.", "en": "Advanced 3D model for visualization."},
        "meta": {"created": "2025-06-15", "owner": "threed-team"},
        "access": {"public": True},
        "format": "3d",
        "i18n": True,
        "audit": {"last_access": "2025-06-15T12:00:00Z"},
        "rgpd": {"anonymized": False},
        "geometry": "cube",
        "size": 1,
        "color": "#0077ff"
    }
    return entity

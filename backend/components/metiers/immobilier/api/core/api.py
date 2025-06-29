# api.py – Point d’entrée FastAPI ultra avancé pour l’API Immobilier (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis immobilier (le PYTHONPATH est déjà sur
# backend/components/metiers)
from immobilier.api.controllers.immobilier_controller import ImmobilierController
from immobilier.api.rgpd.rgpd import rgpd_sanitize
from immobilier.api.accessibility.accessibility import check_accessibility
from immobilier.api.audit.audit import audit_entity
from immobilier.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/immobilier/{id}")
async def get_immobilier(id: str):
    before_action("read", {"id": id})
    entity = ImmobilierController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/immobilier")
async def create_immobilier(data: dict):
    before_action("create", data)
    created = ImmobilierController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/immobilier/{id}")
async def update_immobilier(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = ImmobilierController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/immobilier/{id}")
async def delete_immobilier(id: str):
    before_action("delete", {"id": id})
    deleted = ImmobilierController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}


@router.get("/immobilier/ultra-bien")
async def get_ultra_bien():
    entity = {
        "id": "ultra-bien",
        "label": {"fr": "Bien Ultra", "en": "Ultra Bien"},
        "description": {"fr": "Modèle Immobilier avancé pour visualisation.", "en": "Advanced Immobilier model for visualization."},
        "meta": {"created": "2025-06-15", "owner": "immobilier-team"},
        "access": {"public": True},
        "format": "immobilier",
        "i18n": True,
        "audit": {"last_access": "2025-06-15T12:00:00Z"},
        "rgpd": {"anonymized": False},
        "geometry": "bien",
        "size": 1,
        "color": "#0077ff"
    }
    return entity

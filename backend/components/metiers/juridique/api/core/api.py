# api.py – Point d’entrée FastAPI ultra avancé pour l’API Juridique (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis juridique (le PYTHONPATH est déjà sur
# backend/components/metiers)
from juridique.api.controllers.juridique_controller import JuridiqueController
from juridique.api.rgpd.rgpd import rgpd_sanitize
from juridique.api.accessibility.accessibility import check_accessibility
from juridique.api.audit.audit import audit_entity
from juridique.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/juridique/{id}")
async def get_juridique(id: str):
    before_action("read", {"id": id})
    entity = JuridiqueController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/juridique")
async def create_juridique(data: dict):
    before_action("create", data)
    created = JuridiqueController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/juridique/{id}")
async def update_juridique(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = JuridiqueController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/juridique/{id}")
async def delete_juridique(id: str):
    before_action("delete", {"id": id})
    deleted = JuridiqueController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}


@router.get("/juridique/ultra-dossier")
async def get_ultra_dossier():
    entity = {
        "id": "ultra-dossier",
        "label": {"fr": "Dossier Ultra", "en": "Ultra Dossier"},
        "description": {"fr": "Modèle Juridique avancé pour visualisation.", "en": "Advanced Juridique model for visualization."},
        "meta": {"created": "2025-06-15", "owner": "juridique-team"},
        "access": {"public": True},
        "format": "juridique",
        "i18n": True,
        "audit": {"last_access": "2025-06-15T12:00:00Z"},
        "rgpd": {"anonymized": False},
        "geometry": "dossier",
        "size": 1,
        "color": "#0077ff"
    }
    return entity

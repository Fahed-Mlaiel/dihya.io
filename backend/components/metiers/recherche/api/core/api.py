# api.py – Point d’entrée FastAPI ultra avancé pour l’API Recherche (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis recherche (le PYTHONPATH est déjà sur
# backend/components/metiers)
from recherche.api.controllers.recherche_controller import RechercheController
from recherche.api.rgpd.rgpd import rgpd_sanitize
from recherche.api.accessibility.accessibility import check_accessibility
from recherche.api.audit.audit import audit_entity
from recherche.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/recherche/{id}")
async def get_recherche(id: str):
    before_action("read", {"id": id})
    entity = RechercheController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/recherche")
async def create_recherche(data: dict):
    before_action("create", data)
    created = RechercheController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/recherche/{id}")
async def update_recherche(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = RechercheController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/recherche/{id}")
async def delete_recherche(id: str):
    before_action("delete", {"id": id})
    deleted = RechercheController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

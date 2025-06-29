# api.py – Point d’entrée FastAPI ultra avancé pour l’API administration_publique (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis administration_publique (le PYTHONPATH est déjà sur
# backend/components/metiers)
from administration_publique.api.controllers.administration_publique_controller import administration_publiqueController
from administration_publique.api.rgpd.rgpd import rgpd_sanitize
from administration_publique.api.accessibility.accessibility import check_accessibility
from administration_publique.api.audit.audit import audit_entity
from administration_publique.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/administration_publique/{id}")
async def get_administration_publique(id: str):
    before_action("read", {"id": id})
    entity = administration_publiqueController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/administration_publique")
async def create_administration_publique(data: dict):
    before_action("create", data)
    created = administration_publiqueController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/administration_publique/{id}")
async def update_administration_publique(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = administration_publiqueController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/administration_publique/{id}")
async def delete_administration_publique(id: str):
    before_action("delete", {"id": id})
    deleted = administration_publiqueController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

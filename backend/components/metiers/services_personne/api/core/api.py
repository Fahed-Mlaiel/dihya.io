# api.py – Point d’entrée FastAPI ultra avancé pour l’API ServicesPersonne (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis services_personne (le PYTHONPATH est déjà sur
# backend/components/metiers)
from services_personne.api.controllers.services_personne_controller import ServicesPersonneController
from services_personne.api.rgpd.rgpd import rgpd_sanitize
from services_personne.api.accessibility.accessibility import check_accessibility
from services_personne.api.audit.audit import audit_entity
from services_personne.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/services_personne/{id}")
async def get_services_personne(id: str):
    before_action("read", {"id": id})
    entity = ServicesPersonneController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/services_personne")
async def create_services_personne(data: dict):
    before_action("create", data)
    created = ServicesPersonneController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/services_personne/{id}")
async def update_services_personne(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = ServicesPersonneController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/services_personne/{id}")
async def delete_services_personne(id: str):
    before_action("delete", {"id": id})
    deleted = ServicesPersonneController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

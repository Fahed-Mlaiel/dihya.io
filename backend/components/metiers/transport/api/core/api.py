# api.py – Point d’entrée FastAPI ultra avancé pour l’API Transport (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis transport (le PYTHONPATH est déjà sur
# backend/components/metiers)
from transport.api.controllers.transport_controller import TransportController
from transport.api.rgpd.rgpd import rgpd_sanitize
from transport.api.accessibility.accessibility import check_accessibility
from transport.api.audit.audit import audit_entity
from transport.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/transport/{id}")
async def get_transport(id: str):
    before_action("read", {"id": id})
    entity = TransportController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/transport")
async def create_transport(data: dict):
    before_action("create", data)
    created = TransportController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/transport/{id}")
async def update_transport(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = TransportController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/transport/{id}")
async def delete_transport(id: str):
    before_action("delete", {"id": id})
    deleted = TransportController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

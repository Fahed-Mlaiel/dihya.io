# api.py – Point d’entrée FastAPI ultra avancé pour l’API Health (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis health (le PYTHONPATH est déjà sur
# backend/components/metiers)
from health.api.controllers.health_controller import HealthController
from health.api.rgpd.rgpd import rgpd_sanitize
from health.api.accessibility.accessibility import check_accessibility
from health.api.audit.audit import audit_entity
from health.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/health/{id}")
async def get_health(id: str):
    before_action("read", {"id": id})
    entity = HealthController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/health")
async def create_health(data: dict):
    before_action("create", data)
    created = HealthController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/health/{id}")
async def update_health(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = HealthController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/health/{id}")
async def delete_health(id: str):
    before_action("delete", {"id": id})
    deleted = HealthController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

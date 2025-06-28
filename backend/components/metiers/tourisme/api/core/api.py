# api.py – Point d’entrée FastAPI ultra avancé pour l’API Tourisme (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis tourisme (le PYTHONPATH est déjà sur
# backend/components/metiers)
from tourisme.api.controllers.tourisme_controller import TourismeController
from tourisme.api.rgpd.rgpd import rgpd_sanitize
from tourisme.api.accessibility.accessibility import check_accessibility
from tourisme.api.audit.audit import audit_entity
from tourisme.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/tourisme/{id}")
async def get_tourisme(id: str):
    before_action("read", {"id": id})
    entity = TourismeController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/tourisme")
async def create_tourisme(data: dict):
    before_action("create", data)
    created = TourismeController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/tourisme/{id}")
async def update_tourisme(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = TourismeController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/tourisme/{id}")
async def delete_tourisme(id: str):
    before_action("delete", {"id": id})
    deleted = TourismeController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

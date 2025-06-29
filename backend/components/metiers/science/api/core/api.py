# api.py – Point d’entrée FastAPI ultra avancé pour l’API Science (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis science (le PYTHONPATH est déjà sur
# backend/components/metiers)
from science.api.controllers.science_controller import ScienceController
from science.api.rgpd.rgpd import rgpd_sanitize
from science.api.accessibility.accessibility import check_accessibility
from science.api.audit.audit import audit_entity
from science.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/science/{id}")
async def get_science(id: str):
    before_action("read", {"id": id})
    entity = ScienceController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/science")
async def create_science(data: dict):
    before_action("create", data)
    created = ScienceController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/science/{id}")
async def update_science(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = ScienceController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/science/{id}")
async def delete_science(id: str):
    before_action("delete", {"id": id})
    deleted = ScienceController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

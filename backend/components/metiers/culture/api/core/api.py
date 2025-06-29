# api.py – Point d’entrée FastAPI ultra avancé pour l’API Culture (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis culture (le PYTHONPATH est déjà sur
# backend/components/metiers)
from culture.api.controllers.culture_controller import CultureController
from culture.api.rgpd.rgpd import rgpd_sanitize
from culture.api.accessibility.accessibility import check_accessibility
from culture.api.audit.audit import audit_entity
from culture.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/culture/{id}")
async def get_culture(id: str):
    before_action("read", {"id": id})
    entity = CultureController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/culture")
async def create_culture(data: dict):
    before_action("create", data)
    created = CultureController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/culture/{id}")
async def update_culture(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = CultureController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/culture/{id}")
async def delete_culture(id: str):
    before_action("delete", {"id": id})
    deleted = CultureController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

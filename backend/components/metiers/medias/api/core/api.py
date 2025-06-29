# api.py – Point d’entrée FastAPI ultra avancé pour l’API Medias (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis medias (le PYTHONPATH est déjà sur
# backend/components/metiers)
from medias.api.controllers.medias_controller import MediasController
from medias.api.rgpd.rgpd import rgpd_sanitize
from medias.api.accessibility.accessibility import check_accessibility
from medias.api.audit.audit import audit_entity
from medias.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/medias/{id}")
async def get_medias(id: str):
    before_action("read", {"id": id})
    entity = MediasController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/medias")
async def create_medias(data: dict):
    before_action("create", data)
    created = MediasController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/medias/{id}")
async def update_medias(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = MediasController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/medias/{id}")
async def delete_medias(id: str):
    before_action("delete", {"id": id})
    deleted = MediasController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

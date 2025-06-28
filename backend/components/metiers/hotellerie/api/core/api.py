# api.py – Point d’entrée FastAPI ultra avancé pour l’API Hotellerie (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis hotellerie (le PYTHONPATH est déjà sur
# backend/components/metiers)
from hotellerie.api.controllers.hotellerie_controller import HotellerieController
from hotellerie.api.rgpd.rgpd import rgpd_sanitize
from hotellerie.api.accessibility.accessibility import check_accessibility
from hotellerie.api.audit.audit import audit_entity
from hotellerie.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/hotellerie/{id}")
async def get_hotellerie(id: str):
    before_action("read", {"id": id})
    entity = HotellerieController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/hotellerie")
async def create_hotellerie(data: dict):
    before_action("create", data)
    created = HotellerieController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/hotellerie/{id}")
async def update_hotellerie(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = HotellerieController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/hotellerie/{id}")
async def delete_hotellerie(id: str):
    before_action("delete", {"id": id})
    deleted = HotellerieController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

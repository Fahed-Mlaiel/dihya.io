# api.py – Point d’entrée FastAPI ultra avancé pour l’API voice (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis voice (le PYTHONPATH est déjà sur
# backend/components/metiers)
from voice.api.controllers.voice_controller import voiceController
from voice.api.rgpd.rgpd import rgpd_sanitize
from voice.api.accessibility.accessibility import check_accessibility
from voice.api.audit.audit import audit_entity
from voice.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/voice/{id}")
async def get_voice(id: str):
    before_action("read", {"id": id})
    entity = voiceController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/voice")
async def create_voice(data: dict):
    before_action("create", data)
    created = voiceController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/voice/{id}")
async def update_voice(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = voiceController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/voice/{id}")
async def delete_voice(id: str):
    before_action("delete", {"id": id})
    deleted = voiceController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

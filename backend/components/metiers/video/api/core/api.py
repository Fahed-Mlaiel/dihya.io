# api.py – Point d’entrée FastAPI ultra avancé pour l’API Video (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis video (le PYTHONPATH est déjà sur
# backend/components/metiers)
from video.api.controllers.video_controller import VideoController
from video.api.rgpd.rgpd import rgpd_sanitize
from video.api.accessibility.accessibility import check_accessibility
from video.api.audit.audit import audit_entity
from video.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/video/{id}")
async def get_video(id: str):
    before_action("read", {"id": id})
    entity = VideoController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/video")
async def create_video(data: dict):
    before_action("create", data)
    created = VideoController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/video/{id}")
async def update_video(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = VideoController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/video/{id}")
async def delete_video(id: str):
    before_action("delete", {"id": id})
    deleted = VideoController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

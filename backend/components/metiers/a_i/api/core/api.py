# api.py – Point d’entrée FastAPI ultra avancé pour l’API A_I (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis a_i (le PYTHONPATH est déjà sur
# backend/components/metiers)
from a_i.api.controllers.a_i_controller import A_IController
from a_i.api.rgpd.rgpd import rgpd_sanitize
from a_i.api.accessibility.accessibility import check_accessibility
from a_i.api.audit.audit import audit_entity
from a_i.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/a_i/{id}")
async def get_a_i(id: str):
    before_action("read", {"id": id})
    entity = A_IController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/a_i")
async def create_a_i(data: dict):
    before_action("create", data)
    created = A_IController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/a_i/{id}")
async def update_a_i(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = A_IController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/a_i/{id}")
async def delete_a_i(id: str):
    before_action("delete", {"id": id})
    deleted = A_IController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

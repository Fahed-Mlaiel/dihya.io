# api.py – Point d’entrée FastAPI ultra avancé pour l’API Education (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis education (le PYTHONPATH est déjà sur
# backend/components/metiers)
from education.api.controllers.education_controller import EducationController
from education.api.rgpd.rgpd import rgpd_sanitize
from education.api.accessibility.accessibility import check_accessibility
from education.api.audit.audit import audit_entity
from education.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/education/{id}")
async def get_education(id: str):
    before_action("read", {"id": id})
    entity = EducationController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/education")
async def create_education(data: dict):
    before_action("create", data)
    created = EducationController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/education/{id}")
async def update_education(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = EducationController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/education/{id}")
async def delete_education(id: str):
    before_action("delete", {"id": id})
    deleted = EducationController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

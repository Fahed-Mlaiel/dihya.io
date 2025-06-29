# api.py – Point d’entrée FastAPI ultra avancé pour l’API Ecommerce (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis ecommerce (le PYTHONPATH est déjà sur
# backend/components/metiers)
from ecommerce.api.controllers.ecommerce_controller import EcommerceController
from ecommerce.api.rgpd.rgpd import rgpd_sanitize
from ecommerce.api.accessibility.accessibility import check_accessibility
from ecommerce.api.audit.audit import audit_entity
from ecommerce.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/ecommerce/{id}")
async def get_ecommerce(id: str):
    before_action("read", {"id": id})
    entity = EcommerceController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/ecommerce")
async def create_ecommerce(data: dict):
    before_action("create", data)
    created = EcommerceController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/ecommerce/{id}")
async def update_ecommerce(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = EcommerceController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/ecommerce/{id}")
async def delete_ecommerce(id: str):
    before_action("delete", {"id": id})
    deleted = EcommerceController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

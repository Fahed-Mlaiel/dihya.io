# api.py – Point d’entrée FastAPI ultra avancé pour l’API Crypto (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis crypto (le PYTHONPATH est déjà sur
# backend/components/metiers)
from crypto.api.controllers.crypto_controller import CryptoController
from crypto.api.rgpd.rgpd import rgpd_sanitize
from crypto.api.accessibility.accessibility import check_accessibility
from crypto.api.audit.audit import audit_entity
from crypto.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/crypto/{id}")
async def get_crypto(id: str):
    before_action("read", {"id": id})
    entity = CryptoController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/crypto")
async def create_crypto(data: dict):
    before_action("create", data)
    created = CryptoController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/crypto/{id}")
async def update_crypto(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = CryptoController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/crypto/{id}")
async def delete_crypto(id: str):
    before_action("delete", {"id": id})
    deleted = CryptoController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

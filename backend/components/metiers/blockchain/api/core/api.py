# api.py – Point d’entrée FastAPI ultra avancé pour l’API Blockchain (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis blockchain (le PYTHONPATH est déjà sur
# backend/components/metiers)
from blockchain.api.controllers.blockchain_controller import BlockchainController
from blockchain.api.rgpd.rgpd import rgpd_sanitize
from blockchain.api.accessibility.accessibility import check_accessibility
from blockchain.api.audit.audit import audit_entity
from blockchain.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/blockchain/{id}")
async def get_blockchain(id: str):
    before_action("read", {"id": id})
    entity = BlockchainController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/blockchain")
async def create_blockchain(data: dict):
    before_action("create", data)
    created = BlockchainController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/blockchain/{id}")
async def update_blockchain(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = BlockchainController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/blockchain/{id}")
async def delete_blockchain(id: str):
    before_action("delete", {"id": id})
    deleted = BlockchainController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

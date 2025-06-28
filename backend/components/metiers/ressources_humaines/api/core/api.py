# api.py – Point d’entrée FastAPI ultra avancé pour l’API Ressources_humaines (Python)
from fastapi import APIRouter, HTTPException

# Correction : imports directs depuis ressources_humaines (le PYTHONPATH est déjà sur
# backend/components/metiers)
from ressources_humaines.api.controllers.ressources_humaines_controller import Ressources_humainesController
from ressources_humaines.api.rgpd.rgpd import rgpd_sanitize
from ressources_humaines.api.accessibility.accessibility import check_accessibility
from ressources_humaines.api.audit.audit import audit_entity
from ressources_humaines.api.hooks.hooks import before_action, after_action

router = APIRouter()


@router.get("/ressources_humaines/{id}")
async def get_ressources_humaines(id: str):
    before_action("read", {"id": id})
    entity = Ressources_humainesController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail="Not found")
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/ressources_humaines")
async def create_ressources_humaines(data: dict):
    before_action("create", data)
    created = Ressources_humainesController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/ressources_humaines/{id}")
async def update_ressources_humaines(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = Ressources_humainesController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/ressources_humaines/{id}")
async def delete_ressources_humaines(id: str):
    before_action("delete", {"id": id})
    deleted = Ressources_humainesController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

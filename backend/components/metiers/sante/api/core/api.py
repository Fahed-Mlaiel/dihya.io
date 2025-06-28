# api.py – Point d’entrée FastAPI ultra avancé pour l’API Sante (Python)
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Correction : imports directs depuis sante (le PYTHONPATH est déjà sur
# backend/components/metiers)
from sante.api.controllers.sante_controller import SanteController
from sante.api.rgpd.rgpd import rgpd_sanitize
from sante.api.accessibility.accessibility import check_accessibility
from sante.api.audit.audit import audit_entity
from sante.api.hooks.hooks import before_action, after_action

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/sante/token")

# Ajout CORS (à placer dans l'app FastAPI principale)
# app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Exemple d'internationalisation backend
MESSAGES = {
    'fr': {"not_found": "Non trouvé"},
    'en': {"not_found": "Not found"}
}


@router.get("/sante/{id}")
async def get_sante(id: str, lang: str = 'fr', token: str = Depends(oauth2_scheme)):
    before_action("read", {"id": id})
    entity = SanteController.get_by_id(id)
    if not entity:
        return JSONResponse(status_code=404, content={"detail": MESSAGES[lang]["not_found"]})
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, "read")
    after_action("read", entity)
    return entity


@router.post("/sante")
async def create_sante(data: dict):
    before_action("create", data)
    created = SanteController.create(data)
    audit_entity(created, "create")
    after_action("create", created)
    return rgpd_sanitize(created)


@router.put("/sante/{id}")
async def update_sante(id: str, data: dict):
    before_action("update", {"id": id, **data})
    updated = SanteController.update(id, data)
    audit_entity(updated, "update")
    after_action("update", updated)
    return rgpd_sanitize(updated)


@router.delete("/sante/{id}")
async def delete_sante(id: str):
    before_action("delete", {"id": id})
    deleted = SanteController.delete(id)
    audit_entity({"id": id}, "delete")
    after_action("delete", {"id": id})
    return {"deleted": deleted}

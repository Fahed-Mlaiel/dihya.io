"""
Preview API Routes
Gestion avancée des prévisualisations (projets, IA, VR, AR, etc.)
Sécurité, i18n, multitenancy, plugins, RGPD, audit, SEO, IA fallback.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional
from pydantic import BaseModel, Field
from utils.security import get_current_user, require_roles, waf_protect, anti_ddos
from utils.i18n import get_locale
from utils.audit import audit_log
from utils.seo import seo_headers
from utils.ai import ai_fallback
from utils.plugins import plugin_hook
from utils.rgpd import anonymize, export_data
from utils.multitenancy import get_tenant
from utils.graphql import graphql_endpoint
from utils.cors import cors_protect
from utils.jwt import jwt_auth
from utils.validation import validate_payload
from utils.logging import structured_log
from starlette.responses import JSONResponse

class PreviewProject(BaseModel):
    id: str = Field(..., description="ID de la prévisualisation")
    name: str = Field(..., description="Nom de la prévisualisation")
    description: Optional[str] = Field(None, description="Description de la prévisualisation")
    owner: str = Field(..., description="Propriétaire")
    status: str = Field(..., description="Statut de la prévisualisation")
    language: str = Field(..., description="Langue de la prévisualisation")

router = APIRouter(
    prefix="/preview",
    tags=["preview"],
    dependencies=[Depends(cors_protect), Depends(jwt_auth), Depends(waf_protect), Depends(anti_ddos), Depends(get_tenant)]
)

@router.get("/", response_model=List[PreviewProject], summary="Lister les prévisualisations", tags=["preview"])
async def list_previews(request: Request, user=Depends(get_current_user)):
    """Retourne la liste des prévisualisations pour le tenant courant."""
    await audit_log(request, user, action="list_previews")
    structured_log("preview_list", user=user)
    return plugin_hook("preview_list", tenant=get_tenant(request))

@router.post("/", response_model=PreviewProject, summary="Créer une prévisualisation", tags=["preview"])
async def create_preview(payload: PreviewProject, request: Request, user=Depends(require_roles(["admin", "user"]))):
    """Crée une nouvelle prévisualisation."""
    validate_payload(payload)
    await audit_log(request, user, action="create_preview")
    structured_log("preview_create", user=user)
    return plugin_hook("preview_create", data=payload.dict(), tenant=get_tenant(request))

@router.get("/graphql", summary="Endpoint GraphQL preview", tags=["preview"])
async def graphql(request: Request):
    """Endpoint GraphQL pour la gestion des prévisualisations."""
    return await graphql_endpoint(request, schema="preview")

# RGPD, anonymisation, export
@router.get("/export", summary="Exporter les données preview", tags=["preview"])
async def export(request: Request, user=Depends(require_roles(["admin"]))) -> JSONResponse:
    """Export des données preview (RGPD)."""
    data = plugin_hook("preview_export", tenant=get_tenant(request))
    return JSONResponse(content=export_data(data))

@router.post("/anonymize", summary="Anonymiser les données preview", tags=["preview"])
async def anonymize_data(request: Request, user=Depends(require_roles(["admin"]))):
    """Anonymisation RGPD des données preview."""
    plugin_hook("preview_anonymize", tenant=get_tenant(request))
    return {"status": "anonymized"}

# IA fallback
@router.post("/ia/fallback", summary="Fallback IA open source", tags=["preview"])
async def ia_fallback_route(request: Request, user=Depends(get_current_user)):
    """Utilise fallback IA open source (LLaMA, Mixtral, Mistral)."""
    return await ai_fallback(request, context="preview")

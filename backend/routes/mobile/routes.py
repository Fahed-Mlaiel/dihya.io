"""
Mobile API Routes
Gestion avancée des projets mobiles (apps, IA, VR, AR, etc.)
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

class MobileProject(BaseModel):
    id: str = Field(..., description="ID du projet")
    name: str = Field(..., description="Nom du projet")
    description: Optional[str] = Field(None, description="Description du projet")
    owner: str = Field(..., description="Propriétaire")
    status: str = Field(..., description="Statut du projet")
    language: str = Field(..., description="Langue du projet")

router = APIRouter(
    prefix="/mobile",
    tags=["mobile"],
    dependencies=[Depends(cors_protect), Depends(jwt_auth), Depends(waf_protect), Depends(anti_ddos), Depends(get_tenant)]
)

@router.get("/", response_model=List[MobileProject], summary="Lister les projets mobiles", tags=["mobile"])
async def list_projects(request: Request, user=Depends(get_current_user)):
    """Retourne la liste des projets mobiles pour le tenant courant."""
    await audit_log(request, user, action="list_projects")
    structured_log("mobile_list", user=user)
    return plugin_hook("mobile_list", tenant=get_tenant(request))

@router.post("/", response_model=MobileProject, summary="Créer un projet mobile", tags=["mobile"])
async def create_project(payload: MobileProject, request: Request, user=Depends(require_roles(["admin", "user"]))):
    """Crée un nouveau projet mobile."""
    validate_payload(payload)
    await audit_log(request, user, action="create_project")
    structured_log("mobile_create", user=user)
    return plugin_hook("mobile_create", data=payload.dict(), tenant=get_tenant(request))

@router.get("/graphql", summary="Endpoint GraphQL mobile", tags=["mobile"])
async def graphql(request: Request):
    """Endpoint GraphQL pour la gestion des projets mobiles."""
    return await graphql_endpoint(request, schema="mobile")

# RGPD, anonymisation, export
@router.get("/export", summary="Exporter les données mobile", tags=["mobile"])
async def export(request: Request, user=Depends(require_roles(["admin"]))) -> JSONResponse:
    """Export des données mobile (RGPD)."""
    data = plugin_hook("mobile_export", tenant=get_tenant(request))
    return JSONResponse(content=export_data(data))

@router.post("/anonymize", summary="Anonymiser les données mobile", tags=["mobile"])
async def anonymize_data(request: Request, user=Depends(require_roles(["admin"]))):
    """Anonymisation RGPD des données mobile."""
    plugin_hook("mobile_anonymize", tenant=get_tenant(request))
    return {"status": "anonymized"}

# IA fallback
@router.post("/ia/fallback", summary="Fallback IA open source", tags=["mobile"])
async def ia_fallback_route(request: Request, user=Depends(get_current_user)):
    """Utilise fallback IA open source (LLaMA, Mixtral, Mistral)."""
    return await ai_fallback(request, context="mobile")

"""
Routes Services à la personne : aide, assistance, matching IA, plugins, RGPD, audit.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/services_personne", tags=["Services à la personne"])

@router.get("/services", summary="Lister les services", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_services(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les services à la personne (multilingue, plugins, RGPD).
    """
    services = plugin_hook("services_personne_list_services", tenant=tenant, user=user, locale=locale) or []
    return services

@router.post("/demande", summary="Créer une demande", response_model=Dict[str, Any])
@require_role(["user", "admin"])
@waf_protect
@validate_jwt
@audit_log
async def creer_demande(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Crée une demande de service à la personne (validation, plugins, fallback IA).
    """
    demande = plugin_hook("services_personne_creer_demande", data=data, tenant=tenant, user=user, locale=locale)
    if not demande:
        demande = ai_fallback("creer_demande", data)
    return demande

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

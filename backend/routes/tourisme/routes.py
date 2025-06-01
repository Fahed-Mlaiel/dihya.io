"""
Routes Tourisme : sites, réservations, IA, plugins, RGPD, audit.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/tourisme", tags=["Tourisme"])

@router.get("/sites", summary="Lister les sites touristiques", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_sites(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les sites touristiques (multilingue, plugins, RGPD).
    """
    sites = plugin_hook("tourisme_list_sites", tenant=tenant, user=user, locale=locale) or []
    return sites

@router.post("/reservation", summary="Réserver un site touristique", response_model=Dict[str, Any])
@require_role(["user", "admin"])
@waf_protect
@validate_jwt
@audit_log
async def reserver_site(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Réserve un site touristique (validation, plugins, fallback IA).
    """
    reservation = plugin_hook("tourisme_reserver_site", data=data, tenant=tenant, user=user, locale=locale)
    if not reservation:
        reservation = ai_fallback("reserver_site", data)
    return reservation

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

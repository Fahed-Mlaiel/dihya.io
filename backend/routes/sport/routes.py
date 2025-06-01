"""
Routes Sport : activités, réservations, IA, plugins, RGPD, audit.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/sport", tags=["Sport"])

@router.get("/activites", summary="Lister les activités sportives", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_activites(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste toutes les activités sportives (multilingue, plugins, RGPD).
    """
    activites = plugin_hook("sport_list_activites", tenant=tenant, user=user, locale=locale) or []
    return activites

@router.post("/reservation", summary="Réserver une activité sportive", response_model=Dict[str, Any])
@require_role(["user", "admin"])
@waf_protect
@validate_jwt
@audit_log
async def reserver_activite(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Réserve une activité sportive (validation, plugins, fallback IA).
    """
    reservation = plugin_hook("sport_reserver_activite", data=data, tenant=tenant, user=user, locale=locale)
    if not reservation:
        reservation = ai_fallback("reserver_activite", data)
    return reservation

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

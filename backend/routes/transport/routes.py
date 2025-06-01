"""
Routes Transport : trajets, réservations, IA, plugins, RGPD, audit.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/transport", tags=["Transport"])

@router.get("/trajets", summary="Lister les trajets", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_trajets(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les trajets (multilingue, plugins, RGPD).
    """
    trajets = plugin_hook("transport_list_trajets", tenant=tenant, user=user, locale=locale) or []
    return trajets

@router.post("/reservation", summary="Réserver un trajet", response_model=Dict[str, Any])
@require_role(["user", "admin"])
@waf_protect
@validate_jwt
@audit_log
async def reserver_trajet(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Réserve un trajet (validation, plugins, fallback IA).
    """
    reservation = plugin_hook("transport_reserver_trajet", data=data, tenant=tenant, user=user, locale=locale)
    if not reservation:
        reservation = ai_fallback("reserver_trajet", data)
    return reservation

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

"""
Routes Santé : gestion avancée de la santé (dossiers, RDV, alertes, plugins, RGPD, audit, IA).
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/sante", tags=["Santé"])

@router.get("/dossiers", summary="Lister les dossiers santé", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_dossiers(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les dossiers santé du tenant courant (multilingue, plugins, RGPD).
    """
    dossiers = plugin_hook("sante_list_dossiers", tenant=tenant, user=user, locale=locale) or []
    return dossiers

@router.post("/rdv", summary="Prendre un rendez-vous", response_model=Dict[str, Any])
@require_role(["user", "admin"])
@waf_protect
@validate_jwt
@audit_log
async def prendre_rdv(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Prend un rendez-vous santé (validation, plugins, fallback IA).
    """
    rdv = plugin_hook("sante_prendre_rdv", data=data, tenant=tenant, user=user, locale=locale)
    if not rdv:
        rdv = ai_fallback("prendre_rdv", data)
    return rdv

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

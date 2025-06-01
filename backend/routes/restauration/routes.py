"""
Routes Restauration : gestion avancée de la restauration (menus, commandes, allergies, plugins, RGPD, audit, IA).
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/restauration", tags=["Restauration"])

@router.get("/menus", summary="Lister les menus", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_menus(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les menus disponibles (multilingue, plugins, RGPD).
    """
    menus = plugin_hook("restauration_list_menus", tenant=tenant, user=user, locale=locale) or []
    return menus

@router.post("/commande", summary="Passer une commande", response_model=Dict[str, Any])
@require_role(["user", "admin"])
@waf_protect
@validate_jwt
@audit_log
async def passer_commande(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Passe une commande (validation allergies, plugins, fallback IA).
    """
    commande = plugin_hook("restauration_commande", data=data, tenant=tenant, user=user, locale=locale)
    if not commande:
        commande = ai_fallback("passer_commande", data)
    return commande

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

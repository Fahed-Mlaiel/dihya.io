"""
Routes RH : gestion avancée des ressources humaines (multilingue, sécurisé, plugins, RGPD, audit, IA).
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/ressources_humaines", tags=["Ressources Humaines"])

@router.get("/employes", summary="Lister les employés", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_employes(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les employés du tenant courant (multilingue, plugins, RGPD).
    """
    employes = plugin_hook("rh_list_employes", tenant=tenant, user=user, locale=locale) or []
    return employes

@router.post("/employes", summary="Créer un employé", response_model=Dict[str, Any])
@require_role(["admin"])
@waf_protect
@validate_jwt
@audit_log
async def create_employe(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Crée un nouvel employé (validation RGPD, plugins, fallback IA).
    """
    employe = plugin_hook("rh_create_employe", data=data, tenant=tenant, user=user, locale=locale)
    if not employe:
        employe = ai_fallback("create_employe", data)
    return employe

@router.get("/roles", summary="Lister les rôles RH", response_model=List[str])
@waf_protect
@validate_jwt
@audit_log
async def list_roles(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste les rôles RH disponibles (multilingue, plugins).
    """
    roles = plugin_hook("rh_list_roles", tenant=tenant, user=user, locale=locale) or ["admin", "user", "invité"]
    return roles

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

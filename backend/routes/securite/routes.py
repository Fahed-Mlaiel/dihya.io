"""
Routes Sécurité : audit, rôles, logs, WAF, anti-DDOS, RGPD, plugins, IA.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/securite", tags=["Sécurité"])

@router.get("/audit", summary="Logs d’audit", response_model=List[Dict[str, Any]])
@require_role(["admin"])
@waf_protect
@validate_jwt
@audit_log
async def get_audit_logs(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Retourne les logs d’audit (multilingue, plugins, RGPD).
    """
    logs = plugin_hook("securite_get_audit_logs", tenant=tenant, user=user, locale=locale) or []
    return logs

@router.get("/roles", summary="Lister les rôles sécurité", response_model=List[str])
@waf_protect
@validate_jwt
@audit_log
async def list_roles(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste les rôles sécurité disponibles (multilingue, plugins).
    """
    roles = plugin_hook("securite_list_roles", tenant=tenant, user=user, locale=locale) or ["admin", "user", "invité"]
    return roles

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

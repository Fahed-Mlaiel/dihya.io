"""
Routes Social : activités, messages, modération IA, plugins, RGPD, audit.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/social", tags=["Social"])

@router.get("/activites", summary="Lister les activités sociales", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_activites(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste toutes les activités sociales (multilingue, plugins, RGPD).
    """
    activites = plugin_hook("social_list_activites", tenant=tenant, user=user, locale=locale) or []
    return activites

@router.post("/message", summary="Envoyer un message", response_model=Dict[str, Any])
@require_role(["user", "admin"])
@waf_protect
@validate_jwt
@audit_log
async def envoyer_message(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Envoie un message social (validation, plugins, fallback IA).
    """
    message = plugin_hook("social_envoyer_message", data=data, tenant=tenant, user=user, locale=locale)
    if not message:
        message = ai_fallback("envoyer_message", data)
    return message

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

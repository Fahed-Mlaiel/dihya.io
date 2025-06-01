"""
Routes Science : gestion avancée de la science (projets, publications, plugins, RGPD, audit, IA).
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List, Dict, Any
from backend.utils.security import get_current_user, require_role, audit_log, validate_jwt, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.ai import ai_fallback
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/science", tags=["Science"])

@router.get("/projets", summary="Lister les projets scientifiques", response_model=List[Dict[str, Any]])
@waf_protect
@validate_jwt
@audit_log
async def list_projets(request: Request, user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Liste tous les projets scientifiques (multilingue, plugins, RGPD).
    """
    projets = plugin_hook("science_list_projets", tenant=tenant, user=user, locale=locale) or []
    return projets

@router.post("/publication", summary="Publier un article scientifique", response_model=Dict[str, Any])
@require_role(["admin", "user"])
@waf_protect
@validate_jwt
@audit_log
async def publier_article(request: Request, data: Dict[str, Any], user=Depends(get_current_user), tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Publie un article scientifique (validation, plugins, fallback IA).
    """
    article = plugin_hook("science_publier_article", data=data, tenant=tenant, user=user, locale=locale)
    if not article:
        article = ai_fallback("publier_article", data)
    return article

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

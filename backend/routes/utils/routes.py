"""
Routes Utils : validation, logs, i18n, plugins, RGPD, audit.
"""
from fastapi import APIRouter, Depends, Request
from typing import Dict, Any
from backend.utils.security import audit_log, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.validation import validate_data
from backend.utils.logs import get_structured_logs
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/utils", tags=["Utils"])

@router.get("/validate", summary="Validation de données", response_model=Dict[str, Any])
@waf_protect
@audit_log
async def validate(request: Request, tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Valide des données (multilingue, plugins, RGPD).
    """
    data = await request.json() if request.method == "POST" else {}
    result = plugin_hook("utils_validate", data=data, tenant=tenant, locale=locale) or validate_data(data)
    return result

@router.get("/logs", summary="Logs structurés", response_model=Dict[str, Any])
@waf_protect
@audit_log
async def logs(request: Request, tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Retourne les logs structurés (multilingue, plugins, RGPD).
    """
    logs = plugin_hook("utils_logs", tenant=tenant, locale=locale) or get_structured_logs(tenant, locale)
    return logs

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")

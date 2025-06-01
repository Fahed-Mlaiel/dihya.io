"""
Routes marketing pour la gestion avancée des projets IA, VR, AR, etc.
Sécurité, i18n, audit, multitenancy, plugins, RGPD.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import List, Dict, Any
from backend.django.security import get_current_user, require_roles, jwt_auth, waf_protect
from backend.django.i18n import get_locale
from backend.django.audit import audit_log
from backend.django.plugins import plugin_hook
from backend.django.ai import ai_fallback
from backend.django.models import MarketingProject

router = APIRouter(
    prefix="/marketing",
    tags=["marketing"],
    dependencies=[Depends(jwt_auth), Depends(waf_protect)],
)

@router.get("/projects", response_model=List[MarketingProject])
async def list_projects(locale: str = Depends(get_locale), user=Depends(get_current_user)):
    """
    Liste tous les projets marketing (multi-tenant, i18n, audit, plugins).
    """
    audit_log(user, "list_projects", "marketing")
    projects = MarketingProject.objects.filter(tenant=user.tenant)
    return plugin_hook("marketing_list_projects", projects, locale=locale)

@router.post("/projects", response_model=MarketingProject, status_code=status.HTTP_201_CREATED)
async def create_project(data: Dict[str, Any], user=Depends(require_roles(["admin", "marketeur"])), locale: str = Depends(get_locale)):
    """
    Crée un projet marketing (sécurité, audit, plugins, IA fallback).
    """
    audit_log(user, "create_project", "marketing", data)
    try:
        project = MarketingProject.objects.create(**data, tenant=user.tenant)
    except Exception as e:
        suggestion = ai_fallback("marketing_create_error", str(e), locale=locale)
        raise HTTPException(status_code=400, detail={"error": str(e), "suggestion": suggestion})
    return plugin_hook("marketing_create_project", project, locale=locale)

# ... autres routes CRUD, export RGPD, logs, etc. ...

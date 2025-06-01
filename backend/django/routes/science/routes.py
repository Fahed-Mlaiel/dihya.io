"""
Routes science pour la gestion avancée des projets IA, VR, AR, etc.
Sécurité, i18n, audit, multitenancy, plugins, RGPD.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import List, Dict, Any
from backend.django.security import get_current_user, require_roles, jwt_auth, waf_protect
from backend.django.i18n import get_locale
from backend.django.audit import audit_log
from backend.django.plugins import plugin_hook
from backend.django.ai import ai_fallback
from backend.django.models import ScienceProject

router = APIRouter(
    prefix="/science",
    tags=["science"],
    dependencies=[Depends(jwt_auth), Depends(waf_protect)],
)

@router.get("/projects", response_model=List[ScienceProject])
async def list_projects(locale: str = Depends(get_locale), user=Depends(get_current_user)):
    """
    Liste tous les projets science (multi-tenant, i18n, audit, plugins).
    """
    audit_log(user, "list_projects", "science")
    projects = ScienceProject.objects.filter(tenant=user.tenant)
    return plugin_hook("science_list_projects", projects, locale=locale)

@router.post("/projects", response_model=ScienceProject, status_code=status.HTTP_201_CREATED)
async def create_project(data: Dict[str, Any], user=Depends(require_roles(["admin", "scientifique"])), locale: str = Depends(get_locale)):
    """
    Crée un projet science (sécurité, audit, plugins, IA fallback).
    """
    audit_log(user, "create_project", "science", data)
    try:
        project = ScienceProject.objects.create(**data, tenant=user.tenant)
    except Exception as e:
        suggestion = ai_fallback("science_create_error", str(e), locale=locale)
        raise HTTPException(status_code=400, detail={"error": str(e), "suggestion": suggestion})
    return plugin_hook("science_create_project", project, locale=locale)

# ... autres routes CRUD, export RGPD, logs, etc. ...

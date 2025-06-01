"""
Routes loisirs pour la gestion avancée des projets IA, VR, AR, etc.
Sécurité, i18n, audit, multitenancy, plugins, RGPD.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import List, Dict, Any
from backend.django.security import get_current_user, require_roles, jwt_auth, waf_protect
from backend.django.i18n import get_locale
from backend.django.audit import audit_log
from backend.django.plugins import plugin_hook
from backend.django.ai import ai_fallback
from backend.django.models import LoisirsProject

router = APIRouter(
    prefix="/loisirs",
    tags=["loisirs"],
    dependencies=[Depends(jwt_auth), Depends(waf_protect)],
)

@router.get("/projects", response_model=List[LoisirsProject])
async def list_projects(locale: str = Depends(get_locale), user=Depends(get_current_user)):
    """
    Liste tous les projets loisirs (multi-tenant, i18n, audit, plugins).
    """
    audit_log(user, "list_projects", "loisirs")
    projects = LoisirsProject.objects.filter(tenant=user.tenant)
    return plugin_hook("loisirs_list_projects", projects, locale=locale)

@router.post("/projects", response_model=LoisirsProject, status_code=status.HTTP_201_CREATED)
async def create_project(data: Dict[str, Any], user=Depends(require_roles(["admin", "animateur"])), locale: str = Depends(get_locale)):
    """
    Crée un projet loisirs (sécurité, audit, plugins, IA fallback).
    """
    audit_log(user, "create_project", "loisirs", data)
    try:
        project = LoisirsProject.objects.create(**data, tenant=user.tenant)
    except Exception as e:
        suggestion = ai_fallback("loisirs_create_error", str(e), locale=locale)
        raise HTTPException(status_code=400, detail={"error": str(e), "suggestion": suggestion})
    return plugin_hook("loisirs_create_project", project, locale=locale)

# ... autres routes CRUD, export RGPD, logs, etc. ...

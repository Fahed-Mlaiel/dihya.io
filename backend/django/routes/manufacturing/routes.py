"""
Routes manufacturing pour la gestion avancée des projets IA, VR, AR, etc.
Sécurité, i18n, audit, multitenancy, plugins, RGPD.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import List, Dict, Any
from backend.django.security import get_current_user, require_roles, jwt_auth, waf_protect
from backend.django.i18n import get_locale
from backend.django.audit import audit_log
from backend.django.plugins import plugin_hook
from backend.django.ai import ai_fallback
from backend.django.models import ManufacturingProject

router = APIRouter(
    prefix="/manufacturing",
    tags=["manufacturing"],
    dependencies=[Depends(jwt_auth), Depends(waf_protect)],
)

@router.get("/projects", response_model=List[ManufacturingProject])
async def list_projects(locale: str = Depends(get_locale), user=Depends(get_current_user)):
    """
    Liste tous les projets manufacturing (multi-tenant, i18n, audit, plugins).
    """
    audit_log(user, "list_projects", "manufacturing")
    projects = ManufacturingProject.objects.filter(tenant=user.tenant)
    return plugin_hook("manufacturing_list_projects", projects, locale=locale)

@router.post("/projects", response_model=ManufacturingProject, status_code=status.HTTP_201_CREATED)
async def create_project(data: Dict[str, Any], user=Depends(require_roles(["admin", "manufacturier"])), locale: str = Depends(get_locale)):
    """
    Crée un projet manufacturing (sécurité, audit, plugins, IA fallback).
    """
    audit_log(user, "create_project", "manufacturing", data)
    try:
        project = ManufacturingProject.objects.create(**data, tenant=user.tenant)
    except Exception as e:
        suggestion = ai_fallback("manufacturing_create_error", str(e), locale=locale)
        raise HTTPException(status_code=400, detail={"error": str(e), "suggestion": suggestion})
    return plugin_hook("manufacturing_create_project", project, locale=locale)

# ... autres routes CRUD, export RGPD, logs, etc. ...

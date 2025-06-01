"""
Routes de gestion de projets de voyage (IA, VR, AR, etc.)
Sécurité, audit, RGPD, multilingue, plugins IA.
"""

from fastapi import APIRouter, Request, Depends
from pydantic import BaseModel, Field
from typing import List, Dict, Any

from backend.security import get_current_user, check_roles
from backend.i18n import get_locale_message
from backend.audit import log_audit

router = APIRouter(prefix="/voyage", tags=["voyage"])


class VoyageProject(BaseModel):
    id: int = Field(...)
    name: str = Field(..., min_length=3, max_length=128)
    description: str = Field(..., min_length=10, max_length=2048)
    owner: str = Field(...)
    type: str = Field(..., regex="^(IA|VR|AR|Web|Mobile|Script)$")


voyage_db: List[VoyageProject] = []


@router.post(
    "/create",
    summary="Créer un projet de voyage",
    response_model=Dict[str, Any],
)
async def create_voyage_project(
    payload: VoyageProject, request: Request, user=Depends(get_current_user)
):
    """
    Crée un projet de voyage, sécurité, audit, RGPD, multilingue.
    """
    check_roles(user, ["admin", "user"])
    log_audit(user, "create_voyage_project", payload.dict())
    voyage_db.append(payload)
    return {
        "status": "ok",
        "message": get_locale_message(request, "voyage_created", lang=user.lang),
    }


@router.get(
    "/list",
    summary="Lister les projets de voyage",
    response_model=List[VoyageProject],
)
async def list_voyage_projects(request: Request, user=Depends(get_current_user)):
    """
    Liste tous les projets de voyage, sécurité, audit, RGPD, multilingue.
    """
    check_roles(user, ["admin", "user", "invite"])
    log_audit(user, "list_voyage_projects", {})
    return voyage_db

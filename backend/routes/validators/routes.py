"""
Routes de validation pour l’API Dihya (REST/GraphQL)
Sécurité maximale, multilingue, audit, RGPD, plugins, extensible.
"""
from fastapi import APIRouter, Request, HTTPException, status, Depends
from pydantic import BaseModel, Field, ValidationError
from typing import Any, Dict

# Importations fictives pour respecter le cahier des charges
from backend.security import verify_jwt, get_current_user, check_roles
from backend.i18n import get_locale_message
from backend.audit import log_audit

router = APIRouter(prefix="/validators", tags=["validators"])

class ProjectValidationRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=128)
    description: str = Field(..., min_length=10, max_length=2048)
    type: str = Field(..., regex="^(IA|VR|AR|Web|Mobile|Script)$")
    owner_email: str = Field(..., regex=r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$")

@router.post("/project", summary="Valider la création d’un projet", response_model=Dict[str, Any])
async def validate_project_creation(
    payload: ProjectValidationRequest,
    request: Request,
    user=Depends(get_current_user)
):
    """
    Valide la création d’un projet (IA, VR, AR, etc.) avec sécurité, audit, i18n, RGPD.
    """
    try:
        check_roles(user, ["admin", "user"])
        log_audit(user, "validate_project_creation", payload.dict())
        # RGPD: anonymisation partielle de l’email
        anonymized_email = payload.owner_email[:2] + "***@" + payload.owner_email.split("@")[-1]
        return {"status": "ok", "message": get_locale_message(request, "project_valid", lang=user.lang), "anonymized_email": anonymized_email}
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=get_locale_message(request, "validation_error", lang=user.lang))
    except Exception as e:
        raise HTTPException(status_code=500, detail=get_locale_message(request, "internal_error", lang=user.lang))

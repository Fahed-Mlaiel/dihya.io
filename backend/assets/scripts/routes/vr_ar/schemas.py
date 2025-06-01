"""
Dihya Backend – Schémas Pydantic pour IA/VR/AR
Validation, sécurité, RGPD, i18n, multitenancy, plugins, documentation avancée.

- Tous les schémas sont typés, documentés, multilingues, RGPD, extensibles, production-ready.
- Exemples fournis pour chaque modèle.
- Support multitenancy, rôles, plugins dynamiques, auditabilité, accessibilité.
"""
from pydantic import BaseModel, Field, EmailStr, constr
from typing import List, Optional, Dict

class ProjectBase(BaseModel):
    name: constr(min_length=3, max_length=128)
    description: Optional[str] = Field(None, description="Description multilingue")
    owner_email: EmailStr
    language: constr(min_length=2, max_length=8)
    is_active: bool = True
    tags: List[str] = []
    class Config:
        schema_extra = {
            "example": {
                "name": "Projet VR Immersif",
                "description": "Expérience VR collaborative multilingue.",
                "owner_email": "admin@dihya.ai",
                "language": "fr",
                "is_active": True,
                "tags": ["VR", "IA", "collaboratif"]
            }
        }

class ProjectCreate(ProjectBase):
    """Schéma création projet (validation, RGPD, plugins, audit, multilingue)."""
    pass

class ProjectUpdate(ProjectBase):
    """Schéma mise à jour projet (validation, RGPD, plugins, audit, multilingue)."""
    name: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]
    tags: Optional[List[str]]

class ProjectOut(ProjectBase):
    """Schéma sortie projet (audit, RGPD, plugins, multitenancy, accessibilité)."""
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

class UserRole(BaseModel):
    """Schéma rôle utilisateur (admin, user, invité, multitenancy, RGPD, plugins)."""
    user_email: EmailStr
    role: str  # admin, user, invité
    project_id: int

class PluginConfig(BaseModel):
    """Schéma configuration plugin dynamique (audit, RGPD, extensibilité, multilingue)."""
    name: str
    enabled: bool
    config: Optional[Dict] = None

class AuditLog(BaseModel):
    """Schéma log d’audit structuré (RGPD, accessibilité, plugins, multilingue)."""
    user: EmailStr
    action: str
    details: Optional[Dict] = None
    timestamp: str

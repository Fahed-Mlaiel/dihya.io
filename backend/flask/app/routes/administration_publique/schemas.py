"""
Schemas Pydantic/GraphQL pour le module Administration Publique
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class AdminPubliqueProjectSchema(BaseModel):
    """Schéma d'un projet d'administration publique (REST/OpenAPI)."""
    id: Optional[int] = Field(None, description="ID unique du projet")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet")
    description: str = Field(..., description="Description du projet")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class AdminPubliqueProjectListSchema(BaseModel):
    projects: List[AdminPubliqueProjectSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class AdminPubliqueProjectType:
    id: int
    name: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

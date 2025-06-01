"""
Schemas Pydantic/GraphQL pour le module Automobile
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class AutomobileProjectSchema(BaseModel):
    """Schéma d'un projet automobile (REST/OpenAPI)."""
    id: Optional[int] = Field(None, description="ID unique du projet automobile")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet automobile")
    description: str = Field(..., description="Description du projet automobile")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet automobile")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class AutomobileAssetSchema(BaseModel):
    """Schéma d'un asset automobile (REST/OpenAPI)."""
    id: Optional[int] = Field(None, description="ID unique de l'asset automobile")
    project: int = Field(..., description="ID du projet automobile associé")
    file: str = Field(..., description="Chemin ou URL du fichier asset automobile")
    type: str = Field(..., description="Type d’asset (image, doc, 3D, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset automobile")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class AutomobileProjectListSchema(BaseModel):
    projects: List[AutomobileProjectSchema]

class AutomobileAssetListSchema(BaseModel):
    assets: List[AutomobileAssetSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class AutomobileProjectType:
    id: int
    name: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

@strawberry.type
class AutomobileAssetType:
    id: int
    project: int
    file: str
    type: str
    lang: str
    uploaded_at: str

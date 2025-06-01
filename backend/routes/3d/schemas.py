"""
Schemas Pydantic/GraphQL pour le module 3D (Django routes)
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class ThreeDProjectSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du projet 3D")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet 3D")
    description: str = Field(..., description="Description du projet 3D")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet 3D")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class ThreeDAssetSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de l'asset 3D")
    project: int = Field(..., description="ID du projet 3D associé")
    file: str = Field(..., description="Chemin ou URL du fichier asset 3D")
    type: str = Field(..., description="Type d’asset (3D, texture, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset 3D")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class ThreeDProjectListSchema(BaseModel):
    projects: List[ThreeDProjectSchema]

class ThreeDAssetListSchema(BaseModel):
    assets: List[ThreeDAssetSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class ThreeDProjectType:
    id: int
    name: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

@strawberry.type
class ThreeDAssetType:
    id: int
    project: int
    file: str
    type: str
    lang: str
    uploaded_at: str

"""
Schemas Pydantic/GraphQL pour le module Arts
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class ArtProjectSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du projet artistique")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet artistique")
    description: str = Field(..., description="Description du projet artistique")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet artistique")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class ArtAssetSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de l'asset artistique")
    project: int = Field(..., description="ID du projet artistique associé")
    file: str = Field(..., description="Chemin ou URL du fichier asset artistique")
    type: str = Field(..., description="Type d’asset (image, vidéo, 3D, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset artistique")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class ArtProjectListSchema(BaseModel):
    projects: List[ArtProjectSchema]

class ArtAssetListSchema(BaseModel):
    assets: List[ArtAssetSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class ArtProjectType:
    id: int
    name: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

@strawberry.type
class ArtAssetType:
    id: int
    project: int
    file: str
    type: str
    lang: str
    uploaded_at: str

"""
Schemas Pydantic/GraphQL pour le module VR/AR (Django)
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class SceneSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de la scène")
    title: constr(min_length=1, max_length=256) = Field(..., description="Titre de la scène VR/AR")
    description: str = Field(..., description="Description de la scène")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de la scène")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class AssetSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de l'asset")
    scene: int = Field(..., description="ID de la scène associée")
    file: str = Field(..., description="Chemin ou URL du fichier asset (3D, VR, AR)")
    type: str = Field(..., description="Type d’asset (3D, audio, vidéo, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class SceneListSchema(BaseModel):
    scenes: List[SceneSchema]

class AssetListSchema(BaseModel):
    assets: List[AssetSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class SceneType:
    id: int
    title: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

@strawberry.type
class AssetType:
    id: int
    scene: int
    file: str
    type: str
    lang: str
    uploaded_at: str

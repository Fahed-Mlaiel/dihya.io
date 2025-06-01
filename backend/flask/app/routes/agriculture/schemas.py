"""
Schemas Pydantic/GraphQL pour le module Agriculture
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class AgricultureProjectSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du projet agricole")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet agricole")
    description: str = Field(..., description="Description du projet agricole")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet agricole")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class AgricultureAssetSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de l'asset agricole")
    project: int = Field(..., description="ID du projet agricole associé")
    file: str = Field(..., description="Chemin ou URL du fichier asset agricole")
    type: str = Field(..., description="Type d’asset (image, doc, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset agricole")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class AgricultureProjectListSchema(BaseModel):
    projects: List[AgricultureProjectSchema]

class AgricultureAssetListSchema(BaseModel):
    assets: List[AgricultureAssetSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class AgricultureProjectType:
    id: int
    name: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

@strawberry.type
class AgricultureAssetType:
    id: int
    project: int
    file: str
    type: str
    lang: str
    uploaded_at: str

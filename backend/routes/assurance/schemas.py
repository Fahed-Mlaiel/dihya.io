"""
Schemas Pydantic/GraphQL pour le module Assurance (Dihya)
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class AssuranceProjectSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du projet d'assurance")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet d'assurance")
    description: str = Field(..., description="Description du projet")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet")

class AssuranceAssetSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de l'asset")
    project: int = Field(..., description="ID du projet associé")
    file: str = Field(..., description="Chemin ou URL du fichier asset")
    type: str = Field(..., description="Type d’asset (contrat, doc, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class AssuranceProjectListSchema(BaseModel):
    projects: List[AssuranceProjectSchema]

class AssuranceAssetListSchema(BaseModel):
    assets: List[AssuranceAssetSchema]

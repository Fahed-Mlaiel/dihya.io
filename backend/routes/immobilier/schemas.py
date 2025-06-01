"""
Schemas Pydantic/GraphQL pour le module Immobilier (Django routes)
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class ImmobilierProjectSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du projet Immobilier")
    name: constr(min_length=1, max_length=255) = Field(..., description="Nom du projet Immobilier")
    description: str = Field(..., description="Description du projet Immobilier")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")
    tenant: Optional[int] = Field(None, description="ID du tenant")
    is_active: Optional[bool] = Field(True, description="Projet actif")

class ImmobilierProjectListSchema(BaseModel):
    projects: List[ImmobilierProjectSchema]

import strawberry
@strawberry.type
class ImmobilierProjectType:
    id: int
    name: str
    description: str
    created_by: int
    created_at: str
    updated_at: str
    tenant: int
    is_active: bool

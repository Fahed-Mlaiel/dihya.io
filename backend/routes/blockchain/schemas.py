"""
Schemas Pydantic/GraphQL pour le module Blockchain (Django routes)
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class BlockchainProjectSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du projet blockchain")
    name: constr(min_length=1, max_length=256) = Field(..., description="Nom du projet blockchain")
    description: str = Field(..., description="Description du projet blockchain")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du projet blockchain")
    created_by: Optional[int] = Field(None, description="ID du créateur")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class BlockchainAssetSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique de l'asset blockchain")
    project: int = Field(..., description="ID du projet blockchain associé")
    file: str = Field(..., description="Chemin ou URL du fichier asset blockchain")
    type: str = Field(..., description="Type d’asset (smart contract, NFT, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue de l’asset blockchain")
    uploaded_at: Optional[str] = Field(None, description="Date d’upload ISO8601")

class BlockchainProjectListSchema(BaseModel):
    projects: List[BlockchainProjectSchema]

class BlockchainAssetListSchema(BaseModel):
    assets: List[BlockchainAssetSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class BlockchainProjectType:
    id: int
    name: str
    description: str
    lang: str
    created_by: int
    created_at: str
    updated_at: str

@strawberry.type
class BlockchainAssetType:
    id: int
    project: int
    file: str
    type: str
    lang: str
    uploaded_at: str

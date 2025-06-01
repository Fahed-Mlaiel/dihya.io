"""
Schemas Pydantic/GraphQL pour le module Assurance
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class AssuranceContractSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID unique du contrat d'assurance")
    policy_number: str = Field(..., description="Numéro de police d'assurance")
    insured_name: str = Field(..., description="Nom de l'assuré")
    type: str = Field(..., description="Type de contrat (auto, santé, etc.)")
    lang: constr(min_length=2, max_length=16) = Field('fr', description="Langue du contrat")
    created_at: Optional[str] = Field(None, description="Date de création ISO8601")
    updated_at: Optional[str] = Field(None, description="Date de mise à jour ISO8601")

class AssuranceContractListSchema(BaseModel):
    contracts: List[AssuranceContractSchema]

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class AssuranceContractType:
    id: int
    policy_number: str
    insured_name: str
    type: str
    lang: str
    created_at: str
    updated_at: str

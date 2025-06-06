"""
Schemas avancés pour le domaine Environnement
Inclut la validation, la documentation et l'intégration avec les routes API.
"""

from pydantic import BaseModel, Field
from typing import List, Optional

class EnvironnementBase(BaseModel):
    nom: str = Field(..., description="Nom de l'entité environnementale")
    description: Optional[str] = Field(None, description="Description détaillée de l'entité environnementale.")
    type: Optional[str] = Field(None, description="Type d'entité environnementale (ex: zone, ressource, risque)")
    statut: Optional[str] = Field("actif", description="Statut de l'entité (actif, inactif, archivé)")

class EnvironnementCreate(EnvironnementBase):
    pass

class EnvironnementUpdate(EnvironnementBase):
    pass

class EnvironnementInDB(EnvironnementBase):
    id: int

class EnvironnementList(BaseModel):
    environnements: List[EnvironnementInDB]
    total: int = Field(..., description="Nombre total d'entités environnementales")

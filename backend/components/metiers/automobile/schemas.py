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
    date_creation: Optional[str] = Field(None, description="Date de création de l'entité")
    date_modification: Optional[str] = Field(None, description="Date de dernière modification")

class AuditResult(BaseModel):
    id: int
    environnement_id: int
    score: float
    details: str
    recommandations: Optional[str] = Field(None, description="Recommandations issues de l'audit")

class EnvironnementList(BaseModel):
    environnements: List[EnvironnementInDB]
    total: int = Field(..., description="Nombre total d'entités environnementales")

class AutomobileSchema(BaseModel):
    """
    Schéma principal pour le domaine Automobile (conforme à IndustrieSchema).
    """
    id: int
    nom: str
    description: Optional[str] = None
    type: Optional[str] = None
    statut: Optional[str] = "actif"
    date_creation: Optional[str] = None
    date_modification: Optional[str] = None

# Alias pour compatibilité tests et import
AutomobileSchema = AutomobileSchema

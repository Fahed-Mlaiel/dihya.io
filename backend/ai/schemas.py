"""
Dihya Backend AI – Schemas Pydantic/GraphQL pour API IA
Ultra avancé, multilingue, sécurisé, compatible REST & GraphQL, RGPD-ready.
"""
from typing import Optional, List
from pydantic import BaseModel, Field, constr

class AIRequestSchema(BaseModel):
    prompt: constr(min_length=1, max_length=4096) = Field(..., description="Prompt utilisateur (multilingue)")
    lang: Optional[str] = Field('fr', description="Langue cible (fr, en, ar, tzr, etc.)")
    model: Optional[str] = Field('ollama', description="Moteur IA (ollama, mixtral, llama)")

class AIResponseSchema(BaseModel):
    result: str = Field(..., description="Réponse générée par l'IA")
    lang: str = Field(..., description="Langue de la réponse")
    model: str = Field(..., description="Moteur IA utilisé")
    signature: str = Field(..., description="Signature HMAC pour auditabilité")
    timestamp: str = Field(..., description="Horodatage ISO8601")
    error: Optional[str] = Field(None, description="Erreur éventuelle")

# Pour GraphQL (exemple avec Strawberry)
import strawberry
@strawberry.type
class AIResponseType:
    result: str
    lang: str
    model: str
    signature: str
    timestamp: str
    error: Optional[str]

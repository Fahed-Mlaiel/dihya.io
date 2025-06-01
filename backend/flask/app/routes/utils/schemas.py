"""
Schémas de données utilitaires (Pydantic/Marshmallow ready).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class UUIDSchema(Schema):
    uuid = fields.UUID(required=True, description="Identifiant unique universel")

class SanitizedInputSchema(Schema):
    data = fields.String(required=True, description="Entrée utilisateur nettoyée")

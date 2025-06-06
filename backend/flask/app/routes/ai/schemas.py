"""
Schémas de données pour le module AI (Marshmallow).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class AISchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, metadata={"description": "Nom du modèle ou service AI"})
    type = fields.Str(required=True, metadata={"description": "Type d'IA (NLP, Vision, etc.)"})
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

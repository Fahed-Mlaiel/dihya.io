"""
Schémas de données pour le module Transport (Marshmallow).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class TransportSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, metadata={"description": "Nom du transport"})
    capacity = fields.Int(required=False, metadata={"description": "Capacité du transport"})
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

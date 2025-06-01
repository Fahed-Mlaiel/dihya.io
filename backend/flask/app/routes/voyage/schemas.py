"""
Schémas de données pour le module Voyage (Marshmallow).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class VoyageSchema(Schema):
    id = fields.Int(dump_only=True)
    destination = fields.Str(required=True, description="Destination du voyage")
    date = fields.Str(required=False, description="Date du voyage (ISO)")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

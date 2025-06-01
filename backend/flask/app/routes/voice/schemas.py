"""
Schémas de données pour le module Voice (Marshmallow).
Sécurité, RGPD, extensibilité, production-ready.
"""

from marshmallow import Schema, fields

class VoiceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, description="Nom de la ressource vocale")
    lang = fields.Str(required=False, description="Langue de la voix")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

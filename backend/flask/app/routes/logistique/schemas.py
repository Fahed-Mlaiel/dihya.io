"""
Schemas pour le module Logistique (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class LogistiqueBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    reference = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    type = fields.Str()
    statut = fields.Str(validate=validate.OneOf(['en_cours', 'livre', 'retour', 'annule']))
    date_envoi = fields.DateTime()
    actif = fields.Bool(default=True)

class LogistiqueCreateSchema(LogistiqueBaseSchema):
    pass

class LogistiqueUpdateSchema(LogistiqueBaseSchema):
    pass

"""
Schemas pour le module Immobilier (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class ImmobilierBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    titre = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    description = fields.Str()
    prix = fields.Float(required=True)
    adresse = fields.Str()
    date_publication = fields.DateTime(dump_only=True)
    actif = fields.Bool(default=True)

class ImmobilierCreateSchema(ImmobilierBaseSchema):
    pass

class ImmobilierUpdateSchema(ImmobilierBaseSchema):
    pass

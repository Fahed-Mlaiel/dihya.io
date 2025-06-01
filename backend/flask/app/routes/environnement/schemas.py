"""
Schemas pour le module Environnement (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class EnvironnementBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    description = fields.Str()
    date_creation = fields.DateTime(dump_only=True)
    actif = fields.Bool(default=True)

class EnvironnementCreateSchema(EnvironnementBaseSchema):
    pass

class EnvironnementUpdateSchema(EnvironnementBaseSchema):
    pass

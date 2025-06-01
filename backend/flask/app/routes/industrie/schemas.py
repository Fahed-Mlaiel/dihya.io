"""
Schemas pour le module Industrie (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class IndustrieBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    secteur = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    description = fields.Str()
    chiffre_affaires = fields.Float()
    date_creation = fields.DateTime(dump_only=True)
    actif = fields.Bool(default=True)

class IndustrieCreateSchema(IndustrieBaseSchema):
    pass

class IndustrieUpdateSchema(IndustrieBaseSchema):
    pass

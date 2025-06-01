"""
Schemas pour le module Gamer (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class GamerBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    pseudo = fields.Str(required=True, validate=validate.Length(min=2, max=64))
    email = fields.Email(required=True)
    score = fields.Int()
    date_inscription = fields.DateTime(dump_only=True)
    actif = fields.Bool(default=True)

class GamerCreateSchema(GamerBaseSchema):
    pass

class GamerUpdateSchema(GamerBaseSchema):
    pass

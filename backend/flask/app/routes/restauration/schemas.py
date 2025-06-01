"""
Schemas pour le module Restauration (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class RestaurationBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    type = fields.Str()
    adresse = fields.Str()
    date_ouverture = fields.DateTime()
    actif = fields.Bool(default=True)
class RestaurationCreateSchema(RestaurationBaseSchema):
    pass
class RestaurationUpdateSchema(RestaurationBaseSchema):
    pass

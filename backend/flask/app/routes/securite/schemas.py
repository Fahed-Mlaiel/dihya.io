"""
Schemas pour le module Securite (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class SecuriteBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    niveau = fields.Str()
    description = fields.Str()
    date_ajout = fields.DateTime(dump_only=True)
    actif = fields.Bool(default=True)
class SecuriteCreateSchema(SecuriteBaseSchema):
    pass
class SecuriteUpdateSchema(SecuriteBaseSchema):
    pass

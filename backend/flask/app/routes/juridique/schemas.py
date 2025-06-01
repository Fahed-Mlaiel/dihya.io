"""
Schemas pour le module Juridique (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class JuridiqueBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    titre = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    reference = fields.Str()
    date_publication = fields.DateTime()
    actif = fields.Bool(default=True)

class JuridiqueCreateSchema(JuridiqueBaseSchema):
    pass

class JuridiqueUpdateSchema(JuridiqueBaseSchema):
    pass

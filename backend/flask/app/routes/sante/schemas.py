"""
Schemas pour le module Sante (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class SanteBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    patient = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    diagnostic = fields.Str()
    date_consultation = fields.DateTime()
    actif = fields.Bool(default=True)
class SanteCreateSchema(SanteBaseSchema):
    pass
class SanteUpdateSchema(SanteBaseSchema):
    pass

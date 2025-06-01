"""
Schemas pour le module Health (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class HealthBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    patient = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    diagnostic = fields.Str()
    date_consultation = fields.DateTime()
    actif = fields.Bool(default=True)

class HealthCreateSchema(HealthBaseSchema):
    pass

class HealthUpdateSchema(HealthBaseSchema):
    pass

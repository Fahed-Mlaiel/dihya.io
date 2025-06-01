"""
Schemas pour le module IT DevOps (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class ITDevOpsBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    projet = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    pipeline = fields.Str()
    status = fields.Str(validate=validate.OneOf(['active', 'inactive', 'failed', 'success']))
    date_deploiement = fields.DateTime()
    actif = fields.Bool(default=True)

class ITDevOpsCreateSchema(ITDevOpsBaseSchema):
    pass

class ITDevOpsUpdateSchema(ITDevOpsBaseSchema):
    pass

"""
Schemas pour le module Mobile (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class MobileBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    os = fields.Str()
    version = fields.Str()
    date_release = fields.DateTime()
    actif = fields.Bool(default=True)
class MobileCreateSchema(MobileBaseSchema):
    pass
class MobileUpdateSchema(MobileBaseSchema):
    pass

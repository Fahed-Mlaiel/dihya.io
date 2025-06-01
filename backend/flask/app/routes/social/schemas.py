"""
Schemas pour le module Social (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class SocialBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    type = fields.Str()
    description = fields.Str()
    date_ajout = fields.DateTime(dump_only=True)
    actif = fields.Bool(default=True)
class SocialCreateSchema(SocialBaseSchema):
    pass
class SocialUpdateSchema(SocialBaseSchema):
    pass

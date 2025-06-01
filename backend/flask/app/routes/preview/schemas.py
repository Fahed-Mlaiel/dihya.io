"""
Schemas pour le module Preview (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class PreviewBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    url = fields.Url()
    type = fields.Str()
    date_ajout = fields.DateTime(dump_only=True)
    actif = fields.Bool(default=True)
class PreviewCreateSchema(PreviewBaseSchema):
    pass
class PreviewUpdateSchema(PreviewBaseSchema):
    pass

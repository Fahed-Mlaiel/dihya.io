"""
Schemas pour le module Medias (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class MediasBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    titre = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    url = fields.Url(required=True)
    type = fields.Str()
    date_publication = fields.DateTime()
    actif = fields.Bool(default=True)
class MediasCreateSchema(MediasBaseSchema):
    pass
class MediasUpdateSchema(MediasBaseSchema):
    pass

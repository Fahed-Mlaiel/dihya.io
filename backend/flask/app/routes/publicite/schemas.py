"""
Schemas pour le module Publicité (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class PubliciteBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    titre = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    canal = fields.Str()
    budget = fields.Float()
    date_lancement = fields.DateTime()
    actif = fields.Bool(default=True)
class PubliciteCreateSchema(PubliciteBaseSchema):
    pass
class PubliciteUpdateSchema(PubliciteBaseSchema):
    pass

"""
Schemas pour le module Journalisme (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class JournalismeBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    titre = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    contenu = fields.Str()
    auteur = fields.Str()
    date_publication = fields.DateTime()
    actif = fields.Bool(default=True)

class JournalismeCreateSchema(JournalismeBaseSchema):
    pass

class JournalismeUpdateSchema(JournalismeBaseSchema):
    pass

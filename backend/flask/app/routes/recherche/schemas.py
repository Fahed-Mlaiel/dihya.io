"""
Schemas pour le module Recherche (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate
class RechercheBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    sujet = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    description = fields.Str()
    date_debut = fields.DateTime()
    actif = fields.Bool(default=True)
class RechercheCreateSchema(RechercheBaseSchema):
    pass
class RechercheUpdateSchema(RechercheBaseSchema):
    pass

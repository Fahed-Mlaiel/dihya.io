"""
Schemas pour le module Hotellerie (validation, sérialisation, RGPD, sécurité)
"""
from marshmallow import Schema, fields, validate

class HotellerieBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    nom = fields.Str(required=True, validate=validate.Length(min=2, max=128))
    adresse = fields.Str()
    etoiles = fields.Int(validate=validate.Range(min=1, max=5))
    date_ouverture = fields.DateTime()
    actif = fields.Bool(default=True)

class HotellerieCreateSchema(HotellerieBaseSchema):
    pass

class HotellerieUpdateSchema(HotellerieBaseSchema):
    pass
